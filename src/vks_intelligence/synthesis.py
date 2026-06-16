"""Gộp nhiều AgentResult thành output markdown cuối.

Nạp `prompts/_report_templates.md` cho cấu trúc weekly/monthly (thứ tự section, format
action-item 4 trường, watch list, footer) và `prompts/_output_policy.md` cho nhãn
nguồn inline + dòng so-what + block giới hạn dữ liệu.

Chỉ đọc claim đã structured và validate. Mỗi claim mang theo nguồn và nhãn; synthesis
giữ nguyên truy xuất nguồn, không bịa thêm số liệu ngoài claim. Không có claim có nguồn
thì không sinh recommendation tương ứng.
"""

from __future__ import annotations

from datetime import datetime, timezone
import re

from vks_intelligence.contracts import (
    AgentResult,
    AgentStatus,
    Claim,
    Confidence,
    EvidenceType,
    TaskType,
)

_RAW_JSON_HINTS = (
    '"summary"',
    '"key_findings"',
    '"keyfindings"',
    '"strategicimplications"',
    '"recommended_actions"',
    '"risks"',
    '"gaps"',
)

_URL_RE = re.compile(r"https?://[^\s|)>\]]+")
_DATE_RE = re.compile(r"(20\d{2}-\d{2}-\d{2}|retrieved_at=([^\s|]+)|fetched_at=([^\s|]+))")


def synthesize(
    task_type: TaskType,
    results: list[AgentResult],
    *,
    evidence_warnings: list[str] | None = None,
) -> str:
    """Sinh markdown theo template TL;DR → ... → Sources, output tiếng Việt."""
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    ok = [r for r in results if r.status != AgentStatus.FAILED]

    findings: list[str] = []
    actions: list[str] = []
    risks: list[str] = []
    gaps: list[str] = []
    sources: list[str] = []
    claims: list[Claim] = []

    for r in ok:
        findings.extend(_clean_items(r.key_findings))
        actions.extend(_clean_items(r.recommended_actions))
        risks.extend(_clean_items(r.risks))
        gaps.extend(_clean_items(r.gaps))
        if r.json_parse_status != "valid":
            gaps.append(f"{r.agent}: output JSON không hợp lệ; chỉ dùng claim đã parse được.")
        for c in r.claims:
            claims.append(c)
            if c.source and c.source not in sources:
                sources.append(c.source)
    if evidence_warnings:
        gaps.extend(_clean_items(evidence_warnings))

    if task_type == TaskType.DAILY_INTELLIGENCE:
        return _daily_intelligence(ok, claims, findings, actions, risks, gaps, sources, now)
    if task_type == TaskType.WEEKLY_DIGEST:
        return _weekly_digest(ok, findings, actions, risks, gaps, sources, now)
    if task_type == TaskType.COMPETITOR_MONITOR:
        return _competitor_monitor(ok, findings, actions, risks, sources, now)
    if task_type in (TaskType.BATTLECARD, TaskType.PRICING_ANALYSIS):
        return _single_agent_report(ok, task_type.value, findings, actions, risks, sources, now)
    return _generic_report(task_type.value, ok, findings, actions, sources, now)


# ------------------------------------------------------------------
# Builders
# ------------------------------------------------------------------

def _looks_like_raw_json(item: str) -> bool:
    stripped = item.strip()
    if not stripped:
        return False
    if stripped.startswith("{") or stripped.startswith("[{"):
        return True
    return sum(1 for hint in _RAW_JSON_HINTS if hint in stripped.lower()) >= 2


def _clean_items(items: list[str]) -> list[str]:
    cleaned: list[str] = []
    for item in items:
        if not item or _looks_like_raw_json(item):
            continue
        cleaned.append(item.strip())
    return cleaned


def _claim_line(claim: Claim) -> str:
    source = _format_source_markdown(claim.source)
    if source:
        return f"{source} - {claim.claim}"
    return claim.claim


def _agent_label(agent: str) -> str:
    words = agent.replace("_", " ").replace("-", " ").split()
    return " ".join(word[:1].upper() + word[1:] for word in words)


def _source_title_from_text(source: str, url: str) -> str:
    without_url = re.sub(r"^\s*\[[^\]]+\]\s*", "", source.replace(url, ""))
    pieces = [p.strip(" -|()[]") for p in without_url.split("|")]
    for piece in pieces:
        if not piece or piece.lower().startswith(("retrieved_at", "fetched_at", "published_at")):
            continue
        if piece.lower() in {"rss", "social", "scrape", "search", "workspace"}:
            continue
        return piece
    try:
        from urllib.parse import urlparse

        host = urlparse(url).netloc.replace("www.", "")
        return host or "Source"
    except Exception:
        return "Source"


def _source_date_from_text(source: str) -> str:
    match = _DATE_RE.search(source)
    if not match:
        return ""
    value = match.group(2) or match.group(3) or match.group(1)
    if value.startswith(("retrieved_at=", "fetched_at=")):
        value = value.split("=", 1)[1]
    return value[:10]


def _format_source_markdown(source: str) -> str:
    """Compact source strings so Telegram renders named links instead of full URLs."""
    source = source.strip()
    if not source:
        return ""

    match = _URL_RE.search(source)
    if not match:
        return source

    url = match.group(0)
    label_match = re.match(r"^\s*(\[[^\]]+\])", source)
    label = label_match.group(1) if label_match else ""
    title = _source_title_from_text(source, url)
    date = _source_date_from_text(source)
    date_part = f" ({date})" if date else ""
    prefix = f"{label} " if label else ""
    return f"{prefix}[{title}]({url}){date_part}"


def _confirmed_claims(claims: list[Claim]) -> list[str]:
    valid_types = {
        EvidenceType.MEMORY,
        EvidenceType.RSS,
        EvidenceType.SCRAPE,
        EvidenceType.SOCIAL,
        EvidenceType.SEARCH,
    }
    return [
        _claim_line(c)
        for c in claims
        if c.claim
        and c.confidence in (Confidence.HIGH, Confidence.MEDIUM)
        and c.evidence_type in valid_types
    ]


def _verification_claims(claims: list[Claim], gaps: list[str]) -> list[str]:
    items = [
        _claim_line(c)
        for c in claims
        if c.claim and (c.confidence == Confidence.LOW or c.evidence_type == EvidenceType.MANUAL)
    ]
    items.extend(gaps)
    return _clean_items(items)


def _forecast_items(claims: list[Claim], risks: list[str]) -> list[str]:
    inferred = [
        _claim_line(c)
        for c in claims
        if "suy luận" in c.source.lower() or "dự đoán" in c.claim.lower()
    ]
    inferred.extend(risks)
    return _clean_items(inferred)

def _tldr(findings: list[str], risks: list[str]) -> str:
    top = findings[:3] if findings else ["Không có tín hiệu đáng chú ý trong kỳ này."]
    lines = "\n".join(f"- {f}" for f in top)
    return f"## TL;DR\n\n{lines}\n"


def _findings_section(findings: list[str]) -> str:
    if not findings:
        return "## Key Findings\n\n_Không có finding trong kỳ này._\n"
    items = "\n".join(f"- {f}" for f in findings)
    return f"## Key Findings\n\n{items}\n"


def _risks_section(risks: list[str]) -> str:
    if not risks:
        return ""
    items = "\n".join(f"- {r}" for r in risks)
    return f"## Rủi ro cần theo dõi\n\n{items}\n"


def _actions_section(actions: list[str]) -> str:
    if not actions:
        return ""
    items = "\n".join(f"- {a}" for a in actions)
    return f"## Action Items\n\n{items}\n"


def _gaps_section(gaps: list[str]) -> str:
    if not gaps:
        return ""
    items = "\n".join(f"- {g}" for g in gaps)
    return f"⚠️ **Giới hạn dữ liệu**\n\n{items}\n"


def _sources_section(sources: list[str]) -> str:
    if not sources:
        return "## Sources\n\n_Tất cả dữ liệu từ workspace memory._\n"
    items = "\n".join(f"- {_format_source_markdown(s)}" for s in sources[:20])
    return f"## Sources\n\n{items}\n"


def _section_with_fallback(title: str, items: list[str], fallback: str, limit: int = 8) -> str:
    if not items:
        return f"## {title}\n\n_{fallback}_\n"
    body = "\n".join(f"- {item}" for item in items[:limit])
    if len(items) > limit:
        body += f"\n- ... {len(items) - limit} mục khác trong artifact."
    return f"## {title}\n\n{body}\n"


def _agent_summaries(results: list[AgentResult]) -> str:
    if not results:
        return ""
    parts = []
    for r in results:
        if r.json_parse_status != "valid":
            parts.append(
                f"**{_agent_label(r.agent)}:** output chưa đúng schema; "
                "đã loại raw output khỏi bản tin."
            )
            continue
        if r.summary and not _looks_like_raw_json(r.summary):
            parts.append(f"**{_agent_label(r.agent)}:** {r.summary}")
    if not parts:
        return ""
    return "## Phân tích chi tiết\n\n" + "\n\n".join(parts) + "\n"


def _weekly_digest(
    ok: list[AgentResult],
    findings: list[str],
    actions: list[str],
    risks: list[str],
    gaps: list[str],
    sources: list[str],
    now: str,
) -> str:
    sections = [
        f"# GreenNode VKS Intelligence — Weekly Digest\n\n📅 {now}\n",
        _tldr(findings, risks),
        _findings_section(findings),
        _risks_section(risks),
        _actions_section(actions),
        _gaps_section(gaps),
        _sources_section(sources),
    ]
    return "\n".join(s for s in sections if s)


def _daily_intelligence(
    ok: list[AgentResult],
    claims: list[Claim],
    findings: list[str],
    actions: list[str],
    risks: list[str],
    gaps: list[str],
    sources: list[str],
    now: str,
) -> str:
    confirmed = _confirmed_claims(claims)
    if not confirmed:
        confirmed = [f for f in findings if f.startswith(("[Workspace]", "[RSS]", "[Scrape]", "[Social]", "[Search]"))]

    needs_verification = _verification_claims(claims, gaps)
    forecasts = _forecast_items(claims, risks)

    sections = [
        f"# GreenNode VKS Intelligence — Daily Brief\n\n📅 {now}\n",
        _tldr(confirmed or findings, risks),
        _section_with_fallback(
            "Tin đã xác nhận",
            confirmed,
            "Không có tin mới đã xác nhận trong cửa sổ hiện tại.",
        ),
        _section_with_fallback(
            "Cần xác minh",
            needs_verification,
            "Không có nguồn nào cần xác minh thêm.",
            limit=20,
        ),
        _section_with_fallback(
            "Dự đoán / Suy luận",
            forecasts,
            "Không tạo dự đoán vì chưa đủ evidence mới.",
        ),
        _actions_section(actions),
        _agent_summaries(ok),
        _sources_section(sources),
    ]
    return "\n".join(s for s in sections if s)


def _competitor_monitor(
    ok: list[AgentResult],
    findings: list[str],
    actions: list[str],
    risks: list[str],
    sources: list[str],
    now: str,
) -> str:
    if not findings:
        body = "_Không có thay đổi đáng kể từ đối thủ trong kỳ này._"
    else:
        body = "\n".join(f"- {f}" for f in findings)

    sections = [
        f"# Competitor Monitor\n\n📅 {now}\n",
        f"## Động thái đối thủ\n\n{body}\n",
        _risks_section(risks),
        _actions_section(actions),
        _sources_section(sources),
    ]
    return "\n".join(s for s in sections if s)


def _single_agent_report(
    ok: list[AgentResult],
    label: str,
    findings: list[str],
    actions: list[str],
    risks: list[str],
    sources: list[str],
    now: str,
) -> str:
    sections = [
        f"# {label.replace('-', ' ').title()} — GreenNode VKS\n\n📅 {now}\n",
        _tldr(findings, risks),
        _findings_section(findings),
        _agent_summaries(ok),
        _risks_section(risks),
        _actions_section(actions),
        _sources_section(sources),
    ]
    return "\n".join(s for s in sections if s)


def _generic_report(
    label: str,
    ok: list[AgentResult],
    findings: list[str],
    actions: list[str],
    sources: list[str],
    now: str,
) -> str:
    sections = [
        f"# {label} — GreenNode VKS\n\n📅 {now}\n",
        _findings_section(findings),
        _agent_summaries(ok),
        _actions_section(actions),
        _sources_section(sources),
    ]
    return "\n".join(s for s in sections if s)
