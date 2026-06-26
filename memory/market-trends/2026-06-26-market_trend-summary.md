# Market Trend Summary — 2026-06-26

Source: weekly-digest run | Model: qwen/qwen3-5-27b

## Key Findings

- [RSS] [AWS Containers Blog](https://aws.amazon.com/blogs/containers/amazon-eks-now-supports-control-plane-egress-through-your-vpc) 2026-06-22 — AWS EKS ra mắt tính năng 'customer-routed control plane egress', cho phép định tuyến toàn bộ traffic control plane (admission webhooks, OIDC lookups) qua VPC của khách hàng thay vì internet public. Tác động tới GreenNode: ❌ Feature gap nghiêm trọng về bảo mật và kiến trúc mạng cho phân khúc Enterprise/Gov. Khách hàng tài chính/chính phủ yêu cầu control plane traffic không ra internet sẽ ưu tiên AWS nếu GreenNode chưa có giải pháp tương đương (Private Link cho control plane). GreenNode cần rà soát khả năng triển khai Private Endpoint cho API Server ngay lập tức.
- [RSS] [AWS News Blog](https://aws.amazon.com/blogs/aws/announcing-amazon-ec2-g7-instances-accelerated-by-nvidia-rtx-pro-4500-blackwell-server-edition-gpus) 2026-06-18 — AWS công bố GA EC2 G7 instances với GPU NVIDIA RTX PRO 4500 Blackwell Server Edition cho AI inference và graphics. Tác động tới GreenNode: ❌ Feature gap về phần cứng GPU thế hệ mới. AWS cung cấp lợi thế hiệu năng ngay lập tức cho LLM inference nặng. GreenNode đang thua nếu khách hàng cần performance tối đa cho training/inference mà không có ràng buộc data residency VN. Cần rà soát roadmap GPU (A100/H100/Blackwell) và thời gian ra mắt tại VN.
- [RSS] [AWS News Blog](https://aws.amazon.com/blogs/aws/aws-weekly-roundup-ny-summit-recap-local-zone-in-hanoi-grok-4-3-in-bedrock-price-reductions-and-more-june-22-2026) 2026-06-22 — AWS công bố giảm giá (price reductions) và mở rộng Local Zone tại Hà Nội. Tác động: Áp lực giá trực tiếp lên GreenNode cho các workload không yêu cầu data residency nghiêm ngặt. GreenNode cần rà soát lại TCO cho các workload hybrid để tránh mất khách vào AWS do chênh lệch giá.
- [RSS] [AWS HPC Blog](https://aws.amazon.com/blogs/hpc/transforming-hpc-operations-with-intelligent-workload-orchestration-on-aws) 2026-06-26 — AWS công bố giải pháp orchestration workload thông minh cho HPC, cho phép tự động hóa quy trình tính toán hiệu năng cao thay vì cấu hình thủ công. Tác động tới GreenNode: ⚠️ Feature gap về tự động hóa HPC. Nếu khách hàng Enterprise/Gov có workload HPC/AI nặng, AWS cung cấp giải pháp 'end-to-end' giảm vận hành. GreenNode cần rà soát khả năng tích hợp các công cụ tự động hóa HPC (như Slurm trên K8s) vào VKS.
- [RSS] [Vietnam.vn](https://news.google.com/rss/articles/CBMilgFBVV95cUxPdVhYNFpaQ1FXUWQxVkRRc2RPSUNvVE84eWkzMW5Ha290UVY3LU5nN2otalZhWkdlN08zUWstV1pPaElJTk5LeVk3TDE0NVlrV2x6Q2kwaGNXZzBEV1BPYUlGeHljRU83SzhsdHBxanZRQkI1NFJQcmNfbVVoaXJsaGdhOXBoLWtYemlMVkRlSlBZN1U3bmc?oc=5) 2026-06-19 — Bài báo đề cập đến việc doanh nghiệp Việt Nam đang hưởng lợi từ hạ tầng cloud 'nước ngoài' tại Hà Nội (Local Zone). Tác động: Củng cố xu hướng hybrid/multi-cloud. GreenNode cần định vị rõ ràng lợi thế 'Sovereign AI' (dữ liệu không rời VN) so với Local Zone của AWS để giữ chân khách hàng Gov/Finance.
- [RSS] [Kubernetes Blog](https://kubernetes.io/blog/2026/06/24/wg-device-management-spotlight-2026) 2026-06-24 — Kubernetes upstream tập trung vào quản lý thiết bị (Device Management) cho AI, Edge và Telecom, yêu cầu phân bổ phần cứng vượt qua CPU/RAM (GPU, TPU, NIC). Tác động: Cơ hội cho GreenNode nâng cao VKS bằng cách hỗ trợ tốt hơn các CRD quản lý thiết bị (Device Plugin) cho workload AI/Edge, tạo điểm khác biệt về kỹ thuật so với các đối thủ chỉ cung cấp K8s cơ bản.
- [Blog] [GreenNode Blog](https://greennode.ai/blog/greennode-achieves-soc-2-type2-report) 2026-06-23 — GreenNode công bố đạt báo cáo SOC 2 Type 2. Tác động: ✅ Lợi thế cạnh tranh lớn cho phân khúc Enterprise/Gov. Đây là bằng chứng thực tế về compliance, giúp GreenNode đối đầu với AWS/FPT/Viettel trong các RFP yêu cầu bảo mật cao. Cần đẩy mạnh truyền thông điểm này trong các tài liệu bán hàng.
- [RSS] [CNCF Blog](https://www.cncf.io/blog/2026/06/25/building-a-cluster-aware-ai-agent-with-kubernetes-argo-cd-and-gitops) 2026-06-25 — CNCF giới thiệu cách xây dựng AI Agent tự chủ (self-hosted) trong Kubernetes với GitOps, không cần data rời khỏi cluster. Tác động: Cơ hội cho GreenNode phát triển giải pháp 'Sovereign AI Agent' trên VKS, tận dụng lợi thế data residency để thu hút khách hàng muốn chạy AI Agent nội bộ mà không lo rò rỉ dữ liệu.

## Recommended Actions

- Urgent: Rà soát và xác nhận khả năng triển khai 'Private Link cho Control Plane' (hoặc giải pháp tương đương) trên VKS. Nếu chưa có, đưa vào roadmap ưu tiên cao (P0) để đối phó với yêu cầu bảo mật của khách hàng Gov/Finance.
- Urgent: Cập nhật roadmap phần cứng GPU. Xác định thời gian cung cấp GPU Blackwell hoặc các dòng GPU thế hệ mới tương đương để cạnh tranh với AWS G7.
- Marketing: Đẩy mạnh truyền thông về chứng nhận SOC 2 Type 2 mới đạt được như một điểm khác biệt chính (Key Differentiator) cho phân khúc Enterprise/Gov.
- Product: Nghiên cứu tích hợp các công cụ tự động hóa HPC (như Slurm trên K8s) vào VKS để lấp đầy feature gap so với AWS HPC Blog.
- Sales: Chuẩn bị tài liệu so sánh TCO cho các workload hybrid, nhấn mạnh lợi ích của data residency và SOC 2 để đối phó với áp lực giá từ AWS Local Zone.

## Risks

- Rủi ro mất khách hàng Enterprise/Gov do feature gap về 'Control Plane Egress' (Private Link cho API Server). AWS đã có giải pháp, trong khi GreenNode chưa xác nhận khả năng tương đương.
- Rủi ro về hiệu năng AI: Khách hàng cần GPU Blackwell cho inference nặng sẽ chuyển sang AWS nếu GreenNode không có roadmap rõ ràng về phần cứng mới.
- Áp lực giá từ AWS Local Zone Hà Nội: Các workload không yêu cầu data residency nghiêm ngặt có thể bị thu hút bởi giá thấp hơn của AWS.
- Rủi ro về xu hướng HPC: Nếu GreenNode không tích hợp các công cụ tự động hóa HPC, sẽ mất cơ hội từ các tổ chức nghiên cứu và doanh nghiệp lớn có workload tính toán nặng.

## Gaps / Thiếu dữ liệu

- Cần cập nhật: competitors/2026-06-17_bizfly-bke_profile.md — dữ liệu cũ, chưa dùng được.
- Cần cập nhật: competitors/2026-06-17_fpt-cloud-fke_profile.md — dữ liệu cũ, chưa dùng được.
- Cần cập nhật: competitors/2026-06-17_aws-eks_profile.md — dữ liệu cũ, chưa dùng được.
- Cần cập nhật: competitors/2026-06-17_viettel-voks_profile.md — dữ liệu cũ, chưa dùng được.
- Thiếu thông tin cụ thể về roadmap GPU (Blackwell/A100/H100) của GreenNode để so sánh trực tiếp với AWS G7.
- Thiếu thông tin chi tiết về khả năng triển khai Private Link cho Control Plane của VKS (cần xác minh từ đội ngũ kỹ thuật).
- Thiếu dữ liệu về giá cụ thể của AWS Local Zone Hà Nội sau đợt giảm giá để tính toán TCO so sánh.
