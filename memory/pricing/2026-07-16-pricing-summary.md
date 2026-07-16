# Pricing Summary — 2026-07-16

Source: competitor-monitor run | Model: qwen/qwen3-5-27b

## Key Findings

- [RSS] [FPT Cloud](https://fptcloud.com/uu-dai-len-cloud-tang-03-thang-su-dung-dich-vu-chiet-khau-len-den-20-trieu-dong) 2026-07-14 — FPT Cloud tung ưu đãi 'Tặng 03 tháng sử dụng dịch vụ & chiết khấu lên đến 20 triệu đồng'. Tác động: Tạo áp lực giá trực tiếp cho segment SME/Mid-market đang cân nhắc chuyển đổi cloud. GreenNode nên: Chuẩn bị talk track so sánh TCO dài hạn (tránh chỉ nhìn vào promo ngắn hạn) và xem xét gói chào hàng tương đương cho khách hàng tiềm năng Q3.
- [RSS] [AWS Blog](https://aws.amazon.com/blogs/machine-learning/openai-gpt-5-6-sol-terra-and-luna-are-now-generally-available-on-amazon-bedrock) 2026-07-13 — AWS đưa GPT-5.6 Sol/Terra/Luna lên Bedrock. Tác động: Có thể làm tăng chi phí inference nếu khách hàng dùng model mới; tạo cơ hội cho VKS định vị self-hosted LLM là giải pháp ổn định giá hơn API. GreenNode nên: Cập nhật tài liệu TCO so sánh 'Managed API vs Self-hosted on VKS' với giả định giá model mới.
- [RSS] [GreenNode Blog](https://greennode.ai/blog/greennode-launches-han-1b-availability-zone-to-expand-ai-cloud-infrastructure) 2026-07-14 — GreenNode ra mắt Availability Zone HAN-1B. Tác động: Tăng khả năng disaster recovery và giảm latency miền Bắc, nhưng có thể đi kèm chi phí egress giữa AZ cao hơn. GreenNode nên: Công bố rõ ràng về chi phí data transfer giữa HCM/HAN để tránh bất ngờ cho khách hàng Enterprise.
- [Scrape] Viettel IDC | https://viettelcloud.vn/san-pham/kubernetes | fetched_at=2026-07-16 — Không lấy được dữ liệu giá (loading screen/CSS). Tác động: Không thể so sánh VOKS pricing tự động. GreenNode nên: Yêu cầu Sales Ops thu thập bảng giá VOKS mới nhất qua kênh đối tác hoặc RFP mẫu.

## Recommended Actions

- Sales Enablement: Cung cấp battlecard so sánh 'Promo ngắn hạn vs TCO dài hạn' để xử lý objection về ưu đãi 3 tháng của FPT.
- Product Marketing: Làm rõ chính sách Data Transfer giữa HCM và HAN-1B trong tài liệu kỹ thuật để tránh rủi ro cost surprise.
- Pricing Ops: Refresh snapshot bảng giá đối thủ (Viettel, Bizfly) bằng cách yêu cầu Sales gửi file PDF/RFP mẫu mới nhất.
- TCO Modeling: Xây dựng kịch bản S4 (AI Inference) so sánh chi phí dùng Bedrock (API) vs Self-hosted trên VKS với giả định giá model mới.

## Risks

- Dữ liệu pricing đối thủ (Viettel, Bizfly) không thể xác minh tự động do chặn nội dung web.
- Hồ sơ sản phẩm GreenNode VKS trong memory đã cũ (>60 ngày), cần refresh để đảm bảo tính chính xác khi báo giá.
- Promo của FPT là ngắn hạn, không nên dùng làm baseline cho chiến lược giá dài hạn.

## Gaps / Thiếu dữ liệu

- Cần cập nhật: Bảng giá chi tiết Viettel VOKS (Compute, Egress, LB) — hiện tại không fetch được.
- Cần cập nhật: Bảng giá chi tiết Bizfly BKE — hiện tại chỉ có tin bài marketing, không có số liệu.
- Cần xác minh: Chi phí egress giữa các AZ mới (HCM-HAN) của GreenNode sau khi launch HAN-1B.
- Cần cập nhật: Giá model AI mới trên AWS Bedrock (GPT-5.6) để tính toán TCO scenario S4/S5.
