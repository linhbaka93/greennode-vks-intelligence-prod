# Pricing Summary — 2026-06-21

Source: competitor-monitor run | Model: qwen/qwen3-5-27b

## Key Findings

- [RSS] [AWS News Blog](https://aws.amazon.com/blogs/aws/announcing-amazon-ec2-g7-instances-accelerated-by-nvidia-rtx-pro-4500-blackwell-server-edition-gpus) 2026-06-18 — AWS công bố GA EC2 G7 instances với GPU NVIDIA RTX PRO 4500 Blackwell Server Edition. Tác động: ❌ Feature gap về phần cứng AI inference. AWS cung cấp lợi thế hiệu năng/giá ngay lập tức cho LLM inference nặng. GreenNode đang thua nếu khách hàng cần performance tối đa cho training/inference mà không có ràng buộc data residency VN. GreenNode cần rà soát roadmap GPU (A100/H100/Blackwell) để tránh mất khách hàng cần performance tối đa.
- [RSS] [AWS Blog](https://aws.amazon.com/blogs/machine-learning/introducing-web-search-on-amazon-bedrock-agentcore) 2026-06-19 — AWS công bố GA tính năng Web Search trên Amazon Bedrock AgentCore, cho phép các agent AI truy cập web an toàn và tích hợp RAG pipeline doanh nghiệp. Tác động: ❌ Feature gap về AI Agent infrastructure. AWS cung cấp giải pháp 'end-to-end' cho RAG và Agent mà VKS chưa có. Khách hàng Enterprise muốn triển khai AI nhanh có thể chọn AWS nếu không cần data residency VN.
- [Scrape] Viettel Cloud | https://viettelcloud.vn/san-pham/kubernetes | fetched_at=2026-06-21 — Trang sản phẩm vOKS không hiển thị bảng giá công khai (pricing contact-only). Tác động: ⚠️ Không thể so sánh TCO trực tiếp. Viettel tiếp tục chiến lược giá ẩn (sales-led), tạo rủi ro cho GreenNode trong các deal Enterprise nếu không có dữ liệu benchmark nội bộ.
- [Scrape] FPT Cloud | https://fptcloud.com/kubernetes | fetched_at=2026-06-21 — Trang sản phẩm FKE không hiển thị bảng giá công khai. Tác động: ⚠️ Không thể so sánh TCO trực tiếp. FPT tiếp tục chiến lược giá ẩn, tập trung vào bán hàng trực tiếp cho Enterprise/SOE.
- [Scrape] Bizfly Cloud | https://bizflycloud.vn/kubernetes | fetched_at=2026-06-21 — Trang sản phẩm BKE không hiển thị bảng giá công khai chi tiết. Tác động: ⚠️ Không thể so sánh TCO trực tiếp. Bizfly có thể đang dùng chiến lược giá linh hoạt cho SME nhưng thiếu minh bạch công khai.

## Recommended Actions

- Talk track cho Sales: Nhấn mạnh lợi thế Sovereign AI (Data Residency, Compliance với Luật BVDLCN 2025) thay vì cạnh tranh trực tiếp về hiệu năng GPU với AWS. Đối với khách hàng cần AI inference nặng, đề xuất hybrid model (training/inference nặng trên AWS, data storage/compliance trên GreenNode).
- Pricing recommendation: Không giảm giá list price cho VKS. Thay vào đó, tập trung vào bundling (VKS + AI Agent services + Compliance support) để tăng giá trị tổng thể (value-based pricing).
- Theo dõi thêm: Rà soát roadmap GPU của GreenNode và so sánh với AWS G7. Nếu có GPU tương đương, cần công bố ngay để giảm feature gap.
- Yêu cầu Sales Ops cung cấp quote mẫu từ Viettel, FPT, Bizfly để xây dựng TCO benchmark nội bộ.

## Risks

- Dữ liệu pricing của GreenNode và đối thủ local là 'contact-only' hoặc không công khai, gây khó khăn cho việc xây dựng TCO chuẩn hóa (normalized TCO) để so sánh trực tiếp.
- AWS ra mắt GPU Blackwell (G7) tạo áp lực về hiệu năng/giá cho workload AI inference. Nếu GreenNode không có GPU tương đương hoặc roadmap rõ ràng, sẽ mất khách hàng cần performance tối đa.
- Thiếu dữ liệu về hidden cost (egress, LB, NAT) của đối thủ local khiến việc so sánh TCO toàn phần không chính xác.
- Dữ liệu pricing trong workspace (2026-05-20) có thể đã cũ, cần cập nhật ngay để tránh đưa ra khuyến nghị sai lệch.

## Gaps / Thiếu dữ liệu

- Cần cập nhật: greennode/2026-05-20_greennode-vks_product-overview.md — dữ liệu pricing cũ, chưa dùng được cho phân tích TCO mới.
- Thiếu dữ liệu pricing công khai từ Viettel vOKS, FPT FKE, Bizfly BKE — cần scrape sâu hơn hoặc yêu cầu Sales Ops cung cấp quote mẫu.
- Thiếu thông tin về roadmap GPU của GreenNode (A100/H100/Blackwell) để đánh giá khả năng cạnh tranh với AWS G7.
- Thiếu dữ liệu về hidden cost (egress, LB, NAT) của các đối thủ local để tính toán TCO chính xác.
