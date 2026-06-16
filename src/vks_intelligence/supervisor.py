"""Supervisor — bộ não điều phối một task production.

Trách nhiệm: phân loại task → lập TaskPlan → chọn specialist → cấp budget →
chạy (song song) → synthesis từ claim đã validate → quality check → quyết định
publish/approval. Huỷ agent quá hạn và sinh partial result nếu đủ evidence.

Không trực tiếp scrape, format Telegram, ghi file, hay gọi model — uỷ thác cho
tools, tầng llm, và task_runner.
"""

from __future__ import annotations

import logging
import time
from datetime import datetime, timezone
from pathlib import Path

from vks_intelligence.contracts import (
    AgentTask,
    BudgetPolicy,
    RunMetadata,
    TaskPlan,
    TaskRequest,
    TaskStatus,
    TaskType,
)
from vks_intelligence.llm.budgets import budget_for
from vks_intelligence.llm.router import ModelRouter
from vks_intelligence.run_context import RunContext

log = logging.getLogger(__name__)

# ──────────────────────────────────────────────────────────────────
# Routing matrix: task_type → agents (critical=True nghĩa là fail → run fail)
# ──────────────────────────────────────────────────────────────────
_PLAN_MAP: dict[TaskType, list[tuple[str, bool]]] = {
    TaskType.QA: [
        ("qa_agent", True),
    ],
    TaskType.DAILY_INTELLIGENCE: [
        ("daily_intelligence_agent", True),
        ("competitor_agent", False),
    ],
    TaskType.WEEKLY_DIGEST: [
        ("market_trend_agent", True),
        ("competitor_agent", True),
        ("pricing_agent", False),
        ("regulatory_agent", False),
        ("positioning_agent", False),
    ],
    TaskType.COMPETITOR_MONITOR: [
        ("competitor_agent", True),
        ("regulatory_agent", False),
        ("pricing_agent", False),
    ],
    TaskType.PRICING_ANALYSIS: [
        ("pricing_agent", True),
        ("competitor_agent", False),
    ],
    TaskType.BATTLECARD: [
        ("regulatory_agent", False),
        ("competitor_agent", True),
        ("pricing_agent", False),
        ("battlecard_agent", True),
    ],
    TaskType.MEMORY_MAINTENANCE: [
        ("memory_curator_agent", True),
        ("quality_critic_agent", False),
    ],
    TaskType.MONTHLY_BRIEF: [
        ("market_trend_agent", True),
        ("competitor_agent", True),
        ("pricing_agent", False),
        ("regulatory_agent", False),
        ("positioning_agent", False),
    ],
}


class Supervisor:
    def __init__(self) -> None:
        # Đảm bảo registry đã boot trước khi Supervisor được dùng
        import vks_intelligence.specialists  # noqa: F401 — side-effect import
        self._router = ModelRouter()

    # ------------------------------------------------------------------
    # Build plan
    # ------------------------------------------------------------------
    def build_plan(self, request: TaskRequest) -> TaskPlan:
        """Phân loại task và sinh danh sách AgentTask kèm cờ critical."""
        agent_specs = _PLAN_MAP.get(request.task_type, [])
        rid = request.request_id

        agent_tasks = [
            AgentTask(
                agent=agent_name,
                task_id=f"{rid}_{agent_name}",
                instruction=_instruction_for(request, agent_name),
                inputs=_inputs_for(request, agent_name),
                critical=critical,
            )
            for agent_name, critical in agent_specs
        ]

        parallel = request.task_type not in (TaskType.QA, TaskType.BATTLECARD)
        return TaskPlan(
            task_id=rid,
            task_type=request.task_type,
            agent_tasks=agent_tasks,
            parallel=parallel,
        )

    # ------------------------------------------------------------------
    # Main run lifecycle
    # ------------------------------------------------------------------
    def run(self, request: TaskRequest) -> RunMetadata:
        """Chạy trọn vòng đời task và trả RunMetadata + đường dẫn artifact."""
        from vks_intelligence.config import get_settings
        from vks_intelligence.quality import validate_output
        from vks_intelligence.synthesis import synthesize
        from vks_intelligence.task_runner import run_agents
        from vks_intelligence.task_store import TaskStore

        s = get_settings()
        wb = budget_for(request.task_type)
        run_id = _make_run_id(request)
        budget = _budget_policy_for(request, wb)

        context = RunContext(
            request=request,
            run_id=run_id,
            budget=budget,
            started_monotonic=time.monotonic(),
        )

        artifact_root = s.workspace_path / s.artifact_root
        store = TaskStore(run_id, artifact_root)
        store.init_run(request)

        metadata = RunMetadata(
            task_id=request.request_id,
            run_id=run_id,
            task_type=request.task_type,
            status=TaskStatus.RUNNING,
            trigger_source=request.source,
            started_at=datetime.now(timezone.utc).isoformat(),
        )

        try:
            # 1. Collect evidence nếu task cần dữ liệu mới
            evidence = _collect_evidence(request, s.workspace_path)
            if evidence:
                store.save_evidence(evidence)

            # 2. Build & save plan
            plan = self.build_plan(request)
            if evidence:
                for t in plan.agent_tasks:
                    t.inputs["evidence_bundle"] = evidence.model_dump()
                    t.inputs["memory_context"] = evidence.memory_context
                metadata.warnings.extend(evidence.warnings)
            store.save_plan(plan)

            # 3. Run agents
            results = run_agents(plan.agent_tasks, context, self._router)
            for r in results:
                store.save_agent_result(r)

            metadata.agents = [r.agent for r in results]
            metadata.models = {r.agent: r.model_used for r in results if r.model_used}
            metadata.source_count = sum(len(r.claims) for r in results)

            # 4. Check critical failures
            critical_names = {t.agent for t in plan.agent_tasks if t.critical}
            failed_critical = [
                r for r in results
                if r.agent in critical_names and r.status.value == "failed"
            ]
            if failed_critical and not _allows_partial(request.task_type, results):
                raise RuntimeError(
                    f"Critical agent(s) failed: {[r.agent for r in failed_critical]}"
                )

            # 5. Synthesize + revise loop (max 1 lần khi verdict == REVISE)
            from vks_intelligence.contracts import QualityVerdict
            revise_count = 0
            revise_hint: list[str] | None = None
            while True:
                synthesis_md = synthesize(
                    request.task_type,
                    results,
                    evidence_warnings=evidence.warnings if evidence else None,
                    revise_hint=revise_hint,
                )
                quality = validate_output(synthesis_md, request.task_type)
                if quality.verdict != QualityVerdict.REVISE or revise_count >= 1:
                    break
                revise_count += 1
                revise_hint = quality.failures
                log.info(
                    "Revise attempt %d for run %s — failures: %s",
                    revise_count, run_id, quality.failures,
                )

            # 5b. Citation grader (optional, chạy một lần trên synthesis cuối)
            if s.citation_grader_enabled:
                from vks_intelligence.tools.citation_grader import grade_citations
                dead_links = grade_citations(synthesis_md)
                if dead_links:
                    metadata.warnings.append(
                        f"Citation grader: {len(dead_links)} link chết — {dead_links[:3]}"
                    )

            store.save_synthesis(synthesis_md)

            # 6. Quality gate result
            store.save_quality(quality)
            metadata.quality_score = quality.score
            metadata.warnings.extend(quality.failures + quality.warnings)
            if revise_count:
                metadata.warnings.append(f"Revise loop: {revise_count} lần thử lại")

            # 7. Publish / approval decision
            published, approval_required = self._decide_publish(
                request, quality, context, revise_count=revise_count
            )
            metadata.published = published and not request.dry_run
            metadata.approval_required = approval_required

            # 8. Save final
            store.save_final(synthesis_md)

            # 8b. Auto-persist battlecard vào memory khi qua quality gate
            if (
                request.task_type == TaskType.BATTLECARD
                and quality.passed
                and not request.dry_run
            ):
                _persist_battlecard(request, synthesis_md, metadata)

            metadata.status = (
                TaskStatus.COMPLETED if quality.passed
                else TaskStatus.NEEDS_REVIEW if approval_required
                else TaskStatus.BLOCKED
            )

        except Exception as exc:
            log.error("Supervisor run %s failed: %s", run_id, exc, exc_info=True)
            store.save_error({"error": str(exc), "type": type(exc).__name__})
            metadata.status = TaskStatus.FAILED
            metadata.warnings.append(f"Run failed: {exc}")

        finally:
            metadata.finished_at = datetime.now(timezone.utc).isoformat()
            metadata.input_tokens = context.input_tokens
            metadata.output_tokens = context.output_tokens
            metadata.fallbacks = context.fallbacks
            store.save_metadata(metadata)

        return metadata

    def _decide_publish(
        self,
        request: TaskRequest,
        quality,
        context: RunContext,
        *,
        revise_count: int = 0,
    ) -> tuple[bool, bool]:
        """Áp publish/approval policy; trả (published, approval_required)."""
        from vks_intelligence.contracts import QualityVerdict

        if request.dry_run:
            return False, False

        verdict = quality.verdict

        if verdict == QualityVerdict.PASS and not request.human_approval_required:
            return True, False
        if verdict == QualityVerdict.PASS and request.human_approval_required:
            return False, True
        if verdict == QualityVerdict.NEEDS_REVIEW:
            return False, True
        if verdict == QualityVerdict.REVISE:
            # Sau revise loop: escalate lên needs_review thay vì silent block
            return False, revise_count > 0
        # BLOCKED
        return False, False


# ──────────────────────────────────────────────────────────────────
# Helpers
# ──────────────────────────────────────────────────────────────────

def _persist_battlecard(request: TaskRequest, content: str, metadata: RunMetadata) -> None:
    """Ghi battlecard đã qua quality vào memory.

    battlecard_auto_write=True → ghi thẳng memory/battlecards/; False → memory/_proposed/
    chờ duyệt (governance mặc định). Lỗi ghi không làm fail run.
    """
    from datetime import date

    from vks_intelligence.config import get_settings
    from vks_intelligence.contracts import Confidence, MemoryPatch, MemoryPatchOp
    from vks_intelligence.tools.memory_tool import apply_patch

    s = get_settings()
    competitor = str(request.payload.get("competitor") or "general").lower().replace(" ", "-")
    rel_path = f"battlecards/{date.today().isoformat()}_battlecard_{competitor}.md"
    patch = MemoryPatch(
        op=MemoryPatchOp.UPDATE,
        path=rel_path,
        reason=f"Auto-update battlecard từ run {metadata.run_id}",
        content=content,
        confidence=Confidence.HIGH,
    )
    try:
        out = apply_patch(s.workspace_path, patch, auto=s.battlecard_auto_write)
        where = "memory/battlecards" if s.battlecard_auto_write else "memory/_proposed (chờ duyệt)"
        metadata.warnings.append(f"Battlecard ghi vào {where}: {out.name}")
        log.info("Battlecard persisted → %s", out)
    except Exception as exc:
        log.warning("Persist battlecard thất bại: %s", exc)


def _make_run_id(request: TaskRequest) -> str:
    date_str = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H%M%S")
    return f"{date_str}_{request.task_type.value}_{request.request_id[:8]}"


def _budget_policy_for(request: TaskRequest, workload_budget) -> BudgetPolicy:
    default_policy = BudgetPolicy()
    if request.budget_policy != default_policy:
        return request.budget_policy
    return BudgetPolicy(
        max_agents=workload_budget.max_agents,
        max_agent_seconds=workload_budget.agent_timeout_seconds,
        max_retries=workload_budget.max_retries,
        max_input_tokens=workload_budget.max_input_tokens,
        max_output_tokens=workload_budget.max_output_tokens,
    )


def _instruction_for(request: TaskRequest, agent: str) -> str:
    base = {
        "qa_agent": request.payload.get("question", "Trả lời câu hỏi từ workspace memory."),
        "daily_intelligence_agent": "Tổng hợp tín hiệu market/competitor trong 24-48h gần nhất và tạo daily brief.",
        "market_trend_agent": "Tổng hợp tín hiệu thị trường Kubernetes/AI infra cho kỳ báo cáo này.",
        "competitor_agent": f"Theo dõi và tổng hợp động thái đối thủ{_competitor_hint(request)}.",
        "pricing_agent": "Cập nhật pricing landscape và phân tích TCO so sánh.",
        "regulatory_agent": "Cập nhật văn bản pháp lý và compliance yêu cầu tại VN.",
        "positioning_agent": "Tổng hợp điểm mạnh/yếu GreenNode VKS và hướng positioning.",
        "battlecard_agent": f"Sinh battlecard head-to-head{_competitor_hint(request)}.",
        "memory_curator_agent": "Rà soát memory, phát hiện dữ liệu cũ/trùng, đề xuất patch.",
        "quality_critic_agent": "Soát hallucination, claim thiếu nguồn, và chất lượng output.",
    }
    return base.get(agent, f"Thực hiện nhiệm vụ: {request.task_type.value}.")


def _competitor_hint(request: TaskRequest) -> str:
    c = request.payload.get("competitor")
    return f" với {c}" if c else ""


def _inputs_for(request: TaskRequest, agent: str) -> dict:
    base: dict = {"task_payload": request.payload}
    if agent == "qa_agent":
        base["question"] = request.payload.get("question", "")
    if request.payload.get("user_memory_context"):
        base["user_memory_context"] = request.payload["user_memory_context"]
    if request.payload.get("competitor"):
        base["competitor"] = request.payload["competitor"]
    return base


def _collect_evidence(request: TaskRequest, workspace_path: Path):
    """Collect EvidenceBundle cho task cần dữ liệu mới nhất."""
    from vks_intelligence.config import get_settings
    from vks_intelligence.tools.evidence_tool import collect
    from vks_intelligence.tools.source_tool import social_scrape_targets

    s = get_settings()

    needs_fresh = request.task_type in (
        TaskType.DAILY_INTELLIGENCE,
        TaskType.WEEKLY_DIGEST,
        TaskType.MONTHLY_BRIEF,
        TaskType.COMPETITOR_MONITOR,
        TaskType.PRICING_ANALYSIS,
        TaskType.BATTLECARD,
    )
    if not needs_fresh:
        return None

    days = {
        TaskType.DAILY_INTELLIGENCE: 1,
        TaskType.WEEKLY_DIGEST: 7,
        TaskType.MONTHLY_BRIEF: 30,
        TaskType.COMPETITOR_MONITOR: 3,
        TaskType.PRICING_ANALYSIS: 14,
        TaskType.BATTLECARD: 7,
    }.get(request.task_type, 7)

    interactive = bool(request.payload.get("interactive")) or request.source == "qa-research"
    scrape_targets = None
    if request.task_type == TaskType.DAILY_INTELLIGENCE:
        scrape_targets = social_scrape_targets("interactive_daily" if interactive else "daily")
    elif request.task_type == TaskType.WEEKLY_DIGEST:
        scrape_targets = social_scrape_targets("all")
    elif request.task_type == TaskType.MONTHLY_BRIEF:
        scrape_targets = social_scrape_targets("all")
    elif request.task_type == TaskType.COMPETITOR_MONITOR:
        scrape_targets = [
            "viettel-voks",
            "fpt-fke",
            "bizfly-bke",
            *social_scrape_targets("all"),
        ]
    elif request.task_type == TaskType.PRICING_ANALYSIS:
        scrape_targets = [
            "aws-eks-pricing",
            "gke-pricing",
            *social_scrape_targets("hyperscalers"),
        ]
    elif request.task_type == TaskType.BATTLECARD:
        scrape_targets = [
            "viettel-voks",
            "fpt-fke",
            "bizfly-bke",
            *social_scrape_targets("all"),
        ]

    if interactive and scrape_targets:
        scrape_targets = scrape_targets[:s.evidence_interactive_max_targets]

    return collect(
        workspace_path,
        days=days,
        include_rss=True,
        include_scrape=bool(scrape_targets),
        scrape_targets=scrape_targets,
    )


def _allows_partial(task_type: TaskType, results) -> bool:
    """Cho phép partial result khi có đủ evidence từ agent không-critical."""
    ok_count = sum(1 for r in results if r.status.value != "failed")
    return ok_count >= 2 and task_type in (
        TaskType.WEEKLY_DIGEST,
        TaskType.MONTHLY_BRIEF,
    )
