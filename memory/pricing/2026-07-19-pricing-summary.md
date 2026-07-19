# Pricing Summary — 2026-07-19

Source: competitor-monitor run | Model: qwen/qwen3-5-27b

## Key Findings

- [RSS] [FPT Cloud](https://fptcloud.com/fpt-kubernetes-engine-v2-13-2-nang-cap-van-hanh-cloud-native-toi-uu-gpu-cho-ai-workload) 2026-07-17 — FPT nâng cấp FKE v2.13.2 với tối ưu GPU cho AI Workload. Tác động: Tăng sức mạnh tính toán trên hạ tầng nội địa, thách thức luận điểm 'AI-ready' của GreenNode nếu VKS chưa có tương đương. GreenNode nên: Kiểm tra lại spec GPU cluster VKS; chuẩn bị TCO so sánh hiệu năng/giá cho workload AI inference.
- [RSS] [AWS Blog](https://aws.amazon.com/blogs/machine-learning/introducing-grok-on-amazon-bedrock) 2026-07-16 — AWS thêm Grok 4.3 lên Bedrock. Tác động: Hyperscaler mở rộng catalog model, tăng áp lực cho khách hàng cân nhắc giữa Sovereign Cloud (GreenNode) vs Global Model Access. GreenNode nên: Nhấn mạnh lợi ích data residency và latency thấp hơn khi chạy mô hình tự host trên VKS so với gọi API qua biên giới.
- [Scrape] [Viettel IDC](https://viettelcloud.vn/san-pham/kubernetes) 2026-07-19 — Trang VOKS không trả về dữ liệu giá (chỉ HTML/CSS). Tác động: Không thể cập nhật TCO so sánh Viettel. GreenNode nên: Yêu cầu kỹ thuật refresh scraper hoặc lấy báo giá sales-led từ đối tác để ước tính.

## Recommended Actions

- Sales Talk Track: Khi khách hỏi giá, chuyển hướng sang TCO toàn phần bao gồm chi phí tuân thủ pháp lý (BVDLCN 2025) và độ trễ mạng, thay vì chỉ so sánh giá compute giờ.
- Product Action: Làm mới scraper pricing cho 3 đối thủ chính (FPT, Bizfly, Viettel) bằng cách bypass login wall hoặc dùng API public nếu có.
- Pricing Strategy: Chuẩn bị gói 'Reserved AI Instance' với discount sâu cho cam kết dài hạn nhằm khóa khách hàng Enterprise trước khi đối thủ tung promo GPU.

## Risks

- Dữ liệu giá đối thủ không khả dụng do scraping thất bại (có thể do login wall hoặc dynamic content), dẫn đến TCO analysis thiếu chính xác.
- Hồ sơ sản phẩm GreenNode VKS trong memory (tháng 5/2026) có thể đã lỗi thời về cấu hình giá hiện tại.

## Gaps / Thiếu dữ liệu

- Cần cập nhật: Bảng giá chi tiết GreenNode VKS (Compute, Storage, Egress) — Dữ liệu workspace cũ (2026-05-20), chưa có số mới.
- Cần cập nhật: Bảng giá FPT FKE, Bizfly BKE, Viettel VOKS — Scrape ngày 2026-07-19 không trích xuất được số liệu giá.
- Thiếu thông tin: Chi phí egress và LB/NAT của các đối thủ local cloud — Đây thường là hidden cost lớn ảnh hưởng TCO thực tế.
