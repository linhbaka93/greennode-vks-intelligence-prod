"""Regulatory Agent — tuân thủ Việt Nam, data residency, chính sách cloud công.

Theo dõi văn bản pháp lý ảnh hưởng tới cloud/Kubernetes tại VN và diễn giải hệ quả
cho positioning của GreenNode VKS.
"""

from __future__ import annotations

from vks_intelligence.llm.router import Workload
from vks_intelligence.registry import register
from vks_intelligence.specialists.base import Specialist


@register("regulatory_agent")
class RegulatoryAgent(Specialist):
    name = "regulatory_agent"
    prompt_file = "regulatory_agent.md"
    workload = Workload.RESEARCH
