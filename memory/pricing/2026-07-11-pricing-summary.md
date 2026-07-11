# Pricing Summary — 2026-07-11

Source: competitor-monitor run | Model: qwen/qwen3-5-27b

## Key Findings

- [RSS] [AWS Containers Blog](https://aws.amazon.com/blogs/containers/announcing-amazon-eks-rollback-for-safe-and-reliable-management-of-cluster-upgrades) 2026-07-01 — AWS ra mắt EKS Version Rollback (rollback upgrade K8s trong 7 ngày). Tác động: Nâng tiêu chuẩn 'operational safety'. Khách hàng Enterprise/Gov sẽ kỳ vọng khả năng phục hồi nhanh khi upgrade lỗi. GreenNode nên: Đánh giá lại quy trình upgrade VKS; nếu chưa có rollback tự động, cần ghi rõ SLA recovery time hoặc phát triển tính năng tương đương để giảm churn risk và bảo vệ mức giá premium.
- [RSS] [Vietnam.vn](https://news.google.com/rss/articles/CBMirgFBVV95cUxPeWVaUWxVQnljSmdMZFBjV1BZb1g2dEFVdnN0dHNFemxfZ0dyQjZzak11dVc0QzBWdzJZMktXWHIzNjhpVjY2NGpldHF0ak5WN0xxOXVSWXBMbzlZX3JobjZmOVlDUVZqRHVWdGJNdE9jOXZUTC1tUlFGWjlUNkEyTk1nYm1rWlZrR0xSUWlqNmkzQS1RYUtqcVR6bVRUSFB6dTA0SnpnQ0o1RWxfVGc?oc=5) 2026-07-09 — Mục tiêu 300 tỷ USD ngành công nghệ số nhấn mạnh hạ tầng số là lời giải. Tác động: Tăng willingness-to-pay cho hạ tầng nội địa tuân thủ pháp lý (Sovereign Cloud). GreenNode nên: Định vị VKS không chỉ là K8s mà là 'Sovereign AI Infrastructure' để justify premium so với local competitors.
- [Scrape] Viettel VOKS | https://viettelcloud.vn/san-pham/kubernetes | fetched_at=2026-07-11 — Snapshot trang sản phẩm không hiển thị bảng giá công khai (chỉ thấy CSS/JS loading). Tác động: Đối thủ local đang giữ chiến lược 'price on request' (sales-led). GreenNode nên: Chuẩn bị battlecard so sánh TCO dựa trên cấu hình thực tế thay vì list price, tập trung vào hidden cost (egress, support).

## Recommended Actions

- Talk Track Sales: Nhấn mạnh 'Sovereign Compliance Premium' — Giá VKS bao gồm chi phí tuân thủ Luật BVDLCN 2025 mà hyperscaler không đảm bảo được (data residency).
- Pricing Recommendation: Đề xuất mô hình 'Compliance Bundle' (K8s + Security + Audit Log) thay vì bán riêng lẻ compute để tăng perceived value.
- Data Refresh: Yêu cầu Product Team cung cấp snapshot bảng giá mới nhất (July 2026) để chạy TCO calculator cho scenario SME/Mid/Enterprise.
- Competitor Intel: Gửi yêu cầu RFP giả lập (dummy RFP) đến Viettel/FPT/Bizfly để lấy quote thực tế cho benchmark TCO.

## Risks

- Dữ liệu giá VKS trong memory (2026-05-20) có thể đã cũ (>60 days), cần xác nhận freshness trước khi dùng cho deal lớn.
- Thiếu dữ liệu egress pricing của đối thủ local, khó tính toán TCO ẩn (hidden cost) cho workload data-heavy.
- Không có FX rate cụ thể trong evidence, việc normalize VND/USD cho TCO sẽ mang tính ước lượng.

## Gaps / Thiếu dữ liệu

- Cần cập nhật: Bảng giá niêm yết GreenNode VKS (Compute, Storage, Egress, Control Plane) — Dữ liệu workspace hiện tại không chứa số liệu giá.
- Cần cập nhật: Pricing page của Viettel VOKS, FPT FKE, Bizfly BKE — Scrape hiện tại chỉ lấy được HTML/CSS, không có content giá.
- Cần xác minh: Discount structure cho Reserved Instances/Committed Use của các đối thủ local (thường không public).
- Cần thu thập: Chi phí GPU inference/training thực tế từ đối thủ để phân tích Scenario S4/S5.
