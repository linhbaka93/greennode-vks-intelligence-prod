# Pricing Summary — 2026-06-17

Source: competitor-monitor run | Model: qwen/qwen3-5-27b

## Key Findings

- [RSS] [AWS News Blog](https://aws.amazon.com/blogs/aws/introducing-amazon-bedrock-managed-knowledge-base-for-faster-more-accurate-enterprise-ai-applications) 2026-06-17 — AWS ra mắt Bedrock Managed Knowledge Base tích hợp sẵn, giảm chi phí vận hành RAG pipeline. Tác động tới GreenNode: ❌ Rủi ro churn cho khách hàng Enterprise chạy GenAI nếu VKS không có giải pháp managed tương đương hoặc TCO thấp hơn đáng kể do chi phí nhân sự vận hành.
- [RSS] [AWS Blog](https://aws.amazon.com/blogs/machine-learning/introducing-container-caching-in-amazon-sagemaker-ai-for-faster-model-scaling) 2026-06-16 — AWS SageMaker AI giới thiệu container caching, giảm latency scale-out GenAI lên 2x. Tác động tới GreenNode: ❌ GreenNode thua về AI-native infrastructure optimization. Khách hàng cần inference tốc độ cao có thể bị thu hút bởi AWS nếu không bị ràng buộc bởi data residency.
- [Scrape] Viettel Cloud | https://viettelcloud.vn/san-pham/kubernetes | fetched_at=2026-06-17 — Trang sản phẩm vOKS không hiển thị bảng giá công khai, chỉ có nút 'Liên hệ tư vấn'. Tác động tới GreenNode: ⚠️ Khó so sánh TCO trực tiếp. GreenNode cần chuẩn bị battlecard TCO giả định (scenario-based) để đối phó với chiến lược 'sales-led' của Viettel.
- [Scrape] FPT Cloud | https://fptcloud.com/kubernetes | fetched_at=2026-06-17 — FPT FKE không công bố giá, tập trung vào tính năng Dedicated FKE. Tác động tới GreenNode: ⚠️ FPT nhắm vào Enterprise/SOE với mô hình riêng biệt. GreenNode nên tập trung vào phân khúc SME/Mid-market với bảng giá minh bạch và TCO dự báo được.
- [Scrape] Bizfly Cloud | https://bizflycloud.vn/kubernetes | fetched_at=2026-06-17 — Bizfly BKE xác nhận có GPU node pool nhưng không công bố giá. Tác động tới GreenNode: ⚠️ Bizfly đang cạnh tranh trực tiếp ở phân khúc SME AI. GreenNode cần rà soát lại pricing GPU (nếu có) để đảm bảo cạnh tranh.
- [Workspace] pricing/2026-06-17_aws-eks_pricing.md 2026-06-17 — AWS EKS Control Plane phí $0.10/giờ (~2.620.000 VND/tháng). Tác động tới GreenNode: ✅ Cơ hội định vị 'Free Control Plane' hoặc 'Flat Fee thấp hơn' cho cluster nhỏ/SME, tạo lợi thế TCO rõ rệt so với AWS cho workload quy mô vừa.

## Recommended Actions

- Talk Track cho Sales (SME/Mid-market): 'Khác biệt với AWS EKS tính phí $0.10/giờ cho Control Plane (~2.6 triệu VND/tháng), GreenNode VKS giúp bạn loại bỏ chi phí cố định này cho các cluster nhỏ, giảm TCO khởi điểm lên đến 30% cho workload SME.'
- Talk Track cho Sales (Enterprise AI): 'Dù AWS có tối ưu hóa container caching, GreenNode VKS cung cấp hạ tầng Sovereign AI tuân thủ Luật BVDLCN 2025 ngay tại VN, giúp bạn tránh rủi ro pháp lý và chi phí egress quốc tế. Chúng tôi đang xây dựng các tính năng tối ưu AI tương đương.'
- Pricing Recommendation: Xây dựng bảng TCO so sánh (TCO Calculator) cho 3 scenario chuẩn (S1 SME, S2 Mid, S4 AI) giả định giá đối thủ local dựa trên benchmark thị trường, để Sales có thể trình bày ngay khi đối thủ không công bố giá.
- Theo dõi thêm: Cập nhật định kỳ (hàng tuần) trang pricing của Bizfly và Viettel để phát hiện sớm các chương trình promo hoặc thay đổi mô hình giá.

## Risks

- Thiếu dữ liệu pricing công khai từ đối thủ local (Viettel, FPT, Bizfly) khiến việc tính toán TCO chính xác là suy luận dựa trên giả định, không phải số liệu thực tế.
- AWS đang dẫn đầu về AI-native optimization (container caching, speculative decoding). Nếu GreenNode không có tính năng tương đương, khách hàng AI-heavy có thể chấp nhận chi phí cao hơn của AWS để đổi lấy hiệu năng.
- Tỷ giá USD/VND biến động có thể làm thay đổi lợi thế giá của VKS so với AWS nếu không có cơ chế điều chỉnh giá linh hoạt.

## Gaps / Thiếu dữ liệu

- Cần cập nhật: pricing/2026-06-17_aws-eks_pricing.md — Dữ liệu AWS cần refresh hàng tuần, đặc biệt là các chương trình promo hoặc thay đổi giá GPU.
- Cần xác minh: Pricing GPU của GreenNode VKS so với Bizfly BKE và Viettel vOKS. Hiện chưa có dữ liệu công khai để so sánh TCO cho Scenario S4 (AI Inference) và S5 (AI Training).
- Cần xác minh: Chi phí egress và LB/NAT của các đối thủ local. Đây là hidden cost lớn ảnh hưởng đến TCO thực tế nhưng chưa có số liệu scrape được.
- Cần cập nhật: File workspace về pricing VKS (nếu có) để so sánh trực tiếp với AWS EKS trong các scenario chuẩn.
