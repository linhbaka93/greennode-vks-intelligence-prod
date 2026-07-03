# Competitor Summary — 2026-07-03

Source: competitor-monitor run | Model: qwen/qwen3-5-27b

## Key Findings

- [RSS] [AWS Containers Blog](https://aws.amazon.com/blogs/containers/announcing-amazon-eks-rollback-for-safe-and-reliable-management-of-cluster-upgrades) 2026-07-01 — AWS ra mắt Amazon EKS Version Rollback, cho phép rollback upgrade K8s version trong vòng 7 ngày mà không cần rebuild cluster. Tác động: Nâng tiêu chuẩn 'operational safety' cho Managed K8s. Khách hàng Enterprise/Gov sẽ kỳ vọng khả năng phục hồi nhanh khi upgrade lỗi. GreenNode nên: Đánh giá lại quy trình upgrade VKS; nếu chưa có rollback tự động, cần ghi rõ SLA recovery time hoặc phát triển tính năng tương đương để giảm churn risk.
- [RSS] [Vietnam News](https://news.google.com/rss/articles/CBMiqwFBVV95cUxQYlBCY1FrdVQzbXhwNS1pcGtlS05hd1FSZGpYQnJ2bE5pMnhrUUNONWtQampHUV92WHpMd2V6UkdJX19XbFVDdndmcUZyeVIzMFIyWkxYZmhLRS1leWJZeGRLblJ0REhTandMLU42NEtQRVFHaDBtZGNVTWhfbFhhNkNOYjhQSHhsbDBzSFFQWXNtV0lSRlNPV21pUTAzMkQtM1VyNl9tZHBWM28?oc=5) 2026-07-02 — Bài báo đề cập 'AWS Local Zone in Hà Nội: unlocking AI for Vietnamese businesses'. Tác động: Nếu xác nhận, đây là mối đe dọa trực tiếp đến lợi thế 'local edge/AI' của GreenNode VKS. Hyperscaler có thể cạnh tranh về độ trễ inference AI ngay tại VN. GreenNode nên: Xác minh thông tin này với đội Sales/Partnership; chuẩn bị messaging nhấn mạnh Sovereign Cloud compliance (Luật BVDLCN 2025) mà Local Zone có thể chưa đáp ứng đầy đủ.
- [RSS] [CNCF Blog](https://www.cncf.io/blog/2026/07/01/understanding-dynamic-resource-allocation-in-kubernetes) 2026-07-01 — Dynamic Resource Allocation (DRA) đạt GA trong Kubernetes v1.35, NVIDIA chuyển driver GPU vào SIGs. Tác động: Đây là chuẩn mới cho quản lý tài nguyên GPU hiệu quả. Nếu VKS chưa hỗ trợ DRA, sẽ gặp bất lợi khi khách hàng chạy workload AI/GPU phức tạp. GreenNode nên: Kiểm tra lộ trình hỗ trợ DRA trên VKS; ưu tiên tích hợp dra-driver-nvidia-gpu nếu có kế hoạch mở rộng segment AI.
- [RSS] [Vietnam.vn](https://news.google.com/rss/articles/CBMioAFBVV95cUxPVDdCOUhVN0N1NEZsM1V3R1JXSlpQb2dEYW0zaHZjS2UxSFhpLVMzdmVJZjFNdzMxOER6U0xoLW1QRWpTemJ0TlN2aFJqVklLVFpKUHNtWk9MWHhHVE5EWWZUZUoxS25KM2s1X0pQQk56VmJlN3FmZHNpT2xISm1sbWxoQ3VlMHA4dWR1ZDlzeml4RGRNanFFYWt6N2RVUGp0?oc=5) 2026-07-02 — Viettel dẫn đầu thế giới tại Giải thưởng Công nghệ Globee Awards 2026. Tác động: Tăng uy tín thương hiệu Viettel IDC trong mắt khách hàng Gov/Enterprise. Dù không phải thông tin sản phẩm K8s cụ thể, nhưng củng cố vị thế 'national champion'. GreenNode nên: Theo dõi xem Viettel có dùng momentum này để tung promo VKS/vOKS hay không; duy trì chứng nhận Doanh nghiệp Công nghệ cao TP.HCM làm điểm khác biệt.

## Risks

- ❌ Feature Gap (Operational Safety): AWS EKS Rollback đặt ra yêu cầu mới về khả năng phục hồi sau upgrade. Nếu VKS chưa có, khách hàng kỹ thuật cao có thể so sánh bất lợi.
- ❌ Market Threat (Local Edge): Tín hiệu AWS Local Zone Hà Nội có thể xói mòn lợi thế độ trễ của GreenNode nếu họ tập trung vào AI inference local.
- ⚠️ Data Stale (Competitor Pricing): Không có dữ liệu pricing mới từ FPT/FPT/Bizfly/Viettel trong 3 ngày qua. Các số liệu cũ có thể không phản ánh chiến dịch khuyến mãi Q3.

## Gaps / Thiếu dữ liệu

- Cần cập nhật: Scrape trang web đối thủ (viettelidc.com.vn, fptcloud.com, bizflycloud.vn) thất bại trích xuất nội dung sản phẩm (chỉ thu được CSS/HTML loading). Cần kiểm tra lại crawler hoặc truy cập thủ công để lấy bảng giá/feature matrix hiện tại.
- Cần xác minh: Thông tin 'AWS Local Zone in Hà Nội' từ bài báo Vietnam News. Cần xác nhận chính thức từ AWS hoặc nguồn thứ cấp để đánh giá mức độ ảnh hưởng thực tế.
- Thiếu dữ liệu: Chưa có thông tin về CMC Cloud K8s hoặc VNPT Cloud trong window 3 ngày này.
