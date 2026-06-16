"""Q&A Agent — trả lời nhanh từ workspace memory, có confidence và escalation.

Nguồn dữ liệu duy nhất là memory đã nạp; mọi claim phải gắn nhãn. Trả lời tiếng
Việt, tối đa ~250 từ. Confidence thấp → đánh dấu escalate để supervisor mở
research task thay vì trả lời bừa.
"""

from __future__ import annotations

from collections.abc import Iterator

from pydantic import BaseModel

from vks_intelligence.contracts import AgentResult, AgentStatus, AgentTask, QAEscalationIntent
from vks_intelligence.llm.base import LLMRequest
from vks_intelligence.llm.router import Workload
from vks_intelligence.registry import register
from vks_intelligence.run_context import RunContext
from vks_intelligence.specialists.base import Specialist

_CURRENT_KEYWORDS = (
    "hôm nay", "hôm qua", "tuần này", "tháng này", "mới nhất",
    "gần đây", "latest", "recent", "hiện tại", "hiện nay", "vừa",
    "just", "today", "this week", "current", "update",
    "research", "tìm hiểu", "tim hieu", "mở research", "mo research",
    "cập nhật", "cap nhat",
    "refresh", "chạy lại", "chay lai",
    "đào sâu", "dao sau", "phân tích sâu", "phan tich sau",
)


class _QAOut(BaseModel):
    answer: str = ""
    confidence: str = "medium"
    escalated: bool = False
    sources: list[str] = []


@register("qa_agent")
class QAAgent(Specialist):
    name = "qa_agent"
    prompt_file = "qa_agent.md"
    workload = Workload.QA

    def classify_intent(self, question: str) -> QAEscalationIntent:
        """Phân loại câu hỏi: cần memory hay cần dữ liệu mới nhất."""
        q = question.lower()
        if any(kw in q for kw in _CURRENT_KEYWORDS):
            return QAEscalationIntent.CURRENT_RESEARCH
        return QAEscalationIntent.MEMORY_LOOKUP

    def assess_confidence(self, question: str, memory: str, answer: str) -> tuple[str, bool]:
        """Trả (confidence, escalate) dựa trên độ phủ của memory với câu hỏi."""
        if not memory or len(memory.strip()) < 100:
            return "low", True
        q_lower = question.lower()
        keywords = [w for w in q_lower.split() if len(w) > 4]
        if not keywords:
            return "medium", False
        mem_lower = memory.lower()
        found = sum(1 for kw in keywords if kw in mem_lower)
        ratio = found / len(keywords)
        if ratio >= 0.7:
            return "high", False
        if ratio > 0:
            return "medium", False
        return "low", True

    def answer(self, question: str, context: RunContext) -> tuple[str, str, bool, list[str]]:
        """Trả (answer, confidence, escalated, sources) cho endpoint /tasks/qa.

        Fast-path nếu câu hỏi không cần dữ liệu mới; không gọi external tools.
        """
        from vks_intelligence.config import get_settings
        from vks_intelligence.llm.json_guard import parse_into
        from vks_intelligence.tools.memory_tool import load_memory

        s = get_settings()
        system = self.load_prompt()
        memory = load_memory(s.workspace_path, context_cap=8_000)

        user_msg = f"## Câu hỏi\n{question}\n\n## Workspace Memory\n{memory}"
        user_memory = context.request.payload.get("user_memory_context", "")
        if user_memory:
            user_msg += f"\n\n## User Conversation Memory\n{user_memory}"
        req = LLMRequest(
            model="",
            system=system,
            user=user_msg,
            max_output_tokens=1_500,
            response_json=True,
            timeout_seconds=s.model_timeout_seconds,
        )
        response = self.router.complete(self.workload, req, context)

        try:
            out = parse_into(response.text, _QAOut)
        except Exception:
            out = _QAOut(
                answer=(
                    "🌼 Lin Lin 🌼 nhận được phản hồi không đúng định dạng từ model, "
                    "nên chưa thể trả lời chắc chắn. Bạn thử hỏi lại hoặc yêu cầu refresh nhé."
                ),
                confidence="low",
                escalated=True,
            )

        return out.answer, out.confidence, out.escalated, out.sources

    def stream_answer_text(self, question: str, session_history: str = "") -> Iterator[str]:
        """Yield streaming plain-text answer chunks cho Telegram direct reply.

        Dùng MEMORY_LOOKUP fast-path: không JSON mode, không RunContext, không qua supervisor.
        session_history: các fact/context từ conversation memory trước đó.
        Caller chịu trách nhiệm format final output (HTML, chunking).
        """
        from vks_intelligence.config import get_settings
        from vks_intelligence.tools.memory_tool import load_memory

        s = get_settings()
        system = (
            self.load_prompt()
            + "\n\n---\n"
            "STREAMING MODE: Trả lời trực tiếp bằng văn bản thuần túy, không JSON. "
            "Gắn nhãn claim như thường lệ. Tối đa ~250 từ."
        )
        memory = load_memory(s.workspace_path, context_cap=8_000)
        user_msg = f"## Câu hỏi\n{question}\n\n## Workspace Memory\n{memory}"
        if session_history:
            user_msg += f"\n\n## Lịch sử hội thoại gần đây\n{session_history}"

        req = LLMRequest(
            model="",
            system=system,
            user=user_msg,
            max_output_tokens=1_500,
            temperature=0.2,
            timeout_seconds=s.model_timeout_seconds,
            response_json=False,
        )
        yield from self.router.stream_complete(self.workload, req)

    def run(self, task: AgentTask, context: RunContext) -> AgentResult:
        """Chạy trong supervisor pipeline (research escalation path)."""
        from vks_intelligence.config import get_settings
        from vks_intelligence.llm.json_guard import parse_into
        from vks_intelligence.tools.memory_tool import load_memory

        s = get_settings()
        system = self.load_prompt()
        memory = load_memory(s.workspace_path, context_cap=8_000)
        question = task.inputs.get("question", task.instruction)

        user_msg = f"## Câu hỏi\n{question}\n\n## Workspace Memory\n{memory}"
        user_memory = context.request.payload.get("user_memory_context", "")
        if user_memory:
            user_msg += f"\n\n## User Conversation Memory\n{user_memory}"
        if task.inputs.get("evidence_context"):
            user_msg += f"\n\n## Evidence mới nhất\n{task.inputs['evidence_context']}"

        req = LLMRequest(
            model="",
            system=system,
            user=user_msg,
            max_output_tokens=1_500,
            response_json=True,
            timeout_seconds=s.model_timeout_seconds,
        )
        response = self.router.complete(self.workload, req, context)

        try:
            out = parse_into(response.text, _QAOut)
        except Exception:
            out = _QAOut(
                answer=(
                    "QA agent nhận được output không đúng schema; "
                    "đã loại raw output khỏi câu trả lời."
                ),
                confidence="low",
                escalated=True,
            )

        return AgentResult(
            agent=self.name,
            task_id=task.task_id,
            status=AgentStatus.OK,
            summary=out.answer,
            key_findings=[out.answer] if out.answer else [],
            recommended_actions=out.sources,
            model_used=response.model,
            input_tokens=response.input_tokens,
            output_tokens=response.output_tokens,
        )
