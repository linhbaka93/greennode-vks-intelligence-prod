# Competitor Summary — 2026-06-21

Source: competitor-monitor run | Model: qwen/qwen3-5-27b

## Key Findings

- [RSS] AWS News Blog | https://aws.amazon.com/blogs/aws/announcing-amazon-ec2-g7-instances-accelerated-by-nvidia-rtx-pro-4500-blackwell-server-edition-gpus | published_at=2026-06-18 — [RSS] [AWS News Blog](https://aws.amazon.com/blogs/aws/announcing-amazon-ec2-g7-instances-accelerated-by-nvidia-rtx-pro-4500-blackwell-server-edition-gpus) 2026-06-18 — AWS công bố GA EC2 G7 instances với GPU NVIDIA RTX PRO 4500 Blackwell Server Edition cho AI inference và graphics. Tác động tới GreenNode: ❌ Feature gap về phần cứng GPU thế hệ mới. AWS cung cấp lợi thế hiệu năng ngay lập tức cho LLM inference nặng. GreenNode đang thua nếu khách hàng cần performance tối đa cho training/inference mà không có ràng buộc data residency VN. GreenNode cần rà soát roadmap GPU (A100/H100/Blackwell) để tránh mất khách hàng cần performance tối đa.
- [RSS] AWS Blog | https://aws.amazon.com/blogs/machine-learning/introducing-web-search-on-amazon-bedrock-agentcore | published_at=2026-06-19 — [RSS] [AWS Blog](https://aws.amazon.com/blogs/machine-learning/introducing-web-search-on-amazon-bedrock-agentcore) 2026-06-19 — AWS công bố GA tính năng Web Search trên Amazon Bedrock AgentCore, cho phép các agent AI truy cập web an toàn và tích hợp RAG pipeline doanh nghiệp. Tác động tới GreenNode: ❌ Feature gap về AI Agent infrastructure. AWS cung cấp giải pháp 'end-to-end' cho RAG và Agent mà VKS chưa có. Khách hàng Enterprise muốn triển khai AI nhanh có thể chọn AWS nếu không cần data residency VN.
- [Scrape] Viettel vOKS | https://viettelcloud.vn/san-pham/kubernetes | fetched_at=2026-06-21 — [Scrape] Viettel vOKS | https://viettelcloud.vn/san-pham/kubernetes | fetched_at=2026-06-21 — Không có thay đổi đáng kể trên trang sản phẩm vOKS so với lần scrape trước. Tác động tới GreenNode: ⚠️ Không có tín hiệu mới về pricing hoặc feature. GreenNode cần tiếp tục theo dõi các deal lớn của Viettel trong phân khúc Gov/SOE.
- [Scrape] FPT FKE | https://fptcloud.com/kubernetes | fetched_at=2026-06-21 — [Scrape] FPT FKE | https://fptcloud.com/kubernetes | fetched_at=2026-06-21 — Không có thay đổi đáng kể trên trang sản phẩm FKE so với lần scrape trước. Tác động tới GreenNode: ⚠️ Không có tín hiệu mới về pricing hoặc feature. GreenNode cần tiếp tục theo dõi các động thái của FPT trong phân khúc Enterprise VN.
- [Scrape] Bizfly BKE | https://bizflycloud.vn/kubernetes | fetched_at=2026-06-21 — [Scrape] Bizfly BKE | https://bizflycloud.vn/kubernetes | fetched_at=2026-06-21 — Không có thay đổi đáng kể trên trang sản phẩm BKE so với lần scrape trước. Tác động tới GreenNode: ⚠️ Không có tín hiệu mới về pricing hoặc feature. GreenNode cần tiếp tục theo dõi các động thái của Bizfly trong phân khúc SME.

## Risks

- ❌ Feature gap về phần cứng GPU thế hệ mới (Blackwell) so với AWS, có thể mất khách hàng cần performance tối đa cho AI inference không ràng buộc data residency.
- ❌ Feature gap về AI Agent infrastructure (RAG, Web Search) so với AWS, có thể mất khách hàng Enterprise muốn triển khai AI nhanh.
- ⚠️ Không có dữ liệu mới về pricing hoặc feature từ đối thủ Tier 1 nội địa (Viettel, FPT, Bizfly), cần tiếp tục theo dõi.

## Gaps / Thiếu dữ liệu

- Cần cập nhật: competitors/2026-06-17_viettel-voks_profile.md — dữ liệu cũ, chưa xác minh pricing và SLA.
- Cần cập nhật: competitors/2026-06-17_fpt-cloud-fke_profile.md — dữ liệu cũ, chưa xác minh GPU trên FKE.
- Cần cập nhật: competitors/2026-06-17_bizfly-bke_profile.md — dữ liệu cũ, chưa xác minh SLA và K8s versions.
