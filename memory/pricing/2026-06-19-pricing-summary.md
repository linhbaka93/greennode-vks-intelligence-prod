# Pricing Summary — 2026-06-19

Source: competitor-monitor run | Model: qwen/qwen3-5-27b

## Key Findings

- [RSS] [AWS News Blog](https://aws.amazon.com/blogs/aws/announcing-amazon-ec2-g7-instances-accelerated-by-nvidia-rtx-pro-4500-blackwell-server-edition-gpus) 2026-06-18 — AWS công bố GA EC2 G7 instances với GPU NVIDIA RTX PRO 4500 Blackwell. Tác động: ❌ Feature gap về phần cứng AI inference. AWS cung cấp ngay lập tức lợi thế hiệu năng/giá cho LLM inference nặng. GreenNode đang thua nếu khách hàng cần performance tối đa cho training/inference LLM mà không có ràng buộc data residency. GreenNode cần rà soát roadmap GPU (A100/H100/Blackwell) để tránh mất khách hàng cần performance tối đa.
- [RSS] [AWS News Blog](https://aws.amazon.com/blogs/aws/introducing-amazon-bedrock-managed-knowledge-base-for-faster-more-accurate-enterprise-ai-applications) 2026-06-17 — AWS ra mắt Bedrock Managed Knowledge Base tích hợp sẵn, giảm chi phí vận hành RAG pipeline. Tác động: ❌ Rủi ro churn cho khách hàng Enterprise chạy GenAI nếu VKS không có giải pháp managed tương đương hoặc TCO thấp hơn đáng kể do chi phí nhân sự vận hành. AWS đang đóng gói 'AI Infrastructure' thành sản phẩm tiêu chuẩn, trong khi VKS vẫn bán hạ tầng K8s thuần.
- [Workspace] [pricing/2026-06-17_aws-eks_pricing.md] 2026-06-17 — AWS EKS thu phí Control Plane $0.10/giờ (~73 USD/tháng). Tác động: ✅ Cơ hội định vị. GreenNode VKS có thể dùng chiến lược 'Control Plane miễn phí' để thu hút SME và các cluster nhỏ, tạo ra delta TCO rõ rệt (~$876/năm/cluster) so với AWS.
- [Suy luận] Dựa trên [competitors/2026-06-17_fpt-cloud-fke_profile.md] và [competitors/2026-06-17_viettel-voks_profile.md] — Việc FPT và Viettel không công khai pricing chi tiết cho thấy chiến lược sales-led cho Enterprise. Tác động: ✅ Cơ hội cho VKS thu hút SME bằng bảng giá minh bạch và dễ dự báo TCO, tránh được cuộc chiến giá cả mờ ám ở phân khúc Enterprise.

## Recommended Actions

- Talk Track cho Sales (SME): Nhấn mạnh 'Control Plane miễn phí' của VKS so với AWS EKS ($73/tháng/cluster). Với 3 cluster SME, khách hàng tiết kiệm ~$260/tháng (~6.8 triệu VND/tháng) chỉ từ phí quản lý, chưa kể egress và billing VND.
- Talk Track cho Sales (Enterprise AI): Thừa nhận AWS có GPU Blackwell mới nhất, nhưng nhấn mạnh lợi thế 'Data Residency' và 'Sovereign AI' của VKS cho các tổ chức bị ràng buộc bởi Luật BVDLCN 2025. Đề xuất giải pháp hybrid: Training trên AWS (nếu cho phép), Inference trên VKS (để tối ưu latency và compliance).
- Pricing Recommendation: Giữ nguyên chiến lược 'Control Plane miễn phí' cho VKS để duy trì lợi thế cạnh tranh với AWS. Xem xét ra mắt gói 'AI Inference Bundle' với GPU A100/H100 có giá cố định (committed use) để cạnh tranh với Bizfly và FPT ở phân khúc SME/Mid-market.
- Theo dõi thêm: Cập nhật roadmap GPU của GreenNode (A100/H100/Blackwell) và so sánh hiệu năng/giá với AWS G7 instances. Nếu không có Blackwell trong 6 tháng, cần có chiến lược định vị lại (ví dụ: tập trung vào A100/H100 với giá tốt hơn và support tiếng Việt).
- Theo dõi thêm: Scrape lại trang pricing của FPT, Viettel, Bizfly hàng tuần để phát hiện thay đổi pricing hoặc promo mới.

## Risks

- Dữ liệu pricing của AWS EKS ($0.10/giờ) có thể thay đổi theo region (ap-southeast-1 Singapore thường cao hơn us-east-1 10-15%).
- Thiếu dữ liệu pricing mới nhất cho GPU instances của đối thủ nội địa (FPT, Viettel, Bizfly) khiến việc so sánh TCO cho workload AI chưa chính xác.
- AWS đang thay đổi cuộc chơi bằng cách đóng gói AI infrastructure (Bedrock, SageMaker) thay vì chỉ bán hạ tầng K8s, làm giảm tính so sánh trực tiếp về giá K8s thuần.
- Feature gap về GPU Blackwell của AWS có thể khiến GreenNode mất khách hàng AI cao cấp nếu không có roadmap phần cứng tương đương trong 6-12 tháng tới.

## Gaps / Thiếu dữ liệu

- Cần cập nhật: pricing/2026-06-17_aws-eks_pricing.md — Dữ liệu pricing AWS cần refresh (hạn dùng 30 ngày, hiện tại đã 2 ngày, nhưng cần kiểm tra region pricing cho VN).
- Thiếu dữ liệu: Pricing cụ thể cho GPU instances (A100/H100/Blackwell) của FPT Cloud, Viettel Cloud, và Bizfly Cloud. Cần scrape hoặc request quote để có số liệu so sánh TCO AI.
- Thiếu dữ liệu: Pricing cho các thành phần hidden cost (egress, LB, NAT) của đối thủ nội địa để tính toán TCO toàn diện.
- Không fetch được trang social: Các bài đăng social của đối thủ (FPT, Viettel) không có nội dung pricing công khai, cần xác minh qua kênh sales.
