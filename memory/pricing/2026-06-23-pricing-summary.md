# Pricing Summary — 2026-06-23

Source: competitor-monitor run | Model: qwen/qwen3-5-27b

## Key Findings

- [RSS] [AWS News Blog](https://aws.amazon.com/blogs/aws/aws-weekly-roundup-ny-summit-recap-local-zone-in-hanoi-grok-4-3-in-bedrock-price-reductions-and-more-june-22-2026) 2026-06-22 — AWS công bố giảm giá (price reductions) và mở rộng Local Zone tại Hà Nội. Tác động: Áp lực giá trực tiếp lên GreenNode cho các workload không yêu cầu data residency nghiêm ngặt. GreenNode cần rà soát lại TCO cho các workload hybrid để tránh mất khách vào AWS do chênh lệch giá.
- [RSS] [AWS Containers Blog](https://aws.amazon.com/blogs/containers/amazon-eks-now-supports-control-plane-egress-through-your-vpc) 2026-06-22 — AWS EKS ra mắt 'customer-routed control plane egress', cho phép định tuyến traffic control plane qua VPC khách hàng. Tác động: Feature gap nghiêm trọng về bảo mật cho Enterprise/Gov. Khách hàng tài chính/chính phủ yêu cầu control plane không ra internet sẽ ưu tiên AWS nếu GreenNode chưa có giải pháp Private Link tương đương. Đây là rủi ro churn cao hơn cả rủi ro về giá.
- [Scrape] Viettel Cloud | https://viettelcloud.vn/san-pham/kubernetes | fetched_at=2026-06-23 — Không tìm thấy bảng giá công khai trên trang vOKS. Tác động: Viettel tiếp tục chiến lược 'contact-only' pricing, tạo lợi thế đàm phán cho các deal lớn (SOE/Gov). GreenNode không thể so sánh TCO trực tiếp mà không có dữ liệu quote nội bộ.
- [Scrape] FPT Cloud | https://fptcloud.com/kubernetes | fetched_at=2026-06-23 — Không tìm thấy bảng giá công khai trên trang FKE. Tác động: FPT duy trì mô hình giá ẩn, tập trung vào bán hàng qua quan hệ. GreenNode cần chuẩn bị talk track về 'transparency' nếu định vị là đối thủ minh bạch hơn.
- [Scrape] Bizfly Cloud | https://bizflycloud.vn/kubernetes | fetched_at=2026-06-23 — Không tìm thấy bảng giá công khai trên trang BKE. Tác động: Bizfly (đối thủ SME) cũng không công khai giá, khiến việc so sánh TCO cho phân khúc SME trở nên khó khăn. GreenNode cần dựa vào dữ liệu quote lịch sử để ước tính.

## Recommended Actions

- Talk Track cho Sales: Nhấn mạnh 'Sovereign AI' và 'Data Residency' là yếu tố sống còn cho Gov/Finance, không chỉ là giá. Đối với khách hàng không bắt buộc onshore, thừa nhận AWS có lợi thế giá và tính năng mới, nhưng đề xuất mô hình Hybrid (Control Plane trên AWS, Workload nhạy cảm trên GreenNode) nếu có thể.
- Pricing Recommendation: Rà soát lại bảng giá VKS cho các instance GPU và Compute phổ biến. Nếu AWS giảm giá, cân nhắc điều chỉnh giá hoặc tạo gói 'Reserved' với discount sâu hơn cho các khách hàng SME để giữ chân.
- Technical Action: Yêu cầu Product/Engineering xác nhận ngay lập tức về khả năng triển khai 'Private Control Plane Egress' cho VKS. Nếu chưa có, đưa vào roadmap ưu tiên cao (Q3/Q4) để không mất khách Enterprise.
- Data Refresh: Yêu cầu cập nhật workspace pricing với dữ liệu mới nhất từ Sales Ops (quote mẫu của Viettel/FPT/Bizfly) và chính sách giá mới của GreenNode.

## Risks

- Dữ liệu pricing công khai của đối thủ VN (Viettel, FPT, Bizfly) không khả dụng, không thể tính toán TCO chính xác cho các scenario SME/Mid-market.
- Feature gap về 'Control Plane Egress' của AWS có thể làm mất khách hàng Enterprise/Gov ngay cả khi GreenNode có giá tốt hơn, do yêu cầu bảo mật khắt khe.
- Dữ liệu pricing nội bộ của GreenNode trong workspace đã cũ (20/05/2026), có thể không phản ánh chính xác các chương trình khuyến mãi hoặc điều chỉnh giá mới nhất.
- AWS giảm giá và mở rộng Local Zone Hà Nội làm giảm lợi thế 'độ trễ thấp' và 'giá cạnh tranh' của GreenNode đối với các khách hàng không bắt buộc data residency.

## Gaps / Thiếu dữ liệu

- Cần cập nhật: greennode/2026-05-20_greennode-vks_product-overview.md — Dữ liệu pricing cũ, chưa có số liệu mới để so sánh TCO.
- Không có dữ liệu giá cụ thể (USD/VND) cho các đối thủ Viettel, FPT, Bizfly từ nguồn công khai. Cần yêu cầu Sales Ops cung cấp quote mẫu gần đây.
- Chưa xác minh được GreenNode VKS có tính năng 'Private Control Plane Egress' hay chưa. Cần kiểm tra roadmap kỹ thuật hoặc tài liệu kỹ thuật mới nhất.
- Thiếu thông tin về mức giảm giá cụ thể của AWS (tỷ lệ % hoặc số tiền) để tính toán delta TCO chính xác.
