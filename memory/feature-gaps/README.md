# memory/feature-gaps — Feature Gap Matrices

Lưu feature gap matrix đã validate — so sánh VKS với competitor theo capability, đánh
giá priority cho roadmap. Input cho Product planning và cho `CompetitorAgent`.

## Cấu trúc file

```
## Feature Gap Matrix — <Scope>
**Date / Scope (All | Tier 1 | AI-specific | GPU-specific) / Reviewed by**
### Methodology — số capability, sources, confidence/row
### Matrix
| Capability | Market expectation | VKS | Viettel | FPT | Bizfly | AWS EKS | Gap | Priority |
### Top Gaps — P0/P1/P2
### Roadmap Implication — cụ thể cho từng P0
### Sources
```

## Ký hiệu

✅ Có (production-ready) · ⚠️ Partial (preview/giới hạn) · ❌ Thiếu · 🔨 Roadmap (chưa GA)
· ❓ Chưa xác minh.

## Priority

| P | Tiêu chí |
|---|---|
| P0 | Must-have, mất deal vì thiếu — đóng trong quý |
| P1 | Differentiator, mất deal ở segment cụ thể — đóng trong 2 quý |
| P2 | Nice-to-have, marketing point — đóng trong 4 quý |
| P3 | Watch only |

## Naming

```
YYYY-MM-DD_feature-gap_<scope>.md
```

Ví dụ: `feature-gap_full-matrix`, `feature-gap_ai-gpu`, `feature-gap_enterprise-security`.

## Quy tắc

- ✅ Mỗi capability claim có nguồn + confidence (High/Medium/Low); human review trước khi finalize.
- ❌ Không claim feature competitor mà chưa verify; không liệt kê 100+ feature chung chung.

## Refresh & retention

Trước mỗi planning cycle (mỗi quý), hoặc khi competitor ra feature lớn. Giữ 4 cycle gần
nhất (1 năm rolling).

## Liên kết

- Cross-check: `memory/competitors/` · Agent: `CompetitorAgent` (feature comparison)
- Output ban đầu: `outputs/`
