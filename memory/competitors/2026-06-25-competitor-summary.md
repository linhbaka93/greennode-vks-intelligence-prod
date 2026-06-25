# Competitor Summary — 2026-06-25

Source: daily-intelligence run | Model: qwen/qwen3-5-27b

## Key Findings

- [RSS] [AWS Containers Blog](https://aws.amazon.com/blogs/containers/faster-nodes-smarter-scaling-whats-new-inside-amazon-elastic-kubernetes-service-amazon-eks-auto-mode) 2026-06-23 — AWS công bố nâng cấp hiệu năng và khả năng mở rộng cho EKS Auto Mode trên 4 trụ cột: runtime, compute, storage, networking. — Tác động: Tăng áp lực cạnh tranh về hiệu năng tự động (autoscaling) và trải nghiệm 'serverless K8s'. GreenNode VKS cần rà soát lại khả năng autoscaling (HPA/VPA/Karpenter) và so sánh TCO với EKS Auto Mode để tránh mất khách hàng doanh nghiệp ưu tiên vận hành tối giản. — Tác động tới GreenNode: Feature gap / TCO pressure
- [RSS] [AWS Blog](https://aws.amazon.com/blogs/machine-learning/build-a-healthcare-appointment-agent-with-amazon-nova-2-sonic) 2026-06-24 — AWS ra mắt Amazon Nova 2 Sonic, cho phép xây dựng voice agent xử lý cuộc hẹn y tế, xác thực giọng nói và thu thập dữ liệu sức khỏe. — Tác động: AWS đang dẫn đầu về 'AI-native' với các use-case cụ thể (y tế, protein research). GreenNode VKS thiếu các giải pháp AI agent tích hợp sẵn, tạo rủi ro mất cơ hội trong các dự án chuyển đổi số AI của doanh nghiệp lớn. — Tác động tới GreenNode: Feature gap / Churn risk (AI segment)
- [RSS] [Kubernetes Blog](https://kubernetes.io/blog/2026/06/24/wg-device-management-spotlight-2026) 2026-06-24 — Kubernetes upstream công bố WG Device Management, tập trung vào quản lý phần cứng chuyên sâu (GPU, TPU, network interfaces) cho workload AI, Edge và Telecom. — Tác động: Xu hướng tiêu chuẩn hóa quản lý phần cứng sẽ trở thành yêu cầu bắt buộc cho các workload AI cao cấp. Nếu GreenNode VKS chưa hỗ trợ Device Plugin tiêu chuẩn hoặc tính năng tương tự, sẽ gặp khó khăn khi triển khai các workload AI phức tạp so với hyperscaler. — Tác động tới GreenNode: Feature gap / Technical readiness
- [RSS] [Vietnam.vn](https://news.google.com/rss/articles/CBMihAFBVV95cUxPbkszeEJGZ0RyRjJfZlZiSjJvT3VYeFFFM2dMXzhOcmxRSEVDcHJGbmtrY0pKc011NGdZS2JmTnBPZWJlWEZZbDFtTFlvOFhiUUloVzl2LTA2Q2xNVl9yYXQ5WloxNjBGTzRRZE1kX0ZOYnItdWpTTmlFc0NPSjBmNG51TFc?oc=5) 2026-06-24 — Bài báo đề cập đến 'cuộc đua data center tại Đông Nam Á' và TP.HCM là cực tăng trưởng mới. — Tác động: Tín hiệu thị trường cho thấy sự cạnh tranh khốc liệt về hạ tầng vật lý và vị trí data center. GreenNode cần tận dụng lợi thế 'Sovereign AI' và chứng nhận công nghệ cao tại TP.HCM để định vị khác biệt so với các đối thủ nội địa khác. — Tác động tới GreenNode: Market positioning

## Gaps / Thiếu dữ liệu

- Cần cập nhật: competitors/2026-06-17_viettel-idc-kubernetes_profile.md — dữ liệu cũ, chưa dùng được để so sánh feature/pricing mới nhất.
- Cần cập nhật: competitors/2026-06-17_fpt-cloud-fke_profile.md — dữ liệu cũ, chưa dùng được để so sánh feature/pricing mới nhất.
- Cần cập nhật: competitors/2026-06-17_bizfly-bke_profile.md — dữ liệu cũ, chưa dùng được để so sánh feature/pricing mới nhất.
- Cần xác minh: Khả năng hỗ trợ Device Management và AI Agent của GreenNode VKS so với tiêu chuẩn Kubernetes upstream và AWS EKS.
- Không fetch được trang social: Các nguồn social của đối thủ nội địa (Viettel IDC, FPT Cloud, Bizfly Cloud) không có tin mới trong evidence_bundle; cần kiểm tra lại nếu có thay đổi lớn.
