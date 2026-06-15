from vks_intelligence.contracts import QAEscalationIntent
from vks_intelligence.specialists.qa_agent import QAAgent


class _DummyRouter:
    pass


def test_qa_intent_detects_current_research_phrases():
    agent = QAAgent(_DummyRouter())

    assert agent.classify_intent("VKS có thông tin gì mới hôm nay") == QAEscalationIntent.CURRENT_RESEARCH
    assert agent.classify_intent("research giúp mình") == QAEscalationIntent.CURRENT_RESEARCH
    assert agent.classify_intent("cập nhật thông tin mới trong hôm nay") == QAEscalationIntent.CURRENT_RESEARCH


def test_qa_intent_keeps_normal_memory_lookup():
    agent = QAAgent(_DummyRouter())

    assert agent.classify_intent("Bizfly BKE mạnh điểm nào") == QAEscalationIntent.MEMORY_LOOKUP
