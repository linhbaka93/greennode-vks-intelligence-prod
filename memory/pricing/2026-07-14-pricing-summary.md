# Pricing Summary — 2026-07-14

Source: competitor-monitor run | Model: qwen/qwen3-5-27b

## Key Findings

- [RSS] [FPT Cloud](https://fptcloud.com/doanh-nghiep-van-hanh-ai-tren-ha-tang-make-in-viet-nam-lam-chu-cong-nghe-canh-tranh-toan-cau) 2026-07-13 — FPT công bố chiến dịch vận hành AI trên hạ tầng nội địa. Tác động: Cạnh tranh trực tiếp vào luận điểm Sovereign AI của GreenNode; khách hàng Gov/Enterprise sẽ so sánh cam kết nội địa. GreenNode nên: Chuẩn bị battlecard so sánh chứng nhận Công nghệ cao TP.HCM (GreenNode) vs FPT và nhấn mạnh tuân thủ Luật BVDLCN 2025.
- [RSS] [AWS Artificial Intelligence Blog](https://aws.amazon.com/blogs/machine-learning/openai-gpt-5-6-sol-terra-and-luna-are-now-generally-available-on-amazon-bedrock) 2026-07-13 — AWS mở rộng mô hình GPT-5.6 trên Bedrock. Tác động: Nâng tiêu chuẩn khả năng AI-native cho Managed K8s. Khách hàng kỳ vọng tích hợp agent/model dễ dàng hơn. GreenNode nên: Đánh giá lộ trình tích hợp AI tooling lên VKS để tránh feature gap.
- [Scrape] [Viettel VOKS](https://viettelcloud.vn/san-pham/kubernetes) 2026-07-14 — Trang sản phẩm Viettel VOKS được scrape nhưng snippet chỉ chứa CSS/HTML, không có bảng giá. Tác động: Không thể so sánh giá compute/storage/networking với VKS. GreenNode nên: Yêu cầu team Data Engineering cải thiện scraper để parse bảng giá hoặc thực hiện kiểm tra thủ công.

## Recommended Actions

- Talk Track Sales: Nhấn mạnh 'Chứng nhận Doanh nghiệp Công nghệ cao TP.HCM' và 'Tuân thủ Luật BVDLCN 2025' thay vì so sánh giá CPU/RAM khi đối thủ dùng narrative 'Make in Viet Nam'.
- Pricing Refresh: Kích hoạt task scrape lại trang giá đối thủ với logic parse bảng giá chuyên sâu; đồng thời rà soát lại bảng giá VKS nội bộ.
- Feature Gap Analysis: So sánh tính năng AI integration (Bedrock-like capabilities) giữa VKS và AWS EKS để đánh giá rủi ro churn cho workload AI.

## Risks

- Dữ liệu pricing VKS trong memory đã >60 ngày (từ tháng 5/2026), có nguy cơ không phản ánh promo/discount hiện tại.
- Không có số liệu giá cụ thể từ đối thủ để tính toán TCO delta, dẫn đến khuyến nghị bán hàng thiếu căn cứ số.
- Xu hướng Sovereign AI từ FPT có thể buộc GreenNode phải điều chỉnh chiến lược giá trị (value-based) thay vì cạnh tranh giá.

## Gaps / Thiếu dữ liệu

- Cần cập nhật: greennode/2026-05-20_greennode-vks_product-overview.md — dữ liệu cũ, cần refresh pricing table.
- Thiếu dữ liệu: Bảng giá chi tiết (compute, storage, egress) của Viettel VOKS, FPT FKE, Bizfly BKE — scraper chưa parse được.
- Thiếu dữ liệu: Tỷ giá USD/VND áp dụng cho các quote gần đây để normalize giá.
