# memory/ — Knowledge Base (đã validate)

Kho tri thức đã validate, tinh lọc — `tools/memory_tool.py` nạp từ đây làm context cho
agent, và là nguồn versioned memory khi nối GitHub.

## memory/ vs outputs/

| Thư mục | Mục đích | Tính chất |
|---|---|---|
| `memory/` | Kho tri thức đã validate, dùng để truy xuất | Persistent, tinh lọc, ít thay đổi |
| `outputs/<loại>/` | Deliverable đã publish (weekly, monthly, battlecard...) | Versioned theo ngày, có người nhận |
| `outputs/runs/<run_id>/` | Artifact audit của từng run | Sinh tự động, gitignore |

Một insight chỉ vào `memory/` khi đã validate (qua quality gate + thường có human
review). Output mới nằm ở `outputs/`; sau khi dùng và xác minh, chắt lọc vào `memory/`.

## Cấu trúc

```
memory/
  greennode/          Hồ sơ sản phẩm GreenNode VKS
  competitors/        Competitor profile đã validate
  pricing/            Pricing snapshot theo thời gian
  regulatory/         Văn bản pháp lý đang hiệu lực
  market-trends/      Trend summary dài hạn
  battlecards/        Battlecard active (current) + archive/
  feature-gaps/       Feature gap matrix
  executive-briefs/   Brief đã gửi leadership (audit trail)
```

## Nên / không nên lưu

✅ Competitor profile đã review · pricing snapshot có timestamp + nguồn · strategic
insight đã confirm · battlecard đã field-test · feature comparison đã verify · pattern
pain lặp ≥3 lần · trend có ≥2 nguồn.

❌ Raw HTML/scrape · pricing chưa verify · tin đồn forum · dữ liệu trùng · draft chưa final.

## Naming

```
YYYY-MM-DD_<topic-slug>.md          # snapshot theo ngày
<slug>_current.md                   # bản mới nhất / luôn cập nhật
```

Slug: lowercase, dash. Ví dụ: `viettel-voks`, `bizfly-bke`, `aws-eks`.

## Lifecycle & freshness

Freshness threshold cấu hình tập trung ở `.env` / `config.Settings`
(`TIER1/2/3_FRESHNESS_DAYS`, `GPU_PRICING_FRESHNESS_DAYS`,
`MARKET_TRENDS_FRESHNESS_DAYS`). `memory_tool` flag dữ liệu vượt ngưỡng;
`MemoryCuratorAgent` đề xuất patch refresh.

| Loại | Freshness | Retention |
|---|---|---|
| Competitor/pricing Tier 1 | `TIER1_FRESHNESS_DAYS` | 12 tháng |
| Competitor/pricing Tier 2 | `TIER2_FRESHNESS_DAYS` | 12 tháng |
| Competitor/pricing Tier 3 | `TIER3_FRESHNESS_DAYS` | 4 quý |
| GPU pricing (mọi tier) | `GPU_PRICING_FRESHNESS_DAYS` | 12 snapshot |
| Market trend | `MARKET_TRENDS_FRESHNESS_DAYS` | 8 quý |
| Battlecard current | khi đối thủ đổi / mỗi quý | 1 version active |
| Executive brief | — | giữ tất cả (audit) |

## Liên kết

- Agent đọc/đề xuất: `prompts/` (competitor, pricing, market_trend, memory_curator...)
- Nạp memory: `tools/memory_tool.py` · commit versioned: `tools/github_tool.py`
- Publish output: `tools/output_tool.py` → `outputs/`
