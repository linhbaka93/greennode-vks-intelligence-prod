# Pricing Summary — 2026-06-23

Source: competitor-monitor run | Model: qwen/qwen3-5-27b

## Key Findings

- [RSS] [AWS Containers Blog](https://aws.amazon.com/blogs/containers/amazon-eks-now-supports-control-plane-egress-through-your-vpc) 2026-06-22 — AWS ra mắt 'customer-routed control plane egress' cho EKS, cho phép định tuyến traffic control plane qua VPC khách hàng. Tác động: Tăng áp lực compliance cho GreenNode VKS. Khách hàng Enterprise/Gov yêu cầu tính năng này để tuân thủ chính sách bảo mật nghiêm ngặt. Nếu VKS chưa có, đây là điểm yếu kỹ thuật (feature gap) có thể gây mất deal, không liên quan trực tiếp đến giá nhưng ảnh hưởng đến TCO (chi phí triển khai giải pháp bù đắp).
- [RSS] [AWS News Blog](https://aws.amazon.com/blogs/aws/announcing-amazon-ec2-g7-instances-accelerated-by-nvidia-rtx-pro-4500-blackwell-server-edition-gpus) 2026-06-18 — AWS ra mắt EC2 G7 với GPU NVIDIA RTX PRO 4500 Blackwell. Tác động: Tạo áp lực cạnh tranh về hiệu năng/giá cho workload AI Inference (S4). Nếu GreenNode chưa có GPU Blackwell, sẽ thua thế về hiệu năng/giá cho các workload AI cao cấp, buộc phải cạnh tranh bằng giá thấp hơn hoặc tập trung vào các workload không cần GPU mới nhất.
- [Scrape] Viettel IDC | https://viettelcloud.vn/san-pham/kubernetes | fetched_at=2026-06-23 — Không trích xuất được bảng giá cụ thể từ trang sản phẩm. Tác động: Viettel IDC duy trì chiến lược 'contact-only' pricing, gây khó khăn cho việc so sánh TCO trực tiếp. GreenNode cần chuẩn bị battlecard dựa trên giá niêm yết công khai (nếu có) hoặc nhấn mạnh vào tính minh bạch và billing VND để tạo lợi thế so với đối thủ không công khai giá.
- [Scrape] FPT Cloud | https://fptcloud.com/kubernetes | fetched_at=2026-06-23 — Không trích xuất được bảng giá cụ thể. Tác động: FPT Cloud cũng không công khai giá K8s. Điều này củng cố giả định rằng thị trường Enterprise VN đang cạnh tranh bằng giải pháp tổng thể (solution-led) hơn là giá niêm yết. GreenNode nên tập trung vào TCO toàn diện (bao gồm egress, support) thay vì chỉ so sánh giá compute.
- [Scrape] Bizfly Cloud | https://bizflycloud.vn/kubernetes | fetched_at=2026-06-23 — Không trích xuất được bảng giá cụ thể. Tác động: Bizfly (đối thủ SME) cũng không công khai giá chi tiết. Tuy nhiên, Bizfly đã xác nhận có GPU node pool (từ memory 17/06). GreenNode cần rà soát lại giá GPU của mình so với Bizfly để đảm bảo không bị undercut ở phân khúc SME.

## Recommended Actions

- Talk Track cho Sales: Nhấn mạnh 'TCO minh bạch' và 'Billing VND' của GreenNode so với AWS (USD + egress cao) và đối thủ nội địa (giá không công khai, rủi ro hidden cost). Sử dụng câu chuyện: 'Khách hàng không cần lo lắng về biến động tỷ giá hay chi phí egress bất ngờ khi dùng VKS'.
- Pricing Recommendation: Rà soát lại giá GPU hiện tại của VKS. Nếu chưa có GPU Blackwell, cân nhắc định vị lại ở phân khúc 'AI Inference hiệu quả' (cost-effective) thay vì 'hiệu năng cao nhất', hoặc đẩy nhanh kế hoạch nâng cấp phần cứng.
- Theo dõi thêm: Kiểm tra kỹ tính năng bảo mật 'control plane egress' của VKS. Nếu chưa có, cần phối hợp với Product để đưa vào roadmap hoặc chuẩn bị giải pháp bù đắp (workaround) cho khách hàng Enterprise/Gov.
- Cập nhật dữ liệu: Yêu cầu Product/Finance cung cấp bảng giá VKS mới nhất (tính đến 23/06/2026) để cập nhật vào workspace và tính toán TCO chính xác cho các scenario S1-S5.

## Risks

- Dữ liệu pricing của GreenNode VKS trong workspace (20/05/2026) có thể đã cũ (>30 ngày). Cần xác nhận lại giá hiện hành trước khi đưa ra TCO cụ thể.
- Không có dữ liệu giá GPU mới (Blackwell) từ AWS hoặc đối thủ nội địa để tính toán TCO cho scenario AI Inference (S4).
- Chiến lược 'contact-only' của đối thủ nội địa khiến việc so sánh giá trực tiếp là không khả thi, dễ dẫn đến đánh giá sai lệch về vị thế giá.

## Gaps / Thiếu dữ liệu

- Cần cập nhật: greennode/2026-05-20_greennode-vks_product-overview.md — Dữ liệu pricing VKS cũ, chưa xác minh được giá mới nhất.
- Không có dữ liệu giá chi tiết cho GPU Blackwell (AWS G7) hoặc GPU tương đương của đối thủ nội địa để tính toán TCO cho workload AI.
- Không xác định được giá egress và LB/NAT của Viettel/FPT/Bizfly do không công khai, gây khó khăn cho việc tính toán hidden cost trong TCO.
- Cần xác minh: GreenNode VKS có hỗ trợ tính năng 'control plane egress through VPC' tương tự AWS EKS không? Nếu không, đây là feature gap cần giải quyết.
