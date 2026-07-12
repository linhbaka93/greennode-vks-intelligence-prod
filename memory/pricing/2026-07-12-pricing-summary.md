# Pricing Summary — 2026-07-12

Source: competitor-monitor run | Model: qwen/qwen3-5-27b

## Key Findings

- [RSS] [Cloud Native Computing Foundation](https://www.cncf.io/blog/2026/07/10/where-should-ai-workloads-run-a-sovereign-and-sensible-approach) 2026-07-10 — CNCF nhấn mạnh xu hướng 'Sovereign AI', phù hợp với định vị GreenNode VKS là hạ tầng tuân thủ pháp lý VN. Tác động: Củng cố luận điểm bán hàng cho segment Enterprise/Gov, cho phép duy trì mức giá premium so với hyperscaler nếu chứng minh được lợi ích compliance. GreenNode nên: Tích hợp trích dẫn báo cáo này vào tài liệu GTM để chứng minh tính đúng đắn của chiến lược Sovereign Cloud.
- [RSS] [AWS Containers Blog](https://aws.amazon.com/blogs/containers/announcing-amazon-eks-rollback-for-safe-and-reliable-management-of-cluster-upgrades) 2026-07-01 — AWS ra mắt Amazon EKS Version Rollback, nâng tiêu chuẩn 'operational safety'. Tác động: Khách hàng Enterprise/Gov sẽ kỳ vọng khả năng phục hồi nhanh khi upgrade lỗi. Nếu VKS chưa có rollback tự động, đây là rủi ro churn và áp lực giảm giá trị cảm nhận. GreenNode nên: Đánh giá lại quy trình upgrade VKS; nếu chưa có, cần ghi rõ SLA recovery time hoặc phát triển tính năng tương đương.
- [Scrape] bizfly-bke | https://bizflycloud.vn/kubernetes | fetched_at=2026-07-12 — Không thể trích xuất bảng giá cụ thể từ trang đối thủ (chỉ thu thập được CSS/HTML). Tác động: Thiếu dữ liệu để so sánh trực tiếp TCO với BizFly BKE. GreenNode nên: Yêu cầu Sales Ops kiểm tra manual quote từ đối thủ để cập nhật battlecard.

## Recommended Actions

- Talk Track: Nhấn mạnh 'Sovereign AI Compliance' thay vì chỉ so sánh giá compute/giờ khi đấu thầu với Hyperscaler cho khách Gov/Bank.
- Pricing Recommendation: Giữ nguyên list price nhưng xem xét gói bundle bao gồm SLA recovery time cao hơn để bù đắp thiếu tính năng rollback tự động (nếu có).
- Data Refresh: Yêu cầu Product Team cung cấp snapshot pricing mới nhất (VND/tháng + USD/hour) trước RFP Q3.
- Competitor Intel: Sales Ops cần gửi request quote mẫu cho BizFly/Viettel để có số liệu TCO thực tế cho scenario S4 (AI Inference).

## Risks

- Dữ liệu pricing từ workspace (May 2026) có thể đã lỗi thời so với chính sách thực tế tháng 7/2026.
- Không có số liệu egress/networking cost cụ thể để tính toán TCO ẩn (hidden cost) cho scenario AI Inference.
- Thiếu thông tin về discount Reserved Instances từ đối thủ nội địa để so sánh deal lớn.

## Gaps / Thiếu dữ liệu

- Cần cập nhật: greennode/2026-05-20_greennode-vks_product-overview.md — dữ liệu cũ, chưa dùng được cho pricing claim chính xác.
- Không có bảng giá công khai mới từ GreenNode VKS trong 3 ngày qua.
- Không fetch được bảng giá chi tiết từ BizFly BKE, Viettel VOKS, FPT FKE qua scraper (cần xác minh manual).
