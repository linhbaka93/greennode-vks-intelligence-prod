from pathlib import Path

from vks_intelligence.contracts import Confidence, MemoryPatch, MemoryPatchOp
from vks_intelligence.tools.memory_tool import apply_patch

_PATCH = MemoryPatch(
    op=MemoryPatchOp.UPDATE,
    path="battlecards/2026-06-08_battlecard_fpt.md",
    reason="auto-update từ run test",
    content="# Battlecard FPT\nNội dung.",
    confidence=Confidence.HIGH,
)


def test_apply_patch_proposed_when_not_auto(tmp_path: Path):
    out = apply_patch(tmp_path, _PATCH, auto=False)
    assert out.parent.name == "_proposed"
    assert out.exists()


def test_apply_patch_direct_when_auto(tmp_path: Path):
    out = apply_patch(tmp_path, _PATCH, auto=True)
    assert out == tmp_path / "memory" / "battlecards" / "2026-06-08_battlecard_fpt.md"
    assert out.read_text(encoding="utf-8").startswith("# Battlecard FPT")
