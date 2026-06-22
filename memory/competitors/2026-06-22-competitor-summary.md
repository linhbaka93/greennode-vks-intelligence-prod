# Competitor Summary — 2026-06-22

Source: competitor-monitor run | Model: qwen/qwen3-5-27b

## Key Findings

- [RSS] [AWS Containers Blog](https://aws.amazon.com/blogs/containers/amazon-eks-now-supports-control-plane-egress-through-your-vpc) 2026-06-22 — AWS EKS ra mắt tính năng 'customer-routed control plane egress', cho phép định tuyến traffic control plane (admission webhooks, OIDC lookups) qua VPC của khách hàng thay vì internet public. Tác động tới GreenNode: ❌ Feature gap về bảo mật và kiến trúc mạng cho Enterprise. Khách hàng Gov/Finance yêu cầu control plane traffic không ra internet sẽ ưu tiên AWS nếu GreenNode chưa có giải pháp tương đương (Private Link cho control plane). GreenNode cần rà soát khả năng triển khai Private Endpoint cho API Server.
- [RSS] [AWS ML Blog](https://aws.amazon.com/blogs/machine-learning/introducing-web-search-on-amazon-bedrock-agentcore) 2026-06-19 — AWS Bedrock AgentCore tích hợp Web Search GA, cho phép AI agents truy cập web an toàn (zero egress) và trả về kết quả tìm kiếm. Tác động tới GreenNode: ❌ Feature gap về AI Agent infrastructure. AWS cung cấp giải pháp 'end-to-end' cho RAG và Agent mà VKS chưa có. Khách hàng Enterprise muốn triển khai AI nhanh có thể chọn AWS nếu không cần data residency VN. GreenNode đang thua về tốc độ ra mắt tính năng AI-native.
- [RSS] [AWS News Blog](https://aws.amazon.com/blogs/aws/aws-weekly-roundup-ny-summit-recap-local-zone-in-hanoi-grok-4-3-in-bedrock-price-reductions-and-more-june-22-2026) 2026-06-22 — AWS công bố Local Zone tại Hà Nội và giảm giá một số dịch vụ. Tác động tới GreenNode: ⚠️ Pricing pressure & Latency advantage. AWS Local Zone tại HN giảm latency cho khách hàng miền Bắc, cạnh tranh trực tiếp với GreenNode HAN region. Nếu AWS giảm giá, GreenNode có thể mất lợi thế về giá cho workload không yêu cầu data residency tuyệt đối. GreenNode cần xác minh mức giá cụ thể của Local Zone HN.
- [Scrape] Viettel vOKS | https://viettelcloud.vn/san-pham/kubernetes | fetched_at=2026-06-22 — Không có thay đổi nội dung đáng kể so với snapshot trước. Trang sản phẩm vẫn thiếu thông tin chi tiết về pricing, SLA, và K8s versions. Tác động tới GreenNode: ⚠️ Không có tín hiệu mới. Viettel vẫn giữ vị thế 'black box' với thông tin ít công khai, tập trung vào bán hàng qua quan hệ. GreenNode không bị đe dọa trực tiếp từ tính năng mới trong 24h qua.
- [Scrape] FPT FKE | https://fptcloud.com/kubernetes | fetched_at=2026-06-22 — Không có thay đổi nội dung đáng kể. Trang sản phẩm vẫn ít chi tiết kỹ thuật. Tác động tới GreenNode: ⚠️ Không có tín hiệu mới. FPT vẫn tập trung vào Managed/Dedicated mode nhưng chưa công bố tính năng mới nổi bật.
- [Scrape] Bizfly BKE | https://bizflycloud.vn/kubernetes | fetched_at=2026-06-22 — Không có thay đổi nội dung đáng kể. Tác động tới GreenNode: ⚠️ Không có tín hiệu mới. Bizfly vẫn giữ vị thế Tier 1 SME với GPU node pool đã xác nhận trước đó.

## Risks

- ❌ Feature gap về AI Agent infrastructure: AWS Bedrock AgentCore (Web Search, Payments) đang dẫn trước GreenNode AgentBase về tính năng 'end-to-end' cho RAG và Agent. Khách hàng Enterprise muốn triển khai AI nhanh có thể chọn AWS nếu không cần data residency VN.
- ❌ Feature gap về Control Plane Security: AWS EKS cho phép định tuyến control plane traffic qua VPC riêng (zero egress). GreenNode cần có giải pháp tương đương để cạnh tranh với khách hàng Gov/Finance yêu cầu bảo mật cao.
- ❌ Pricing pressure từ AWS Local Zone HN: AWS mở rộng Local Zone tại Hà Nội có thể giảm latency và cạnh tranh giá với GreenNode HAN region cho workload không yêu cầu data residency tuyệt đối.

## Gaps / Thiếu dữ liệu

- Cần cập nhật: competitors/2026-06-21-competitor-summary.md — Dữ liệu cũ, chưa phản ánh tin tức AWS EKS control plane egress (2026-06-22) và AWS Local Zone HN.
- Cần xác minh: Pricing AWS Local Zone HN — Chưa có số liệu cụ thể về giá và so sánh với GreenNode HAN.
- Cần xác minh: GreenNode VKS Private Endpoint cho Control Plane — Chưa rõ khả năng triển khai để đáp ứng yêu cầu 'zero egress' của khách hàng.
