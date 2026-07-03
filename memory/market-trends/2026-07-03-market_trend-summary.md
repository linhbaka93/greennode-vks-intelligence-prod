# Market Trend Summary — 2026-07-03

Source: weekly-digest run | Model: qwen/qwen3-5-27b

## Key Findings

- [RSS] [vietnamnews.vn](https://news.google.com/rss/articles/CBMiqwFBVV95cUxQYlBCY1FrdVQzbXhwNS1pcGtlS05hd1FSZGpYQnJ2bE5pMnhrUUNONWtQampHUV92WHpMd2V6UkdJX19XbFVDdndmcUZyeVIzMFIyWkxYZmhLRS1leWJZeGRLblJ0REhTandMLU42NEtQRVFHaDBtZGNVTWhfbFhhNkNOYjhQSHhsbDBzSFFQWXNtV0lSRlNPV21pUTAzMkQtM1VyNl9tZHBWM28?oc=5) 2026-07-02 — AWS Local Zone tại Hà Nội được quảng bá là giải pháp 'unlocking AI for Vietnamese businesses'. Tác động: Cạnh tranh trực tiếp về độ trễ và residency cho workload AI tại miền Bắc. GreenNode cần nhấn mạnh lợi thế Sovereign Compliance (Luật BVDLCN) mà Local Zone có thể chưa đáp ứng đầy đủ so với data center nội địa hoàn toàn.
- [RSS] [CNCF Blog](https://www.cncf.io/blog/2026/07/01/understanding-dynamic-resource-allocation-in-kubernetes) 2026-07-01 — Dynamic Resource Allocation (DRA) đạt GA trong Kubernetes v1.35, NVIDIA driver chuyển sang SIGs. Tác động: Yêu cầu bắt buộc để tối ưu hiệu năng GPU node pool cho AI workloads. Nếu GreenNode VKS chậm hỗ trợ DRA, sẽ bị tụt hậu về TCO so với đối thủ hyperscaler.
- [RSS] [AWS Containers Blog](https://aws.amazon.com/blogs/containers/announcing-amazon-eks-rollback-for-safe-and-reliable-management-of-cluster-upgrades) 2026-07-01 — AWS ra mắt Amazon EKS Version Rollback cho phép hạ cấp cluster an toàn trong 7 ngày. Tác động: Feature gap về độ tin cậy vận hành. Khách hàng Enterprise/Gov coi đây là tiêu chuẩn bảo hiểm khi upgrade; thiếu tính năng này làm tăng rủi ro churn khi gặp sự cố upgrade.
- [RSS] [Vietnam.vn](https://news.google.com/rss/articles/CBMijwFBVV95cUxQUF9HNTZhVFREd0p4TWY5S0JEOEZTc09kTkQxVzg0MlRrZWQwWWRySF9vRmsyS3RfQmJsYnY2azRMazNsME9MSVo5eTR4SUxHUzc2dUNCUTdvYXBiOS11T0IyemU3eDBhWFV1aGNWaW9YZWJMQVRKbTJySVFpaW9YQjVQSmpMbFFrUmF2VU5Fdw?oc=5) 2026-06-27 — Hà Nội và CMC hợp tác phát triển chính phủ số và thành phố AI. Tác động: Xác nhận xu hướng đầu tư hạ tầng AI chủ quyền tại VN. Cơ hội cho GreenNode tham gia RFP các dự án GovTech nếu chứng minh được khả năng tuân thủ dữ liệu tốt hơn đối thủ nước ngoài.

## Recommended Actions

- Product Team: Đánh giá khả năng tích hợp K8s DRA vào VKS trong Q3/Q4 2026 để tối ưu GPU scheduling.
- Sales/Marketing: Chuẩn bị tài liệu so sánh 'Sovereign Compliance' giữa GreenNode VKS và AWS Local Zone, nhấn mạnh Luật BVDLCN 2025.
- Engineering: Nghiên cứu thiết kế tính năng 'Safe Upgrade/Rollback' cho VKS để thu hẹp feature gap với EKS.
- Business Dev: Theo dõi sát sao các gói thầu Chính phủ số tại Hà Nội liên quan đến CMC để tìm cơ hội đối tác hoặc cạnh tranh.

## Risks

- Khách hàng AI tại miền Bắc có thể chuyển sang AWS Local Zone Hà Nội do tích hợp sâu với hệ sinh thái AWS (Bedrock, Sagemaker) mặc dù chi phí egress/residency có thể cao hơn.
- Feature gap về EKS Rollback và Control Plane Observability làm giảm điểm tin cậy (trust score) khi đấu thầu các dự án Gov/Finance yêu cầu SLA cao.
- Nếu không hỗ trợ K8s DRA kịp thời, hiệu năng GPU của GreenNode VKS sẽ kém tối ưu hơn so với đối thủ, dẫn đến TCO cao hơn cho khách hàng chạy AI training/inference.

## Gaps / Thiếu dữ liệu

- Cần xác minh giá cụ thể và SLA của AWS Local Zone Hà Nội để so sánh trực tiếp với GreenNode HAN Region.
- Chưa rõ lộ trình internal của GreenNode VKS cho việc implement tính năng Rollback tương đương EKS.
- Thiếu dữ liệu về mức độ adoption thực tế của K8s DRA trong cộng đồng khách hàng hiện tại của GreenNode.
