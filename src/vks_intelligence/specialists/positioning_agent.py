"""Positioning Agent — góc GTM, talking point cho sales, xử lý objection.

Biến finding của các agent khác thành thông điệp bán hàng và phần action cho
executive, giữ giọng điệu không hype marketing.
"""

from __future__ import annotations

from vks_intelligence.llm.router import Workload
from vks_intelligence.registry import register
from vks_intelligence.specialists.base import Specialist


@register("positioning_agent")
class PositioningAgent(Specialist):
    name = "positioning_agent"
    prompt_file = "positioning_agent.md"
    workload = Workload.SYNTHESIS
