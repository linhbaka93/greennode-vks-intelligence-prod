# Competitor Profile: Viettel vOKS

## Metadata

- **Đối thủ:** Viettel Cloud (thuộc Tập đoàn Công nghiệp – Viễn thông Quân đội Viettel)
- **Dịch vụ:** Viettel Open Kubernetes Service (vOKS)
- **URL chính thức:** https://viettelcloud.vn
- **Threat Level:** 🔴 CAO — Tier 1, đối thủ mạnh nhất thị trường VN
- **Profile date:** 2026-05-20
- **Last updated:** 2026-05-20
- **Confidence:** Medium (từ nguồn công khai; pricing và SLA chưa xác minh)

---

## TL;DR

Viettel vOKS là đối thủ K8s nguy hiểm nhất với GreenNode. Viettel là telco lớn nhất VN với hạ tầng quốc gia, vừa gia nhập CNCF Gold Member (01/2026) — tín hiệu cho thấy họ đang đầu tư nghiêm túc vào cloud-native enterprise. Khách hàng chính phủ, quốc phòng, và telco là stronghold của Viettel; GreenNode khó cạnh tranh trực tiếp ở phân khúc này.

---

## 1. Product Profile

| Mục | Giá trị | Nguồn |
|---|---|---|
| Tên dịch vụ K8s | Viettel Open Kubernetes Service (vOKS) | [viettelcloud.vn](https://solutions.viettel.vn) |
| Mô tả | PaaS — môi trường ảo hóa hoàn chỉnh để phát triển, test, và deploy microservices trên K8s | [Scribd doc](https://www.scribd.com/document/696897693) |
| CNCF membership | Gold Member từ 01/2026 | [cncf.io](https://www.cncf.io/announcements/2026/01/07/viettel-joins-the-cloud-native-computing-foundation-as-a-gold-member/) |
| Hạ tầng | Một trong những open source cloud lớn nhất SEA — OpenStack + K8s production | [PR Newswire](https://www.prnewswire.com/news-releases/viettel-joins-the-cloud-native-computing-foundation-as-a-gold-member-302654447.html) |
| Đầu tư cloud | 10.000 tỷ VND mở rộng lên 17.000 rack (2025) | [PR Newswire](https://www.prnewswire.com/news-releases/viettel-make-in-vietnam-cloud-computing-to-gain-market-share-at-home-301649657.html) |
| SLA | [Chưa xác minh] | — |
| Pricing | [Chưa xác minh — cần access portal Viettel Cloud] | — |
| K8s versions | [Chưa xác minh] | — |

---

## 2. Điểm Mạnh (vs GreenNode)

- **Hạ tầng quy mô quốc gia:** 17.000 rack mục tiêu, phủ khắp VN, ưu tiên latency nội địa
- **Khách hàng chính phủ / quốc phòng:** Viettel có lợi thế chính trị không thể sao chép
- **CNCF Gold Member:** Tín hiệu enterprise-readiness mạnh, dùng được trong RFP / compliance checklist
- **Brand recognition cao:** Viettel là top-of-mind tại VN về viễn thông + cloud
- **Make in Vietnam positioning:** Mạnh trong government procurement — ưu tiên theo chính sách

## 3. Điểm Yếu (cơ hội cho GreenNode)

- **AI/GPU capability không rõ:** Docs không đề cập GPU node pool hay AI-native tooling
- **Pricing không minh bạch công khai:** Khách phải liên hệ sales — friction cao cho SME/startup
- **Developer UX chưa mạnh:** Ít Terraform provider, SDK, community ecosystem so với GreenNode
- **Chậm adopt cloud-native patterns mới:** CNCF Gold mới từ 01/2026 — catch-up mode

---

## 4. Threat Assessment

| Phân khúc | Mức độ đe dọa | Lý do |
|---|---|---|
| Government / Quốc phòng | 🔴 Rất cao | Viettel stronghold — GreenNode không nên compete trực tiếp |
| Enterprise VN lớn | 🔴 Cao | Brand + CNCF badge + hạ tầng scale |
| SME / Startup | 🟡 Trung bình | Viettel kém flexible hơn GreenNode về pricing/onboarding |
| AI/ML workload | 🟢 Thấp | GPU capability chưa rõ; GreenNode có thể lead |

---

## 5. Signals cần theo dõi

- Viettel announce GPU node pool hoặc AI infrastructure offering
- Viettel leverage CNCF membership cho compliance certification (ISO, SOC2)
- Viettel cut pricing public cho SME
- Partnership với hyperscaler (AWS/GCP via CNCF ecosystem)

---

## Refresh Notes

- **Next refresh:** 2026-06-20
- **Trigger:** Feature launch, pricing change, government contract announcement
