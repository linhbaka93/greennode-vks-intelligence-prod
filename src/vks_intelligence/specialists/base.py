"""Lớp cha cho mọi specialist agent.

Một specialist: nạp system prompt tiếng Việt từ `prompts/`, gọi model qua router,
ép output qua json_guard, và trả AgentResult đã validate. Specialist không tự
quyết định publish — đó là việc của supervisor.
"""

from __future__ import annotations

from pathlib import Path
import json

from vks_intelligence.contracts import AgentResult, AgentStatus, AgentTask
from vks_intelligence.llm.base import LLMRequest
from vks_intelligence.llm.router import ModelRouter, Workload
from vks_intelligence.run_context import RunContext

def _find_prompts_dir() -> Path:
    current = Path(__file__).resolve()
    for parent in current.parents:
        candidate = parent / "prompts"
        if (candidate / "_output_policy.md").exists():
            return candidate
    return current.parents[3] / "prompts"


_PROMPTS_DIR = _find_prompts_dir()


class Specialist:
    name: str = ""
    prompt_file: str = ""
    workload: Workload = Workload.RESEARCH

    def __init__(self, router: ModelRouter) -> None:
        self.router = router

    def load_prompt(self) -> str:
        """Đọc prompt partial chung và system prompt riêng từ prompts/."""
        shared_paths = [
            _PROMPTS_DIR / "_output_policy.md",
            _PROMPTS_DIR / "_social_sources.md",
        ]
        spec_path = _PROMPTS_DIR / self.prompt_file

        parts: list[str] = []
        for shared_path in shared_paths:
            if shared_path.exists():
                parts.append(shared_path.read_text(encoding="utf-8"))
        if spec_path.exists():
            parts.append(spec_path.read_text(encoding="utf-8"))

        if parts:
            return "\n\n---\n\n".join(parts)
        return f"Bạn là {self.name}. Trả lời bằng tiếng Việt, executive-readable."

    def run(self, task: AgentTask, context: RunContext) -> AgentResult:
        """Chạy agent end-to-end và trả AgentResult structured."""
        from vks_intelligence.config import get_settings
        from vks_intelligence.llm.json_guard import parse_into
        from vks_intelligence.tools.memory_tool import load_memory

        s = get_settings()
        system = self.load_prompt()
        memory = load_memory(s.workspace_path)

        user_parts = [f"## Nhiệm vụ\n{task.instruction}"]
        if task.inputs:
            user_parts.append(
                f"## Inputs bổ sung\n{json.dumps(task.inputs, ensure_ascii=False, indent=2)}"
            )
        user_parts.append(f"## Workspace Memory\n{memory}")
        user_msg = "\n\n".join(user_parts)

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
                gaps=["Agent output không đúng schema; cần review prompt/schema hoặc model response."],
                json_parse_status="failed",
            )

        result.agent = self.name
        result.task_id = task.task_id
        result.model_used = response.model
        result.input_tokens = response.input_tokens
        result.output_tokens = response.output_tokens
        return result
