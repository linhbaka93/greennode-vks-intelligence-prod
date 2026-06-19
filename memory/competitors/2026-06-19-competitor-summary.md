# Competitor Summary — 2026-06-19

Source: weekly-digest run | Model: qwen/qwen3-5-27b

## Key Findings

- [RSS] [AWS News Blog](https://aws.amazon.com/blogs/aws/announcing-amazon-ec2-g7-instances-accelerated-by-nvidia-rtx-pro-4500-blackwell-server-edition-gpus) 2026-06-18 — AWS ra mắt EC2 G7 instances với GPU NVIDIA RTX PRO 4500 Blackwell Server Edition, tập trung vào AI inference và graphics workloads. — Tác động tới GreenNode: Tăng áp lực cạnh tranh về hiệu năng AI inference. AWS có lợi thế công nghệ phần cứng mới nhất mà các đối thủ nội địa chưa công bố tương đương.
- [RSS] [AWS News Blog](https://aws.amazon.com/blogs/aws/announcing-web-search-on-amazon-bedrock-agentcore-ground-your-ai-agents-in-current-accurate-web-knowledge) 2026-06-17 — AWS công bố Web Search on Amazon Bedrock AgentCore, cho phép agents truy cập kiến thức web cập nhật mà không cần egress data. — Tác động tới GreenNode: AWS mở rộng khả năng Agentic AI, tạo khoảng cách feature với các nền tảng K8s thuần túy nếu GreenNode chưa có giải pháp tương tự tích hợp sẵn.
- [RSS] [Vietnam.vn](https://news.google.com/rss/articles/CBMikgFBVV95cUxQV2ExNGdzR1BneXhBNUhxMDNVY3dMZXhlUGlvcWFBYUk2OVZZdFJqTUZuY3NzdWUtWHZvUTJvZW1rZElGSWRzendwNlFfVEdNMjRoVUI2eExHeHQxTUtUWjJnaGxEdHlhSjdmM2UzdDhCVVlzZ3A4YldMcHZ5QmRUS0ZKWmpzWVpZX1hFVGdSd2Y0QQ?oc=5) 2026-06-17 — MSB Bank hợp tác chiến lược với GreenNode để vận hành hàng trăm ứng dụng AI, mở rộng từ ngân hàng số sang ngân hàng AI. — Tác động tới GreenNode: Củng cố vị thế GreenNode là đối tác AI Cloud uy tín cho phân khúc tài chính-ngân hàng tại Việt Nam, tạo case study mạnh cho các RFP tương lai.
- [RSS] [Vietnam.vn](https://news.google.com/rss/articles/CBMipAFBVV95cUxPQi0zZkRtNTlkR3JIbU45XzM1aElKTHljQWEzRVM4RnhXZ0s5OWZVV0Y0eGg5NUV4TWxPS00xRzhDNDlQRjhMOGVqVWFXcmswQ3JSUDV4aTFXeG0tclNVSE9ubnBpYl9YSTY4RGR4bENYZFJ2QW13dG1IRnluWGV0U051b3J2VFJjUzJIYjdtY2dRM25jbEZmNU52NzBMQWxiNG1Qbg?oc=5) 2026-06-12 — TP.HCM cấp Chứng nhận Doanh nghiệp Công nghệ cao đầu tiên cho nhà cung cấp hạ tầng AI (GreenNode). — Tác động tới GreenNode: Tăng lợi thế cạnh tranh trong các dự án chính phủ và doanh nghiệp lớn yêu cầu tuân thủ quy định nội địa và ưu tiên doanh nghiệp công nghệ cao.
- [RSS] [FPT Cloud Blog](https://fptcloud.com/cac-lo-hong-bao-mat-duoc-cong-bo-va-su-kien-an-ninh-mang-dang-chu-y-trong-thang-6-2) 2026-06-17 — FPT Cloud công bố bài viết về các lỗ hổng bảo mật và sự kiện an ninh mạng tháng 6. — Tác động tới GreenNode: FPT Cloud duy trì hoạt động truyền thông về bảo mật, nhưng chưa có thông tin về tính năng mới cho FKE hoặc thay đổi pricing.

## Risks

- {"risk": "AWS EC2 G7 với GPU Blackwell tạo lợi thế hiệu năng vượt trội cho các workload AI inference cao cấp mà GreenNode chưa có thông tin về phần cứng tương đương.", "mitigation": "Tập trung vào các workload không yêu cầu Blackwell, nhấn mạnh lợi thế về chi phí egress, hỗ trợ kỹ thuật tiếng Việt và tuân thủ data residency."}
- {"risk": "Thiếu thông tin công khai về pricing và feature mới của đối thủ nội địa (Viettel, FPT, Bizfly) trong tuần qua, có thể dẫn đến bất ngờ trong các RFP nếu họ có thay đổi nội bộ.", "mitigation": "Tiếp tục theo dõi các kênh chính thức và social media của đối thủ; chuẩn bị kịch bản phản hồi nếu có thông tin mới."}

## Gaps / Thiếu dữ liệu

- Cần cập nhật: competitors/2026-06-17_viettel-idc-kubernetes_profile.md — dữ liệu cũ, chưa có thông tin mới về VKS/vOKS trong 7 ngày qua.
- Cần cập nhật: competitors/2026-06-17_fpt-cloud-fke_profile.md — chưa xác minh được thông tin về GPU node pool trên FKE.
- Cần cập nhật: competitors/2026-06-17_bizfly-bke_profile.md — cần xác minh lại SLA và K8s versions mới nhất.
