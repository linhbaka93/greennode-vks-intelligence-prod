"""Pricing Agent — pricing delta, TCO, hidden cost, kèm assumption và ngày dữ liệu.

Mọi con số pricing phải có nguồn và timestamp. Reasoning số học cần cẩn trọng nên
ưu tiên model mạnh và bắt buộc nêu caveat khi dữ liệu cũ.
"""

from __future__ import annotations

from vks_intelligence.llm.router import Workload
from vks_intelligence.registry import register
from vks_intelligence.specialists.base import Specialist


@register("pricing_agent")
class PricingAgent(Specialist):
    name = "pricing_agent"
    prompt_file = "pricing_agent.md"
    workload = Workload.RESEARCH
