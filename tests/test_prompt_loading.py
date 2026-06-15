from vks_intelligence.specialists.qa_agent import QAAgent


def test_specialist_loads_output_policy_and_agent_spec():
    prompt = QAAgent(router=object()).load_prompt()

    assert "Output Policy" in prompt
    assert "Social Sources" in prompt
    assert "https://www.facebook.com/greennode23" in prompt
    assert "Agent: Q&A" in prompt
