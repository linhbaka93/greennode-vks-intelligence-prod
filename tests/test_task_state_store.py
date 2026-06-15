from pathlib import Path

from vks_intelligence.tools.task_state_store import TaskStateStore


def test_task_state_lifecycle_returns_completed_summary(tmp_path: Path):
    store = TaskStateStore(tmp_path)
    run_dir = tmp_path / "outputs" / "runs" / "run-123"
    run_dir.mkdir(parents=True)
    (run_dir / "final.md").write_text("Tóm tắt research đã hoàn tất.", encoding="utf-8")

    store.upsert(
        actor_id="user-1",
        session_id="tg-1-2026-06-02",
        run_id="qa-research-abc",
        task_type="daily-intelligence",
        stage="collect_evidence",
        artifact_path=str(run_dir),
    )
    active = store.get_by_actor("user-1")
    assert active is not None
    assert active["status"] == "running"

    store.complete("qa-research-abc", str(run_dir))
    completed = store.get_by_actor("user-1")
    assert completed is not None
    assert completed["status"] == "completed"
    assert "Research xong" in store.build_status_reply(completed)
    assert "Tóm tắt research" in store.build_status_reply(completed)


def test_task_state_fail_marks_actor_task_failed(tmp_path: Path):
    store = TaskStateStore(tmp_path)
    store.upsert("user-1", "session-1", "run-1", "qa")

    store.fail("run-1", "model timeout")

    active = store.get_by_actor("user-1")
    assert active is not None
    assert active["status"] == "failed"
    assert "model timeout" in store.build_status_reply(active)
