"""Tests for memory write-back after research runs."""
from __future__ import annotations

from unittest.mock import MagicMock, patch

from vks_intelligence.contracts import AgentResult, AgentStatus
from vks_intelligence.tools.memory_writer import _format_findings, write_back_from_run


def _result(agent: str, status=AgentStatus.OK, findings=None, actions=None, risks=None, gaps=None):
    return AgentResult(
        agent=agent,
        task_id=f"t_{agent}",
        status=status,
        key_findings=findings if findings is not None else ["Finding A", "Finding B"],
        recommended_actions=actions if actions is not None else ["Action X"],
        risks=risks if risks is not None else [],
        gaps=gaps if gaps is not None else [],
        model_used="google/gemma-4-31b-it",
    )


def test_write_back_creates_local_files(tmp_path):
    results = [
        _result("competitor_agent"),
        _result("market_trend_agent"),
        _result("regulatory_agent"),
    ]
    written = write_back_from_run(results, "weekly-digest", tmp_path, "", "main", "")
    assert len(written) == 3
    assert any("competitors" in p for p in written)
    assert any("market-trends" in p for p in written)
    assert any("regulatory" in p for p in written)


def test_write_back_skips_failed_agent(tmp_path):
    results = [
        _result("competitor_agent", status=AgentStatus.FAILED),
        _result("market_trend_agent"),
    ]
    written = write_back_from_run(results, "weekly-digest", tmp_path, "", "main", "")
    assert len(written) == 1
    assert "market-trends" in written[0]


def test_write_back_skips_empty_findings(tmp_path):
    results = [
        _result("competitor_agent", findings=[]),
        _result("regulatory_agent"),
    ]
    written = write_back_from_run(results, "weekly-digest", tmp_path, "", "main", "")
    assert len(written) == 1
    assert "regulatory" in written[0]


def test_write_back_skips_unknown_agent(tmp_path):
    results = [
        _result("qa_agent"),
        _result("competitor_agent"),
    ]
    written = write_back_from_run(results, "weekly-digest", tmp_path, "", "main", "")
    assert len(written) == 1
    assert "competitors" in written[0]


def test_write_back_partial_agent_included(tmp_path):
    results = [_result("pricing_agent", status=AgentStatus.PARTIAL)]
    written = write_back_from_run(results, "weekly-digest", tmp_path, "", "main", "")
    assert len(written) == 1
    assert "pricing" in written[0]


def test_local_file_content(tmp_path):
    today = "2026-06-17"
    with patch("vks_intelligence.tools.memory_writer.date") as mock_date:
        mock_date.today.return_value = MagicMock(isoformat=lambda: today)
        results = [_result("competitor_agent", findings=["[RSS] Some finding"])]
        write_back_from_run(results, "weekly-digest", tmp_path, "", "main", "")

    written_file = next((tmp_path / "memory" / "competitors").glob("*.md"))
    content = written_file.read_text(encoding="utf-8")
    assert "Competitor Summary" in content
    assert "[RSS] Some finding" in content
    assert "weekly-digest" in content


def test_github_commit_called_when_credentials_set(tmp_path):
    results = [_result("competitor_agent")]
    with patch("vks_intelligence.tools.github_tool.commit_output") as mock_commit:
        write_back_from_run(results, "weekly-digest", tmp_path, "owner/repo", "main", "token123")
        assert mock_commit.called
        call_args = mock_commit.call_args
        assert "owner/repo" in call_args[0]
        assert "memory/competitors" in call_args[0][3]


def test_github_commit_skipped_when_no_token(tmp_path):
    results = [_result("competitor_agent")]
    with patch("vks_intelligence.tools.github_tool.commit_output") as mock_commit:
        write_back_from_run(results, "weekly-digest", tmp_path, "owner/repo", "main", "")
        assert not mock_commit.called


def test_github_commit_failure_does_not_raise(tmp_path):
    results = [_result("competitor_agent")]
    with patch("vks_intelligence.tools.github_tool.commit_output", side_effect=RuntimeError("network")):
        written = write_back_from_run(results, "weekly-digest", tmp_path, "owner/repo", "main", "tok")
        assert len(written) == 1  # local write still succeeded


def test_format_findings_all_sections():
    result = AgentResult(
        agent="competitor_agent",
        task_id="t1",
        key_findings=["Finding 1"],
        recommended_actions=["Action 1"],
        risks=["Risk 1"],
        gaps=["Gap 1"],
        model_used="qwen/qwen3-5-27b",
    )
    content = _format_findings(result, "2026-06-17", "weekly-digest")
    assert "## Key Findings" in content
    assert "## Recommended Actions" in content
    assert "## Risks" in content
    assert "## Gaps" in content
    assert "Finding 1" in content
    assert "Action 1" in content
    assert "qwen/qwen3-5-27b" in content


def test_format_findings_skips_empty_sections():
    result = AgentResult(
        agent="regulatory_agent",
        task_id="t2",
        key_findings=["Law update"],
        model_used="gemma",
    )
    content = _format_findings(result, "2026-06-17", "weekly-digest")
    assert "## Key Findings" in content
    assert "## Risks" not in content
    assert "## Gaps" not in content
