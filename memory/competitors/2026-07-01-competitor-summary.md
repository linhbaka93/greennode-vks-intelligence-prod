# Competitor Summary — 2026-07-01

Source: competitor-monitor run | Model: qwen/qwen3-5-27b

## Key Findings

- [RSS] [AWS Containers Blog](https://aws.amazon.com/blogs/containers/announcing-amazon-eks-rollback-for-safe-and-reliable-management-of-cluster-upgrades) 2026-07-01 — AWS công bố Amazon EKS Version Rollback, cho phép rollback upgrade K8s version trong vòng 7 ngày mà không cần rebuild cluster. — Tác động: Tăng tiêu chuẩn về 'operational safety' cho Managed K8s. Khách hàng Enterprise/Gov sẽ kỳ vọng khả năng phục hồi nhanh khi upgrade lỗi.
GreenNode nên: Đánh giá lại quy trình upgrade VKS; nếu chưa có rollback tự động, cần ghi rõ SLA recovery time hoặc phát triển tính năng tương đương để giảm churn risk.
- [RSS] [CNCF Blog](https://www.cncf.io/blog/2026/07/01/understanding-dynamic-resource-allocation-in-kubernetes) 2026-07-01 — Dynamic Resource Allocation (DRA) đạt GA trong Kubernetes v1.35; NVIDIA dra-driver-nvidia-gpu chuyển sang SIGs. — Tác động: DRA là xu hướng bắt buộc cho workload AI/GPU hiệu quả cao. Nếu GreenNode VKS hỗ trợ DRA sớm hơn đối thủ VN, đây là lợi thế kỹ thuật lớn.
GreenNode nên: Kiểm tra roadmap VKS về DRA support; nếu đã có, đưa vào battlecard như điểm khác biệt 'AI-native infrastructure'.
- [RSS] [Bizfly Cloud News](https://bizflycloud.vn/tin-tuc/kubernetes-136-haru-giai-thich-chi-tiet-20260629145644358.htm) 2026-06-29 — Bizfly Cloud đăng bài giải thích chi tiết Kubernetes 1.36 (Haru), cùng các bài về Kafka, API performance. — Tác động: Bizfly đang đẩy mạnh developer engagement qua content kỹ thuật sâu, cạnh tranh trực tiếp với GreenNode về uy tín cộng đồng.
GreenNode nên: Tăng tần suất blog kỹ thuật (không chỉ digest sản phẩm); cân nhắc series 'Deep Dive' về K8s versions mới để giữ chân DevOps audience.
- [Scrape] Viettel IDC | https://viettelcloud.vn/san-pham/kubernetes | fetched_at=2026-07-01 — Trang sản phẩm VKS/vOKS trả về nội dung HTML/CSS không parse được text chính sách/giá. — Tác động: Không xác minh được thay đổi pricing/feature gần nhất của Viettel IDC từ nguồn public.
GreenNode nên: Yêu cầu team Sales/Partner cung cấp thông tin internal về deal Viettel gần đây; không dùng dữ liệu cũ để so sánh TCO.

## Risks

- ❌ **Feature Gap - Cluster Upgrade Safety**: AWS EKS Rollback tạo áp lực lên GreenNode VKS nếu chưa có cơ chế rollback tự động tương đương. Khách hàng Gov/Bank coi trọng tính ổn định khi upgrade major version.
- ⚠️ **Data Stale - Competitor Specs**: Profile Viettel/FPT/CMC trong workspace có thể đã cũ (last updated trước tháng 6). Scrape hiện tại không lấy được nội dung mới, gây rủi ro so sánh sai lệch về K8s version hoặc SLA.

## Gaps / Thiếu dữ liệu

- Cần cập nhật: `competitors/2026-06-xx-viettel-idc-profile.md` — Dữ liệu cũ, scrape thất bại, chưa xác minh được pricing/feature mới nhất của Viettel IDC VKS.
- Cần cập nhật: `competitors/2026-06-xx-fpt-cloud-profile.md` — Chưa có evidence mới về FKE pricing hoặc region expansion.
- Thiếu dữ liệu: CMC Cloud K8s — Không có tin mới trong 3 ngày qua, cần refresh từ nguồn khác ngoài RSS Google News.
