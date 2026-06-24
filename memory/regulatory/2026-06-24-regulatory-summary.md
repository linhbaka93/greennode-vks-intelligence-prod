# Regulatory Summary — 2026-06-24

Source: competitor-monitor run | Model: qwen/qwen3-5-27b

## Key Findings

- evidence_bundle.items (không có mục nào thuộc loại [RSS] từ nguồn pháp lý chính phủ hoặc [Scrape] từ thuvienphapluat.vn, moitruongphaply.vn) — [Chưa xác minh] Không có văn bản pháp lý mới (Nghị định, Thông tư, Luật) nào được công bố trong 3 ngày qua (21/06/2026 – 24/06/2026) liên quan trực tiếp đến quy định data residency, bảo mật cloud, hoặc AI tại Việt Nam.
- [RSS] [Vietnam.vn](https://news.google.com/rss/articles/CBMinwFBVV95cUxOSGVIQkYza2NGeklzU1BXYk1SMHlZalNNRWgtdmE0ODhLUWJEQ25pTi1yczIxVHhWSkFsbVRWYmFfZEFsdXdwVjJUZk9sdXhaTmdGVGE4cWhyQ3k0MWN5SmJUQ2JsN29kenlnWWw1WjRLbjNsN1JEc0cxRnNuOXpvRGFyLXRpTGhCejBURmw2Z2JoMTE0bko1dDN3eVpGMnc?oc=5) 2026-06-23 — 'Ho Chi Minh City: A new growth pole for data centers, cloud computing, and AI.' — [Suy luận] Xu hướng 'Sovereign AI' và đầu tư hạ tầng data center tại Việt Nam tiếp tục được nhấn mạnh qua các bài báo tổng hợp (Vietnam.vn) về TP.HCM và khu vực Đông Nam Á, mặc dù không có văn bản luật mới.
- [RSS] [AWS Containers Blog](https://aws.amazon.com/blogs/containers/amazon-eks-now-supports-control-plane-egress-through-your-vpc) 2026-06-22 — [Suy luận] AWS công bố tính năng 'customer-routed control plane egress' cho EKS (22/06/2026), cho phép định tuyến lưu lượng control plane qua VPC của khách hàng. Đây là nâng cấp bảo mật quan trọng nhưng không thay thế được yêu cầu pháp lý về vị trí vật lý của dữ liệu.

## Recommended Actions

- {"target": "Sales & Marketing", "action": "Tận dụng xu hướng 'Sovereign AI' và đầu tư hạ tầng tại TP.HCM (từ tin Vietnam.vn) để củng cố luận điểm về sự cần thiết của cloud nội địa cho khách hàng regulated.", "priority": "Medium"}
- {"target": "Product & Competitive Intelligence", "action": "Cập nhật Battle Card đối với AWS EKS: Làm rõ tính năng 'control plane egress' mới của AWS là giải pháp bảo mật mạng, nhưng không thay thế được yêu cầu pháp lý về lưu trữ dữ liệu tại Việt Nam (Data Residency) mà GreenNode VKS đáp ứng.", "priority": "High"}
- {"target": "Compliance Team", "action": "Tiếp tục theo dõi các nguồn tin pháp lý chính thống hàng ngày để phát hiện sớm các văn bản mới (Nghị định, Thông tư) liên quan đến AI và dữ liệu.", "priority": "High"}

## Gaps / Thiếu dữ liệu

- Cần cập nhật: Không có dữ liệu mới từ các nguồn pháp lý chính thống (thuvienphapluat.vn, moitruongphaply.vn) trong evidence_bundle. Cần mở rộng query để bao gồm các nguồn này trong các lần chạy tiếp theo để đảm bảo không bỏ sót văn bản mới.
- Cần xác minh: Các bài báo trên Vietnam.vn về 'Sovereign AI' và 'Data Center race' chỉ mang tính chất tin tức tổng hợp, chưa trích dẫn văn bản pháp lý cụ thể. Cần xác minh xem có văn bản mới nào đi kèm hay chỉ là bình luận xu hướng.
