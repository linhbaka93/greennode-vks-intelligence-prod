# Pricing Summary — 2026-06-19

Source: competitor-monitor run | Model: qwen/qwen3-5-27b

## Key Findings

- [RSS] [AWS News Blog](https://aws.amazon.com/blogs/aws/announcing-amazon-ec2-g7-instances-accelerated-by-nvidia-rtx-pro-4500-blackwell-server-edition-gpus) 2026-06-18 — AWS ra mắt EC2 G7 instances với GPU NVIDIA RTX PRO 4500 Blackwell Server Edition. Tác động: Tăng áp lực cạnh tranh về hiệu năng/giá cho workload AI inference (S4). GreenNode chưa có thông tin pricing công khai cho GPU tương đương, gây rủi ro thua thế trong các RFP yêu cầu hiệu năng cao cấp nếu không có chiến lược giá linh hoạt. GreenNode nên: Theo dõi sát giá G7 khi công bố để cập nhật TCO S4 và chuẩn bị talk track về 'Total Cost of Ownership' (bao gồm egress, latency, và data residency).
- [RSS] [Vietnam.vn](https://news.google.com/rss/articles/CBMikgFBVV95cUxQV2ExNGdzR1BneXhBNUhxMDNVY3dMZXhlUGlvcWFBYUk2OVZZdFJqTUZuY3NzdWUtWHZvUTJvZW1rZElGSWRzendwNlFfVEdNMjRoVUI2eExHeHQxTUtUWjJnaGxEdHlhSjdmM2UzdDhCVVlzZ3A4YldMcHZ5QmRUS0ZKWmpzWVpZX1hFVGdSd2Y0QQ) 2026-06-17 — MSB Bank hợp tác chiến lược với GreenNode để triển khai hàng trăm ứng dụng AI. Tác động: Xác nhận GreenNode là lựa chọn ưu tiên cho Enterprise Banking cần Sovereign AI. Tuy nhiên, deal này không tiết lộ pricing, nhưng cho thấy khách hàng sẵn sàng trả giá cao hơn cho compliance và data residency. GreenNode nên: Sử dụng case study MSB để định vị giá trị 'Sovereign AI Premium' thay vì cạnh tranh trực tiếp về giá list.
- [Scrape] Viettel IDC | https://viettelcloud.vn/san-pham/kubernetes | fetched_at=2026-06-19 — Trang sản phẩm VKS/vOKS của Viettel không hiển thị bảng giá công khai (contact-only). Tác động: Khó so sánh TCO trực tiếp. Viettel thường áp dụng giá linh hoạt theo deal lớn (Enterprise/SOE). GreenNode nên: Giả định Viettel có thể cạnh tranh về giá cho các deal lớn, nhưng GreenNode có lợi thế về tính minh bạch và tốc độ triển khai cho SME/Mid-market.
- [Scrape] FPT Cloud | https://fptcloud.com/kubernetes | fetched_at=2026-06-19 — Trang sản phẩm FKE của FPT không hiển thị bảng giá công khai (contact-only). Tác động: Tương tự Viettel, FPT tập trung vào sales-led pricing. GreenNode nên: Nhấn mạnh lợi thế 'Self-service' và 'Transparent Pricing' của VKS để thu hút khách hàng SME/Mid-market không muốn đàm phán giá phức tạp.
- [Scrape] Bizfly Cloud | https://bizflycloud.vn/kubernetes | fetched_at=2026-06-19 — Trang sản phẩm BKE của Bizfly không hiển thị bảng giá công khai chi tiết cho K8s (chỉ có link 'Liên hệ'). Tác động: Bizfly có thể đang dùng chiến lược giá ẩn để linh hoạt cạnh tranh. GreenNode nên: Theo dõi các chương trình khuyến mãi hoặc bundle của Bizfly (thường xuất hiện trên social/blog) để điều chỉnh pricing strategy.

## Recommended Actions

- Talk Track cho Sales: Nhấn mạnh 'Sovereign AI Premium' — GreenNode VKS không chỉ là hạ tầng K8s, mà là giải pháp AI tuân thủ Luật BVDLCN 2025, giúp khách hàng tránh rủi ro pháp lý và bảo vệ dữ liệu nhạy cảm. Sử dụng case study MSB Bank để minh chứng.
- Pricing Recommendation: Đề xuất mô hình 'Transparent Pricing' cho SME/Mid-market — Công khai bảng giá chi tiết cho các gói tiêu chuẩn (S1, S2) để tạo lợi thế cạnh tranh so với đối thủ nội địa (contact-only).
- Pricing Recommendation: Chuẩn bị 'TCO Calculator' cho AI Inference (S4) — Khi AWS công bố giá G7, lập tức tính toán TCO so sánh (bao gồm egress, latency, và data residency) để chứng minh GreenNode có thể rẻ hơn hoặc có giá trị tương đương cho các workload cần data residency.
- Theo dõi thêm: Cập nhật pricing GPU của đối thủ nội địa — Liên hệ Sales/Marketing để thu thập thông tin pricing GPU từ Viettel, FPT, Bizfly (nếu có) hoặc theo dõi các chương trình khuyến mãi trên social/blog.
- Theo dõi thêm: Giá AWS EC2 G7 — Theo dõi sát sao khi AWS công bố giá chính thức để cập nhật TCO S4 và điều chỉnh chiến lược pricing nếu cần.

## Risks

- Thiếu dữ liệu pricing GPU công khai từ GreenNode và đối thủ nội địa, gây khó khăn trong việc tính toán TCO chính xác cho scenario S4 (AI Inference).
- AWS EC2 G7 có thể công bố giá thấp hơn dự kiến, tạo áp lực cạnh tranh lớn về hiệu năng/giá cho các workload AI cao cấp.
- Đối thủ nội địa có thể áp dụng giá linh hoạt (discount sâu) cho các deal lớn mà không công khai, gây rủi ro mất deal nếu GreenNode chỉ dựa vào giá list.
- Dữ liệu pricing AWS EKS (2026-06-17) có thể đã thay đổi, cần xác minh lại nếu có thông tin mới.

## Gaps / Thiếu dữ liệu

- Cần cập nhật: pricing/2026-06-17_aws-eks_pricing.md — Dữ liệu pricing AWS EKS cần được refresh để đảm bảo tính chính xác (cuối cùng cập nhật 2026-06-17).
- Cần xác minh: Pricing GPU của GreenNode VKS — Chưa có thông tin công khai về giá GPU node pool cho VKS, cần thu thập từ Sales/Marketing hoặc trang pricing nội bộ.
- Cần xác minh: Pricing GPU của đối thủ nội địa (Viettel, FPT, Bizfly) — Cần thu thập thông tin từ các nguồn khác (social, blog, hoặc contact sales) để so sánh TCO.
- Cần theo dõi: Giá AWS EC2 G7 — Cần theo dõi sát sao khi AWS công bố giá chính thức để cập nhật TCO S4.
