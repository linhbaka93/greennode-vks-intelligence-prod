# Competitor Summary — 2026-06-19

Source: competitor-monitor run | Model: qwen/qwen3-5-27b

## Key Findings

- [RSS] AWS News Blog | https://aws.amazon.com/blogs/aws/announcing-amazon-ec2-g7-instances-accelerated-by-nvidia-rtx-pro-4500-blackwell-server-edition-gpus | published_at=2026-06-18 — AWS ra mắt EC2 G7 instances với GPU NVIDIA RTX PRO 4500 Blackwell Server Edition, tập trung vào AI inference và graphics workloads. — Tác động tới GreenNode: Tăng áp lực cạnh tranh về hiệu năng/giá cho workload AI inference. AWS có lợi thế công nghệ phần cứng mới nhất mà các đối thủ nội địa chưa công bố tương đương.
- [RSS] AWS News Blog | https://aws.amazon.com/blogs/aws/announcing-web-search-on-amazon-bedrock-agentcore-ground-your-ai-agents-in-current-accurate-web-knowledge | published_at=2026-06-17 — AWS công bố Web Search on Amazon Bedrock AgentCore (GA) và Managed Knowledge Base, cho phép agents truy cập kiến thức web và doanh nghiệp với zero data egress. — Tác động tới GreenNode: Mở rộng khả năng Agentic AI của AWS, tạo rào cản công nghệ cho các nền tảng K8s thuần túy không có AI-native tooling tích hợp sẵn.
- [RSS] Vietnam.vn | https://news.google.com/rss/articles/CBMikgFBVV95cUxQV2ExNGdzR1BneXhBNUhxMDNVY3dMZXhlUGlvcWFBYUk2OVZZdFJqTUZuY3NzdWUtWHZvUTJvZW1rZElGSWRzendwNlFfVEdNMjRoVUI2eExHeHQxTUtUWjJnaGxEdHlhSjdmM2UzdDhCVVlzZ3A4YldMcHZ5QmRUS0ZKWmpzWVpZX1hFVGdSd2Y0QQ | published_at=2026-06-17 — MSB Bank và GreenNode mở rộng hợp tác chiến lược, triển khai hàng trăm ứng dụng AI để chuyển đổi từ digital banking sang AI banking. — Tác động tới GreenNode: Củng cố vị thế GreenNode là đối tác AI Cloud hàng đầu cho ngân hàng tại VN, tạo case study mạnh cho phân khúc Enterprise/Gov.
- [RSS] Artificial Intelligence | https://aws.amazon.com/blogs/machine-learning/introducing-container-caching-in-amazon-sagemaker-ai-for-faster-model-scaling | published_at=2026-06-16 — AWS ra mắt container caching cho SageMaker AI, giảm latency scale-out model Generative AI lên đến 2 lần. — Tác động tới GreenNode: Cải thiện hiệu năng và chi phí cho workload AI inference, tạo áp lực lên các giải pháp K8s không có tối ưu hóa container layer tương tự.
- [RSS] FPT Cloud Blog | https://fptcloud.com/fpt-cloud-desktop-3-1-va-backup-veeam-1-5-ra-mat-loat-nang-cap-moi-hoan-thien-trai-nghiem-va-kha-nang-kiem-soat-van-hanh | published_at=2026-06-16 — FPT Cloud ra mắt FPT Cloud Desktop 3.1 và FPT Backup Veeam 1.5 với nâng cấp trải nghiệm và kiểm soát vận hành. — Tác động tới GreenNode: FPT tập trung vào các dịch vụ desktop và backup, chưa có tín hiệu mới về K8s/AI. Tuy nhiên, việc nâng cấp liên tục cho thấy FPT đang củng cố nền tảng dịch vụ tổng thể.

## Risks

- Tác động tới GreenNode: Rủi ro thua thế trong các RFP yêu cầu hiệu năng AI cao cấp hoặc chi phí inference tối ưu.
- Tác động tới GreenNode: Không thể đánh giá chính xác mức độ cạnh tranh trực tiếp từ đối thủ nội địa.

## Gaps / Thiếu dữ liệu

- Cần cập nhật: competitors/2026-06-17_viettel-idc-kubernetes_profile.md — dữ liệu cũ, chưa xác minh pricing K8s và SLA mới nhất.
- Cần cập nhật: competitors/2026-06-17_fpt-cloud-fke_profile.md — thiếu thông tin về GPU node pool và pricing mới.
- Không fetch được nội dung chi tiết từ các trang scrape (viettel-voks, bizfly-bke, fpt-fke) do chỉ thu được HTML/CSS, cần công cụ parse sâu hơn.
