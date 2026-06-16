"""Eval harness — validates quality gate behavior against eval spec cases.

Fixtures referenced in evals/*.json do not exist yet; test content is inlined here
to match the eval case intent until fixture files are created.
"""

from vks_intelligence.contracts import QualityVerdict, TaskType
from vks_intelligence.quality import validate_output

_WEEKLY_NORMAL = """\
# GreenNode VKS Intelligence — Weekly Digest

📅 2026-06-16 06:00 UTC

## TL;DR
- [RSS] [AWS Blog](https://aws.amazon.com/blogs/containers/eks-auto-mode) 2026-06-15 — AWS ra mắt EKS Auto Mode tự động hóa node management.
- [RSS] [Viettel Cloud](https://viettelcloud.vn/tin-tuc/gpu-pricing) 2026-06-14 — Viettel giảm giá GPU node pool xuống $0.8/giờ tại VN.
- [Workspace] VKS control plane miễn phí — lợi thế chi phí so với AWS EKS $0.10/giờ.

## Key Findings
- [RSS] [CNCF Blog](https://cncf.io/blog/arm64-adoption-2026) 2026-06-15 — Arm64 chiếm >50% instance mới trên AWS; GreenNode cần roadmap Arm64 rõ ràng.

## Rủi ro cần theo dõi
- Viettel đẩy mạnh GPU pricing và hệ sinh thái AI — churn risk cho AI workload segment.

## Action Items
- Cập nhật talk track về control plane miễn phí và data sovereignty.
- Lên roadmap Arm64 support cho VKS trong Q3/2026.

## Sources
- [RSS] [AWS Blog](https://aws.amazon.com/blogs/containers/eks-auto-mode) (2026-06-15)
- [RSS] [Viettel Cloud](https://viettelcloud.vn/tin-tuc/gpu-pricing) (2026-06-14)
- [Workspace] memory/pricing/vks-pricing-2026.md
"""

_WEEKLY_NO_SOURCES = """\
# GreenNode VKS Intelligence — Weekly Digest

📅 2026-06-16 06:00 UTC

## TL;DR
- Không có tin mới đáng chú ý trong kỳ này.

## Key Findings
_Không có finding trong kỳ này._

## Action Items
- Theo dõi thêm tuần sau.
"""


def test_weekly_happy_path_passes_or_needs_review():
    """weekly-happy-path: content đầy đủ → pass hoặc needs_review."""
    result = validate_output(_WEEKLY_NORMAL, task_type=TaskType.WEEKLY_DIGEST)
    assert result.verdict in (QualityVerdict.PASS, QualityVerdict.NEEDS_REVIEW), (
        f"Expected pass/needs_review, got {result.verdict.value} "
        f"(score={result.score:.3f}, failures={result.failures})"
    )


def test_weekly_missing_sources_is_revise_or_blocked():
    """weekly-missing-sources: không có sources → revise hoặc blocked."""
    result = validate_output(_WEEKLY_NO_SOURCES, task_type=TaskType.WEEKLY_DIGEST)
    assert result.verdict in (QualityVerdict.REVISE, QualityVerdict.BLOCKED), (
        f"Expected revise/blocked, got {result.verdict.value} "
        f"(score={result.score:.3f}, failures={result.failures})"
    )
