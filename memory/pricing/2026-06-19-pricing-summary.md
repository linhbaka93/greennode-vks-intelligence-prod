# Pricing Summary — 2026-06-19

Source: weekly-digest run | Model: qwen/qwen3-5-27b

## Key Findings

- [RSS] [AWS News Blog](https://aws.amazon.com/blogs/aws/announcing-amazon-ec2-g7-instances-accelerated-by-nvidia-rtx-pro-4500-blackwell-server-edition-gpus) 2026-06-18 — AWS ra mắt EC2 G7 instances với GPU NVIDIA RTX PRO 4500 Blackwell, tập trung vào AI inference. Tác động: Tăng áp lực cạnh tranh về hiệu năng/giá cho workload AI. GreenNode chưa có thông tin pricing công khai cho GPU tương đương, gây rủi ro thua thế trong các RFP yêu cầu hiệu năng cao cấp nếu không có chiến lược giá linh hoạt.
- [Workspace] [pricing/2026-06-17_aws-eks_pricing.md] 2026-06-17 — AWS EKS thu phí Control Plane $0.10/giờ (~73 USD/tháng). Tác động: Tạo cơ hội cho GreenNode VKS định vị 'miễn phí control plane' để thu hút SME và các cluster nhỏ, nơi chi phí cố định này chiếm tỷ trọng lớn trong TCO.
- [Suy luận] Dựa trên [competitors/2026-06-17_fpt-cloud-fke_profile.md] và [competitors/2026-06-17_viettel-idc-kubernetes_profile.md] — FPT và Viettel áp dụng mô hình pricing 'contact-only' (không công khai). Tác động: Tạo rào cản so sánh giá trực tiếp cho khách hàng SME, nhưng đồng thời tạo cơ hội cho GreenNode trở thành lựa chọn 'minh bạch' và 'dễ dự báo chi phí' cho các doanh nghiệp vừa và nhỏ.
- [RSS] [Vietnam.vn](https://news.google.com/rss/articles/CBMipAFBVV95cUxPQi0zZkRtNTlkR3JIbU45XzM1aElKTHljQWEzRVM4RnhXZ0s5OWZVV0Y0eGg5NUV4TWxPS00xRzhDNDlQRjhMOGVqVWFXcmswQ3JSUDV4aTFXeG0tclNVSE9ubnBpYl9YSTY4RGR4bENYZFJ2QW13dG1IRnluWGV0U051b3J2VFJjUzJIYjdtY2dRM25jbEZmNU52NzBMQWxiNG1Qbg?oc=5) 2026-06-12 — GreenNode được cấp Chứng nhận Doanh nghiệp Công nghệ cao đầu tiên tại TP.HCM. Tác động: Tăng giá trị thương hiệu và khả năng đàm phán giá (premium pricing) cho phân khúc Enterprise/Gov, bù đắp cho việc thiếu lợi thế giá thuần túy so với các đối thủ giá rẻ.

## Recommended Actions

- Talk Track cho Sales (SME): Nhấn mạnh 'TCO minh bạch' và 'Không phí ẩn Control Plane'. So sánh trực tiếp với AWS EKS ($73/tháng phí cố định) để chứng minh GreenNode VKS rẻ hơn cho các cluster nhỏ và môi trường dev/test.
- Talk Track cho Sales (Enterprise/AI): Tập trung vào 'Sovereign AI' và 'Compliance' (Chứng nhận CNCA) thay vì chỉ so sánh giá. Đề xuất mô hình Reserved/Committed Use để cạnh tranh với các deal giá ẩn của FPT/Viettel.
- Pricing Recommendation: Ưu tiên công bố bảng giá GPU (nếu có) hoặc tạo gói 'AI Inference Starter' với giá cố định/tháng để đối phó với sự ra mắt của AWS G7, tránh để khách hàng phải chờ báo giá.
- Theo dõi thêm: Scrape trang pricing AWS ngay khi có thông tin giá EC2 G7 để cập nhật TCO scenario S4 trong vòng 48h tới.

## Risks

- Dữ liệu pricing của GreenNode VKS trong memory (2026-05-20) có thể đã lỗi thời, đặc biệt là về phí GPU và egress, chưa được cập nhật sau sự kiện rebrand và các thay đổi thị trường gần đây.
- Thiếu dữ liệu pricing công khai cho AWS EC2 G7 (Blackwell) khiến việc tính toán TCO cho scenario AI Inference (S4) chưa thể thực hiện chính xác, gây rủi ro đánh giá sai vị thế cạnh tranh.
- Đối thủ nội địa (FPT, Viettel) sử dụng chiến lược giá ẩn (contact-only), khiến việc so sánh trực tiếp TCO cho khách hàng Enterprise trở nên khó khăn và phụ thuộc vào quá trình bán hàng.

## Gaps / Thiếu dữ liệu

- Cần cập nhật: pricing/2026-05-20_greennode-vks_product-overview.md — Dữ liệu pricing chi tiết (đặc biệt là GPU node pool và egress) chưa được xác minh trong 7 ngày qua.
- Thiếu dữ liệu: Giá niêm yết cho AWS EC2 G7 instances (Blackwell) chưa có trong evidence bundle, cần scrape trang pricing AWS để tính toán TCO scenario S4.
- Thiếu dữ liệu: Bảng giá công khai của FPT FKE và Viettel VKS (nếu có) để so sánh trực tiếp với GreenNode VKS.
- Cần xác minh: Phí egress và LB/NAT của GreenNode VKS so với AWS và đối thủ nội địa để đánh giá hidden cost thực tế.
