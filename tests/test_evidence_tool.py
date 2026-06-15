from pathlib import Path

from vks_intelligence.contracts import EvidenceItem, EvidenceType
from vks_intelligence.tools.evidence_tool import collect_evidence
from vks_intelligence.tools.source_tool import SourceSnapshot, social_scrape_targets


def test_collect_evidence_dedupes_normalized_rss_urls(monkeypatch, tmp_path: Path):
    def fake_news(days: int):
        return [
            EvidenceItem(
                title="VKS update",
                url="https://example.com/post?utm_source=x",
                published_at="2026-06-02T00:00:00Z",
                publisher="Example",
                evidence_type=EvidenceType.RSS,
            ),
            EvidenceItem(
                title="VKS update duplicate",
                url="https://example.com/post",
                published_at="2026-06-02T00:00:00Z",
                publisher="Example",
                evidence_type=EvidenceType.RSS,
            ),
            EvidenceItem(
                title="Missing URL",
                published_at="2026-06-02T00:00:00Z",
                publisher="Example",
                evidence_type=EvidenceType.RSS,
            ),
        ]

    monkeypatch.setattr("vks_intelligence.tools.news_tool.fetch_fresh_news", fake_news)

    bundle = collect_evidence(workspace_path=tmp_path, days=1, include_rss=True)

    assert len(bundle.items) == 1
    assert bundle.items[0].url == "https://example.com/post"
    assert bundle.items[0].source_label == "[RSS]"
    assert bundle.dedupe_stats["dedupe_dropped"] == 1
    assert any("thiếu URL" in warning for warning in bundle.warnings)


def test_scrape_snapshot_missing_source_url_is_not_promoted(monkeypatch, tmp_path: Path):
    def fake_source(name: str):
        return SourceSnapshot(
            provider=name,
            source_type="web",
            source_url="",
            fetched_at="2026-06-02T00:00:00Z",
            content_hash="abc",
            raw_data={"text_preview": "pricing page"},
        )

    monkeypatch.setattr("vks_intelligence.tools.source_tool.fetch_source", fake_source)

    bundle = collect_evidence(
        workspace_path=tmp_path,
        include_rss=False,
        include_scrape=True,
        scrape_targets=["viettel-voks"],
    )

    assert bundle.items == []
    assert any("thiếu source_url" in warning for warning in bundle.warnings)


def test_social_snapshot_is_labeled_social(monkeypatch, tmp_path: Path):
    def fake_source(name: str):
        return SourceSnapshot(
            provider=name,
            source_type="social",
            source_url="https://www.facebook.com/greennode23/posts/example",
            fetched_at="2026-06-02T00:00:00Z",
            content_hash="abc",
            raw_data={"text_preview": "GreenNode public post"},
        )

    monkeypatch.setattr("vks_intelligence.tools.source_tool.fetch_source", fake_source)

    bundle = collect_evidence(
        workspace_path=tmp_path,
        include_rss=False,
        include_scrape=True,
        scrape_targets=["greennode-facebook"],
    )

    assert len(bundle.items) == 1
    assert bundle.items[0].evidence_type == EvidenceType.SOCIAL
    assert bundle.items[0].source_label == "[Social]"


def test_social_fetch_failure_is_reported_explicitly(monkeypatch, tmp_path: Path):
    def fake_source(name: str):
        return SourceSnapshot(
            provider=name,
            source_type="social",
            source_url="https://www.facebook.com/example",
            fetched_at="2026-06-02T00:00:00Z",
            content_hash="",
            errors=["login wall"],
        )

    monkeypatch.setattr("vks_intelligence.tools.source_tool.fetch_source", fake_source)

    bundle = collect_evidence(
        workspace_path=tmp_path,
        include_rss=False,
        include_scrape=True,
        scrape_targets=["greennode-facebook"],
    )

    assert bundle.items == []
    assert any("không fetch được trang social" in warning for warning in bundle.warnings)


def test_social_targets_parked_by_default(monkeypatch):
    from vks_intelligence.config import Settings

    s = Settings(_env_file=None, enable_social_scrape=False)
    monkeypatch.setattr("vks_intelligence.config.get_settings", lambda: s)

    assert social_scrape_targets("all") == []
    assert social_scrape_targets("daily") == []


def test_social_registry_contains_core_sources_when_enabled(monkeypatch):
    from vks_intelligence.config import Settings

    s = Settings(_env_file=None, enable_social_scrape=True)
    monkeypatch.setattr("vks_intelligence.config.get_settings", lambda: s)

    targets = set(social_scrape_targets("all"))

    assert "greennode-facebook" in targets
    assert "greennode-linkedin" in targets
    assert "viettel-idc-linkedin" in targets
    assert "fpt-cloud-linkedin" in targets
    assert "bizfly-cloud-linkedin" in targets
    assert "aws-linkedin" in targets
    assert "google-cloud-linkedin" in targets
