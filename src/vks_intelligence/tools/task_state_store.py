"""Task/session state store — biết task nào đang chạy, ở stage nào.

Lưu tại outputs/runs/_index/active_tasks.json (file-based, không cần DB).
Bot dùng để trả lời follow-up "research xong chưa?", "đang bị treo?".

Schema một entry:
{
  "actor_id":    "tg-123456",
  "session_id":  "tg-123456-2026-06-02",
  "run_id":      "2026-06-02_qa_current_abc12345",
  "task_type":   "qa",
  "status":      "running" | "completed" | "failed",
  "stage":       "collect_evidence" | "run_agents" | "quality_gate" | "done",
  "started_at":  "ISO 8601",
  "updated_at":  "ISO 8601",
  "artifact_path": "outputs/runs/..."
}
"""

from __future__ import annotations

import json
import logging
from datetime import datetime, timezone
from pathlib import Path

log = logging.getLogger(__name__)

_INDEX_DIR = "_index"
_ACTIVE_FILE = "active_tasks.json"


def _now() -> str:
    return datetime.now(timezone.utc).isoformat()


class TaskStateStore:
    def __init__(self, workspace_path: Path) -> None:
        self.index_dir = workspace_path / "outputs" / "runs" / _INDEX_DIR
        self.index_dir.mkdir(parents=True, exist_ok=True)
        self._path = self.index_dir / _ACTIVE_FILE

    def _load(self) -> list[dict]:
        if not self._path.exists():
            return []
        try:
            return json.loads(self._path.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError):
            return []

    def _save(self, tasks: list[dict]) -> None:
        try:
            tmp_path = self._path.with_suffix(".tmp")
            tmp_path.write_text(
                json.dumps(tasks, indent=2, ensure_ascii=False),
                encoding="utf-8",
            )
            tmp_path.replace(self._path)
        except OSError as exc:
            log.error("TaskStateStore write failed: %s", exc)

    # ──────────────────────────────────────────────────────
    # Write operations
    # ──────────────────────────────────────────────────────

    def upsert(
        self,
        actor_id: str,
        session_id: str,
        run_id: str,
        task_type: str,
        stage: str = "starting",
        artifact_path: str = "",
    ) -> None:
        """Tạo hoặc cập nhật active task cho actor."""
        tasks = self._load()
        # Xoá entry cũ của actor (1 actor 1 active task)
        tasks = [t for t in tasks if t.get("actor_id") != actor_id]
        tasks.append({
            "actor_id": actor_id,
            "session_id": session_id,
            "run_id": run_id,
            "task_type": task_type,
            "status": "running",
            "stage": stage,
            "started_at": _now(),
            "updated_at": _now(),
            "artifact_path": artifact_path,
        })
        self._save(tasks)

    def update_stage(self, run_id: str, stage: str, status: str = "running") -> None:
        tasks = self._load()
        for t in tasks:
            if t.get("run_id") == run_id:
                t["stage"] = stage
                t["status"] = status
                t["updated_at"] = _now()
                break
        self._save(tasks)

    def complete(self, run_id: str, artifact_path: str = "") -> None:
        tasks = self._load()
        for t in tasks:
            if t.get("run_id") == run_id:
                t["status"] = "completed"
                t["stage"] = "done"
                t["updated_at"] = _now()
                if artifact_path:
                    t["artifact_path"] = artifact_path
                break
        self._save(tasks)

    def fail(self, run_id: str, reason: str = "") -> None:
        tasks = self._load()
        for t in tasks:
            if t.get("run_id") == run_id:
                t["status"] = "failed"
                t["stage"] = reason or "failed"
                t["updated_at"] = _now()
                break
        self._save(tasks)

    # ──────────────────────────────────────────────────────
    # Read operations
    # ──────────────────────────────────────────────────────

    def get_by_actor(self, actor_id: str) -> dict | None:
        for t in self._load():
            if t.get("actor_id") == actor_id:
                return t
        return None

    def get_run_summary(self, artifact_path: str, max_chars: int = 1500) -> str | None:
        """Đọc final.md hoặc synthesis.md từ artifact path."""
        if not artifact_path:
            return None
        base = Path(artifact_path)
        for fname in ("final.md", "synthesis.md"):
            f = base / fname
            if f.exists():
                content = f.read_text(encoding="utf-8", errors="ignore")
                return content[:max_chars] + ("…" if len(content) > max_chars else "")
        return None

    def build_status_reply(self, task: dict) -> str:
        """Sinh câu trả lời trạng thái tự nhiên cho follow-up."""
        status = task.get("status", "unknown")
        stage = task.get("stage", "")
        run_id = task.get("run_id", "")
        started = task.get("started_at", "")

        # Tính thời gian chạy
        elapsed = ""
        if started:
            try:
                dt = datetime.fromisoformat(started.replace("Z", "+00:00"))
                secs = int((datetime.now(timezone.utc) - dt).total_seconds())
                elapsed = f" ({secs}s)" if secs < 120 else f" ({secs // 60}m {secs % 60}s)"
            except Exception:
                pass

        if status == "running":
            stage_label = {
                "starting": "chuẩn bị",
                "collect_evidence": "đang collect RSS/news",
                "run_agents": "đang chạy agents",
                "quality_gate": "đang qua quality check",
            }.get(stage, stage)
            return (
                f"⏳ 🌼 Lin Lin 🌼 đang xử lý research task{elapsed}.\n"
                f"Bước hiện tại: *{stage_label}*\n"
                f"Run ID: `{run_id[:20]}...`\n\n"
                "_Sẽ gửi kết quả khi hoàn tất._"
            )
        elif status == "completed":
            summary = self.get_run_summary(task.get("artifact_path", ""))
            if summary:
                return f"✅ Research xong rồi! Đây là tóm tắt:\n\n{summary}"
            return f"✅ Research task `{run_id[:20]}...` đã hoàn tất. Artifact: `{task.get('artifact_path', '-')}`"
        elif status == "failed":
            return (
                f"❌ Task bị lỗi ở bước: *{stage}*\n"
                "Bạn muốn 🌼 Lin Lin 🌼 thử lại không? Nhắn _\"thử lại\"_ nhé."
            )
        return f"Trạng thái task: {status} / {stage}"
