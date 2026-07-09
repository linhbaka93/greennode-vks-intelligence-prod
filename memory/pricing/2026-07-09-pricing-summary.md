# Pricing Summary — 2026-07-09

Source: competitor-monitor run | Model: qwen/qwen3-5-27b

## Key Findings

- [RSS] [AWS Containers Blog](https://aws.amazon.com/blogs/containers/announcing-amazon-eks-rollback-for-safe-and-reliable-management-of-cluster-upgrades) 2026-07-01 — AWS ra mắt EKS Version Rollback (rollback upgrade K8s trong 7 ngày không rebuild cluster). Tác động: Giảm rủi ro downtime khi upgrade, giảm chi phí vận hành khắc phục sự cố. GreenNode nên: Đánh giá quy trình upgrade VKS; nếu chưa có rollback tự động, cần công bố SLA recovery time hoặc roadmap tính năng tương đương để tránh churn khách hàng Enterprise/Gov.
- [RSS] [CNCF Blog](https://www.cncf.io/blog/2026/07/09/navigating-the-ingress-nginx-retirement) 2026-07-09 — CNCF thông báo retirement của ingress-nginx controller từ tháng 3/2026, cảnh báo rủi ro CVE unpatched. Tác động: Khách hàng dùng ingress-nginx cũ sẽ phát sinh chi phí migration bắt buộc. GreenNode nên: Đưa ra gói hỗ trợ migration managed service cho VKS như một upsell opportunity để giữ chân khách hàng đang lo ngại bảo mật.
- [Scrape] [Viettel VOKS](https://viettelcloud.vn/san-pham/kubernetes) 2026-07-09 — Snapshot trang sản phẩm Viettel VOKS chỉ chứa CSS/HTML header, không trích xuất được bảng giá. Tác động: Không thể so sánh trực tiếp giá compute/networking. GreenNode nên: Yêu cầu Sales Ops cung cấp battlecard pricing mới nhất từ đối thủ vì public scrape không đủ tin cậy.
- [RSS] [Bizfly Cloud News](https://bizflycloud.vn/tin-tuc/ai-giam-sat-sla-nhac-viec-va-theo-doi-trach-nhiem-20260708150949689.htm) 2026-07-08 — Bizfly công bố loạt tính năng AI giám sát SLA và phân tích phản hồi khách hàng. Tác động: Đối thủ nội địa đang đóng gói AI features vào hạ tầng, có thể định giá premium cho giải pháp 'AI-ready'. GreenNode nên: Xem xét bundling AI governance tools vào gói VKS Enterprise để tăng perceived value thay vì chỉ bán compute.
- [Workspace] [greennode/2026-05-20_greennode-vks_product-overview.md] — Hồ sơ sản phẩm VKS cập nhật đến 2026-05-20, đề cập 3 region (HCM, HAN, BKK) và CNI options. Tác động: Dữ liệu giá có thể đã stale (>60 ngày). GreenNode nên: Refresh pricing sheet từ Finance trước khi chạy TCO model cho deal Q3/Q4.

## Recommended Actions

- Talk Track: Nhấn mạnh 'Total Cost of Compliance' thay vì chỉ 'Compute Price'. Với khách hàng Gov/Bank, chi phí tuân thủ Luật BVDLCN 2025 và Data Residency quan trọng hơn chênh lệch $0.01/hour so với Hyperscaler.
- Pricing Recommendation: Đề xuất gói 'VKS Sovereign Bundle' bao gồm Control Plane Egress routing (nếu có) + Migration Support cho Ingress-NGINX để tạo khác biệt giá trị.
- Internal Action: Yêu cầu Product Team cung cấp bảng giá mới nhất (July 2026) và cấu trúc Reserved Instances để xây dựng TCO Model S2/S3 chuẩn xác.
- Monitoring: Theo dõi AWS EKS Rollback feature; nếu VKS chưa có, cần ghi rõ trong RFP response về quy trình manual rollback và thời gian dự kiến.

## Risks

- Dữ liệu giá đối thủ không khả dụng trong evidence bundle (scrape snippets chỉ chứa CSS/HTML).
- Hồ sơ giá GreenNode VKS trong memory có thể đã stale (cập nhật lần cuối 2026-05-20).
- Thiếu thông tin về discount structure (Reserved/Savings Plans) của đối thủ nội địa để tính TCO thực tế.

## Gaps / Thiếu dữ liệu

- Cần cập nhật: Bảng giá niêm yết VND/USD của FPT Cloud, Bizfly Cloud, Viettel IDC cho Kubernetes Service (Scrape thất bại lấy nội dung giá).
- Cần cập nhật: Pricing sheet nội bộ GreenNode VKS (tính đến 2026-07-09) để normalize đơn vị tiền tệ và VAT.
- Cần xác minh: Chi tiết hidden cost (Egress, LB, NAT Gateway) của đối thủ nội địa vì thường không công khai rõ ràng trên web.
