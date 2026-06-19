# Pricing Summary — 2026-06-19

Source: weekly-digest run | Model: qwen/qwen3-5-27b

## Key Findings

- [RSS] [AWS News Blog](https://aws.amazon.com/blogs/aws/announcing-amazon-ec2-g7-instances-accelerated-by-nvidia-rtx-pro-4500-blackwell-server-edition-gpus) 2026-06-18 — AWS ra mắt EC2 G7 instances với GPU NVIDIA RTX PRO 4500 Blackwell Server Edition. Tác động: Tăng áp lực cạnh tranh về hiệu năng/giá cho workload AI inference. GreenNode chưa có thông tin pricing công khai cho GPU tương đương, gây rủi ro thua thế trong các RFP yêu cầu hiệu năng cao cấp nếu không có chiến lược giá linh hoạt. GreenNode nên: Theo dõi sát giá G7 khi công bố để cập nhật TCO S4 (AI Inference) và chuẩn bị talk track về 'Total Cost of Ownership' (bao gồm egress, latency) thay vì chỉ so sánh giá instance.
- [Workspace] [pricing/2026-06-17_aws-eks_pricing.md] 2026-06-17 — AWS EKS thu phí Control Plane $0.10/giờ (~73 USD/tháng). Tác động: Tạo cơ hội cho GreenNode VKS định vị 'Control Plane miễn phí' hoặc 'tối ưu hơn' cho các cluster nhỏ/SME. GreenNode nên: Nhấn mạnh điểm này trong battlecard cho phân khúc SME (S1, S2) để giảm rào cản gia nhập (adoption barrier).
- [RSS] [Vietnam.vn](https://news.google.com/rss/articles/CBMikgFBVV95cUxQV2ExNGdzR1BneXhBNUhxMDNVY3dMZXhlUGlvcWFBYUk2OVZZdFJqTUZuY3NzdWUtWHZvUTJvZW1rZElGSWRzendwNlFfVEdNMjRoVUI2eExHeHQxTUtUWjJnaGxEdHlhSjdmM2UzdDhCVVlzZ3A4YldMcHZ5QmRUS0ZKWmpzWVpZX1hFVGdSd2Y0QQ?oc=5) 2026-06-17 — MSB Bank hợp tác chiến lược với GreenNode để triển khai hàng trăm ứng dụng AI. Tác động: Xác nhận tín hiệu 'willingness-to-pay' cao cho giải pháp Sovereign AI tại VN, bất chấp giá có thể cao hơn hyperscaler. GreenNode nên: Sử dụng case study MSB để định giá premium cho phân khúc Enterprise (S3) và Gov, tập trung vào giá trị 'compliance' và 'data residency' thay vì cạnh tranh giá thấp.
- [RSS] [AWS News Blog](https://aws.amazon.com/blogs/machine-learning/introducing-container-caching-in-amazon-sagemaker-ai-for-faster-model-scaling) 2026-06-16 — AWS ra mắt container image caching cho SageMaker AI, giảm latency scale-out lên đến 2 lần. Tác động: AWS tối ưu hóa chi phí vận hành AI inference (giảm thời gian chờ, tăng hiệu suất). GreenNode nên: Đánh giá lại khả năng tối ưu hóa scaling của VKS/AgentBase để đảm bảo không bị tụt hậu về hiệu năng/giá trong các workload AI burst.

## Recommended Actions

- Talk Track cho Sales (SME/S1-S2): Nhấn mạnh 'Control Plane miễn phí' của GreenNode VKS so với AWS EKS ($73/tháng), giúp giảm chi phí khởi điểm cho các cluster nhỏ. Ví dụ: 'Với GreenNode VKS, bạn không phải trả phí quản lý cluster, chỉ trả cho tài nguyên thực tế sử dụng, giúp tiết kiệm ngay từ đầu.'
- Talk Track cho Sales (Enterprise/S3-S5): Tập trung vào 'Sovereign AI' và 'Data Residency' thay vì giá thấp. Sử dụng case study MSB Bank để chứng minh khả năng triển khai quy mô lớn và tuân thủ pháp lý. Ví dụ: 'GreenNode là lựa chọn duy nhất tại VN đảm bảo dữ liệu AI nằm hoàn toàn trong nước, tuân thủ Luật BVDLCN 2025, như MSB Bank đã chứng minh.'
- Pricing Recommendation: Theo dõi sát giá AWS EC2 G7 khi công bố. Nếu giá G7 cao hơn đáng kể so với GPU hiện tại của GreenNode, hãy nhấn mạnh 'Cost-Performance Ratio' và 'Local Support'. Nếu giá G7 cạnh tranh, cần xem xét chiến lược giá linh hoạt (discount, reserved instances) cho workload AI.
- Action: Cập nhật TCO Calculator cho scenario S4 (AI Inference) và S5 (AI Training) khi có dữ liệu pricing GPU mới. Bao gồm cả hidden cost (egress, storage, networking) để so sánh toàn diện với AWS.

## Risks

- Dữ liệu pricing GPU của AWS (G7) chưa có, không thể tính TCO chính xác cho scenario AI Inference (S4) và AI Training (S5).
- Pricing của đối thủ nội địa (Viettel, FPT, Bizfly) vẫn là 'contact-only', khó so sánh trực tiếp bảng giá công khai.
- Dữ liệu pricing AWS EKS Control Plane ($0.10/giờ) có thể thay đổi theo region (ap-southeast-1 +10-15% so với us-east-1).
- Thiếu dữ liệu về hidden cost (egress, LB, NAT) của đối thủ nội địa để tính TCO toàn diện.

## Gaps / Thiếu dữ liệu

- Cần cập nhật: pricing/2026-06-17_aws-eks_pricing.md — Dữ liệu pricing AWS EKS cần refresh (next refresh: 2026-06-24).
- Thiếu dữ liệu: Giá công khai cho GPU NVIDIA Blackwell (RTX PRO 4500) trên AWS EC2 G7 và các đối thủ nội địa.
- Thiếu dữ liệu: Pricing chi tiết cho FPT FKE, Viettel VKS/vOKS, Bizfly BKE (chỉ có thông tin contact-only).
- Thiếu dữ liệu: Hidden cost (egress, LB, NAT) của các đối thủ nội địa để tính TCO so sánh.
