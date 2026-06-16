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


def test_weekly_digest_no_tldr_key_findings_overlap():
    """TL;DR shows top 3; Key Findings shows only items beyond top 3."""
    # Each finding has distinct content so dedup does not collapse them.
    findings = [
        "[RSS] AWS ra mắt Graviton 4 với hiệu năng tăng 40% cho workload K8s.",
        "[RSS] Viettel Cloud giảm giá GPU node pool xuống còn 0.8 USD/giờ tại VN.",
        "[RSS] CNCF công bố Kubernetes 1.32 GA với Gateway API stable.",
        "[RSS] FPT Cloud thông báo mở region Hà Nội mới hỗ trợ sovereign data.",
        "[RSS] Google Cloud ra mắt GKE Auto Mode với tự động scaling GPU nodes.",
        "[RSS] Microsoft Azure AKS tích hợp Karpenter làm node provisioner mặc định.",
    ]
    result = AgentResult(
        agent="market_trend_agent",
        task_id="w-1",
        status=AgentStatus.OK,
        key_findings=findings,
    )
    content = synthesize(TaskType.WEEKLY_DIGEST, [result])
    tldr_pos = content.index("## TL;DR")
    kf_pos = content.index("## Key Findings")
    assert "Graviton 4" in content[tldr_pos:kf_pos]
    assert "Graviton 4" not in content[kf_pos:]
    assert "FPT Cloud" in content[kf_pos:]


def test_weekly_digest_dedup_cross_agent_findings():
    """Same event phrase from two agents appears only once in output."""
    shared = "Viettel tổ chức Vietnam AI Open Hackathon 2026 cùng NVIDIA"
    r1 = AgentResult(
        agent="market_trend_agent",
        task_id="w-2",
        status=AgentStatus.OK,
        key_findings=[f"[RSS] {shared} — tác động A."],
    )
    r2 = AgentResult(
        agent="competitor_agent",
        task_id="w-2",
        status=AgentStatus.OK,
        key_findings=[f"[RSS] {shared} — tác động B."],
    )
    content = synthesize(TaskType.WEEKLY_DIGEST, [r1, r2])
    assert content.count(shared) == 1


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
