"""Ghi và đọc artifact của mỗi run dưới `outputs/runs/<run_id>/`.

Ghi tăng dần trong suốt vòng đời run để luôn có audit trail kể cả khi run fail
giữa chừng: request.json → plan.json → <agent>.json → synthesis.md →
quality.json → final.md → metadata.json → fallback_trace.json → errors.json.
"""

from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from vks_intelligence.contracts import (
    AgentResult,
    EvidenceBundle,
    QualityResult,
    RunMetadata,
    TaskPlan,
    TaskRequest,
)


class TaskStore:
    def __init__(self, run_id: str, root: Path) -> None:
        self.run_id = run_id
        self.run_dir = root / run_id

    def _write_json(self, name: str, data: str) -> None:
        self.run_dir.mkdir(parents=True, exist_ok=True)
        (self.run_dir / name).write_text(data, encoding="utf-8")

    def _write_text(self, name: str, content: str) -> None:
        self.run_dir.mkdir(parents=True, exist_ok=True)
        (self.run_dir / name).write_text(content, encoding="utf-8")

    def init_run(self, request: TaskRequest) -> None:
        self.run_dir.mkdir(parents=True, exist_ok=True)
        self._write_json("request.json", request.model_dump_json(indent=2))

    def save_plan(self, plan: TaskPlan) -> None:
        self._write_json("plan.json", plan.model_dump_json(indent=2))

    def save_evidence(self, evidence: EvidenceBundle) -> None:
        self._write_json("evidence.json", evidence.model_dump_json(indent=2))

    def save_agent_result(self, result: AgentResult) -> None:
        self._write_json(f"{result.agent}.json", result.model_dump_json(indent=2))

    def save_synthesis(self, markdown: str) -> None:
        self._write_text("synthesis.md", markdown)

    def save_quality(self, quality: QualityResult) -> None:
        self._write_json("quality.json", quality.model_dump_json(indent=2))

    def save_final(self, markdown: str) -> None:
        self._write_text("final.md", markdown)

    def save_metadata(self, metadata: RunMetadata) -> None:
        self._write_json("metadata.json", metadata.model_dump_json(indent=2))
        if metadata.fallbacks:
            traces = [f.model_dump() for f in metadata.fallbacks]
            self._write_json(
                "fallback_trace.json",
                json.dumps(traces, indent=2, ensure_ascii=False),
            )

    def save_error(self, error: dict[str, Any]) -> None:
        error_path = self.run_dir / "errors.json"
        self.run_dir.mkdir(parents=True, exist_ok=True)
        existing: list[dict[str, Any]] = []
        if error_path.exists():
            try:
                existing = json.loads(error_path.read_text(encoding="utf-8"))
            except (json.JSONDecodeError, OSError):
                pass
        error["timestamp"] = datetime.now(timezone.utc).isoformat()
        existing.append(error)
        error_path.write_text(
            json.dumps(existing, indent=2, ensure_ascii=False), encoding="utf-8"
        )
