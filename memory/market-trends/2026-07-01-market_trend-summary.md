# Market Trend Summary — 2026-07-01

Source: monthly-brief run | Model: qwen/qwen3-5-27b

## Key Findings

- [RSS] [CNCF Blog](https://www.cncf.io/blog/2026/07/01/understanding-dynamic-resource-allocation-in-kubernetes) 2026-07-01 — Dynamic Resource Allocation (DRA) đạt GA trên Kubernetes v1.35, kèm theo NVIDIA dra-driver-nvidia-gpu được đưa vào SIGs. Tác động: Đây là tiêu chuẩn mới để quản lý GPU hiệu quả; GreenNode VKS cần hỗ trợ DRA ngay để tối ưu chi phí GPU node pool cho khách hàng AI.
- [RSS] [AWS Containers Blog](https://aws.amazon.com/blogs/containers/amazon-eks-now-supports-control-plane-egress-through-your-vpc) 2026-06-22 — AWS ra mắt 'customer-routed control plane egress' cho EKS, cho phép lưu lượng control plane đi qua VPC riêng thay vì internet công cộng. Tác động: Tăng rủi ro churn với khách hàng ngân hàng/chính phủ yêu cầu isolation tuyệt đối; GreenNode cần rà soát kiến trúc network hiện tại để đảm bảo tương đương hoặc vượt trội.
- [RSS] [Vietnam.vn](https://news.google.com/rss/articles/CBMijwFBVV95cUxQUF9HNTZhVFREd0p4TWY5S0JEOEZTc09kTkQxVzg0MlRrZWQwWWRySF9vRmsyS3RfQmJsYnY2azRMazNsME9MSVo5eTR4SUxHUzc2dUNCUTdvYXBiOS11T0IyemU3eDBhWFV1aGNWaW9YZWJMQVRKbTJySVFpaW9YQjVQSmpMbFFrUmF2VU5Fdw?oc=5) 2026-06-27 — CMC hợp tác UBND TP. Hà Nội phát triển chính phủ số và thành phố AI. Tác động: Đối thủ nội địa đang chiếm lĩnh các dự án Gov lớn; GreenNode cần tận dụng chứng nhận Doanh nghiệp Công nghệ cao (TP.HCM) để mở rộng sang khu vực miền Bắc hoặc tìm kiếm đối tác tích hợp.
- [RSS] [AWS News Blog](https://aws.amazon.com/blogs/aws/introducing-amazon-bedrock-managed-knowledge-base-for-faster-more-accurate-enterprise-ai-applications) 2026-06-17 — AWS giới thiệu Bedrock Managed Knowledge Base và AgentCore Web Search. Tác động: Hyperscaler đang đóng gói sẵn hạ tầng Agentic AI; GreenNode AgentBase cần nhấn mạnh lợi ích về data residency và tùy biến sâu hơn so với dịch vụ managed đóng kín.

## Recommended Actions

- Kiểm tra và lên kế hoạch hỗ trợ Kubernetes DRA (Dynamic Resource Allocation) cho VKS trong Q3/2026 để tối ưu hóa chi phí GPU cho khách hàng AI.
- Đánh giá lại kiến trúc Network của VKS: Nếu chưa có tính năng Control Plane Egress qua VPC, cần xây dựng bản whitepaper hoặc lộ trình roadmap để trấn an khách hàng regulated.
- Tận dụng chứng nhận Doanh nghiệp Công nghệ cao (TP.HCM) trong marketing tài liệu bán hàng (sales deck) để gia tăng uy tín khi đấu thầu các dự án Gov/Sovereign AI.

## Risks

- Churn risk từ khách hàng ngân hàng/chính phủ nếu GreenNode VKS chưa có tính năng Control Plane Egress qua VPC tương đương AWS EKS (đang là yêu cầu bắt buộc cho nhiều RFP mới).
- Áp lực cạnh tranh giá GPU khi AWS tung instance Blackwell mới; GreenNode cần minh bạch TCO cho các workload inference dài hạn.
- Đối thủ nội địa (CMC, Viettel IDC) đang tăng tốc hợp tác với chính quyền địa phương (Hà Nội, TP.HCM), có thể làm giảm thị phần dự án Gov của GreenNode nếu không có chiến lược đối tác rõ ràng.

## Gaps / Thiếu dữ liệu

- Cần xác minh kỹ thuật: GreenNode VKS hiện tại đã hỗ trợ DRA driver nào? Có roadmap cụ thể cho Kubernetes v1.35 chưa?
- Thiếu dữ liệu pricing chi tiết cho GPU Node Pool của GreenNode so với AWS EC2 G7 để đánh giá khả năng cạnh tranh về chi phí.
- Cần cập nhật thông tin về tiến độ triển khai thực tế của dự án CMC - Hà Nội để hiểu rõ scope và công nghệ họ sử dụng.
