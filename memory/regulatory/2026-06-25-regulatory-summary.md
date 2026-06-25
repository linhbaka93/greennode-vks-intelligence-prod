# Regulatory Summary — 2026-06-25

Source: competitor-monitor run | Model: qwen/qwen3-5-27b

## Key Findings

- [Chưa xác minh] Không có văn bản pháp lý mới hoặc cập nhật quy định nào về data residency, bảo mật cloud, hay AI tại Việt Nam được ghi nhận trong dữ liệu đầu vào (evidence_bundle) trong cửa sổ 3 ngày qua (22/06 - 25/06/2026).
- [Suy luận] Dựa trên các bài báo từ Vietnam.vn về 'cuộc đua data center' và 'AI tại TP.HCM' (23/06 - 25/06), xu hướng chính sách vẫn tập trung vào việc thúc đẩy hạ tầng số nội địa và an ninh mạng, củng cố lợi thế của các nhà cung cấp có data center tại Việt Nam.
- [Suy luận] Các đối thủ hyperscaler (AWS) đang tập trung vào tính năng kỹ thuật nâng cao (EKS Auto Mode, Control Plane Egress qua VPC) thay vì thay đổi chính sách pháp lý. Điều này cho thấy áp lực cạnh tranh hiện tại nằm ở mặt kỹ thuật và TCO, không phải thay đổi quy định.

## Recommended Actions

- {"target": "Legal/Compliance Team", "action": "Xác nhận lại tình trạng hiệu lực của các văn bản pháp lý hiện hành (Luật BVDLCN 2025, Nghị định 13/2023) và kiểm tra xem có văn bản mới nào đang trong giai đoạn dự thảo hoặc ban hành chưa được công bố trên các kênh tin tức đại chúng.", "priority": "High"}
- {"target": "Product Team", "action": "Rà soát lại tài liệu kỹ thuật về tính năng bảo mật mạng (Network Security) và khả năng định tuyến traffic nội bộ của VKS để chuẩn bị câu trả lời cho các RFP yêu cầu cao về data sovereignty và network isolation.", "priority": "Medium"}
- {"target": "Sales/Marketing", "action": "Sử dụng các bài báo về xu hướng phát triển data center tại VN (từ Vietnam.vn) để củng cố narrative về 'Sovereign AI/Cloud' trong các cuộc họp với khách hàng khu vực công và tài chính.", "priority": "Low"}

## Gaps / Thiếu dữ liệu

- Cần cập nhật: Không có dữ liệu mới về văn bản pháp lý cụ thể (Nghị định, Thông tư, Luật) trong evidence_bundle. Các bài báo từ Vietnam.vn chỉ mang tính chất tin tức tổng quan về xu hướng, không trích dẫn số hiệu văn bản mới.
- Cần xác minh: Các file profile đối thủ (Viettel IDC, FPT Cloud, Bizfly Cloud) trong workspace bị đánh dấu [STALE] (cũ từ 2026-06-17). Cần cập nhật lại để so sánh chính xác năng lực tuân thủ của đối thủ nội địa.
- Cần xác minh: Không có thông tin cụ thể về các thông tư hướng dẫn Luật BVDLCN 2025 (nếu có) trong dữ liệu đầu vào. Cần truy vấn trực tiếp các nguồn chính phủ hoặc Legal team để có thông tin chính xác.
