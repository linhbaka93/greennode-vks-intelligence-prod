# Pricing Summary — 2026-06-20

Source: competitor-monitor run | Model: qwen/qwen3-5-27b

## Key Findings

- [RSS] [AWS News Blog](https://aws.amazon.com/blogs/aws/announcing-amazon-ec2-g7-instances-accelerated-by-nvidia-rtx-pro-4500-blackwell-server-edition-gpus) 2026-06-18 — AWS ra mắt EC2 G7 instances với GPU NVIDIA RTX PRO 4500 Blackwell Server Edition cho AI inference. Tác động: Tăng áp lực cạnh tranh về hiệu năng/giá cho workload AI (S4). GreenNode chưa có thông tin pricing công khai cho GPU tương đương, gây rủi ro thua thế trong các RFP yêu cầu hiệu năng cao cấp nếu không có chiến lược giá linh hoạt. GreenNode nên: Theo dõi sát giá G7 khi công bố để cập nhật TCO S4 và chuẩn bị talk track về 'Total Cost of Ownership' (bao gồm egress, latency, và data residency).
- [Scrape] Viettel IDC | https://viettelcloud.vn/san-pham/kubernetes | fetched_at=2026-06-20 — Trang sản phẩm VKS/vOKS không hiển thị bảng giá công khai, chỉ có nút 'Liên hệ'. Tác động: Khó so sánh TCO trực tiếp với GreenNode VKS trong các deal SME/Mid-market. GreenNode nên: Tận dụng lợi thế pricing transparent (nếu có) để tạo ưu thế trong RFP, hoặc chuẩn bị bảng giá nội bộ để đối chiếu khi khách yêu cầu.
- [Scrape] FPT Cloud | https://fptcloud.com/kubernetes | fetched_at=2026-06-20 — Trang FKE không hiển thị bảng giá, yêu cầu liên hệ sales. Tác động: FPT Cloud tiếp tục chiến lược 'contact-only' cho Enterprise, làm giảm khả năng so sánh giá tự động. GreenNode nên: Nhấn mạnh tính minh bạch và khả năng dự báo chi phí (TCO calculator) trong tài liệu bán hàng.
- [Scrape] Bizfly Cloud | https://bizflycloud.vn/kubernetes | fetched_at=2026-06-20 — Trang BKE không hiển thị bảng giá công khai. Tác động: Bizfly Cloud duy trì mô hình giá kín, phù hợp với phân khúc SME nhưng khó so sánh nhanh. GreenNode nên: Theo dõi các chương trình khuyến mãi hoặc gói giá cố định (nếu có) qua kênh social/blog để cập nhật TCO.
- [Workspace] pricing/2026-06-17_aws-eks_pricing.md — AWS EKS control plane $0.10/giờ (tính đến 2026-06-17). Tác động: GreenNode VKS control plane miễn phí (theo memory cũ) vẫn là lợi thế lớn cho SME và các cluster nhỏ. GreenNode nên: Duy trì và quảng bá chính sách control plane miễn phí như một điểm khác biệt so với AWS EKS.

## Recommended Actions

- Theo dõi sát giá EC2 G7 của AWS khi công bố để cập nhật TCO S4 (AI Inference) và chuẩn bị talk track về 'Total Cost of Ownership' (bao gồm egress, latency, và data residency).
- Xác minh lại chính sách pricing GreenNode VKS (đặc biệt là control plane miễn phí và giá GPU) để đảm bảo dữ liệu chính xác cho các RFP.
- Tận dụng lợi thế pricing transparent (nếu có) để tạo ưu thế trong các deal SME/Mid-market so với đối thủ nội địa có mô hình 'contact-only'.
- Chuẩn bị bảng giá nội bộ và TCO calculator để đối chiếu khi khách hàng yêu cầu so sánh với Viettel, FPT, Bizfly.
- Theo dõi các chương trình khuyến mãi hoặc gói giá cố định từ đối thủ nội địa qua kênh social/blog để cập nhật TCO.

## Risks

- Dữ liệu pricing từ đối thủ nội địa (Viettel, FPT, Bizfly) không công khai, gây khó khăn cho việc so sánh TCO trực tiếp.
- AWS EC2 G7 chưa công bố giá, tạo khoảng trống thông tin cho việc đánh giá cạnh tranh trong phân khúc AI Inference.
- Dữ liệu pricing GreenNode VKS từ memory có thể đã cũ (tính đến 2026-05-20), cần xác minh lại chính sách control plane miễn phí và giá GPU.

## Gaps / Thiếu dữ liệu

- Cần cập nhật: pricing/2026-06-17_aws-eks_pricing.md — dữ liệu cũ, chưa có giá EC2 G7 mới.
- Cần cập nhật: greennode/2026-05-20_greennode-vks_product-overview.md — dữ liệu cũ, chưa xác minh lại chính sách pricing VKS.
- Không fetch được bảng giá công khai từ trang Viettel Cloud, FPT Cloud, Bizfly Cloud — cần liên hệ sales hoặc theo dõi kênh social/blog để cập nhật.
- Thiếu dữ liệu pricing GPU cho GreenNode VKS để so sánh với AWS EC2 G7.
