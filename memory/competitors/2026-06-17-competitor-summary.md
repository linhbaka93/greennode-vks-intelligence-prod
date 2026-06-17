# Competitor Summary — 2026-06-17

Source: daily-intelligence run | Model: qwen/qwen3-5-27b

## Key Findings

- [RSS] [AWS Blog](https://aws.amazon.com/blogs/machine-learning/introducing-container-caching-in-amazon-sagemaker-ai-for-faster-model-scaling) 2026-06-16 — AWS ra mắt container image caching cho SageMaker AI, giảm latency scale-out Generative AI lên đến 2x. — Tác động tới GreenNode: ❌ GreenNode đang thua về AI-native infrastructure. AWS cung cấp tối ưu hóa hạ tầng K8s cho AI (scale-out speed) mà local providers chưa công bố. Khách hàng Enterprise chạy GenAI có thể bị thu hút bởi hiệu năng này nếu không bị ràng buộc bởi data residency.
- [RSS] [AWS Blog](https://aws.amazon.com/blogs/machine-learning/parallelize-speculative-decoding-with-p-eagle-on-amazon-sagemaker-ai) 2026-06-16 — AWS hỗ trợ P-EAGLE (parallel speculative decoding) trên SageMaker để tăng tốc inference LLM. — Tác động tới GreenNode: ❌ Feature gap trong AI/ML. AWS đang dẫn đầu về các kỹ thuật tối ưu inference LLM trên K8s. GreenNode VKS chưa có thông báo tương tự, tạo rủi ro mất khách hàng trong phân khúc AI-heavy.
- [RSS] [AWS Blog](https://aws.amazon.com/blogs/machine-learning/safeguard-your-agentic-ai-applications-with-the-amazon-bedrock-guardrails-invokeguardrailchecks-api) 2026-06-16 — AWS ra mắt InvokeGuardrailChecks API để áp dụng bảo mật AI (safety checks) linh hoạt trong ứng dụng Agentic AI. — Tác động tới GreenNode: ⚠️ Tương đương/Thiếu dữ liệu. AWS mở rộng khả năng bảo mật AI (Guardrails) cho các ứng dụng tự động (agents). GreenNode cần xác định xem VKS có tích hợp sẵn các công cụ bảo mật AI tương tự hay không để đáp ứng nhu cầu Enterprise về AI safety.
- [RSS] [AWS Blog](https://aws.amazon.com/blogs/machine-learning/introducing-gemma-4-models-on-amazon-bedrock) 2026-06-15 — AWS đưa mô hình Gemma 4 (Google DeepMind) lên Bedrock, mở rộng catalog open-weight models. — Tác động tới GreenNode: ⚠️ Tương đương. AWS mở rộng khả năng truy cập mô hình AI đa dạng. GreenNode VKS cần đảm bảo khả năng deploy các mô hình open-weight (như Gemma, Llama) dễ dàng trên K8s để cạnh tranh về sự linh hoạt.
- [RSS] [FPT Cloud Blog](https://fptcloud.com/fpt-cloud-desktop-3-1-va-backup-veeam-1-5-ra-mat-loat-nang-cap-moi-hoan-thien-trai-nghiem-va-kha-nang-kiem-soat-van-hanh) 2026-06-16 — FPT Cloud ra mắt Desktop 3.1 và Backup Veeam 1.5. — Tác động tới GreenNode: ✅ Không tác động trực tiếp. Động thái này tập trung vào DaaS và Backup, không liên quan đến FPT Kubernetes Engine (FKE). Không có tín hiệu thay đổi về pricing hay feature K8s.
- [RSS] [CNCF Blog](https://www.cncf.io/blog/2026/06/16/from-data-residency-to-digital-sovereignty-architectural-patterns-for-cloud-native-platforms) 2026-06-16 — Xu hướng 'Digital Sovereignty' chuyển từ chính sách sang thực thi kỹ thuật (Platform Engineering), chịu ảnh hưởng từ EU Data Act. — Tác động tới GreenNode: ✅ Cơ hội lớn. Xu hướng này củng cố định vị 'Sovereign AI Cloud' của GreenNode. Khách hàng Gov/Enterprise cần kiến trúc tuân thủ (compliance-by-design) hơn là chỉ hạ tầng thuần túy.

## Gaps / Thiếu dữ liệu

- Không có thông tin mới về Viettel vOKS, Bizfly BKE trong 24h qua. Cần tiếp tục giám sát các kênh social và blog của họ để phát hiện sớm các động thái về GPU hoặc pricing.
- Thiếu dữ liệu về việc GreenNode VKS có tích hợp sẵn các tính năng AI-native tương tự AWS (container caching, speculative decoding) hay không. Cần xác minh từ team Product/R&D.
- Không có thông tin về các deal lớn hoặc partnership mới của đối thủ Tier 1 trong 24h qua.
