"""Persist agent findings from research runs back to dated memory files.

Sau mỗi research run thành công (quality.passed), supervisor gọi
write_back_from_run() để tạo file .md có ngày hôm nay trong memory/.
File mới có date > threshold → _is_stale() trả False → run kế tiếp
nhận fresh context thay vì STALE stub.

GitHub commit: dùng github_tool.commit_output() để persist across deploys.
Lỗi commit không block run — chỉ log warning.
"""

from __future__ import annotations

import logging
from datetime import date
from pathlib import Path

from vks_intelligence.contracts import AgentResult, AgentStatus

log = logging.getLogger(__name__)

# Map agent name → memory subfolder
_AGENT_FOLDER: dict[str, str] = {
    "competitor_agent": "competitors",
    "market_trend_agent": "market-trends",
    "regulatory_agent": "regulatory",
    "pricing_agent": "pricing",
    "positioning_agent": "greennode",
}


def write_back_from_run(
    results: list[AgentResult],
    task_type_value: str,
    workspace_path: Path,
    github_repo: str,
    github_branch: str,
    github_token: str,
) -> list[str]:
    """Write key_findings from successful agents to dated memory files.

    Skips agents with status FAILED or empty key_findings.
    Returns list of relative paths written (e.g. "memory/competitors/...").
    """
    today = date.today().isoformat()
    written: list[str] = []

    for result in results:
        if result.status == AgentStatus.FAILED or not result.key_findings:
            continue
        folder = _AGENT_FOLDER.get(result.agent)
        if not folder:
            continue

        agent_short = result.agent.replace("_agent", "")
        filename = f"{today}-{agent_short}-summary.md"
        content = _format_findings(result, today, task_type_value)
        rel_path = f"memory/{folder}/{filename}"

        # Write local — available for same-container runs immediately
        local_path = workspace_path / "memory" / folder / filename
        try:
            local_path.parent.mkdir(parents=True, exist_ok=True)
            local_path.write_text(content, encoding="utf-8")
        except Exception as exc:
            log.warning("memory_writer: local write failed for %s: %s", filename, exc)
            continue

        # Commit to GitHub — survives across container deploys
        if github_repo and github_token:
            try:
                from vks_intelligence.tools.github_tool import commit_output
                commit_output(
                    github_repo,
                    github_branch,
                    github_token,
                    rel_path,
                    content,
                    f"chore: update {folder} from {task_type_value} {today}",
                )
            except Exception as exc:
                log.warning(
                    "memory_writer: github commit failed for %s: %s", filename, exc
                )

        written.append(rel_path)
        log.info("memory_writer: wrote %s", rel_path)

    return written


def _format_findings(result: AgentResult, today: str, task_type: str) -> str:
    agent_label = result.agent.replace("_agent", "").replace("_", " ").title()
    lines = [
        f"# {agent_label} Summary — {today}",
        "",
        f"Source: {task_type} run | Model: {result.model_used}",
        "",
    ]

    if result.key_findings:
        lines += ["## Key Findings", ""]
        for item in result.key_findings:
            lines.append(f"- {item}")
        lines.append("")

    if result.recommended_actions:
        lines += ["## Recommended Actions", ""]
        for item in result.recommended_actions:
            lines.append(f"- {item}")
        lines.append("")

    if result.risks:
        lines += ["## Risks", ""]
        for item in result.risks:
            lines.append(f"- {item}")
        lines.append("")

    if result.gaps:
        lines += ["## Gaps / Thiếu dữ liệu", ""]
        for item in result.gaps:
            lines.append(f"- {item}")
        lines.append("")

    return "\n".join(lines)
