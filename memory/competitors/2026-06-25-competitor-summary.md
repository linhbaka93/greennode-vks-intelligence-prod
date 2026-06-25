# Competitor Summary — 2026-06-25

Source: competitor-monitor run | Model: qwen/qwen3-5-27b

## Key Findings

- [RSS] [AWS Containers Blog](https://aws.amazon.com/blogs/containers/amazon-eks-now-supports-control-plane-egress-through-your-vpc) 2026-06-22 — AWS công bố tính năng 'customer-routed control plane egress' cho Amazon EKS, cho phép định tuyến lưu lượng control plane (admission webhooks, OIDC lookups) qua VPC của khách hàng thay vì internet công cộng. — Tác động tới GreenNode: Tăng áp lực cạnh tranh về bảo mật và compliance (churn risk) cho GreenNode VKS. Đây là tính năng bắt buộc đối với nhiều khách hàng ngân hàng/chính phủ yêu cầu lưu lượng control plane không ra internet. Nếu GreenNode chưa có tính năng tương đương, sẽ mất điểm trong các RFP Q3/Q4.
- [RSS] [AWS Containers Blog](https://aws.amazon.com/blogs/containers/faster-nodes-smarter-scaling-whats-new-inside-amazon-elastic-kubernetes-service-amazon-eks-auto-mode) 2026-06-23 — AWS nâng cấp hiệu năng và khả năng mở rộng cho EKS Auto Mode trên 4 trụ cột: runtime, compute, storage, networking. — Tác động tới GreenNode: Tăng áp lực về TCO và trải nghiệm 'serverless K8s'. AWS đang thu hẹp khoảng cách vận hành, khiến khách hàng doanh nghiệp ưu tiên giải pháp tự động hóa cao. GreenNode VKS có nguy cơ bị coi là 'nặng nề' hơn nếu không có autoscaling (HPA/VPA/Karpenter) tối ưu tương đương.
- [RSS] [AWS News Blog](https://aws.amazon.com/blogs/aws/aws-weekly-roundup-ny-summit-recap-local-zone-in-hanoi-grok-4-3-in-bedrock-price-reductions-and-more-june-22-2026) 2026-06-22 — AWS công bố Local Zone tại Hà Nội và giảm giá cho một số dịch vụ. — Tác động tới GreenNode: Mở rộng lợi thế về độ trễ và giá cho AWS tại VN. Local Zone Hà Nội giúp AWS cạnh tranh trực tiếp với các nhà cung cấp nội địa về độ trễ cho workload AI/Real-time. Giảm giá tạo áp lực pricing pressure lên GreenNode VKS.
- [RSS] [AWS Blog](https://aws.amazon.com/blogs/machine-learning/optimize-model-training-on-amazon-sagemaker-ai-with-nvidia-blackwell) 2026-06-25 — AWS hướng dẫn tối ưu hóa training model trên SageMaker AI với kiến trúc NVIDIA Blackwell. — Tác động tới GreenNode: AWS đang dẫn đầu về hỗ trợ phần cứng AI mới nhất (Blackwell). Các đối thủ nội địa chưa có thông tin công khai về GPU thế hệ mới, tạo lợi thế công nghệ cho AWS trong các workload AI cao cấp. GreenNode VKS có nguy cơ bị coi là lạc hậu về phần cứng AI.
- [Scrape] FPT Cloud | https://fptcloud.com/kubernetes | fetched_at=2026-06-25 — Trang sản phẩm FPT Kubernetes Engine (FKE) không có thay đổi nội dung đáng kể so với snapshot trước đó. — Tác động tới GreenNode: FPT Cloud không có động thái mới về tính năng hoặc giá trong ngắn hạn. Tuy nhiên, việc thiếu cập nhật có thể là dấu hiệu của sự chậm trễ trong phát triển sản phẩm hoặc chiến lược marketing.
- [Scrape] Viettel IDC | https://viettelcloud.vn/san-pham/kubernetes | fetched_at=2026-06-25 — Trang sản phẩm Viettel Kubernetes Service (VKS/vOKS) không có thay đổi nội dung đáng kể. — Tác động tới GreenNode: Viettel IDC duy trì ổn định sản phẩm, không có tín hiệu về giảm giá hoặc tính năng mới. Tuy nhiên, vị thế của Viettel trong segment Gov/Enterprise vẫn rất mạnh nhờ quan hệ và compliance.
- [Scrape] Bizfly Cloud | https://bizflycloud.vn/kubernetes | fetched_at=2026-06-25 — Trang sản phẩm Bizfly Kubernetes Engine (BKE) không có thay đổi nội dung đáng kể. — Tác động tới GreenNode: Bizfly Cloud không có động thái mới. Tuy nhiên, cần lưu ý các hoạt động marketing hoặc partnership của họ trong segment SME và startup.

## Risks

- {"risk": "Feature gap về bảo mật control plane (customer-routed egress).", "severity": "high", "description": "AWS đã công bố tính năng cho phép định tuyến lưu lượng control plane qua VPC của khách hàng. Đây là yêu cầu bắt buộc đối với nhiều khách hàng ngân hàng/chính phủ. Nếu GreenNode VKS chưa có tính năng này, sẽ mất điểm trong các RFP và có nguy cơ churn cao."}
- {"risk": "Lợi thế phần cứng AI của AWS (NVIDIA Blackwell).", "severity": "medium", "description": "AWS đang dẫn đầu về hỗ trợ phần cứng AI mới nhất. Các đối thủ nội địa chưa có thông tin công khai về GPU thế hệ mới, tạo lợi thế công nghệ cho AWS trong các workload AI cao cấp."}
- {"risk": "Áp lực TCO từ EKS Auto Mode.", "severity": "medium", "description": "AWS nâng cấp khả năng tự động hóa và hiệu năng của EKS Auto Mode, tạo áp lực về TCO và trải nghiệm vận hành cho GreenNode VKS."}

## Gaps / Thiếu dữ liệu

- Cần cập nhật: competitors/2026-06-17_viettel-idc-kubernetes_profile.md — dữ liệu cũ, chưa dùng được cho so sánh chi tiết.
- Cần cập nhật: competitors/2026-06-17_bizfly-bke_profile.md — dữ liệu cũ, chưa dùng được cho so sánh chi tiết.
- Cần cập nhật: competitors/2026-06-17_fpt-cloud-fke_profile.md — dữ liệu cũ, chưa dùng được cho so sánh chi tiết.
- Cần cập nhật: competitors/2026-06-17_aws-eks_profile.md — dữ liệu cũ, chưa dùng được cho so sánh chi tiết.
- Thiếu thông tin về giá và tính năng cụ thể của GreenNode VKS so với đối thủ nội địa trong 3 ngày qua.
- Thiếu thông tin về kế hoạch nâng cấp phần cứng GPU của GreenNode.
