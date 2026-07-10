# Pricing Summary — 2026-07-10

Source: weekly-digest run | Model: qwen/qwen3-5-27b

## Key Findings

- [RSS] [AWS Containers Blog](https://aws.amazon.com/blogs/containers/announcing-amazon-eks-rollback-for-safe-and-reliable-management-of-cluster-upgrades) 2026-07-01 — AWS ra mắt EKS Version Rollback tự động. Tác động: Giảm rủi ro downtime khi upgrade, giảm chi phí vận hành ẩn. GreenNode nên: Đánh giá quy trình recovery time của VKS; nếu chưa có rollback tự động, cần nhấn mạnh SLA hỗ trợ người dùng để bù đắp gap kỹ thuật.
- [RSS] [AWS Containers Blog](https://aws.amazon.com/blogs/containers/amazon-eks-now-supports-control-plane-egress-through-your-vpc) 2026-06-22 — AWS cho phép định tuyến control plane egress qua VPC khách hàng. Tác động: Giải quyết yêu cầu bảo mật nghiêm ngặt (ngân hàng/chính phủ) mà không cần gateway phức tạp. GreenNode nên: Kiểm tra xem VKS đã có tính năng tương đương hay chưa; đây là điểm chốt deal quan trọng cho segment Enterprise/Gov.
- [RSS] [Vietnam.vn](https://news.google.com/rss/articles/CBMirgFBVV95cUxPeWVaUWxVQnljSmdMZFBjV1BZb1g2dEFVdnN0dHNFemxfZ0dyQjZzak11dVc0QzBWdzJZMktXWHIzNjhpVjY2NGpldHF0ak5WN0xxOXVSWXBMbzlZX3JobjZmOVlDUVZqRHVWdGJNdE9jOXZUTC1tUlFGWjlUNkEyTk1nYm1rWlZrR0xSUWlqNmkzQS1RYUtqcVR6bVRUSFB6dTA0SnpnQ0o1RWxfVGc?oc=5) 2026-07-09 — Mục tiêu 300 tỷ USD ngành công nghệ số, hạ tầng số là lời giải. Tác động: Nhu cầu đầu tư hạ tầng nội địa tăng. GreenNode nên: Định vị VKS là giải pháp 'Make in Vietnam' an toàn pháp lý, chấp nhận margin cao hơn hyperscaler nhưng thấp hơn custom build.
- [Workspace] greennode/2026-05-20_greennode-vks_product-overview.md — VKS có 3 region (HCM, HAN, BKK) và CNI options (Cilium). Lưu ý: Dữ liệu cũ >30 ngày. Tác động: Cần xác nhận lại cấu hình pricing hiện tại. GreenNode nên: Yêu cầu Sales Ops cập nhật bảng giá tháng 7/2026 trước khi chạy TCO battlecard.

## Recommended Actions

- Talk Track Sales: Khi khách hỏi giá, tránh so sánh trực tiếp $/hour với AWS. Chuyển sang TCO tổng thể bao gồm chi phí tuân thủ (compliance), chi phí vận hành (ops overhead do thiếu rollback), và rủi ro pháp lý data residency.
- Pricing Recommendation: Đề xuất gói Reserved Instance hoặc Committed Use Discount cho khách hàng Enterprise cam kết >12 tháng để khóa lợi thế giá so với on-demand của hyperscaler.
- Product Feedback: Yêu cầu Engineering đánh giá timeline triển khai tính năng 'Control Plane Egress via VPC' và 'Cluster Rollback' để giảm churn risk ở phân khúc Gov/Bank.
- Data Refresh: Yêu cầu Finance/Sales Ops cung cấp snapshot giá mới nhất (July 2026) để agent có thể chạy mô hình TCO chuẩn S1-S5.

## Risks

- Dữ liệu sản phẩm VKS trong workspace (May 2026) đã quá hạn (>30 ngày), có thể không phản ánh chính sách giá mới nhất tháng 7/2026.
- Thiếu dữ liệu giá thực tế (effective rate) sau discount cho các deal lớn, chỉ dựa vào list price công khai sẽ sai lệch TCO thực tế.
- Đối thủ nội địa (FPT/Viettel) thường bán theo quote riêng (sales-led), khó so sánh trực tiếp với public pricing của AWS.

## Gaps / Thiếu dữ liệu

- Cần cập nhật: Bảng giá chi tiết VKS (Compute, Storage, Egress) tháng 7/2026 — hiện tại chỉ có product overview cũ.
- Cần xác minh: Chính sách egress fee của GreenNode so với AWS (thường là hidden cost lớn nhất trong TCO K8s).
- Không có dữ liệu giá GPU cụ thể cho scenario AI Inference/Training để tính toán TCO S4/S5.
- Không fetch được trang social của đối thủ để kiểm tra promo ngắn hạn (nếu có).
