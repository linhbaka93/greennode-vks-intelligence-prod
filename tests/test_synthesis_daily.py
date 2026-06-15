from vks_intelligence.contracts import (
    AgentResult,
    AgentStatus,
    Claim,
    Confidence,
    EvidenceType,
    TaskType,
)
from vks_intelligence.synthesis import synthesize


def test_daily_synthesis_filters_raw_json_and_groups_claims():
    result = AgentResult(
        agent="daily_intelligence_agent",
        task_id="daily-1",
        status=AgentStatus.OK,
        key_findings=[
            '{"summary":"raw","keyfindings":[],"strategicimplications":{"finding":"bad"}}',
            "[RSS] Clean finding. Tác động tới GreenNode: x. GreenNode nên: y.",
        ],
        claims=[
            Claim(
                claim="GreenNode đăng cập nhật public trên social.",
                source="[Social] GreenNode Facebook | https://facebook.com/x | fetched_at=2026-06-02",
                confidence=Confidence.HIGH,
                evidence_type=EvidenceType.SOCIAL,
            )
        ],
    )

    content = synthesize(TaskType.DAILY_INTELLIGENCE, [result])

    assert "Tin đã xác nhận" in content
    assert "Cần xác minh" in content
    assert "Dự đoán / Suy luận" in content
    assert "strategicimplications" not in content
    assert "[Social] [GreenNode Facebook](https://facebook.com/x) (2026-06-02)" in content


def test_daily_synthesis_includes_evidence_warnings():
    result = AgentResult(
        agent="daily_intelligence_agent",
        task_id="daily-1",
        status=AgentStatus.OK,
    )

    content = synthesize(
        TaskType.DAILY_INTELLIGENCE,
        [result],
        evidence_warnings=[
            "Social 'greennode-facebook': không fetch được trang social "
            "(https://www.facebook.com/greennode23): login wall"
        ],
    )

    assert "Cần xác minh" in content
    assert "không fetch được trang social" in content


def test_synthesis_formats_agent_names_and_source_links():
    result = AgentResult(
        agent="daily_intelligence_agent",
        task_id="daily-1",
        status=AgentStatus.OK,
        summary="Có tín hiệu mới cần theo dõi.",
        claims=[
            Claim(
                claim="Một cập nhật public có liên quan tới VKS.",
                source="[RSS] Vietnam.vn | https://vietnam.vn/example | retrieved_at=2026-06-02T00:00:00Z",
                confidence=Confidence.HIGH,
                evidence_type=EvidenceType.RSS,
            )
        ],
    )

    content = synthesize(TaskType.DAILY_INTELLIGENCE, [result])

    assert "**Daily Intelligence Agent:**" in content
    assert "[RSS] [Vietnam.vn](https://vietnam.vn/example) (2026-06-02)" in content
