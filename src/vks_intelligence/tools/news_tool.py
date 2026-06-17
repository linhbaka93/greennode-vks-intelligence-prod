"""Thu thập tin tức mới từ RSS (Google News) theo query đối thủ/thị trường VN.

Chuẩn hoá item thành EvidenceItem (tiêu đề, link, publisher, ngày), lọc theo cửa
sổ thời gian, và dedupe trước khi đưa cho agent.
"""

from __future__ import annotations

import hashlib
import logging
import re
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
from urllib.parse import quote_plus

from vks_intelligence.contracts import EvidenceItem, EvidenceType

log = logging.getLogger(__name__)

NEWS_QUERIES = (
    # Viettel IDC — cả hai sản phẩm: VKS (2024, mới) và vOKS (2023, vẫn active)
    "Viettel IDC VKS Kubernetes",
    "Viettel IDC vOKS Kubernetes",
    "FPT Cloud FKE Kubernetes AI",
    "Bizfly Kubernetes Engine BKE",
    "GreenNode VKS cloud",
    "GPU H100 cloud Vietnam",
    "sovereign AI cloud Vietnam 2026",
    "Kubernetes Vietnam CNCF 2026",
    # viettelidc.com.vn và viettelcloud.vn là SPA không scrape được — cover qua Google News
    "site:viettelidc.com.vn",
)

INDUSTRY_RSS_FEEDS = (
    ("cncf-blog", "https://www.cncf.io/blog/feed/"),
    ("aws-containers-blog", "https://aws.amazon.com/blogs/containers/feed/"),
    ("google-cloud-kubernetes-blog", "https://cloud.google.com/blog/products/containers-kubernetes/rss/"),
    ("kubernetes-official-blog", "https://kubernetes.io/feed.xml"),
    ("aws-news-blog", "https://aws.amazon.com/blogs/aws/feed/"),
    ("aws-ml-blog", "https://aws.amazon.com/blogs/machine-learning/feed/"),
    ("aws-hpc-blog", "https://aws.amazon.com/blogs/hpc/feed/"),
    ("azure-blog", "https://azure.microsoft.com/en-us/blog/feed/"),
)

RELEVANT_KEYWORDS = (
    "kubernetes",
    "k8s",
    "container",
    "cloud-native",
    "cncf",
    "eks",
    "gke",
    "aks",
    "vks",
    "voks",
    "bke",
    "karpenter",
    "cilium",
    "calico",
    "istio",
    "argo",
    "gitops",
    "gpu",
    "nvidia",
    "h100",
    "h200",
    "llm",
    "inference",
    "sovereign",
    "data residency",
    "pricing",
    # Hyperscaler AI/ML/HPC feeds (aws-ml/hpc, azure) — không thêm token trần
    # "ai" vì substring match sẽ dính "maintain"/"domain"
    "machine learning",
    "sagemaker",
    "bedrock",
    "generative",
    "foundation model",
    "hpc",
    "slurm",
    "azure",
    "trainium",
    "data center",
)

_GOOGLE_NEWS_RSS = "https://news.google.com/rss/search?q={query}&hl=vi&gl=VN&ceid=VN:vi"
_DEFAULT_TIMEOUT = 8
# Một số feed (fptcloud, aws WAF...) trả 403 cho UA không phải browser
_BROWSER_UA = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/126.0 Safari/537.36"
)

# Cache link Google News đã resolve → URL bài gốc (tránh resolve lại mỗi run)
_resolved_link_cache: dict[str, str] = {}


def _item_hash(title: str, url: str) -> str:
    return hashlib.md5(f"{title}|{url}".encode()).hexdigest()[:12]


def _resolve_google_news_url(link: str, timeout: int = _DEFAULT_TIMEOUT) -> str:
    """Đổi link redirect của Google News thành URL bài gốc của publisher.

    1. Fast path: decode token base64 `CBMi...` trong path → URL publisher.
    2. Fallback: follow HTTP redirect; nhận URL cuối nếu host ≠ news.google.com.
    3. Mọi lỗi → trả link cũ, không bao giờ vỡ pipeline.
    (Token thế hệ mới `AU_yqL...` không decode được — fallback redirect cover một phần;
    mitigation chính là ưu tiên direct publisher RSS/blog crawler.)
    """
    if "news.google.com" not in link:
        return link
    if link in _resolved_link_cache:
        return _resolved_link_cache[link]

    resolved = link
    m = re.search(r"news\.google\.com/(?:rss/)?articles/(CBMi[\w-]+)", link)
    if m:
        try:
            import base64

            token = m.group(1)
            decoded = base64.urlsafe_b64decode(token + "=" * (-len(token) % 4))
            # Chỉ nhận ký tự URL hợp lệ — tránh dính byte protobuf phía sau
            urls = re.findall(rb"https?://[A-Za-z0-9\-._~:/?#@!$&'()*+,;=%]+", decoded)
            for raw in urls:
                candidate = raw.decode("ascii", errors="ignore")
                if "google.com" not in candidate:
                    resolved = candidate
                    break
        except Exception:
            pass

    if resolved == link:
        try:
            import urllib.request

            req = urllib.request.Request(link, headers={"User-Agent": _BROWSER_UA})
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                final_url = resp.geturl()
            if final_url and "news.google.com" not in final_url:
                resolved = final_url
        except Exception:
            pass

    _resolved_link_cache[link] = resolved
    return resolved


def _utc_now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _parse_rss_date(date_str: str) -> str:
    """Cố parse RFC 2822 / ISO 8601 → ISO 8601 UTC. Trả chuỗi rỗng nếu không parse được."""
    if not date_str:
        return ""
    from email.utils import parsedate_to_datetime
    try:
        dt = parsedate_to_datetime(date_str)
        return dt.astimezone(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    except Exception:
        pass
    try:
        dt = datetime.fromisoformat(date_str.replace("Z", "+00:00"))
        return dt.astimezone(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    except Exception:
        return ""


def _is_within_window(published_at: str, days: int) -> bool:
    if not published_at:
        return True  # không có ngày → giữ lại
    try:
        dt = datetime.fromisoformat(published_at.replace("Z", "+00:00"))
        age_days = (datetime.now(timezone.utc) - dt.astimezone(timezone.utc)).days
        return age_days <= days
    except Exception:
        return True


def _is_relevant(title: str, snippet: str) -> bool:
    text = f"{title} {snippet}".lower()
    return any(keyword in text for keyword in RELEVANT_KEYWORDS)


def _fetch_query(query: str, days: int, timeout: int = _DEFAULT_TIMEOUT) -> list[EvidenceItem]:
    """Fetch RSS cho một query; trả list EvidenceItem hoặc [] nếu lỗi."""
    try:
        import xml.etree.ElementTree as ET
        import urllib.request

        url = _GOOGLE_NEWS_RSS.format(query=quote_plus(query))
        with urllib.request.urlopen(url, timeout=timeout) as resp:
            data = resp.read()

        root = ET.fromstring(data)
        channel = root.find("channel")
        if channel is None:
            return []

        from vks_intelligence.config import get_settings

        s = get_settings()
        resolved_count = 0
        items: list[EvidenceItem] = []
        for item in channel.findall("item"):
            title = (item.findtext("title") or "").strip()
            link = (item.findtext("link") or "").strip()
            pub_date = _parse_rss_date(item.findtext("pubDate") or "")
            source_el = item.find("source")
            publisher = source_el.text.strip() if source_el is not None and source_el.text else ""
            snippet = (item.findtext("description") or "").strip()[:300]

            if not title or not link:
                continue
            if not _is_within_window(pub_date, days):
                continue

            # Link Google News là redirect — resolve về bài gốc (cap mỗi query)
            if s.google_news_resolve_links and resolved_count < s.google_news_resolve_max:
                resolved = _resolve_google_news_url(link, timeout)
                if resolved != link:
                    link = resolved
                resolved_count += 1

            items.append(EvidenceItem(
                title=title,
                url=link,
                published_at=pub_date,
                retrieved_at=_utc_now(),
                publisher=publisher,
                snippet=snippet,
                evidence_type=EvidenceType.RSS,
                source_label="[RSS]",
                content_hash=_item_hash(title, link),
                query=query,
            ))
        return items
    except Exception as exc:
        log.warning("RSS fetch thất bại cho '%s': %s", query, exc)
        return []


def _fetch_feed(name: str, url: str, days: int, timeout: int = _DEFAULT_TIMEOUT) -> list[EvidenceItem]:
    """Fetch a direct industry RSS feed inherited from the prototype scraper set."""
    try:
        import urllib.request

        import feedparser

        req = urllib.request.Request(
            url,
            headers={"User-Agent": _BROWSER_UA},
        )
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            data = resp.read(512_000)

        feed = feedparser.parse(data)
        publisher = feed.feed.get("title", name) if getattr(feed, "feed", None) else name
        items: list[EvidenceItem] = []
        for entry in feed.entries[:30]:
            title = (entry.get("title") or "").strip()
            link = (entry.get("link") or "").strip()
            snippet = (entry.get("summary") or entry.get("description") or "").strip()[:300]
            published_at = _parse_rss_date(entry.get("published") or entry.get("updated") or "")

            if not title or not link:
                continue
            if not _is_within_window(published_at, days):
                continue
            if not _is_relevant(title, snippet):
                continue

            items.append(EvidenceItem(
                title=title,
                url=link,
                published_at=published_at,
                retrieved_at=_utc_now(),
                publisher=publisher or name,
                snippet=snippet,
                evidence_type=EvidenceType.RSS,
                source_label="[RSS]",
                content_hash=_item_hash(title, link),
                query=name,
            ))
        return items
    except Exception as exc:
        log.warning("RSS feed fetch thất bại cho '%s': %s", name, exc)
        return []


def fetch_fresh_news(days: int = 7) -> list[EvidenceItem]:
    """Trả danh sách EvidenceItem trong `days` ngày gần nhất, đã dedupe."""
    from vks_intelligence.config import get_settings

    from vks_intelligence.tools.blog_crawler import BLOG_SOURCES, fetch_blog_source

    s = get_settings()
    seen: set[str] = set()
    results: list[EvidenceItem] = []

    source_count = len(NEWS_QUERIES) + len(INDUSTRY_RSS_FEEDS) + len(BLOG_SOURCES)
    max_workers = max(1, min(s.evidence_fetch_max_workers, source_count))
    with ThreadPoolExecutor(max_workers=max_workers) as pool:
        futures = {
            pool.submit(_fetch_query, query, days, s.evidence_rss_timeout_seconds): query
            for query in NEWS_QUERIES
        }
        futures.update({
            pool.submit(_fetch_feed, name, url, days, s.evidence_rss_timeout_seconds): name
            for name, url in INDUSTRY_RSS_FEEDS
        })
        futures.update({
            pool.submit(fetch_blog_source, name, days, s.evidence_web_timeout_seconds): name
            for name in BLOG_SOURCES
        })
        for future in as_completed(futures):
            for item in future.result():
                key = _item_hash(item.title, item.url)
                if key not in seen:
                    seen.add(key)
                    results.append(item)

    # Sắp theo ngày mới nhất
    results.sort(
        key=lambda i: i.published_at or "0000",
        reverse=True,
    )
    log.info("news_tool: %d items sau dedupe (window %d ngày)", len(results), days)
    return results
