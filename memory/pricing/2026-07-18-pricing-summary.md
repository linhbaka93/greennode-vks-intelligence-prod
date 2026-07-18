# Pricing Summary — 2026-07-18

Source: competitor-monitor run | Model: qwen/qwen3-5-27b

## Key Findings

- [RSS] [FPT Cloud](https://fptcloud.com/fpt-kubernetes-engine-v2-13-2-nang-cap-van-hanh-cloud-native-toi-uu-gpu-cho-ai-workload) 2026-07-17 — FPT cập nhật FKE v2.13.2 tối ưu GPU cho AI Workload. Tác động: Tăng sức cạnh tranh trực tiếp vào segment AI Inference/Training của GreenNode VKS. Khách hàng sẽ so sánh hiệu năng/giá GPU. GreenNode nên: Kiểm tra lại cấu hình GPU H100/A100 trên VKS; chuẩn bị talk track về 'GPU efficiency' nếu không có thông tin giá cụ thể.
- [RSS] [Vietnam.vn](https://news.google.com/rss/articles/CBMiswFBVV95cUxQajZBdm9qT1dtclNDemFMZU10d2lLd0liTlh4Q3dHZmRTT0dWMzZzc29ZaEhwT04xQ0xrSnhCLWZxN2JGWG9zZXlKMVNVbEtaVjhacm9jeGZYNlpFLUZNbkNVV1lRYmZ6MllVMDBiSy02SkdNWnZkaDBnaHRWZ3Z2d1ZJQmFkWWI1dmFCczgtTms2SHBQU3JQVFh6ZTRLMVZkTTc1VkI2MzkxeWpoS185YXlHWQ?oc=5) 2026-07-18 — Chính phủ hỗ trợ tài năng AI và công nghệ Make in Vietnam. Tác động: Củng cố luận điểm Sovereign AI, cho phép GreenNode duy trì định vị premium dựa trên compliance (Luật BVDLCN 2025). GreenNode nên: Nhấn mạnh chứng nhận Công nghệ cao TP.HCM trong proposal để biện minh cho mức giá cao hơn hyperscaler.
- [Scrape] Viettel IDC | https://viettelcloud.vn/san-pham/kubernetes | fetched_at=2026-07-18 — Trang VOKS tồn tại nhưng scrape không lấy được bảng giá (chỉ thu thập được CSS). Tác động: Không thể so sánh giá chi tiết với Viettel IDC. GreenNode nên: Yêu cầu Sales Ops cung cấp quote mẫu từ Viettel IDC hoặc tự động hóa scraper chuyên sâu vào trang pricing.

## Recommended Actions

- Ưu tiên cao: Kích hoạt scraper chuyên sâu vào trang pricing detail của FPT/Viettel/Bizfly (không chỉ landing page) để trích xuất bảng giá.
- Sales Enablement: Chuẩn bị battlecard tập trung vào 'Compliance & Data Residency' thay vì giá, dựa trên tín hiệu chính sách Make in Vietnam (Vietnam.vn 2026-07-18).
- Product Review: Đánh giá lại cấu hình GPU trên VKS sau khi FPT công bố tối ưu GPU (v2.13.2); nếu VKS chưa tối ưu tương đương, cần roadmap rõ ràng để tránh churn risk ở segment AI.
- Pricing Refresh: Cập nhật file pricing internal của GreenNode VKS trước RFP Q3/Q4; flag các component có thể biến động (GPU spot/on-demand).

## Risks

- Dữ liệu pricing GreenNode VKS trong memory đã >60 ngày (May 2026), vi phạm quy tắc refresh >60 ngày cho pricing data.
- Không có số liệu giá cụ thể từ đối thủ để tính toán TCO delta, dẫn đến rủi ro đưa ra khuyến nghị sai lệch về chiến lược giá.
- Xu hướng Sovereign AI mạnh (tin tức chính phủ) có thể làm giảm độ nhạy cảm về giá (price elasticity), nhưng cần bằng chứng deal win/loss để xác nhận.

## Gaps / Thiếu dữ liệu

- Cần cập nhật: greennode/2026-05-20_greennode-vks_product-overview.md — dữ liệu cũ, chưa dùng được cho pricing analysis Q3.
- Thiếu bảng giá niêm yết (list price) của FPT FKE, Viettel VOKS, Bizfly BKE cho các instance type GPU (H100/A100) và CPU.
- Thiếu thông tin về phí egress và control plane fee của đối thủ để tính hidden cost.
- Không có dữ liệu promo/discount rate hiện hành của đối thủ (Reserved Instances, Committed Use).
