# Pricing Summary — 2026-07-07

Source: competitor-monitor run | Model: qwen/qwen3-5-27b

## Key Findings

- [RSS] [AWS Containers Blog](https://aws.amazon.com/blogs/containers/full-request-and-response-compliance-logging-on-amazon-eks) 2026-07-07 — AWS tung giải pháp logging tuân thủ đầy đủ trên EKS bằng Envoy ext_proc. Tác động: Nâng tiêu chuẩn compliance cho khách hàng Enterprise/Gov. GreenNode nên: Đánh giá xem VKS có hỗ trợ audit trail tương đương mà không cần code custom; nếu có, đây là điểm bán hàng mạnh để bù đắp chênh lệch giá với hyperscaler.
- [Workspace] competitors/2026-07-03-competitor-summary.md — AWS ra mắt EKS Version Rollback (2026-07-01), cho phép rollback upgrade K8s trong 7 ngày. Tác động: Tăng kỳ vọng về 'operational safety'. Nếu VKS chưa có tính năng này, rủi ro churn tăng ở phân khúc ngân hàng/chính phủ. GreenNode nên: Kiểm tra SLA recovery time hiện tại hoặc lên kế hoạch roadmap tính năng rollback tự động.
- [Scrape] Viettel/Bizfly/FPT | https://viettelcloud.vn/san-pham/kubernetes | fetched_at=2026-07-07 — Các trang pricing Kubernetes của đối thủ nội địa (Viettel, Bizfly, FPT) trả về mã CSS/JS, không trích xuất được bảng giá. Tác động: Không thể tính toán TCO chính xác. GreenNode nên: Yêu cầu Sales Ops cung cấp bảng giá nội bộ mới nhất để xây dựng battlecard TCO thực tế.
- [Blog] GreenNode | https://greennode.ai/blog/agentbase-ai-coding-layer-suport-claude-code-and-openai | published_at=2026-07-04 — GreenNode công bố AgentBase AI Coding Layer. Tác động: Mở rộng doanh thu sang mảng AI Infrastructure. GreenNode nên: Xác định mô hình định giá cho AgentBase (pay-per-token hay subscription) để tránh cannibalize VKS revenue.

## Recommended Actions

- Talk Track: Nhấn mạnh 'Total Value of Ownership' bao gồm Data Residency (Luật BVDLCN 2025) + Support tiếng Việt + Uptime SLA, thay vì chỉ so sánh giá instance/giờ.
- Pricing Recommendation: Xây dựng gói 'Compliance Bundle' cho VKS bao gồm tính năng logging/audit trail (nếu có) để cạnh tranh trực tiếp với tính năng mới của AWS EKS.
- Internal Action: Làm việc với Finance/Product để có bảng giá nội bộ mới nhất (cập nhật Q3 2026) nhằm hoàn thiện TCO calculator cho Sales.

## Risks

- Dữ liệu pricing đối thủ bị che khuất (JS-rendered hoặc login wall), dẫn đến ước tính TCO thiếu chính xác.
- Tính năng EKS Rollback của AWS tạo áp lực buộc GreenNode phải đầu tư R&D để giữ chân khách hàng Enterprise.
- Thiếu thông tin về chi phí egress và storage của VKS trong workspace memory hiện tại.

## Gaps / Thiếu dữ liệu

- Cần cập nhật: Bảng giá chi tiết VKS (Compute, Storage, Egress) — Dữ liệu hiện tại trong memory chỉ là tổng quan sản phẩm (2026-05-20), chưa có số liệu giá cụ thể.
- Cần xác minh: Giá GPU inference/training của VKS so với AWS Bedrock/SageMaker — Chưa có evidence về pricing model AI workload.
- Cần fetch lại: Trang pricing của Viettel IDC, FPT Cloud, Bizfly Cloud — Lần scrape trước đó không lấy được nội dung giá.
