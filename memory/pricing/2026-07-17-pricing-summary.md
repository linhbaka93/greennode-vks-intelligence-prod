# Pricing Summary — 2026-07-17

Source: competitor-monitor run | Model: qwen/qwen3-5-27b

## Key Findings

- [RSS] [FPT Cloud](https://fptcloud.com/uu-dai-len-cloud-tang-03-thang-su-dung-dich-vu-chiet-khau-len-den-20-trieu-dong) 2026-07-14 — FPT Cloud tung chương trình khuyến mãi trực tiếp giảm giá và tặng thời gian sử dụng. Tác động: Tạo áp lực pricing pressure ngắn hạn cho các deal SME/Mid-market đang so sánh vendor nội địa. GreenNode nên: Đánh giá lại chính sách promo Q3; nếu không match được, cần nhấn mạnh khác biệt về SLA/GPU availability để biện minh cho giá cao hơn.
- [RSS] [AWS Containers Blog](https://aws.amazon.com/blogs/containers/announcing-amazon-eks-rollback-for-safe-and-reliable-management-of-cluster-upgrades) 2026-07-01 — AWS ra mắt tính năng rollback tự động cho EKS upgrade. Tác động: Nâng tiêu chuẩn 'operational safety'. Khách hàng Enterprise sẽ kỳ vọng khả năng phục hồi nhanh khi upgrade lỗi mà không rebuild cluster. GreenNode nên: Kiểm tra quy trình upgrade VKS; nếu chưa có rollback tự động, cần ghi rõ SLA recovery time hoặc phát triển tính năng tương đương để giảm churn risk.
- [RSS] [GreenNode](https://greennode.ai/blog/greennode-launches-han-1b-availability-zone-to-expand-ai-cloud-infrastru) 2026-07-14 — GreenNode mở rộng Availability Zone HAN-1B. Tác động: Tăng khả năng cung cấp GPU onshore tại miền Bắc, giảm egress latency cho khách hàng Gov/Hà Nội. GreenNode nên: Sử dụng đây là điểm bán hàng chính cho segment Enterprise/Gov cần data residency Hà Nội, bù đắp nếu giá compute cao hơn hyperscaler.
- [Workspace] greennode/2026-05-20_greennode-vks_product-overview.md — Hồ sơ sản phẩm VKS cập nhật đến tháng 5/2026. Tác động: Dữ liệu cấu hình cơ bản (region, CNI options) vẫn dùng được nhưng thiếu thông tin giá mới nhất. GreenNode nên: Yêu cầu Sales Ops refresh bảng giá nội bộ trước khi chốt RFP Q3.

## Recommended Actions

- Sales Talk Track: Khi khách hỏi giá, chuyển hướng sang TCO tổng thể bao gồm chi phí tuân thủ (compliance cost) và rủi ro pháp lý (data residency), nơi GreenNode có lợi thế tuyệt đối so với Hyperscaler.
- Pricing Recommendation: Không match trực tiếp promo '3 tháng free' của FPT trừ khi deal lớn (>500M VND/year). Thay vào đó, đề xuất Reserved Instance discount sâu hơn cho cam kết 1-3 năm.
- Product Action: Yêu cầu Engineering đánh giá tính năng 'Cluster Upgrade Rollback' để对标 AWS EKS, giảm rào cản kỹ thuật khi bán cho Enterprise.
- Data Refresh: Yêu cầu Source Tool re-scrape trang pricing của FPT/Bizfly/Viettel với parser chuyên biệt cho bảng giá (table extraction) thay vì full page scrape.

## Risks

- Dữ liệu pricing thô (compute/storage/egress rates) của đối thủ không có trong evidence bundle hiện tại (scrape chỉ trả về CSS/HTML noise). Không thể tính toán TCO chính xác.
- Hồ sơ sản phẩm VKS trong workspace đã cũ (tháng 5/2026), có thể không phản ánh điều chỉnh giá tháng 7/2026.
- Ưu đãi của FPT là ngắn hạn (promo), không phải baseline price, tránh nhầm lẫn khi xây dựng chiến lược giá dài hạn.

## Gaps / Thiếu dữ liệu

- Cần cập nhật: Bảng giá chi tiết (USD/VND) cho Compute, Storage, Egress của FPT FKE, Bizfly BKE, Viettel VOKS — scrape hiện tại không lấy được số liệu.
- Cần xác minh: Chính sách Control Plane fee của VKS (miễn phí hay tính phí?) — không tìm thấy trong snippet memory.
- Cần làm mới: File `greennode/2026-05-20_greennode-vks_product-overview.md` — dữ liệu >30 ngày tuổi, rủi ro stale pricing.
- Thiếu dữ liệu: Chi phí egress inter-region/internet của GreenNode so với AWS/FPT để phân tích hidden cost.
