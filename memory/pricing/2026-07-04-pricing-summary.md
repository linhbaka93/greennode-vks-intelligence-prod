# Pricing Summary — 2026-07-04

Source: competitor-monitor run | Model: qwen/qwen3-5-27b

## Key Findings

- [RSS] [AWS Containers Blog](https://aws.amazon.com/blogs/containers/announcing-amazon-eks-rollback-for-safe-and-reliable-management-of-cluster-upgrades) 2026-07-01 — AWS ra mắt EKS Version Rollback cho phép rollback upgrade K8s trong 7 ngày. Tác động: Nâng tiêu chuẩn 'operational safety'. Khách hàng Enterprise/Gov sẽ kỳ vọng khả năng phục hồi nhanh. GreenNode nên: Đánh giá lại quy trình upgrade VKS; nếu chưa có rollback tự động, cần ghi rõ SLA recovery time hoặc phát triển tính năng tương đương để giảm churn risk khi so sánh TCO.
- [RSS] [Vietnam News](https://news.google.com/rss/articles/CBMisgFBVV95cUxNRjVxOHpyYXc0QnFCdHhVbFFKM3hSRThJNjc3d3ZWbDRteHIzTDZ6SHFUMnoya21rQzh3WWJfcXRFTVBxRWUzbUhWU0dFX0ZFdzhLLThZakIwWEVRNDktMmlZc3JLSTQ0ZFRhSXAtUkt3NWtvZi1wc1JtRlphclRPU1JKWjBIcEFwZGpoNkQyd2RRQmVfRXhKSlF4cUd6eUcyRmRJMHMzMWxlSUkxQlpkUy1n?oc=5) 2026-07-04 — G-Group nhận giấy phép đầu tư $300 triệu cho AI Campus. Tác động: Đối thủ hạ tầng AI mới gia nhập thị trường Sovereign Cloud. Áp lực cạnh tranh về giá GPU/AI workload có thể tăng trong 6–12 tháng tới. GreenNode nên: Theo dõi tiến độ xây dựng và chính sách giá khi họ đi vào hoạt động; củng cố lợi thế hiện hữu (chứng nhận công nghệ cao, hợp tác MSB).
- [Scrape] Viettel IDC | https://viettelcloud.vn/san-pham/kubernetes | fetched_at=2026-07-04 — Snapshot trang vOKS không trích xuất được bảng giá (chỉ thấy CSS). Tác động: Không thể tính toán TCO delta giữa VKS và vOKS. Rủi ro Sales thiếu số liệu so sánh chi tiết. GreenNode nên: Yêu cầu team Research thực hiện manual check pricing page hoặc liên hệ Sales Partner để lấy bảng giá nội bộ cập nhật.

## Recommended Actions

- Talk Track cho Sales: Tập trung vào 'Sovereign Compliance' và 'Data Residency' thay vì so sánh giá trực tiếp khi chưa có số liệu. Nhấn mạnh chứng nhận Doanh nghiệp Công nghệ cao của GreenNode.
- Pricing Recommendation: Ưu tiên mô hình Reserved/Committed Use cho khách hàng Enterprise để lock-in revenue trước khi đối thủ mới (G-Group) tung giá cạnh tranh.
- Action Item: Yêu cầu Source Tool chạy lại scraper với JavaScript rendering enabled hoặc nhân sự kiểm tra thủ công trang giá của 3 đối thủ trong vòng 48h tới.

## Risks

- Không thể cung cấp TCO comparison chính xác do thiếu dữ liệu giá đối thủ (vOKS, BKE, FKE).
- Dữ liệu product overview của GreenNode VKS đã cũ (2026-05-20), có thể không phản ánh chính sách giá mới nhất Q3 2026.
- Đối thủ mới (G-Group AI Campus) có thể thay đổi cấu trúc giá GPU/AI trong tương lai gần.

## Gaps / Thiếu dữ liệu

- Cần cập nhật: Bảng giá niêm yết của Viettel vOKS, Bizfly BKE, FPT FKE — dữ liệu scrape thất bại, cần manual verify.
- Cần cập nhật: Chính sách giá GPU/AI inference của GreenNode VKS — chưa có trong workspace memory.
- Cần xác minh: Chi phí egress và storage của các đối thủ local cloud để tính toán hidden cost.
