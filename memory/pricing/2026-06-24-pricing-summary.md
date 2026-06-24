# Pricing Summary — 2026-06-24

Source: competitor-monitor run | Model: qwen/qwen3-5-27b

## Key Findings

- [RSS] [AWS Containers Blog](https://aws.amazon.com/blogs/containers/faster-nodes-smarter-scaling-whats-new-inside-amazon-elastic-kubernetes-service-amazon-eks-auto-mode) 2026-06-23 — AWS nâng cấp EKS Auto Mode (runtime, compute, storage, networking). Tác động: Tăng áp lực về hiệu quả vận hành (TCO) cho GreenNode. Khách hàng SME/Mid-market có thể yêu cầu tính năng tự động hóa tương tự để giảm chi phí vận hành, nếu GreenNode không có giải pháp tương đương, sẽ mất lợi thế về giá trị vận hành.
- [RSS] [AWS Containers Blog](https://aws.amazon.com/blogs/containers/amazon-eks-now-supports-control-plane-egress-through-your-vpc) 2026-06-22 — AWS ra mắt 'customer-routed control plane egress'. Tác động: Feature gap nghiêm trọng về bảo mật cho Enterprise/Gov. Khách hàng tài chính/chính phủ có thể từ chối GreenNode nếu không có giải pháp Private Link cho control plane, bất kể giá thấp hơn. Đây là rào cản kỹ thuật lớn hơn rào cản giá.
- [RSS] [AWS News Blog](https://aws.amazon.com/blogs/aws/announcing-amazon-ec2-g7-instances-accelerated-by-nvidia-rtx-pro-4500-blackwell-server-edition-gpus) 2026-06-18 — AWS GA GPU Blackwell (RTX PRO 4500). Tác động: Feature gap về phần cứng AI mới nhất. Nếu GreenNode chưa có Blackwell, sẽ mất lợi thế về hiệu năng/giá cho workload AI inference nặng. Cần rà soát roadmap GPU để tránh bị định vị là 'legacy' trong phân khúc AI.
- [RSS] [greennode-blog](https://greennode.ai/blog/greennode-achieves-soc-2-type2-report) 2026-06-23 — GreenNode đạt SOC 2 Type 2. Tác động: Tăng giá trị thương hiệu và khả năng thắng thầu Enterprise/Gov. Đây là 'price premium enabler' cho phép GreenNode giữ giá cao hơn đối thủ chưa có chứng nhận tương đương trong phân khúc Sovereign AI.
- [Scrape] Viettel Cloud | https://viettelcloud.vn/san-pham/kubernetes | fetched_at=2026-06-24 — Trang vOKS không hiển thị bảng giá công khai. Tác động: Viettel tiếp tục chiến lược 'contact-only pricing', tạo rào cản so sánh trực tiếp. GreenNode cần chuẩn bị battlecard so sánh TCO dựa trên cấu hình giả định (scenario-based) thay vì so sánh list price.

## Recommended Actions

- Talk Track cho Sales: Nhấn mạnh SOC 2 Type 2 và Data Residency VN như yếu tố 'must-have' cho Enterprise/Gov, không chỉ là 'nice-to-have'. Sử dụng chứng nhận này để biện minh cho giá cao hơn so với đối thủ chưa có chứng nhận tương đương.
- Pricing Recommendation: Không giảm giá list price. Thay vào đó, tập trung vào gói 'Enterprise Security Bundle' bao gồm SOC 2, Private Cluster, và hỗ trợ 24/7 để tăng giá trị cảm nhận.
- Theo dõi thêm: Rà soát roadmap GPU Blackwell và tính năng Control Plane Egress. Nếu không có trong 6 tháng tới, cần chuẩn bị chiến lược 'feature parity' hoặc 'workaround' để đối phó với yêu cầu của khách hàng Enterprise.
- Theo dõi thêm: Đánh giá khả năng triển khai tính năng tự động hóa tương tự EKS Auto Mode để giảm TCO vận hành cho khách hàng SME/Mid-market.

## Risks

- Dữ liệu pricing công khai của đối thủ (Viettel, FPT, Bizfly) không có sẵn, gây khó khăn cho việc so sánh TCO chính xác.
- Feature gap về Control Plane Egress và GPU Blackwell có thể khiến GreenNode mất thầu Enterprise/AI nếu không có giải pháp thay thế hoặc roadmap rõ ràng.
- Áp lực từ EKS Auto Mode có thể buộc khách hàng SME yêu cầu tính năng tự động hóa tương tự, ảnh hưởng đến định vị giá trị của VKS.

## Gaps / Thiếu dữ liệu

- Cần cập nhật: pricing list price của GreenNode VKS, AWS EKS, Viettel vOKS, FPT FKE, Bizfly BKE — dữ liệu cũ, chưa dùng được để tính TCO mới.
- Cần xác minh: Roadmap GPU Blackwell của GreenNode và thời gian ra mắt tại VN.
- Cần xác minh: Khả năng triển khai Private Link cho control plane của GreenNode VKS.
- Cần xác minh: Chi tiết tính năng tự động hóa (Auto Mode) của GreenNode VKS so với AWS.
