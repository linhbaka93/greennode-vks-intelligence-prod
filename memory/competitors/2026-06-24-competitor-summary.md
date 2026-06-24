# Competitor Summary — 2026-06-24

Source: competitor-monitor run | Model: qwen/qwen3-5-27b

## Key Findings

- [RSS] AWS Containers Blog | https://aws.amazon.com/blogs/containers/faster-nodes-smarter-scaling-whats-new-inside-amazon-elastic-kubernetes-service-amazon-eks-auto-mode | published_at=2026-06-23 — [RSS] [AWS Containers Blog](https://aws.amazon.com/blogs/containers/faster-nodes-smarter-scaling-whats-new-inside-amazon-elastic-kubernetes-service-amazon-eks-auto-mode) 2026-06-23 — AWS công bố nâng cấp hiệu năng và khả năng mở rộng cho EKS Auto Mode (runtime, compute, storage, networking). Tác động tới GreenNode: ⚠️ Feature gap về tự động hóa và tối ưu hóa chi phí. EKS Auto Mode giúp khách hàng giảm vận hành và chi phí node; GreenNode cần rà soát khả năng cung cấp giải pháp autoscaling tự động tương đương (Karpenter/Cluster Autoscaler) để cạnh tranh về TCO.
- [RSS] AWS Containers Blog | https://aws.amazon.com/blogs/containers/amazon-eks-now-supports-control-plane-egress-through-your-vpc | published_at=2026-06-22 — [RSS] [AWS Containers Blog](https://aws.amazon.com/blogs/containers/amazon-eks-now-supports-control-plane-egress-through-your-vpc) 2026-06-22 — AWS EKS ra mắt tính năng 'customer-routed control plane egress', cho phép định tuyến toàn bộ traffic control plane (admission webhooks, OIDC lookups) qua VPC của khách hàng thay vì internet public. Tác động tới GreenNode: ❌ Feature gap nghiêm trọng về bảo mật và kiến trúc mạng cho phân khúc Enterprise/Gov. Khách hàng tài chính/chính phủ yêu cầu control plane traffic không ra internet sẽ ưu tiên AWS nếu GreenNode chưa có giải pháp tương đương (Private Link cho control plane).
- [RSS] AWS News Blog | https://aws.amazon.com/blogs/aws/announcing-amazon-ec2-g7-instances-accelerated-by-nvidia-rtx-pro-4500-blackwell-server-edition-gpus | published_at=2026-06-18 — [RSS] [AWS News Blog](https://aws.amazon.com/blogs/aws/announcing-amazon-ec2-g7-instances-accelerated-by-nvidia-rtx-pro-4500-blackwell-server-edition-gpus) 2026-06-18 — AWS công bố GA EC2 G7 instances với GPU NVIDIA RTX PRO 4500 Blackwell Server Edition cho AI inference và graphics. Tác động tới GreenNode: ❌ Feature gap về phần cứng GPU thế hệ mới. AWS cung cấp lợi thế hiệu năng ngay lập tức cho LLM inference nặng. GreenNode đang thua nếu khách hàng cần performance tối đa cho training/inference mà không có ràng buộc data residency VN.
- [RSS] Kubernetes Blog | https://kubernetes.io/blog/2026/06/24/wg-device-management-spotlight-2026 | published_at=2026-06-24 — [RSS] [Kubernetes Blog](https://kubernetes.io/blog/2026/06/24/wg-device-management-spotlight-2026) 2026-06-24 — Kubernetes SIG Device Management công bố spotlight về yêu cầu quản lý phần cứng mới (GPU, TPU, network interfaces) cho workload AI/Edge. Tác động tới GreenNode: ⚠️ Cơ hội định vị. GreenNode cần nhấn mạnh khả năng hỗ trợ GPU/Device Plugin tiên tiến trong VKS để đáp ứng xu hướng này, đặc biệt khi đối thủ nội địa chưa công bố rõ ràng về tính năng này.

## Risks

- ❌ Feature gap về Control Plane Egress: AWS đã có giải pháp định tuyến traffic control plane qua VPC riêng, trong khi GreenNode VKS chưa công bố tính năng tương đương. Đây là rào cản lớn cho khách hàng Gov/Finance yêu cầu bảo mật tối đa.
- ❌ Feature gap về GPU Blackwell: AWS đã GA GPU Blackwell (RTX PRO 4500) cho inference nặng. GreenNode cần rà soát roadmap GPU (A100/H100/Blackwell) để tránh mất khách hàng AI-native.
- ⚠️ Feature gap về Autoscaling tự động: EKS Auto Mode của AWS cung cấp khả năng tự động hóa cao hơn, giảm chi phí vận hành. GreenNode cần đảm bảo VKS có giải pháp autoscaling (Karpenter/Cluster Autoscaler) mạnh mẽ để cạnh tranh về TCO.

## Gaps / Thiếu dữ liệu

- Cần cập nhật: competitors/2026-06-17_viettel-voks_profile.md — dữ liệu cũ, chưa có thông tin mới về pricing hoặc feature update trong 7 ngày qua.
- Cần cập nhật: competitors/2026-06-17_fpt-cloud-fke_profile.md — dữ liệu cũ, chưa xác minh được GPU node pool hoặc pricing mới.
- Cần cập nhật: competitors/2026-06-17_bizfly-bke_profile.md — dữ liệu cũ, cần xác minh lại SLA và K8s versions mới nhất.
- Không fetch được trang social của đối thủ nội địa (Viettel, FPT, Bizfly) trong 24h qua do thiếu nội dung public hoặc login wall. Cần xác minh lại qua kênh khác.
