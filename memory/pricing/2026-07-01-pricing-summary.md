# Pricing Summary — 2026-07-01

Source: monthly-brief run | Model: qwen/qwen3-5-27b

## Key Findings

- [RSS] [AWS News Blog](https://aws.amazon.com/blogs/aws/aws-weekly-roundup-ny-summit-recap-local-zone-in-hanoi-grok-4-3-in-bedrock-price-reductions-and-more-june-22-2026) 2026-06-22 — AWS thông báo giảm giá chung trong bản tin tuần. Tác động: Tăng áp lực biên lợi nhuận cho GreenNode nếu chỉ cạnh tranh bằng giá compute. GreenNode nên chuẩn bị battlecard nhấn mạnh TCO toàn diện (bao gồm chi phí tuân thủ pháp lý mà hyperscaler không cover).
- [RSS] [FPT Cloud Blog](https://fptcloud.com/dung-thu-chi-0d-nhan-03-uu-dai-cung-fpt-cloud) 2026-06-04 — FPT Cloud triển khai chương trình 'Dùng thử 0 đồng'. Tác động: Rủi ro churn ở phân khúc SME/Startup nhạy cảm giá. GreenNode nên xem xét mở rộng free tier hoặc trial period cho VKS để giữ chân khách hàng giai đoạn onboarding.
- [RSS] [GreenNode Blog](https://greennode.ai/blog/digest-june-2026) 2026-06-30 — GreenNode ra mắt Cost Explorer trong digest tháng 6. Tác động: Cải thiện khả năng minh bạch hóa chi phí cho khách hàng, giúp Sales thuyết phục về TCO thực tế thay vì chỉ list price. Cần đào tạo Sales cách sử dụng tool này trong proposal.
- [RSS] [AWS Containers Blog](https://aws.amazon.com/blogs/containers/amazon-eks-now-supports-control-plane-egress-through-your-vpc) 2026-06-22 — AWS cho phép định tuyến egress control plane qua VPC của khách hàng. Tác động: Thu hẹp khoảng cách về bảo mật/compliance với GreenNode VKS. Nếu khách hàng yêu cầu tính năng này, GreenNode cần xác nhận ngay khả năng tương đương để tránh mất điểm trong RFP.

## Recommended Actions

- Talk Track Sales: Khi khách hỏi về chênh lệch giá với AWS, hãy dẫn dắt sang 'Compliance Risk Cost'. Ví dụ: 'Giá AWS thấp hơn X%, nhưng chi phí xử lý vi phạm Luật BVDLCN 2025 hoặc data residency risk có thể lên tới Y% doanh thu.'
- Product Marketing: Đẩy mạnh tính năng Cost Explorer trong các demo. Chứng minh GreenNode giúp khách hàng tối ưu chi phí vận hành (FinOps) tốt hơn nhờ visibility cao hơn.
- Pricing Strategy: Xem xét đề xuất gói 'Trial Extended' hoặc 'Proof of Concept Discount' cho các deal Enterprise lớn để đối phó với Free Trial của FPT Cloud.
- Competitive Intel: Yêu cầu Product Team xác nhận timeline feature parity cho 'Control Plane Egress via VPC' để trả lời RFP ngân hàng/chính phủ.

## Risks

- Dữ liệu pricing từ workspace (`greennode/2026-05-20...`) đã cũ hơn 1 tháng so với thời điểm hiện tại (July 2026), có thể không phản ánh chính sách giá mới nhất.
- Thiếu số liệu cụ thể về mức giảm giá của AWS và FPT Cloud, khó định lượng delta TCO chính xác.
- Rủi ro churn tăng nếu khách hàng Enterprise so sánh trực tiếp list price GPU/Compute mà bỏ qua yếu tố compliance.

## Gaps / Thiếu dữ liệu

- Cần cập nhật: Bảng giá công khai mới nhất của GreenNode VKS (Compute, Storage, Egress) — Dữ liệu hiện tại từ May 2026 chưa đủ để tính toán TCO scenario S1-S5.
- Cần xác minh: Mức giảm giá cụ thể (%) của AWS trong bản tin 22/06/2026 — Snippet RSS chỉ ghi 'price reductions' không có con số.
- Cần xác minh: Chi tiết gói Free Trial của FPT Cloud (thời hạn, giới hạn tài nguyên) để đánh giá mức độ ảnh hưởng đến segment SME.
- Cần cập nhật: Chính sách giá cho instance GPU mới (Blackwell G7) của AWS để so sánh với roadmap GPU của GreenNode.
