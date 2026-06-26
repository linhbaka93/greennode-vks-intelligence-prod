# Competitor Summary — 2026-06-26

Source: competitor-monitor run | Model: qwen/qwen3-5-27b

## Key Findings

- [RSS] [AWS HPC Blog](https://aws.amazon.com/blogs/hpc/transforming-hpc-operations-with-intelligent-workload-orchestration-on-aws) 2026-06-26 — AWS công bố giải pháp orchestration workload thông minh cho HPC, tự động hóa quy trình tính toán thay vì cấu hình thủ công, giúp giảm chi phí vận hành đáng kể cho các tổ chức chạy workload HPC/AI nặng. — Tác động tới GreenNode: ⚠️ Feature gap về tự động hóa HPC. Khách hàng Enterprise/Gov có workload HPC/AI nặng sẽ thấy AWS giảm chi phí vận hành đáng kể so với mô hình thủ công của GreenNode VKS.
- [RSS] [AWS Containers Blog](https://aws.amazon.com/blogs/containers/faster-nodes-smarter-scaling-whats-new-inside-amazon-elastic-kubernetes-service-amazon-eks-auto-mode) 2026-06-23 — AWS nâng cấp EKS Auto Mode với cải tiến hiệu năng và khả năng mở rộng trên 4 trụ cột: runtime, compute, storage, networking, giúp tối ưu chi phí và vận hành node tự động. — Tác động tới GreenNode: ⚠️ Feature gap về tự động hóa và tối ưu hóa chi phí. EKS Auto Mode giúp khách hàng giảm vận hành và chi phí node; GreenNode cần cân nhắc nếu VKS chưa có tính năng auto-scaling node pool thông minh tương đương.
- [RSS] [AWS News Blog](https://aws.amazon.com/blogs/aws/announcing-amazon-ec2-g7-instances-accelerated-by-nvidia-rtx-pro-4500-blackwell-server-edition-gpus) 2026-06-18 — AWS công bố GA EC2 G7 instances với GPU NVIDIA RTX PRO 4500 Blackwell Server Edition cho AI inference và graphics, mang lại lợi thế hiệu năng ngay lập tức cho LLM inference nặng. — Tác động tới GreenNode: ❌ Feature gap về phần cứng GPU thế hệ mới. AWS cung cấp lợi thế hiệu năng ngay lập tức cho LLM inference nặng. GreenNode đang thua nếu khách hàng cần performance tối đa cho training/inference mà không có ràng buộc data residency VN.
- [RSS] [AWS Containers Blog](https://aws.amazon.com/blogs/containers/amazon-eks-now-supports-control-plane-egress-through-your-vpc) 2026-06-22 — AWS EKS ra mắt tính năng 'customer-routed control plane egress', cho phép định tuyến toàn bộ traffic control plane (admission webhooks, OIDC lookups) qua VPC của khách hàng thay vì internet public. — Tác động tới GreenNode: ❌ Feature gap nghiêm trọng về bảo mật và kiến trúc mạng cho phân khúc Enterprise/Gov. Khách hàng tài chính/chính phủ yêu cầu control plane traffic không ra internet sẽ ưu tiên AWS nếu GreenNode chưa có giải pháp tương đương (Private Link cho control plane).
- [RSS] [FPT Cloud Blog](https://fptcloud.com/3-yeu-to-cot-loi-danh-gia-hieu-nang-cua-ha-tang-cloud) 2026-06-25 — FPT Cloud đăng tải bài viết về 3 yếu tố cốt lõi đánh giá hiệu năng hạ tầng Cloud và hành trình tái kiến trúc hạ tầng cho workload hiệu năng cao, tập trung vào messaging về hiệu năng và khả năng mở rộng. — Tác động tới GreenNode: ⚠️ Tín hiệu GTM: FPT Cloud đang định vị mạnh mẽ về hiệu năng hạ tầng cho workload cao. Có thể tạo áp lực cạnh tranh về messaging với GreenNode trong phân khúc Enterprise cần hiệu năng cao.
- [RSS] [GreenNode Blog](https://greennode.ai/blog/agentbase-supported-frameworks-langgraph-crewai-llamaindex) 2026-06-25 — GreenNode tiếp tục xuất bản nội dung về AgentBase, IDP và chiến lược multi-cloud cho SME, củng cố vị thế trong phân khúc AI Agent và xử lý tài liệu thông minh. — Tác động tới GreenNode: ✅ Lợi thế về nội dung và giáo dục thị trường. GreenNode đang dẫn đầu trong việc cung cấp giải pháp AI Agent và IDP cho doanh nghiệp Việt, tạo sự khác biệt so với đối thủ nội địa chưa có giải pháp tương tự.

## Risks

- Feature gap về GPU Blackwell và HPC orchestration so với AWS có thể làm mất khách hàng Enterprise cần performance tối đa.
- Thiếu tính năng 'customer-routed control plane egress' có thể làm giảm khả năng cạnh tranh với AWS trong phân khúc Gov/Finance yêu cầu bảo mật cao.
- FPT Cloud đang tăng cường messaging về hiệu năng hạ tầng, có thể tạo áp lực cạnh tranh về perception với GreenNode.

## Gaps / Thiếu dữ liệu

- Cần cập nhật: competitors/2026-06-17_bizfly-bke_profile.md — dữ liệu cũ, chưa dùng được.
- Cần cập nhật: competitors/2026-06-17_fpt-cloud-fke_profile.md — dữ liệu cũ, chưa dùng được.
- Cần cập nhật: competitors/2026-06-17_aws-eks_profile.md — dữ liệu cũ, chưa dùng được.
- Cần cập nhật: competitors/2026-06-17_viettel-voks_profile.md — dữ liệu cũ, chưa dùng được.
- Không có dữ liệu pricing mới từ đối thủ Tier 1 nội địa trong 3 ngày qua; cần scrape trang pricing của Viettel, FPT, Bizfly để cập nhật.
