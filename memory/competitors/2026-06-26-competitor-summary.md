# Competitor Summary — 2026-06-26

Source: competitor-monitor run | Model: qwen/qwen3-5-27b

## Key Findings

- [RSS] AWS Containers Blog | https://aws.amazon.com/blogs/containers/faster-nodes-smarter-scaling-whats-new-inside-amazon-elastic-kubernetes-service-amazon-eks-auto-mode | published_at=2026-06-23 — [RSS] [AWS Containers Blog](https://aws.amazon.com/blogs/containers/faster-nodes-smarter-scaling-whats-new-inside-amazon-elastic-kubernetes-service-amazon-eks-auto-mode) 2026-06-23 — AWS công bố cải tiến hiệu năng và khả năng mở rộng cho Amazon EKS Auto Mode, tập trung vào 4 trụ cột: runtime, compute, storage, networking. — Tác động tới GreenNode: AWS đang tối ưu hóa trải nghiệm 'zero-management' cho K8s, tăng áp lực cạnh tranh về độ tự động hóa và hiệu năng cho GreenNode VKS. — GreenNode nên: Đánh giá lại tính năng autoscaling và fleet management của VKS để đảm bảo không bị tụt hậu về trải nghiệm người dùng.
- [RSS] AWS Machine Learning Blog | https://aws.amazon.com/blogs/machine-learning/optimize-model-training-on-amazon-sagemaker-ai-with-nvidia-blackwell | published_at=2026-06-25 — [RSS] [AWS Machine Learning Blog](https://aws.amazon.com/blogs/machine-learning/optimize-model-training-on-amazon-sagemaker-ai-with-nvidia-blackwell) 2026-06-25 — AWS hướng dẫn tối ưu hóa training model trên Amazon SageMaker AI với kiến trúc NVIDIA Blackwell, tận dụng bộ nhớ mở rộng và định dạng precision phù hợp. — Tác động tới GreenNode: AWS đang dẫn đầu về hỗ trợ phần cứng AI mới nhất (Blackwell) cho workload training. Nếu GreenNode chưa có GPU Blackwell hoặc tối ưu tương đương, sẽ mất lợi thế trong các dự án AI training lớn. — GreenNode nên: Kiểm tra lộ trình cung cấp GPU Blackwell và công bố roadmap nếu có.
- [RSS] Kubernetes Blog | https://kubernetes.io/blog/2026/06/25/visual-context-volcano-headlamp-plugin | published_at=2026-06-25 — [RSS] [Kubernetes Blog](https://kubernetes.io/blog/2026/06/25/visual-context-volcano-headlamp-plugin) 2026-06-25 — Kubernetes Blog giới thiệu plugin Headlamp cho Volcano (batch scheduler cho HPC/AI/ML), giúp kiểm tra workload nhanh hơn. — Tác động tới GreenNode: Cộng đồng K8s đang tích hợp sâu các công cụ quản lý workload AI/HPC. GreenNode VKS cần đảm bảo hỗ trợ Volcano và các plugin tương tự để đáp ứng nhu cầu khách hàng AI-native. — GreenNode nên: Xác nhận khả năng tích hợp Volcano và các công cụ observability AI trên VKS.
- [RSS] FPT Cloud Blog | https://fptcloud.com/3-yeu-to-cot-loi-danh-gia-hieu-nang-cua-ha-tang-cloud | published_at=2026-06-25 — [RSS] [FPT Cloud Blog](https://fptcloud.com/3-yeu-to-cot-loi-danh-gia-hieu-nang-cua-ha-tang-cloud) 2026-06-25 — FPT Cloud đăng bài về 3 yếu tố cốt lõi đánh giá hiệu năng hạ tầng Cloud. — Tác động tới GreenNode: FPT Cloud đang định vị lại thông điệp về hiệu năng, có thể là tín hiệu chuẩn bị cho chiến dịch marketing hoặc ra mắt tính năng mới. — GreenNode nên: Theo dõi thêm nội dung chi tiết và so sánh với tiêu chuẩn hiệu năng của VKS.
- [RSS] FPT Cloud Blog | https://fptcloud.com/khi-cloud-khong-con-la-nut-that-co-chai-hanh-trinh-tai-kien-truc-ha-tang-cho-workload-hieu-nang-cao | published_at=2026-06-25 — [RSS] [FPT Cloud Blog](https://fptcloud.com/khi-cloud-khong-con-la-nut-that-co-chai-hanh-trinh-tai-kien-truc-ha-tang-cho-workload-hieu-nang-cao) 2026-06-25 — FPT Cloud chia sẻ hành trình tái kiến trúc hạ tầng cho workload hiệu năng cao. — Tác động tới GreenNode: FPT Cloud đang nhấn mạnh khả năng xử lý workload hiệu năng cao, có thể là tín hiệu cạnh tranh trực tiếp với GreenNode VKS trong phân khúc HPC/AI. — GreenNode nên: Chuẩn bị case study hoặc benchmark để chứng minh khả năng xử lý workload hiệu năng cao của VKS.

## Risks

- [Workspace] competitors/2026-06-26-competitor-summary.md
- [RSS] AWS Machine Learning Blog | https://aws.amazon.com/blogs/machine-learning/optimize-model-training-on-amazon-sagemaker-ai-with-nvidia-blackwell | published_at=2026-06-25

## Gaps / Thiếu dữ liệu

- Cần cập nhật: competitors/2026-06-17_viettel-idc-kubernetes_profile.md — dữ liệu cũ, chưa dùng được cho so sánh chi tiết.
- Cần cập nhật: competitors/2026-06-17_bizfly-bke_profile.md — dữ liệu cũ, chưa dùng được cho so sánh chi tiết.
- Cần cập nhật: competitors/2026-06-17_fpt-cloud-fke_profile.md — dữ liệu cũ, chưa dùng được cho so sánh chi tiết.
- Cần cập nhật: competitors/2026-06-17_aws-eks_profile.md — dữ liệu cũ, chưa dùng được cho so sánh chi tiết.
- Không fetch được trang social của Viettel IDC, FPT Cloud, Bizfly Cloud trong 3 ngày qua — cần xác minh lại bằng công cụ khác hoặc chờ dữ liệu mới.
- Chưa xác minh được tính năng 'customer-routed control plane egress' trên GreenNode VKS — cần liên hệ đội ngũ sản phẩm để xác nhận.
