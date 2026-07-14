# Competitor Summary — 2026-07-14

Source: daily-intelligence run | Model: qwen/qwen3-5-27b

## Key Findings

- [RSS] [FPT Cloud](https://fptcloud.com/doanh-nghiep-van-hanh-ai-tren-ha-tang-make-in-viet-nam-lam-chu-cong-nghe-canh-tranh-toan-cau) 2026-07-13 — FPT công bố bài viết về vận hành AI trên hạ tầng 'Make in Viet Nam'. Tác động: Cạnh tranh trực tiếp vào luận điểm Sovereign AI của GreenNode. Khách hàng Gov/Enterprise sẽ so sánh cam kết định vị nội địa giữa FPT và GreenNode. GreenNode nên: Chuẩn bị battlecard so sánh chứng nhận Công nghệ cao TP.HCM (GreenNode) vs các chứng nhận tương đương của FPT; nhấn mạnh tính tuân thủ Luật BVDLCN 2025 trong tài liệu bán hàng.
- [RSS] [AWS Artificial Intelligence Blog](https://aws.amazon.com/blogs/machine-learning/openai-gpt-5-6-sol-terra-and-luna-are-now-generally-available-on-amazon-bedrock) 2026-07-13 — AWS đưa GPT-5.6 Sol/Terra/Luna lên Amazon Bedrock GA. Tác động: Nâng cao kỳ vọng về khả năng truy cập mô hình mới nhất cho khách hàng doanh nghiệp. Nếu GreenNode chỉ cung cấp K8s thuần mà không có layer AI model access, có thể bị coi là thiếu tính năng 'AI-ready'. GreenNode nên: Đánh giá lại roadmap tích hợp marketplace mô hình AI hoặc partner với nhà cung cấp model local để bù đắp khoảng cách này.
- [RSS] [AWS Containers Blog](https://aws.amazon.com/blogs/containers/accessing-private-git-repositories-from-amazon-eks-capability-for-argo-cd) 2026-07-13 — AWS hướng dẫn tích hợp Argo CD với private Git repo qua CodeConnections trên EKS. Tác động: Khẳng định tiêu chuẩn bảo mật GitOps cho workload nhạy cảm. Khách hàng ngân hàng/chính phủ sẽ yêu cầu khả năng tương tự trên VKS. GreenNode nên: Kiểm tra xem VKS đã hỗ trợ native integration với private Git server (tương tự CodeConnections) hay chưa; nếu chưa, cần ghi rõ giải pháp workaround trong docs.
- [RSS] [Kubernetes Blog](https://kubernetes.io/blog/2026/07/13/introducing-headlamp-plugin-for-kubeflow) 2026-07-13 — Kubernetes giới thiệu plugin Headlamp cho Kubeflow để quản lý AI/ML workloads. Tác động: Xu hướng chuyển dịch UI quản lý K8s sang Headlamp thay vì Dashboard cũ. GreenNode nên: Đảm bảo VKS hỗ trợ deploy Headlamp dễ dàng hoặc tích hợp sẵn như một option observability để tăng trải nghiệm người dùng.

## Gaps / Thiếu dữ liệu

- Cần xác minh: Viettel IDC RSS feed trả về item trống/snippet HTML anchor, không đọc được nội dung tin tức cụ thể. Không thể đánh giá động thái mới của Viettel VKS/vOKS.
- Cần xác minh: Bài viết FPT Cloud (2026-07-13) có snippet rỗng trong evidence bundle. Chỉ dựa vào tiêu đề để phân tích, thiếu chi tiết về sản phẩm cụ thể họ đang quảng bá.
- Dữ liệu pricing: Không có thông tin thay đổi giá cả nào từ đối thủ trong 24h qua. Dữ liệu pricing hiện tại vẫn dựa trên snapshot cũ (tham chiếu memory).
