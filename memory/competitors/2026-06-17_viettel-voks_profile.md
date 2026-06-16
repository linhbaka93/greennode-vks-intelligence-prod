# Competitor Profile: Viettel vOKS

## Metadata

- **Đối thủ:** Viettel Cloud (thuộc Tập đoàn Công nghiệp – Viễn thông Quân đội Viettel)
- **Dịch vụ:** Viettel Open Kubernetes Service (vOKS)
- **URL chính thức:** https://viettelcloud.vn | https://viettel-cloud.com.vn
- **Threat Level:** 🔴 CAO — Tier 1, đối thủ mạnh nhất thị trường VN
- **Profile date:** 2026-06-17
- **Last updated:** 2026-06-17
- **Confidence:** Medium (từ nguồn công khai; pricing và SLA chưa xác minh)

---

## TL;DR

Viettel vOKS là đối thủ K8s nguy hiểm nhất với GreenNode. Viettel là telco lớn nhất VN với hạ tầng quốc gia, đã trở thành CNCF Gold Member từ 01/2026 — tín hiệu đầu tư nghiêm túc vào cloud-native enterprise. GPU Cloud thực sự đã có (T4, A30, roadmap A100/H100) và kết nối được với vOKS cho AI workloads, thu hẹp gap so với GreenNode. Khách hàng chính phủ, quốc phòng, và telco là stronghold Viettel không thể cạnh tranh trực tiếp.

---

## 1. Product Profile

| Mục | Giá trị | Nguồn |
|---|---|---|
| Tên dịch vụ K8s | Viettel Open Kubernetes Service (vOKS) | viettelcloud.vn |
| CNCF membership | Gold Member từ 01/01/2026 | [cncf.io](https://www.cncf.io/announcements/2026/01/07/viettel-joins-the-cloud-native-computing-foundation-as-a-gold-member/) |
| Hạ tầng | Một trong những open-source cloud lớn nhất SEA — OpenStack + K8s production | [PR Newswire](https://www.prnewswire.com/news-releases/viettel-joins-the-cloud-native-computing-foundation-as-a-gold-member-302654447.html) |
| Đầu tư cloud | 10.000 tỷ VND mở rộng lên 17.000 rack (mục tiêu 2025-2026) | PR Newswire |
| GPU Cloud | ✅ Có — NVIDIA Tesla T4 16GB (hiện tại) + A30 24GB; roadmap A100, Quadro A6000 | [viettel-cloud.com.vn](https://viettel-cloud.com.vn/cloud-gpu-en/) |
| GPU → K8s tích hợp | Kết nối với vOKS cho containerized AI (chi tiết node pool chưa xác minh) | viettel-cloud.com.vn |
| Cloud NPU | ✅ Có — dịch vụ NPU riêng biệt | viettel-cloud.com.vn |
| SLA | [Chưa xác minh] | — |
| Pricing vOKS | [Chưa xác minh — cần access portal Viettel Cloud] | — |
| K8s versions | [Chưa xác minh] | — |

### GPU Pricing (Cloud GPU, as of 2026-06-17)

| Cấu hình | GPU | vCPU | RAM | Giá/tháng |
|---|---|---|---|---|
| A30_GPU 1 | 1× A30 24GB | 8 | 16GB | 14,600,000 VND |
| A30_GPU 2 | 1× A30 24GB | 16 | 32GB | 16,700,000 VND |
| A30_GPU 3 | 2× A30 24GB | 8 | 16GB | 31,600,000 VND |
| A30_GPU 4 | 3× A30 24GB | 64 | 16GB | 53,200,000 VND |

> Tất cả plans gồm 500GB SSD, không giới hạn data transfer, 300Mbps domestic bandwidth.

---

## 2. Điểm Mạnh (vs GreenNode)

- **Hạ tầng quy mô quốc gia:** 17.000 rack mục tiêu, phủ khắp VN, ưu tiên latency nội địa
- **CNCF Gold Member (01/2026):** Badge enterprise-readiness mạnh cho RFP / compliance checklist — mới hơn nhiều đối thủ nội địa
- **GPU Cloud thực sự có sản phẩm:** A30 + T4 với pricing công khai; roadmap A100 và Quadro A6000
- **GPU + vOKS tích hợp:** AI containerized workloads có thể chạy trên vOKS, thu hẹp competitive gap với GreenNode AI-native
- **Cloud NPU:** Dịch vụ NPU riêng — đây là capability mà GreenNode chưa có công bố tương đương
- **Khách hàng chính phủ / quốc phòng:** Lợi thế chính trị không thể sao chép
- **Brand recognition cao:** Top-of-mind tại VN về viễn thông + cloud
- **Make in Vietnam positioning:** Mạnh trong government procurement

## 3. Điểm Yếu (cơ hội cho GreenNode)

- **Pricing không minh bạch (vOKS):** Khách phải liên hệ sales — friction cao cho SME/startup
- **Developer UX chưa mạnh:** Ít Terraform provider, SDK, community ecosystem so với GreenNode
- **GPU node pool trên K8s chưa xác nhận chi tiết:** GPU pricing công khai nhưng K8s node pool integration chưa documented rõ
- **Chậm adopt cloud-native patterns mới:** CNCF Gold mới từ 01/2026 — catch-up mode về tooling
- **SME/Startup onboarding khó:** Viettel tập trung enterprise/gov, SME phải đi qua sales cycle dài

---

## 4. Threat Assessment

| Phân khúc | Mức độ đe dọa | Lý do |
|---|---|---|
| Government / Quốc phòng | 🔴 Rất cao | Viettel stronghold — GreenNode không nên compete trực tiếp |
| Enterprise VN lớn | 🔴 Cao | Brand + CNCF Gold + hạ tầng scale + GPU Cloud hiện có |
| SME / Startup | 🟡 Trung bình | Viettel kém flexible về pricing/onboarding; GreenNode có lợi thế DevEx |
| AI/ML workload | 🟡 Trung bình-Cao | ↑ Tăng so với trước — A30 GPU + vOKS integration thực sự đã có; nhưng thiếu managed AI tooling |

---

## 5. Signals cần theo dõi

- Viettel announce **GPU node pool chính thức trên vOKS** (hiện chỉ có "kết nối được")
- Viettel release **A100 / H100** Cloud GPU — nâng AI threat level lên 🔴
- Viettel leverage CNCF membership cho **compliance certification** (ISO 27017, SOC2)
- Viettel **cut public pricing** cho SME segment (hiện contact-only)
- Viettel announce **Cloud NPU tích hợp K8s** — đây sẽ là differentiator lớn

---

## Refresh Notes

- **Next refresh:** 2026-06-24
- **Trigger:** GPU node pool K8s launch, A100/H100 announcement, pricing transparency
