# Competitor Summary — 2026-07-01

Source: monthly-brief run | Model: qwen/qwen3-5-27b

## Key Findings

- [RSS] AWS Containers Blog | https://aws.amazon.com/blogs/containers/amazon-eks-now-supports-control-plane-egress-through-your-vpc | published_at=2026-06-22
- [RSS] Vietnam.vn | https://news.google.com/rss/articles/CBMijwFBVV95cUxQUF9HNTZhVFREd0p4TWY5S0JEOEZTc09kTkQxVzg0MlRrZWQwWWRySF9vRmsyS3RfQmJsYnY2azRMazNsME9MSVo5eTR4SUxHUzc2dUNCUTdvYXBiOS11T0IyemU3eDBhWFV1aGNWaW9YZWJMQVRKbTJySVFpaW9YQjVQSmpMbFFrUmF2VU5Fdw?oc=5 | published_at=2026-06-27
- [RSS] AWS News Blog | https://aws.amazon.com/blogs/aws/introducing-amazon-bedrock-managed-knowledge-base-for-faster-more-accurate-enterprise-ai-applications | published_at=2026-06-17
- [RSS] GreenNode Blog | https://greennode.ai/blog/digest-june-2026 | published_at=2026-06-30
- [RSS] CNCF Blog | https://www.cncf.io/blog/2026/07/01/understanding-dynamic-resource-allocation-in-kubernetes | published_at=2026-07-01

## Risks

- {"risk": "Feature Gap - Control Plane Security", "description": "AWS EKS đã có tính năng định tuyến control plane traffic qua VPC riêng. Nếu GreenNode VKS chưa có cơ chế tương đương (private endpoint cho API server), sẽ khó thắng thầu các dự án ngân hàng/chính phủ yêu cầu strict network isolation.", "mitigation": "Kiểm tra kiến trúc mạng hiện tại của VKS. Nếu chưa hỗ trợ, cần có timeline rõ ràng hoặc giải pháp workaround (Private Link/VPC Peering) để Sales trình bày."}
- {"risk": "Gov Segment Competition", "description": "CMC Cloud vừa ký hợp tác lớn với UBND TP. Hà Nội. Đối thủ nội địa đang chiếm lĩnh các dự án chính phủ số ở miền Bắc.", "mitigation": "Tập trung vào lợi thế Chứng nhận Công nghệ cao TP.HCM và mối quan hệ hiện hữu (ví dụ: MSB Bank) để mở rộng sang các tỉnh thành phía Nam trước, sau đó tìm đối tác chiến lược cho miền Bắc."}

## Gaps / Thiếu dữ liệu

- Pricing details: Chưa có dữ liệu cụ thể về mức giá mới của FPT Cloud FKE hoặc Viettel IDC VKS trong tuần qua để so sánh TCO.
- Feature Parity: Chưa xác minh được GreenNode VKS đã hỗ trợ Kubernetes v1.35 (DRA GA) hay chưa. Cần kiểm tra internal docs.
- Social Signals: Không fetch được nội dung chi tiết từ trang Facebook/LinkedIn của đối thủ do login wall/consent wall. Chỉ dựa vào RSS/Blog public.
