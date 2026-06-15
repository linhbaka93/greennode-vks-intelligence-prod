import base64

from vks_intelligence.tools import news_tool
from vks_intelligence.tools.news_tool import _is_relevant, _resolve_google_news_url


def _legacy_token(url: str) -> str:
    """Tạo token CBMi hợp lệ (protobuf bytes \\x08\\x13\\x22 + len + URL)."""
    raw = b'\x08\x13"' + bytes([len(url)]) + url.encode() + b"\xd2\x01\x00"
    return base64.urlsafe_b64encode(raw).decode().rstrip("=")


def test_resolve_decodes_legacy_cbmi_token(monkeypatch):
    news_tool._resolved_link_cache.clear()

    def no_network(*args, **kwargs):
        raise AssertionError("không được gọi network khi decode được token")

    monkeypatch.setattr("urllib.request.urlopen", no_network)

    target = "https://example.com/bai-viet-goc"
    link = f"https://news.google.com/rss/articles/{_legacy_token(target)}?oc=5"
    assert _resolve_google_news_url(link) == target


def test_resolve_returns_original_on_failure(monkeypatch):
    news_tool._resolved_link_cache.clear()

    def boom(*args, **kwargs):
        raise OSError("blocked")

    monkeypatch.setattr("urllib.request.urlopen", boom)

    link = "https://news.google.com/rss/articles/AU_yqLkhongdecode?oc=5"
    assert _resolve_google_news_url(link) == link
    # Kết quả (kể cả fail) được cache để không resolve lại
    assert link in news_tool._resolved_link_cache


def test_resolve_passthrough_non_google_links():
    assert _resolve_google_news_url("https://fptcloud.com/abc") == "https://fptcloud.com/abc"


def test_is_relevant_passes_new_hyperscaler_topics():
    assert _is_relevant("Amazon SageMaker now supports new GPU instances", "")
    assert _is_relevant("Microsoft Azure announces data center in Asia", "")
    assert _is_relevant("Running Slurm workloads", "an HPC cluster guide")
    assert _is_relevant("Anthropic foundation model on Bedrock", "")
    # Token trần "ai" KHÔNG được thêm — title không liên quan phải rớt
    assert not _is_relevant("How to maintain a domain name", "")


def test_new_feeds_registered():
    names = {name for name, _ in news_tool.INDUSTRY_RSS_FEEDS}
    assert {"aws-news-blog", "aws-ml-blog", "aws-hpc-blog", "azure-blog"} <= names
    # Feed cũ giữ nguyên
    assert {"cncf-blog", "aws-containers-blog", "kubernetes-official-blog"} <= names
    assert "site:viettelcloud.vn" in news_tool.NEWS_QUERIES
