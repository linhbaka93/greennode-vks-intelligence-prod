# Competitor Profile: FPT Cloud FKE

## Metadata

- **Competitor:** FPT Smart Cloud (thuộc FPT Corporation)
- **Service:** FPT Kubernetes Engine (FKE) — hai mode: Managed FKE + Dedicated FKE (D-FKE)
- **URL chính thức:** https://fptcloud.com/en/product/kubernetes-engine-en/
- **Docs:** https://docs.fptcloud.com/docs/category/managed---fpt-kubernetes-engine/
- **Threat Level:** 🟡 TRUNG BÌNH-CAO — Tier 1, mạnh với Enterprise VN và SOE
- **Profile date:** 2026-06-17
- **Last updated:** 2026-06-17
- **Confidence:** Medium-Low (trang sản phẩm rất ít detail; pricing contact-only; GPU trên FKE chưa xác minh)

---

## TL;DR

FPT FKE có hai mode độc đáo: Managed (FPT quản lý toàn bộ) và Dedicated/D-FKE (khách tự quản control plane). FPT Smart Cloud đã test với H100 + H200 cho AI workloads (dùng Soperator từ Nebius) nhưng GPU trên FKE cụ thể chưa xác minh. Pricing contact-only — friction cao cho SME nhưng phù hợp enterprise deal. Tháng 6/2026, FPT release FPT Cloud Desktop 3.1 + Backup Veeam 1.5 — focus vào operational tooling cho enterprise.

---

## 1. Product Profile

| Mục | Giá trị | Nguồn |
|---|---|---|
| Tên dịch vụ K8s | FPT Kubernetes Engine (FKE) | [fptcloud.com](https://fptcloud.com/en/product/kubernetes-engine-en/) |
| Mode Managed FKE | FPT quản lý toàn bộ infrastructure; khách quản lý workload | Docs |
| Mode D-FKE (Dedicated) | Khách quản lý cả master + worker nodes; giữ tất cả advanced features | [fptcloud.com docs](https://fptcloud.com/en/documents/dedicated-fpt-kubernetes-engine-2/) |
| Regions | [Chưa xác minh rõ — HN + HCM likely, Da Nang chưa confirm] | — |
| SLA uptime | [Chưa xác minh rõ; các provider VN tier top đạt 99.99%] | — |
| K8s version support | [Chưa xác minh — không công bố trên trang chính] | — |
| Pricing | Flexible pricing — **contact FPT Cloud sales**; không public | Product page |
| GPU trên FKE | [Chưa xác minh — FPT AI Factory có H100/H200 nhưng FKE node pool chưa confirm] | GPU review 2025 |
| GPU AI Infrastructure | FPT Smart Cloud tested: H100 + H200, dùng Soperator (Nebius) | [GPU cloud review 2025](https://factory.fpt.ai) |
| Multi-cloud compatible | ✅ Compatible với AWS/Azure/GCP workloads | Product page |

---

## 2. Feature Matrix

| Feature | Status | Notes |
|---|---|---|
| Managed control plane | ✅ Có | Managed FKE mode |
| Dedicated control plane | ✅ Có | D-FKE — unique mode ít thấy ở VN |
| Autoscale (worker nodes) | ✅ Có | Auto node expansion khi load tăng |
| Load Balancer integration | ✅ Có | K8s Services LB type |
| Persistent Volume | ✅ Có | Storage integration |
| K8s version upgrade | ✅ Có | Version Upgrade feature trong D-FKE |
| GPU node pool | ⚠️ [Chưa xác minh trên FKE] | FPT AI Factory có GPU riêng |
| Container Registry | ⚠️ [Chưa xác minh integration] | — |
| Karpenter | ⚠️ [Chưa xác minh] | — |
| Multi-cluster | ⚠️ [Chưa xác minh] | — |
| MCP server | ⚠️ [Chưa tìm thấy] | — |

---

## 3. Cập nhật mới (2026)

| Ngày | Sự kiện | Ảnh hưởng đến FKE |
|---|---|---|
| 2026-06-16 | FPT Cloud Desktop 3.1 + Backup Veeam 1.5 ra mắt | Operational tooling cho Enterprise — không ảnh hưởng trực tiếp FKE nhưng hoàn thiện hệ sinh thái quản trị |
| 2025 (review) | FPT Smart Cloud tested với H100 + H200 (Soperator/Nebius) nhưng bị "serious security issues" trong GPU cloud review | Cho thấy FPT có AI infrastructure nhưng security gap cần theo dõi |

---

## 4. Điểm Mạnh (vs GreenNode)

- **D-FKE mode độc đáo:** Khách muốn kiểm soát toàn bộ cluster nhưng vẫn có managed tooling — GreenNode cần verify có offering tương đương không
- **FPT brand cho enterprise/SOE:** FPT là brand lớn nhất VN trong IT outsourcing → K8s deal thường đi kèm IT services
- **Hệ sinh thái FPT:** FPT Telecom + FPT Software + FPT Smart Cloud = full-stack offering cho enterprise
- **AI GPU infrastructure có H100/H200:** Mặc dù FKE integration chưa confirm, FPT có AI compute
- **Multi-cloud compatibility:** Giúp enterprise migrate từ AWS/Azure sang FPT dễ hơn

## 5. Điểm Yếu (cơ hội cho GreenNode)

- **Pricing hoàn toàn opaque:** Contact-only — SME không thể self-service evaluate
- **Trang sản phẩm thiếu detail:** Feature matrix không rõ, K8s versions không public — không tốt cho tech evaluation
- **Security concerns:** GPU cloud review 2025 note "serious security issues" — có thể là vấn đề với AI infrastructure cụ thể, nhưng cần theo dõi
- **GPU trên FKE chưa confirm:** FPT AI Factory ≠ FKE GPU node pool — khách hàng AI cần làm rõ
- **Ecosystem developer tools yếu:** Không có Karpenter provider, MCP server, CSI driver công khai

---

## 6. Threat Assessment

| Phân khúc | Mức độ đe dọa | Lý do |
|---|---|---|
| Government / SOE | 🔴 Cao | FPT là nhà thầu IT quốc gia, lợi thế quan hệ |
| Enterprise VN lớn | 🔴 Cao | FPT Software outsourcing → K8s upsell tự nhiên |
| SME / Startup | 🟢 Thấp | Contact-only pricing = không phù hợp self-service SME |
| AI/ML workload | 🟡 Trung bình | H100/H200 có nhưng FKE integration và security chưa rõ |

---

## 7. Signals cần theo dõi

- FPT announce **GPU node pool chính thức trên FKE** (hiện chỉ có FPT AI Factory riêng)
- FPT publish **public pricing** cho FKE (Managed và D-FKE)
- FPT release **compliance certifications** rõ ràng (ISO, SOC2, PCIDSS cho FKE)
- FPT resolve **GPU security issues** từ review 2025 và re-certify
- FPT launch **FKE feature parity với D-FKE** — thu hút enterprise muốn managed experience

---

## Refresh Notes

- **Next refresh:** 2026-06-24
- **Trigger:** GPU FKE announcement, pricing transparency, security issue resolution
