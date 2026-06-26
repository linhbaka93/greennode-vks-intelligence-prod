# Competitor Summary — 2026-06-26

Source: weekly-digest run | Model: qwen/qwen3-5-27b

## Key Findings

- [RSS] [AWS HPC Blog](https://aws.amazon.com/blogs/hpc/transforming-hpc-operations-with-intelligent-workload-orchestration-on-aws) 2026-06-26 — AWS công bố giải pháp orchestration workload thông minh cho HPC, tự động hóa quy trình tính toán thay vì cấu hình thủ công. — Tác động tới GreenNode: ⚠️ Feature gap về tự động hóa HPC. Khách hàng Enterprise/Gov có workload HPC/AI nặng sẽ thấy AWS giảm chi phí vận hành đáng kể so với mô hình thủ công của GreenNode VKS.
- [RSS] [AWS Containers Blog](https://aws.amazon.com/blogs/containers/amazon-eks-now-supports-control-plane-egress-through-your-vpc) 2026-06-22 — AWS EKS ra mắt 'customer-routed control plane egress', cho phép định tuyến toàn bộ traffic control plane (admission webhooks, OIDC) qua VPC của khách hàng. — Tác động tới GreenNode: ❌ Feature gap nghiêm trọng về bảo mật. Khách hàng tài chính/chính phủ yêu cầu control plane traffic không ra internet sẽ ưu tiên AWS nếu GreenNode chưa có giải pháp Private Link cho control plane.
- [RSS] [AWS News Blog](https://aws.amazon.com/blogs/aws/announcing-amazon-ec2-g7-instances-accelerated-by-nvidia-rtx-pro-4500-blackwell-server-edition-gpus) 2026-06-18 — AWS công bố GA EC2 G7 instances với GPU NVIDIA RTX PRO 4500 Blackwell Server Edition. — Tác động tới GreenNode: ❌ Feature gap về phần cứng GPU thế hệ mới. AWS có lợi thế hiệu năng ngay lập tức cho LLM inference nặng. GreenNode đang thua nếu khách hàng cần performance tối đa mà không bị ràng buộc data residency VN.
- [RSS] [FPT Cloud Blog](https://fptcloud.com/3-yeu-to-cot-loi-danh-gia-hieu-nang-cua-ha-tang-cloud) 2026-06-25 — FPT Cloud đăng bài về 3 yếu tố cốt lõi đánh giá hiệu năng hạ tầng Cloud. — Tác động tới GreenNode: ⚠️ Tín hiệu GTM. FPT đang định vị lại thông điệp về hiệu năng, có thể nhắm vào phân khúc khách hàng quan tâm đến benchmark và performance.
- [RSS] [AWS News Blog](https://aws.amazon.com/blogs/aws/aws-weekly-roundup-ny-summit-recap-local-zone-in-hanoi-grok-4-3-in-bedrock-price-reductions-and-more-june-22-2026) 2026-06-22 — AWS công bố giảm giá và mở rộng Local Zone tại Hà Nội. — Tác động tới GreenNode: ⚠️ Áp lực giá trực tiếp. Các workload không yêu cầu data residency nghiêm ngặt có thể chuyển sang AWS Local Zone Hà Nội do chênh lệch giá.

## Gaps / Thiếu dữ liệu

- Cần cập nhật: competitors/2026-06-17_bizfly-bke_profile.md — dữ liệu cũ, chưa dùng được cho so sánh chi tiết.
- Cần cập nhật: competitors/2026-06-17_fpt-cloud-fke_profile.md — dữ liệu cũ, chưa dùng được cho so sánh chi tiết.
- Cần cập nhật: competitors/2026-06-17_aws-eks_profile.md — dữ liệu cũ, chưa dùng được cho so sánh chi tiết.
- Cần cập nhật: competitors/2026-06-17_viettel-voks_profile.md — dữ liệu cũ, chưa dùng được cho so sánh chi tiết.
- Không có tin mới từ đối thủ Tier 1 nội địa (Viettel, FPT, Bizfly) trong 24h qua; cần theo dõi thêm các kênh social và news feed để phát hiện deal lớn hoặc công bố sản phẩm.
