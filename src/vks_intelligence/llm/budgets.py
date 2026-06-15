"""Budget mặc định theo workload.

Bốn tầng budget: run, agent, model, publish. Giá trị ở đây là default an toàn;
Settings có thể override qua env. Agent không tự định nghĩa budget riêng.
"""

from __future__ import annotations

from dataclasses import dataclass

from vks_intelligence.contracts import TaskType


@dataclass(frozen=True)
class WorkloadBudget:
    max_agents: int
    run_timeout_seconds: int
    agent_timeout_seconds: int
    max_retries: int
    max_input_tokens: int
    max_output_tokens: int


WORKLOAD_BUDGETS: dict[TaskType, WorkloadBudget] = {
    TaskType.QA: WorkloadBudget(1, 30, 20, 1, 20_000, 1_500),
    TaskType.DAILY_INTELLIGENCE: WorkloadBudget(3, 180, 90, 2, 80_000, 3_000),
    TaskType.WEEKLY_DIGEST: WorkloadBudget(5, 480, 120, 2, 160_000, 6_000),
    TaskType.MONTHLY_BRIEF: WorkloadBudget(6, 720, 150, 2, 220_000, 8_000),
    TaskType.COMPETITOR_MONITOR: WorkloadBudget(4, 300, 90, 2, 120_000, 4_000),
    TaskType.PRICING_ANALYSIS: WorkloadBudget(3, 300, 120, 2, 120_000, 4_000),
    TaskType.BATTLECARD: WorkloadBudget(4, 420, 120, 2, 120_000, 4_000),
    TaskType.MEMORY_MAINTENANCE: WorkloadBudget(3, 360, 120, 1, 120_000, 4_000),
}


def budget_for(task_type: TaskType) -> WorkloadBudget:
    return WORKLOAD_BUDGETS[task_type]
