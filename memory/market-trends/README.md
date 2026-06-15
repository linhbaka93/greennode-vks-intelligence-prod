# memory/market-trends — Trend Summaries

Lưu trend summary dài hạn — pattern observe qua thời gian, không phải tin tức ngày.
`MarketTrendAgent` đọc/đề xuất cập nhật từ đây.

## Phạm vi

- **Technology:** AI inference/training on K8s, platform engineering/IDP, GPU
  (H100/H200/B200), Karpenter/Cilium/Gateway API, FinOps.
- **Market:** Kubernetes adoption VN/SEA/global, sovereign cloud, chính sách & đầu tư
  AI VN, động thái region của hyperscaler.
- **Customer:** switching pattern, pain point theo segment, buying behavior.

## Cấu trúc file

```
## Trend: <Tên>
**Date observed / Stage (Early|Growing|Mainstream|Declining) / Priority (P0..P3)**
### What        — mô tả trend
### Signals      — ≥3 signal độc lập + nguồn
### Who's leading
### Timeline estimate (khi nào mainstream)
### Implication cho GreenNode VKS (cụ thể)
### Action status (checklist)
### Last reviewed: YYYY-MM-DD
```

## Naming

```
YYYY-MM-DD_<trend-slug>.md      # mới / major update
<trend-slug>_current.md         # rolling update
```

Ví dụ: `ai-inference-on-k8s`, `sovereign-ai-sea`, `fractional-gpu-mig`.

## Quy tắc

- ✅ ≥3 signal độc lập từ nguồn khác nhau; stage assessment có lý do.
- ✅ Implication cụ thể cho VKS, không chung chung.
- ❌ Không lưu trend từ 1 announcement đơn lẻ; phân biệt AI hype (PR) vs production reality.

## Refresh

| Stage | Review |
|---|---|
| Early | hàng quý |
| Growing | hàng tháng |
| Mainstream | hàng quý |
| Declining | 6 tháng |

Freshness tổng thể: `MARKET_TRENDS_FRESHNESS_DAYS` (`.env`/`config.Settings`).

## Liên kết

- Agent: `prompts/market_trend_agent.md` (`MarketTrendAgent`)
- Output: `tools/output_tool.py` → `outputs/` (weekly, monthly)
