# Competitor Summary — 2026-06-19

Source: daily-intelligence run | Model: qwen/qwen3-5-27b

## Key Findings

- [RSS] AWS News Blog | https://aws.amazon.com/blogs/aws/announcing-amazon-ec2-g7-instances-accelerated-by-nvidia-rtx-pro-4500-blackwell-server-edition-gpus | published_at=2026-06-18 — [RSS] [AWS News Blog](https://aws.amazon.com/blogs/aws/announcing-amazon-ec2-g7-instances-accelerated-by-nvidia-rtx-pro-4500-blackwell-server-edition-gpus) 2026-06-18 — AWS công bố GA EC2 G7 instances với GPU NVIDIA RTX PRO 4500 Blackwell Server Edition cho AI inference và graphics.
**Tác động:** ❌ Feature gap về phần cứng GPU thế hệ mới (Blackwell). AWS cung cấp ngay lập tức lợi thế hiệu năng cho LLM inference nặng. GreenNode đang thua nếu khách hàng cần performance tối đa và không bị ràng buộc bởi data residency VN.
**Hành động:** Rà soát roadmap GPU (A100/H100/Blackwell) và thời gian ra mắt tại VN; chuẩn bị kịch bản TCO so sánh cho khách hàng Enterprise cần inference nặng.
- [RSS] AWS News Blog | https://aws.amazon.com/blogs/aws/introducing-amazon-bedrock-managed-knowledge-base-for-faster-more-accurate-enterprise-ai-applications | published_at=2026-06-17 — [RSS] [AWS News Blog](https://aws.amazon.com/blogs/aws/introducing-amazon-bedrock-managed-knowledge-base-for-faster-more-accurate-enterprise-ai-applications) 2026-06-17 — AWS ra mắt Amazon Bedrock Managed Knowledge Base và Web Search trên AgentCore, cho phép xây dựng RAG pipeline doanh nghiệp với data connector tự động và truy cập web an toàn (zero egress).
**Tác động:** ❌ GreenNode đang thua về AI Agent infrastructure. AWS cung cấp giải pháp 'end-to-end' cho RAG và Agent mà VKS chưa có. Khách hàng Enterprise muốn triển khai AI nhanh có thể chọn AWS nếu không cần data residency VN.
**Hành động:** Đánh giá khả năng tích hợp các công cụ RAG/Agent managed hoặc xây dựng giải pháp tương tự trên VKS; nhấn mạnh lợi thế 'data residency VN' và 'zero egress' trong môi trường nội địa.
- [RSS] Vietnam.vn | https://news.google.com/rss/articles/CBMikgFBVV95cUxQV2ExNGdzR1BneXhBNUhxMDNVY3dMZXhlUGlvcWFBYUk2OVZZdFJqTUZuY3NzdWUtWHZvUTJvZW1rZElGSWRzendwNlFfVEdNMjRoVUI2eExHeHQxTUtUWjJnaGxEdHlhSjdmM2UzdDhCVVlzZ3A4YldMcHZ5QmRUS0ZKWmpzWVpZX1hFVGdSd2Y0QQ?oc=5 | published_at=2026-06-17 — [RSS] [Vietnam.vn](https://news.google.com/rss/articles/CBMikgFBVV95cUxQV2ExNGdzR1BneXhBNUhxMDNVY3dMZXhlUGlvcWFBYUk2OVZZdFJqTUZuY3NzdWUtWHZvUTJvZW1rZElGSWRzendwNlFfVEdNMjRoVUI2eExHeHQxTUtUWjJnaGxEdHlhSjdmM2UzdDhCVVlzZ3A4YldMcHZ5QmRUS0ZKWmpzWVpZX1hFVGdSd2Y0QQ?oc=5) 2026-06-17 — MSB Bank hợp tác chiến lược với GreenNode để vận hành hàng trăm ứng dụng AI, thúc đẩy chuyển đổi từ digital banking sang AI banking.
**Tác động:** ✅ Cơ hội lớn về brand trust và proof point cho phân khúc Fintech/Banking. Đây là bằng chứng thực tế cho khả năng vận hành AI quy mô lớn của GreenNode tại VN.
**Hành động:** Sử dụng case study MSB trong battlecard và tài liệu marketing; tiếp cận các ngân hàng khác với thông điệp 'AI Banking Sovereign'.
- [RSS] AWS News Blog | https://aws.amazon.com/blogs/aws/amazon-ecs-introduces-new-high-resolution-metrics-for-faster-service-auto-scaling | published_at=2026-06-18 — [RSS] [AWS News Blog](https://aws.amazon.com/blogs/aws/amazon-ecs-introduces-new-high-resolution-metrics-for-faster-service-auto-scaling) 2026-06-18 — Amazon ECS giới thiệu high-resolution metrics để tăng tốc độ auto-scaling dịch vụ.
**Tác động:** ⚠️ Tương đương. AWS cải thiện khả năng scaling cho container. GreenNode VKS cần đảm bảo các tính năng autoscaling (HPA/VPA/Karpenter) có độ trễ thấp và hiệu quả tương đương.
**Hành động:** Kiểm tra lại hiệu năng autoscaling của VKS; nếu có gap, ưu tiên cải thiện trong roadmap kỹ thuật.

## Risks

- ❌ Feature gap về GPU Blackwell (AWS) và AI Agent infrastructure (Bedrock) có thể làm mất khách hàng Enterprise không bị ràng buộc bởi data residency VN.
- ❌ Đối thủ Tier 1 nội địa (Viettel, FPT, Bizfly) không có động thái mới trong 24h, nhưng vẫn là mối đe dọa tiềm tàng về giá và quan hệ chính phủ.

## Gaps / Thiếu dữ liệu

- Cần cập nhật: pricing/2026-06-17_aws-eks_pricing.md — Dữ liệu pricing AWS cần được làm mới để phản ánh chính xác chi phí cho EC2 G7 mới.
- Cần xác minh: Không có thông tin mới về pricing hoặc feature update từ Viettel vOKS, FPT FKE, Bizfly BKE trong 24h qua. Cần theo dõi thêm trong tuần tới.
