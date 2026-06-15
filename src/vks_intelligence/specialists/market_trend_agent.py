"""Market Trend Agent — tổng hợp tin Kubernetes/cloud/AI infra và đánh giá tác động.

Lọc tín hiệu theo ma trận tác động × tốc độ, gắn nhãn sự kiện/dự đoán/chưa xác
minh, và trả claim kèm nguồn cho weekly digest.
"""

from __future__ import annotations

from vks_intelligence.llm.router import Workload
from vks_intelligence.registry import register
from vks_intelligence.specialists.base import Specialist


@register("market_trend_agent")
class MarketTrendAgent(Specialist):
    name = "market_trend_agent"
    prompt_file = "market_trend_agent.md"
    workload = Workload.RESEARCH
