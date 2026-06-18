# Pricing Summary — 2026-06-18

Source: competitor-monitor run | Model: qwen/qwen3-5-27b

## Key Findings

- [RSS] [AWS News Blog](https://aws.amazon.com/blogs/aws/announcing-amazon-ec2-g7-instances-accelerated-by-nvidia-rtx-pro-4500-blackwell-server-edition-gpus) 2026-06-18 — AWS ra mắt EC2 G7 instances với GPU Blackwell, tập trung vào AI inference. Tác động: Tăng áp lực cạnh tranh về hiệu năng/giá cho workload AI, nhưng chưa có thông tin giá cụ thể để tính TCO so sánh với GreenNode. GreenNode cần theo dõi giá G7 khi công bố để đánh giá lại vị thế AI Inference.
- [RSS] [Vietnam.vn](https://news.google.com/rss/articles/CBMikgFBVV95cUxQV2ExNGdzR1BneXhBNUhxMDNVY3dMZXhlUGlvcWFBYUk2OVZZdFJqTUZuY3NzdWUtWHZvUTJvZW1rZElGSWRzendwNlFfVEdNMjRoVUI2eExHeHQxTUtUWjJnaGxEdHlhSjdmM2UzdDhCVVlzZ3A4YldMcHZ5QmRUS0ZKWmpzWVpZX1hFVGdSd2Y0QQ?oc=5) 2026-06-17 — MSB Bank hợp tác chiến lược với GreenNode để vận hành hàng trăm ứng dụng AI. Tác động: Xác nhận GreenNode là lựa chọn ưu tiên cho Enterprise Banking cần Sovereign AI. Đây là tín hiệu 'willingness-to-pay' cao cho giá trị compliance và an toàn dữ liệu, cho phép GreenNode định vị ở phân khúc giá trị cao hơn (premium) so với đối thủ chỉ cạnh tranh giá.
- [Scrape] Viettel IDC | https://viettelcloud.vn/san-pham/kubernetes | fetched_at=2026-06-18 — Trang sản phẩm Viettel vOKS không hiển thị bảng giá công khai. Tác động: Khó so sánh TCO trực tiếp. GreenNode nên tận dụng sự minh bạch của mình để thu hút SME và các doanh nghiệp cần dự toán chi phí rõ ràng, trong khi Viettel tập trung vào doanh nghiệp lớn qua kênh sales.
- [Scrape] FPT Cloud | https://fptcloud.com/kubernetes | fetched_at=2026-06-18 — FPT FKE không công khai pricing chi tiết trên web. Tác động: Tương tự Viettel, FPT dùng chiến lược sales-led. GreenNode có cơ hội chiếm lĩnh phân khúc SME và Mid-market bằng bảng giá công khai và TCO calculator minh bạch.
- [Scrape] Bizfly Cloud | https://bizflycloud.vn/kubernetes | fetched_at=2026-06-18 — Bizfly BKE có trang sản phẩm nhưng không hiển thị giá cụ thể cho K8s. Tác động: Bizfly vẫn là đối thủ mạnh ở SME nhưng thiếu tính minh bạch về giá. GreenNode có thể dùng 'Free Control Plane' (nếu có) hoặc 'Transparent Pricing' làm đòn bẩy marketing.

## Recommended Actions

- Talk Track cho Sales: Nhấn mạnh 'TCO Minh Bạch' và 'Tuân thủ Luật BVDLCN 2025' khi đối đầu với Viettel/FPT. Đối thủ không công khai giá khiến khách hàng SME khó dự toán, trong khi GreenNode cung cấp bảng giá rõ ràng và cam kết data residency.
- Pricing Recommendation: Xây dựng TCO Calculator công khai cho Scenario S4 (AI Inference) dựa trên giả định giá GPU hiện tại, so sánh với AWS (khi có giá G7) và đối thủ nội địa (ước tính).
- Theo dõi thêm: Cập nhật giá EC2 G7 của AWS ngay khi công bố để đánh giá lại vị thế cạnh tranh cho workload AI.
- Internal Action: Yêu cầu Product/Finance cung cấp bảng giá GPU và egress mới nhất để hoàn thiện TCO model cho AI workloads.

## Risks

- Dữ liệu pricing đối thủ nội địa (Viettel, FPT, Bizfly) không công khai, dẫn đến TCO so sánh dựa trên giả định hoặc dữ liệu cũ.
- AWS vừa ra mắt instance G7 mới cho AI, nếu giá cạnh tranh có thể làm xói mòn lợi thế giá của GreenNode trong phân khúc AI Inference nếu không có GPU onshore.
- Thiếu dữ liệu về chi phí egress và storage của đối thủ nội địa, đây là hidden cost lớn ảnh hưởng đến TCO thực tế.

## Gaps / Thiếu dữ liệu

- Cần cập nhật: pricing/2026-06-17_aws-eks_pricing.md — Dữ liệu AWS cần refresh khi có thông tin giá EC2 G7 mới.
- Thiếu dữ liệu: Giá GPU (H100/A100/Blackwell) của GreenNode và đối thủ nội địa để tính TCO cho Scenario S4 (AI Inference) và S5 (AI Training).
- Thiếu dữ liệu: Chi phí egress và storage của Viettel, FPT, Bizfly để so sánh hidden cost.
- Không fetch được trang social của đối thủ để xác nhận promo hoặc discount ngắn hạn.
