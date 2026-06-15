"""Import tất cả specialist để @register decorator boot registry khi package load."""

from vks_intelligence.specialists.qa_agent import QAAgent
from vks_intelligence.specialists.daily_intelligence_agent import DailyIntelligenceAgent
from vks_intelligence.specialists.market_trend_agent import MarketTrendAgent
from vks_intelligence.specialists.competitor_agent import CompetitorAgent
from vks_intelligence.specialists.pricing_agent import PricingAgent
from vks_intelligence.specialists.regulatory_agent import RegulatoryAgent
from vks_intelligence.specialists.positioning_agent import PositioningAgent
from vks_intelligence.specialists.battlecard_agent import BattlecardAgent
from vks_intelligence.specialists.memory_curator_agent import MemoryCuratorAgent
from vks_intelligence.specialists.quality_critic_agent import QualityCriticAgent

__all__ = [
    "QAAgent",
    "DailyIntelligenceAgent",
    "MarketTrendAgent",
    "CompetitorAgent",
    "PricingAgent",
    "RegulatoryAgent",
    "PositioningAgent",
    "BattlecardAgent",
    "MemoryCuratorAgent",
    "QualityCriticAgent",
]
