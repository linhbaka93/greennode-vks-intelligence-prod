# Pricing Summary — 2026-06-16

Source: competitor-monitor run | Model: google/gemma-4-31b-it

## Key Findings

- [Workspace] [pricing/2026-06-17_aws-eks_pricing.md] 2026-06-17 — AWS EKS thu phí Control Plane $0.10/giờ (~73 USD/tháng), tạo ra một baseline chi phí cố định mà VKS có thể dùng để định vị 'miễn phí' hoặc 'tối ưu hơn' cho các cluster nhỏ/SME.
- [Suy luận] Dựa trên [competitors/2026-06-17_fpt-cloud-fke_profile.md] và [competitors/2026-06-17_viettel-voks_profile.md] — Việc FPT và Viettel không công khai pricing chi tiết cho thấy chiến lược sales-led cho Enterprise, tạo cơ hội cho GreenNode thu hút SME bằng bảng giá minh bạch và dễ dự báo TCO.
- [Suy luận] Dựa trên [regulatory/vietnam-compliance.md] — Việc tuân thủ Luật BVDLCN 2025 khiến chi phí chuyển đổi (switching cost) từ AWS sang VKS trở nên thấp hơn so với rủi ro pháp lý (compliance risk), làm giảm độ nhạy cảm về giá của phân khúc Gov/Enterprise.

## Recommended Actions

- Talk track cho Sales: 'Thay vì trả ~2 triệu VND/tháng chỉ cho Control Plane như EKS, khách hàng sử dụng VKS có thể tối ưu chi phí này để đầu tư vào Compute/GPU, đồng thời đảm bảo tuân thủ Luật BVDLCN 2025'.
- Pricing Recommendation: Xây dựng gói 'Sovereign AI Starter' bundle (K8s + GPU Node + Local Storage) với giá cố định theo tháng để đánh vào phân khúc SME đang muốn thử nghiệm AI nhưng ngại chi phí biến đổi của AWS.

## Risks

- Dữ liệu pricing của Viettel vOKS và FPT FKE hiện tại là 'contact-only', không có số liệu cụ thể để tính TCO chính xác.
- Giả định tỷ giá 26,200 VND/USD có thể biến động, ảnh hưởng đến so sánh TCO với AWS.

## Gaps / Thiếu dữ liệu

- Thiếu bảng giá chi tiết (Compute/Storage/Egress) của Viettel vOKS, FPT FKE và Bizfly BKE để thực hiện normalize TCO theo Scenario S1-S5.
- Thiếu dữ liệu pricing cụ thể của GreenNode VKS trong workspace để tính delta so với đối thủ.
