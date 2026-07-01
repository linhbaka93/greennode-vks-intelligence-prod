# Competitor Summary — 2026-07-01

Source: monthly-brief run | Model: qwen/qwen3-5-27b

## Key Findings

- [RSS] AWS Containers Blog | https://aws.amazon.com/blogs/containers/amazon-eks-now-supports-control-plane-egress-through-your-vpc | published_at=2026-06-22 — [RSS] [AWS Containers Blog](https://aws.amazon.com/blogs/containers/amazon-eks-now-supports-control-plane-egress-through-your-vpc) 2026-06-22 — AWS EKS ra mắt tính năng 'customer-routed control plane egress', cho phép định tuyến toàn bộ traffic control plane (admission webhooks, OIDC lookups) qua VPC của khách hàng thay vì internet public.

**Tác động tới GreenNode:** ❌ Feature gap nghiêm trọng về bảo mật và kiến trúc mạng cho phân khúc Enterprise/Gov. Khách hàng tài chính/chính phủ yêu cầu control plane traffic không ra internet sẽ ưu tiên AWS nếu GreenNode chưa có giải pháp tương đương (Private Link cho control plane).

**GreenNode nên:** Rà soát khả năng triển khai Private Endpoint cho Control Plane VKS; nếu chưa có, cần đưa vào roadmap ưu tiên cao để đáp ứng RFP Q3/Q4.
- [RSS] Vietnam.vn | https://news.google.com/rss/articles/CBMijwFBVV95cUxQUF9HNTZhVFREd0p4TWY5S0JEOEZTc09kTkQxVzg0MlRrZWQwWWRySF9vRmsyS3RfQmJsYnY2azRMazNsME9MSVo5eTR4SUxHUzc2dUNCUTdvYXBiOS11T0IyemU3eDBhWFV1aGNWaW9YZWJMQVRKbTJySVFpaW9YQjVQSmpMbFFrUmF2VU5Fdw?oc=5 | published_at=2026-06-27 — [RSS] [Vietnam.vn](https://news.google.com/rss/articles/CBMijwFBVV95cUxQUF9HNTZhVFREd0p4TWY5S0JEOEZTc09kTkQxVzg0MlRrZWQwWWRySF9vRmsyS3RfQmJsYnY2azRMazNsME9MSVo5eTR4SUxHUzc2dUNCUTdvYXBiOS11T0IyemU3eDBhWFV1aGNWaW9YZWJMQVRKbTJySVFpaW9YQjVQSmpMbFFrUmF2VU5Fdw?oc=5) 2026-06-27 — Hà Nội và CMC hợp tác phát triển chính phủ số và thành phố AI.

**Tác động tới GreenNode:** ⚠️ Churn risk trong segment Gov. CMC đang củng cố vị thế 'đối tác chiến lược' với địa phương lớn, cạnh tranh trực tiếp với lợi thế data residency của GreenNode.

**GreenNode nên:** Tăng cường PR về chứng nhận Doanh nghiệp Công nghệ đã đạt được tại TP.HCM để cân bằng tín hiệu thị trường; rà soát pipeline deal với các sở ban ngành khác ngoài HCM.
- [RSS] AWS ML Blog | https://aws.amazon.com/blogs/machine-learning/introducing-claude-sonnet-5-on-aws-anthropics-most-capable-sonnet-model | published_at=2026-06-30 — [RSS] [AWS ML Blog](https://aws.amazon.com/blogs/machine-learning/introducing-claude-sonnet-5-on-aws-anthropics-most-capable-sonnet-model) 2026-06-30 — AWS công bố Claude Sonnet 5 trên Amazon Bedrock, mô hình Sonnet tiên tiến nhất của Anthropic.

**Tác động tới GreenNode:** ⚠️ Feature gap về AI-native pipeline. Khách hàng Enterprise cần giải pháp xử lý tài liệu tự động (OCR + LLM) sẽ thấy AWS cung cấp mô hình mới nhất ngay lập tức. GreenNode AgentBase cần chứng minh khả năng chạy các mô hình open-source tương đương hoặc tích hợp API an toàn.

**GreenNode nên:** Cập nhật benchmark hiệu năng/cost của AgentBase khi chạy các mô hình tương đương (Llama 3.1/3.2) so với Bedrock để làm tư liệu bán hàng cho khách hàng quan tâm Sovereign AI.
- [RSS] AWS News Blog | https://aws.amazon.com/blogs/aws/announcing-amazon-ec2-g7-instances-accelerated-by-nvidia-rtx-pro-4500-blackwell-server-edition-gpus | published_at=2026-06-18 — [RSS] [AWS News Blog](https://aws.amazon.com/blogs/aws/announcing-amazon-ec2-g7-instances-accelerated-by-nvidia-rtx-pro-4500-blackwell-server-edition-gpus) 2026-06-18 — AWS công bố GA EC2 G7 instances với GPU NVIDIA RTX PRO 4500 Blackwell Server Edition.

**Tác động tới GreenNode:** ❌ Feature gap về phần cứng GPU thế hệ mới. AWS cung cấp lợi thế hiệu năng ngay lập tức cho LLM inference nặng. GreenNode đang thua nếu khách hàng cần performance tối đa cho training/inference mà không có ràng buộc data residency VN.

**GreenNode nên:** Theo dõi nguồn cung GPU Blackwell tại VN; nếu có thể, thông báo kế hoạch nâng cấp node pool GPU trong digest tháng tới để giữ chân khách hàng AI.
- [Blog] Bizfly Cloud | https://bizflycloud.vn/tin-tuc/kubernetes-136-haru-giai-thich-chi-tiet-20260629145644358.htm | published_at=2026-06-29 — [Blog] [Bizfly Cloud](https://bizflycloud.vn/tin-tuc/kubernetes-136-haru-giai-thich-chi-tiet-20260629145644358.htm) 2026-06-29 — Bizfly Cloud đăng bài chi tiết về Kubernetes 1.36 (Haru).

**Tác động tới GreenNode:** ⚠️ Brand visibility. Đối thủ nội địa đang chủ động giáo dục thị trường về phiên bản K8s mới nhất. Nếu GreenNode chậm cập nhật version support, sẽ bị coi là lỗi thời.

**GreenNode nên:** Đảm bảo VKS hỗ trợ K8s 1.36 trong vòng 30 ngày sau GA upstream; xuất tin tức ngắn gọn về việc này trên blog để khẳng định tốc độ cập nhật.

## Risks

- ❌ **Kiến trúc Mạng (Network Architecture):** AWS EKS đã có tính năng định tuyến control plane qua VPC riêng. GreenNode VKS hiện tại chưa có evidence xác nhận tính năng tương tự (Private Link for Control Plane). Đây là rào cản lớn cho khách hàng Finance/Gov yêu cầu security cao.
- ❌ **Phần cứng GPU:** AWS đã GA instance G7 với GPU Blackwell. GreenNode cần xác minh xem có kế hoạch nhập/hỗ trợ card này hay không để tránh mất khách hàng workload AI nặng.
- ⚠️ **Thị phần Chính phủ:** CMC vừa ký hợp tác chiến lược với Hà Nội. GreenNode cần tăng tốc các deal tại các tỉnh/thành khác để bù đắp.

## Gaps / Thiếu dữ liệu

- Cần cập nhật: `competitors/2026-06-30-competitor-summary.md` — Dữ liệu cũ, chưa dùng được cho phân tích sâu pricing.
- Không có dữ liệu pricing cụ thể cho FPT Cloud/FKE và Viettel vOKS trong tuần này (chỉ có blog content). Cần `pricing_agent` fetch bảng giá mới nhất.
- Chưa xác minh được nội dung chi tiết bài đăng Facebook của GreenNode do crawler bị chặn/login wall (nếu có). Chỉ dựa vào RSS blog.
