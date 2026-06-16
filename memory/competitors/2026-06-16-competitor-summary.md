# Competitor Summary — 2026-06-16

Source: weekly-digest run | Model: google/gemma-4-31b-it

## Key Findings

- [RSS] [AWS Blog](https://aws.amazon.com/blogs/machine-learning/introducing-container-caching-in-amazon-sagemaker-ai-for-faster-model-scaling) 2026-06-16 — AWS ra mắt container image caching cho SageMaker AI, giúp tăng tốc độ scale-out cho các mô hình GenAI lên đến 2 lần. — Tạo áp lực về hiệu năng triển khai AI model. GreenNode VKS cần xem xét tối ưu hóa image pulling/caching cho GPU node để không bị hổng gap về 'time-to-scale' khi khách hàng triển khai LLM lớn.
- [RSS] [Vietnam.vn](https://news.google.com/rss/articles/CBMi-wFBVV95cUxPVWFxTVlicE9mLWdqTWhGWGZCdy1jUGJ1eWRpZVc0NXhXQmtDV3J5aVFQaDlKLWFqa1JDM05QNGZlMFhremp0ZV9PcmdpNzg1RUw3Um9XblBLb1NDa2tEZVRkbEN2S1FwZW54YXNxWFo3NERqRUVLQ2R4V1ZQSmhnWHgzOTFLZGlSVVQzVWJsU0F1NTZKVTlaRGF4ZlR2Ynp4TDYxVmdFclVsWFhpTTFLRWpLODJZYTFTN3liU0VuLWxXcWY3Q2k1V0c5NjM1ek13Wl9XT1RaLXpkNG1vUWluUVNQdDdQZUFCUThKeE56VlhsZmFRdWpiZU1ubw?oc=5) 2026-06-11 — Viettel ra mắt Vietnam AI Open Hackathon 2026 phối hợp với NVIDIA nhằm mở rộng tiếp cận hạ tầng 'AI Supercomputing'. — Viettel đang tận dụng quan hệ chiến lược với NVIDIA để thu hút cộng đồng dev và doanh nghiệp AI. GreenNode cần đẩy mạnh các chương trình cộng đồng hoặc ưu đãi GPU để giữ chân tệp khách hàng startup AI.
- [RSS] [Vietnam.vn](https://news.google.com/rss/articles/CBMipAFBVV95cUxPQi0zZkRtNTlkR3JIbU45XzM1aElKTHljQWEzRVM4RnhXZ0s5OWZVV0Y0eGg5NUV4TWxPS00xRzhDNDlQRjhMOGVqVWFXcmswQ3JSUDV4aTFXeG0tclNVSE9ubnBpYl9YSTY4RGR4bENYZFJ2QW13dG1IRnluWGV0U051b3J2VFJjUzJIYjdtY2dRM25jbEZmNU52NzBMQWxiNG1Qbg?oc=5) 2026-06-12 — GreenNode được TP.HCM cấp Chứng nhận Doanh nghiệp Công nghệ cao đầu tiên cho nhà cung cấp hạ tầng AI. — Củng cố vị thế pháp lý tuyệt đối trong phân khúc Sovereign AI Cloud tại VN, đặc biệt khi đối chiếu với Luật BVDLCN 2025. Đây là điểm bán hàng chủ chốt (USP) khi đấu thầu dự án Gov/Enterprise.
- [RSS] [AWS Containers Blog](https://aws.amazon.com/blogs/containers/better-together-amazon-eks-auto-mode-and-istio-ambient-mesh) 2026-06-09 — AWS kết hợp EKS Auto Mode với Istio Ambient Mesh để tự động hóa quản lý hạ tầng và bảo mật mTLS. — Xu hướng giảm tải vận hành (operational overhead) cho K8s. GreenNode VKS nên đánh giá khả năng tích hợp Ambient Mesh để giảm chi phí tài nguyên cho sidecar, tăng tính cạnh tranh về TCO.

## Risks

- Tác động tới GreenNode: Khách hàng AI scale nhanh có thể rời bỏ VKS nếu thời gian khởi tạo node GPU quá chậm.
- Tác động tới GreenNode: Nguy cơ mất tệp khách hàng tiềm năng là các AI Startup ngay từ giai đoạn build.

## Gaps / Thiếu dữ liệu

- Cần cập nhật: competitors/2026-05-20_viettel-voks_profile.md — dữ liệu cũ, không dùng được.
- Cần cập nhật: competitors/2026-05-20_fpt-cloud-fke_profile.md — dữ liệu cũ, không dùng được.
- Cần cập nhật: competitors/2026-05-20_bizfly-bke_profile.md — dữ liệu cũ, không dùng được.
- Thiếu dữ liệu pricing mới nhất của Viettel vOKS và FPT FKE để so sánh head-to-head.
