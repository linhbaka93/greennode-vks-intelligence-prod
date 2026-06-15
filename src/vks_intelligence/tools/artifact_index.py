"""Helpers đọc artifact store để tái sử dụng run fresh cho current-research."""

from __future__ import annotations

import json
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path

from vks_intelligence.contracts import TaskType

_FRESH_STATUSES = {"completed", "needs_review"}


@dataclass(frozen=True)
class ArtifactHit:
    run_id: str
    task_type: TaskType
    run_dir: Path
    finished_at: datetime
    metadata: dict


def _parse_dt(value: str) -> datetime | None:
    if not value:
        return None
    try:
        return datetime.fromisoformat(value.replace("Z", "+00:00")).astimezone(timezone.utc)
    except ValueError:
        return None


def _load_metadata(path: Path) -> dict | None:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return None


def latest_artifact(root: Path, task_type: TaskType) -> ArtifactHit | None:
    """Lấy artifact mới nhất theo task type, chỉ tính run có final/synthesis và status dùng được."""
    if not root.exists():
        return None

    hits: list[ArtifactHit] = []
    for run_dir in root.iterdir():
        if not run_dir.is_dir():
            continue
        meta = _load_metadata(run_dir / "metadata.json")
        if not meta:
            continue
        if meta.get("task_type") != task_type.value:
            continue
        if meta.get("status") not in _FRESH_STATUSES:
            continue
        if not ((run_dir / "final.md").exists() or (run_dir / "synthesis.md").exists()):
            continue
        finished_at = _parse_dt(meta.get("finished_at", ""))
        if not finished_at:
            continue
        hits.append(ArtifactHit(
            run_id=meta.get("run_id", run_dir.name),
            task_type=task_type,
            run_dir=run_dir,
            finished_at=finished_at,
            metadata=meta,
        ))

    if not hits:
        return None
    return max(hits, key=lambda hit: hit.finished_at)


def latest_fresh_artifact(root: Path, task_type: TaskType, ttl_seconds: int) -> ArtifactHit | None:
    """Lấy artifact mới nhất nếu còn trong TTL."""
    hit = latest_artifact(root, task_type)
    if not hit:
        return None
    age = datetime.now(timezone.utc) - hit.finished_at
    if age.total_seconds() <= ttl_seconds:
        return hit
    return None
