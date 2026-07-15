# Pricing Summary — 2026-07-15

Source: competitor-monitor run | Model: qwen/qwen3-5-27b

## Key Findings

- [RSS] [FPT Cloud](https://fptcloud.com/doanh-nghiep-van-hanh-ai-tren-ha-tang-make-in-viet-nam-lam-chu-cong-nghe-canh-tranh-toan-cau) 2026-07-13 — FPT đẩy mạnh thông điệp 'Make in Viet Nam' cho hạ tầng AI. Tác động: Cạnh tranh trực tiếp vào luận điểm Sovereign AI của GreenNode; khách hàng Gov/Enterprise sẽ so sánh cam kết nội địa. GreenNode nên: Chuẩn bị battlecard so sánh chứng nhận Công nghệ cao TP.HCM (GreenNode) vs các chứng nhận tương đương của FPT; nhấn mạnh tính tuân thủ Luật BVDLCN 2025.
- [RSS] [AWS Containers Blog](https://aws.amazon.com/blogs/containers/announcing-amazon-eks-rollback-for-safe-and-reliable-management-of-cluster-upgrades) 2026-07-01 — AWS ra mắt Amazon EKS Version Rollback (rollback upgrade K8s version trong 7 ngày). Tác động: Nâng tiêu chuẩn 'operational safety' cho Managed K8s. Khách hàng Enterprise/Gov sẽ kỳ vọng khả năng phục hồi nhanh khi upgrade lỗi. GreenNode nên: Đánh giá lại quy trình upgrade VKS; nếu chưa có rollback tự động, cần ghi rõ SLA recovery time hoặc phát triển tính năng tương đương để giảm churn risk.
- [Scrape] Viettel VOKS | https://viettelcloud.vn/san-pham/kubernetes | fetched_at=2026-07-15 — Không thể trích xuất bảng giá từ trang sản phẩm (snippet chỉ chứa CSS/HTML cấu trúc). Tác động: Không thể so sánh giá list price với Viettel IDC. GreenNode nên: Yêu cầu Sales Ops thu thập báo giá thực tế (RFP) từ Viettel để cập nhật database pricing.
- [Scrape] FPT FKE | https://fptcloud.com/kubernetes | fetched_at=2026-07-15 — Không thể trích xuất bảng giá từ trang sản phẩm (snippet chỉ chứa JS/CSS). Tác động: Không thể so sánh giá list price với FPT Cloud. GreenNode nên: Theo dõi thêm qua kênh partner hoặc yêu cầu Sales Ops cung cấp quote mẫu.
- [RSS] [GreenNode Blog](https://greennode.ai/blog/greennode-launches-han-1b-availability-zone-to-expand-ai-cloud-infrastructure) 2026-07-14 — GreenNode mở rộng Availability Zone HAN-1B. Tác động: Tăng capacity cho workload tại miền Bắc, giảm latency cho khách hàng HN/Hà Nội. GreenNode nên: Đẩy mạnh bán hàng cho segment Gov/Enterprise tại Hà Nội với ưu tiên về data residency.

## Recommended Actions

- Talk Track: Chuyển trọng tâm từ 'giá rẻ' sang 'chi phí tuân thủ & an toàn'. Nhấn mạnh việc tránh rủi ro pháp lý (Luật BVDLCN 2025) và downtime do upgrade cluster (so sánh với EKS Rollback).
- Pricing Recommendation: Đề xuất gói 'Sovereign Bundle' bao gồm VKS + Compliance Audit Support + Dedicated Support để gia tăng perceived value thay vì giảm giá compute.
- Data Refresh: Yêu cầu Engineering/Sales Ops chạy script scrape nâng cao (headless browser) hoặc thu thập 3 quote mẫu từ Viettel/FPT/Bizfly trong tuần tới để cập nhật baseline.
- Feature Parity: Kiểm tra ngay quy trình upgrade VKS; nếu chưa có auto-rollback, cần thông báo rõ ràng về SLA recovery time để tránh mất niềm tin khi so sánh với AWS.

## Risks

- Dữ liệu pricing workspace (May 2026) đã quá 2 tháng, có thể không phản ánh promo/discount hiện tại.
- Không có số liệu egress/networking cost cụ thể để tính TCO hidden cost.
- Thiếu dữ liệu GPU pricing (H100/A100) để phân tích scenario AI Inference/Training.

## Gaps / Thiếu dữ liệu

- Cần cập nhật: Bảng giá chi tiết VKS (Compute, Storage, Networking, Control Plane) — dữ liệu cũ, chưa dùng được cho TCO calculation.
- Cần cập nhật: Bảng giá đối thủ (VOKS, FKE, BKE) — scraper không lấy được nội dung giá, cần fetch thủ công hoặc RFP.
- Cần xác minh: Chính sách Reserved Instances/Committed Use Discount của GreenNode so với AWS Savings Plans.
- Cần xác minh: Chi phí egress giữa các AZ (HCM-HAN) của GreenNode.
