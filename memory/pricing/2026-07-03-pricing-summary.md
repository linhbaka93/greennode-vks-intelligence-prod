# Pricing Summary — 2026-07-03

Source: competitor-monitor run | Model: qwen/qwen3-5-27b

## Key Findings

- [Scrape] [Viettel IDC](https://viettelcloud.vn/san-pham/kubernetes) 2026-07-03 — Trang sản phẩm Kubernetes không hiển thị bảng giá công khai, chỉ chứa mã CSS/HTML giao diện. Tác động: Viettel IDC có thể đang dùng chiến lược báo giá linh hoạt theo deal lớn; GreenNode khó so sánh TCO trực tiếp từ web. GreenNode nên: Yêu cầu Sales Ops thu thập quote mẫu từ đối thủ để xây dựng battlecard.
- [RSS] [AWS Containers Blog](https://aws.amazon.com/blogs/containers/announcing-amazon-eks-rollback-for-safe-and-reliable-management-of-cluster-upgrades) 2026-07-01 — AWS ra mắt tính năng rollback phiên bản K8s trong 7 ngày mà không cần rebuild cluster. Tác động: Tiêu chuẩn 'operational safety' được nâng lên; khách hàng Gov/Bank sẽ kỳ vọng khả năng phục hồi tương tự. GreenNode nên: Đánh giá quy trình upgrade VKS; nếu chưa có rollback tự động, cần ghi rõ SLA recovery time hoặc phát triển tính năng này để giảm churn risk.
- [Workspace] [greennode/2026-07-03-positioning-summary.md] 2026-07-03 — GreenNode định vị là hạ tầng AI đầu tiên được TP.HCM cấp Chứng nhận Doanh nghiệp Công nghệ cao, tập trung vào Sovereign Cloud. Tác động: Định vị này tạo cơ sở để áp mức giá premium cho các workload nhạy cảm pháp lý (Luật BVDLCN 2025). GreenNode nên: Nhấn mạnh 'chi phí rủi ro pháp lý' khi so sánh TCO với hyperscaler, không chỉ so sánh chi phí vận hành thuần túy.
- [Scrape] [FPT Cloud](https://fptcloud.com/kubernetes) 2026-07-03 — Trang FPT Kubernetes Engine không hiển thị giá niêm yết công khai. Tác động: Thị trường Managed K8s tại VN thiếu minh bạch về giá, tạo lợi thế cho bên nắm giữ thông tin deal trước đó. GreenNode nên: Xây dựng bộ câu hỏi RFP tiêu chuẩn để buộc đối thủ tiết lộ cấu trúc giá (control plane fee, egress rate) trong quá trình đấu thầu.

## Recommended Actions

- Talk Track: Khi khách hàng hỏi giá, chuyển hướng sang 'Total Cost of Compliance'. Giải thích rằng chi phí thấp hơn của đối thủ quốc tế có thể đi kèm rủi ro pháp lý (data residency) mà GreenNode loại bỏ.
- Pricing Recommendation: Đề xuất gói 'Compliance Bundle' bao gồm VKS + Audit Log + Data Residency Certification support để tách biệt khỏi cuộc đua giá compute thuần túy.
- Data Refresh: Yêu cầu team Research chạy lại scraper với headless browser (nếu cần JS render) để lấy giá từ trang đối thủ, hoặc liên hệ Sales để xin quote mẫu ẩn danh.

## Risks

- Thiếu dữ liệu giá thực tế (unit price) khiến việc phân tích TCO số học không thể thực hiện chính xác trong chu kỳ này.
- Giả định đối thủ nội địa dùng mô hình sales-led pricing có thể sai lệch nếu họ đã cập nhật bảng giá công khai nhưng scraper bị chặn nội dung động.
- Dữ liệu positioning summary có thể chưa phản ánh chính sách giá mới nhất nếu có điều chỉnh nội bộ sau tháng 6/2026.

## Gaps / Thiếu dữ liệu

- Cần thu thập bảng giá chi tiết (compute, storage, egress, control plane) của VKS, vOKS, BKE, FKE từ Sales Ops hoặc tài liệu internal.
- Cần xác minh cấu trúc phí egress (internet vs inter-region) của đối thủ để tính toán hidden cost trong TCO.
- Cần cập nhật file `greennode/2026-05-20_greennode-vks_product-overview.md` nếu có thay đổi về SKU hoặc region pricing.
