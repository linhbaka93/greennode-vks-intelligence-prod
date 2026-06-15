from vks_intelligence.contracts import QualityVerdict, TaskType
from vks_intelligence.quality import validate_output


def test_quality_gate_flags_search_claim_without_url_and_date():
    content = "\n".join([
        "# QA",
        "[Search] Viettel công bố thay đổi pricing nhưng dòng này thiếu URL và ngày.",
    ])

    result = validate_output(content, TaskType.QA)

    assert result.verdict != QualityVerdict.PASS
    assert any("thiếu URL/ngày" in failure for failure in result.failures)


def test_quality_gate_flags_social_claim_without_date():
    content = "[Social] GreenNode Facebook có post mới https://facebook.com/greennode23/posts/x"

    result = validate_output(content, TaskType.QA)

    assert result.verdict != QualityVerdict.PASS
    assert any("thiếu ngày" in failure for failure in result.failures)
