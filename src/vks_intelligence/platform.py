"""AgentBase Runtime entry point.

Khởi động uvicorn serving FastAPI app (`api.py`) trên port 8080.
Toàn bộ routing logic nằm trong api.py — platform.py chỉ lo startup.

Runtime contract (chuẩn AgentBase):
  GET  /health      → liveness probe
  POST /invocations → task routing
  PORT 8080
"""

from __future__ import annotations

import logging
import sys

log = logging.getLogger(__name__)


def build_app():
    """Trả FastAPI app đã có đầy đủ routes + scheduler nội bộ."""
    from vks_intelligence.api import app
    from vks_intelligence.scheduler import attach_scheduler

    attach_scheduler(app)
    return app


def run() -> None:
    """Log startup info và serve uvicorn trên port cấu hình."""
    import uvicorn
    from vks_intelligence.config import get_settings

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
        stream=sys.stdout,
        force=True,
    )

    s = get_settings()
    log.info("=" * 60)
    log.info("GreenNode VKS Intelligence — AgentBase Runtime")
    log.info("Workspace : %s", s.workspace_path)
    log.info("Models    : qa=%s  research=%s", s.model_qa, s.model_research)
    log.info("Port      : %d", s.port)
    log.info("=" * 60)

    if not s.ai_platform_api_key:
        log.warning("AI_PLATFORM_API_KEY chưa set — model call sẽ thất bại")
    if not s.telegram_bot_token:
        log.warning("TELEGRAM_BOT_TOKEN chưa set — Telegram webhook tắt")

    uvicorn.run(build_app(), host="0.0.0.0", port=s.port, log_level=s.log_level.lower())
