import json
from pathlib import Path

from vks_intelligence.contracts import BudgetPolicy, TaskRequest, TaskType
from vks_intelligence.dashboard import summary
from vks_intelligence.run_context import RunContext


def test_run_context_defaults_to_task_type_timeout():
    request = TaskRequest(request_id="qa-1", task_type=TaskType.QA)
    context = RunContext(
        request=request,
        run_id="qa-1",
        budget=BudgetPolicy(max_agents=1, max_agent_seconds=20),
    )

    assert 29 <= context.run_deadline() - context.started_monotonic <= 31


def test_dashboard_summary_uses_all_runs_when_limit_is_zero(tmp_path: Path):
    for idx in range(2):
        run_dir = tmp_path / f"run-{idx}"
        run_dir.mkdir()
        (run_dir / "metadata.json").write_text(
            json.dumps({
                "run_id": f"run-{idx}",
                "task_id": f"task-{idx}",
                "task_type": "qa",
                "status": "completed",
                "quality_score": 0.9,
                "input_tokens": 10,
                "output_tokens": 5,
                "published": True,
                "finished_at": "2026-06-02T00:00:00Z",
            }),
            encoding="utf-8",
        )

    dashboard = summary(tmp_path)

    assert dashboard.total_runs == 2
    assert dashboard.runs_published == 2
    assert dashboard.total_input_tokens == 20
