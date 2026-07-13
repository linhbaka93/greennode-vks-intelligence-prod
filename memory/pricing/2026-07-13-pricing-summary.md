# Pricing Summary — 2026-07-13

Source: competitor-monitor run | Model: qwen/qwen3-5-27b

## Key Findings

- [RSS] [Cloud Native Computing Foundation](https://www.cncf.io/blog/2026/07/10/where-should-ai-workloads-run-a-sovereign-and-sensible-approach) 2026-07-10 — CNCF nhấn mạnh xu hướng 'Sovereign AI' cho doanh nghiệp, phù hợp với định vị GreenNode VKS là hạ tầng tuân thủ pháp lý VN. Tác động: Củng cố luận điểm bán hàng cho segment Enterprise/Gov, giảm áp lực cạnh tranh giá thuần túy. GreenNode nên: Tích hợp trích dẫn báo cáo này vào tài liệu GTM để chứng minh tính đúng đắn của chiến lược Sovereign Cloud.
- [RSS] [AWS Containers Blog](https://aws.amazon.com/blogs/containers/announcing-amazon-eks-rollback-for-safe-and-reliable-management-of-cluster-upgrades) 2026-07-01 — AWS ra mắt Amazon EKS Version Rollback, cho phép rollback upgrade K8s version trong vòng 7 ngày mà không cần rebuild cluster. Tác động: Nâng tiêu chuẩn 'operational safety' cho Managed K8s. Khách hàng Enterprise/Gov sẽ kỳ vọng khả năng phục hồi nhanh khi upgrade lỗi. GreenNode nên: Đánh giá lại quy trình upgrade VKS; nếu chưa có rollback tự động, cần ghi rõ SLA recovery time hoặc phát triển tính năng tương đương để giảm churn risk.
- [Scrape] Viettel IDC | https://viettelcloud.vn/san-pham/kubernetes | fetched_at=2026-07-13 — Trang sản phẩm vOKS được truy cập nhưng nội dung snippet chỉ chứa CSS/loading, không trích xuất được bảng giá. Tác động: Không thể so sánh TCO chi tiết với đối thủ nội địa lớn nhất. GreenNode nên: Yêu cầu team Data Engineering tối ưu scraper để parse bảng giá thực tế từ trang web đối thủ.

## Recommended Actions

- Talk Track Sales: Tập trung vào 'Sovereign Compliance Value' thay vì giá thấp. Sử dụng báo cáo CNCF (July 2026) để chứng minh nhu cầu thị trường về hạ tầng tuân thủ nội địa.
- Product Ops: Kiểm tra tính năng 'Cluster Upgrade Rollback' trên VKS. Nếu chưa có, cần lên kế hoạch roadmap hoặc chuẩn bị câu trả lời về SLA Recovery Time khi khách hỏi.
- Data Team: Tối ưu hóa scraper cho trang đối thủ (Viettel/FPT/Bizfly) để trích xuất bảng giá thực tế, tránh chỉ lấy HTML/CSS.
- Pricing Strategy: Chờ dữ liệu giá mới trước khi đề xuất điều chỉnh giá list. Hiện tại giữ nguyên chiến lược giá trị gia tăng (value-based) dựa trên compliance.

## Risks

- Dữ liệu pricing từ workspace (May 2026) đã quá 30 ngày, có thể không phản ánh chính sách giá hiện tại (July 2026).
- Không có số liệu giá đối thủ để tính toán TCO delta, làm giảm độ tin cậy của khuyến nghị giá.
- Scraper không lấy được nội dung giá từ trang web đối thủ (chỉ thấy CSS), rủi ro thiếu thông tin thị trường.

## Gaps / Thiếu dữ liệu

- Cần cập nhật: Bảng giá niêm yết GreenNode VKS (Compute, Storage, Egress) — Dữ liệu cũ trong memory, chưa validate.
- Cần cập nhật: Bảng giá Viettel vOKS, FPT FKE, Bizfly BKE — Scraper chưa parse được nội dung giá.
- Thiếu dữ liệu: Chi phí ẩn (hidden cost) như egress fee, NAT Gateway, Load Balancer của các đối thủ để so sánh TCO thực tế.
