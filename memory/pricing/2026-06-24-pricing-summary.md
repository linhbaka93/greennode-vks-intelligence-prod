# Pricing Summary — 2026-06-24

Source: competitor-monitor run | Model: qwen/qwen3-5-27b

## Key Findings

- [RSS] [AWS Containers Blog](https://aws.amazon.com/blogs/containers/amazon-eks-now-supports-control-plane-egress-through-your-vpc) 2026-06-22 — AWS ra mắt 'customer-routed control plane egress' cho EKS, cho phép định tuyến lưu lượng control plane qua VPC của khách hàng. Tác động: Tăng áp lực compliance cho GreenNode VKS. Khách hàng Enterprise/Gov (đặc biệt ngân hàng) sẽ yêu cầu tính năng tương tự như điều kiện bắt buộc. Nếu VKS chưa có, đây là rủi ro mất deal (churn risk) hoặc phải giảm giá để bù đắp thiếu hụt tính năng bảo mật. GreenNode cần xác nhận ngay khả năng hỗ trợ và đưa vào talk track 'Sovereign Security'.
- [RSS] [AWS News Blog](https://aws.amazon.com/blogs/aws/announcing-amazon-ec2-g7-instances-accelerated-by-nvidia-rtx-pro-4500-blackwell-server-edition-gpus) 2026-06-18 — AWS công bố EC2 G7 với GPU NVIDIA RTX PRO 4500 Blackwell Server Edition cho AI inference. Tác động: AWS có lợi thế công nghệ phần cứng mới nhất. Nếu GreenNode chưa có GPU thế hệ Blackwell, sẽ khó cạnh tranh về hiệu năng/giá (performance/price) cho workload AI inference cao cấp. Tuy nhiên, đối với các khách hàng cần data residency tại VN, GreenNode vẫn có thể định giá cao hơn (premium) dựa trên yếu tố chủ quyền dữ liệu và độ trễ thấp, miễn là có GPU thế hệ mới nhất hiện có (ví dụ H100/H200).
- [RSS] [GreenNode Blog](https://greennode.ai/blog/greennode-achieves-soc-2-type2-report) 2026-06-23 — GreenNode đạt chứng nhận SOC 2 Type 2 cho dịch vụ GPU Cloud. Tác động: Đây là 'proof point' mạnh để định giá premium cho phân khúc Enterprise/Gov. SOC 2 Type 2 là rào cản gia nhập (moat) mà các đối thủ nhỏ hơn hoặc AWS (vùng global) khó đáp ứng nhanh cho yêu cầu cụ thể của VN. GreenNode nên dùng chứng nhận này để biện minh cho mức giá cao hơn (10-20%) so với đối thủ nội địa chưa có chứng nhận tương đương.
- [Scrape] Viettel IDC | https://viettelcloud.vn/san-pham/kubernetes | fetched_at=2026-06-24 — Trang sản phẩm Viettel vOKS không hiển thị bảng giá công khai (contact-only). Tác động: Viettel tiếp tục chiến lược 'sales-led pricing' cho Enterprise. GreenNode không thể so sánh trực tiếp list price. Cần tập trung vào TCO (Total Cost of Ownership) bao gồm chi phí ẩn (egress, support, compliance) để chứng minh giá trị.
- [Scrape] FPT Cloud | https://fptcloud.com/kubernetes | fetched_at=2026-06-24 — Trang sản phẩm FPT FKE không hiển thị bảng giá công khai. Tác động: Tương tự Viettel, FPT dùng mô hình giá tùy chỉnh. GreenNode cần chuẩn bị battlecard TCO cho các scenario cụ thể (SME, Mid, Enterprise) để Sales có thể so sánh trực tiếp trong RFP.

## Recommended Actions

- Talk Track cho Sales: Khi khách hàng so sánh với AWS, nhấn mạnh 'Sovereign AI' và 'SOC 2 Type 2'. 'AWS có công nghệ mới nhất, nhưng GreenNode là lựa chọn duy nhất tại VN đáp ứng Luật BVDLCN 2025 với chứng nhận bảo mật quốc tế SOC 2 Type 2. Chi phí egress và độ trễ của AWS sẽ làm tăng TCO thực tế của bạn.'
- Pricing Recommendation: Định vị VKS ở mức 'Premium Value' (cao hơn 10-15% so với đối thủ nội địa chưa có SOC 2) cho phân khúc Enterprise/Gov. Không đua giá với AWS trên các workload AI inference tiêu chuẩn; thay vào đó, tập trung vào các workload yêu cầu data residency và độ trễ thấp.
- Product Action: Yêu cầu Product Team xác nhận ngay khả năng hỗ trợ 'control plane egress through VPC' cho VKS. Nếu chưa có, cần đưa vào roadmap ngắn hạn (Q3 2026) để không mất khách hàng Enterprise.
- Market Intelligence: Theo dõi sát sao việc ra mắt GPU Blackwell tại các data center VN của đối thủ nội địa. Nếu Viettel/FPT có Blackwell trước, cần điều chỉnh chiến lược giá ngay lập tức.

## Risks

- Thiếu dữ liệu pricing công khai từ đối thủ nội địa (Viettel, FPT, Bizfly) khiến việc so sánh trực tiếp list price là không thể. Phải dựa vào TCO và giá trị gia tăng (compliance, support).
- AWS đang dẫn đầu về công nghệ phần cứng AI (Blackwell) và tính năng bảo mật K8s (control plane egress). Nếu GreenNode không cập nhật phần cứng hoặc tính năng tương đương, sẽ mất lợi thế cạnh tranh về giá trị (value gap) với các khách hàng không bị ràng buộc bởi data residency.
- Dữ liệu pricing từ workspace memory (2026-05-20) có thể đã cũ. Cần xác nhận lại các mức giá hiện hành của VKS trước khi đưa ra khuyến nghị cụ thể.

## Gaps / Thiếu dữ liệu

- Cần cập nhật: memory/pricing/vks-pricing-2026.md — Dữ liệu pricing VKS cuối cùng là 2026-05-20, chưa có update mới trong 3 ngày qua.
- Cần xác minh: Pricing GPU của GreenNode cho các instance thế hệ mới nhất (H100/H200) so với AWS G7 (Blackwell).
- Cần xác minh: Khả năng hỗ trợ 'control plane egress through VPC' của GreenNode VKS. Nếu chưa có, cần roadmap rõ ràng để Sales trả lời khách hàng Enterprise.
- Cần thu thập: Bảng giá công khai hoặc promo từ Bizfly Cloud BKE (nếu có) để so sánh phân khúc SME.
