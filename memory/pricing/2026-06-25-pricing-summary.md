# Pricing Summary — 2026-06-25

Source: competitor-monitor run | Model: qwen/qwen3-5-27b

## Key Findings

- [RSS] [AWS News Blog](https://aws.amazon.com/blogs/aws/aws-weekly-roundup-ny-summit-recap-local-zone-in-hanoi-grok-4-3-in-bedrock-price-reductions-and-more-june-22-2026) 2026-06-22 — AWS công bố giảm giá (price reductions) và mở rộng Local Zone tại Hà Nội. Tác động: Áp lực giá trực tiếp lên GreenNode cho các workload không yêu cầu data residency nghiêm ngặt. GreenNode cần rà soát lại TCO cho các workload hybrid để tránh mất khách vào AWS do chênh lệch giá.
- [RSS] [AWS Containers Blog](https://aws.amazon.com/blogs/containers/faster-nodes-smarter-scaling-whats-new-inside-amazon-elastic-kubernetes-service-amazon-eks-auto-mode) 2026-06-23 — AWS nâng cấp EKS Auto Mode (runtime, compute, storage, networking). Tác động: Tăng áp lực về hiệu quả vận hành (TCO) cho GreenNode. Khách hàng SME/Mid-market có thể yêu cầu tính năng tự động hóa tương tự để giảm chi phí vận hành, nếu GreenNode không có giải pháp tương đương, sẽ mất lợi thế về giá trị vận hành.
- [RSS] [AWS Containers Blog](https://aws.amazon.com/blogs/containers/amazon-eks-now-supports-control-plane-egress-through-your-vpc) 2026-06-22 — AWS EKS ra mắt tính năng 'customer-routed control plane egress'. Tác động: Feature gap nghiêm trọng về bảo mật và kiến trúc mạng cho phân khúc Enterprise/Gov. Khách hàng tài chính/chính phủ yêu cầu control plane traffic không ra internet sẽ ưu tiên AWS nếu GreenNode chưa có giải pháp tương đương (Private Link cho control plane).

## Recommended Actions

- Talk track cho Sales: Nhấn mạnh lợi thế 'Sovereign AI' và Data Residency tại VN của GreenNode khi đối thủ AWS giảm giá. Sử dụng câu chuyện 'An toàn dữ liệu > Tiết kiệm chi phí' cho phân khúc Gov/Finance.
- Pricing Recommendation: Rà soát lại bảng giá VKS cho các instance tiêu chuẩn (SME/Mid-market) để đảm bảo cạnh tranh với AWS Local Zone Hà Nội. Cân nhắc gói 'Reserved' hoặc 'Committed Use' sâu hơn để khóa khách hàng.
- Product Action: Ưu tiên phát triển tính năng 'Private Link cho Control Plane' hoặc 'Customer-routed egress' để lấp đầy feature gap so với AWS EKS, đặc biệt cho phân khúc Enterprise.
- Data Action: Kích hoạt scraper để cập nhật bảng giá FPT, Viettel, Bizfly ngay lập tức (dữ liệu hiện tại quá cũ >8 ngày).

## Risks

- Dữ liệu pricing đối thủ (FPT, Viettel, Bizfly) trong workspace đã STALE (cập nhật lần cuối 2026-06-17), không thể dùng để tính toán TCO chính xác cho các scenario hiện tại.
- Thiếu dữ liệu về mức giảm giá cụ thể của AWS (price reductions) và giá Local Zone Hà Nội, không thể định lượng mức chênh lệch TCO.
- Không có thông tin về giá GPU Blackwell (RTX PRO 4500) của AWS, không thể so sánh TCO cho workload AI Inference/Training.

## Gaps / Thiếu dữ liệu

- Cần cập nhật: competitors/2026-06-17_bizfly-bke_profile.md — dữ liệu cũ, chưa dùng được.
- Cần cập nhật: competitors/2026-06-17_fpt-cloud-fke_profile.md — dữ liệu cũ, chưa dùng được.
- Cần cập nhật: competitors/2026-06-17_viettel-voks_profile.md — dữ liệu cũ, chưa dùng được.
- Cần xác minh: Mức giảm giá cụ thể của AWS và giá Local Zone Hà Nội (chưa có số liệu trong evidence).
- Cần xác minh: Roadmap và giá GPU Blackwell của GreenNode để so sánh với AWS EC2 G7.
- Cần xác minh: Khả năng triển khai 'customer-routed control plane egress' của GreenNode VKS (feature gap tiềm năng).
