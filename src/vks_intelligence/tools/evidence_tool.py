"""Chuẩn hóa evidence từ workspace memory, RSS, search optional và scrape allowlist.

Agent chỉ nhận `EvidenceBundle` đã validate/dedupe. Web evidence thiếu URL hoặc ngày
truy xuất/publish không được promote thành claim hợp lệ.
"""

from __future__ import annotations

import hashlib
import logging
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import parse_qsl, urlencode, urlparse, urlunparse

from vks_intelligence.contracts import Confidence, EvidenceBundle, EvidenceItem, EvidenceType

log = logging.getLogger(__name__)

_TRACKING_PARAMS = {
    "utm_source",
    "utm_medium",
    "utm_campaign",
    "utm_term",
    "utm_content",
    "fbclid",
    "gclid",
}


def _utc_now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _hash_text(text: str) -> str:
    return hashlib.sha256(text.encode()).hexdigest()[:16]


def _normalize_url(url: str) -> str:
    if not url:
        return ""
    parsed = urlparse(url.strip())
    query = urlencode(
        [(k, v) for k, v in parse_qsl(parsed.query, keep_blank_values=True) if k not in _TRACKING_PARAMS],
        doseq=True,
    )
    return urlunparse((
        parsed.scheme.lower(),
        parsed.netloc.lower(),
        parsed.path.rstrip("/"),
        parsed.params,
        query,
        "",
    ))


def _label_for(evidence_type: EvidenceType) -> str:
    labels = {
        EvidenceType.MEMORY: "[Workspace]",
        EvidenceType.RSS: "[RSS]",
        EvidenceType.SCRAPE: "[Scrape]",
        EvidenceType.SOCIAL: "[Social]",
        EvidenceType.SEARCH: "[Search]",
        EvidenceType.MANUAL: "[Workspace]",
    }
    return labels.get(evidence_type, "[Workspace]")


def _normalize_item(item: EvidenceItem) -> EvidenceItem:
    url = _normalize_url(item.url)
    content_basis = "|".join([
        item.title.strip(),
        url,
        item.publisher.strip(),
        item.snippet.strip()[:500],
    ])
    if not item.source_label:
        item.source_label = _label_for(item.evidence_type)
    item.url = url
    if not item.retrieved_at:
        item.retrieved_at = _utc_now()
    if not item.content_hash:
        item.content_hash = _hash_text(content_basis)
    return item


def _dedupe_key(item: EvidenceItem) -> str:
    if item.url:
        return f"url:{item.url}"
    if item.content_hash:
        return f"hash:{item.content_hash}"
    return f"title:{item.title.strip().lower()}"


def _is_valid_web_item(item: EvidenceItem) -> tuple[bool, str]:
    if item.evidence_type not in (EvidenceType.SEARCH, EvidenceType.SCRAPE, EvidenceType.SOCIAL):
        return True, ""
    if not item.url:
        return False, f"{item.source_label}: loại '{item.title[:60]}' vì thiếu URL"
    if not (item.published_at or item.retrieved_at):
        return False, f"{item.source_label}: loại '{item.title[:60]}' vì thiếu ngày"
    return True, ""


def _rss_to_items(days: int) -> tuple[list[EvidenceItem], list[str]]:
    warnings: list[str] = []
    try:
        from vks_intelligence.tools.news_tool import fetch_fresh_news

        items = [_normalize_item(i) for i in fetch_fresh_news(days=days)]
    except Exception as exc:
        return [], [f"RSS fetch thất bại: {exc}"]

    kept: list[EvidenceItem] = []
    for item in items:
        if not item.url:
            warnings.append(f"RSS: loại '{item.title[:60]}' vì thiếu URL")
            continue
        if not item.published_at:
            warnings.append(f"RSS: '{item.title[:60]}' không có published_at từ feed")
        kept.append(item)
    return kept, warnings


def _scrape_warning(target: str, snap) -> str:
    if snap.source_type == "social":
        url_part = f" ({snap.source_url})" if snap.source_url else ""
        return f"Social '{target}': không fetch được trang social{url_part}"
    return f"Scrape '{target}'"


def _scrape_to_items(scrape_targets: list[str]) -> tuple[list[EvidenceItem], list[str]]:
    from vks_intelligence.tools.source_tool import fetch_source
    from vks_intelligence.config import get_settings

    items: list[EvidenceItem] = []
    warnings: list[str] = []
    s = get_settings()
    max_workers = max(1, min(s.evidence_fetch_max_workers, len(scrape_targets)))

    with ThreadPoolExecutor(max_workers=max_workers) as pool:
        futures = {pool.submit(fetch_source, target): target for target in scrape_targets}
        for future in as_completed(futures):
            target = futures[future]
            try:
                snap = future.result()
            except Exception as exc:
                warnings.append(f"Scrape '{target}': fetch failed: {exc}")
                continue

            item, item_warnings = _snapshot_to_item(target, snap)
            warnings.extend(item_warnings)
            if item:
                items.append(item)
    return items, warnings


def _snapshot_to_item(target: str, snap) -> tuple[EvidenceItem | None, list[str]]:
    warnings: list[str] = []

    if snap.errors:
        warnings.append(f"{_scrape_warning(target, snap)}: {snap.errors[0]}")
        return None, warnings
    if not (snap.source_url and snap.fetched_at and snap.provider and snap.source_type):
        warnings.append(f"Scrape '{target}': thiếu source_url/fetched_at/provider/source_type")
        return None, warnings

    preview = snap.raw_data.get("text_preview", "")
    if not preview:
        warnings.append(f"{_scrape_warning(target, snap)}: không có nội dung text để promote")
        return None, warnings

    return _normalize_item(EvidenceItem(
        title=f"Snapshot: {target}",
        url=snap.source_url,
        published_at=snap.fetched_at,
        retrieved_at=snap.fetched_at,
        publisher=snap.provider,
        snippet=preview[:500],
        evidence_type=EvidenceType.SOCIAL
        if snap.source_type == "social"
        else EvidenceType.SCRAPE,
        confidence=Confidence(snap.confidence),
        source_label="[Social]" if snap.source_type == "social" else "[Scrape]",
        content_hash=snap.content_hash,
    )), warnings


def _source_counts(items: list[EvidenceItem], include_workspace: bool) -> dict[str, int]:
    counts: dict[str, int] = {"workspace": 1 if include_workspace else 0}
    for item in items:
        key = item.evidence_type.value
        counts[key] = counts.get(key, 0) + 1
    return counts


def collect_evidence(
    query: str = "",
    scope: str = "",
    days: int = 7,
    *,
    include_workspace: bool = True,
    include_rss: bool = True,
    include_search: bool = False,
    include_scrape: bool = False,
    workspace_path: Path | None = None,
    scrape_targets: list[str] | None = None,
    memory_cap: int = 10_000,
) -> EvidenceBundle:
    """Gom evidence từ nguồn cho phép và trả bundle đã validate/dedupe."""
    from vks_intelligence.config import get_settings
    from vks_intelligence.tools.memory_tool import load_memory

    s = get_settings()
    workspace = workspace_path or s.workspace_path
    generated_at = _utc_now()
    memory_context = ""
    items: list[EvidenceItem] = []
    warnings: list[str] = []
    sources_used: list[str] = []
    invalid_dropped = 0

    if include_workspace:
        memory_context = load_memory(workspace, context_cap=memory_cap)
        sources_used.append("workspace_memory")

    if include_rss:
        rss_items, rss_warnings = _rss_to_items(days)
        items.extend(rss_items)
        warnings.extend(rss_warnings)
        if rss_items:
            sources_used.append(f"rss({len(rss_items)} items)")

    if include_search:
        warnings.append("Search adapter chưa bật; dùng RSS/scrape allowlist làm nguồn miễn phí mặc định.")

    if include_scrape and scrape_targets:
        scrape_items, scrape_warnings = _scrape_to_items(scrape_targets)
        items.extend(scrape_items)
        warnings.extend(scrape_warnings)
        if scrape_items:
            sources_used.append(f"scrape({len(scrape_items)} items)")

    validated: list[EvidenceItem] = []
    for item in [_normalize_item(i) for i in items]:
        ok, warning = _is_valid_web_item(item)
        if not ok:
            invalid_dropped += 1
            warnings.append(warning)
            continue
        validated.append(item)

    seen: set[str] = set()
    deduped: list[EvidenceItem] = []
    for item in validated:
        key = _dedupe_key(item)
        if key in seen:
            continue
        seen.add(key)
        deduped.append(item)

    dedupe_dropped = len(validated) - len(deduped)
    source_counts = _source_counts(deduped, include_workspace)
    dedupe_stats = {
        "raw_items": len(items),
        "invalid_dropped": invalid_dropped,
        "dedupe_dropped": dedupe_dropped,
        "final_items": len(deduped),
    }

    log.info(
        "evidence_tool: final=%d invalid=%d dedupe=%d counts=%s warnings=%d",
        len(deduped),
        invalid_dropped,
        dedupe_dropped,
        source_counts,
        len(warnings),
    )

    return EvidenceBundle(
        query=query or scope,
        generated_at=generated_at,
        items=deduped,
        memory_context=memory_context,
        collected_at=generated_at,
        days_window=days,
        sources_used=sources_used,
        source_counts=source_counts,
        dedupe_stats=dedupe_stats,
        warnings=warnings,
    )


def collect(
    workspace_path: Path,
    *,
    days: int = 7,
    include_rss: bool = True,
    include_scrape: bool = False,
    scrape_targets: list[str] | None = None,
    memory_cap: int = 10_000,
) -> EvidenceBundle:
    """Backward-compatible wrapper cho supervisor hiện tại."""
    return collect_evidence(
        days=days,
        include_workspace=True,
        include_rss=include_rss,
        include_scrape=include_scrape,
        workspace_path=workspace_path,
        scrape_targets=scrape_targets,
        memory_cap=memory_cap,
    )
