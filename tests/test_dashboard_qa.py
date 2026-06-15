import json
from pathlib import Path

from vks_intelligence.dashboard import cost_trend, qa_activity, run_detail
from vks_intelligence.tools import qa_log


def test_qa_log_record_and_read_roundtrip(tmp_path: Path):
    qa_log.record(tmp_path, actor_id="u1", intent="memory_lookup", latency_ms=1200)
    qa_log.record(tmp_path, actor_id="u2", intent="current_research", latency_ms=8000, ok=True)

    events = qa_log.read_events(tmp_path)
    assert len(events) == 2
    assert {e["intent"] for e in events} == {"memory_lookup", "current_research"}


def test_qa_activity_aggregates_intents_and_latency(tmp_path: Path):
    qa_log.record(tmp_path, actor_id="u1", intent="memory_lookup", latency_ms=1000, routed_by="llm")
    qa_log.record(tmp_path, actor_id="u1", intent="memory_lookup", latency_ms=3000, fallback=True, routed_by="keyword")
    qa_log.record(tmp_path, actor_id="u2", intent="current_research", latency_ms=5000,
                  routed_by="llm", task_type="battlecard")

    activity = qa_activity(tmp_path)

    assert activity.total_qa == 3
    assert activity.memory_lookup == 2
    assert activity.current_research == 1
    assert activity.fallback_count == 1
    assert activity.avg_latency_ms == 3000.0
    assert activity.by_routed_by == {"keyword": 1, "llm": 2}
    assert activity.by_task_type == {"battlecard": 1}


def test_qa_activity_empty_when_no_log(tmp_path: Path):
    activity = qa_activity(tmp_path / "missing")
    assert activity.total_qa == 0
    assert activity.avg_latency_ms is None


def test_cost_trend_groups_tokens_by_day(tmp_path: Path):
    days = ["2026-06-01T10:00:00Z", "2026-06-01T12:00:00Z", "2026-06-02T09:00:00Z"]
    for idx, finished in enumerate(days):
        run_dir = tmp_path / f"run-{idx}"
        run_dir.mkdir()
        (run_dir / "metadata.json").write_text(
            json.dumps({
                "run_id": f"run-{idx}",
                "task_id": f"task-{idx}",
                "task_type": "qa",
                "status": "completed",
                "input_tokens": 100,
                "output_tokens": 50,
                "finished_at": finished,
            }),
            encoding="utf-8",
        )

    points = cost_trend(tmp_path)

    assert [p.date for p in points] == ["2026-06-01", "2026-06-02"]
    assert points[0].input_tokens == 200
    assert points[0].output_tokens == 100
    assert points[0].runs == 2
    assert points[1].runs == 1


def test_run_detail_reads_agents_and_quality(tmp_path: Path):
    run_dir = tmp_path / "2026-06-08T100000_battlecard_abc12345"
    run_dir.mkdir()
    (run_dir / "metadata.json").write_text(
        json.dumps({
            "run_id": run_dir.name,
            "task_id": "req-1",
            "task_type": "battlecard",
            "status": "completed",
            "quality_score": 0.86,
            "input_tokens": 1000,
            "output_tokens": 400,
            "agents": ["competitor_agent", "battlecard_agent"],
            "models": {"competitor_agent": "qwen", "battlecard_agent": "gemma"},
            "fallbacks": [{"from_model": "gemma", "to_model": "qwen"}],
            "finished_at": "2026-06-08T10:05:00Z",
        }),
        encoding="utf-8",
    )
    (run_dir / "competitor_agent.json").write_text(
        json.dumps({"status": "ok", "model_used": "qwen", "input_tokens": 600,
                    "output_tokens": 200, "json_parse_status": "valid", "summary": "ok"}),
        encoding="utf-8",
    )
    (run_dir / "quality.json").write_text(
        json.dumps({"verdict": "pass", "score": 0.86, "failures": [], "warnings": ["w1"]}),
        encoding="utf-8",
    )
    (run_dir / "final.md").write_text("# Battlecard\nNội dung", encoding="utf-8")

    detail = run_detail(tmp_path, run_dir.name)

    assert detail is not None
    assert detail.task_type == "battlecard"
    assert len(detail.agents) == 2
    assert detail.agents[0].agent == "competitor_agent"
    assert detail.agents[0].input_tokens == 600
    assert detail.fallbacks == ["gemma→qwen"]
    assert detail.quality_verdict == "pass"
    assert detail.synthesis_preview.startswith("# Battlecard")


def test_run_detail_missing_returns_none(tmp_path: Path):
    assert run_detail(tmp_path, "khong-ton-tai") is None
