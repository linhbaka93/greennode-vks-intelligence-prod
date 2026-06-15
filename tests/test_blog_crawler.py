from datetime import datetime, timezone

from vks_intelligence.tools import blog_crawler


_FPT_HTML = """
<div class="bota_blog_list_item">
  <div class="bota_blog_list_info_item">
    <h3><a href="https://fptcloud.com/bai-viet-moi-nhat/" title="x">
      Bài viết mới nhất về Kubernetes
    </a></h3>
    <div class="bota_blog_list_time_item"><svg></svg> 13:26 04/06/2026 </div>
  </div>
</div>
<div class="bota_blog_list_item">
  <div class="bota_blog_list_info_item">
    <h3><a href="https://fptcloud.com/bai-viet-moi-nhat/" title="x">
      Bài viết mới nhất về Kubernetes
    </a></h3>
    <div class="bota_blog_list_time_item"><svg></svg> 13:26 04/06/2026 </div>
  </div>
</div>
"""

_BIZFLY_HTML = """
<a href="/tin-tuc/bai-moi-ve-cloud-server-20260610144020355.htm">Bài mới về cloud server</a>
<a href="/tin-tuc/bai-cu-tu-2021-20211220004118384.htm">Bài cũ từ 2021 về linux</a>
"""

_GREENNODE_SITEMAP = """<?xml version="1.0" encoding="UTF-8"?>
<urlset>
<url><loc>https://greennode.ai/blog/author</loc><lastmod>2026-06-10</lastmod></url>
<url><loc>https://greennode.ai/blog/kubernetes-startup-deploy</loc><lastmod>2026-06-10</lastmod></url>
<url><loc>https://greennode.ai/blog/bai-rat-cu</loc><lastmod>2020-01-01</lastmod></url>
</urlset>
"""


def _freeze_window(monkeypatch, now_utc: datetime):
    """_is_within_window so với datetime.now — fixture dùng ngày cố định nên patch now."""

    def fake_window(published_at: str, days: int) -> bool:
        if not published_at:
            return True
        dt = datetime.fromisoformat(published_at.replace("Z", "+00:00"))
        return (now_utc - dt.astimezone(timezone.utc)).days <= days

    monkeypatch.setattr(blog_crawler, "_is_within_window", fake_window)


def test_fetch_fpt_parses_cards_and_dedupes(monkeypatch):
    monkeypatch.setattr(blog_crawler, "_http_get", lambda url, timeout: _FPT_HTML)
    _freeze_window(monkeypatch, datetime(2026, 6, 12, tzinfo=timezone.utc))

    items = blog_crawler.fetch_blog_source("fpt-cloud-blog", days=14)

    assert len(items) == 1
    item = items[0]
    assert item.title == "Bài viết mới nhất về Kubernetes"
    assert item.url == "https://fptcloud.com/bai-viet-moi-nhat/"
    # 13:26 ICT = 06:26 UTC
    assert item.published_at == "2026-06-04T06:26:00Z"
    assert item.source_label == "[Blog]"
    assert item.evidence_type.value == "rss"


def test_fetch_bizfly_date_from_slug_and_window(monkeypatch):
    monkeypatch.setattr(blog_crawler, "_http_get", lambda url, timeout: _BIZFLY_HTML)
    _freeze_window(monkeypatch, datetime(2026, 6, 12, tzinfo=timezone.utc))

    items = blog_crawler.fetch_blog_source("bizfly-cloud-news", days=7)

    assert len(items) == 1
    item = items[0]
    assert item.url.startswith("https://bizflycloud.vn/tin-tuc/bai-moi")
    # 2026-06-10 14:40:20 ICT = 07:40:20 UTC
    assert item.published_at == "2026-06-10T07:40:20Z"


def test_fetch_greennode_sitemap_skips_author_and_old(monkeypatch):
    monkeypatch.setattr(blog_crawler, "_http_get", lambda url, timeout: _GREENNODE_SITEMAP)
    monkeypatch.setattr(blog_crawler, "_fetch_article_title", lambda url, timeout: "Tiêu đề thật")
    _freeze_window(monkeypatch, datetime(2026, 6, 12, tzinfo=timezone.utc))

    items = blog_crawler.fetch_blog_source("greennode-blog", days=7)

    assert len(items) == 1
    assert items[0].url == "https://greennode.ai/blog/kubernetes-startup-deploy"
    assert items[0].title == "Tiêu đề thật"
    assert items[0].published_at == "2026-06-10T00:00:00Z"


def test_unknown_source_returns_empty():
    assert blog_crawler.fetch_blog_source("khong-ton-tai", days=7) == []


def test_fetch_error_returns_empty(monkeypatch):
    def boom(url, timeout):
        raise OSError("network down")

    monkeypatch.setattr(blog_crawler, "_http_get", boom)
    assert blog_crawler.fetch_blog_source("fpt-cloud-blog", days=7) == []
