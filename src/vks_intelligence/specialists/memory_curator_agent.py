"""Memory Curator Agent — phát hiện memory cũ/trùng, đề xuất patch.

Chỉ tạo proposed patch; không bao giờ tự ghi memory đã approve. Patch đi qua
critic và human approval trước khi commit vào repo.
"""

from __future__ import annotations

from vks_intelligence.contracts import MemoryPatch
from vks_intelligence.llm.router import Workload
from vks_intelligence.registry import register
from vks_intelligence.specialists.base import Specialist


@register("memory_curator_agent")
class MemoryCuratorAgent(Specialist):
    name = "memory_curator_agent"
    prompt_file = "memory_curator_agent.md"
    workload = Workload.RESEARCH

    def build_patches(self, context_summary: str) -> list[MemoryPatch]:
        """Sinh danh sách MemoryPatch đề xuất từ context_summary (plain text).

        Dùng khi caller cần patches trực tiếp thay vì đi qua AgentResult pipeline.
        Trong production flow, Supervisor gọi run() → patches được extract từ
        key_findings của AgentResult. Hàm này dành cho caller trực tiếp.
        """
        if not context_summary:
            return []
        from vks_intelligence.contracts import Confidence, MemoryPatchOp
        import re
        patches: list[MemoryPatch] = []
        for line in context_summary.splitlines():
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            op = MemoryPatchOp.UPDATE
            if re.search(r"\b(thêm|add|tạo mới|create)\b", line, re.I):
                op = MemoryPatchOp.CREATE
            elif re.search(r"\b(xoá|archive|outdated|lỗi thời)\b", line, re.I):
                op = MemoryPatchOp.ARCHIVE
            patches.append(MemoryPatch(
                op=op,
                path=f"proposed/{len(patches):03d}.md",
                reason=line[:200],
                content=line,
                confidence=Confidence.LOW,
            ))
        return patches
