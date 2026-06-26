# Pricing Summary — 2026-06-26

Source: competitor-monitor run | Model: qwen/qwen3-5-27b

## Key Findings

- [RSS] [AWS Containers Blog](https://aws.amazon.com/blogs/containers/faster-nodes-smarter-scaling-whats-new-inside-amazon-elastic-kubernetes-service-amazon-eks-auto-mode) 2026-06-23 — AWS nâng cấp EKS Auto Mode với tối ưu hóa tự động cho runtime, compute, storage, networking. Tác động: ⚠️ GreenNode VKS đối mặt với áp lực TCO nếu không có cơ chế tự động hóa tương đương để giảm chi phí vận hành (OPEX) cho khách hàng. Khách hàng có thể chuyển sang AWS nếu thấy lợi thế về hiệu quả chi phí từ tự động hóa.
- [RSS] [AWS Containers Blog](https://aws.amazon.com/blogs/containers/amazon-eks-now-supports-control-plane-egress-through-your-vpc) 2026-06-22 — AWS EKS cho phép định tuyến traffic control plane qua VPC khách hàng (Private Link). Tác động: ❌ Feature gap nghiêm trọng về bảo mật. GreenNode VKS đang thua thế trong các deal Enterprise/Gov yêu cầu control plane traffic không ra internet. Nếu GreenNode không có giải pháp tương đương, khách hàng sẽ chấp nhận chi phí cao hơn của AWS để đổi lấy bảo mật.
- [RSS] [AWS News Blog](https://aws.amazon.com/blogs/aws/announcing-amazon-ec2-g7-instances-accelerated-by-nvidia-rtx-pro-4500-blackwell-server-edition-gpus) 2026-06-18 — AWS GA instance G7 với GPU NVIDIA RTX PRO 4500 Blackwell. Tác động: ⚠️ Feature gap về phần cứng AI. AWS có lợi thế hiệu năng/giá cho workload AI inference nặng. GreenNode cần rà soát roadmap GPU (A100/H100/Blackwell) để tránh mất khách hàng cần performance tối đa.
- [Workspace] greennode/2026-05-20_greennode-vks_product-overview.md — GreenNode VKS có lợi thế về Data Residency tuyệt đối tại VN (HCM, HAN, BKK) và hỗ trợ Private Cluster với IP Whitelist. Tác động: ✅ Đây là điểm định vị giá trị chính (Value-based pricing) để bù đắp cho các feature gap về tự động hóa và phần cứng mới so với AWS. Khách hàng Gov/Finance sẽ ưu tiên tuân thủ pháp lý hơn là tối ưu chi phí nhỏ.

## Recommended Actions

- Talk Track cho Sales: Nhấn mạnh 'Data Residency & Compliance' là yếu tố quyết định (must-have) cho khách hàng Gov/Finance, không thể thay thế bằng giá rẻ hay tính năng tự động hóa của AWS. 'Chúng tôi không chỉ là Kubernetes, chúng tôi là hạ tầng tuân thủ Luật BVDLCN 2025.'
- Pricing Recommendation: Đề xuất mô hình 'Compliance Premium' cho các cluster yêu cầu Private Link/Control Plane Isolation. Nếu chưa có tính năng này, cần đẩy nhanh roadmap hoặc đề xuất giải pháp workaround (VPC Endpoint) và định giá như một add-on bảo mật cao cấp.
- Theo dõi thêm: Rà soát roadmap GPU của GreenNode để đối phó với AWS G7 (Blackwell). Nếu không có GPU mới, cần định vị lại vào phân khúc AI Inference vừa và nhỏ (SME) hoặc Training nhẹ, tránh cạnh tranh trực tiếp về performance với AWS.
- Hành động nội bộ: Yêu cầu Product Team cung cấp TCO so sánh giữa VKS và AWS EKS Auto Mode dựa trên giả định usage pattern cụ thể (S1-S5) để chuẩn bị cho các cuộc đấu thầu Q3/Q4.

## Risks

- Dữ liệu pricing cụ thể (số tiền, discount, cấu hình giá) trong workspace đã quá hạn (STALE > 30 ngày), không thể dùng để tính toán TCO chính xác.
- Thiếu dữ liệu về giá GPU Blackwell của AWS và giá GPU hiện tại của GreenNode để so sánh trực tiếp.
- Không có thông tin về chính sách Reserved Instances hoặc Committed Use Discount mới của đối thủ trong 3 ngày qua.

## Gaps / Thiếu dữ liệu

- Cần cập nhật: pricing/2026-06-26-pricing-summary.md — Dữ liệu pricing hiện tại chưa có số liệu mới, cần scrape lại trang giá của AWS, FPT, Viettel, Bizfly.
- Cần xác minh: Giá GPU Blackwell (RTX PRO 4500) của AWS và thời gian ra mắt tại VN của GreenNode.
- Cần xác minh: Chi phí cụ thể của tính năng 'customer-routed control plane egress' trên AWS EKS (có tính phí thêm hay không).
- Cần cập nhật: competitors/2026-06-17_*_profile.md — Các file profile đối thủ đã STALE, không dùng được để so sánh cấu hình giá.
