from vks_intelligence.contracts import QAEscalationIntent
from vks_intelligence.specialists.qa_agent import QAAgent


class _DummyRouter:
    pass


def test_qa_intent_detects_current_research_phrases():
    agent = QAAgent(_DummyRouter())

    assert agent.classify_intent("VKS có thông tin gì mới hôm nay") == QAEscalationIntent.CURRENT_RESEARCH
    assert agent.classify_intent("research giúp mình") == QAEscalationIntent.CURRENT_RESEARCH
    assert agent.classify_intent("cập nhật thông tin mới trong hôm nay") == QAEscalationIntent.CURRENT_RESEARCH


def test_qa_intent_detects_explicit_update_triggers():
    agent = QAAgent(_DummyRouter())

    assert agent.classify_intent("cập nhật pricing Viettel") == QAEscalationIntent.CURRENT_RESEARCH
    assert agent.classify_intent("mở research về FPT Cloud") == QAEscalationIntent.CURRENT_RESEARCH
    assert agent.classify_intent("refresh thông tin đối thủ") == QAEscalationIntent.CURRENT_RESEARCH
    assert agent.classify_intent("đào sâu về thị trường K8s VN") == QAEscalationIntent.CURRENT_RESEARCH
    assert agent.classify_intent("chạy lại research pricing") == QAEscalationIntent.CURRENT_RESEARCH
    assert agent.classify_intent("phân tích sâu về Bizfly") == QAEscalationIntent.CURRENT_RESEARCH


def test_qa_intent_keeps_normal_memory_lookup():
    agent = QAAgent(_DummyRouter())

    assert agent.classify_intent("Bizfly BKE mạnh điểm nào") == QAEscalationIntent.MEMORY_LOOKUP
