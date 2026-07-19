# Competitor Summary — 2026-07-19

Source: competitor-monitor run | Model: qwen/qwen3-5-27b

## Key Findings

- [Blog] FPT Cloud | https://fptcloud.com/fpt-kubernetes-engine-v2-13-2-nang-cap-van-hanh-cloud-native-toi-uu-gpu-cho-ai-workload | published_at=2026-07-17
- [Blog] Bizfly Cloud | https://bizflycloud.vn/tin-tuc/huong-dan-claude-code-trong-claude-fable-5-20260719175959671.htm | published_at=2026-07-19
- [RSS] AWS Artificial Intelligence | https://aws.amazon.com/blogs/machine-learning/introducing-grok-on-amazon-bedrock | published_at=2026-07-16
- [RSS] Vietnam.vn | https://news.google.com/rss/articles/CBMilwFBVV95cUxPOXN3b3h6cDJLSmxVN1BXMHg3S01OUnhreTdhZ0ZsVjlQY1AxbHI1RnZRcTFQaGMyOGRsaVd1Vmh3U0xBS0c4U3UzZkppNjZlcHRZU2NWS25lZG9fVTloLTFOMXFETDY2b09ILXF6SDJXWnZkOTRBS1drZ24xNTk4cExvZ0NYUlB6UjZNekIzNmRuNXVIRlBJ | published_at=2026-07-17

## Risks

- {"risk": "Feature Gap về AI Management Layer", "description": "Đối thủ (FPT, Bizfly) đang marketing mạnh mẽ các tính năng AI ứng dụng cụ thể. GreenNode VKS hiện chủ yếu tập trung vào hạ tầng K8s thuần túy theo hồ sơ workspace cũ (2026-05-20).\n**Khuyến nghị:** Cần xác minh xem VKS có layer quản lý model hay không. Nếu không, đây là điểm yếu khi đấu thầu các gói 'AI Solution' trọn gói.", "confidence": "medium"}
- {"risk": "Dữ liệu Pricing & SLA chưa cập nhật", "description": "Các trang scrape của Viettel/Bizfly/FPT (19/07/2026) chỉ trả về CSS/HTML, không có thông tin giá mới. Không thể so sánh TCO chính xác tuần này.\n**Khuyến nghị:** Yêu cầu `pricing_agent` chạy crawl chuyên sâu vào bảng giá chi tiết của FPT FKE và Bizfly BKE.", "confidence": "high"}

## Gaps / Thiếu dữ liệu

- Cần cập nhật: Dữ liệu scrape trang sản phẩm Viettel IDC, Bizfly BKE, FPT FKE (19/07/2026) — chỉ thu thập được code nguồn, không đọc được nội dung pricing/feature matrix. Không dùng để đưa ra claim về giá.
- Cần xác minh: Chứng nhận Công nghệ cao của FPT Cloud — Workspace memory (2026-07-14) đề cập FPT có bài viết 'Make in Vietnam', nhưng chưa có bằng chứng cụ thể về chứng nhận tương đương GreenNode (TP.HCM) để so sánh head-to-head.
