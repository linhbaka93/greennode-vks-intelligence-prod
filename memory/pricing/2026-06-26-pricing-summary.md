# Pricing Summary — 2026-06-26

Source: weekly-digest run | Model: qwen/qwen3-5-27b

## Key Findings

- [RSS] [AWS News Blog](https://aws.amazon.com/blogs/aws/aws-weekly-roundup-ny-summit-recap-local-zone-in-hanoi-grok-4-3-in-bedrock-price-reductions-and-more-june-22-2026) 2026-06-22 — AWS công bố giảm giá (price reductions) và mở rộng Local Zone tại Hà Nội. Tác động: Áp lực giá trực tiếp lên GreenNode cho các workload không yêu cầu data residency nghiêm ngặt. GreenNode cần rà soát lại TCO cho các workload hybrid để tránh mất khách vào AWS do chênh lệch giá.
- [RSS] [AWS News Blog](https://aws.amazon.com/blogs/aws/announcing-amazon-ec2-g7-instances-accelerated-by-nvidia-rtx-pro-4500-blackwell-server-edition-gpus) 2026-06-18 — AWS GA EC2 G7 instances với GPU NVIDIA RTX PRO 4500 Blackwell Server Edition. Tác động: Feature gap về phần cứng GPU thế hệ mới. AWS cung cấp lợi thế hiệu năng ngay lập tức cho LLM inference nặng. GreenNode đang thua nếu khách hàng cần performance tối đa cho training/inference mà không có ràng buộc data residency VN.
- [RSS] [AWS Containers Blog](https://aws.amazon.com/blogs/containers/amazon-eks-now-supports-control-plane-egress-through-your-vpc) 2026-06-22 — AWS EKS ra mắt tính năng 'customer-routed control plane egress', cho phép định tuyến toàn bộ traffic control plane qua VPC của khách hàng. Tác động: Feature gap nghiêm trọng về bảo mật và kiến trúc mạng cho phân khúc Enterprise/Gov. Khách hàng tài chính/chính phủ yêu cầu control plane traffic không ra internet sẽ ưu tiên AWS nếu GreenNode chưa có giải pháp tương đương (Private Link cho control plane).
- [RSS] [AWS Containers Blog](https://aws.amazon.com/blogs/containers/faster-nodes-smarter-scaling-whats-new-inside-amazon-elastic-kubernetes-service-amazon-eks-auto-mode) 2026-06-23 — AWS công bố nâng cấp hiệu năng và khả năng mở rộng cho EKS Auto Mode. Tác động: Feature gap về tự động hóa và tối ưu hóa chi phí. EKS Auto Mode giúp khách hàng giảm vận hành và chi phí node; GreenNode cần đánh giá khả năng cạnh tranh về TCO vận hành cho các workload biến động cao.

## Recommended Actions

- Talk track cho Sales: Nhấn mạnh lợi thế data residency VN, compliance (Luật BVDLCN 2025, Luật An ninh mạng 2018), và hỗ trợ kỹ thuật local cho các khách hàng Enterprise/Gov. Đối với khách hàng không yêu cầu data residency, cần rà soát lại TCO và đề xuất giải pháp hybrid nếu cần.
- Pricing recommendation: Rà soát lại bảng giá VKS và đề xuất discount model (Reserved, Committed) cạnh tranh hơn cho các workload không yêu cầu data residency nghiêm ngặt để giữ khách trước áp lực giảm giá của AWS.
- Theo dõi thêm: Cập nhật ngay bảng giá đối thủ (AWS, FPT, Viettel, Bizfly) và tính toán TCO scenario S4 (AI Inference) với GPU Blackwell để đánh giá khả năng cạnh tranh của GreenNode.
- Theo dõi thêm: Đánh giá khả năng triển khai Private Link cho control plane hoặc giải pháp tương đương để đáp ứng yêu cầu bảo mật cao của Enterprise/Gov.

## Risks

- Thiếu dữ liệu pricing cụ thể (số liệu giá, discount, TCO) mới trong evidence bundle tuần này, không thể tính toán TCO delta chính xác.
- Dữ liệu pricing đối thủ (AWS, FPT, Viettel, Bizfly) trong workspace memory đã STALE (cần cập nhật), không dùng được cho phân tích TCO chi tiết.
- Feature gap về GPU Blackwell và Control Plane Egress có thể dẫn đến mất khách Enterprise/Gov nếu không có chiến lược giá bù đắp hoặc giải pháp kỹ thuật tương đương.

## Gaps / Thiếu dữ liệu

- Cần cập nhật: competitors/2026-06-17_bizfly-bke_profile.md — dữ liệu cũ, chưa dùng được.
- Cần cập nhật: competitors/2026-06-17_fpt-cloud-fke_profile.md — dữ liệu cũ, chưa dùng được.
- Cần cập nhật: competitors/2026-06-17_aws-eks_profile.md — dữ liệu cũ, chưa dùng được.
- Cần cập nhật: competitors/2026-06-17_viettel-voks_profile.md — dữ liệu cũ, chưa dùng được.
- Thiếu bảng giá cụ thể của AWS (EC2 G7, EKS Auto Mode) và đối thủ nội địa để tính toán TCO scenario S4 (AI Inference) và S2 (Mid Production).
- Thiếu thông tin về discount model (Reserved, Committed) của AWS và đối thủ nội địa để so sánh TCO dài hạn.
