"""Scheduler nội bộ chạy trong runtime — thay control plane n8n.

Fire các task định kỳ theo cron ICT (config.Settings.cron_*), tái dùng đúng
các hàm endpoint trong api.py, rồi tự deliver kết quả lên Telegram (việc mà
trước đây n8n nodes đảm nhiệm). GitHub Actions backup gọi POST /scheduler/run/{job}
với cùng guard idempotency để không đăng trùng trong ngày.

Lưu ý vận hành:
  - Chỉ an toàn khi runtime có 1 replica (deploy.ps1 pin min=max=1).
  - Guard idempotency dựa trên outputs/runs/*/metadata.json — FS ephemeral,
    restart giữa ngày có thể mất guard; GH Actions vì vậy đặt lệch 30 phút.
"""

from __future__ import annotations

import atexit
import hmac
import json
import logging
import threading
from dataclasses import dataclass
from datetime import datetime
from zoneinfo import ZoneInfo

from fastapi import FastAPI, Header, HTTPException

log = logging.getLogger(__name__)

# Trigger source được guard idempotency công nhận là "run scheduled trong ngày"
_SCHEDULED_SOURCES = {"scheduler", "gh-actions", "n8n-cron"}
_DONE_STATUSES = {"completed", "needs_review"}


@dataclass(frozen=True)
class JobSpec:
    name: str            # tên job trong URL /scheduler/run/{name}
    task_type: str       # TaskType value khớp metadata.json
    label: str           # header tiếng Việt khi đăng Telegram
    cron_setting: str    # tên field cron trong Settings
    silent: bool         # True → chỉ báo owner, không đăng kênh chính


JOBS: dict[str, JobSpec] = {
    spec.name: spec
    for spec in (
        JobSpec("daily-intelligence", "daily-intelligence",
                "Daily Intelligence", "cron_daily_intelligence", False),
        JobSpec("weekly-digest", "weekly-digest",
                "Weekly Digest", "cron_weekly_digest", False),
        JobSpec("monthly-brief", "monthly-brief",
                "Monthly Brief", "cron_monthly_brief", False),
        JobSpec("competitor-monitor", "competitor-monitor",
                "Competitor Monitor", "cron_competitor_monitor", True),
        JobSpec("memory-maintenance", "memory-maintenance",
                "Memory Maintenance", "cron_memory_maintenance", True),
    )
}

_scheduler = None
_lock = threading.Lock()
_last_results: dict[str, dict] = {}


# ──────────────────────────────────────────────────────────────────
# Idempotency guard
# ──────────────────────────────────────────────────────────────────

def _tz() -> ZoneInfo:
    from vks_intelligence.config import get_settings
    return ZoneInfo(get_settings().scheduler_timezone)


def _today_local() -> str:
    return datetime.now(_tz()).date().isoformat()


def _already_ran_today(task_type: str, local_date: str) -> bool:
    """True nếu hôm nay (theo scheduler_timezone) đã có run scheduled hoàn tất."""
    from vks_intelligence.config import get_settings

    s = get_settings()
    artifact_root = s.workspace_path / s.artifact_root
    if not artifact_root.exists():
        return False
    for run_dir in artifact_root.iterdir():
        meta_path = run_dir / "metadata.json"
        if not meta_path.exists():
            continue
        try:
            meta = json.loads(meta_path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            continue
        if meta.get("task_type") != task_type:
            continue
        if meta.get("trigger_source") not in _SCHEDULED_SOURCES:
            continue
        if meta.get("status") not in _DONE_STATUSES:
            continue
        started_at = meta.get("started_at", "")
        try:
            started_local = datetime.fromisoformat(started_at).astimezone(_tz())
        except ValueError:
            continue
        if started_local.date().isoformat() == local_date:
            return True
    return False


# ──────────────────────────────────────────────────────────────────
# Task execution — tái dùng endpoint functions trong api.py
# ──────────────────────────────────────────────────────────────────

def _execute_task(job: JobSpec, request_id: str, source: str):
    """Chạy task tương ứng và trả TaskResponse (import lazy tránh cycle)."""
    from vks_intelligence.api import (
        _supervisor,
        _task_response_from_metadata,
        task_competitor_monitor,
        task_daily_intelligence,
        task_memory_maintenance,
        task_weekly_digest,
    )
    from vks_intelligence.contracts import TaskRequest, TaskType
    from vks_intelligence.schemas import DailyIntelligenceRequestBody, TaskRequestBody

    if job.name == "daily-intelligence":
        return task_daily_intelligence(DailyIntelligenceRequestBody(
            request_id=request_id, source=source, days_window=1,
        ))
    if job.name == "weekly-digest":
        return task_weekly_digest(TaskRequestBody(
            request_id=request_id, source=source, human_approval_required=False,
        ))
    if job.name == "monthly-brief":
        # Gọi supervisor trực tiếp: endpoint /tasks/monthly-brief ép approval=True,
        # còn lịch tự động đã chốt auto-publish khi quality pass.
        meta = _supervisor().run(TaskRequest(
            request_id=request_id,
            task_type=TaskType.MONTHLY_BRIEF,
            source=source,
            human_approval_required=False,
        ))
        return _task_response_from_metadata(meta)
    if job.name == "competitor-monitor":
        return task_competitor_monitor(TaskRequestBody(request_id=request_id, source=source))
    if job.name == "memory-maintenance":
        return task_memory_maintenance(TaskRequestBody(request_id=request_id, source=source))
    raise ValueError(f"Job không hỗ trợ: {job.name}")


# ──────────────────────────────────────────────────────────────────
# Telegram delivery — thay các node Telegram của n8n
# ──────────────────────────────────────────────────────────────────

def _send_chunks(token: str, chat_id: str, markdown: str) -> bool:
    from vks_intelligence.config import get_settings
    from vks_intelligence.tools.telegram_tool import (
        format_telegram_html_messages,
        send_message,
    )

    s = get_settings()
    ok = True
    for chunk in format_telegram_html_messages(markdown, s.telegram_max_chars_per_message):
        if send_message(token, chat_id, chunk, parse_mode="HTML") is None:
            ok = False
    return ok


def _notify_owner(text: str) -> None:
    from vks_intelligence.config import get_settings
    from vks_intelligence.tools.telegram_tool import send_message

    s = get_settings()
    chat_id = s.telegram_owner_chat_id or s.telegram_chat_id
    if not (s.telegram_bot_token and chat_id):
        log.warning("Không gửi được owner alert — thiếu Telegram config")
        return
    send_message(s.telegram_bot_token, chat_id, text, parse_mode="")


def deliver_report(resp, job: JobSpec) -> str:
    """Đăng kết quả run lên Telegram; trả mô tả delivery cho status/log."""
    from pathlib import Path

    from vks_intelligence.config import get_settings

    s = get_settings()
    if not s.telegram_bot_token:
        return "skipped: thiếu TELEGRAM_BOT_TOKEN"

    today = _today_local()
    summary = (
        f"{job.label} — {today}\n"
        f"status={resp.status} score={resp.quality_score} artifact={resp.artifact_path}"
    )

    if resp.status == "completed" and resp.quality_passed:
        if job.silent:
            _notify_owner(f"✅ {summary}")
            return "owner-summary"
        final_path = Path(resp.artifact_path) / "final.md"
        try:
            report_md = final_path.read_text(encoding="utf-8")
        except OSError as exc:
            _notify_owner(f"🚨 {job.label} — {today}: run xong nhưng không đọc được final.md ({exc})")
            return "error: final.md unreadable"
        header = f"📰 **{job.label} — {today}**\n\n"
        sent = _send_chunks(s.telegram_bot_token, s.telegram_chat_id, header + report_md)
        return "published" if sent else "partial: một số chunk gửi lỗi"

    warn = "; ".join(resp.warnings[:3])
    _notify_owner(f"🚨 {summary}\n{warn}")
    return f"alerted-owner: status={resp.status}"


# ──────────────────────────────────────────────────────────────────
# Job runner — guard → task → delivery (dùng chung cho cron + HTTP trigger)
# ──────────────────────────────────────────────────────────────────

def run_job_now(job_name: str, source: str = "scheduler") -> dict:
    job = JOBS.get(job_name)
    if job is None:
        raise KeyError(job_name)

    today = _today_local()
    with _lock:
        if _already_ran_today(job.task_type, today):
            log.info("Scheduler skip %s — đã có run %s hôm nay", job.name, job.task_type)
            result = {"job": job.name, "status": "skipped_already_ran", "date": today}
            _last_results[job.name] = result
            return result

    request_id = f"sched-{job.name}-{today}"
    log.info("Scheduler fire %s (request_id=%s, source=%s)", job.name, request_id, source)
    resp = _execute_task(job, request_id, source)
    delivery = deliver_report(resp, job)
    result = {
        "job": job.name,
        "status": "ran",
        "date": today,
        "task_status": resp.status,
        "quality_score": resp.quality_score,
        "delivery": delivery,
    }
    _last_results[job.name] = result
    return result


def _job_wrapper(job_name: str) -> None:
    """Cron entry — nuốt mọi exception để thread scheduler không chết."""
    try:
        run_job_now(job_name, source="scheduler")
    except Exception as exc:
        log.error("Scheduler job %s lỗi: %s", job_name, exc, exc_info=True)
        _last_results[job_name] = {"job": job_name, "status": "error", "error": str(exc)}
        try:
            _notify_owner(f"🚨 Scheduler job {job_name} lỗi: {exc}")
        except Exception:
            log.exception("Không gửi được owner alert cho job %s", job_name)


# ──────────────────────────────────────────────────────────────────
# HTTP endpoints
# ──────────────────────────────────────────────────────────────────

def scheduler_status() -> dict:
    from vks_intelligence.config import get_settings

    s = get_settings()
    jobs = []
    for job in JOBS.values():
        entry: dict = {
            "job": job.name,
            "cron": getattr(s, job.cron_setting),
            "timezone": s.scheduler_timezone,
            "last_result": _last_results.get(job.name),
        }
        if _scheduler is not None:
            ap_job = _scheduler.get_job(job.name)
            if ap_job and ap_job.next_run_time:
                entry["next_fire"] = ap_job.next_run_time.astimezone(_tz()).isoformat()
        jobs.append(entry)
    return {
        "enabled": s.scheduler_enabled,
        "running": _scheduler is not None,
        "jobs": jobs,
    }


def trigger_job(job_name: str, x_scheduler_token: str = Header(default="")) -> dict:
    from vks_intelligence.config import get_settings

    s = get_settings()
    if not s.scheduler_trigger_token:
        raise HTTPException(status_code=503, detail="SCHEDULER_TRIGGER_TOKEN chưa cấu hình")
    if not hmac.compare_digest(x_scheduler_token, s.scheduler_trigger_token):
        raise HTTPException(status_code=403, detail="Token không hợp lệ")
    try:
        return run_job_now(job_name, source="gh-actions")
    except KeyError:
        raise HTTPException(status_code=404, detail=f"Job '{job_name}' không tồn tại") from None


# ──────────────────────────────────────────────────────────────────
# Lifecycle
# ──────────────────────────────────────────────────────────────────

def _start() -> None:
    global _scheduler
    from apscheduler.schedulers.background import BackgroundScheduler
    from apscheduler.triggers.cron import CronTrigger

    from vks_intelligence.config import get_settings

    s = get_settings()
    tz = ZoneInfo(s.scheduler_timezone)
    sched = BackgroundScheduler(timezone=tz)
    for job in JOBS.values():
        sched.add_job(
            _job_wrapper,
            CronTrigger.from_crontab(getattr(s, job.cron_setting), timezone=tz),
            args=[job.name],
            id=job.name,
            coalesce=True,
            misfire_grace_time=3600,
            max_instances=1,
        )
    sched.start()
    _scheduler = sched
    log.info(
        "Scheduler nội bộ chạy (%s): %s",
        s.scheduler_timezone,
        {j.name: getattr(s, j.cron_setting) for j in JOBS.values()},
    )


def _stop() -> None:
    global _scheduler
    if _scheduler is not None:
        _scheduler.shutdown(wait=False)
        _scheduler = None


def attach_scheduler(app: FastAPI) -> None:
    """Gắn scheduler + endpoint điều khiển vào app. Gọi từ platform.build_app()."""
    from vks_intelligence.config import get_settings

    app.add_api_route("/scheduler/status", scheduler_status, methods=["GET"])
    app.add_api_route("/scheduler/run/{job_name}", trigger_job, methods=["POST"])

    s = get_settings()
    if not s.scheduler_enabled:
        log.info("Scheduler nội bộ TẮT (SCHEDULER_ENABLED=false)")
        return
    if not s.telegram_bot_token:
        log.warning("Scheduler nội bộ TẮT — thiếu TELEGRAM_BOT_TOKEN (báo cáo không gửi được)")
        return
    # BackgroundScheduler chạy thread riêng — start ngay tại build_app(),
    # không cần lifespan (FastAPI mới đã bỏ add_event_handler).
    _start()
    atexit.register(_stop)
