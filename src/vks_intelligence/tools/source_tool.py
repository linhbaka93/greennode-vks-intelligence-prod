"""Scrape trang pricing/feature đối thủ và diff so với snapshot trước.

Mỗi nguồn trả về snapshot kèm confidence và content hash để phát hiện thay đổi
có nghĩa, tránh alert nhiễu.
"""

from __future__ import annotations

import hashlib
import logging
from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any

log = logging.getLogger(__name__)

# Danh sách URL public cho phép scrape — không crawl ngoài allowlist
_SCRAPE_ALLOWLIST: dict[str, str] = {
    "viettel-voks": "https://viettelcloud.vn/san-pham/kubernetes",
    "fpt-fke": "https://fptcloud.com/kubernetes",
    "bizfly-bke": "https://bizflycloud.vn/kubernetes",
    "aws-eks-pricing": "https://aws.amazon.com/eks/pricing/",
    "gke-pricing": "https://cloud.google.com/kubernetes-engine/pricing",
    "greennode-facebook": "https://www.facebook.com/greennode23",
    "greennode-facebook-post-pfbid02k8gsea": (
        "https://www.facebook.com/greennode23/posts/"
        "pfbid02k8gseaPDWDWRzXG3KWsRgukfNv7EXq1cvxhgmBj42vnGitw3cBf8s174xycgmFeDl"
    ),
    "greennode-linkedin": "https://www.linkedin.com/company/green-node/",
    "viettel-idc-facebook": "https://www.facebook.com/viettelidc/",
    "viettel-idc-linkedin": "https://www.linkedin.com/company/viettel-idc/",
    "fpt-cloud-facebook": "https://www.facebook.com/fptsmartcloud",
    "fpt-cloud-linkedin": "https://www.linkedin.com/company/fpt-cloud/",
    "fpt-cloud-x": "https://x.com/FPT_Cloud",
    "fpt-cloud-youtube": "https://www.youtube.com/channel/UCJM51jaizo0jSbv35HD2nYA",
    "bizfly-cloud-facebook": "https://facebook.com/BizflyCloud.VCCorp",
    "bizfly-cloud-linkedin": "https://www.linkedin.com/company/bizfly-cloud-vccorp/",
    "bizfly-cloud-x": "https://x.com/bizflycloud",
    "bizfly-cloud-telegram": "https://t.me/s/bizflycloudvn",
    "bizfly-cloud-youtube": "https://www.youtube.com/@giaiphapientoanammaybizfly9256",
    "aws-linkedin": "https://www.linkedin.com/company/amazon-web-services/",
    "aws-x": "https://x.com/awscloud",
    "aws-youtube": "https://www.youtube.com/user/AmazonWebServices",
    "google-cloud-facebook": "https://www.facebook.com/googlecloud/",
    "google-cloud-linkedin": "https://www.linkedin.com/showcase/google-cloud/",
    "google-cloud-x": "https://x.com/googlecloud",
    "google-cloud-youtube": "https://www.youtube.com/@googlecloudtech",
    "gke-linkedin": "https://www.linkedin.com/products/google-cloud-google-kubernetes-engine/",
    "azure-facebook": "https://www.facebook.com/microsoftazure/",
    "azure-linkedin": "https://www.linkedin.com/showcase/microsoft-azure/",
    "azure-x": "https://x.com/azure",
    "azure-youtube": "https://www.youtube.com/user/windowsazure",
}

_GREENNODE_SOCIAL_TARGETS = [
    "greennode-facebook",
    "greennode-facebook-post-pfbid02k8gsea",
    "greennode-linkedin",
]

_VN_COMPETITOR_SOCIAL_TARGETS = [
    "viettel-idc-facebook",
    "viettel-idc-linkedin",
    "fpt-cloud-facebook",
    "fpt-cloud-linkedin",
    "fpt-cloud-x",
    "fpt-cloud-youtube",
    "bizfly-cloud-facebook",
    "bizfly-cloud-linkedin",
    "bizfly-cloud-x",
    "bizfly-cloud-telegram",
    "bizfly-cloud-youtube",
]

_HYPERSCALER_SOCIAL_TARGETS = [
    "aws-linkedin",
    "aws-x",
    "aws-youtube",
    "google-cloud-facebook",
    "google-cloud-linkedin",
    "google-cloud-x",
    "google-cloud-youtube",
    "gke-linkedin",
    "azure-facebook",
    "azure-linkedin",
    "azure-x",
    "azure-youtube",
]

_SOCIAL_TARGETS = set(
    _GREENNODE_SOCIAL_TARGETS
    + _VN_COMPETITOR_SOCIAL_TARGETS
    + _HYPERSCALER_SOCIAL_TARGETS
)

_DEFAULT_TIMEOUT = 10
_MAX_CONTENT = 8_000  # ký tự tối đa lưu trong snapshot


@dataclass
class SourceSnapshot:
    provider: str
    source_type: str
    source_url: str
    fetched_at: str
    content_hash: str
    confidence: str = "medium"
    raw_data: dict[str, Any] = field(default_factory=dict)
    errors: list[str] = field(default_factory=list)


def _fetch_page_text(url: str, timeout: int = _DEFAULT_TIMEOUT) -> tuple[str, list[str]]:
    """Tải trang, trả (text thuần, errors). Không raise."""
    errors: list[str] = []
    try:
        import urllib.request
        headers = {
            "User-Agent": (
                "Mozilla/5.0 (compatible; GreenNodeBot/1.0; +https://greennode.ai)"
            )
        }
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            raw = resp.read(512_000)  # tối đa ~500 KB
        # Strip HTML tags đơn giản
        import re
        text = re.sub(r"<[^>]+>", " ", raw.decode("utf-8", errors="ignore"))
        text = re.sub(r"\s+", " ", text).strip()
        return text[:_MAX_CONTENT], errors
    except Exception as exc:
        errors.append(str(exc))
        return "", errors


def _content_hash(text: str) -> str:
    return hashlib.sha256(text.encode()).hexdigest()[:16]


def _looks_like_social_blocker(url: str, text: str) -> bool:
    lowered = text.lower()
    if "linkedin.com" in url:
        public_linkedin_markers = ("updates", "followers", "about us", "website", "company size")
        if any(marker in lowered for marker in public_linkedin_markers):
            return False
        return "join now" in lowered and "sign in" in lowered

    blockers = (
        "see posts, photos and more on facebook",
        "content isn't available",
        "join facebook",
        "log into facebook",
        "you must log in to continue",
        "this content isn't available right now",
        "before you continue to youtube",
        "sign in to confirm",
        "this browser is no longer supported",
    )
    return any(marker in lowered for marker in blockers)


def social_scrape_targets(scope: str = "all") -> list[str]:
    """Return social source keys by monitoring scope."""
    from vks_intelligence.config import get_settings

    # Park: Facebook/LinkedIn... chặn fetch tĩnh bằng login wall — bật lại qua ENABLE_SOCIAL_SCRAPE
    if not get_settings().enable_social_scrape:
        return []
    if scope == "greennode":
        return list(_GREENNODE_SOCIAL_TARGETS)
    if scope == "interactive_daily":
        return [
            "greennode-facebook",
            "greennode-linkedin",
            "viettel-idc-linkedin",
            "fpt-cloud-linkedin",
            "bizfly-cloud-linkedin",
            "gke-linkedin",
        ]
    if scope == "vn-competitors":
        return list(_VN_COMPETITOR_SOCIAL_TARGETS)
    if scope == "hyperscalers":
        return list(_HYPERSCALER_SOCIAL_TARGETS)
    if scope == "daily":
        return list(
            _GREENNODE_SOCIAL_TARGETS
            + _VN_COMPETITOR_SOCIAL_TARGETS
            + ["aws-linkedin", "google-cloud-linkedin", "gke-linkedin", "azure-linkedin"]
        )
    return list(_GREENNODE_SOCIAL_TARGETS + _VN_COMPETITOR_SOCIAL_TARGETS + _HYPERSCALER_SOCIAL_TARGETS)


def fetch_source(name: str) -> SourceSnapshot:
    """Chạy một scraper theo tên và trả snapshot."""
    from vks_intelligence.config import get_settings

    name_lower = name.lower().replace(" ", "-")
    url = _SCRAPE_ALLOWLIST.get(name_lower)
    source_type = "social" if name_lower in _SOCIAL_TARGETS else "web"

    fetched_at = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    if url is None:
        return SourceSnapshot(
            provider=name,
            source_type=source_type,
            source_url="",
            fetched_at=fetched_at,
            content_hash="",
            confidence="low",
            errors=[f"'{name}' không có trong scrape allowlist"],
        )

    s = get_settings()
    timeout = (
        s.evidence_social_timeout_seconds
        if source_type == "social"
        else s.evidence_web_timeout_seconds
    )
    text, errors = _fetch_page_text(url, timeout=timeout)
    if source_type == "social" and text and _looks_like_social_blocker(url, text):
        errors.append("Social page trả login wall hoặc nội dung không đọc được công khai")
        text = ""
    confidence = "low" if errors else ("medium" if text else "low")

    return SourceSnapshot(
        provider=name,
        source_type=source_type,
        source_url=url,
        fetched_at=fetched_at,
        content_hash=_content_hash(text) if text else "",
        confidence=confidence,
        raw_data={"url": url, "text_preview": text[:500]},
        errors=errors,
    )


def diff_snapshot(
    previous: SourceSnapshot,
    current: SourceSnapshot,
) -> dict[str, Any]:
    """So sánh hai snapshot — trả dict {changed, hash_before, hash_after, note}."""
    changed = previous.content_hash != current.content_hash
    return {
        "provider": current.provider,
        "changed": changed,
        "hash_before": previous.content_hash,
        "hash_after": current.content_hash,
        "fetched_before": previous.fetched_at,
        "fetched_after": current.fetched_at,
        "note": "Nội dung thay đổi — cần review thủ công." if changed else "Không thay đổi.",
    }
