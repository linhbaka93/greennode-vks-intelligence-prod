# Pricing Summary — 2026-06-29

Source: competitor-monitor run | Model: qwen/qwen3-5-27b

## Key Findings

- [RSS] [AWS HPC Blog](https://aws.amazon.com/blogs/hpc/transforming-hpc-operations-with-intelligent-workload-orchestration-on-aws) 2026-06-26 — AWS công bố giải pháp tự động hóa orchestration cho HPC, giảm chi phí vận hành thủ công. Tác động: ⚠️ GreenNode VKS có thể thua về TCO cho workload HPC/AI nặng nếu không có tính năng tự động hóa tương đương, dù giá list có thể thấp hơn. Khách hàng sẽ so sánh OpEx tổng thể chứ không chỉ giá compute.
- [RSS] [AWS Containers Blog](https://aws.amazon.com/blogs/containers/amazon-eks-now-supports-control-plane-egress-through-your-vpc) 2026-06-22 — AWS EKS cho phép định tuyến control plane traffic qua VPC khách hàng. Tác động: ❌ Feature gap bảo mật nghiêm trọng. Khách hàng Gov/Finance (đoạn 2026-06-26-positioning-summary.md) yêu cầu data residency và an ninh mạng cao sẽ ưu tiên AWS nếu GreenNode chưa có Private Link cho control plane, bất kể giá VKS rẻ hơn.
- [RSS] [AWS News Blog](https://aws.amazon.com/blogs/aws/announcing-amazon-ec2-g7-instances-accelerated-by-nvidia-rtx-pro-4500-blackwell-server-edition-gpus) 2026-06-18 — AWS GA GPU Blackwell (RTX PRO 4500) cho AI inference. Tác động: ❌ Feature gap phần cứng. Nếu GreenNode chưa có GPU Blackwell, sẽ mất lợi thế cạnh tranh về hiệu năng/giá cho các workload LLM inference nặng, đặc biệt khi khách hàng không bị ràng buộc data residency tuyệt đối.
- [Scrape] Viettel Cloud | https://viettelcloud.vn/san-pham/kubernetes | fetched_at=2026-06-29 — Trang sản phẩm VOKS được scrape nhưng chỉ trả về HTML/CSS, không có bảng giá. Tác động: Không xác định được giá list của đối thủ trực tiếp tại VN. Cần xác minh thủ công hoặc yêu cầu Sales Ops cung cấp quote mẫu.
- [Scrape] Bizfly Cloud | https://bizflycloud.vn/kubernetes | fetched_at=2026-06-29 — Trang sản phẩm BKE không hiển thị giá công khai. Tác động: Đối thủ VN đang giữ chiến lược giá kín (sales-led), khiến việc so sánh TCO trực tiếp trở nên khó khăn. GreenNode cần chuẩn bị battlecard dựa trên TCO ước tính thay vì so sánh giá list.

## Recommended Actions

- Talk Track cho Sales: Khi khách hàng hỏi về giá, chuyển hướng sang TCO tổng thể (OpEx + CapEx + Security). Nhấn mạnh GreenNode VKS giúp giảm chi phí tuân thủ pháp lý (Luật BVDLCN 2025) và chi phí vận hành nhờ Data Residency tuyệt đối, bù đắp cho việc có thể thiếu một số tính năng tự động hóa của AWS.
- Pricing Recommendation: Đề xuất mô hình giá trị (value-based pricing) cho phân khúc Gov/Finance, tập trung vào tính năng Private Cluster và IP Whitelist thay vì cạnh tranh giá list. Xem xét gói Reserved Instances với discount sâu hơn để cạnh tranh với AWS EKS Auto Mode.
- Theo dõi thêm: Rà soát roadmap GPU (A100/H100/Blackwell) của GreenNode và so sánh với AWS G7 instances. Nếu có kế hoạch ra mắt GPU mới, cần chuẩn bị pricing strategy riêng cho workload AI inference.
- Yêu cầu Sales Ops cung cấp quote mẫu từ FPT, Bizfly, Viettel để cập nhật dữ liệu pricing và tính toán TCO chính xác hơn.

## Risks

- Dữ liệu pricing đối thủ (AWS, FPT, Bizfly, Viettel) đã STALE (>12 ngày), không thể đảm bảo độ chính xác cho TCO calculation.
- Thiếu dữ liệu về giá GPU Blackwell của AWS và roadmap GPU của GreenNode, gây khó khăn trong việc định giá cho workload AI inference.
- Không có thông tin về discount structure (Reserved, Spot) của đối thủ VN, dẫn đến ước tính TCO có thể sai lệch lớn.
- Feature gap về bảo mật (control plane egress) có thể khiến GreenNode mất deal lớn dù giá rẻ hơn, do khách hàng Gov/Finance ưu tiên an ninh.

## Gaps / Thiếu dữ liệu

- Cần cập nhật: competitors/2026-06-17_aws-eks_profile.md — dữ liệu cũ, chưa dùng được cho pricing analysis.
- Cần cập nhật: competitors/2026-06-17_fpt-cloud-fke_profile.md — dữ liệu cũ, chưa dùng được.
- Cần cập nhật: competitors/2026-06-17_bizfly-bke_profile.md — dữ liệu cũ, chưa dùng được.
- Cần cập nhật: competitors/2026-06-17_viettel-voks_profile.md — dữ liệu cũ, chưa dùng được.
- Không fetch được bảng giá công khai từ trang web của Viettel VOKS, FPT FKE, Bizfly BKE (chỉ thấy HTML/CSS). Cần xác minh thủ công hoặc yêu cầu Sales Ops cung cấp quote mẫu.
- Thiếu thông tin về giá GPU Blackwell của AWS và thời gian ra mắt tại VN của GreenNode.
