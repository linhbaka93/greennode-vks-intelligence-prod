"""Daily Intelligence Agent — brief/alert hằng ngày từ RSS + scrape allowlist.

Nhận EvidenceBundle (đã collect từ evidence_tool), lọc tín hiệu trong 24-48h,
và tạo daily brief ngắn gọn. Không dùng paid search trong milestone đầu.
"""

from __future__ import annotations

import json

from vks_intelligence.contracts import AgentResult, AgentStatus, AgentTask, EvidenceBundle
from vks_intelligence.llm.base import LLMRequest
from vks_intelligence.llm.router import Workload
from vks_intelligence.registry import register
from vks_intelligence.run_context import RunContext
from vks_intelligence.specialists.base import Specialist


@register("daily_intelligence_agent")
class DailyIntelligenceAgent(Specialist):
    name = "daily_intelligence_agent"
    prompt_file = "daily_intelligence_agent.md"
    workload = Workload.RESEARCH

    def run(self, task: AgentTask, context: RunContext) -> AgentResult:
        from vks_intelligence.config import get_settings
        from vks_intelligence.llm.json_guard import parse_into

        s = get_settings()
        system = self.load_prompt()

        # Lấy evidence bundle từ inputs nếu có
        bundle_data = task.inputs.get("evidence_bundle")
        evidence_text = ""
        if bundle_data:
            try:
                bundle = EvidenceBundle.model_validate(bundle_data)
                items_text = "\n".join(
                    f"- [{i.published_at[:10] if i.published_at else '?'}] "
                    f"{i.source_label or '[' + i.evidence_type.value.upper() + ']'} "
                    f"{i.title} | {i.publisher} | {i.url} | retrieved_at={i.retrieved_at}"
                    for i in bundle.items[:40]
                )
                evidence_text = (
                    f"## Evidence mới nhất ({bundle.days_window} ngày)\n{items_text}\n\n"
                    f"## Workspace Memory\n{bundle.memory_context[:4_000]}"
                )
                if bundle.warnings:
                    evidence_text += f"\n\n⚠️ Warnings: {'; '.join(bundle.warnings)}"
            except Exception:
                evidence_text = json.dumps(bundle_data, ensure_ascii=False)[:2_000]

        user_msg = (
            f"## Nhiệm vụ\n{task.instruction}\n\n"
            + (evidence_text or f"## Workspace Memory\n{task.inputs.get('memory_context', '')}")
        )

        req = LLMRequest(
            model="",
            system=system,
            user=user_msg,
            max_output_tokens=s.max_output_tokens_worker,
            response_json=True,
            timeout_seconds=s.model_timeout_seconds,
        )

        response = self.router.complete(self.workload, req, context)

        try:
            result = parse_into(response.text, AgentResult)
        except Exception:
            result = AgentResult(
                agent=self.name,
                task_id=task.task_id,
                status=AgentStatus.PARTIAL,
                summary="Agent output không đúng schema; raw output đã bị loại khỏi bản tin.",
                key_findings=[],
                gaps=["Daily agent output không đúng schema; cần review prompt/schema hoặc model response."],
                json_parse_status="failed",
            )

        result.agent = self.name
        result.task_id = task.task_id
        result.model_used = response.model
        result.input_tokens = response.input_tokens
        result.output_tokens = response.output_tokens
        return result
