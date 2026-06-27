# Pricing Summary — 2026-06-27

Source: competitor-monitor run | Model: qwen/qwen3-5-27b

## Key Findings

- [RSS] [AWS HPC Blog](https://aws.amazon.com/blogs/hpc/transforming-hpc-operations-with-intelligent-workload-orchestration-on-aws) 2026-06-26 — AWS công bố giải pháp tự động hóa orchestration cho HPC, giảm chi phí vận hành thủ công. Tác động: GreenNode VKS có thể thua về TCO vận hành (OpEx) cho các khách hàng Enterprise chạy workload AI/HPC nặng nếu không có tính năng tự động hóa tương đương, dù giá compute (CapEx) có thể rẻ hơn.
- [RSS] [AWS News Blog](https://aws.amazon.com/blogs/aws/announcing-amazon-ec2-g7-instances-accelerated-by-nvidia-rtx-pro-4500-blackwell-server-edition-gpus) 2026-06-18 — AWS ra mắt GPU Blackwell (RTX PRO 4500) cho inference. Tác động: Tạo ra 'performance gap' lớn. Khách hàng cần inference LLM tốc độ cao có thể chấp nhận trả giá premium cho AWS nếu GreenNode chưa có GPU thế hệ mới tại VN, làm giảm tính cạnh tranh về giá của VKS trong phân khúc AI cao cấp.
- [RSS] [AWS Containers Blog](https://aws.amazon.com/blogs/containers/amazon-eks-now-supports-control-plane-egress-through-your-vpc) 2026-06-22 — AWS cho phép định tuyến control plane traffic qua VPC khách hàng. Tác động: Giảm rủi ro bảo mật và chi phí egress cho khách hàng Gov/Finance. GreenNode cần rà soát lại cấu trúc giá cho Private Cluster/Network để cạnh tranh với lợi thế 'zero egress' này của AWS.
- [Scrape] Viettel IDC | https://viettelcloud.vn/san-pham/kubernetes | fetched_at=2026-06-27 — Không trích xuất được bảng giá cụ thể từ trang sản phẩm. Tác động: Không thể so sánh trực tiếp giá list price với Viettel VOKS. Cần yêu cầu Sales Ops cung cấp quote nội bộ hoặc scrape lại trang pricing chi tiết.
- [Scrape] FPT Cloud | https://fptcloud.com/kubernetes | fetched_at=2026-06-27 — Không trích xuất được bảng giá cụ thể từ trang sản phẩm. Tác động: Không thể so sánh trực tiếp giá list price với FPT FKE. Cần cập nhật dữ liệu pricing từ nguồn chính thức.
- [Scrape] Bizfly Cloud | https://bizflycloud.vn/kubernetes | fetched_at=2026-06-27 — Không trích xuất được bảng giá cụ thể từ trang sản phẩm. Tác động: Không thể so sánh trực tiếp giá list price với Bizfly BKE.

## Recommended Actions

- Talk Track cho Sales: Khi khách hàng hỏi về giá AI/HPC, nhấn mạnh 'Total Cost of Ownership' bao gồm cả chi phí tuân thủ (compliance) và an ninh dữ liệu tại VN. Giải thích rằng AWS có thể rẻ hơn về compute nhưng chi phí egress và rủi ro pháp lý (nếu data ra nước ngoài) sẽ làm tăng TCO thực tế cho các tổ chức Gov/Finance.
- Talk Track cho Sales: Đối với khách hàng cần GPU Blackwell, thừa nhận AWS có lợi thế phần cứng mới nhất nhưng đề xuất giải pháp 'Hybrid' hoặc 'Burst' nếu GreenNode chưa có sẵn, hoặc cam kết roadmap cập nhật GPU trong 6-12 tháng tới.
- Pricing Recommendation: Yêu cầu Product Team rà soát lại cấu trúc giá cho 'Private Cluster' và 'Control Plane Egress' để có thể cạnh tranh với tính năng mới của AWS (customer-routed egress). Cân nhắc gói 'HPC Auto-Scaling' để giảm OpEx cho khách hàng.
- Data Refresh: Kích hoạt lại scraper chuyên sâu cho trang pricing của Viettel, FPT, Bizfly và AWS (region AP-Southeast-1) để cập nhật bảng giá mới nhất trước khi chạy báo cáo TCO tiếp theo.

## Risks

- Dữ liệu pricing đối thủ trong workspace (tính đến 2026-06-17) đã bị đánh dấu là STALE và không được sử dụng để đưa ra claim về giá.
- Không có số liệu giá cụ thể (USD/giờ hoặc VND/tháng) cho các instance GPU mới (Blackwell) của AWS để tính toán TCO cho scenario AI Inference.
- Rủi ro 'hidden cost' từ phía khách hàng khi so sánh với AWS: AWS đang giảm chi phí vận hành (OpEx) thông qua tự động hóa HPC và tối ưu hóa egress, trong khi GreenNode có thể đang bán giá compute rẻ nhưng OpEx cao hơn do thiếu tính năng tự động hóa.
- Thiếu dữ liệu về chính sách Reserved Instances hoặc Committed Use Discount của đối thủ VN để ước tính giá thực tế cho Enterprise.

## Gaps / Thiếu dữ liệu

- Cần cập nhật: competitors/2026-06-17_viettel-voks_profile.md — dữ liệu cũ, chưa dùng được.
- Cần cập nhật: competitors/2026-06-17_fpt-cloud-fke_profile.md — dữ liệu cũ, chưa dùng được.
- Cần cập nhật: competitors/2026-06-17_bizfly-bke_profile.md — dữ liệu cũ, chưa dùng được.
- Cần scrape lại trang pricing chi tiết của Viettel, FPT, Bizfly (không chỉ trang tổng quan sản phẩm) để lấy số liệu giá list price.
- Cần xác minh giá GPU Blackwell của AWS tại region AP-Southeast-1 (Singapore) để ước tính TCO cho khách hàng VN nếu họ chấp nhận latency.
- Thiếu dữ liệu về chi phí egress thực tế của GreenNode VKS so với AWS để tính toán TCO cho các workload có traffic lớn.
