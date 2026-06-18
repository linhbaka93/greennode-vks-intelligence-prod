# Regulatory Summary — 2026-06-18

Source: competitor-monitor run | Model: qwen/qwen3-5-27b

## Key Findings

- [Workspace] regulatory/vietnam-compliance.md — [Không có tin mới về văn bản pháp lý] Trong cửa sổ 3 ngày (16–18/06/2026), không có thông báo chính thức nào từ cơ quan nhà nước hoặc nguồn tin cậy về việc ban hành, sửa đổi Luật BVDLCN 2025, Nghị định 356/2025/NĐ-CP, hay các quy định mới về AI/Cloud tại Việt Nam. Các tin tức hiện có tập trung vào hoạt động kinh doanh (hợp tác MSB-GreenNode) và công nghệ (AWS, CNCF).
- [RSS] Vietnam.vn | https://news.google.com/rss/articles/CBMikgFBVV95cUxQV2ExNGdzR1BneXhBNUhxMDNVY3dMZXhlUGlvcWFBYUk2OVZZdFJqTUZuY3NzdWUtWHZvUTJvZW1rZElGSWRzendwNlFfVEdNMjRoVUI2eExHeHQxTUtUWjJnaGxEdHlhSjdmM2UzdDhCVVlzZ3A4YldMcHZ5QmRUS0ZKWmpzWVpZX1hFVGdSd2Y0QQ | published_at=2026-06-17 — [RSS] [Vietnam.vn](https://news.google.com/rss/articles/CBMikgFBVV95cUxQV2ExNGdzR1BneXhBNUhxMDNVY3dMZXhlUGlvcWFBYUk2OVZZdFJqTUZuY3NzdWUtWHZvUTJvZW1rZElGSWRzendwNlFfVEdNMjRoVUI2eExHeHQxTUtUWjJnaGxEdHlhSjdmM2UzdDhCVVlzZ3A4YldMcHZ5QmRUS0ZKWmpzWVpZX1hFVGdSd2Y0QQ) 2026-06-17 — MSB Bank hợp tác chiến lược với GreenNode để vận hành hàng trăm ứng dụng AI, đánh dấu bước chuyển từ 'digital banking' sang 'AI banking'.
- [Suy luận] Cơ sở: [Workspace] regulatory/vietnam-compliance.md + [RSS] AWS News Blog (2026-06-17) — [Suy luận] Dựa trên [Workspace] regulatory/vietnam-compliance.md (Luật BVDLCN 2025 hiệu lực 01/01/2026) và [RSS] tin tức về AWS ra mắt các tính năng AI mới (Bedrock AgentCore, SageMaker) — AWS đang đẩy mạnh narrative về 'AI-native' nhưng không thể đáp ứng yêu cầu lưu trữ dữ liệu cá nhân người VN trong lãnh thổ VN một cách trực tiếp (trừ khi dùng hybrid hoặc partner).

## Recommended Actions

- {"target": "Sales & Marketing", "action": "Tạo tài liệu 'Compliance & Sovereignty Playbook' cho ngành Ngân hàng, sử dụng case study MSB Bank và trích dẫn Luật BVDLCN 2025 để chứng minh GreenNode là lựa chọn duy nhất an toàn cho AI banking tại VN.", "priority": "High", "timeline": "Trong 2 tuần tới"}
- {"target": "Product", "action": "Rà soát lại tính năng 'Private VPC' và 'Data Residency' của VKS để đảm bảo tài liệu kỹ thuật (docs) nêu rõ việc dữ liệu không bao giờ rời khỏi VN, đáp ứng yêu cầu của Nghị định 356/2025/NĐ-CP.", "priority": "Medium", "timeline": "Trước Q3 2026"}
- {"target": "Legal/Compliance", "action": "Theo dõi sát sao các thông tư hướng dẫn mới của Bộ Công Thương và Ngân hàng Nhà nước về AI trong tháng 7/2026, đặc biệt là các quy định về mô hình AI được phép sử dụng trong ngân hàng.", "priority": "Medium", "timeline": "Liên tục"}

## Gaps / Thiếu dữ liệu

- Cần cập nhật: regulatory/vietnam-compliance.md — File ghi chú 'Cập nhật tiếp theo: 2026-07-24'. Cần xác nhận xem có thông tư hướng dẫn mới nào về AI hoặc dữ liệu tài chính (SBV) trong tháng 6/2026 hay không, vì tin tức hiện tại chưa đề cập cụ thể đến văn bản mới.
- Cần xác minh: Chi tiết hợp đồng MSB-GreenNode — Tin tức chỉ nêu 'hợp tác chiến lược' và 'hàng trăm ứng dụng AI'. Cần làm rõ phạm vi (on-prem, private cloud, hay hybrid) để định vị chính xác giải pháp VKS trong case study.
