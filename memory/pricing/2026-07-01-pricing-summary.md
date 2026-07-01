# Pricing Summary — 2026-07-01

Source: competitor-monitor run | Model: qwen/qwen3-5-27b

## Key Findings

- [RSS] [AWS Containers Blog](https://aws.amazon.com/blogs/containers/amazon-eks-now-supports-control-plane-egress-through-your-vpc) 2026-06-22 — AWS cho phép định tuyến lưu lượng control plane qua VPC khách hàng. Tác động: Giảm rủi ro compliance cho ngân hàng/chính phủ; GreenNode cần xác nhận VKS đã đáp ứng yêu cầu này để tránh churn risk khi khách so sánh tính năng bảo mật.
- [RSS] [AWS News Blog](https://aws.amazon.com/blogs/aws/upgrade-amazon-eks-clusters-with-confidence-using-kubernetes-version-rollbacks) 2026-07-01 — AWS ra mắt tính năng rollback phiên bản Kubernetes trong 7 ngày. Tác động: Giảm chi phí downtime do lỗi upgrade; GreenNode cần rà soát quy trình upgrade VKS để đảm bảo SLA tương đương.
- [Scrape] Viettel/Bizfly/FPT | https://viettelcloud.vn/san-pham/kubernetes | fetched_at=2026-07-01 — Không thu thập được dữ liệu giá từ trang web đối thủ (chỉ thấy CSS/JS). Tác động: Không thể so sánh TCO trực tiếp; Sales cần dựa vào báo giá tùy chỉnh (quote-based) thay vì list price.

## Recommended Actions

- Talk Track: Nhấn mạnh Sovereign Compliance & Data Residency thay vì chỉ so sánh giá compute. Đối thủ global (AWS) đang tăng tính năng bảo mật (Egress), nhưng GreenNode vẫn giữ lợi thế tuyệt đối về Luật BVDLCN 2025.
- Pricing Recommendation: Yêu cầu Product Team cung cấp bảng giá VKS mới nhất (vòng 7 ngày tới) để update TCO calculator.
- Feature Check: Kiểm tra ngay khả năng định tuyến traffic control plane của VKS. Nếu chưa có, đánh giá lộ trình roadmap để tránh mất điểm với khách hàng ngân hàng.
- Sales Enablement: Cung cấp tài liệu so sánh 'Hidden Cost' (egress, support, migration) giữa VKS và Hyperscaler, vì list price thường không phản ánh đúng TCO thực tế.

## Risks

- Dữ liệu pricing GreenNode VKS trong workspace (file 2026-05-20) đã quá 40 ngày, chưa được refresh theo policy >30 ngày.
- Không có số liệu giá cụ thể từ đối thủ nội địa để tính toán delta TCO chính xác.
- Tính năng Control Plane Egress của AWS có thể tạo lợi thế cạnh tranh về security/compliance mà không cần giảm giá.

## Gaps / Thiếu dữ liệu

- Cần cập nhật: greennode/2026-05-20_greennode-vks_product-overview.md — dữ liệu cũ, chưa dùng được cho phân tích giá hiện tại.
- Thiếu bảng giá niêm yết (list price) của Viettel VOKS, Bizfly BKE, FPT FKE — scraper không lấy được nội dung giá.
- Thiếu thông tin về discount structure (Reserved/Savings Plan) của đối thủ nội địa để so sánh TCO dài hạn.
- Cần xác minh: GreenNode VKS có tính năng tương đương 'Control Plane Egress' hay không?
