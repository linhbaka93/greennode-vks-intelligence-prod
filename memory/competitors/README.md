# memory/competitors — Competitor Profiles

Lưu competitor profile đã validate. Mỗi đối thủ có 1 file `_current.md` + snapshot lịch sử.

## Phạm vi

Danh sách theo dõi (chi tiết tier trong `prompts/competitor_agent.md`):

- **Tier 1 nội địa:** Viettel IDC VKS/vOKS, FPT Cloud FKE, CMC, Bizfly BKE
- **Tier 2 hyperscale:** AWS EKS, Google GKE, Azure AKS, Alibaba ACK, Oracle OKE
- **Tier 3 khác:** Sunteco SKS, VinCloud, VNPT Kubernetes

## Cấu trúc profile

Mỗi profile chứa: core product (URL, ngày ra mắt, K8s version, region, SLA) · feature
matrix · pricing summary (chi tiết ở `memory/pricing/`) · positioning & GTM · SWOT từ
góc GreenNode · customer evidence · sources có timestamp.

Khung phân tích đầy đủ: `prompts/competitor_agent.md`.

## Naming

```
YYYY-MM-DD_<competitor-slug>_profile.md
<competitor-slug>_current.md            # bản mới nhất
```

Slug: `viettel-idc`, `fpt-cloud-fke`, `bizfly-bke`, `aws-eks`...

## Quy tắc

- ✅ Timestamp bắt buộc cho mọi data point; ≥3 nguồn cite/profile.
- ✅ Profile mới qua human review (Product/Solution Architect) trước khi vào memory.
- ❌ Không lưu profile dựa 1 nguồn duy nhất; không dùng partner intel chưa verify.

## Refresh

Theo freshness threshold ở `.env`/`config.Settings`: Tier 1 `TIER1_FRESHNESS_DAYS`,
Tier 2 `TIER2_FRESHNESS_DAYS`, Tier 3 `TIER3_FRESHNESS_DAYS`.

Trigger ngoài lịch: đối thủ ra feature lớn · pricing đổi >10% · M&A/funding · customer
reference công khai.

Quản lý bởi `CompetitorAgent` (đề xuất) + human review.
