# Pricing Summary — 2026-07-01

Source: monthly-brief run | Model: qwen/qwen3-5-27b

## Key Findings

- [RSS] [AWS Containers Blog](https://aws.amazon.com/blogs/containers/faster-nodes-smarter-scaling-whats-new-inside-amazon-elastic-kubernetes-service-amazon-eks-auto-mode) 2026-06-23 — AWS nâng cấp EKS Auto Mode tự động hóa runtime/compute/storage/networking. Tác động: Giảm chi phí vận hành (Ops Cost) cho khách hàng AWS; GreenNode VKS nếu thiếu tự động hóa tương đương sẽ thua về TCO tổng thể dù giá compute ngang bằng. Hành động: Đánh giá roadmap tự động hóa cluster scaling của VKS.
- [RSS] [AWS News Blog](https://aws.amazon.com/blogs/aws/announcing-amazon-ec2-g7-instances-accelerated-by-nvidia-rtx-pro-4500-blackwell-server-edition-gpus) 2026-06-18 — AWS GA instance G7 với GPU NVIDIA RTX PRO 4500 Blackwell. Tác động: Tạo lợi thế hiệu năng/giá cho AI Inference nặng trên AWS; GreenNode mất cơ hội deal AI cao cấp nếu không có GPU thế hệ mới hoặc phải chấp nhận margin thấp hơn để bù phần cứng cũ. Hành động: Rà soát inventory GPU hiện tại và kế hoạch upgrade Blackwell.
- [RSS] [FPT Cloud Blog](https://fptcloud.com/dung-thu-chi-0d-nhan-03-uu-dai-cung-fpt-cloud) 2026-06-04 — FPT Cloud tung chương trình dùng thử 0 đồng kèm ưu đãi. Tác động: Tín hiệu cạnh tranh giá trực tiếp ở phân khúc SMB/Startup; áp lực giảm giá entry-level cho GreenNode VKS. Hành động: Xem xét gói Free Tier hoặc Promo ngắn hạn cho SME để giữ thị phần.
- [Workspace] greennode/2026-06-26-positioning-summary.md — GreenNode được TP.HCM cấp Chứng nhận Doanh nghiệp Công nghệ và hợp tác MSB Bank. Tác động: Khẳng định vị thế Sovereign AI, cho phép định giá premium cho segment Gov/Finance bất chấp feature gap kỹ thuật. Hành động: Nhấn mạnh 'Compliance & Data Residency' trong talk track pricing thay vì chỉ so sánh giá list.

## Recommended Actions

- Talk Track Sales: Khi khách hỏi giá, chuyển trọng tâm sang TCO bao gồm chi phí tuân thủ (compliance cost) và rủi ro pháp lý khi dùng hyperscaler global, thay vì chỉ so sánh giá giờ chạy máy ảo.
- Internal Task: Yêu cầu Product Team cung cấp bảng giá VKS mới nhất (Q3 2026) và roadmap GPU Blackwell để cập nhật battlecard.
- Pricing Strategy: Đề xuất gói 'Sovereign Bundle' (VKS + Compliance Audit Support) để gia tăng giá trị cảm nhận cho khách hàng Gov/Bank.
- Monitoring: Theo dõi sát sao các chương trình promo của FPT/Bizfly trong 30 ngày tới để phản ứng kịp thời.

## Risks

- Thiếu bảng giá niêm yết (Price List) cập nhật của GreenNode VKS, AWS, FPT, Bizfly để tính toán delta chính xác.
- Dữ liệu workspace về VKS Product Overview (2026-05-20) có thể đã cũ so với digest tháng 6/2026.
- Không có thông tin về FX rate VND/USD tại thời điểm phân tích để normalize giá.

## Gaps / Thiếu dữ liệu

- Cần thu thập bảng giá chi tiết (Compute, Storage, Egress, LB) của GreenNode VKS, AWS (ap-southeast-1), FPT Cloud, Bizfly Cloud.
- Cần làm rõ mức discount Reserved Instances/Committed Use của từng nhà cung cấp.
- Cần xác minh nội dung chi tiết bài 'price reductions' của AWS để biết scope ảnh hưởng (EC2, S3, hay EKS).
- File workspace `greennode/2026-05-20_greennode-vks_product-overview.md` cần kiểm tra freshness (cũ >30 ngày).
