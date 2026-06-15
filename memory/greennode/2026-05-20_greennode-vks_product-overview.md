# GreenNode VKS — Tổng Quan Sản Phẩm

## Metadata

- **Sản phẩm:** GreenNode VKS (GreenNode Kubernetes Service)
- **Công ty:** GreenNode — thuộc VNG Corporation
- **URL:** https://vngcloud.vn/product/vks | https://docs.vngcloud.vn/vng-cloud-document/vks
- **Lưu ý:** GreenNode và VNG Cloud là cùng một công ty. Luôn dùng tên "GreenNode" trong mọi tài liệu.
- **Profile date:** 2026-05-20
- **Last updated:** 2026-05-20

---

## TL;DR

GreenNode VKS là managed Kubernetes service của GreenNode (thuộc VNG Corporation), mạnh về kỹ thuật và compliance. Có 3 region tại VN (HCM, HAN, BKK Thailand), 3 CNI options bao gồm Cilium VPC Native, Fleet management cho multi-cluster. Differentiator nổi bật: hỗ trợ Private Cluster với IP Whitelist, Terraform-first deployment, Container-Optimized OS, data residency VN (Luật BVDLCN 2025 + Nghị định 356/2025).

---

## 1. Core Product Profile

| Item | Value | Source |
|---|---|---|
| Tên dịch vụ K8s | VNGCloud Kubernetes Service (VKS) | [vngcloud.vn](https://vngcloud.vn/product/vks) |
| URL chính thức | https://vngcloud.vn/product/vks | — |
| Ngày ra mắt (GA) | [Chưa xác minh — cần search press release] | — |
| Kubernetes version support | v1.28, v1.29, v1.30 (1.28 deprecated 2025-11-24) | [Release notes](https://docs.vngcloud.vn/vng-cloud-document/vks/thong-bao-va-cap-nhat/release-notes) |
| Regions available | HCM03 (HCM), HAN (Hà Nội), BKK (Bangkok) | Release notes — verify region availability |
| SLA uptime commitment | [Chưa xác minh — không nêu rõ trên docs công khai] | — |
| Control plane | Fully Managed | [docs](https://docs.vngcloud.vn/vng-cloud-document/vks/vks-la-gi) |
| Pricing model | Pay-per-resource (cluster management + Cloud Server + Volume + LB) | [Charging Fee](https://docs.vngcloud.vn/vng-cloud-document/vks/cach-tinh-gia) |

---

## 2. Feature Matrix

| Dimension | Status | Notes |
|---|---|---|
| Multi-cluster management | ✅ Có | Fleet management — GLB cho North-South, MCS cho East-West (Cilium VPC Native) |
| GPU node pool | ⚠️ [Chưa xác minh] | Docs không nêu rõ GPU support — cần check vServer GPU integration |
| Spot node | ⚠️ [Chưa xác minh] | — |
| Auto node provisioning (Karpenter-like) | ❓ Unknown | Cần verify |
| HPA / VPA | ✅ Có | Standard K8s capability |
| Cluster Autoscaler | ✅ Có | `auto_scale_config` trong Terraform với min_size/max_size |
| KEDA | ⚠️ [Chưa xác minh] | — |
| CNI options | ✅ Có 3 options | Calico, Cilium Overlay, Cilium VPC Native Routing |
| VPC native | ✅ Có | Cilium VPC Native Routing |
| Network policy | ✅ Có | Standard với Calico/Cilium |
| CSI driver options | ✅ Có | Block Store CSI plugin enabled by default |
| RBAC | ✅ Có | Standard K8s + IAM integration (VKSFullAccess policy) |
| Pod Security | ✅ Có | Standard K8s |
| Secrets management | ⚠️ Partial | Có KMS service riêng (Key Management System) |
| Observability tích hợp | ✅ Có | Monitoring section trong docs |
| GPU operator pre-installed | ❓ Unknown | — |
| MIG / fractional GPU | ❓ Unknown | — |
| ArgoCD / Flux | ❌ [Không thấy doc] | Phải tự install |
| Multi-cloud / hybrid | ✅ Có | "Built on open-source K8s, can manage workloads from multiple cloud providers or on-premises" |
| ISO 27001 | ⚠️ [Chưa xác minh — cần check certification page] | — |
| SOC2 | ⚠️ [Chưa xác minh] | — |
| PCI-DSS | ⚠️ [Chưa xác minh] | — |
| Nghị định 13 compliance | ✅ Có (suy luận từ vị trí VN entity) | — |
| Support 24/7 | ⚠️ [Chưa xác minh] | — |
| Tiếng Việt support | ✅ Có | Docs có tiếng Việt; VN entity |
| Private Cluster | ✅ Có | Hỗ trợ trong HAN region — Private Node Groups với Private IPs only |
| IP Whitelist | ✅ Có | Feature riêng cho access control |
| Terraform support | ✅ Có | Provider `vngcloud/vngcloud` v1.2.2 |
| Container-Optimized OS | ✅ Có (cho v1.29.1, v1.30.5 ở HCM, BKK) | — |

---

## 3. Pricing Summary

> ⚠️ **Chi tiết pricing cần được collect riêng:** Xem `/memory/pricing/2026-05-20_vng-vks_pricing.md` (TBD — cần access vCalculator hoặc Sales quote).

**Highlights từ public docs:**
- **Pricing model:** Cluster management fee + resource-based (Cloud Server, Volume, Load Balancer tính riêng theo policy của từng service)
- **Control plane:** [Chưa xác minh có phí riêng hay miễn phí]
- **Pricing đã VAT:** vCalculator estimates đã bao gồm VAT
- **Free tier:** [Chưa xác minh]
- **Auto-renew:** Mặc định bật cho tất cả resources

---

## 4. Positioning & GTM

### Target segment
- **Suy luận từ docs:** Mid-market đến enterprise (focus vào VPC, IAM, Fleet management — features thường cho enterprise)
- Hỗ trợ migration từ EKS/GKE/on-prem (có docs Velero playbook) → target khách hàng đang chạy hyperscaler

### Key messaging
- "Managed K8s based on open-source — focus on application, not management"
- "Multi-AZ deployment cho high availability"
- "Seamless upgrade between K8s versions"

### Differentiator họ claim
- 3 CNI options (flexibility)
- Fleet management (multi-cluster, đa region/zone)
- Native integration với vLB (NLB + ALB)
- Private Cluster với IP Whitelist
- Terraform-first

### Sales channel
- **Suy luận:** Direct + Partner Portal (docs có "Partner Portal user guide" section)

### Geographic strategy
- VN-first (HCM + HAN), expand sang SEA (BKK Thailand)
- Cạnh tranh trực tiếp với GreenNode tại thị trường VN

---

## 5. GTM Signals

| Signal | Observation | Implication |
|---|---|---|
| BKK region | Đã có Bangkok zone | Đang expand SEA — cạnh tranh với regional players |
| Fleet management feature mới | Multi-cluster, multi-region với GLB + MCS | Targeting enterprise multi-deployment |
| Container-Optimized OS launch | Roll out theo region (HCM → BKK) | Đang invest vào performance tuning |
| Velero migration playbook | Docs cho migrate từ EKS, GKE | Aggressive về switching deal từ hyperscaler |
| Terraform provider chính thức | v1.2.2 (Jan 2026) | Developer-friendly, IaC-first |
| MCP server cho cloud management | [Cần verify — Bizfly có cái này] | — |

---

## 6. Customer Evidence

- **Case studies công khai:** [Chưa search — cần check trang vngcloud.vn/case-studies]
- **Logo customer:** [Chưa search]
- **G2 / Capterra rating:** [Chưa có data]
- **Common praise:** [Chưa có data]
- **Common complaint:** [Chưa có data]

> **Action:** Solution Architect / Marketing tìm case study công khai để fill section này.

---

## 7. SWOT (Góc Nhìn GreenNode)

### Strengths của VNG VKS (so với GreenNode)
- **Scale infrastructure VN lớn:** 2 region VN + 1 SEA region (BKK)
- **CNI flexibility:** 3 lựa chọn (Calico, Cilium Overlay, Cilium VPC Native)
- **Fleet management:** Multi-cluster federation — feature enterprise
- **Native vLB integration:** Tích hợp sâu với load balancer ecosystem
- **Terraform mature:** Provider chính thức v1.2.2
- **Velero migration playbook:** Aggressive về switching deal

### Weaknesses của VNG VKS (so với GreenNode — cần verify)
- **GPU / AI capability không rõ:** Docs không nêu GPU node pool prominent
- **SLA uptime không công bố công khai:** Khác với hyperscaler (99.95%)
- **Compliance certification chưa thấy rõ:** ISO 27001, SOC2 — không xuất hiện trong docs search
- **AI/ML tooling integration thiếu (KServe, KubeFlow, vLLM):** Chưa thấy doc đề cập

### Opportunities GreenNode có thể khai thác
- **AI / GPU positioning:** Nếu GreenNode có GPU H100 onshore VN với MIG/fractional, đây là lợi thế lớn
- **SLA commitment công khai:** Publish SLA % rõ ràng → đáp ứng enterprise expectation
- **Compliance certification rõ ràng:** ISO 27001, SOC2, Nghị định 13 với evidence
- **AI-native templating (vLLM, KServe ready):** Pre-installed cho AI startup
- **VAT pricing transparency:** Pricing VND đã VAT, không cần FX risk

### Threats từ VNG VKS
- **Brand recognition cao:** VNG là tên tuổi lớn tại VN (game, fintech)
- **VCCorp ecosystem cross-sell:** Nếu khách dùng dịch vụ VCCorp khác, dễ adopt VKS
- **Aggressive về migration deal:** Velero playbook → cạnh tranh trực tiếp migration từ EKS/GKE
- **Terraform-first developer love:** Dev nhanh chóng prefer cloud có Terraform mature
- **Fleet management chiếm pole position multi-cluster:** Nếu GreenNode chưa có, lose deals multi-region

---

## 8. Strategic Implications

| Finding | Impact | Cần action? | Bộ phận |
|---|---|---|---|
| VNG có Fleet multi-cluster mà GreenNode chưa rõ trạng thái | High | Có — assess capability gap | Product |
| Compliance certifications của VNG không rõ → GreenNode có thể leverage | Medium | Có — publish cert của GreenNode rõ | Marketing |
| VKS thiếu AI/GPU positioning → cơ hội cho GreenNode | High | Có — push AI positioning aggressive | Product Marketing |
| Brand "GreenNode" appear trong docs VNG → cần clarify | High | Có — escalate Product/Legal | Legal/Product |
| VNG có Terraform mature → GreenNode cần parity | Medium | Có — check Terraform provider của GreenNode | Engineering |

---

## 9. Recommendations

**P0 (must do):**
- Clarify mention "GreenNode" trong docs VNG VKS — escalate Legal/Product team
- Verify GreenNode SLA và compliance certification và publish công khai
- Push AI/GPU differentiator nếu GreenNode có lợi thế (H100, MIG, etc.)

**P1 (should do):**
- Assess feature gap: Fleet management multi-cluster, 3 CNI options, Container-Optimized OS
- Develop migration playbook (đáp ứng Velero playbook của VNG)
- Verify Terraform provider của GreenNode có mature không

**P2 (nice to do):**
- Search case study công khai của VNG VKS để hiểu customer segment thật
- Track Bangkok region expansion → assess SEA strategy

---

## 10. Sources

| Nguồn | URL | Ngày truy cập | Confidence |
|---|---|---|---|
| VKS product page | https://vngcloud.vn/product/vks | 2026-05-20 | High |
| VKS docs overview | https://docs.vngcloud.vn/vng-cloud-document/vks/vks-la-gi | 2026-05-20 | High |
| Charging Fee | https://docs.vngcloud.vn/vng-cloud-document/vks/cach-tinh-gia | 2026-05-20 | Medium |
| Release notes | https://docs.vngcloud.vn/vng-cloud-document/vks/thong-bao-va-cap-nhat/release-notes | 2026-05-20 | High |
| Version schedule | https://docs.vngcloud.vn/vng-cloud-document/vks/thong-bao-va-cap-nhat/vks-release-schedule | 2026-05-20 | High |
| Terraform docs | https://docs.vngcloud.vn/vng-cloud-document/vks/su-dung-vks-voi-terraform | 2026-05-20 | High |
| VKS Networking (DeepWiki) | https://deepwiki.com/vngcloud/docs/3.2-vks-networking | 2026-05-20 | Medium |
| Migration docs | https://docs.vngcloud.vn/vng-cloud-document/vks/migration/migrate-cluster-from-other-to-vks | 2026-05-20 | High |

---

## Refresh Notes

**Next refresh due:** 2026-06-20 (Tier 1 = hàng tháng)

**Refresh triggers (ngoài lịch):**
- Pricing thay đổi > 10%
- Ra mắt feature lớn (GPU node pool, Karpenter, AI tooling)
- M&A / funding lớn của VCCorp/VNG
- Customer reference công khai

**Open questions cần investigation:**
1. Mention "GreenNode" trong VKS docs — clarify nature (rebrand? partnership? typo?)
2. GPU node pool có support trên VKS không? Pricing như thế nào?
3. SLA uptime % cụ thể (99.9? 99.95?)
4. Compliance certifications cụ thể (ISO 27001, SOC2, PCI-DSS)
5. Pricing chi tiết per instance type — cần access vCalculator
6. Free tier / startup program (nếu có)

---

*Template based on `/skills/competitor-analysis.md` v1.0.0*
*Initial research từ public web sources only. Confidence: Medium. Cần Solution Architect review.*
