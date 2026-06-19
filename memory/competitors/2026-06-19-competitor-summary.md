# Competitor Summary — 2026-06-19

Source: competitor-monitor run | Model: qwen/qwen3-5-27b

## Key Findings

- [RSS] [AWS News Blog](https://aws.amazon.com/blogs/aws/announcing-amazon-ec2-g7-instances-accelerated-by-nvidia-rtx-pro-4500-blackwell-server-edition-gpus) 2026-06-18 — AWS công bố GA EC2 G7 instances với GPU NVIDIA RTX PRO 4500 Blackwell Server Edition cho AI inference và graphics. — Tác động tới GreenNode: ❌ Feature gap về phần cứng GPU thế hệ mới. AWS cung cấp lợi thế hiệu năng ngay lập tức cho LLM inference nặng. GreenNode đang thua nếu khách hàng cần performance tối đa cho training/inference mà không có ràng buộc data residency VN.
- [RSS] [AWS News Blog](https://aws.amazon.com/blogs/aws/introducing-amazon-bedrock-managed-knowledge-base-for-faster-more-accurate-enterprise-ai-applications) 2026-06-17 — AWS ra mắt Web Search và Managed Knowledge Base trên Amazon Bedrock AgentCore, cho phép xây dựng RAG pipeline doanh nghiệp với data connector tự động và truy cập web an toàn (zero egress). — Tác động tới GreenNode: ❌ GreenNode đang thua về AI Agent infrastructure. AWS cung cấp giải pháp 'end-to-end' cho RAG và Agent mà VKS chưa có. Khách hàng Enterprise muốn triển khai AI nhanh có thể chọn AWS nếu không cần data residency VN.
- [RSS] [AWS News Blog](https://aws.amazon.com/blogs/machine-learning/introducing-container-caching-in-amazon-sagemaker-ai-for-faster-model-scaling) 2026-06-16 — AWS giới thiệu container image caching cho SageMaker AI, giúp giảm latency khi scale-out model Generative AI lên đến 2 lần. — Tác động tới GreenNode: ❌ Rủi ro về hiệu năng và chi phí vận hành cho workload GenAI. AWS tối ưu hóa quy trình scale-out tự động, trong khi GreenNode cần đảm bảo VKS có các tính năng autoscaling tương đương (Karpenter/KEDA) để cạnh tranh.
- [RSS] [Vietnam.vn](https://news.google.com/rss/articles/CBMivwFBVV95cUxNaXJWdV81LVFQNTJ3RURHcVdybFZ1bnZPMlJfc29NdTVSVlBQTXNfOTJONURNV3gxTTd4d3F6dlVuMFh0d1R6cVU5eFNWNXZ2QTg4cEQyYVFFVWZTdkp3U3BxbU1hbk5TajhWSGs3dURkT1hYTzJCYlI2eGVMaXFpMVBhSnZ1WGZfejh1ZWliQ0RYWU9PcnpFbGhvWTRzc2pSR0hNbU1uSTVEZmNVa0hPaUtaUHo2al95ejNBc2pPNA) 2026-06-17 — MSB Bank và GreenNode mở rộng hợp tác chiến lược, thúc đẩy chuyển đổi từ digital banking sang AI banking. — Tác động tới GreenNode: ✅ Cơ hội lớn về brand trust và proof point. Hợp đồng với MSB Bank là bằng chứng thực tế cho khả năng vận hành hàng trăm ứng dụng AI của GreenNode, củng cố vị thế Sovereign AI Cloud.
- [RSS] [FPT Cloud Blog](https://fptcloud.com/fpt-cloud-desktop-3-1-va-backup-veeam-1-5-ra-mat-loat-nang-cap-moi-hoan-thien-trai-nghiem-va-kha-nang-kiem-soat-van-hanh) 2026-06-16 — FPT Cloud ra mắt FPT Cloud Desktop 3.1 và FPT Backup Veeam 1.5 với các nâng cấp về trải nghiệm và kiểm soát vận hành. — Tác động tới GreenNode: ⚠️ FPT tập trung vào các dịch vụ desktop và backup, chưa có động thái trực tiếp về K8s/AI trong 24h qua. Tuy nhiên, việc cải thiện trải nghiệm vận hành cho thấy FPT đang củng cố nền tảng cho Enterprise.

## Risks

- Feature gap về GPU Blackwell và AI Agent infrastructure so với AWS có thể dẫn đến mất khách hàng Enterprise cần performance tối đa cho AI/ML nếu không có ràng buộc data residency.
- Áp lực cạnh tranh từ AWS về các tính năng tối ưu hóa GenAI (container caching, speculative decoding) có thể làm tăng chi phí vận hành và giảm hiệu năng của GreenNode VKS nếu không cập nhật kịp thời.

## Gaps / Thiếu dữ liệu

- Cần cập nhật: competitors/2026-06-17_viettel-voks_profile.md — Dữ liệu pricing và SLA của Viettel vOKS chưa xác minh, cần scrape lại trang sản phẩm hoặc tìm nguồn mới.
- Cần cập nhật: competitors/2026-06-17_fpt-cloud-fke_profile.md — Chưa xác minh được thông tin về GPU node pool trên FPT FKE, cần kiểm tra lại trang sản phẩm hoặc tài liệu kỹ thuật.
- Không fetch được trang social của đối thủ (Viettel, FPT, Bizfly) trong 24h qua do giới hạn của crawler, cần xác minh thủ công nếu có tin tức quan trọng.
