# Pricing Summary — 2026-06-29

Source: competitor-monitor run | Model: qwen/qwen3-5-27b

## Key Findings

- [RSS] [AWS Containers Blog](https://aws.amazon.com/blogs/containers/amazon-eks-now-supports-control-plane-egress-through-your-vpc) 2026-06-22 — AWS công bố tính năng 'customer-routed control plane egress' cho EKS. Tác động: Tăng áp lực cạnh tranh về bảo mật (churn risk) cho GreenNode VKS. Nếu GreenNode chưa có tính năng tương đương, khách hàng ngân hàng/chính phủ có thể yêu cầu giảm giá hoặc chuyển dịch sang AWS nếu họ chấp nhận rủi ro pháp lý thấp hơn. GreenNode cần xác minh tính năng này và chuẩn bị talk track về lợi thế 'data residency' tuyệt đối.
- [RSS] [AWS Containers Blog](https://aws.amazon.com/blogs/containers/faster-nodes-smarter-scaling-whats-new-inside-amazon-elastic-kubernetes-service-amazon-eks-auto-mode) 2026-06-23 — AWS cải tiến EKS Auto Mode (runtime, compute, storage, networking). Tác động: AWS đang tối ưu hóa trải nghiệm 'zero-management', làm giảm rào cản vận hành. GreenNode VKS cần xem xét lại định vị giá trị: nếu không thể cạnh tranh về độ tự động hóa, cần nhấn mạnh vào hỗ trợ kỹ thuật chuyên sâu (premium support) và tuân thủ pháp lý nội địa để biện minh cho mức giá.
- [RSS] [Vietnam.vn](https://news.google.com/rss/articles/CBMijwFBVV95cUxQUF9HNTZhVFREd0p4TWY5S0JEOEZTc09kTkQxVzg0MlRrZWQwWWRySF9vRmsyS3RfQmJsYnY2azRMazNsME9MSVo5eTR4SUxHUzc2dUNCUTdvYXBiOS11T0IyemU3eDBhWFV1aGNWaW9YZWJMQVRKbTJySVFpaW9YQjVQSmpMbFFrUmF2VU5Fdw?oc=5) 2026-06-27 — CMC Cloud hợp tác với UBND TP. Hà Nội phát triển chính phủ số và thành phố AI. Tác động: CMC gia tăng thị phần trong phân khúc GovTech. GreenNode cần rà soát lại chiến lược giá cho các dự án chính phủ (RFP) sắp tới, đặc biệt khi đối thủ có lợi thế địa phương mạnh.
- [Scrape] Viettel Cloud | https://viettelcloud.vn/san-pham/kubernetes | fetched_at=2026-06-29 — Trang sản phẩm Viettel vOKS không hiển thị bảng giá công khai. Tác động: Viettel tiếp tục chiến lược 'sales-led pricing' (giá qua đàm phán). GreenNode không thể so sánh trực tiếp giá niêm yết, cần tập trung vào TCO tổng thể (bao gồm chi phí vận hành và tuân thủ) thay vì chỉ so sánh giá compute.

## Recommended Actions

- Talk Track cho Sales: Khi khách hàng hỏi về giá so với AWS, nhấn mạnh 'Total Cost of Ownership' (TCO) bao gồm chi phí tuân thủ pháp lý (Data Residency), chi phí vận hành (managed service) và rủi ro pháp lý khi dùng hyperscaler. Không so sánh trực tiếp giá compute nếu không có dữ liệu mới.
- Pricing Recommendation: Rà soát lại bảng giá VKS cho phân khúc Enterprise/Gov. Nếu tính năng 'control plane egress' chưa có, cần ưu tiên phát triển hoặc chuẩn bị giải pháp thay thế (workaround) để không mất điểm trong RFP.
- Theo dõi thêm: Thiết lập cảnh báo tự động cho các thay đổi pricing trên trang web của AWS, GCP, Azure và các đối thủ nội địa. Yêu cầu bộ phận Sales thu thập thông tin giá từ các deal gần đây của đối thủ để cập nhật vào workspace.
- Phân tích TCO giả định: Sử dụng dữ liệu pricing cũ (với nhãn 'STALE') để xây dựng mô hình TCO giả định cho các scenario S1-S5, nhưng phải ghi rõ giả định và ngày dữ liệu. So sánh với các tính năng mới của AWS để đánh giá khoảng cách giá trị.

## Risks

- Thiếu dữ liệu pricing cụ thể (USD/giờ hoặc VND/tháng) từ tất cả các đối thủ trong 3 ngày qua, không thể tính toán TCO chính xác.
- Dữ liệu về tính năng mới của AWS (Control Plane Egress) có thể tạo ra rủi ro churn nếu GreenNode VKS không có tính năng tương đương hoặc không có chiến lược giá trị rõ ràng để bù đắp.
- Các đối thủ nội địa (Viettel, FPT, Bizfly) sử dụng mô hình giá kín (sales-led), gây khó khăn cho việc so sánh giá niêm yết trực tiếp.

## Gaps / Thiếu dữ liệu

- Cần cập nhật: memory/pricing/vks-pricing-2026.md — Dữ liệu pricing hiện tại trong workspace có thể đã cũ (last updated 2026-05-20), cần xác minh lại các mức giá compute, storage, egress và control plane.
- Không có thông tin về chương trình khuyến mãi (promo) hoặc giá Reserved Instances mới từ AWS, GCP, Azure trong 3 ngày qua.
- Không có dữ liệu về giá GPU (H100/A100) mới nhất từ các đối thủ, cần thiết cho phân tích TCO AI Inference/Training.
- Cần xác minh xem GreenNode VKS đã có tính năng 'customer-routed control plane egress' hay chưa để so sánh trực tiếp với AWS.
