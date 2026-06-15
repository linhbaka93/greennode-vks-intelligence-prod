"""Orchestrator routing — phân loại câu hỏi Telegram thành quyết định routing.

Thay keyword routing (brittle) bằng một LLM call (Gemma) trả JSON intent/task_type/
force_refresh. LLM lỗi hoặc JSON hỏng → fallback deterministic keyword, không bao giờ
crash request path. Orchestrator KHÔNG sinh AgentResult, chỉ quyết định routing.
"""

from __future__ import annotations

import logging
from collections.abc import Callable
from dataclasses import dataclass

from pydantic import BaseModel

from vks_intelligence.contracts import TaskType

log = logging.getLogger(__name__)

_VALID_TASK_TYPES = {
    TaskType.DAILY_INTELLIGENCE,
    TaskType.WEEKLY_DIGEST,
    TaskType.COMPETITOR_MONITOR,
    TaskType.PRICING_ANALYSIS,
    TaskType.BATTLECARD,
}


@dataclass
class RouteDecision:
    intent: str               # "memory_lookup" | "current_research"
    task_type: TaskType       # research task khi intent = current_research
    force_refresh: bool       # bypass cache
    routed_by: str            # "llm" | "keyword"
    reasoning: str = ""


class _OrchestratorOut(BaseModel):
    intent: str = "memory_lookup"
    task_type: str = "daily-intelligence"
    force_refresh: bool = False
    reasoning: str = ""


def route(
    question: str,
    router,
    *,
    keyword_intent: Callable[[str], str],
    keyword_task: Callable[[str], tuple[TaskType, int]],
    keyword_force: Callable[[str], bool],
) -> RouteDecision:
    """Quyết định routing: LLM orchestrator trước, keyword fallback khi lỗi.

    keyword_* là callable deterministic dùng khi LLM fail — đảm bảo không regression.
    """
    try:
        decision = _llm_route(question, router)
        if decision is not None:
            return decision
    except Exception as exc:
        log.warning("Orchestrator LLM route lỗi (%s) — fallback keyword", exc)

    task_type, _days = keyword_task(question)
    return RouteDecision(
        intent=keyword_intent(question),
        task_type=task_type,
        force_refresh=keyword_force(question),
        routed_by="keyword",
    )


def _llm_route(question: str, router) -> RouteDecision | None:
    from vks_intelligence.llm.base import LLMRequest
    from vks_intelligence.llm.json_guard import parse_into
    from vks_intelligence.llm.router import Workload
    from vks_intelligence.specialists.base import _PROMPTS_DIR

    prompt_path = _PROMPTS_DIR / "_orchestrator.md"
    if not prompt_path.exists():
        return None
    system = prompt_path.read_text(encoding="utf-8")

    req = LLMRequest(
        model="",
        system=system,
        user=f"Câu hỏi người dùng:\n{question}",
        max_output_tokens=300,
        temperature=0.0,
        response_json=True,
    )
    resp = router.complete_once(Workload.ORCHESTRATOR, req)
    out = parse_into(resp.text, _OrchestratorOut)

    intent = "current_research" if out.intent.strip().lower() == "current_research" else "memory_lookup"
    try:
        task_type = TaskType(out.task_type.strip())
    except ValueError:
        task_type = TaskType.DAILY_INTELLIGENCE
    if task_type not in _VALID_TASK_TYPES:
        task_type = TaskType.DAILY_INTELLIGENCE

    return RouteDecision(
        intent=intent,
        task_type=task_type,
        force_refresh=bool(out.force_refresh),
        routed_by="llm",
        reasoning=out.reasoning[:200],
    )
