# Pricing Summary — 2026-06-26

Source: weekly-digest run | Model: qwen/qwen3-5-27b

## Key Findings

- [RSS] [AWS News Blog](https://aws.amazon.com/blogs/aws/announcing-amazon-ec2-g7-instances-accelerated-by-nvidia-rtx-pro-4500-blackwell-server-edition-gpus) 2026-06-18 — AWS ra mắt EC2 G7 với GPU NVIDIA RTX PRO 4500 Blackwell, tập trung vào AI inference. Tác động: Tăng áp lực cạnh tranh về hiệu năng/giá cho workload AI inference (S4). Nếu GreenNode chưa có GPU thế hệ mới tương đương, sẽ khó cạnh tranh về TCO cho các workload AI cao cấp, buộc phải định vị dựa trên yếu tố chủ quyền dữ liệu (Sovereign) thay vì chỉ giá phần cứng.
- [RSS] [AWS Containers Blog](https://aws.amazon.com/blogs/containers/amazon-eks-now-supports-control-plane-egress-through-your-vpc) 2026-06-22 — AWS công bố tính năng 'customer-routed control plane egress' cho EKS, cho phép định tuyến lưu lượng control plane qua VPC khách hàng. Tác động: Tăng áp lực về bảo mật và compliance (churn risk) cho GreenNode VKS. Đây là tính năng bắt buộc với nhiều khách hàng ngân hàng/chính phủ. Nếu GreenNode chưa có tính năng tương đương, sẽ mất điểm trong các RFP yêu cầu strict security, dù giá có thể thấp hơn.
- [RSS] [AWS HPC Blog](https://aws.amazon.com/blogs/hpc/transforming-hpc-operations-with-intelligent-workload-orchestration-on-aws) 2026-06-26 — AWS công bố giải pháp tự động hóa orchestration cho workload HPC. Tác động: Tăng áp lực cạnh tranh về khả năng tự động hóa (automation) cho các workload tính toán hiệu năng cao. Nếu GreenNode VKS chưa có công cụ orchestration tương tự, sẽ khó cạnh tranh trong phân khúc HPC/AI training (S5) về mặt TCO vận hành.
- [Workspace] greennode/2026-06-19-positioning-summary.md — GreenNode là nhà cung cấp hạ tầng AI đầu tiên được TP.HCM cấp Chứng nhận Doanh nghiệp Công nghệ cao. Tác động: Đây là lợi thế định vị (positioning) mạnh để bảo vệ biên giá (premium pricing) trong phân khúc Enterprise & Gov (Sovereign AI), nơi khách hàng ưu tiên compliance (Luật BVDLCN 2025) hơn là giá list price thấp nhất.
- [Workspace] greennode/2026-05-20_greennode-vks_product-overview.md — GreenNode VKS có 3 region tại VN (HCM, HAN, BKK) và hỗ trợ Cilium VPC Native. Tác động: Lợi thế về độ trễ (latency) và egress cost cho khách hàng nội địa so với Hyperscaler (thường phải egress qua Singapore/Global). Đây là điểm mấu chốt để tính toán TCO thấp hơn cho các workload data-heavy, dù compute price có thể cao hơn.

## Recommended Actions

- Talk Track cho Sales: Nhấn mạnh 'Sovereign AI' và 'Data Residency' là yếu tố quyết định TCO thực tế (bao gồm chi phí tuân thủ pháp luật, rủi ro pháp lý) thay vì chỉ so sánh giá compute/giờ. Sử dụng chứng nhận SOC 2 Type 2 và Doanh nghiệp Công nghệ cao làm bằng chứng.
- Pricing Recommendation: Không cạnh tranh trực tiếp về giá list price cho GPU mới (Blackwell) nếu chưa có phần cứng tương đương. Thay vào đó, tập trung vào gói 'Reserved' hoặc 'Committed Use' cho các workload AI inference dài hạn, kèm theo cam kết hỗ trợ kỹ thuật (support) và tối ưu hóa egress nội địa.
- Theo dõi thêm: Cập nhật ngay lập tức pricing và tính năng của AWS EKS (Control Plane Egress) và FPT Cloud để đánh giá lại khả năng đáp ứng RFP của khách hàng ngân hàng/chính phủ.
- Phân tích TCO: Xây dựng mô hình TCO cho scenario S4 (AI Inference) và S5 (AI Training) dựa trên giả định egress cost thấp hơn của GreenNode so với AWS (do data center tại VN), bù đắp cho chênh lệch giá compute nếu có.

## Risks

- Thiếu dữ liệu pricing công khai (list price) mới nhất của GreenNode VKS và đối thủ nội địa (FPT, Viettel, Bizfly) để tính toán TCO chính xác theo scenario.
- Dữ liệu profile đối thủ (AWS EKS, FPT FKE, Viettel IDC) trong workspace đã STALE (cập nhật lần cuối 2026-06-17), không thể dùng để so sánh chi tiết tính năng/giá.
- Không có thông tin về chương trình khuyến mãi (promo) hoặc discount reserved instance mới từ các đối thủ trong 7 ngày qua.

## Gaps / Thiếu dữ liệu

- Cần cập nhật: competitors/2026-06-17_aws-eks_profile.md — dữ liệu cũ, chưa có thông tin pricing mới cho tính năng EKS Auto Mode và Control Plane Egress.
- Cần cập nhật: competitors/2026-06-17_fpt-cloud-fke_profile.md — thiếu dữ liệu pricing và tính năng mới của FPT Cloud.
- Cần cập nhật: competitors/2026-06-17_viettel-idc-kubernetes_profile.md — thiếu dữ liệu pricing và tính năng mới của Viettel IDC.
- Thiếu dữ liệu pricing công khai cho GPU Blackwell (G7) của AWS để ước tính TCO cho scenario AI Inference (S4).
- Thiếu thông tin về chính sách egress pricing của GreenNode VKS so với AWS (inter-region/internet) để tính toán TCO cho workload data-heavy.
