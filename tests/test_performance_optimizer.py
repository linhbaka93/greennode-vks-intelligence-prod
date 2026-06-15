import json
from datetime import datetime, timezone
from pathlib import Path
from types import SimpleNamespace

from vks_intelligence.contracts import EvidenceBundle, TaskRequest, TaskType
from vks_intelligence.schemas import QARequestBody
from vks_intelligence.tools.artifact_index import latest_fresh_artifact
from vks_intelligence.tools.task_state_store import TaskStateStore


class _FakeMemory:
    def save_event(self, *args, **kwargs):
        return None

    def search_user_memory(self, *args, **kwargs):
        return []

    def generate_records(self, *args, **kwargs):
        return None


def _settings(tmp_path: Path):
    return SimpleNamespace(
        workspace_path=tmp_path,
        artifact_root=Path("outputs/runs"),
        qa_current_research_cache_ttl_seconds=21_600,
        evidence_interactive_max_targets=6,
        enable_social_scrape=False,
    )


def _write_run(root: Path, run_id: str, task_type: TaskType, content: str) -> Path:
    run_dir = root / "outputs" / "runs" / run_id
    run_dir.mkdir(parents=True)
    (run_dir / "metadata.json").write_text(
        json.dumps({
            "run_id": run_id,
            "task_id": run_id,
            "task_type": task_type.value,
            "status": "completed",
            "finished_at": datetime.now(timezone.utc).isoformat(),
        }),
        encoding="utf-8",
    )
    (run_dir / "final.md").write_text(content, encoding="utf-8")
    return run_dir


def test_latest_fresh_artifact_returns_completed_run(tmp_path: Path):
    run_dir = _write_run(tmp_path, "daily-run", TaskType.DAILY_INTELLIGENCE, "fresh daily")

    hit = latest_fresh_artifact(tmp_path / "outputs" / "runs", TaskType.DAILY_INTELLIGENCE, 21_600)

    assert hit is not None
    assert hit.run_dir == run_dir


def test_current_research_uses_fresh_artifact_without_live_supervisor(monkeypatch, tmp_path: Path):
    _write_run(tmp_path, "daily-run", TaskType.DAILY_INTELLIGENCE, "cached daily answer")

    monkeypatch.setattr("vks_intelligence.config.get_settings", lambda: _settings(tmp_path))
    monkeypatch.setattr(
        "vks_intelligence.tools.agentbase_memory_tool.get_memory_tool",
        lambda: _FakeMemory(),
    )
    monkeypatch.setattr("vks_intelligence.api._router", lambda: object())
    monkeypatch.setattr(
        "vks_intelligence.api._supervisor",
        lambda: (_ for _ in ()).throw(AssertionError("supervisor should not run")),
    )

    from vks_intelligence.api import task_qa

    resp = task_qa(QARequestBody(
        question="VKS có cập nhật gì mới hôm nay",
        actor_id="tg-1",
        session_id="s-1",
    ))

    assert "cached daily answer" in resp.answer
    assert resp.confidence == "high"
    assert resp.research_used is True


def test_current_research_active_task_guard_skips_new_supervisor(monkeypatch, tmp_path: Path):
    store = TaskStateStore(tmp_path)
    store.upsert("tg-1", "s-1", "run-active", "daily-intelligence", stage="collect_evidence")

    monkeypatch.setattr("vks_intelligence.config.get_settings", lambda: _settings(tmp_path))
    monkeypatch.setattr(
        "vks_intelligence.tools.agentbase_memory_tool.get_memory_tool",
        lambda: _FakeMemory(),
    )
    monkeypatch.setattr("vks_intelligence.api._router", lambda: object())
    monkeypatch.setattr(
        "vks_intelligence.api._supervisor",
        lambda: (_ for _ in ()).throw(AssertionError("supervisor should not run")),
    )

    from vks_intelligence.api import task_qa

    resp = task_qa(QARequestBody(
        question="VKS có gì mới hôm nay",
        actor_id="tg-1",
        session_id="s-1",
    ))

    assert "đang xử lý research task" in resp.answer
    assert resp.research_used is True


def _interactive_collect_capture(monkeypatch, tmp_path: Path, enable_social: bool) -> dict:
    captured = {}

    def fake_collect(workspace_path, **kwargs):
        captured.update(kwargs)
        return EvidenceBundle()

    settings = _settings(tmp_path)
    settings.enable_social_scrape = enable_social
    monkeypatch.setattr("vks_intelligence.config.get_settings", lambda: settings)
    monkeypatch.setattr("vks_intelligence.tools.evidence_tool.collect", fake_collect)

    from vks_intelligence.supervisor import _collect_evidence

    _collect_evidence(
        TaskRequest(
            request_id="qa-live",
            task_type=TaskType.DAILY_INTELLIGENCE,
            source="qa-research",
            payload={"interactive": True},
        ),
        tmp_path,
    )
    return captured


def test_interactive_collect_uses_capped_social_scope(monkeypatch, tmp_path: Path):
    captured = _interactive_collect_capture(monkeypatch, tmp_path, enable_social=True)

    assert captured["include_scrape"] is True
    assert len(captured["scrape_targets"]) <= 6
    assert "greennode-facebook" in captured["scrape_targets"]
    assert "aws-x" not in captured["scrape_targets"]


def test_interactive_collect_skips_social_when_parked(monkeypatch, tmp_path: Path):
    captured = _interactive_collect_capture(monkeypatch, tmp_path, enable_social=False)

    assert captured["scrape_targets"] == []
    assert captured["include_scrape"] is False
