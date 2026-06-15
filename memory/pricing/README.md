# memory/pricing — Pricing Snapshots

Lưu pricing snapshot theo thời gian của competitor — cho phép tracking movement + phân
tích trend. `tools/memory_tool.py` và `PricingAgent` đọc từ đây.

## Thêm nhanh pricing competitor VN

1. Tra pricing từ trang chính thức của provider.
2. Dùng khung snapshot ở `prompts/pricing_agent.md` (6 nhóm component).
3. Điền số thực, ghi rõ timestamp + URL nguồn + FX rate.
4. Lưu `memory/pricing/YYYY-MM-DD_<provider>_pricing.md`.
5. Commit lên GitHub → agent đọc vào tuần digest tiếp theo.

| Provider Tier 1 | Trang pricing |
|---|---|
| Viettel vOKS | portal.viettelcloud.vn |
| FPT Cloud FKE | fptcloud.com/kubernetes |
| Bizfly BKE | bizflycloud.vn/kubernetes-engine |

Pricing không public → ghi `[Quote-based — cần liên hệ Sales]`, để trống phần số.

## Cấu trúc snapshot

```
## Pricing Snapshot — <Provider>
**Timestamp / Region / Currency / FX rate (nguồn, ngày) / Nguồn pricing (URL)**
### Control Plane
### Compute — On-demand / Reserved / Spot
### GPU (nếu có)
### Storage / Networking / Egress
### Support
### Free tier / Credit
```

## Quy tắc

- **Timestamp bắt buộc** — không timestamp = data vô giá trị. Ghi ngày+giờ, FX rate, URL.
- List price niêm yết → snapshot; enterprise discount ước tính 20–40% → ghi rõ estimate;
  promo lưu field riêng, không thay list price.

## Refresh (theo `.env`/`config.Settings`)

| Tier | Freshness | Trigger ngoài lịch |
|---|---|---|
| Tier 1 (Viettel, FPT, CMC, Bizfly) | `TIER1_FRESHNESS_DAYS` | thay đổi >5% |
| Tier 2 (AWS, GKE, AKS...) | `TIER2_FRESHNESS_DAYS` | regional pricing VN/SEA |
| Tier 3 (Sunteco, VinCloud, VNPT) | `TIER3_FRESHNESS_DAYS` | thay đổi >10% |
| GPU pricing (mọi tier) | `GPU_PRICING_FRESHNESS_DAYS` | GPU biến động nhanh |

## Retention

Giữ 12 snapshot gần nhất mỗi competitor. Cũ hơn: chỉ giữ nếu có giá trị tracking lịch sử.

## Liên kết

- Khung phân tích: `prompts/pricing_agent.md` · Agent: `PricingAgent`
- Output publish: `tools/output_tool.py` → `outputs/`
