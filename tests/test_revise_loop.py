"""Tests cho M2: revise loop + citation grader."""

from unittest.mock import MagicMock, patch

from vks_intelligence.contracts import AgentResult, AgentStatus, QualityVerdict, TaskType
from vks_intelligence.synthesis import synthesize


# ------------------------------------------------------------------
# Synthesis — revise_hint
# ------------------------------------------------------------------

def test_synthesize_revise_hint_appears_in_gaps():
    result = AgentResult(agent="market_trend_agent", task_id="t1", status=AgentStatus.OK)
    hints = ["Output quá ngắn (150 ký tự)", "Thiếu section bắt buộc: Sources"]

    content = synthesize(TaskType.WEEKLY_DIGEST, [result], revise_hint=hints)

    assert "[Cần sửa] Output quá ngắn" in content
    assert "[Cần sửa] Thiếu section bắt buộc" in content
    assert "Giới hạn dữ liệu" in content


def test_synthesize_no_revise_hint_no_can_sua():
    result = AgentResult(
        agent="market_trend_agent",
        task_id="t1",
        status=AgentStatus.OK,
        key_findings=["[RSS] Finding A — tác động. GreenNode nên: theo dõi."],
    )

    content = synthesize(TaskType.WEEKLY_DIGEST, [result])

    assert "[Cần sửa]" not in content


# ------------------------------------------------------------------
# Supervisor — _decide_publish revise escalation
# ------------------------------------------------------------------

def _make_quality(verdict: QualityVerdict, score: float):
    from vks_intelligence.contracts import QualityResult
    return QualityResult(verdict=verdict, score=score, failures=["test failure"])


def test_decide_publish_revise_no_retry_is_silent_block():
    from vks_intelligence.supervisor import Supervisor
    sup = Supervisor.__new__(Supervisor)
    req = MagicMock(dry_run=False, human_approval_required=False)
    q = _make_quality(QualityVerdict.REVISE, 0.55)

    published, approval = sup._decide_publish(req, q, MagicMock(), revise_count=0)

    assert published is False
    assert approval is False  # silent block (no retry yet)


def test_decide_publish_revise_after_retry_escalates_to_approval():
    from vks_intelligence.supervisor import Supervisor
    sup = Supervisor.__new__(Supervisor)
    req = MagicMock(dry_run=False, human_approval_required=False)
    q = _make_quality(QualityVerdict.REVISE, 0.55)

    published, approval = sup._decide_publish(req, q, MagicMock(), revise_count=1)

    assert published is False
    assert approval is True  # escalated to needs_review after retry


def test_decide_publish_blocked_never_approval():
    from vks_intelligence.supervisor import Supervisor
    sup = Supervisor.__new__(Supervisor)
    req = MagicMock(dry_run=False, human_approval_required=False)
    q = _make_quality(QualityVerdict.BLOCKED, 0.30)

    published, approval = sup._decide_publish(req, q, MagicMock(), revise_count=1)

    assert published is False
    assert approval is False


# ------------------------------------------------------------------
# Citation grader
# ------------------------------------------------------------------

def test_grade_citations_no_urls():
    from vks_intelligence.tools.citation_grader import grade_citations

    dead = grade_citations("Không có URL trong đây.")

    assert dead == []


def test_grade_citations_dedup_urls():
    from vks_intelligence.tools.citation_grader import grade_citations

    markdown = (
        "[RSS] [GreenNode](https://greennode.vn) 2026-06-01 — finding.\n"
        "[RSS] [GreenNode](https://greennode.vn) 2026-06-02 — khác.\n"
    )

    with patch("vks_intelligence.tools.citation_grader._head_check", return_value=True):
        dead = grade_citations(markdown)

    assert dead == []


def test_grade_citations_marks_4xx_as_dead():
    from vks_intelligence.tools.citation_grader import grade_citations

    markdown = "- [RSS] [Bad link](https://example.com/dead) 2026-06-01 — bad."

    with patch("vks_intelligence.tools.citation_grader._head_check", return_value=False):
        dead = grade_citations(markdown)

    assert "https://example.com/dead" in dead


def test_grade_citations_network_error_is_not_dead():
    from vks_intelligence.tools.citation_grader import grade_citations

    markdown = "- [RSS] [Error link](https://example.com/err) 2026-06-01 — err."

    with patch(
        "vks_intelligence.tools.citation_grader._head_check",
        side_effect=Exception("connection refused"),
    ):
        dead = grade_citations(markdown)

    assert dead == []
