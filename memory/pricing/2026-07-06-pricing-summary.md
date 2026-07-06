# Pricing Summary — 2026-07-06

Source: competitor-monitor run | Model: qwen/qwen3-5-27b

## Key Findings

- [RSS] [AWS Containers Blog](https://aws.amazon.com/blogs/containers/announcing-amazon-eks-rollback-for-safe-and-reliable-management-of-cluster-upgrades) 2026-07-01 — AWS ra mắt EKS Version Rollback (rollback upgrade K8s trong 7 ngày). Tác động: Nâng tiêu chuẩn 'operational safety'. Nếu GreenNode chưa có rollback tự động, khách hàng Enterprise sẽ coi đây là rủi ro downtime khi upgrade, gây áp lực phải bù đắp bằng giá thấp hơn hoặc cam kết SLA cao hơn.
- [RSS] [AWS Containers Blog](https://aws.amazon.com/blogs/containers/amazon-eks-now-supports-control-plane-egress-through-your-vpc) 2026-06-22 — AWS cho phép định tuyến control plane egress qua VPC khách hàng. Tác động: Đây là yêu cầu bắt buộc cho nhiều ngân hàng/chính phủ. Nếu GreenNode VKS chưa hỗ trợ native, sẽ mất điểm cạnh tranh về compliance, dù giá rẻ hơn.
- [Scrape] Viettel Cloud | https://viettelcloud.vn/san-pham/kubernetes | fetched_at=2026-07-06 — Trang sản phẩm VOKS không hiển thị bảng giá công khai (snippet chỉ chứa CSS). Tác động: Đối thủ nội địa dùng mô hình sales-led pricing (giá thương lượng). GreenNode nên cân nhắc công bố bảng giá minh bạch hơn để tạo lợi thế cho SME/Mid-market, nơi họ cần dự toán nhanh.
- [Workspace] greennode/2026-05-20_greennode-vks_product-overview.md — GreenNode VKS có 3 region (HCM, HAN, BKK) và hỗ trợ Cilium VPC Native. Tác động: Lợi thế kỹ thuật về CNI hiện đại giúp giảm chi phí networking ẩn (egress/internal traffic) so với Calico truyền thống, nhưng cần làm rõ trong TCO calculation.

## Recommended Actions

- Talk Track Sales: Khi khách hỏi giá, đừng chỉ báo unit price. Hãy nhấn mạnh 'TCO Tuân thủ': Giá VKS bao gồm Data Residency + Compliance Audit Support, trong khi AWS/GCP cần thêm chi phí tư vấn pháp lý và risk mitigation.
- Pricing Recommendation: Đề xuất gói 'Compliance Bundle' cho Enterprise (bao gồm Control Plane Egress routing nếu có, hoặc tư vấn kiến trúc an toàn) để match tính năng của AWS EKS mà không cần giảm giá compute.
- Theo dõi thêm: Yêu cầu Scrape Agent target trực tiếp các URL `/pricing` hoặc `/gia-ca` của đối thủ nội địa để lấy số liệu thực tế.

## Risks

- Dữ liệu giá đối thủ thiếu: Không thể tính toán TCO chính xác do không có số liệu giá niêm yết từ Viettel/FPT/Bizfly trong evidence scrape.
- Dữ liệu GreenNode cũ: Hồ sơ sản phẩm VKS cập nhật đến 2026-05-20, có thể đã thay đổi cấu hình/giá sau 2 tháng.
- Giả định FX: So sánh TCO cần quy đổi USD/VND, tỷ giá biến động ảnh hưởng đến độ chính xác của delta giá.

## Gaps / Thiếu dữ liệu

- Cần cập nhật: memory/pricing/vks-pricing-table.md — Dữ liệu giá VKS hiện tại (July 2026) chưa có trong workspace.
- Cần fetch sâu hơn: Các trang pricing của Viettel/FPT/Bizfly thường nằm ở tab 'Giá cả' riêng biệt, scraper chỉ lấy được landing page.
- Thiếu thông tin: Chi phí egress cụ thể của GreenNode so với AWS (thường là hidden cost lớn nhất).
