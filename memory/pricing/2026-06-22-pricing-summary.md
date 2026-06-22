# Pricing Summary — 2026-06-22

Source: competitor-monitor run | Model: qwen/qwen3-5-27b

## Key Findings

- [RSS] [AWS News Blog](https://aws.amazon.com/blogs/aws/aws-weekly-roundup-ny-summit-recap-local-zone-in-hanoi-grok-4-3-in-bedrock-price-reductions-and-more-june-22-2026) 2026-06-22 — AWS công bố giảm giá (price reductions) và mở rộng Local Zone tại Hà Nội. Tác động: Áp lực giá trực tiếp lên GreenNode nếu khách hàng không yêu cầu data residency nghiêm ngặt. GreenNode cần rà soát lại TCO cho các workload không bắt buộc onshore để tránh mất khách vào AWS do giá thấp hơn.
- [RSS] [AWS Containers Blog](https://aws.amazon.com/blogs/containers/amazon-eks-now-supports-control-plane-egress-through-your-vpc) 2026-06-22 — AWS EKS hỗ trợ định tuyến control plane egress qua VPC của khách hàng. Tác động: Giảm chi phí egress ẩn (hidden cost) cho khách hàng AWS, làm giảm lợi thế giá của GreenNode trong các kiến trúc hybrid phức tạp. GreenNode cần làm rõ chính sách egress của VKS để so sánh TCO thực tế.
- [RSS] [AWS News Blog](https://aws.amazon.com/blogs/aws/announcing-amazon-ec2-g7-instances-accelerated-by-nvidia-rtx-pro-4500-blackwell-server-edition-gpus) 2026-06-18 — AWS GA EC2 G7 với GPU Blackwell. Tác động: Feature gap về phần cứng AI inference. Nếu GreenNode chưa có Blackwell, sẽ thua về hiệu năng/giá cho các workload LLM nặng không cần data residency VN. Cần rà soát roadmap GPU để tránh mất khách hàng cần performance tối đa.
- [Scrape] Viettel Cloud | https://viettelcloud.vn/san-pham/kubernetes | fetched_at=2026-06-22 — Trang sản phẩm vOKS không hiển thị bảng giá công khai. Tác động: Viettel vẫn giữ chiến lược 'sales-led pricing' cho Enterprise. GreenNode không thể so sánh giá trực tiếp, cần tập trung vào TCO tổng thể (bao gồm support, compliance) thay vì chỉ so sánh list price.
- [Scrape] FPT Cloud | https://fptcloud.com/kubernetes | fetched_at=2026-06-22 — Trang sản phẩm FKE không hiển thị bảng giá công khai. Tác động: Tương tự Viettel, FPT dùng giá ẩn để linh hoạt đàm phán. GreenNode cần chuẩn bị battlecard TCO cho các scenario cụ thể (SME vs Enterprise) để đối phó khi khách hàng yêu cầu báo giá.
- [Scrape] Bizfly Cloud | https://bizflycloud.vn/kubernetes | fetched_at=2026-06-22 — Trang sản phẩm BKE không hiển thị bảng giá công khai. Tác động: Bizfly vẫn là đối thủ mạnh ở phân khúc SME nhưng không công khai giá. GreenNode cần theo dõi các chương trình khuyến mãi hoặc gói giá cố định nếu Bizfly thay đổi chiến lược.

## Recommended Actions

- Talk track cho Sales: Nhấn mạnh lợi thế Sovereign AI và data residency của GreenNode VKS, đặc biệt với khách hàng Enterprise/Gov. Giải thích rằng AWS Local Zone tại Hà Nội vẫn không thay thế được yêu cầu data residency nghiêm ngặt.
- Pricing recommendation: Rà soát lại TCO cho các scenario SME và Enterprise, tập trung vào hidden cost (egress, support) để làm nổi bật lợi thế giá trị của GreenNode so với AWS.
- Theo dõi thêm: Cập nhật roadmap GPU của GreenNode và so sánh với AWS G7 Blackwell để chuẩn bị chiến lược cạnh tranh cho workload AI inference.
- Theo dõi thêm: Thu thập dữ liệu pricing thực tế từ các deal đã ký để hiểu willingness-to-pay của khách hàng và điều chỉnh chiến lược giá.

## Risks

- Dữ liệu pricing của đối thủ VN (Viettel, FPT, Bizfly) không công khai, gây khó khăn cho việc so sánh TCO chính xác.
- AWS giảm giá và mở rộng Local Zone tại Hà Nội có thể làm giảm lợi thế giá của GreenNode cho các workload không bắt buộc onshore.
- Feature gap về GPU Blackwell so với AWS có thể làm mất khách hàng cần performance tối đa cho AI inference.
- Dữ liệu pricing của GreenNode VKS trong workspace có thể đã cũ (last updated 2026-05-20), cần cập nhật lại để đảm bảo chính xác.

## Gaps / Thiếu dữ liệu

- Cần cập nhật bảng giá công khai của GreenNode VKS (nếu có) hoặc chính sách giá nội bộ để so sánh với đối thủ.
- Cần xác minh chính sách egress và hidden cost của GreenNode VKS để so sánh với AWS EKS mới.
- Cần rà soát roadmap GPU của GreenNode để đánh giá khả năng cạnh tranh với AWS G7 Blackwell.
- Cần thu thập dữ liệu pricing thực tế từ các deal đã ký (win/loss) để hiểu willingness-to-pay của khách hàng.
