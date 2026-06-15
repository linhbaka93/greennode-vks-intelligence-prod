"""Nạp workspace memory thành context cho agent.

Đọc memory phân tầng theo ưu tiên (đối thủ VN Tier 1 trước hyperscaler, regulatory
trước pricing), cắt mỗi file theo cap để không vượt context, và áp freshness
threshold để cảnh báo dữ liệu cũ.
"""

from __future__ import annotations

import re
from datetime import datetime, timezone
from pathlib import Path

from vks_intelligence.contracts import Confidence, MemoryPatch

_PRIORITY_FOLDERS = [
    "greennode",
    "competitors",
    "pricing",
    "regulatory",
    "market-trends",
    "battlecards",
    "feature-gaps",
    "executive-briefs",
]

_DATE_RE = re.compile(r"^(\d{4}-\d{2}-\d{2})[_-]")

# VN Tier 1 nhận dạng từ tên file
_TIER1_NAMES = ("viettel", "fpt", "cmccloud", "bizfly")
_TIER2_NAMES = ("aws", "gke", "aks", "alibaba", "oracle")


def _file_date(name: str) -> datetime | None:
    m = _DATE_RE.match(name)
    if not m:
        return None
    try:
        return datetime.fromisoformat(m.group(1)).replace(tzinfo=timezone.utc)
    except ValueError:
        return None


def _is_stale(path: Path) -> bool:
    from vks_intelligence.config import get_settings
    s = get_settings()
    date = _file_date(path.name)
    if date is None:
        return False
    age = (datetime.now(timezone.utc) - date).days
    name = path.name.lower()
    parent = path.parent.name.lower()

    if parent == "pricing" or "pricing" in name:
        threshold = s.gpu_pricing_freshness_days if "gpu" in name else s.tier1_freshness_days
        return age > threshold
    if parent == "market-trends":
        return age > s.market_trends_freshness_days
    if parent == "competitors":
        if any(t in name for t in _TIER1_NAMES):
            return age > s.tier1_freshness_days
        if any(t in name for t in _TIER2_NAMES):
            return age > s.tier2_freshness_days
        return age > s.tier3_freshness_days
    return False


def _sort_key(f: Path):
    is_current = "current" in f.name
    d = _file_date(f.name)
    ts = d.timestamp() if d else 0.0
    return (0 if is_current else 1, -ts)


def load_memory(workspace_path: Path, context_cap: int = 12_000) -> str:
    """Trả context string gộp từ memory/, đã sắp ưu tiên và cắt theo cap."""
    memory_root = workspace_path / "memory"
    if not memory_root.exists():
        return ""

    per_file_cap = max(400, context_cap // 16)
    chunks: list[str] = []
    used = 0

    for folder_name in _PRIORITY_FOLDERS:
        folder = memory_root / folder_name
        if not folder.exists():
            continue

        files = sorted(
            [f for f in folder.iterdir() if f.suffix == ".md" and f.name != "README.md"],
            key=_sort_key,
        )

        for f in files:
            if used >= context_cap:
                break
            stale = _is_stale(f)
            raw = f.read_text(encoding="utf-8", errors="ignore")[:per_file_cap]
            prefix = (
                f"\n⚠️ [Dữ liệu cũ — {folder_name}/{f.name}]\n"
                if stale
                else f"\n[{folder_name}/{f.name}]\n"
            )
            chunk = prefix + raw
            chunks.append(chunk)
            used += len(chunk)

    return "\n".join(chunks)[:context_cap]


def load_competitor(workspace_path: Path, competitor: str) -> str:
    """Đọc profile của một đối thủ cụ thể từ memory/competitors."""
    root = workspace_path / "memory" / "competitors"
    if not root.exists():
        return ""
    slug = competitor.lower().replace(" ", "-")
    for f in sorted(root.iterdir(), key=_sort_key):
        if f.suffix == ".md" and slug in f.name.lower():
            return f.read_text(encoding="utf-8", errors="ignore")
    return f"[Không tìm thấy profile '{competitor}' trong memory/competitors]"


def apply_patch(workspace_path: Path, patch: MemoryPatch, auto: bool) -> Path:
    """Áp MemoryPatch vào memory/.

    auto=False → ghi ra memory/_proposed/ chờ duyệt.
    auto=True  → ghi thẳng, chỉ khi Settings và quality gate cho phép.
    """
    if not auto:
        proposed = workspace_path / "memory" / "_proposed"
        proposed.mkdir(parents=True, exist_ok=True)
        ts = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S")
        slug = patch.path.replace("/", "_").replace("\\", "_")
        out = proposed / f"{ts}_{slug}.md"
        out.write_text(
            f"# Proposed patch\nOp: {patch.op}\nPath: {patch.path}\n"
            f"Reason: {patch.reason}\n\n{patch.content}",
            encoding="utf-8",
        )
        return out

    target = workspace_path / "memory" / patch.path
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(patch.content, encoding="utf-8")
    return target


def can_auto_write(patch: MemoryPatch, quality_score: float) -> bool:
    """Kiểm tra patch có đủ điều kiện auto-write theo policy trong Settings."""
    from vks_intelligence.config import get_settings
    s = get_settings()
    if not s.memory_auto_write_enabled:
        return False
    if patch.confidence != Confidence.HIGH:
        return False
    return quality_score >= s.memory_auto_write_min_quality
