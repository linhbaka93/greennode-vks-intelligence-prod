"""Competitor Agent — theo dõi AWS EKS, Bizfly BKE, FPT FKE, Viettel vOKS.

Bóc tách động thái sản phẩm/pricing/feature, so sánh với GreenNode VKS, và phân
loại severity để supervisor quyết định có alert hay không.
"""

from __future__ import annotations

from vks_intelligence.llm.router import Workload
from vks_intelligence.registry import register
from vks_intelligence.specialists.base import Specialist


@register("competitor_agent")
class CompetitorAgent(Specialist):
    name = "competitor_agent"
    prompt_file = "competitor_agent.md"
    workload = Workload.RESEARCH
