# Competitor Summary — 2026-06-23

Source: daily-intelligence run | Model: qwen/qwen3-5-27b

## Key Findings

- [RSS] AWS Containers Blog | https://aws.amazon.com/blogs/containers/amazon-eks-now-supports-control-plane-egress-through-your-vpc | published_at=2026-06-22 — [RSS] [AWS Containers Blog](https://aws.amazon.com/blogs/containers/amazon-eks-now-supports-control-plane-egress-through-your-vpc) 2026-06-22 — AWS công bố tính năng 'customer-routed control plane egress' cho Amazon EKS, cho phép định tuyến lưu lượng control plane (admission webhooks, OIDC lookups) qua VPC của khách hàng thay vì internet công cộng. — Tác động tới GreenNode: Tăng áp lực cạnh tranh về bảo mật và compliance cho GreenNode VKS. Đây là tính năng bắt buộc đối với nhiều khách hàng ngân hàng/chính phủ yêu cầu lưu lượng control plane không bao giờ ra internet. Nếu GreenNode chưa có hoặc chưa công bố rõ ràng, đây là điểm yếu trong RFP.
- [RSS] AWS Containers Blog | https://aws.amazon.com/blogs/containers/faster-nodes-smarter-scaling-whats-new-inside-amazon-elastic-kubernetes-service-amazon-eks-auto-mode | published_at=2026-06-23 — [RSS] [AWS Containers Blog](https://aws.amazon.com/blogs/containers/faster-nodes-smarter-scaling-whats-new-inside-amazon-elastic-kubernetes-service-amazon-eks-auto-mode) 2026-06-23 — AWS công bố cải tiến hiệu năng và khả năng mở rộng cho EKS Auto Mode trên 4 trụ cột: runtime, compute, storage, networking. — Tác động tới GreenNode: AWS đang tối ưu hóa trải nghiệm 'zero-ops' cho Kubernetes, giảm rào cản gia nhập cho các khách hàng không có đội ngũ K8s chuyên sâu. Điều này đe dọa phân khúc khách hàng SME/Mid-market mà GreenNode đang nhắm đến nếu không có giải pháp tự động hóa tương đương.
- [RSS] AWS News Blog | https://aws.amazon.com/blogs/aws/aws-weekly-roundup-ny-summit-recap-local-zone-in-hanoi-grok-4-3-in-bedrock-price-reductions-and-more-june-22-2026 | published_at=2026-06-22 — [RSS] [AWS News Blog](https://aws.amazon.com/blogs/aws/aws-weekly-roundup-ny-summit-recap-local-zone-in-hanoi-grok-4-3-in-bedrock-price-reductions-and-more-june-22-2026) 2026-06-22 — AWS nhắc lại thông tin về Local Zone tại Hà Nội và giảm giá trong bản tin tuần. — Tác động tới GreenNode: Việc AWS nhắc lại Local Zone Hà Nội cho thấy họ đang tích cực khai thác lợi thế 'hybrid' (hạ tầng tại VN + dịch vụ global). Điều này làm mờ ranh giới giữa 'local cloud' và 'hyperscaler', gây khó khăn cho GreenNode khi thuyết phục khách hàng về sự cần thiết của một nhà cung cấp thuần Việt.

## Risks

- {"risk": "Gap về tính năng bảo mật control plane: AWS đã công bố tính năng định tuyến egress qua VPC, trong khi GreenNode chưa có thông tin công khai tương tự trong 24h qua.", "mitigation": "Kiểm tra kỹ thuật nội bộ và chuẩn bị tài liệu kỹ thuật ngay lập tức. Nếu chưa có, cần có kế hoạch phát triển hoặc giải pháp thay thế rõ ràng."}
- {"risk": "Áp lực từ AI-native của AWS: AWS liên tục ra mắt các tính năng AI (Bedrock AgentCore, SageMaker) tích hợp sâu với EKS, trong khi đối thủ nội địa (Viettel, FPT, Bizfly) chưa có động thái tương tự trong 24h qua.", "mitigation": "Tập trung vào các use-case AI cụ thể của khách hàng VN (xử lý văn bản tiếng Việt, tuân thủ dữ liệu) mà AWS khó đáp ứng tốt bằng các mô hình global."}

## Gaps / Thiếu dữ liệu

- Không có tin tức mới từ Viettel IDC, FPT Cloud, Bizfly Cloud trong 24h qua. Cần theo dõi thêm các kênh social và website chính thức của họ để phát hiện các động thái không được đăng tải qua RSS.
- Thiếu thông tin chi tiết về pricing và SLA của các đối thủ nội địa. Cần cập nhật định kỳ từ các nguồn scrape hoặc contact sales.
