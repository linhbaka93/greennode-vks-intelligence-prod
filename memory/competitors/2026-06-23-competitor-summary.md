# Competitor Summary — 2026-06-23

Source: daily-intelligence run | Model: qwen/qwen3-5-27b

## Key Findings

- [RSS] AWS Containers Blog | https://aws.amazon.com/blogs/containers/amazon-eks-now-supports-control-plane-egress-through-your-vpc | published_at=2026-06-22 — [RSS] [AWS Containers Blog](https://aws.amazon.com/blogs/containers/amazon-eks-now-supports-control-plane-egress-through-your-vpc) 2026-06-22 — AWS EKS ra mắt tính năng 'customer-routed control plane egress', cho phép định tuyến toàn bộ traffic control plane (admission webhooks, OIDC lookups) qua VPC của khách hàng thay vì internet public. Tác động tới GreenNode: ❌ Feature gap nghiêm trọng về bảo mật và kiến trúc mạng cho phân khúc Enterprise/Gov. Khách hàng tài chính/chính phủ yêu cầu control plane traffic không ra internet sẽ ưu tiên AWS nếu GreenNode chưa có giải pháp Private Link tương đương cho control plane. GreenNode cần rà soát khả năng triển khai Private Endpoint cho control plane ngay lập tức.
- [RSS] AWS News Blog | https://aws.amazon.com/blogs/aws/aws-weekly-roundup-ny-summit-recap-local-zone-in-hanoi-grok-4-3-in-bedrock-price-reductions-and-more-june-22-2026 | published_at=2026-06-22 — [RSS] [AWS News Blog](https://aws.amazon.com/blogs/aws/aws-weekly-roundup-ny-summit-recap-local-zone-in-hanoi-grok-4-3-in-bedrock-price-reductions-and-more-june-22-2026) 2026-06-22 — AWS công bố giảm giá (price reductions) và mở rộng Local Zone tại Hà Nội. Tác động tới GreenNode: Áp lực giá trực tiếp lên GreenNode đối với các workload không bắt buộc data residency onshore. Khách hàng có thể chuyển sang AWS Local Zone Hà Nội để tận dụng giá thấp hơn và độ trễ thấp, làm giảm lợi thế 'địa phương' của GreenNode. GreenNode cần rà soát lại TCO cho các use-case không yêu cầu lưu trữ dữ liệu trong nước để tránh mất khách.
- [RSS] AWS ML Blog | https://aws.amazon.com/blogs/machine-learning/building-pay-per-intelligence-for-ai-agents-how-ampersend-uses-amazon-bedrock-agentcore-payments | published_at=2026-06-22 — [RSS] [AWS ML Blog](https://aws.amazon.com/blogs/machine-learning/building-pay-per-intelligence-for-ai-agents-how-ampersend-uses-amazon-bedrock-agentcore-payments) 2026-06-22 — AWS công bố case study về 'pay-per-intelligence' cho AI Agents trên Bedrock AgentCore Payments. Tác động tới GreenNode: ❌ Feature gap về AI Agent infrastructure. AWS đang định hình tiêu chuẩn mới cho việc triển khai AI Agents với mô hình thanh toán linh hoạt. GreenNode VKS chưa có giải pháp tương đương cho AI Agents, có thể bị bỏ lại phía sau trong các dự án AI tiên tiến của doanh nghiệp.

## Risks

- Feature gap về bảo mật mạng (control plane egress) có thể khiến GreenNode mất các deal Enterprise/Gov lớn trong Q3/Q4 2026.
- Áp lực giá từ AWS Local Zone Hà Nội có thể làm giảm biên lợi nhuận hoặc mất khách hàng SME không yêu cầu data residency.
- Thiếu hụt giải pháp AI Agent infrastructure so với AWS Bedrock có thể làm giảm sức hút của GreenNode trong các dự án AI mới.

## Gaps / Thiếu dữ liệu

- Không có tin tức mới từ đối thủ Tier 1 nội địa (Viettel vOKS, FPT FKE, Bizfly BKE) trong 24h qua. Cần theo dõi thêm các kênh social và trang chủ của họ để phát hiện động thái pricing hoặc feature mới.
- Dữ liệu pricing chi tiết của AWS Local Zone Hà Nội chưa rõ ràng, cần `pricing_agent` phân tích sâu hơn để so sánh TCO.
