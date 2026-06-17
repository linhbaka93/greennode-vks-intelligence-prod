# Competitor Summary — 2026-06-17

Source: competitor-monitor run | Model: qwen/qwen3-5-27b

## Key Findings

- [Blog] FPT Cloud | https://fptcloud.com/fpt-cloud-desktop-3-1-va-backup-veeam-1-5-ra-mat-loat-nang-cap-moi-hoan-thien-trai-nghiem-va-kha-nang-kiem-soat-van-hanh | published_at=2026-06-16 — [Blog] [FPT Cloud](https://fptcloud.com/fpt-cloud-desktop-3-1-va-backup-veeam-1-5-ra-mat-loat-nang-cap-moi-hoan-thien-trai-nghiem-va-kha-nang-kiem-soat-van-hanh) 2026-06-16 — FPT Cloud ra mắt FPT Desktop 3.1 và Backup Veeam 1.5, tập trung vào trải nghiệm người dùng và kiểm soát vận hành, không đề cập đến FPT Kubernetes Engine (FKE).
- [Scrape] Viettel IDC | https://viettelidc.com.vn | fetched_at=2026-06-17 — [Scrape] Viettel IDC | https://viettelidc.com.vn | fetched_at=2026-06-17 — Trang chủ Viettel IDC không hiển thị thông báo mới về VKS/vOKS. Dữ liệu scrape chỉ ghi nhận giao diện loading, không có nội dung sản phẩm mới.
- [Scrape] Bizfly Cloud | https://bizflycloud.vn/kubernetes | fetched_at=2026-06-17 — [Scrape] Bizfly Cloud | https://bizflycloud.vn/kubernetes | fetched_at=2026-06-17 — Trang sản phẩm BKE không có thay đổi nội dung đáng kể so với profile trước đó (GPU node pool vẫn được xác nhận là có).
- [RSS] AWS Machine Learning Blog | https://aws.amazon.com/blogs/machine-learning/safeguard-your-agentic-ai-applications-with-the-amazon-bedrock-guardrails-invokeguardrailchecks-api | published_at=2026-06-16 — [RSS] [AWS Machine Learning Blog](https://aws.amazon.com/blogs/machine-learning/safeguard-your-agentic-ai-applications-with-the-amazon-bedrock-guardrails-invokeguardrailchecks-api) 2026-06-16 — AWS ra mắt API InvokeGuardrailChecks cho Amazon Bedrock Guardrails, cho phép áp dụng các biện pháp bảo vệ an toàn linh hoạt cho AI agents.
- [RSS] AWS Machine Learning Blog | https://aws.amazon.com/blogs/machine-learning/introducing-container-caching-in-amazon-sagemaker-ai-for-faster-model-scaling | published_at=2026-06-16 — [RSS] [AWS Machine Learning Blog](https://aws.amazon.com/blogs/machine-learning/introducing-container-caching-in-amazon-sagemaker-ai-for-faster-model-scaling) 2026-06-16 — AWS giới thiệu container caching cho SageMaker AI, giảm latency scale-out lên đến 2x cho Generative AI.
- [RSS] Vietnam.vn | https://news.google.com/rss/articles/CBMiuAFBVV95cUxQOWJfSE9ncmhiNUd6YmR1ZEZnUG1DTFZBZXVicWNIeWRlNlFwQnJPcElhV2lVLWFHU0NHR3lQMmIzbVdNNjY5UC02TlRTdzBGTXh1VzA1S2tzZU10VDZfZ21qcG1GWDhkSWUtLWRIVldvNlhuU1B3RVQ2dkxvc2hoUlppT2U3MEd3TDVnZzlvblFmdzNLZXlncEJKR05OOW1iMW5PRnhhRGMxU283bzZaWERCWkRXV3M5?oc=5 | published_at=2026-06-14 — [RSS] [Vietnam.vn](https://news.google.com/rss/articles/CBMiuAFBVV95cUxQOWJfSE9ncmhiNUd6YmR1ZEZnUG1DTFZBZXVicWNIeWRlNlFwQnJPcElhV2lVLWFHU0NHR3lQMmIzbVdNNjY5UC02TlRTdzBGTXh1VzA1S2tzZU10VDZfZ21qcG1GWDhkSWUtLWRIVldvNlhuU1B3RVQ2dkxvc2hoUlppT2U3MEd3TDVnZzlvblFmdzNLZXlncEJKR05OOW1iMW5PRnhhRGMxU283bzZaWERCWkRXV3M5?oc=5) 2026-06-14 — TP.HCM cấp Chứng nhận Doanh nghiệp Công nghệ cao đầu tiên cho nhà cung cấp hạ tầng AI (GreenNode).

## Risks

- {"risk": "Đối thủ nội địa (Viettel, FPT, Bizfly) không công khai thông tin mới, khiến GreenNode khó xác định chính xác động thái pricing hoặc feature gap.", "mitigation": "Tăng cường thu thập thông tin qua các kênh gián tiếp (tin tức doanh nghiệp, hợp đồng công khai, phỏng vấn lãnh đạo) và duy trì chiến lược 'transparency' của GreenNode để thu hút SME."}
- {"risk": "AWS liên tục ra mắt tính năng AI-native (Guardrails, Caching) tạo áp lực về mặt kỹ thuật cho GreenNode VKS.", "mitigation": "Nhấn mạnh lợi thế 'Sovereign AI' (dữ liệu tại VN, tuân thủ luật BVDLCN 2025) và chứng nhận công nghệ cao để bù đắp cho khoảng cách feature AI so với hyperscaler."}

## Gaps / Thiếu dữ liệu

- Không có thông tin pricing mới từ Viettel IDC, FPT Cloud, hay Bizfly Cloud trong 3 ngày qua. Cần cập nhật pricing snapshot từ các nguồn khác (sales inquiry, đối tác) để có dữ liệu so sánh TCO chính xác.
- Không xác nhận được nội dung cụ thể từ trang Viettel IDC và Bizfly Cloud do scrape chỉ trả về giao diện loading/CSS. Cần kiểm tra lại bằng công cụ khác hoặc chờ tin tức chính thức.
