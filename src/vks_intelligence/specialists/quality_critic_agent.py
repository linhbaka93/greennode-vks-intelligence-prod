"""Quality Critic Agent — soát hallucination, thiếu nguồn, claim vô căn cứ.

Chạy bằng model khác họ với generator để bắt blind spot. Chỉ được trả verdict
block/needs_review/pass kèm lý do; không tự publish và không tự sửa nội dung.
"""

from __future__ import annotations

from vks_intelligence.llm.router import Workload
from vks_intelligence.registry import register
from vks_intelligence.specialists.base import Specialist


@register("quality_critic_agent")
class QualityCriticAgent(Specialist):
    name = "quality_critic_agent"
    prompt_file = "quality_critic_agent.md"
    workload = Workload.CRITIC
