"""Log QA activity từ Telegram cho dashboard observability.

QA streaming (MEMORY_LOOKUP fast-path) và current-research reply không đi qua
supervisor pipeline nên không sinh run artifact dưới outputs/runs/. Module này ghi
mỗi lượt QA thành một dòng JSONL dưới outputs/qa_log/<date>.jsonl để dashboard tổng
hợp volume, intent, latency. Ghi best-effort, không bao giờ raise vào request path.
"""

from __future__ import annotations

import json
import logging
from datetime import datetime, timezone
from pathlib import Path

log = logging.getLogger(__name__)


def record(
    qa_log_root: Path,
    *,
    actor_id: str,
    intent: str,
    latency_ms: int,
    ok: bool = True,
    fallback: bool = False,
    task_type: str = "",
    routed_by: str = "",
) -> None:
    """Ghi một QA event vào outputs/qa_log/<date>.jsonl. Không raise."""
    try:
        now = datetime.now(timezone.utc)
        qa_log_root.mkdir(parents=True, exist_ok=True)
        event = {
            "ts": now.isoformat(),
            "actor_id": actor_id,
            "intent": intent,
            "latency_ms": int(latency_ms),
            "ok": ok,
            "fallback": fallback,
            "task_type": task_type,
            "routed_by": routed_by,
        }
        path = qa_log_root / f"{now:%Y-%m-%d}.jsonl"
        with path.open("a", encoding="utf-8") as f:
            f.write(json.dumps(event, ensure_ascii=False) + "\n")
    except Exception as exc:
        log.debug("qa_log.record failed: %s", exc)


def read_events(qa_log_root: Path, days: int = 14) -> list[dict]:
    """Đọc QA events từ N file ngày gần nhất, mới nhất trước."""
    if not qa_log_root.exists():
        return []
    events: list[dict] = []
    files = sorted(qa_log_root.glob("*.jsonl"), reverse=True)[:days]
    for f in files:
        try:
            for line in f.read_text(encoding="utf-8").splitlines():
                line = line.strip()
                if line:
                    events.append(json.loads(line))
        except (OSError, json.JSONDecodeError):
            continue
    return events
