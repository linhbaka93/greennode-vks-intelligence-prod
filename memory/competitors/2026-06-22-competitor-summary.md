# Competitor Summary — 2026-06-22

Source: daily-intelligence run | Model: qwen/qwen3-5-27b

## Key Findings

- [RSS] AWS Containers Blog | https://aws.amazon.com/blogs/containers/amazon-eks-now-supports-control-plane-egress-through-your-vpc | published_at=2026-06-22 — [RSS] [AWS Containers Blog](https://aws.amazon.com/blogs/containers/amazon-eks-now-supports-control-plane-egress-through-your-vpc) 2026-06-22 — AWS công bố tính năng 'customer-routed control plane egress' cho Amazon EKS, cho phép định tuyến lưu lượng control plane (admission webhooks, OIDC lookups) qua VPC của khách hàng thay vì đi qua internet công cộng. — Tác động tới GreenNode: Tăng áp lực cạnh tranh về bảo mật và compliance cho GreenNode VKS. Tính năng này là yêu cầu bắt buộc cho các khách hàng Enterprise/Gov có chính sách 'zero-trust' hoặc yêu cầu lưu lượng control plane không được ra internet. Nếu GreenNode chưa có tính năng tương đương, sẽ mất điểm trong các RFP yêu cầu cao về bảo mật.
- [RSS] AWS News Blog | https://aws.amazon.com/blogs/aws/aws-weekly-roundup-ny-summit-recap-local-zone-in-hanoi-grok-4-3-in-bedrock-price-reductions-and-more-june-22-2026 | published_at=2026-06-22 — [RSS] [AWS News Blog](https://aws.amazon.com/blogs/aws/aws-weekly-roundup-ny-summit-recap-local-zone-in-hanoi-grok-4-3-in-bedrock-price-reductions-and-more-june-22-2026) 2026-06-22 — AWS công bố mở rộng Local Zone tại Hà Nội và giảm giá một số dịch vụ (chi tiết chưa rõ trong snippet). — Tác động tới GreenNode: Mở rộng Local Zone tại Hà Nội giúp AWS giảm latency và chi phí egress cho khách hàng miền Bắc, trực tiếp cạnh tranh với GreenNode về data residency và hiệu năng. Giảm giá (nếu có) sẽ tạo áp lực pricing cho GreenNode trong các deal Enterprise.
- [RSS] GreenNode Blog | https://greennode.ai/blog/greennode-va-vng-cloud-hop-nhat-thuong-hieu | published_at=2026-06-21 — [RSS] [GreenNode Blog](https://greennode.ai/blog/greennode-va-vng-cloud-hop-nhat-thuong-hieu) 2026-06-21 — GreenNode chính thức công bố hợp nhất thương hiệu với VNG Cloud, xây dựng hệ sinh thái AI Cloud toàn diện. — Tác động tới GreenNode: Tín hiệu mạnh về định vị thương hiệu và cam kết đầu tư dài hạn. Tuy nhiên, đây là thông tin nội bộ, chưa có phản ứng từ đối thủ. Cần theo dõi xem đối thủ (đặc biệt là FPT, Viettel) có ra thông cáo phản ứng hay không.

## Risks

- {"risk": "AWS EKS đang dẫn đầu về tính năng bảo mật control plane (egress routing) và mở rộng hạ tầng tại VN (Local Zone Hà Nội). GreenNode có nguy cơ thua thế trong các RFP yêu cầu cao về bảo mật và latency nếu không có giải pháp tương đương.", "mitigation": "Kiểm tra và công bố tính năng tương đương của GreenNode VKS. Nếu chưa có, cần có kế hoạch triển khai nhanh hoặc chuẩn bị chiến lược cạnh tranh dựa trên các yếu tố khác (compliance, hỗ trợ, giá)."}
- {"risk": "Không có thông tin mới từ đối thủ Tier 1 nội địa (Viettel, FPT, Bizfly) trong 24h qua. Có thể họ đang chuẩn bị động thái lớn hoặc đang im lặng để quan sát phản ứng của thị trường với AWS.", "mitigation": "Tiếp tục theo dõi sát sao các nguồn tin của đối thủ. Chuẩn bị sẵn battlecard để phản ứng nhanh nếu có động thái mới."}

## Gaps / Thiếu dữ liệu

- Cần cập nhật: competitors/2026-06-17_viettel-idc-kubernetes_profile.md — dữ liệu cũ (2026-06-17), chưa có thông tin mới về VKS/vOKS trong 24h qua.
- Cần cập nhật: competitors/2026-06-17_fpt-cloud-fke_profile.md — dữ liệu cũ (2026-06-17), chưa có thông tin mới về FKE trong 24h qua.
- Cần cập nhật: competitors/2026-06-17_bizfly-bke_profile.md — dữ liệu cũ (2026-06-17), chưa có thông tin mới về BKE trong 24h qua.
- Không fetch được trang social của Viettel IDC, FPT Cloud, Bizfly Cloud trong 24h qua (có thể do login wall hoặc không có bài đăng mới). Cần xác minh lại bằng công cụ khác.
