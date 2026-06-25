# Pricing Summary — 2026-06-25

Source: competitor-monitor run | Model: qwen/qwen3-5-27b

## Key Findings

- [RSS] [AWS Containers Blog](https://aws.amazon.com/blogs/containers/faster-nodes-smarter-scaling-whats-new-inside-amazon-elastic-kubernetes-service-amazon-eks-auto-mode) 2026-06-23 — AWS nâng cấp EKS Auto Mode (runtime, compute, storage, networking). Tác động: Tăng áp lực TCO cho GreenNode VKS ở phân khúc doanh nghiệp ưu tiên 'serverless K8s' và tự động hóa vận hành. GreenNode cần rà soát lại chi phí vận hành (OPEX) so với EKS Auto Mode để tránh mất khách hàng do feature gap.
- [RSS] [AWS Containers Blog](https://aws.amazon.com/blogs/containers/amazon-eks-now-supports-control-plane-egress-through-your-vpc) 2026-06-22 — AWS cho phép định tuyến control plane egress qua VPC khách hàng. Tác động: Đây là tính năng bắt buộc cho các khách hàng ngân hàng/chính phủ (Sovereign AI). Nếu GreenNode VKS chưa có tính năng tương đương, sẽ mất cơ hội deal lớn bất kể giá rẻ hơn. Cần xác minh ngay khả năng 'Private Control Plane' của VKS.
- [RSS] [AWS News Blog](https://aws.amazon.com/blogs/aws/announcing-amazon-ec2-g7-instances-accelerated-by-nvidia-rtx-pro-4500-blackwell-server-edition-gpus) 2026-06-18 — AWS ra mắt GPU Blackwell (RTX PRO 4500) cho AI Inference. Tác động: Tạo áp lực cạnh tranh về hiệu năng/giá cho workload AI. Nếu GreenNode chưa có GPU thế hệ mới, sẽ khó cạnh tranh ở phân khúc AI Training/Inference cao cấp, buộc phải tập trung vào lợi thế 'onshore VN' và latency thấp.
- [Scrape] Viettel IDC | https://viettelcloud.vn/san-pham/kubernetes | fetched_at=2026-06-25 — Trang sản phẩm VOKS không hiển thị bảng giá công khai (list price). Tác động: Viettel IDC tiếp tục chiến lược 'sales-led pricing' (giá theo thỏa thuận). GreenNode không thể so sánh trực tiếp list price, cần tập trung vào TCO tổng thể và các gói cam kết (reserved) nếu có.
- [Scrape] FPT Cloud | https://fptcloud.com/kubernetes | fetched_at=2026-06-25 — Trang sản phẩm FKE không hiển thị bảng giá công khai. Tác động: Tương tự Viettel, FPT Cloud không công bố giá. Cạnh tranh sẽ diễn ra ở mức độ deal-to-deal. GreenNode cần chuẩn bị battlecard TCO dựa trên giả định discount 20-40% cho enterprise.
- [Scrape] Bizfly Cloud | https://bizflycloud.vn/kubernetes | fetched_at=2026-06-25 — Trang sản phẩm BKE không hiển thị bảng giá công khai. Tác động: Không có dữ liệu pricing để so sánh. Cần thu thập thêm thông tin từ các case study hoặc RFP gần đây để ước tính giá.

## Recommended Actions

- Talk Track cho Sales: Nhấn mạnh lợi thế 'Sovereign AI' và 'Onshore Latency' của GreenNode VKS thay vì cạnh tranh trực tiếp về list price với AWS. Sử dụng tính năng 'Private Control Plane' (nếu có) hoặc cam kết triển khai nhanh để bù đắp cho việc thiếu tính năng 'Control Plane Egress' của AWS.
- Pricing Recommendation: Không điều chỉnh list price công khai (vì đối thủ không công bố). Tập trung vào việc xây dựng các gói 'Reserved Instances' hoặc 'Committed Use' với discount 20-40% cho các deal Enterprise lớn để cạnh tranh với chiến lược sales-led của đối thủ.
- Theo dõi thêm: Cập nhật ngay dữ liệu pricing của đối thủ (Viettel, FPT, Bizfly) và AWS (đặc biệt là GPU Blackwell) để có thể tính toán TCO chính xác cho các scenario AI Inference/Training.
- Theo dõi thêm: Xác minh khả năng 'Control Plane Egress' của GreenNode VKS. Nếu chưa có, cần lên kế hoạch phát triển hoặc đưa ra giải pháp thay thế (workaround) để đáp ứng yêu cầu bảo mật của khách hàng.

## Risks

- Dữ liệu pricing đối thủ (Viettel, FPT, Bizfly) trong workspace đã quá hạn (>30 ngày) và được đánh dấu STALE. Không thể so sánh TCO chính xác mà không có dữ liệu mới.
- Không có thông tin về giá GPU Blackwell của AWS hoặc các đối thủ nội địa, gây khó khăn cho việc định giá workload AI Inference/Training.
- Chiến lược 'sales-led pricing' của đối thủ nội địa khiến việc so sánh list price trở nên vô nghĩa; cần tập trung vào TCO và giá trị gia tăng (compliance, latency).
- Tính năng 'Control Plane Egress' của AWS có thể là yêu cầu bắt buộc (must-have) cho các deal ngân hàng/chính phủ, tạo rủi ro mất khách nếu GreenNode chưa có tính năng tương đương.

## Gaps / Thiếu dữ liệu

- Cần cập nhật: competitors/2026-06-17_viettel-idc-kubernetes_profile.md — dữ liệu cũ, chưa dùng được.
- Cần cập nhật: competitors/2026-06-17_bizfly-bke_profile.md — dữ liệu cũ, chưa dùng được.
- Cần cập nhật: competitors/2026-06-17_fpt-cloud-fke_profile.md — dữ liệu cũ, chưa dùng được.
- Cần cập nhật: competitors/2026-06-17_aws-eks_profile.md — dữ liệu cũ, chưa dùng được.
- Thiếu dữ liệu pricing công khai cho GreenNode VKS (list price, reserved discount, egress fee) để tính toán TCO cho các scenario S1-S5.
- Thiếu thông tin về giá GPU Blackwell (RTX PRO 4500) của AWS và các đối thủ nội địa để phân tích cạnh tranh cho workload AI.
- Thiếu thông tin về tính năng 'Control Plane Egress' của GreenNode VKS để đánh giá khả năng đáp ứng yêu cầu bảo mật của khách hàng Enterprise/Gov.
