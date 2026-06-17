# Competitor Summary — 2026-06-17

Source: daily-intelligence run | Model: qwen/qwen3-5-27b

## Key Findings

- [RSS] AWS Machine Learning Blog | https://aws.amazon.com/blogs/machine-learning/safeguard-your-agentic-ai-applications-with-the-amazon-bedrock-guardrails-invokeguardrailchecks-api | published_at=2026-06-16 — [RSS] [AWS Machine Learning Blog](https://aws.amazon.com/blogs/machine-learning/safeguard-your-agentic-ai-applications-with-the-amazon-bedrock-guardrails-invokeguardrailchecks-api) 2026-06-16 — AWS ra mắt API InvokeGuardrailChecks cho Amazon Bedrock Guardrails, cho phép áp dụng các biện pháp bảo vệ an toàn (safety checks) linh hoạt tại bất kỳ điểm nào trong ứng dụng AI agent mà không cần tạo tài nguyên guardrail riêng biệt.
- [RSS] AWS Machine Learning Blog | https://aws.amazon.com/blogs/machine-learning/introducing-container-caching-in-amazon-sagemaker-ai-for-faster-model-scaling | published_at=2026-06-16 — [RSS] [AWS Machine Learning Blog](https://aws.amazon.com/blogs/machine-learning/introducing-container-caching-in-amazon-sagemaker-ai-for-faster-model-scaling) 2026-06-16 — AWS giới thiệu container image caching cho Amazon SageMaker AI inference, giảm độ trễ end-to-end lên đến 2x trong các sự kiện scale-out cho mô hình Generative AI.
- [RSS] AWS Machine Learning Blog | https://aws.amazon.com/blogs/machine-learning/parallelize-speculative-decoding-with-p-eagle-on-amazon-sagemaker-ai | published_at=2026-06-16 — [RSS] [AWS Machine Learning Blog](https://aws.amazon.com/blogs/machine-learning/parallelize-speculative-decoding-with-p-eagle-on-amazon-sagemaker-ai) 2026-06-16 — AWS hướng dẫn triển khai P-EAGLE (Parallel Speculative Decoding) trên SageMaker AI để tăng tốc độ suy luận mô hình LLM.
- [RSS] AWS Machine Learning Blog | https://aws.amazon.com/blogs/machine-learning/introducing-gemma-4-models-on-amazon-bedrock | published_at=2026-06-15 — [RSS] [AWS Machine Learning Blog](https://aws.amazon.com/blogs/machine-learning/introducing-gemma-4-models-on-amazon-bedrock) 2026-06-15 — AWS chính thức đưa họ mô hình Gemma 4 (từ Google DeepMind) lên Amazon Bedrock, mở rộng catalog mô hình open-weight cho khách hàng.
- [RSS] FPT Cloud Blog | https://fptcloud.com/fpt-cloud-desktop-3-1-va-backup-veeam-1-5-ra-mat-loat-nang-cap-moi-hoan-thien-trai-nghiem-va-kha-nang-kiem-soat-van-hanh | published_at=2026-06-16 — [RSS] [FPT Cloud Blog](https://fptcloud.com/fpt-cloud-desktop-3-1-va-backup-veeam-1-5-ra-mat-loat-nang-cap-moi-hoan-thien-trai-nghiem-va-kha-nang-kiem-soat-van-hanh) 2026-06-16 — FPT Cloud ra mắt FPT Cloud Desktop 3.1 và Backup Veeam 1.5 với các nâng cấp về trải nghiệm và kiểm soát vận hành.
- [RSS] CNCF Blog | https://www.cncf.io/blog/2026/06/16/from-data-residency-to-digital-sovereignty-architectural-patterns-for-cloud-native-platforms | published_at=2026-06-16 — [RSS] [CNCF Blog](https://www.cncf.io/blog/2026/06/16/from-data-residency-to-digital-sovereignty-architectural-patterns-for-cloud-native-platforms) 2026-06-16 — CNCF công bố bài viết về xu hướng chuyển từ 'Data Residency' sang 'Digital Sovereignty' trong kiến trúc Cloud Native, nhấn mạnh các mô hình kiến trúc để tuân thủ quy định (như EU Data Act).
So-what: Củng cố định hướng 'Sovereign AI Cloud' của GreenNode. Đây là cơ hội để VKS không chỉ bán hạ tầng mà bán 'kiến trúc tuân thủ' cho khối Gov/Enterprise tại VN, đặc biệt trong bối cảnh Luật BVDLCN 2025 đã có hiệu lực.
Hành động: Sử dụng bài viết này làm tài liệu tham khảo (battlecard) để Sales/Pre-sales giải thích lợi thế của VKS về compliance và data residency so với hyperscalers.

## Risks

- {"risk": "Gap về AI-native tooling so với AWS.", "description": "AWS liên tục ra mắt các tính năng tối ưu hóa AI (Guardrails, Container Caching, Speculative Decoding, Model Catalog) trong khi các provider nội địa (bao gồm GreenNode) chủ yếu cung cấp hạ tầng K8s thuần túy. Khách hàng muốn triển khai AI nhanh chóng có thể bị thu hút bởi sự tiện lợi của AWS Bedrock/SageMaker.", "mitigation": "Nhấn mạnh lợi thế về Data Residency (Luật BVDLCN 2025), chi phí egress thấp hơn, và hỗ trợ tiếng Việt. Chuẩn bị các playbook để khách hàng tự deploy các tool AI tối ưu hóa trên VKS nếu cần."}
- {"risk": "Thiếu thông tin về GPU/AI từ đối thủ nội địa.", "description": "Profile của FPT FKE và Viettel vOKS vẫn còn thiếu dữ liệu công khai về GPU node pool và tính năng AI cụ thể. Có thể họ đang phát triển các tính năng tương tự nhưng chưa công bố rộng rãi.", "mitigation": "Tiếp tục theo dõi các kênh social và blog của đối thủ. Nếu có thông tin mới, cập nhật ngay lập tức."}

## Gaps / Thiếu dữ liệu

- Không có thông tin mới về pricing hoặc tính năng K8s từ Viettel vOKS, FPT FKE, và Bizfly BKE trong 24h qua.
- Không có dữ liệu về việc đối thủ nội địa có hỗ trợ các tính năng AI mới của AWS (như P-EAGLE hay Guardrails) hay không.
- Cần xác minh xem FPT Cloud Desktop 3.1 có liên quan gì đến K8s hay không (hiện tại chỉ thấy là DaaS).
