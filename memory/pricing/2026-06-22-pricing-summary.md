# Pricing Summary — 2026-06-22

Source: competitor-monitor run | Model: qwen/qwen3-5-27b

## Key Findings

- [RSS] [AWS Containers Blog](https://aws.amazon.com/blogs/containers/amazon-eks-now-supports-control-plane-egress-through-your-vpc) 2026-06-22 — AWS ra mắt tính năng định tuyến control plane egress qua VPC khách hàng cho EKS. Tác động: Tăng áp lực về compliance cho GreenNode VKS. Nếu GreenNode chưa có tính năng tương đương, khách hàng Enterprise/Gov có thể yêu cầu giảm giá hoặc từ chối chuyển đổi do lo ngại bảo mật. GreenNode cần xác nhận roadmap tính năng này ngay lập tức.
- [RSS] [AWS News Blog](https://aws.amazon.com/blogs/aws/announcing-amazon-ec2-g7-instances-accelerated-by-nvidia-rtx-pro-4500-blackwell-server-edition-gpus) 2026-06-18 — AWS công bố instance G7 với GPU Blackwell cho AI inference. Tác động: Tạo áp lực cạnh tranh về hiệu năng/giá cho workload AI. Nếu GreenNode chưa có GPU thế hệ mới, sẽ mất lợi thế về TCO cho các dự án AI inference cao cấp. Cần rà soát lại danh mục GPU hiện có và so sánh hiệu năng/giá với G7.
- [Scrape] Viettel IDC | https://viettelcloud.vn/san-pham/kubernetes | fetched_at=2026-06-22 — Trang sản phẩm vOKS không hiển thị bảng giá công khai. Tác động: Viettel tiếp tục chiến lược 'contact-only' pricing, gây khó khăn cho việc so sánh TCO trực tiếp. GreenNode cần chuẩn bị battlecard dựa trên giá trị (value) thay vì chỉ so sánh list price.
- [Scrape] FPT Cloud | https://fptcloud.com/kubernetes | fetched_at=2026-06-22 — Trang FKE không có thông tin giá công khai. Tác động: FPT cũng áp dụng mô hình giá tùy chỉnh. GreenNode cần tập trung vào các yếu tố khác biệt hóa như hỗ trợ tiếng Việt, SLA, và data residency để thắng thầu.
- [Scrape] Bizfly Cloud | https://bizflycloud.vn/kubernetes | fetched_at=2026-06-22 — Trang BKE không hiển thị bảng giá chi tiết. Tác động: Bizfly cũng không công khai giá. Thị trường VN đang thiếu minh bạch về giá K8s, khiến GreenNode khó định vị giá dựa trên đối thủ. Cần dựa vào dữ liệu win/loss nội bộ để điều chỉnh.

## Recommended Actions

- Talk Track cho Sales: Khi khách hàng hỏi về giá, nhấn mạnh vào 'Sovereign AI' và 'Data Residency' thay vì chỉ so sánh list price. Giải thích rằng GreenNode là lựa chọn duy nhất đáp ứng Luật BVDLCN 2025 và Luật An ninh mạng 2018 với hạ tầng AI tại VN.
- Pricing Recommendation: Đề xuất mô hình giá 'value-based' cho các workload AI, tập trung vào TCO tổng thể (bao gồm cả chi phí egress, support, và compliance) thay vì chỉ giá compute. Xem xét giảm giá cho các gói Reserved Instances để cạnh tranh với AWS.
- Product Roadmap: Ưu tiên phát triển tính năng 'control plane egress through VPC' cho GreenNode VKS để đáp ứng yêu cầu bảo mật của khách hàng Enterprise/Gov.
- GPU Strategy: Rà soát lại danh mục GPU hiện có và so sánh hiệu năng/giá với AWS G7 Blackwell. Nếu chưa có GPU thế hệ mới, cần có kế hoạch nhập hàng hoặc hợp tác với nhà cung cấp GPU ngay lập tức.
- Data Refresh: Cập nhật ngay lập tức dữ liệu pricing và cấu hình sản phẩm từ GreenNode VKS để đảm bảo tính chính xác của các phân tích TCO.

## Risks

- Thiếu dữ liệu pricing công khai từ đối thủ nội địa (Viettel, FPT, Bizfly) khiến việc so sánh TCO trực tiếp không khả thi. Phải dựa vào dữ liệu win/loss nội bộ hoặc phỏng đoán.
- AWS đang dẫn đầu về công nghệ AI-native (Blackwell GPU, Bedrock AgentCore). Nếu GreenNode không có GPU tương đương hoặc tính năng AI-native, sẽ mất lợi thế về giá trị (value) cho các workload AI cao cấp.
- Tính năng 'control plane egress through VPC' của AWS là yêu cầu bắt buộc cho nhiều khách hàng Enterprise/Gov. Nếu GreenNode chưa có, đây là rủi ro mất thầu lớn.
- Dữ liệu pricing từ workspace memory (2026-05-20) có thể đã cũ. Cần cập nhật ngay lập tức nếu có thay đổi về giá hoặc cấu hình.

## Gaps / Thiếu dữ liệu

- Cần cập nhật: greennode/2026-05-20_greennode-vks_product-overview.md — dữ liệu cũ, chưa có bảng giá mới nhất hoặc thông tin về GPU Blackwell.
- Không có dữ liệu pricing công khai từ Viettel vOKS, FPT FKE, Bizfly BKE. Cần scrape sâu hơn hoặc liên hệ sales để lấy thông tin.
- Không có thông tin về giá GPU hiện tại của GreenNode để so sánh với AWS G7 Blackwell.
- Không có dữ liệu về tính năng 'control plane egress through VPC' của GreenNode VKS. Cần xác nhận roadmap.
