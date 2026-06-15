"""Ghi output cuối ra workspace outputs/ theo quy ước đặt tên ngày-loại.

Tách khỏi task_store (artifact audit của một run) — đây là bản publish chính thức
dùng cho weekly/monthly và để memory_tool đọc lại làm lịch sử so sánh.
"""

from __future__ import annotations

from datetime import date
from pathlib import Path

from vks_intelligence.contracts import TaskType

_TYPE_DIR: dict[str, str] = {
    TaskType.WEEKLY_DIGEST.value:      "digests",
    TaskType.MONTHLY_BRIEF.value:      "briefs",
    TaskType.COMPETITOR_MONITOR.value: "competitor-reports",
    TaskType.DAILY_INTELLIGENCE.value: "daily-intelligence",
    TaskType.BATTLECARD.value:         "battlecards",
    TaskType.PRICING_ANALYSIS.value:   "pricing",
    TaskType.MEMORY_MAINTENANCE.value: "memory-patches",
}


def write_output(workspace_path: Path, task_type: TaskType, when: date, content: str) -> Path:
    """Ghi content vào outputs/<loại>/<ngày>_<task_type>.md, trả đường dẫn đã ghi."""
    dir_name = _TYPE_DIR.get(task_type.value, task_type.value)
    out_dir = workspace_path / "outputs" / dir_name
    out_dir.mkdir(parents=True, exist_ok=True)

    filename = f"{when.isoformat()}_{task_type.value}.md"
    out_path = out_dir / filename

    # Nếu file đã tồn tại hôm nay, thêm suffix để không overwrite
    if out_path.exists():
        import time
        suffix = time.strftime("%H%M%S")
        filename = f"{when.isoformat()}_{task_type.value}_{suffix}.md"
        out_path = out_dir / filename

    out_path.write_text(content, encoding="utf-8")
    return out_path
