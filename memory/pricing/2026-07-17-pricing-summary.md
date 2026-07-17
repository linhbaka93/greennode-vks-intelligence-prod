# Pricing Summary — 2026-07-17

Source: weekly-digest run | Model: qwen/qwen3-5-27b

## Key Findings

- [RSS] [FPT Cloud](https://fptcloud.com/uu-dai-len-cloud-tang-03-thang-su-dung-dich-vu-chiet-khau-len-den-20-trieu-dong) 2026-07-14 — FPT tung ưu đãi tặng 03 tháng sử dụng dịch vụ & chiết khấu lên đến 20 triệu đồng. Tác động: Áp lực giảm giá trực tiếp cho segment SME/Mid-market; khách hàng nhạy cảm về chi phí ban đầu có thể chuyển đổi. GreenNode nên: Chuẩn bị counter-offer tập trung vào TCO dài hạn hoặc gói cam kết (reserved) thay vì discount ngắn hạn.
- [RSS] [AWS Containers Blog](https://aws.amazon.com/blogs/containers/announcing-amazon-eks-rollback-for-safe-and-reliable-management-of-cluster-upgrades) 2026-07-01 — AWS ra mắt EKS Version Rollback (rollback upgrade K8s trong 7 ngày). Tác động: Nâng tiêu chuẩn 'operational safety' cho Managed K8s Enterprise. Nếu VKS chưa có tính năng tương đương, đây là feature gap làm giảm willingness-to-pay của khách hàng Gov/Bank. GreenNode nên: Đánh giá quy trình upgrade VKS và ghi rõ SLA recovery time nếu chưa có rollback tự động.
- [RSS] [GreenNode Blog](https://greennode.ai/blog/greennode-launches-han-1b-availability-zone-to-expand-ai-cloud-infrastructure) 2026-07-14 — GreenNode ra mắt Availability Zone HAN-1B. Tác động: Mở rộng khả năng Multi-AZ/DR tại VN, tăng giá trị cho workload yêu cầu High Availability. GreenNode nên: Đưa ra pricing model bundle cho Multi-AZ deployment để tối ưu doanh thu từ segment Enterprise.
- [RSS] [CNCF Blog](https://www.cncf.io/blog/2026/07/10/where-should-ai-workloads-run-a-sovereign-and-sensible-approach) 2026-07-10 — CNCF nhấn mạnh xu hướng 'Sovereign AI' cho doanh nghiệp. Tác động: Củng cố luận điểm định vị Sovereign Cloud của GreenNode, giúp biện minh cho mức giá cao hơn hyperscaler do tuân thủ pháp lý (Luật BVDLCN 2025). GreenNode nên: Tích hợp trích dẫn này vào tài liệu GTM để chứng minh tính đúng đắn của chiến lược Sovereign Cloud.

## Recommended Actions

- Talk Track Sales: Khi khách hàng so sánh giá với FPT, nhấn mạnh 'TCO toàn diện' bao gồm chi phí tuân thủ pháp lý (compliance cost) và rủi ro downtime, thay vì chỉ so sánh giá giờ máy ảo. Sử dụng ưu đãi FPT làm đòn bẩy để chốt deal Reserved Commitment dài hạn.
- Pricing Recommendation: Xây dựng gói 'Multi-AZ Bundle' cho HAN-1B mới ra mắt, định giá cạnh tranh cho workload yêu cầu HA/DR để tận dụng lợi thế hạ tầng mới.
- Feature Gap Analysis: Yêu cầu Engineering đánh giá khả năng triển khai 'Cluster Upgrade Rollback' cho VKS trong Q3/Q4 để đáp ứng kỳ vọng Enterprise/Gov sau khi AWS ra mắt tính năng này.
- Data Refresh: Yêu cầu bộ phận Product/Sales Ops cung cấp bảng giá nội bộ (internal rate card) và bảng giá công khai mới nhất của đối thủ để agent có thể chạy mô hình TCO S1-S5.

## Risks

- Dữ liệu pricing cụ thể (USD/giờ, VND/tháng) cho compute, storage, egress thiếu trong evidence bundle, không thể tính toán TCO chính xác.
- Hồ sơ sản phẩm VKS trong workspace (May 2026) có thể chưa cập nhật các thay đổi giá sau khi rebrand thành GreenNode.
- Ưu đãi của FPT là ngắn hạn, không phản ánh giá niêm yết dài hạn, dễ gây hiểu lầm về cấu trúc giá cơ bản.

## Gaps / Thiếu dữ liệu

- Cần cập nhật: Bảng giá công khai (Public Price List) của GreenNode VKS, FPT SmartCloud, Bizfly Cloud cho các component: Control Plane, Compute (vCPU/RAM), Storage, Networking (LB/NAT/IP), Egress.
- Cần xác minh: Chính sách giá Reserved Instances/Committed Use Discount của GreenNode so với đối thủ.
- Cần xác minh: Chi phí ẩn (hidden costs) như Data Transfer/Egress giữa các AZ và Internet cho cả 3 nhà cung cấp.
- File workspace `greennode/2026-05-20_greennode-vks_product-overview.md` bị cắt cụt ở phần Differentiator, cần bổ sung thông tin đầy đủ về tính năng hỗ trợ.
