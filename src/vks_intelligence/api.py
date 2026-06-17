"""FastAPI app — toàn bộ HTTP surface của GreenNode VKS Intelligence.

Phục vụ trên port 8080:
  GET  /health              AgentBase liveness probe
  POST /invocations         AgentBase task routing
  POST /tasks/qa            Q&A nhanh từ memory
  POST /tasks/daily-intelligence
  POST /tasks/weekly-digest
  POST /tasks/monthly-brief
  POST /tasks/competitor-monitor
  POST /tasks/pricing-analysis
  POST /tasks/battlecard
  POST /tasks/memory-maintenance
  GET  /tasks/{task_id}     Status check
  POST /quality/check       Deterministic quality gate
  GET  /dashboard/summary   Observability
  GET  /dashboard/runs
  GET  /dashboard/cost-trend   Token usage theo ngày
  GET  /dashboard/qa-activity  QA activity từ Telegram (streaming + research)
  GET  /dashboard/evaluation   Evaluation loop stats (revise rate, citation warnings)
  GET  /dashboard/ui/       Static HTML dashboard
  POST /telegram/webhook    Telegram bot handler (không cần n8n cho Q&A)
"""

from __future__ import annotations

import json
import logging
import os
import uuid
from datetime import datetime, timedelta, timezone
from functools import lru_cache
from pathlib import Path

from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel

from vks_intelligence.contracts import BudgetPolicy, ModelPolicy, TaskRequest, TaskType
from vks_intelligence.schemas import (
    CostTrendPoint,
    DailyIntelligenceRequestBody,
    DashboardSummary,
    EvalSummary,
    HealthResponse,
    QAActivitySummary,
    QARequestBody,
    QAResponse,
    QualityCheckRequest,
    QualityCheckResponse,
    RunDetail,
    RunSummary,
    TaskRequestBody,
    TaskResponse,
)

log = logging.getLogger(__name__)
app = FastAPI(title="GreenNode VKS Intelligence", version="0.1.0")


def _runtime_info() -> dict:
    from vks_intelligence.config import get_settings

    s = get_settings()
    return {
        "version": "0.1.0",
        "build_image": s.app_build_image,
        "build_tag": s.app_build_tag,
        "build_sha": s.app_build_sha,
        "build_time": s.app_build_time,
        "optimizer": {
            "evidence_rss_timeout_seconds": s.evidence_rss_timeout_seconds,
            "evidence_web_timeout_seconds": s.evidence_web_timeout_seconds,
            "evidence_social_timeout_seconds": s.evidence_social_timeout_seconds,
            "evidence_fetch_max_workers": s.evidence_fetch_max_workers,
            "evidence_interactive_max_targets": s.evidence_interactive_max_targets,
            "qa_current_research_cache_ttl_seconds": s.qa_current_research_cache_ttl_seconds,
        },
        "features": {
            "artifact_fast_path": True,
            "telegram_active_task_guard": True,
            "interactive_daily_scope": True,
            "parallel_evidence_fetch": True,
            "raw_json_filter": True,
        },
    }


# ──────────────────────────────────────────────────────────────────
# Models
# ──────────────────────────────────────────────────────────────────

class _InvocationRequest(BaseModel):
    task_type: str = ""
    question: str = ""
    request_id: str = ""
    dry_run: bool = False
    notify: bool = False
    model_policy: str = "balanced"
    payload: dict = {}

    model_config = {"extra": "allow", "protected_namespaces": ()}


# ──────────────────────────────────────────────────────────────────
# Singletons (lazy init — tránh import nặng lúc startup)
# ──────────────────────────────────────────────────────────────────

@lru_cache(maxsize=1)
def _supervisor():
    from vks_intelligence.supervisor import Supervisor
    return Supervisor()


@lru_cache(maxsize=1)
def _router():
    from vks_intelligence.llm.router import ModelRouter
    return ModelRouter()


# ──────────────────────────────────────────────────────────────────
# Internal helpers
# ──────────────────────────────────────────────────────────────────

def _task_response_from_metadata(meta) -> TaskResponse:
    from vks_intelligence.config import get_settings
    s = get_settings()
    return TaskResponse(
        task_id=meta.task_id,
        status=meta.status.value,
        quality_passed=bool(meta.quality_score and meta.quality_score >= s.quality_min_score_publish),
        quality_score=meta.quality_score,
        artifact_path=str(s.workspace_path / s.artifact_root / meta.run_id),
        requires_approval=meta.approval_required,
        fallbacks_used=[f"{fb.from_model}→{fb.to_model}" for fb in meta.fallbacks],
        warnings=meta.warnings[:10],
    )


def _make_qa_context(question: str, session_id: str):
    from vks_intelligence.contracts import BudgetPolicy
    from vks_intelligence.llm.budgets import budget_for
    from vks_intelligence.run_context import RunContext

    req = TaskRequest(
        request_id=session_id or uuid.uuid4().hex[:8],
        task_type=TaskType.QA,
        payload={"question": question},
        model_policy=ModelPolicy.BALANCED,
    )
    wb = budget_for(TaskType.QA)
    ctx = RunContext(
        request=req,
        run_id=f"qa_{req.request_id}",
        budget=BudgetPolicy(
            max_agents=wb.max_agents,
            max_agent_seconds=wb.agent_timeout_seconds,
            max_retries=wb.max_retries,
        ),
    )
    return req, ctx


# ──────────────────────────────────────────────────────────────────
# AgentBase Runtime contract
# ──────────────────────────────────────────────────────────────────

@app.get("/health", response_model=HealthResponse)
def health() -> HealthResponse:
    from vks_intelligence.config import get_settings
    s = get_settings()
    models = list(dict.fromkeys([
        s.model_qa, s.model_research, s.model_synthesis, s.model_critic, s.model_premium,
    ]))
    return HealthResponse(
        status="ok",
        timestamp=datetime.now(timezone.utc).isoformat(),
        version="0.1.0",
        models_enabled=models,
        build_image=s.app_build_image,
        build_tag=s.app_build_tag,
        build_sha=s.app_build_sha,
        build_time=s.app_build_time,
    )


@app.get("/runtime/info")
def runtime_info() -> dict:
    """Expose non-secret build/runtime metadata để verify deployed image."""
    return _runtime_info()


@app.post("/invocations")
def invocations(body: _InvocationRequest) -> dict:
    """AgentBase Runtime contract — route theo task_type hoặc question."""
    task_type_raw = body.task_type or ("qa" if body.question else "")

    if not task_type_raw:
        return {"error": "Thiếu task_type hoặc question trong payload."}

    try:
        task_type = TaskType(task_type_raw)
    except ValueError:
        valid = [t.value for t in TaskType]
        return {"error": f"task_type không hợp lệ: '{task_type_raw}'. Giá trị hợp lệ: {valid}"}

    if task_type == TaskType.QA:
        qa_body = QARequestBody(
            question=body.question,
            session_id=body.request_id,
        )
        r = task_qa(qa_body)
        return r.model_dump()

    req = TaskRequest(
        request_id=body.request_id or f"inv-{os.urandom(4).hex()}",
        task_type=task_type,
        source="invocations",
        payload=body.payload or body.model_dump(),
        dry_run=body.dry_run,
        notify=body.notify,
        save_output=True,
        model_policy=ModelPolicy(body.model_policy),
    )
    meta = _supervisor().run(req)
    return _task_response_from_metadata(meta).model_dump()


# ──────────────────────────────────────────────────────────────────
# Task endpoints
# ──────────────────────────────────────────────────────────────────

_STATUS_KEYWORDS = {
    "xong chưa", "done chưa", "kết quả", "treo", "timeout",
    "research lâu", "đang chạy", "bao lâu", "mấy lâu", "status",
    "tiến độ", "đến đâu", "xử lý chưa", "hoàn tất chưa",
}


def _is_status_query(question: str) -> bool:
    q = question.lower()
    return any(kw in q for kw in _STATUS_KEYWORDS)


def _research_task_for_question(question: str) -> tuple[TaskType, int]:
    q = question.lower()
    weekly_markers = ("tuần này", "tuan nay", "weekly", "digest", "tuần qua", "tuan qua")
    if any(marker in q for marker in weekly_markers):
        return TaskType.WEEKLY_DIGEST, 7
    competitor_markers = (
        "fpt", "viettel", "bizfly", "vng cloud", "bke", "fke", "voks",
        "aws", "gke", "gcp", "azure", "aks", "eks",
        "đối thủ", "doi thu", "competitor",
    )
    if any(marker in q for marker in competitor_markers):
        return TaskType.COMPETITOR_MONITOR, 3
    pricing_markers = (
        "pricing", "giá", "price", "tco", "cost", "chi phí", "chi phi",
        "báo giá", "bao gia", "so sánh giá", "so sanh gia",
    )
    if any(marker in q for marker in pricing_markers):
        return TaskType.PRICING_ANALYSIS, 7
    return TaskType.DAILY_INTELLIGENCE, 1


_FORCE_REFRESH_MARKERS = (
    "refresh",
    "refresh lại",
    "refresh lai",
    "làm mới",
    "lam moi",
    "chạy lại",
    "chay lai",
    "research lại",
    "research lai",
    "fetch lại",
    "fetch lai",
    "mở research",
    "mo research",
    "mở một research",
    "đào sâu",
    "dao sau",
    "phân tích sâu",
    "phan tich sau",
    "deep dive",
)


def _force_refresh_question(question: str) -> bool:
    q = question.lower()
    if any(marker in q for marker in _FORCE_REFRESH_MARKERS):
        return True
    # "chạy/tìm hiểu + research" combo — bắt "mở một research task về..."
    has_research = "research" in q
    has_action = any(w in q for w in ("mở", "chạy", "chay", "tìm hiểu", "tim hieu"))
    return has_research and has_action


@app.post("/tasks/qa", response_model=QAResponse)
def task_qa(body: QARequestBody) -> QAResponse:
    """Q&A từ memory + AgentBase conversation memory; trả final answer thật."""
    import uuid as _uuid
    from vks_intelligence.config import get_settings
    from vks_intelligence.specialists.qa_agent import QAAgent
    from vks_intelligence.tools.agentbase_memory_tool import get_memory_tool
    from vks_intelligence.tools.task_state_store import TaskStateStore

    s = get_settings()
    mem = get_memory_tool()
    state = TaskStateStore(s.workspace_path)

    actor_id = body.actor_id or body.session_id or ""
    session_id = body.session_id or f"api-{_uuid.uuid4().hex[:8]}"

    # ── 1. Status query: kiểm tra active task trước khi làm bất cứ thứ gì ──
    if _is_status_query(body.question):
        active = state.get_by_actor(actor_id) if actor_id else None
        if active:
            return QAResponse(
                answer=state.build_status_reply(active),
                confidence="high",
                escalated=False,
                session_id=session_id,
            )

    # ── 2. Save user event vào conversation memory ──────────────────────────
    if actor_id:
        mem.save_event(actor_id, session_id, "user", body.question)

    # ── 3. Search user memory để enrich context ─────────────────────────────
    user_facts: list[str] = []
    if actor_id:
        user_facts = mem.search_user_memory(actor_id, body.question, limit=5)

    # ── 4. Build QA context + classify intent ───────────────────────────────
    req, ctx = _make_qa_context(body.question, session_id)
    agent = QAAgent(_router())
    intent = agent.classify_intent(body.question)

    if user_facts:
        req.payload["user_memory_context"] = "\n".join(user_facts)

    # ── 5. Current research path — chạy đồng bộ, trả final answer thật ─────
    if intent.value == "current_research":
        run_id = f"qa-research-{_uuid.uuid4().hex[:8]}"
        artifact_root = str(s.workspace_path / s.artifact_root / run_id)
        artifact_path = artifact_root
        research_task_type, days_window = _research_task_for_question(body.question)
        if body.task_type_override:
            try:
                research_task_type = TaskType(body.task_type_override)
            except ValueError:
                pass
        active = state.get_by_actor(actor_id) if actor_id else None

        if active and active.get("status") == "running":
            resp = QAResponse(
                answer=state.build_status_reply(active),
                confidence="high",
                escalated=True,
                research_used=True,
                session_id=session_id,
                artifact_path=active.get("artifact_path", ""),
            )

        elif not (body.force_refresh or _force_refresh_question(body.question)):
            from vks_intelligence.tools.artifact_index import latest_fresh_artifact

            cached = latest_fresh_artifact(
                s.workspace_path / s.artifact_root,
                research_task_type,
                s.qa_current_research_cache_ttl_seconds,
            )
            if cached:
                summary = state.get_run_summary(str(cached.run_dir), max_chars=6_000)
                if summary:
                    finished_local = cached.finished_at.astimezone(
                        timezone(timedelta(hours=7))
                    ).strftime("%Y-%m-%d %H:%M ICT")
                    answer = (
                        f"{summary}\n\n"
                        f"_Dùng artifact {research_task_type.value} đã collect gần nhất: "
                        f"{finished_local}. Nhắn \"refresh lại\" nếu muốn chạy live research._"
                    )
                    resp = QAResponse(
                        answer=answer,
                        confidence="high",
                        escalated=True,
                        research_used=True,
                        session_id=session_id,
                        artifact_path=str(cached.run_dir),
                    )
                else:
                    resp = None
            else:
                resp = None

        else:
            resp = None

        if resp is None and actor_id:
            state.upsert(actor_id, session_id, run_id, research_task_type.value,
                         stage="starting", artifact_path=artifact_root)
            state.update_stage(run_id, "collect_evidence")

        if resp is None:
            try:
                research_req = req.__class__(
                    request_id=run_id,
                    task_type=research_task_type,
                    source="qa-research",
                    payload={**req.payload, "days_window": days_window, "interactive": True},
                    dry_run=False,
                    save_output=True,
                )
                if actor_id:
                    state.update_stage(run_id, "run_agents")
                meta = _supervisor().run(research_req)
                artifact_path = str(s.workspace_path / s.artifact_root / meta.run_id)

                if actor_id:
                    state.complete(run_id, artifact_path)

                summary = state.get_run_summary(artifact_path, max_chars=6_000)
                if not summary and meta.warnings:
                    summary = meta.warnings[0]
                if not summary:
                    # Fallback: đọc synthesis từ run
                    synth = s.workspace_path / s.artifact_root / meta.run_id / "synthesis.md"
                    if synth.exists():
                        summary = synth.read_text(encoding="utf-8")[:6_000]

                answer = summary or "Đã collect dữ liệu mới nhất nhưng không có tóm tắt — xem artifact."

            except Exception as exc:
                if actor_id:
                    state.fail(run_id, str(exc)[:80])
                answer = f"Research gặp lỗi: {exc}. Thử lại sau nhé."

            resp = QAResponse(
                answer=answer,
                confidence="medium",
                escalated=True,
                research_used=True,
                session_id=session_id,
                artifact_path=artifact_path,
            )

    else:
        # ── 6. Memory fast-path ─────────────────────────────────────────────
        if user_facts:
            ctx.request.payload["user_memory_context"] = "\n".join(user_facts)

        answer, confidence, escalated, sources = agent.answer(body.question, ctx)

        if escalated:
            research_task_type, days_window = _research_task_for_question(body.question)
            run_id = f"qa-esc-{_uuid.uuid4().hex[:8]}"
            if actor_id:
                state.upsert(actor_id, session_id, run_id, research_task_type.value,
                             stage="run_agents",
                             artifact_path=str(s.workspace_path / s.artifact_root / run_id))
            try:
                research_req = req.__class__(
                    request_id=run_id,
                    task_type=research_task_type,
                    source="qa-escalated",
                    payload={**req.payload, "days_window": days_window, "interactive": True},
                    dry_run=False,
                    save_output=True,
                )
                meta = _supervisor().run(research_req)
                artifact_path = str(s.workspace_path / s.artifact_root / meta.run_id)
                if actor_id:
                    state.complete(run_id, artifact_path)
                sup_summary = state.get_run_summary(artifact_path)
                if sup_summary and len(sup_summary) > len(answer or ""):
                    answer = sup_summary
            except Exception as exc:
                if actor_id:
                    state.fail(run_id, str(exc)[:80])

            resp = QAResponse(
                answer=answer or "🌼 Lin Lin 🌼 chưa có đủ dữ liệu về câu này — đang tìm hiểu thêm.",
                confidence=confidence,
                escalated=True,
                research_used=True,
                sources=sources,
                session_id=session_id,
            )
        else:
            resp = QAResponse(
                answer=answer,
                confidence=confidence,
                escalated=False,
                research_used=False,
                sources=sources,
                session_id=session_id,
            )

    # ── 7. Save assistant event + trigger memory generation ─────────────────
    if actor_id and resp.answer:
        mem.save_event(actor_id, session_id, "assistant", resp.answer)
        try:
            mem.generate_records(actor_id, session_id)
        except Exception:
            log.debug("memory record generation failed for actor %s", actor_id, exc_info=True)

    return resp


@app.post("/tasks/daily-intelligence", response_model=TaskResponse)
def task_daily_intelligence(body: DailyIntelligenceRequestBody) -> TaskResponse:
    """Daily brief/alert từ RSS + scrape; hỗ trợ dry_run."""
    meta = _supervisor().run(TaskRequest(
        request_id=body.request_id,
        task_type=TaskType.DAILY_INTELLIGENCE,
        source=body.source,
        payload={"days_window": body.days_window},
        dry_run=body.dry_run,
        notify=body.notify,
        save_output=body.save_output,
        human_approval_required=body.human_approval_required,
        model_policy=body.model_policy,
    ))
    return _task_response_from_metadata(meta)


@app.post("/tasks/weekly-digest", response_model=TaskResponse)
def task_weekly_digest(body: TaskRequestBody) -> TaskResponse:
    """Sinh weekly digest qua supervisor + specialist agents."""
    meta = _supervisor().run(TaskRequest(
        request_id=body.request_id,
        task_type=TaskType.WEEKLY_DIGEST,
        source=body.source,
        payload=body.payload,
        dry_run=body.dry_run,
        notify=body.notify,
        save_output=body.save_output,
        human_approval_required=body.human_approval_required,
        model_policy=body.model_policy,
        timeout_seconds=body.timeout_seconds,
        budget_policy=body.budget_policy or BudgetPolicy(),
    ))
    return _task_response_from_metadata(meta)


@app.post("/tasks/monthly-brief", response_model=TaskResponse)
def task_monthly_brief(body: TaskRequestBody) -> TaskResponse:
    """Sinh monthly executive brief; mặc định yêu cầu human approval."""
    meta = _supervisor().run(TaskRequest(
        request_id=body.request_id,
        task_type=TaskType.MONTHLY_BRIEF,
        source=body.source,
        payload=body.payload,
        dry_run=body.dry_run,
        notify=body.notify,
        save_output=body.save_output,
        human_approval_required=True if not body.dry_run else body.human_approval_required,
        model_policy=body.model_policy,
        timeout_seconds=body.timeout_seconds,
        budget_policy=body.budget_policy or BudgetPolicy(),
    ))
    return _task_response_from_metadata(meta)


@app.post("/tasks/competitor-monitor", response_model=TaskResponse)
def task_competitor_monitor(body: TaskRequestBody) -> TaskResponse:
    """Theo dõi đối thủ; alert khi có signal đủ severity."""
    meta = _supervisor().run(TaskRequest(
        request_id=body.request_id,
        task_type=TaskType.COMPETITOR_MONITOR,
        source=body.source,
        payload=body.payload,
        dry_run=body.dry_run,
        notify=body.notify,
        save_output=body.save_output,
        model_policy=body.model_policy,
        timeout_seconds=body.timeout_seconds,
        budget_policy=body.budget_policy or BudgetPolicy(),
    ))
    return _task_response_from_metadata(meta)


@app.post("/tasks/pricing-analysis", response_model=TaskResponse)
def task_pricing_analysis(body: TaskRequestBody) -> TaskResponse:
    """Phân tích pricing/TCO từ workspace + evidence pricing mới."""
    meta = _supervisor().run(TaskRequest(
        request_id=body.request_id,
        task_type=TaskType.PRICING_ANALYSIS,
        source=body.source,
        payload=body.payload,
        dry_run=body.dry_run,
        notify=body.notify,
        save_output=body.save_output,
        human_approval_required=body.human_approval_required,
        model_policy=body.model_policy,
        timeout_seconds=body.timeout_seconds,
        budget_policy=body.budget_policy or BudgetPolicy(),
    ))
    return _task_response_from_metadata(meta)


@app.post("/tasks/battlecard", response_model=TaskResponse)
def task_battlecard(body: TaskRequestBody) -> TaskResponse:
    """Sinh battlecard: competitor → pricing → battlecard_agent → quality."""
    if not body.payload.get("competitor"):
        raise HTTPException(status_code=422, detail="payload.competitor là bắt buộc")
    meta = _supervisor().run(TaskRequest(
        request_id=body.request_id,
        task_type=TaskType.BATTLECARD,
        source=body.source,
        payload=body.payload,
        dry_run=body.dry_run,
        save_output=body.save_output,
        model_policy=body.model_policy,
        timeout_seconds=body.timeout_seconds,
        budget_policy=body.budget_policy or BudgetPolicy(),
    ))
    return _task_response_from_metadata(meta)


@app.post("/tasks/memory-maintenance", response_model=TaskResponse)
def task_memory_maintenance(body: TaskRequestBody) -> TaskResponse:
    """Memory Curator đề xuất patch; auto-apply patch confidence cao."""
    meta = _supervisor().run(TaskRequest(
        request_id=body.request_id,
        task_type=TaskType.MEMORY_MAINTENANCE,
        source=body.source,
        payload=body.payload,
        dry_run=body.dry_run,
        save_output=body.save_output,
        model_policy=body.model_policy,
        timeout_seconds=body.timeout_seconds,
        budget_policy=body.budget_policy or BudgetPolicy(),
    ))
    return _task_response_from_metadata(meta)


@app.get("/tasks/{task_id}", response_model=TaskResponse)
def get_task(task_id: str) -> TaskResponse:
    """Đọc trạng thái + artifact của một run đã chạy."""
    from vks_intelligence.config import get_settings
    s = get_settings()
    artifact_root = s.workspace_path / s.artifact_root
    if not artifact_root.exists():
        raise HTTPException(status_code=404, detail=f"Task '{task_id}' không tìm thấy")
    for run_dir in sorted(artifact_root.iterdir(), key=lambda d: d.stat().st_mtime, reverse=True):
        meta_path = run_dir / "metadata.json"
        if not meta_path.exists():
            continue
        meta = json.loads(meta_path.read_text(encoding="utf-8"))
        if meta.get("task_id") == task_id or meta.get("run_id") == task_id:
            return TaskResponse(
                task_id=meta["task_id"],
                status=meta.get("status", "unknown"),
                quality_score=meta.get("quality_score"),
                artifact_path=str(run_dir),
                requires_approval=meta.get("approval_required", False),
                fallbacks_used=[
                    f"{fb['from_model']}→{fb['to_model']}"
                    for fb in meta.get("fallbacks", [])
                ],
                warnings=meta.get("warnings", [])[:10],
            )
    raise HTTPException(status_code=404, detail=f"Task '{task_id}' không tìm thấy")


# ──────────────────────────────────────────────────────────────────
# Quality & Dashboard
# ──────────────────────────────────────────────────────────────────

@app.post("/quality/check", response_model=QualityCheckResponse)
def quality_check(body: QualityCheckRequest) -> QualityCheckResponse:
    from vks_intelligence.quality import validate_output
    r = validate_output(body.content, body.task_type)
    return QualityCheckResponse(verdict=r.verdict.value, score=r.score, failures=r.failures, warnings=r.warnings)


@app.get("/dashboard/summary", response_model=DashboardSummary)
def dashboard_summary() -> DashboardSummary:
    from vks_intelligence.config import get_settings
    from vks_intelligence.dashboard import summary
    s = get_settings()
    return summary(s.workspace_path / s.artifact_root)


@app.get("/dashboard/runs", response_model=list[RunSummary])
def dashboard_runs(limit: int = 50) -> list[RunSummary]:
    from vks_intelligence.config import get_settings
    from vks_intelligence.dashboard import list_runs
    s = get_settings()
    return list_runs(s.workspace_path / s.artifact_root, limit=limit)


def _qa_log_root(s) -> Path:
    """qa_log nằm cạnh artifact_root: outputs/qa_log/."""
    return (s.workspace_path / s.artifact_root).parent / "qa_log"


@app.get("/dashboard/cost-trend", response_model=list[CostTrendPoint])
def dashboard_cost_trend(days: int = 14) -> list[CostTrendPoint]:
    from vks_intelligence.config import get_settings
    from vks_intelligence.dashboard import cost_trend
    s = get_settings()
    return cost_trend(s.workspace_path / s.artifact_root, days=days)


@app.get("/dashboard/qa-activity", response_model=QAActivitySummary)
def dashboard_qa_activity(days: int = 14) -> QAActivitySummary:
    from vks_intelligence.config import get_settings
    from vks_intelligence.dashboard import qa_activity
    s = get_settings()
    return qa_activity(_qa_log_root(s), days=days)


@app.get("/dashboard/evaluation", response_model=EvalSummary, tags=["dashboard"])
def dashboard_evaluation() -> EvalSummary:
    from vks_intelligence.config import get_settings
    from vks_intelligence.dashboard import evaluation_summary
    s = get_settings()
    return evaluation_summary(s.workspace_path / s.artifact_root)


@app.get("/dashboard/runs/{run_id}", response_model=RunDetail)
def dashboard_run_detail(run_id: str) -> RunDetail:
    from vks_intelligence.config import get_settings
    from vks_intelligence.dashboard import run_detail
    s = get_settings()
    detail = run_detail(s.workspace_path / s.artifact_root, run_id)
    if detail is None:
        raise HTTPException(status_code=404, detail=f"Run '{run_id}' không tồn tại")
    return detail


class _ChatRequestBody(BaseModel):
    message: str
    history: list[dict] = []


@app.post("/dashboard/chat")
def dashboard_chat(body: _ChatRequestBody):
    """Chat streaming trên dashboard — SSE, tái dùng QAAgent.stream_answer_text.

    History giữ phía browser và gửi kèm mỗi request (server stateless).
    Đây là ngoại lệ có chủ đích của nguyên tắc "dashboard chỉ đọc artifact".
    """
    import time as _time

    from fastapi.responses import StreamingResponse

    from vks_intelligence.config import get_settings
    from vks_intelligence.specialists.qa_agent import QAAgent
    from vks_intelligence.tools import qa_log

    if not body.message.strip():
        raise HTTPException(status_code=422, detail="message rỗng")

    s = get_settings()
    history_lines = []
    for turn in body.history[-6:]:
        role = "User" if turn.get("role") == "user" else "Assistant"
        history_lines.append(f"{role}: {str(turn.get('text', ''))[:500]}")
    session_history = "\n".join(history_lines)

    qa_agent = QAAgent(_router())
    start = _time.monotonic()

    def _gen():
        ok = True
        yield 'data: {"thinking": true}\n\n'
        try:
            for chunk in qa_agent.stream_answer_text(body.message, session_history=session_history):
                yield f"data: {json.dumps({'delta': chunk}, ensure_ascii=False)}\n\n"
        except Exception as exc:
            ok = False
            yield f"data: {json.dumps({'error': str(exc)}, ensure_ascii=False)}\n\n"
        finally:
            yield 'data: {"done": true}\n\n'
            qa_log.record(
                _qa_log_root(s),
                actor_id="dashboard",
                intent="memory_lookup",
                latency_ms=int((_time.monotonic() - start) * 1000),
                ok=ok,
                routed_by="dashboard",
            )

    return StreamingResponse(_gen(), media_type="text/event-stream")


# ──────────────────────────────────────────────────────────────────
# Telegram Webhook — không cần n8n cho Q&A
# Set webhook 1 lần: POST /telegram/set-webhook {"url": "https://<endpoint>/telegram/webhook"}
# ──────────────────────────────────────────────────────────────────

_GREETINGS = {
    "hi", "hey", "hello", "xin chào", "xin chao", "chào", "chao",
    "alo", "yo", "hola", "howdy", "sup", "ciao",
}
_HELP_CMDS = {"/help", "/start", "help", "bạn là ai", "ban la ai",
              "làm được gì", "lam duoc gi", "bạn có thể làm gì"}

# Affirmative responses — "có" sau khi bot đề xuất research
_AFFIRMATIVES = {
    "có", "co", "ok", "oke", "được", "duoc", "yes", "ừ", "u",
    "đúng", "dung", "sure", "vâng", "vang", "muốn", "muon",
    "có chứ", "tất nhiên", "tat nhien", "đồng ý", "dong y",
}

# Maps actor_id → (original_topic, timestamp) — pending research offer từ bot
_PENDING_RESEARCH: dict[str, tuple[str, float]] = {}

_RESEARCH_OFFER_MARKERS = (
    "mở research",
    "chạy research",
    "nghiên cứu thêm",
    "đào sâu hơn",
    "bạn có muốn",
    "tìm hiểu thêm",
    "live research",
    "collect thêm",
)


def _is_affirmative(text: str) -> bool:
    return text.lower().strip().rstrip("!?.") in _AFFIRMATIVES


def _contains_research_offer(text: str) -> bool:
    t = text.lower()
    return any(m in t for m in _RESEARCH_OFFER_MARKERS)


def _format_telegram_qa_reply(qa_resp: QAResponse) -> str:
    answer = (
        qa_resp.answer
        or "🌼 Lin Lin 🌼 chưa có dữ liệu để trả lời câu này. Muốn mở research task không? 🔍"
    )
    footer_parts: list[str] = []
    if qa_resp.research_used:
        footer_parts.append("🔍 _Đã collect dữ liệu mới nhất._")
    if qa_resp.escalated and not qa_resp.research_used:
        footer_parts.append("⚡ _Đang mở research task để tìm hiểu thêm..._")
    elif qa_resp.confidence == "low":
        footer_parts.append("⚠️ _Dữ liệu còn hạn chế — kết quả có thể chưa đầy đủ._")
    if qa_resp.sources:
        footer_parts.append("📚 " + ", ".join(qa_resp.sources[:3]))

    if footer_parts:
        return answer + "\n\n" + "\n".join(footer_parts)
    return answer


def _send_telegram_reply(
    token: str,
    chat_id: str,
    text: str,
    *,
    reply_to: int | None = None,
    max_chars: int = 3900,
) -> None:
    from vks_intelligence.tools.telegram_tool import format_telegram_html_messages, send_message

    chunks = format_telegram_html_messages(text, max_chars)
    for idx, chunk in enumerate(chunks):
        send_message(
            token,
            chat_id,
            chunk,
            parse_mode="HTML",
            reply_to=reply_to if idx == 0 else None,
        )


@app.post("/telegram/webhook")
async def telegram_webhook(request: Request) -> dict:
    """Nhận Telegram Update, route sang Lin Lin QA agent."""
    from vks_intelligence.config import get_settings
    from vks_intelligence.tools.telegram_tool import send_action, send_message

    s = get_settings()
    if not s.telegram_bot_token:
        return {"ok": False, "error": "TELEGRAM_BOT_TOKEN chưa set"}

    try:
        update = await request.json()
    except Exception:
        return {"ok": False}

    msg = update.get("message") or update.get("channel_post") or {}
    text = (msg.get("text") or "").strip()
    chat_id = str(msg.get("chat", {}).get("id", ""))
    msg_id = msg.get("message_id")
    from_info = msg.get("from", {})
    user_id = str(from_info.get("id", ""))
    first_name = from_info.get("first_name", "")
    username = from_info.get("username", "")

    if not text or not chat_id:
        return {"ok": True}

    text_lower = text.lower().strip()

    # Greeting — trả lời thân thiện, không qua QA pipeline
    if text_lower in _GREETINGS:
        name_part = f" {first_name}" if first_name else ""
        reply = (
            f"👋 Chào{name_part}! 🌼 Lin Lin 🌼 đây — trợ lý AI của GreenNode VKS 😊\n\n"
            "Mình có thể giúp bạn:\n"
            "🔍 So sánh đối thủ (Viettel, FPT, Bizfly, AWS...)\n"
            "💰 Pricing & TCO analysis\n"
            "📈 Market trends & AI infra\n"
            "🎯 Positioning & battlecard\n\n"
            "Cứ hỏi thẳng nhé!"
        )
        send_message(s.telegram_bot_token, chat_id, reply, reply_to=msg_id)
        return {"ok": True}

    # Help command
    if text_lower in _HELP_CMDS:
        reply = (
            "🤖 *🌼 Lin Lin 🌼 — GreenNode VKS Intelligence*\n\n"
            "🌼 Lin Lin 🌼 có thể giúp bạn:\n\n"
            "🔍 *Research*\n"
            "• So sánh đối thủ, tính năng, SLA\n"
            "• Pricing analysis & TCO\n"
            "• Market trends Kubernetes/AI infra\n\n"
            "📊 *Intelligence*\n"
            "• Động thái Viettel vOKS, FPT FKE, Bizfly BKE\n"
            "• AWS EKS, GKE, AKS update mới nhất\n"
            "• GPU node pool, AI-native feature\n\n"
            "💡 *Strategy*\n"
            "• Positioning & talk track vs từng đối thủ\n"
            "• Objection handling\n"
            "• Regulatory VN & data residency\n\n"
            "Chỉ cần hỏi tự nhiên là được! 💬"
        )
        send_message(s.telegram_bot_token, chat_id, reply, reply_to=msg_id)
        return {"ok": True}

    # Typing indicator
    send_action(s.telegram_bot_token, chat_id)

    # QA pipeline
    import time as _time

    from vks_intelligence.tools import qa_log
    _qa_start = _time.monotonic()
    _qa_log_dir = _qa_log_root(s)
    ict = timezone(timedelta(hours=7))
    session_day = datetime.now(ict).strftime("%Y-%m-%d")
    actor_id = user_id or username or chat_id
    session_id = f"tg-{chat_id}-{session_day}"

    from vks_intelligence.tools.agentbase_memory_tool import get_memory_tool
    _mem = get_memory_tool()

    # Lưu user message vào conversation memory
    if actor_id:
        _mem.save_event(actor_id, session_id, "user", text)

    # Nếu user xác nhận ("có/ok") sau khi bot đề xuất research → reroute
    _pending_key = actor_id or chat_id
    if _is_affirmative(text):
        _pending = _PENDING_RESEARCH.pop(_pending_key, None)
        if _pending:
            _stored_topic, _pts = _pending
            if _time.time() - _pts < 300:  # 5-min TTL
                text = f"refresh {_stored_topic} research"

    # Load user memory facts để enrich context cho streaming QA
    _user_facts: list[str] = _mem.search_user_memory(actor_id, text, limit=3) if actor_id else []
    _session_history = "\n".join(_user_facts) if _user_facts else ""

    from vks_intelligence.orchestrator import route as _route
    from vks_intelligence.specialists.qa_agent import QAAgent

    qa_agent = QAAgent(_router())
    _decision = _route(
        text,
        _router(),
        keyword_intent=lambda q: qa_agent.classify_intent(q).value,
        keyword_task=_research_task_for_question,
        keyword_force=_force_refresh_question,
    )
    if _decision.intent == "current_research":
        from vks_intelligence.tools.artifact_index import latest_fresh_artifact
        from vks_intelligence.tools.task_state_store import TaskStateStore

        state = TaskStateStore(s.workspace_path)
        active = state.get_by_actor(actor_id) if actor_id else None
        if active and active.get("status") == "running":
            _send_telegram_reply(
                s.telegram_bot_token,
                chat_id,
                state.build_status_reply(active),
                reply_to=msg_id,
                max_chars=s.telegram_max_chars_per_message,
            )
            return {"ok": True}

        if not _decision.force_refresh:
            research_task_type = _decision.task_type
            cached = latest_fresh_artifact(
                s.workspace_path / s.artifact_root,
                research_task_type,
                s.qa_current_research_cache_ttl_seconds,
            )
            if cached:
                summary = state.get_run_summary(str(cached.run_dir), max_chars=6_000)
                if summary:
                    finished_local = cached.finished_at.astimezone(ict).strftime("%Y-%m-%d %H:%M ICT")
                    cached_answer = (
                        f"{summary}\n\n"
                        f"_Dùng artifact {research_task_type.value} đã collect gần nhất: "
                        f"{finished_local}. Nhắn \"refresh lại\" nếu muốn chạy live research._"
                    )
                    _send_telegram_reply(
                        s.telegram_bot_token,
                        chat_id,
                        cached_answer,
                        reply_to=msg_id,
                        max_chars=s.telegram_max_chars_per_message,
                    )
                    return {"ok": True}

        placeholder_id = send_message(
            s.telegram_bot_token,
            chat_id,
            "🔍 🌼 Lin Lin 🌼 đang collect dữ liệu mới nhất và chạy research. Mình sẽ gửi kết quả ở tin nhắn tiếp theo.",
            reply_to=msg_id,
        )

        import threading

        _done = [False]
        _start_ts = _time.time()

        _STAGE_LABELS = {
            "starting": "khởi động",
            "collect_evidence": "thu thập dữ liệu",
            "run_agents": "chạy agents",
            "quality_gate": "kiểm tra chất lượng",
        }

        def _typing_loop() -> None:
            if _done[0]:
                return
            try:
                send_action(s.telegram_bot_token, chat_id)
            except Exception:
                pass
            threading.Timer(4.0, _typing_loop).start()

        def _heartbeat() -> None:
            if _done[0]:
                return
            try:
                from vks_intelligence.tools.telegram_tool import edit_message as _edit
                elapsed = int(_time.time() - _start_ts)
                m, sr = divmod(elapsed, 60)
                active = state.get_by_actor(actor_id) if actor_id else None
                stage = _STAGE_LABELS.get((active or {}).get("stage", ""), "đang xử lý")
                elapsed_str = f"{m} phút {sr}s" if m else f"{elapsed}s"
                if placeholder_id:
                    _edit(
                        s.telegram_bot_token, chat_id, placeholder_id,
                        f"🔄 🌼 Lin Lin 🌼 đang nghiên cứu...\n\n"
                        f"⏱️ Đã chạy: {elapsed_str}\n"
                        f"📋 Giai đoạn: {stage}\n\n"
                        "_Nhắn \"xong chưa?\" để xem tiến độ chi tiết_",
                    )
            except Exception:
                pass
            threading.Timer(60.0, _heartbeat).start()

        threading.Timer(2.0, _typing_loop).start()
        threading.Timer(45.0, _heartbeat).start()

        def _run_research_reply() -> None:
            _research_start = _time.monotonic()
            try:
                qa_resp = task_qa(QARequestBody(
                    question=text,
                    actor_id=actor_id,
                    session_id=session_id,
                    task_type_override=_decision.task_type.value,
                    force_refresh=_decision.force_refresh,
                ))
                _send_telegram_reply(
                    s.telegram_bot_token,
                    chat_id,
                    _format_telegram_qa_reply(qa_resp),
                    reply_to=msg_id,
                    max_chars=s.telegram_max_chars_per_message,
                )
                qa_log.record(
                    _qa_log_dir,
                    actor_id=actor_id,
                    intent="current_research",
                    latency_ms=(_time.monotonic() - _research_start) * 1000,
                    ok=True,
                    task_type=_decision.task_type.value,
                    routed_by=_decision.routed_by,
                )
            except Exception as exc:
                send_message(
                    s.telegram_bot_token,
                    chat_id,
                    f"Research gặp lỗi: {type(exc).__name__}: {str(exc)[:160]}",
                    reply_to=msg_id,
                )
                qa_log.record(
                    _qa_log_dir,
                    actor_id=actor_id,
                    intent="current_research",
                    latency_ms=(_time.monotonic() - _research_start) * 1000,
                    ok=False,
                    task_type=_decision.task_type.value,
                    routed_by=_decision.routed_by,
                )
            finally:
                _done[0] = True

        threading.Thread(target=_run_research_reply, daemon=True).start()
        return {"ok": True}

    from vks_intelligence.tools.telegram_tool import (
        edit_message,
        format_telegram_html_messages,
        stream_and_edit_message,
    )

    qa_agent_stream = QAAgent(_router())
    try:
        text_iter = qa_agent_stream.stream_answer_text(text, session_history=_session_history)
        streamed_text, placeholder_id = stream_and_edit_message(
            s.telegram_bot_token,
            chat_id,
            text_iter,
            reply_to=msg_id,
        )
        if streamed_text.strip() and placeholder_id:
            chunks = format_telegram_html_messages(streamed_text, s.telegram_max_chars_per_message)
            edit_message(s.telegram_bot_token, chat_id, placeholder_id, chunks[0], parse_mode="HTML")
            for extra in chunks[1:]:
                from vks_intelligence.tools.telegram_tool import send_message as _tg_send
                _tg_send(s.telegram_bot_token, chat_id, extra, parse_mode="HTML")
            # Lưu assistant response + trích xuất long-term facts + detect research offer
            if actor_id:
                _mem.save_event(actor_id, session_id, "assistant", streamed_text[:2000])
                _mem.generate_records(actor_id, session_id)
            if _contains_research_offer(streamed_text):
                _PENDING_RESEARCH[_pending_key] = (text, _time.time())
        elif not streamed_text.strip():
            raise ValueError("streaming trả về rỗng")
        qa_log.record(
            _qa_log_dir,
            actor_id=actor_id,
            intent="memory_lookup",
            latency_ms=(_time.monotonic() - _qa_start) * 1000,
            ok=True,
            routed_by=_decision.routed_by,
        )
    except Exception as stream_exc:
        import logging as _log
        _log.getLogger(__name__).warning("Streaming QA thất bại (%s) — fallback sang task_qa", stream_exc)
        qa_resp = task_qa(QARequestBody(
            question=text,
            actor_id=actor_id,
            session_id=session_id,
        ))
        _send_telegram_reply(
            s.telegram_bot_token,
            chat_id,
            _format_telegram_qa_reply(qa_resp),
            reply_to=msg_id,
            max_chars=s.telegram_max_chars_per_message,
        )
        qa_log.record(
            _qa_log_dir,
            actor_id=actor_id,
            intent="memory_lookup",
            latency_ms=(_time.monotonic() - _qa_start) * 1000,
            ok=True,
            fallback=True,
            routed_by=_decision.routed_by,
        )
    return {"ok": True}


@app.post("/telegram/set-webhook")
def telegram_set_webhook(body: dict) -> dict:
    """Helper: gọi Telegram setWebhook API với URL cung cấp."""
    import httpx
    from vks_intelligence.config import get_settings

    s = get_settings()
    if not s.telegram_bot_token:
        raise HTTPException(status_code=503, detail="TELEGRAM_BOT_TOKEN chưa set")
    url = body.get("url", "")
    if not url:
        raise HTTPException(status_code=422, detail="url là bắt buộc")

    resp = httpx.post(
        f"https://api.telegram.org/bot{s.telegram_bot_token}/setWebhook",
        json={"url": url, "allowed_updates": ["message", "channel_post"]},
        timeout=10,
    )
    return resp.json()


# ──────────────────────────────────────────────────────────────────
# Dashboard UI — serve HTML trực tiếp, không dùng StaticFiles mount
# ──────────────────────────────────────────────────────────────────

from fastapi.responses import FileResponse as _FileResponse  # noqa: E402


@app.get("/dashboard/ui", include_in_schema=False)
@app.get("/dashboard/ui/", include_in_schema=False)
def dashboard_ui() -> _FileResponse:
    html = Path(__file__).parent / "static" / "index.html"
    if not html.exists():
        raise HTTPException(status_code=404, detail="Dashboard UI chưa được build")
    return _FileResponse(str(html), media_type="text/html")
