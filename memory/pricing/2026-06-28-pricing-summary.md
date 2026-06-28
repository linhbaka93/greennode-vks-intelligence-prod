# Pricing Summary — 2026-06-28

Source: competitor-monitor run | Model: qwen/qwen3-5-27b

## Key Findings

- [Chưa xác minh] Không có tin mới về biến động giá hoặc chương trình khuyến mãi từ đối thủ nội địa (Viettel IDC, FPT Cloud, Bizfly Cloud) trong 3 ngày qua. Các trang pricing của đối thủ (scrape 2026-06-28) chỉ trả về giao diện tải trang, không trích xuất được số liệu giá cụ thể. — Tác động: Không thể xác định áp lực giá (pricing pressure) tức thời. GreenNode cần duy trì chiến lược giá hiện tại dựa trên dữ liệu cũ cho đến khi có scrape thành công.
- [RSS] [Vietnam.vn](https://news.google.com/rss/articles/CBMijwFBVV95cUxQUF9HNTZhVFREd0p4TWY5S0JEOEZTc09kTkQxVzg0MlRrZWQwWWRySF9vRmsyS3RfQmJsYnY2azRMazNsME9MSVo5eTR4SUxHUzc2dUNCUTdvYXBiOS11T0IyemU3eDBhWFV1aGNWaW9YZWJMQVRKbTJySVFpaW9YQjVQSmpMbFFrUmF2VU5Fdw?oc=5) 2026-06-27 — Hà Nội và CMC hợp tác phát triển chính phủ số và thành phố AI. — Tác động: CMC (đối thủ trực tiếp trong mảng Sovereign Cloud) đang tăng cường vị thế trong các dự án chính phủ lớn. GreenNode cần chuẩn bị TCO so sánh (bao gồm cả chi phí tuân thủ và vận hành) để cạnh tranh trong các RFP sắp tới, thay vì chỉ cạnh tranh về giá list.
- [RSS] [AWS Containers Blog](https://aws.amazon.com/blogs/containers/amazon-eks-now-supports-control-plane-egress-through-your-vpc) 2026-06-22 — AWS công bố tính năng 'customer-routed control plane egress' cho EKS. — Tác động: AWS đang giải quyết điểm yếu về bảo mật cho khách hàng ngân hàng/chính phủ. Nếu GreenNode VKS chưa có tính năng tương đương (hoặc tính năng này không được định vị rõ trong pricing), GreenNode có thể mất điểm trong các cuộc đấu thầu yêu cầu strict compliance, bất kể giá thấp hơn.
- [RSS] [AWS News Blog](https://aws.amazon.com/blogs/aws/announcing-amazon-ec2-g7-instances-accelerated-by-nvidia-rtx-pro-4500-blackwell-server-edition-gpus) 2026-06-18 — AWS ra mắt instance G7 với GPU Blackwell. — Tác động: Tăng áp lực cạnh tranh về hiệu năng/giá cho workload AI Inference (S4). GreenNode cần rà soát lại giá GPU hiện tại (nếu có) so với hiệu năng Blackwell để tránh bị coi là 'legacy' trong các deal AI.

## Recommended Actions

- Ưu tiên cao: Kích hoạt lại quy trình scrape pricing cho Viettel, FPT, Bizfly và GreenNode để cập nhật dữ liệu giá (compute, storage, egress) trước khi chạy phân tích TCO.
- Chuẩn bị Talk Track cho Sales: Nhấn mạnh lợi thế 'Sovereign AI' và 'Data Residency' của GreenNode thay vì cạnh tranh trực tiếp về giá list khi chưa có số liệu mới. Sử dụng ví dụ hợp tác MSB Bank và chứng nhận TP.HCM làm bằng chứng uy tín.
- Theo dõi thêm: Cập nhật roadmap tính năng bảo mật (control plane egress) của GreenNode VKS để đối phó với tính năng mới của AWS EKS, tránh mất điểm trong các RFP ngân hàng.
- Đề xuất: Xây dựng mô hình TCO giả định (scenario S2, S4) dựa trên dữ liệu cũ nhưng gắn nhãn rõ ràng 'Estimate based on stale data' để dùng làm tài liệu tham khảo nội bộ, không dùng cho khách hàng.

## Risks

- Dữ liệu pricing đối thủ và GreenNode đang bị STALE (>30 ngày). Mọi phân tích TCO hiện tại đều dựa trên giả định giá không đổi, có thể dẫn đến sai lệch trong chiến lược đấu thầu.
- Không thể xác định được hidden cost (egress, LB, NAT) của đối thủ do scrape thất bại, làm giảm độ chính xác của bài toán TCO so sánh.
- AWS đang tung ra các tính năng bảo mật mới (control plane egress) và phần cứng mới (Blackwell) mà đối thủ nội địa chưa công bố tương đương, tạo rủi ro về 'feature gap' trong các deal Enterprise.

## Gaps / Thiếu dữ liệu

- Cần cập nhật: greennode/2026-05-20_greennode-vks_product-overview.md — dữ liệu cũ, chưa dùng được cho phân tích TCO mới.
- Không fetch được trang pricing của Viettel Cloud, FPT Cloud, Bizfly Cloud (scrape 2026-06-28). Cần retry với tool scrape chuyên sâu hoặc manual check để lấy số liệu giá mới.
- Thiếu dữ liệu về giá GPU (H100/A100/Blackwell) của GreenNode và đối thủ để phân tích scenario S4 (AI Inference) và S5 (AI Training).
- Thiếu thông tin về chính sách Reserved Instances/Committed Use Discount mới nhất của đối thủ nội địa.
