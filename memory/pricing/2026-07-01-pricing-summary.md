# Pricing Summary — 2026-07-01

Source: monthly-brief run | Model: qwen/qwen3-5-27b

## Key Findings

- [RSS] [AWS Containers Blog](https://aws.amazon.com/blogs/containers/faster-nodes-smarter-scaling-whats-new-inside-amazon-elastic-kubernetes-service-amazon-eks-auto-mode) 2026-06-23 — AWS cải tiến EKS Auto Mode giảm overhead vận hành. Tác động: Tăng áp lực cạnh tranh về TCO vận hành cho GreenNode VKS. Hành động: Đánh giá lại các tính năng automation của VKS để so sánh lợi ích giảm nhân sự DevOps.
- [RSS] [Vietnam.vn](https://news.google.com/rss/articles/CBMijwFBVV95cUxQUF9HNTZhVFREd0p4TWY5S0JEOEZTc09kTkQxVzg0MlRrZWQwWWRySF9vRmsyS3RfQmJsYnY2azRMazNsME9MSVo5eTR4SUxHUzc2dUNCUTdvYXBiOS11T0IyemU3eDBhWFV1aGNWaW9YZWJMQVRKbTJySVFpaW9YQjVQSmpMbFFrUmF2VU5Fdw?oc=5) 2026-06-27 — CMC Cloud hợp tác chính phủ số Hà Nội. Tác động: Khẳng định cuộc đua Sovereign Cloud không chỉ là giá mà là quan hệ đối tác chiến lược. Hành động: Sales cần nhấn mạnh chứng nhận Doanh nghiệp Công nghệ cao của GreenNode khi đấu thầu Gov/Enterprise.
- [Workspace] greennode/2026-05-20_greennode-vks_product-overview.md — Hồ sơ sản phẩm VKS cập nhật tháng 5/2026. Tác động: Dữ liệu giá có thể đã cũ (>30 ngày). Hành động: Cần xác minh bảng giá hiện hành trước khi dùng cho RFP Q3.

## Recommended Actions

- Talk Track: Khi khách hỏi giá, chuyển trọng tâm sang TCO toàn phần (bao gồm chi phí tuân thủ pháp lý BVDLCN 2025) thay vì chỉ so sánh giá compute giờ.
- Internal Check: Yêu cầu Product Team xác nhận lại bảng giá VKS và các chương trình Reserved Instance (nếu có) trước 15/07/2026.
- Competitor Intel: Thu thập brochure giá của CMC Cloud sau tin hợp tác Hà Nội để đánh giá mức giá tham chiếu cho segment Gov.

## Risks

- Dữ liệu giá cụ thể (USD/VND/giờ) không có trong evidence bundle hoặc memory context mới nhất.
- Hồ sơ sản phẩm VKS trong memory có timestamp tháng 5/2026, có nguy cơ stale (>30 ngày) so với thời điểm hiện tại (01/07/2026).
- Không có thông tin về discount/reserved instance cho đối thủ nội địa (FPT, Viettel) trong feed này.

## Gaps / Thiếu dữ liệu

- Cần cập nhật: Bảng giá public VKS mới nhất (tháng 6/2026) — hiện tại chỉ có hồ sơ tháng 5.
- Cần thu thập: Pricing page của FPT Cloud và Bizfly Cloud cho Managed K8s để so sánh delta.
- Cần xác minh: Chi tiết 'cost-optimized' trong bài viết AWS Nova 2 Lite + Claude (liệu có giảm giá model hay chỉ tối ưu kiến trúc?).
- Thiếu dữ liệu: Egress fee và LB cost của GreenNode so với AWS Local Zone Hanoi (nếu có).
