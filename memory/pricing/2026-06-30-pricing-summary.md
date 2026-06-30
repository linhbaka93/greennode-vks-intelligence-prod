# Pricing Summary — 2026-06-30

Source: competitor-monitor run | Model: qwen/qwen3-5-27b

## Key Findings

- [RSS] [AWS Containers Blog](https://aws.amazon.com/blogs/containers/amazon-eks-now-supports-control-plane-egress-through-your-vpc) 2026-06-22 — AWS công bố tính năng 'customer-routed control plane egress' cho EKS, cho phép lưu lượng control plane đi qua VPC khách hàng. Tác động: Tăng thanh chắn bảo mật (security bar), gây rủi ro churn cho GreenNode VKS nếu chưa có tính năng tương đương cho khách hàng ngân hàng/chính phủ yêu cầu strict compliance.
- [RSS] [Artificial Intelligence](https://aws.amazon.com/blogs/machine-learning/introducing-claude-sonnet-5-on-aws-anthropics-most-capable-sonnet-model) 2026-06-30 — AWS ra mắt Claude Sonnet 5 trên Bedrock. Tác động: Làm mới hệ sinh thái AI, tăng áp lực cạnh tranh về khả năng tích hợp mô hình mới nhất cho workload AI inference/training của GreenNode.
- [Scrape] viettel-voks | https://viettelcloud.vn/san-pham/kubernetes | fetched_at=2026-06-30 — Trang sản phẩm Kubernetes của Viettel Cloud không hiển thị bảng giá công khai trong nội dung scrape được (chỉ chứa CSS/boilerplate). Tác động: Không thể so sánh TCO trực tiếp với Viettel VOKS, cần xác minh lại cơ chế lấy giá.
- [Workspace] greennode/2026-05-20_greennode-vks_product-overview.md — Hồ sơ sản phẩm VKS cập nhật đến tháng 5/2026 nhấn mạnh compliance và kỹ thuật nhưng thiếu chi tiết pricing structure mới nhất. Tác động: Dữ liệu định vị giá trị có thể đã lỗi thời so với các tính năng bảo mật mới của hyperscaler.

## Recommended Actions

- Talk Track Sales: Nhấn mạnh lợi thế Sovereign Compliance (Luật BVDLCN 2025) thay vì chỉ so sánh giá compute khi khách hàng hỏi về EKS features mới của AWS.
- Product Team: Xác nhận timeline triển khai tính năng 'private control plane egress' cho VKS để giảm churn risk ở segment Ngân hàng/Chính phủ.
- Data Ops: Refresh scraping logic cho trang giá đối thủ hoặc liên hệ Sales Intel để lấy bảng giá nội bộ (nếu có) nhằm hoàn thiện TCO model.
- Pricing Strategy: Xem xét gói bundle AI (GPU + Bedrock-like access) để cạnh tranh với AWS Nova/Claude pipeline mà không cần hạ tầng GPU quá đắt đỏ.

## Risks

- Dữ liệu giá đối thủ không khả dụng do scraper bị chặn hoặc nội dung động (dynamic content) không được render.
- Hồ sơ sản phẩm GreenNode VKS trong memory có thể chưa phản ánh các điều chỉnh giá gần đây (last updated 2026-05-20).
- Thiếu thông tin về hidden cost (egress, LB) để tính toán TCO thực tế cho scenario SME/Mid/Enterprise.

## Gaps / Thiếu dữ liệu

- Cần cập nhật: memory/pricing/vks-pricing-2026.md — Dữ liệu giá cũ, chưa dùng được để tính TCO.
- Cần khắc phục: Cơ chế scrape trang giá đối thủ (Viettel/FPT/Bizfly) đang trả về HTML/CSS trống, cần thêm logic xử lý JavaScript hoặc login wall.
- Thiếu dữ liệu: Chi phí egress và support tiers của GreenNode VKS so với AWS EKS để phân tích hidden cost.
