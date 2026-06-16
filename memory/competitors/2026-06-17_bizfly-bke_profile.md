# Competitor Profile: Bizfly Cloud BKE

## Metadata

- **Competitor:** Bizfly Cloud (thuộc VCCorp — Công ty Cổ phần VCCorp)
- **Service:** Bizfly Cloud Kubernetes Engine (BKE)
- **URL:** https://bizflycloud.vn/en/kubernetes-engine
- **Threat Level:** 🟡 TRUNG BÌNH-CAO — Tier 1, đối thủ mạnh nhất phân khúc SME
- **Profile date:** 2026-06-17
- **Last updated:** 2026-06-17
- **Confidence:** Medium (pricing page accessible; GPU node pool confirmed; SLA và K8s versions chưa public)

---

## TL;DR

Bizfly BKE đã xác nhận có GPU node pool cho K8s (ML, graphics, video workloads), đây là update quan trọng so với trước. ISO 27001/27017/PCI DSS 4.0 Level 1 certified. Karpenter provider và MCP server (10 services) đều active trên GitHub — Bizfly đang build developer tooling nghiêm túc. Pricing tier Standard-0 free + Standard-1 ở 1.26M VND/cluster/month là competitive mạnh với SME VN.

---

## 1. Core Product Profile

| Item | Value | Source |
|---|---|---|
| Tên dịch vụ K8s | Bizfly Cloud Kubernetes Engine (BKE) | [bizflycloud.vn](https://bizflycloud.vn/en/kubernetes-engine) |
| URL pricing | https://bizflycloud.vn/en/kubernetes-engine/bang-gia | — |
| Ngày ra mắt (GA) | Trước 2021 | About page |
| Regions | Hà Nội + Hồ Chí Minh City | Product page |
| ISO 27001:2013 | ✅ Certified | Product page |
| ISO 27017:2015 | ✅ Certified | Product page |
| PCI DSS 4.0 Level 1 | ✅ Certified | Product page |
| GPU node pool | ✅ Có — GPU K8s node pool available for ML, graphics, video | [bizflycloud.vn](https://bizflycloud.vn/en/kubernetes-engine) |
| Karpenter provider | ✅ Active — [karpenter-provider-bizflycloud](https://github.com/bizflycloud/karpenter-provider-bizflycloud) trên GitHub | GitHub |
| MCP server | ✅ Có — 10 services: Server, Volume, LB, Kubernetes, Database, DNS, CDN, KMS, Container Registry, AutoScaling, Alert | [GitHub](https://github.com/bizflycloud) / MCP Market |
| K8s version upgrade | Auto hoặc manual upgrade (chi tiết versions chưa public) | Product page |
| SLA uptime | [Chưa xác minh — "24/7 system continuity" claim chung chung] | — |
| Multi-zone cluster | ✅ Có — flexible node pool configuration | Product page |

---

## 2. Pricing (as of 2026-06-17)

| Tier | Phí cluster/tháng | Ghi chú |
|---|---|---|
| Standard-0 | **Miễn phí** | Free cluster management |
| Standard-1 | **1,260,000 VND/cluster/month** | Enhanced cluster management |

> Resources tính riêng theo Bizfly Cloud Server + Volume + Load Balancer rates.
> Không có GPU pricing riêng cho K8s node pool — GPU Cloud Server pricing apply.

---

## 3. Feature Matrix

| Dimension | Status | Notes |
|---|---|---|
| GPU node pool | ✅ Có | ML, graphics, video workloads confirmed |
| Karpenter autoscaler | ✅ Có | Open-source provider trên GitHub, active |
| MCP server | ✅ Có | 10 services, listed on MCP Market |
| HPA / VPA | ✅ Có (K8s standard) | — |
| Multi-zone cluster | ✅ Có | HN + HCM node pools |
| Cloud Controller Manager | ✅ Có | [GitHub](https://github.com/bizflycloud/bizfly-cloud-controller-manager) |
| CSI Driver | ✅ Có | [bizflycloud/csi-bizflycloud](https://github.com/bizflycloud/csi-bizflycloud) |
| Container Registry integration | ✅ Có | Bizfly Container Registry |
| API access restriction by IP | ✅ Có | Cluster security feature |
| Multi-cluster management | ⚠️ [Chưa xác minh] | — |
| Spot node | ⚠️ [Chưa xác minh] | — |
| KEDA | ⚠️ [Chưa xác minh] | — |

---

## 4. Điểm Mạnh (vs GreenNode)

- **GPU node pool đã có:** K8s GPU workloads confirmed — gap với GreenNode tùy thuộc GPU models và pricing
- **Free cluster tier:** Standard-0 free là differentiator mạnh cho startup/POC stage
- **PCI DSS 4.0 Level 1:** GreenNode cần verify có certification tương đương không — đây là must-have cho fintech
- **Karpenter provider open-source:** Hệ sinh thái tốt hơn, enterprise adoption dễ hơn
- **MCP server 10 services:** Developer tooling AI-native, phù hợp trend MCP adoption 2026
- **ISO 27001/27017:** Compliance baseline tốt

## 5. Điểm Yếu (cơ hội cho GreenNode)

- **Pricing chỉ public cluster fee:** GPU node pool pricing không rõ — khách phải estimate từ Cloud Server rates
- **K8s version support không transparent:** Versions không công bố — potential lock-in risk cho enterprise
- **SLA không rõ:** "24/7 continuity" không phải SLA số — GreenNode có thể win nếu có SLA 99.9%+ rõ ràng
- **VCCorp context:** SME media company background — enterprise cloud credibility thấp hơn Viettel/FPT
- **Make in Vietnam:** Không tìm thấy certification trên trang web hiện tại (trước đó có mention 153 tiêu chí)

---

## 6. Threat Assessment

| Phân khúc | Mức độ đe dọa | Lý do |
|---|---|---|
| SME / Startup VN | 🔴 Cao | Free tier + 1.26M/cluster affordable + local ecosystem |
| Fintech / E-commerce | 🔴 Cao | PCI DSS 4.0 Level 1 là điểm mạnh quyết định |
| Enterprise VN | 🟡 Trung bình | ISO certs có nhưng brand credibility thấp hơn Viettel/FPT |
| AI/ML workload | 🟡 Trung bình | GPU node pool có nhưng GPU models chưa rõ vs GreenNode |

---

## 7. Signals cần theo dõi

- Bizfly công bố **GPU node pool pricing và models** cụ thể trên K8s
- Bizfly đạt **Make in Vietnam certification** (có thể đã có nhưng link hiện tại không thấy)
- Karpenter provider **upgrade lên latest Karpenter version** — adoption indicator
- MCP server Bizfly được **featured trên Claude/cursor MCP marketplaces**
- Bizfly announce **SLA số cụ thể** (99.9% hay 99.99%)

---

## Refresh Notes

- **Next refresh:** 2026-06-24
- **Trigger:** GPU node pool pricing announcement, Make in Vietnam cert update, K8s version list
