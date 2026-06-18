# Pricing Summary — 2026-06-18

Source: competitor-monitor run | Model: qwen/qwen3-5-27b

## Key Findings

- [RSS] [AWS News Blog](https://aws.amazon.com/blogs/aws/announcing-amazon-ec2-g7-instances-accelerated-by-nvidia-rtx-pro-4500-blackwell-server-edition-gpus) 2026-06-18 — AWS ra mắt EC2 G7 instances với GPU NVIDIA RTX PRO 4500 Blackwell. Tác động tới GreenNode: ❌ Rủi ro về feature gap cho workload AI inference. AWS cung cấp phần cứng mới nhất ngay lập tức, trong khi GreenNode cần xác nhận roadmap GPU tương đương để cạnh tranh về hiệu năng/giá cho khách hàng cần training/inference nặng.
- [RSS] [AWS News Blog](https://aws.amazon.com/blogs/machine-learning/introducing-container-caching-in-amazon-sagemaker-ai-for-faster-model-scaling) 2026-06-16 — AWS SageMaker AI giới thiệu container caching giúp giảm latency scale-out lên đến 2x. Tác động tới GreenNode: ❌ Rủi ro TCO cho AI Inference (S4). Khách hàng chạy GenAI sẽ thấy chi phí vận hành và latency thấp hơn trên AWS nếu không cần data residency VN. GreenNode cần đánh giá khả năng tối ưu hóa container startup time để bù đắp.
- [Workspace] [pricing/2026-06-17_aws-eks_pricing.md] 2026-06-17 — AWS EKS tính phí Control Plane $0.10/giờ (~73 USD/tháng). Tác động tới GreenNode: ✅ Cơ hội định vị cho SME. GreenNode VKS có thể dùng chính sách 'Control Plane miễn phí' (nếu áp dụng) để tạo lợi thế TCO rõ rệt cho các cluster nhỏ, nơi chi phí cố định này chiếm tỷ trọng lớn.
- [Scrape] Viettel Cloud | https://viettelcloud.vn/san-pham/kubernetes | fetched_at=2026-06-18 — Trang sản phẩm vOKS không hiển thị bảng giá công khai, chỉ có nút 'Liên hệ'. Tác động tới GreenNode: ✅ Cơ hội thu hút SME. Sự thiếu minh bạch của đối thủ Tier 1 (Viettel) tạo khoảng trống cho GreenNode tiếp cận khách hàng SME cần dự toán chi phí nhanh và rõ ràng.
- [Scrape] FPT Cloud | https://fptcloud.com/kubernetes | fetched_at=2026-06-18 — Trang FKE không có bảng giá chi tiết, chiến lược 'contact-only'. Tác động tới GreenNode: ✅ Cơ hội định vị 'Transparent Pricing'. GreenNode có thể nhấn mạnh vào bảng giá online và TCO calculator để thu hút khách hàng không muốn đi qua quy trình sales phức tạp.
- [RSS] [Vietnam.vn](https://news.google.com/rss/articles/CBMikgFBVV95cUxQV2ExNGdzR1BneXhBNUhxMDNVY3dMZXhlUGlvcWFBYUk2OVZZdFJqTUZuY3NzdWUtWHZvUTJvZW1rZElGSWRzendwNlFfVEdNMjRoVUI2eExHeHQxTUtUWjJnaGxEdHlhSjdmM2UzdDhCVVlzZ3A4YldMcHZ5QmRUS0ZKWmpzWVpZX1hFVGdSd2Y0QQ?oc=5) 2026-06-17 — MSB Bank hợp tác với GreenNode vận hành hàng trăm ứng dụng AI. Tác động tới GreenNode: ✅ Proof of Value cho Enterprise. Dù chưa có số liệu giá, đây là bằng chứng thực tế về khả năng vận hành quy mô lớn, giúp GreenNode đàm phán giá tốt hơn cho các deal Enterprise tương lai so với đối thủ chưa có case study tương tự.

## Recommended Actions

- Talk Track cho Sales (SME): Nhấn mạnh 'Zero Control Plane Cost' so với AWS ($73/tháng) và 'Transparent Pricing' so với Viettel/FPT (phải chờ báo giá). Sử dụng TCO calculator online để chứng minh tiết kiệm ngay lập tức cho các cluster nhỏ.
- Talk Track cho Sales (Enterprise AI): Thừa nhận AWS có phần cứng mới nhất (G7), nhưng nhấn mạnh 'Data Sovereignty' (Luật BVDLCN 2025) và 'Low Latency Onshore' là yếu tố bắt buộc. Đề xuất giải pháp hybrid: Training trên AWS (nếu cần GPU mới nhất) nhưng Inference/Production trên VKS để tối ưu chi phí và tuân thủ.
- Product/Finance: Ưu tiên công khai bảng giá GPU và Egress trong vòng 2 tuần tới. Nếu không thể cạnh tranh về giá phần cứng, cần định vị lại dựa trên 'Managed AI Services' (hỗ trợ vận hành, tối ưu hóa container) để bù đắp chi phí phần cứng.
- Marketing: Tận dụng case study MSB Bank để chứng minh khả năng vận hành quy mô lớn, nhưng cần xin phép trích dẫn số liệu cụ thể (số lượng node, tiết kiệm chi phí) để tăng độ tin cậy.

## Risks

- Thiếu dữ liệu pricing công khai về GPU và Egress của GreenNode VKS, không thể tính toán TCO chính xác cho Scenario S4 (AI Inference) và S5 (AI Training).
- AWS đang cải thiện hiệu năng inference (container caching, speculative decoding) có thể làm giảm lợi thế giá của GreenNode nếu khách hàng không bị ràng buộc bởi data residency.
- Đối thủ local (Viettel, FPT) có thể áp dụng chiết khấu sâu (20-40%) cho Enterprise mà không công khai, làm giảm hiệu quả của chiến lược 'transparent pricing' của GreenNode ở phân khúc lớn.

## Gaps / Thiếu dữ liệu

- Cần cập nhật: pricing/2026-06-17_aws-eks_pricing.md — Dữ liệu AWS cần refresh định kỳ, đặc biệt là giá GPU mới (G7 instances) chưa có trong snapshot.
- Cần xác minh: Giá GPU node pool của GreenNode VKS (nếu có) và chính sách egress fee để so sánh TCO với AWS G7 và local competitors.
- Cần xác minh: Chi tiết hợp đồng MSB Bank (số lượng node, loại instance, mức giá) để làm case study định lượng cho sales.
- Cần cập nhật: Bảng giá chính thức của Bizfly BKE (có GPU node pool) để so sánh trực tiếp với VKS.
