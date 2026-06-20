# Pricing Summary — 2026-06-20

Source: competitor-monitor run | Model: qwen/qwen3-5-27b

## Key Findings

- [RSS] [AWS News Blog](https://aws.amazon.com/blogs/aws/announcing-amazon-ec2-g7-instances-accelerated-by-nvidia-rtx-pro-4500-blackwell-server-edition-gpus) 2026-06-18 — AWS công bố GA EC2 G7 instances với GPU NVIDIA RTX PRO 4500 Blackwell. Tác động: ❌ Feature gap về phần cứng AI inference. AWS cung cấp lợi thế hiệu năng/giá ngay lập tức cho LLM inference nặng. GreenNode đang thua nếu khách hàng cần performance tối đa cho training/inference mà không có ràng buộc data residency VN. GreenNode cần rà soát roadmap GPU (A100/H100/Blackwell) để tránh mất khách hàng cần performance tối đa.
- [RSS] [AWS News Blog](https://aws.amazon.com/blogs/machine-learning/introducing-web-search-on-amazon-bedrock-agentcore) 2026-06-19 — AWS công bố GA tính năng Web Search trên Amazon Bedrock AgentCore, cho phép các AI Agent truy cập web an toàn và tích hợp dữ liệu thời gian thực mà không cần egress phức tạp. Tác động: ❌ Feature gap về AI Agent infrastructure. AWS cung cấp giải pháp 'end-to-end' cho RAG và Agent có khả năng truy cập web, trong khi VKS hiện tại tập trung vào K8s infrastructure thuần. Rủi ro churn cho khách hàng Enterprise muốn triển khai AI nhanh nếu không cần data residency VN.
- [Scrape] Viettel Cloud | https://viettelcloud.vn/san-pham/kubernetes | fetched_at=2026-06-20 — Trang sản phẩm vOKS không hiển thị bảng giá công khai (pricing contact-only). Tác động: ⚠️ Không thể tính toán TCO so sánh trực tiếp với VKS. Viettel có thể đang dùng chiến lược pricing linh hoạt theo deal (enterprise sales-led) để cạnh tranh trực tiếp với GreenNode trong các dự án lớn.
- [Scrape] FPT Cloud | https://fptcloud.com/kubernetes | fetched_at=2026-06-20 — Trang sản phẩm FKE không hiển thị bảng giá công khai. Tác động: ⚠️ Không thể xác định pricing delta. FPT có thể đang cạnh tranh bằng gói dedicated (D-FKE) hoặc bundling với các dịch vụ khác, gây khó khăn cho việc so sánh TCO chuẩn.
- [Scrape] Bizfly Cloud | https://bizflycloud.vn/kubernetes | fetched_at=2026-06-20 — Trang sản phẩm BKE không hiển thị bảng giá công khai chi tiết. Tác động: ⚠️ Không thể xác định pricing delta. Bizfly đã xác nhận có GPU node pool (từ memory), nhưng thiếu giá để đánh giá tính cạnh tranh cho workload AI.

## Recommended Actions

- Talk track cho Sales: Nhấn mạnh lợi thế data residency VN, billing VND, và support tiếng Việt của GreenNode VKS so với AWS. Đối với khách hàng cần GPU Blackwell, đề xuất giải pháp hybrid hoặc roadmap GPU của GreenNode (nếu có).
- Pricing recommendation: Đề xuất gói Reserved/Committed Discount cho VKS để cạnh tranh với AWS EKS Reserved Instances (nếu có).
- Action: Cập nhật pricing snapshot của đối thủ nội địa (Viettel, FPT, Bizfly) bằng cách liên hệ sales hoặc tìm kiếm quote mẫu.
- Action: Rà soát roadmap GPU của GreenNode và chuẩn bị thông tin về hiệu năng/giá để đối phó với AWS G7.
- Action: Xây dựng TCO scenario cho workload AI inference (S4) và AI training (S5) với giả định về giá GPU của GreenNode và AWS G7.

## Risks

- Dữ liệu pricing của đối thủ nội địa (Viettel, FPT, Bizfly) không công khai, gây khó khăn cho việc tính toán TCO chính xác và xây dựng battlecard.
- AWS ra mắt GPU Blackwell (G7) tạo áp lực về hiệu năng/giá cho workload AI inference nặng, trong khi GreenNode chưa có thông tin về roadmap GPU tương đương.
- AWS Bedrock AgentCore Web Search tạo feature gap cho các giải pháp RAG/Agent, có thể khiến khách hàng Enterprise chuyển sang AWS nếu không cần data residency VN.
- Dữ liệu pricing AWS EKS (2026-06-17) đã cũ hơn 3 ngày, cần cập nhật nếu có thay đổi về giá hoặc region pricing.

## Gaps / Thiếu dữ liệu

- Cần cập nhật: pricing/2026-06-17_aws-eks_pricing.md — dữ liệu cũ, cần refresh để đảm bảo tính chính xác.
- Cần thu thập: Bảng giá công khai hoặc quote mẫu của Viettel vOKS, FPT FKE, Bizfly BKE để tính toán TCO so sánh.
- Cần xác minh: Roadmap GPU của GreenNode (A100/H100/Blackwell) và thời gian ra mắt để đối phó với AWS G7.
- Cần xác minh: Pricing của AWS EC2 G7 instances (GPU Blackwell) để đánh giá tác động đến TCO AI inference.
