"""Crawl bài viết mới từ blog/tin tức các cloud provider VN không có RSS.

Mỗi nguồn một chiến lược đã verify với HTML thật (2026-06-12):
  - fpt-cloud-blog:    listing HTML WordPress — card `.bota_blog_list_item`,
                       ngày dạng "HH:mm dd/MM/yyyy" (giờ ICT). WAF chặn /feed/
                       và UA không phải browser → bắt buộc browser User-Agent.
  - bizfly-cloud-news: listing HTML — link "/tin-tuc/<slug>-<timestamp>.htm",
                       ngày nằm trong 14 số đầu của timestamp (yyyyMMddHHmmss, ICT).
  - greennode-blog:    sitemap.xml — <loc>https://greennode.ai/blog/...</loc> +
                       <lastmod>yyyy-MM-dd</lastmod> (trang blog render JS,
                       không scrape listing được).

Viettel Cloud (viettelcloud.vn/en/news) là Nuxt SPA không scrape tĩnh được —
cover qua Google News query "site:viettelcloud.vn" trong news_tool.NEWS_QUERIES.

Item trả về dùng EvidenceType.RSS + source_label "[Blog]" để đi nguyên qua
dedup/validation hiện có của evidence_tool (chỉ hard-gate SCRAPE/SOCIAL/SEARCH).
Nguồn first-party đã pre-scope nên KHÔNG áp RELEVANT_KEYWORDS (keyword tiếng Anh
sẽ lọc rụng bài tiếng Việt).
"""

from __future__ import annotations

import logging
import re
import urllib.request
from datetime import datetime, timezone
from zoneinfo import ZoneInfo

from vks_intelligence.contracts import EvidenceItem, EvidenceType
from vks_intelligence.tools.news_tool import _is_within_window, _item_hash, _utc_now

log = logging.getLogger(__name__)

BROWSER_UA = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/126.0 Safari/537.36"
)
_ICT = ZoneInfo("Asia/Ho_Chi_Minh")
_MAX_ITEMS_PER_SOURCE = 10
_MAX_BYTES = 1_048_576

BLOG_SOURCES = ("fpt-cloud-blog", "bizfly-cloud-news", "greennode-blog")


def _http_get(url: str, timeout: int) -> str:
    req = urllib.request.Request(
        url, headers={"User-Agent": BROWSER_UA, "Accept-Encoding": "gzip"}
    )
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        data = resp.read(_MAX_BYTES)
    # Một số server (greennode.ai) ép gzip kể cả khi client không yêu cầu
    if data[:2] == b"\x1f\x8b":
        import gzip

        data = gzip.decompress(data)
    return data.decode("utf-8", errors="replace")


def _to_utc_iso(dt: datetime) -> str:
    return dt.astimezone(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _make_item(name: str, title: str, url: str, published_at: str, snippet: str = "") -> EvidenceItem:
    return EvidenceItem(
        title=title,
        url=url,
        published_at=published_at,
        retrieved_at=_utc_now(),
        publisher=name,
        snippet=snippet[:300],
        evidence_type=EvidenceType.RSS,
        source_label="[Blog]",
        content_hash=_item_hash(title, url),
        query=name,
    )


# ──────────────────────────────────────────────────────────────────
# FPT Cloud — https://fptcloud.com/blog/
# ──────────────────────────────────────────────────────────────────

_FPT_CARD_RE = re.compile(
    r'bota_blog_list_info_item.*?<a\s[^>]*href="(https://fptcloud\.com/[^"]+)"[^>]*>\s*'
    r"([^<]{10,200})</a>.*?bota_blog_list_time_item.*?</svg>\s*([^<]+)<",
    re.DOTALL,
)
_FPT_DATE_RE = re.compile(r"(\d{1,2}):(\d{2})\s+(\d{1,2})/(\d{1,2})/(\d{4})")


def _fetch_fpt(days: int, timeout: int) -> list[EvidenceItem]:
    html = _http_get("https://fptcloud.com/blog/", timeout)
    items: list[EvidenceItem] = []
    seen: set[str] = set()
    for url, raw_title, raw_date in _FPT_CARD_RE.findall(html):
        if url in seen:
            continue
        seen.add(url)
        title = " ".join(raw_title.split())
        published_at = ""
        m = _FPT_DATE_RE.search(raw_date)
        if m:
            hour, minute, day, month, year = (int(g) for g in m.groups())
            published_at = _to_utc_iso(datetime(year, month, day, hour, minute, tzinfo=_ICT))
        if not _is_within_window(published_at, days):
            continue
        items.append(_make_item("fpt-cloud-blog", title, url, published_at))
    return items[:_MAX_ITEMS_PER_SOURCE]


# ──────────────────────────────────────────────────────────────────
# Bizfly Cloud — https://bizflycloud.vn/tin-tuc/
# ──────────────────────────────────────────────────────────────────

_BIZFLY_LINK_RE = re.compile(
    r'<a\s[^>]*href="(/tin-tuc/[a-z0-9-]+-(\d{14})\d*\.htm)"[^>]*>\s*([^<]{10,200})<'
)


def _fetch_bizfly(days: int, timeout: int) -> list[EvidenceItem]:
    html = _http_get("https://bizflycloud.vn/tin-tuc/", timeout)
    items: list[EvidenceItem] = []
    seen: set[str] = set()
    for path, stamp, raw_title in _BIZFLY_LINK_RE.findall(html):
        url = f"https://bizflycloud.vn{path}"
        if url in seen:
            continue
        seen.add(url)
        title = " ".join(raw_title.split())
        published_at = ""
        try:
            published_at = _to_utc_iso(
                datetime.strptime(stamp, "%Y%m%d%H%M%S").replace(tzinfo=_ICT)
            )
        except ValueError:
            pass
        if not _is_within_window(published_at, days):
            continue
        items.append(_make_item("bizfly-cloud-news", title, url, published_at))
    return items[:_MAX_ITEMS_PER_SOURCE]


# ──────────────────────────────────────────────────────────────────
# GreenNode — https://greennode.ai/sitemap.xml (blog render JS)
# ──────────────────────────────────────────────────────────────────

_GREENNODE_SITEMAP_RE = re.compile(
    r"<loc>(https://greennode\.ai/blog/([^<]+))</loc>\s*<lastmod>([^<]+)</lastmod>"
)
_GREENNODE_SKIP_SLUGS = {"author", "category", "tag"}
_MAX_TITLE_FETCHES = 5
_OG_TITLE_RE = re.compile(r'<meta\s[^>]*property="og:title"[^>]*content="([^"]+)"')
_TITLE_TAG_RE = re.compile(r"<title[^>]*>([^<]+)</title>")


def _fetch_article_title(url: str, timeout: int) -> str:
    try:
        html = _http_get(url, timeout)
    except Exception:
        return ""
    for pattern in (_OG_TITLE_RE, _TITLE_TAG_RE):
        m = pattern.search(html)
        if m:
            return " ".join(m.group(1).split())
    return ""


def _fetch_greennode(days: int, timeout: int) -> list[EvidenceItem]:
    xml = _http_get("https://greennode.ai/sitemap.xml", timeout)
    candidates: list[tuple[str, str, str]] = []
    for url, slug, lastmod in _GREENNODE_SITEMAP_RE.findall(xml):
        if slug.split("/")[0] in _GREENNODE_SKIP_SLUGS:
            continue
        published_at = f"{lastmod}T00:00:00Z" if re.match(r"\d{4}-\d{2}-\d{2}$", lastmod) else ""
        if not _is_within_window(published_at, days):
            continue
        candidates.append((url, slug, published_at))

    candidates.sort(key=lambda c: c[2], reverse=True)
    items: list[EvidenceItem] = []
    for i, (url, slug, published_at) in enumerate(candidates[:_MAX_ITEMS_PER_SOURCE]):
        title = _fetch_article_title(url, timeout) if i < _MAX_TITLE_FETCHES else ""
        if not title:
            title = slug.replace("-", " ").strip().capitalize()
        items.append(_make_item("greennode-blog", title, url, published_at))
    return items


# ──────────────────────────────────────────────────────────────────
# Public API
# ──────────────────────────────────────────────────────────────────

_FETCHERS = {
    "fpt-cloud-blog": _fetch_fpt,
    "bizfly-cloud-news": _fetch_bizfly,
    "greennode-blog": _fetch_greennode,
}


def fetch_blog_source(name: str, days: int, timeout: int = 10) -> list[EvidenceItem]:
    """Fetch bài mới của một nguồn blog; trả [] nếu lỗi (không vỡ pipeline)."""
    fetcher = _FETCHERS.get(name)
    if fetcher is None:
        log.warning("blog_crawler: nguồn không hỗ trợ '%s'", name)
        return []
    try:
        items = fetcher(days, timeout)
        log.info("blog_crawler: %s → %d items (window %d ngày)", name, len(items), days)
        return items
    except Exception as exc:
        log.warning("blog_crawler: fetch thất bại cho '%s': %s", name, exc)
        return []
