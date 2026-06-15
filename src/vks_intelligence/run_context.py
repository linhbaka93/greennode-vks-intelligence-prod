"""State và budget cho một lần chạy task.

Giữ deadline phân tầng (run → agent → model), đếm token/agent đã dùng, và tích
luỹ fallback trace. Mọi tầng đọc deadline từ đây thay vì tự tính timeout.
"""

from __future__ import annotations

import time
from dataclasses import dataclass, field

from vks_intelligence.contracts import BudgetPolicy, FallbackTrace, TaskRequest


@dataclass
class RunContext:
    request: TaskRequest
    run_id: str
    budget: BudgetPolicy
    started_monotonic: float = 0.0
    agents_used: int = 0
    input_tokens: int = 0
    output_tokens: int = 0
    fallbacks: list[FallbackTrace] = field(default_factory=list)

    def __post_init__(self) -> None:
        if self.started_monotonic == 0.0:
            self.started_monotonic = time.monotonic()

    def run_deadline(self) -> float:
        from vks_intelligence.llm.budgets import budget_for

        timeout = self.request.timeout_seconds or budget_for(self.request.task_type).run_timeout_seconds
        return self.started_monotonic + timeout

    def agent_deadline(self) -> float:
        return min(
            self.run_deadline(),
            time.monotonic() + self.budget.max_agent_seconds,
        )

    def remaining_seconds(self) -> float:
        return max(0.0, self.run_deadline() - time.monotonic())

    def can_spawn_agent(self) -> bool:
        return self.agents_used < self.budget.max_agents

    def record_usage(self, input_tokens: int, output_tokens: int) -> None:
        self.input_tokens += input_tokens
        self.output_tokens += output_tokens

    def record_fallback(self, trace: FallbackTrace) -> None:
        self.fallbacks.append(trace)
