import json
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

from fastapi import FastAPI
from fastapi.testclient import TestClient

from vks_intelligence.config import Settings
from vks_intelligence import scheduler as sched_mod
from vks_intelligence.scheduler import (
    JOBS,
    _already_ran_today,
    _job_wrapper,
    attach_scheduler,
    run_job_now,
)

_ICT = ZoneInfo("Asia/Ho_Chi_Minh")


def _settings(tmp_path: Path | None = None, **overrides) -> Settings:
    kwargs = {"_env_file": None}
    if tmp_path is not None:
        kwargs["workspace_path"] = tmp_path
    kwargs.update(overrides)
    return Settings(**kwargs)


def test_attach_noop_when_disabled(monkeypatch):
    s = _settings(scheduler_enabled=False)
    monkeypatch.setattr("vks_intelligence.config.get_settings", lambda: s)

    app = FastAPI()
    attach_scheduler(app)

    paths = {r.path for r in app.routes}
    assert "/scheduler/status" in paths
    assert "/scheduler/run/{job_name}" in paths
    assert sched_mod._scheduler is None


def test_cron_defaults_fire_at_correct_times():
    from apscheduler.triggers.cron import CronTrigger

    s = _settings()
    # Thứ 2 2026-06-08 → fire kế tiếp của weekly phải là thứ 6 2026-06-12 15:00 ICT
    now = datetime(2026, 6, 8, 0, 0, tzinfo=_ICT)
    trigger = CronTrigger.from_crontab(s.cron_weekly_digest, timezone=_ICT)
    nxt = trigger.get_next_fire_time(None, now)
    assert nxt == datetime(2026, 6, 12, 15, 0, tzinfo=_ICT)

    # Daily intelligence chạy lúc 08:00 ICT
    daily = CronTrigger.from_crontab(s.cron_daily_intelligence, timezone=_ICT)
    nxt_daily = daily.get_next_fire_time(None, now)
    assert (nxt_daily.hour, nxt_daily.minute) == (8, 0)

    monthly = CronTrigger.from_crontab(s.cron_monthly_brief, timezone=_ICT)
    nxt_monthly = monthly.get_next_fire_time(None, now)
    assert (nxt_monthly.day, nxt_monthly.hour) == (1, 15)


def _write_run_metadata(root: Path, run_id: str, **meta):
    run_dir = root / "outputs" / "runs" / run_id
    run_dir.mkdir(parents=True)
    (run_dir / "metadata.json").write_text(json.dumps(meta), encoding="utf-8")


def test_already_ran_today_guard(monkeypatch, tmp_path: Path):
    s = _settings(tmp_path)
    monkeypatch.setattr("vks_intelligence.config.get_settings", lambda: s)

    today_local = datetime.now(_ICT).date().isoformat()
    _write_run_metadata(
        tmp_path, "run-old",
        task_type="weekly-digest", trigger_source="n8n-cron",
        status="completed", started_at="2020-01-01T08:00:00+00:00",
    )
    assert _already_ran_today("weekly-digest", today_local) is False

    _write_run_metadata(
        tmp_path, "run-today",
        task_type="weekly-digest", trigger_source="scheduler",
        status="completed", started_at=datetime.now(_ICT).isoformat(),
    )
    assert _already_ran_today("weekly-digest", today_local) is True
    # Task khác cùng ngày không bị guard chặn
    assert _already_ran_today("daily-intelligence", today_local) is False
    # Run thủ công (trigger_source khác) không tính là scheduled
    _write_run_metadata(
        tmp_path, "run-manual",
        task_type="monthly-brief", trigger_source="telegram",
        status="completed", started_at=datetime.now(_ICT).isoformat(),
    )
    assert _already_ran_today("monthly-brief", today_local) is False


def test_run_job_now_skips_when_already_ran(monkeypatch, tmp_path: Path):
    s = _settings(tmp_path)
    monkeypatch.setattr("vks_intelligence.config.get_settings", lambda: s)
    monkeypatch.setattr(sched_mod, "_already_ran_today", lambda *_: True)

    result = run_job_now("weekly-digest")
    assert result["status"] == "skipped_already_ran"


def test_job_wrapper_failure_notifies_owner(monkeypatch, tmp_path: Path):
    s = _settings(tmp_path)
    monkeypatch.setattr("vks_intelligence.config.get_settings", lambda: s)
    monkeypatch.setattr(sched_mod, "_already_ran_today", lambda *_: False)

    def boom(job, request_id, source):
        raise RuntimeError("model down")

    monkeypatch.setattr(sched_mod, "_execute_task", boom)
    alerts: list[str] = []
    monkeypatch.setattr(sched_mod, "_notify_owner", alerts.append)

    _job_wrapper("daily-intelligence")  # không được raise

    assert any("model down" in a for a in alerts)
    assert sched_mod._last_results["daily-intelligence"]["status"] == "error"


def test_trigger_endpoint_token_checks(monkeypatch):
    s = _settings(scheduler_enabled=False, scheduler_trigger_token="secret-token")
    monkeypatch.setattr("vks_intelligence.config.get_settings", lambda: s)

    app = FastAPI()
    attach_scheduler(app)
    client = TestClient(app)

    # Sai token → 403
    r = client.post("/scheduler/run/daily-intelligence", headers={"X-Scheduler-Token": "wrong"})
    assert r.status_code == 403
    # Token đúng + job không tồn tại → 404
    r = client.post("/scheduler/run/khong-ton-tai", headers={"X-Scheduler-Token": "secret-token"})
    assert r.status_code == 404
    # Token đúng + job hợp lệ → chạy (monkeypatch để không gọi model thật)
    monkeypatch.setattr(sched_mod, "run_job_now", lambda name, source: {"job": name, "status": "ran"})
    r = client.post("/scheduler/run/daily-intelligence", headers={"X-Scheduler-Token": "secret-token"})
    assert r.status_code == 200
    assert r.json()["status"] == "ran"


def test_trigger_endpoint_unconfigured_token_is_503(monkeypatch):
    s = _settings(scheduler_enabled=False, scheduler_trigger_token="")
    monkeypatch.setattr("vks_intelligence.config.get_settings", lambda: s)

    app = FastAPI()
    attach_scheduler(app)
    client = TestClient(app)
    r = client.post("/scheduler/run/daily-intelligence")
    assert r.status_code == 503


def test_jobs_cover_all_report_types():
    assert set(JOBS) == {
        "daily-intelligence", "weekly-digest", "monthly-brief",
        "competitor-monitor", "memory-maintenance",
    }
