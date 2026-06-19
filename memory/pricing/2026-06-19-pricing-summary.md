# Pricing Summary — 2026-06-19

Source: weekly-digest run | Model: qwen/qwen3-5-27b

## Key Findings

- [RSS] [AWS News Blog](https://aws.amazon.com/blogs/aws/announcing-amazon-ec2-g7-instances-accelerated-by-nvidia-rtx-pro-4500-blackwell-server-edition-gpus) 2026-06-18 — AWS công bố GA EC2 G7 instances với GPU NVIDIA RTX PRO 4500 Blackwell. Tác động: ❌ Feature gap về phần cứng AI inference. AWS cung cấp ngay lập tức lợi thế hiệu năng/giá cho LLM inference nặng. GreenNode cần rà soát roadmap GPU (A100/H100/Blackwell) để tránh mất khách hàng cần performance tối đa.
- [RSS] [AWS News Blog](https://aws.amazon.com/blogs/machine-learning/introducing-container-caching-in-amazon-sagemaker-ai-for-faster-model-scaling) 2026-06-16 — AWS ra mắt container image caching cho SageMaker AI, giảm latency scale-out lên đến 2x. Tác động: ❌ Rủi ro TCO cho AI inference. AWS tối ưu hóa chi phí vận hành và hiệu năng tự động, trong khi VKS chưa có thông tin công khai về tính năng tương đương. Khách hàng Enterprise có thể bị thu hút bởi TCO thấp hơn của AWS nếu không cần data residency VN.
- [RSS] [Vietnam.vn](https://news.google.com/rss/articles/CBMipAFBVV95cUxPQi0zZkRtNTlkR3JIbU45XzM1aElKTHljQWEzRVM4RnhXZ0s5OWZVV0Y0eGg5NUV4TWxPS00xRzhDNDlQRjhMOGVqVWFXcmswQ3JSUDV4aTFXeG0tclNVSE9ubnBpYl9YSTY4RGR4bENYZFJ2QW13dG1IRnluWGV0U051b3J2VFJjUzJIYjdtY2dRM25jbEZmNU52NzBMQWxiNG1Qbg?oc=5) 2026-06-12 — GreenNode là nhà cung cấp hạ tầng AI đầu tiên được TP.HCM cấp Chứng nhận Doanh nghiệp Công nghệ cao. Tác động: ✅ Cơ hội định vị giá trị (Value-based pricing). Chứng nhận này củng cố vị thế 'Sovereign AI' cho các deal Enterprise/Gov, cho phép GreenNode định giá cao hơn dựa trên compliance và an ninh dữ liệu thay vì chỉ cạnh tranh giá phần cứng.
- [RSS] [Vietnam.vn](https://news.google.com/rss/articles/CBMikgFBVV95cUxQV2ExNGdzR1BneXhBNUhxMDNVY3dMZXhlUGlvcWFBYUk2OVZZdFJqTUZuY3NzdWUtWHZvUTJvZW1rZElGSWRzendwNlFfVEdNMjRoVUI2eExHeHQxTUtUWjJnaGxEdHlhSjdmM2UzdDhCVVlzZ3A4YldMcHZ5QmRUS0ZKWmpzWVpZX1hFVGdSd2Y0QQ?oc=5) 2026-06-17 — MSB Bank hợp tác chiến lược với GreenNode để vận hành hàng trăm ứng dụng AI. Tác động: ✅ Proof of Concept (PoC) thành công. Đây là tín hiệu mạnh về willingness-to-pay của khách hàng ngân hàng đối với giải pháp AI onshore, hỗ trợ talk track về TCO và an toàn dữ liệu trong các deal tương tự.
- [Workspace] [pricing/2026-06-17_aws-eks_pricing.md] 2026-06-17 — AWS EKS thu phí Control Plane $0.10/giờ (~73 USD/tháng). Tác động: ✅ Cơ hội định vị cho SME. GreenNode có thể dùng chiến lược 'Control Plane miễn phí' hoặc giá thấp hơn để thu hút khách hàng SME, trong khi AWS có chi phí cố định bắt buộc.

## Recommended Actions

- Talk Track cho Sales (AI Workload): 'Trong khi AWS cung cấp phần cứng mới nhất (Blackwell), GreenNode cung cấp giải pháp Sovereign AI với chứng nhận Doanh nghiệp Công nghệ cao và tuân thủ tuyệt đối Luật BVDLCN 2025. Với hợp tác MSB Bank, chúng tôi đã chứng minh khả năng vận hành hàng trăm ứng dụng AI an toàn ngay tại Việt Nam, giúp bạn tránh rủi ro pháp lý và chi phí egress quốc tế.'
- Pricing Recommendation: Xây dựng bảng TCO so sánh cho Scenario S4 (AI Inference) giả định với AWS G7, tập trung vào 'Hidden Cost' của AWS (egress, data transfer, control plane fee) và lợi thế 'Data Residency' của GreenNode. Nếu không có giá GPU cụ thể, hãy đề xuất 'Custom Quote' dựa trên nhu cầu thực tế của khách hàng.
- Theo dõi thêm: Rà soát roadmap GPU của GreenNode để xác định thời điểm ra mắt các instance tương đương Blackwell. Nếu chưa có, cần chuẩn bị kịch bản 'Hybrid Cloud' hoặc 'Borrowed GPU' để cạnh tranh trong ngắn hạn.
- Tận dụng chứng nhận: Đưa chứng nhận Doanh nghiệp Công nghệ cao và hợp tác MSB vào mọi tài liệu marketing và proposal cho phân khúc Enterprise/Gov để tăng giá trị cảm nhận (perceived value) và biện minh cho mức giá cao hơn nếu cần.

## Risks

- Dữ liệu pricing GPU của GreenNode chưa được cập nhật trong workspace, không thể tính toán TCO chính xác cho Scenario S4 (AI Inference) so với AWS G7.
- AWS liên tục ra mắt tính năng tối ưu hóa AI (caching, speculative decoding) làm giảm TCO thực tế, trong khi GreenNode chưa có thông tin công khai về các tính năng tương đương.
- Đối thủ nội địa (FPT, Viettel) có thể đang áp dụng discount sâu cho Enterprise (không công khai), tạo rủi ro mất deal nếu GreenNode chỉ dựa vào bảng giá niêm yết.

## Gaps / Thiếu dữ liệu

- Cần cập nhật: pricing/2026-06-17_aws-eks_pricing.md — Dữ liệu pricing AWS cần refresh (next refresh 2026-06-24) để đảm bảo độ chính xác cho các tính toán TCO mới.
- Thiếu dữ liệu: Pricing GPU (A100/H100/Blackwell) của GreenNode VKS. Không có thông tin về giá/giờ hoặc giá/tháng cho các instance GPU để so sánh trực tiếp với AWS G7.
- Thiếu dữ liệu: TCO breakdown cho Scenario S4 (AI Inference) trên GreenNode. Cần số liệu về egress, storage, và compute để xây dựng bảng so sánh.
- Thiếu dữ liệu: Pricing chính xác của FPT FKE và Viettel vOKS. Cần xác minh xem họ có áp dụng discount cho GPU node pool hay không.
