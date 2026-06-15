"""Battlecard Agent — battlecard theo từng đối thủ, win/loss talking point.

Tổng hợp điểm mạnh/yếu và ma trận objection của người mua thành battlecard một
trang dùng được ngay cho sales/presales.
"""

from __future__ import annotations

from vks_intelligence.llm.router import Workload
from vks_intelligence.registry import register
from vks_intelligence.specialists.base import Specialist


@register("battlecard_agent")
class BattlecardAgent(Specialist):
    name = "battlecard_agent"
    prompt_file = "battlecard_agent.md"
    workload = Workload.SYNTHESIS
