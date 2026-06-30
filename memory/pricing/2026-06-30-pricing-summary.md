# Pricing Summary — 2026-06-30

Source: competitor-monitor run | Model: qwen/qwen3-5-27b

## Key Findings

- [RSS] [AWS ML Blog](https://aws.amazon.com/blogs/machine-learning/pair-nova-2-lite-with-claude-for-cost-optimized-document-processing) 2026-06-29 — AWS công bố giải pháp xử lý tài liệu quy mô lớn kết hợp Nova 2 Lite và Claude Sonnet 4.6 trên Bedrock, tối ưu chi phí và hiệu năng. Tác động tới GreenNode: ⚠️ Feature gap về AI-native pipeline. Khách hàng Enterprise cần xử lý tài liệu tự động sẽ thấy AWS giảm OpEx đáng kể so với mô hình self-managed trên VKS nếu không có managed AI service tương đương. GreenNode nên: Đánh giá khả năng tích hợp model AI managed hoặc cung cấp template deployment tối ưu chi phí.
- [RSS] [AWS Containers Blog](https://aws.amazon.com/blogs/containers/amazon-eks-now-supports-control-plane-egress-through-your-vpc) 2026-06-22 — AWS EKS ra mắt tính năng 'customer-routed control plane egress', định tuyến traffic control plane qua VPC khách hàng thay vì internet public. Tác động tới GreenNode: ❌ Feature gap nghiêm trọng về bảo mật mạng cho phân khúc Enterprise/Gov. Khách hàng tài chính/chính phủ yêu cầu control plane traffic không ra internet sẽ ưu tiên AWS nếu GreenNode chưa có Private Link cho control plane. GreenNode nên: Rà soát kiến trúc Private Endpoint cho control plane và cập nhật battlecard về Data Residency tuyệt đối.
- [Scrape] Viettel Cloud | https://viettelcloud.vn/san-pham/kubernetes | fetched_at=2026-06-30 — Trích xuất trang sản phẩm Kubernetes của Viettel chỉ thu được cấu trúc HTML/CSS, không có bảng giá cụ thể. Tác động tới GreenNode: ⚠️ Không thể so sánh trực tiếp list price với Viettel VOKS. GreenNode nên: Yêu cầu Sales Ops thu thập quote thực tế từ đối thủ nội địa để xây dựng TCO scenario S1-S3.
- [Workspace] greennode/2026-05-20_greennode-vks_product-overview.md — Hồ sơ sản phẩm VKS cuối cùng cập nhật 2026-05-20 (quá hạn >30 ngày). Tác động tới GreenNode: ⚠️ Dữ liệu pricing có thể không phản ánh promo/discount hiện hành Q3. GreenNode nên: Kích hoạt refresh pricing sheet ngay lập tức trước khi chốt deal Enterprise.

## Recommended Actions

- Talk Track Sales: Nhấn mạnh 'Data Residency tuyệt đối tại VN' và 'Compliance Luật BVDLCN 2025' là yếu tố quyết định hơn giá cho phân khúc Gov/Finance, bù đắp feature gap về AI managed service.
- Pricing Refresh: Yêu cầu Product Team cập nhật bảng giá VKS và GPU instance mới nhất (nếu có Blackwell/NVIDIA RTX PRO) trước 2026-07-15.
- TCO Modeling: Xây dựng TCO scenario S2 (Mid Production) giả định dựa trên memory cũ nhưng flag rõ assumption, tập trung vào hidden cost (egress, support) nơi GreenNode có thể cạnh tranh.
- Competitor Intel: Giao Sales Ops thu thập quote thực tế từ Viettel IDC và FPT Cloud cho 3 cluster size tiêu chuẩn để validate pricing landscape.

## Risks

- Dữ liệu pricing đối thủ thiếu hụt hoàn toàn trong evidence bundle, không thể tính toán TCO delta chính xác.
- Hồ sơ sản phẩm GreenNode VKS (May-2026) có nguy cơ stale, không phản ánh discount/promo Q3.
- Feature gap về Control Plane Security và AI Managed Service có thể dẫn đến churn risk ở phân khúc Gov/Finance nếu không có talk track phù hợp.

## Gaps / Thiếu dữ liệu

- Cần cập nhật: greennode/2026-05-20_greennode-vks_product-overview.md — dữ liệu cũ, chưa dùng được cho pricing analysis Q3.
- Không fetch được bảng giá từ trang web đối thủ (Viettel/Bizfly/FPT) do scraper chỉ trả về CSS/HTML structure.
- Thiếu thông tin về Reserved Instance discount và GPU pricing (H100/A100) của cả GreenNode và đối thủ để tính TCO Scenario S4/S5.
