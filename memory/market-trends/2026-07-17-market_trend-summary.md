# Market Trend Summary — 2026-07-17

Source: weekly-digest run | Model: qwen/qwen3-5-27b

## Key Findings

- [RSS] [FPT Cloud](https://fptcloud.com/fpt-kubernetes-engine-v2-13-2-nang-cap-van-hanh-cloud-native-toi-uu-gpu-cho-ai-workload) 2026-07-17 — FPT ra mắt FPT Kubernetes Engine v2.13.2 với trọng tâm tối ưu GPU cho AI Workload. Tác động: Cạnh tranh trực tiếp về tính năng Managed K8s cho AI. GreenNode nên: So sánh spec GPU node pool và khả năng scheduling giữa VKS và FPT trong battlecard bán hàng.
- [RSS] [FPT Cloud](https://fptcloud.com/doanh-nghiep-van-hanh-ai-tren-ha-tang-make-in-viet-nam-lam-chu-cong-nghe-canh-tranh-toan-cau) 2026-07-13 — FPT đẩy mạnh thông điệp 'Make in Viet Nam' cho hạ tầng AI. Tác động: Gây áp lực lên luận điểm Sovereign AI của GreenNode. GreenNode nên: Nhấn mạnh chứng nhận Doanh nghiệp Công nghệ cao TP.HCM và tuân thủ Luật BVDLCN 2025 để phân biệt rõ ràng.
- [RSS] [GreenNode Blog](https://greennode.ai/blog/greennode-launches-han-1b-availability-zone-to-expand-ai-cloud-infrastructure) 2026-07-14 — GreenNode chính thức mở rộng Availability Zone HAN-1B. Tác động: Tăng khả năng disaster recovery và multi-region cho khách hàng Enterprise. GreenNode nên: Cập nhật tài liệu GTM ngay lập tức để quảng bá tính sẵn sàng cao (High Availability) mới này.
- [RSS] [CNCF Blog](https://www.cncf.io/blog/2026/07/09/navigating-the-ingress-nginx-retirement) 2026-07-09 — CNCF xác nhận landscape sau tháng 3/2026 khi ingress-nginx controller ngừng hỗ trợ đặc tính mới. Tác động: Rủi ro bảo mật và vận hành cho khách hàng VKS đang dùng legacy ingress. GreenNode nên: Gửi advisory proactively đề xuất migration path sang Gateway API hoặc Cilium.
- [RSS] [CNCF Blog](https://www.cncf.io/blog/2026/07/15/hami-becomes-a-cncf-incubating-project) 2026-07-15 — HAMi trở thành dự án incubating của CNCF, giải quyết vấn đề fragment GPU. Tác động: Chuẩn hóa công nghệ chia sẻ GPU trên K8s. GreenNode nên: Đánh giá tích hợp HAMi vào VKS để tối ưu chi phí GPU cho khách hàng inference.

## Recommended Actions

- Product Team: Đánh giá khả năng tích hợp HAMi vào GreenNode VKS để cải thiện hiệu quả sử dụng GPU (P1).
- Sales Enablement: Cập nhật Battlecard Sovereign AI so sánh Chứng nhận Công nghệ cao TP.HCM (GreenNode) vs FPT Cloud (P0).
- Customer Success: Gửi thông báo kỹ thuật (Advisory) cho tất cả khách hàng VKS đang dùng ingress-nginx về kế hoạch migration sang Gateway API/Cilium (P0).
- Marketing: Đẩy mạnh thông điệp về Availability Zone HAN-1B mới trong các case study DR/HA cho khách hàng Gov/Bank (P1).

## Risks

- Rủi ro churn từ khách hàng Enterprise nếu không có lộ trình migration rõ ràng khỏi ingress-nginx trước khi CVEs tích lũy.
- Áp lực định vị Sovereign AI khi FPT Cloud sử dụng thông điệp 'Make in Viet Nam' tương tự nhưng chưa rõ bằng chứng pháp lý cụ thể so với GreenNode.
- Khách hàng có thể bị thu hút bởi ưu đãi giá ngắn hạn của đối thủ (FPT tặng 03 tháng + chiết khấu) nếu không có counter-offer về TCO dài hạn.

## Gaps / Thiếu dữ liệu

- Chi tiết kỹ thuật cụ thể của FPT Kubernetes Engine v2.13.2 (snippet rỗng, chỉ có tiêu đề). Cần scrape trang sản phẩm để biết spec GPU cụ thể.
- Nội dung chi tiết bài viết Bizfly Cloud về AI sales/CRM (snippet rỗng), khó đánh giá mức độ ảnh hưởng thực tế đến hạ tầng.
- Dữ liệu Viettel IDC trong evidence bundle (Item 15) có snippet lỗi/trống, không xác minh được nội dung tin tức.
- Chưa có số liệu pricing cụ thể cho ưu đãi của FPT Cloud ngoài con số 'lên đến 20 triệu đồng' trong tiêu đề.
