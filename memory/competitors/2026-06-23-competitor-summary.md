# Competitor Summary — 2026-06-23

Source: competitor-monitor run | Model: qwen/qwen3-5-27b

## Key Findings

- [RSS] AWS Containers Blog | https://aws.amazon.com/blogs/containers/amazon-eks-now-supports-control-plane-egress-through-your-vpc | published_at=2026-06-22 — AWS EKS ra mắt tính năng 'customer-routed control plane egress', cho phép định tuyến toàn bộ traffic control plane (admission webhooks, OIDC lookups) qua VPC của khách hàng thay vì internet public. — Tác động tới GreenNode: ❌ Feature gap nghiêm trọng về bảo mật và kiến trúc mạng cho phân khúc Enterprise/Gov. Khách hàng tài chính/chính phủ yêu cầu control plane traffic không ra internet sẽ ưu tiên AWS nếu GreenNode chưa có giải pháp tương đương (Private Link cho control plane).
- [RSS] AWS News Blog | https://aws.amazon.com/blogs/aws/aws-weekly-roundup-ny-summit-recap-local-zone-in-hanoi-grok-4-3-in-bedrock-price-reductions-and-more-june-22-2026 | published_at=2026-06-22 — AWS công bố giảm giá (price reductions) và mở rộng Local Zone tại Hà Nội trong bản tin tuần. — Tác động tới GreenNode: ⚠️ Áp lực giá trực tiếp lên GreenNode nếu khách hàng không yêu cầu data residency nghiêm ngặt. Local Zone Hà Nội giúp AWS cạnh tranh tốt hơn về latency và giá cho các workload hybrid.
- [RSS] AWS Containers Blog | https://aws.amazon.com/blogs/containers/faster-nodes-smarter-scaling-whats-new-inside-amazon-elastic-kubernetes-service-amazon-eks-auto-mode | published_at=2026-06-23 — AWS EKS Auto Mode cập nhật cải thiện hiệu năng và khả năng mở rộng trên 4 trụ cột: runtime, compute, storage, networking. — Tác động tới GreenNode: ❌ Feature gap về tự động hóa vận hành (Auto Mode). AWS cung cấp trải nghiệm 'serverless K8s' mạnh mẽ hơn, giảm gánh nặng vận hành cho khách hàng. GreenNode VKS cần so sánh khả năng autoscaling (HPA/VPA/Karpenter) hiện tại.
- [RSS] AWS Artificial Intelligence | https://aws.amazon.com/blogs/machine-learning/shared-infrastructure-isolated-tenants-pool-model-multi-tenancy-with-amazon-bedrock-agentcore | published_at=2026-06-23 — AWS Bedrock AgentCore ra mắt các mẫu kiến trúc cho multi-tenancy (shared infrastructure, isolated tenants) và pay-per-intelligence cho AI agents. — Tác động tới GreenNode: ❌ Feature gap về AI Agent infrastructure. AWS cung cấp giải pháp 'end-to-end' cho RAG và Agent với mô hình tính phí linh hoạt. GreenNode AgentBase cần rà soát khả năng hỗ trợ multi-tenancy và pay-per-use cho AI agents.
- [Scrape] Viettel IDC | https://viettelcloud.vn/san-pham/kubernetes | fetched_at=2026-06-23 — Không có tin tức mới từ đối thủ Tier 1 nội địa (Viettel vOKS, FPT FKE, Bizfly BKE) trong 24h qua. — Tác động tới GreenNode: ⚠️ Không có thay đổi đáng kể về pricing hoặc feature từ đối thủ nội địa. Tuy nhiên, dữ liệu scrape chỉ trả về HTML/CSS, không có nội dung sản phẩm mới.

## Risks

- Feature gap về bảo mật mạng (control plane egress) so với AWS có thể làm mất khách hàng Enterprise/Gov nếu không được giải quyết sớm.
- Áp lực giá từ AWS Local Zone Hà Nội và giảm giá có thể ảnh hưởng đến các khách hàng không yêu cầu data residency nghiêm ngặt.
- Thiếu thông tin cập nhật về đối thủ nội địa (Viettel, FPT, Bizfly) do dữ liệu scrape không đầy đủ.

## Gaps / Thiếu dữ liệu

- Cần cập nhật: competitors/2026-06-17_viettel-voks_profile.md — dữ liệu cũ, chưa xác minh pricing và SLA mới.
- Cần cập nhật: competitors/2026-06-17_fpt-cloud-fke_profile.md — dữ liệu cũ, chưa xác minh GPU support trên FKE.
- Cần cập nhật: competitors/2026-06-17_bizfly-bke_profile.md — dữ liệu cũ, chưa xác minh SLA và K8s versions mới.
- Không fetch được nội dung chi tiết từ trang sản phẩm của Viettel, FPT, Bizfly (chỉ có HTML/CSS); cần cải thiện scraper hoặc kiểm tra social media.
