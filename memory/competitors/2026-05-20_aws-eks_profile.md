# Competitor Profile: AWS EKS

## Metadata

- **Competitor:** Amazon Web Services (AWS)
- **Service:** Amazon Elastic Kubernetes Service (EKS)
- **URL:** https://aws.amazon.com/eks/
- **Tier:** 2 (hyperscale — review hàng tháng, benchmark pricing & features)
- **Profile date:** 2026-05-20
- **Last updated:** 2026-05-20
- **Prepared by:** Kubernetes Market Analyst Agent
- **Reviewed by:** [Pending — cần Solution Architect verify]
- **Confidence level:** High (public pricing rõ ràng, docs phong phú)

---

## TL;DR

AWS EKS là Kubernetes service market leader toàn cầu với pricing model trong sạch ($0.10/hr control plane standard support) nhưng có vài "trap costs" lớn: Extended Support 6x ($0.60/hr) cho phiên bản cũ, egress đắt, và 12% Auto Mode fee. Features mới quan trọng 2025-2026: Provisioned Control Plane tiers (XL→8XL), EKS Capabilities (managed ArgoCD/ACK/KRO), Hybrid Nodes. Đối với khách VN: deal lost với EKS thường vì brand/ecosystem chứ không phải kỹ thuật — GreenNode có lợi thế lớn về data residency, VND pricing, tiếng Việt support.

---

## 1. Core Product Profile

| Item | Value | Source |
|---|---|---|
| Tên dịch vụ K8s | Amazon Elastic Kubernetes Service (EKS) | [aws.amazon.com/eks](https://aws.amazon.com/eks/) |
| URL chính thức | https://aws.amazon.com/eks/ | — |
| Ngày ra mắt (GA) | 2018-06-05 | AWS press release (well-known) |
| Kubernetes version support | Multiple versions, standard support 14 tháng + extended 12 tháng | [Pricing page](https://aws.amazon.com/eks/pricing/) |
| Regions available | Tất cả AWS regions (tới 30+ regions global, gần VN: Singapore, Tokyo, Seoul, Hong Kong) | AWS regional availability |
| SLA uptime commitment | 99.95% (standard control plane), 99.99% (Provisioned Control Plane) | EKS SLA |
| Control plane | Fully Managed | — |
| Pricing model | $0.10/hr per cluster (standard) + EC2/Fargate compute riêng | Pricing page |

---

## 2. Feature Matrix

| Dimension | Status | Notes |
|---|---|---|
| Multi-cluster management | ✅ Có | EKS Hybrid Nodes (GA Dec 2024) + Fleets |
| GPU node pool | ✅ Có | P5 (H100), P4 (A100), G6, G4 (T4) |
| Spot node | ✅ Có | EC2 Spot instances integration |
| Auto node provisioning (Karpenter-like) | ✅ Có | Karpenter (AWS-built, native integration) + EKS Auto Mode |
| HPA / VPA | ✅ Có | Standard K8s + CloudWatch metrics |
| Cluster Autoscaler | ✅ Có | + Karpenter alternative |
| KEDA | ✅ Có | Standard K8s, community add-on |
| CNI options | ✅ Có | AWS VPC CNI (default) + alternatives |
| VPC native | ✅ Có | AWS VPC CNI native |
| Network policy | ✅ Có | VPC CNI Network Policy GA |
| CSI driver options | ✅ Có | EBS, EFS, FSx CSI drivers |
| RBAC | ✅ Có | + IRSA (IAM Roles for Service Accounts) |
| Pod Security | ✅ Có | Pod Security Standards |
| Secrets management | ✅ Có | Integration với AWS Secrets Manager, KMS |
| Observability tích hợp | ✅ Có | CloudWatch Container Insights, AWS Distro for OpenTelemetry |
| GPU operator pre-installed | ⚠️ Partial | Phải tự install NVIDIA GPU Operator |
| MIG / fractional GPU | ✅ Có | Standard K8s support với NVIDIA tooling |
| ArgoCD / Flux | ✅ Có | EKS Capabilities (GA Nov 2025) — managed ArgoCD |
| Multi-cloud / hybrid | ✅ Có | EKS Anywhere, Hybrid Nodes |
| ISO 27001 | ✅ Có | AWS-wide certification |
| SOC2 | ✅ Có | AWS-wide |
| PCI-DSS | ✅ Có | AWS-wide |
| Nghị định 13 compliance | ❌ Không (data residency VN) | AWS không có region tại VN; closest = Singapore |
| Support 24/7 | ✅ Có (Business/Enterprise tier) | $$$ — Business tier ≥ 10% bill |
| Tiếng Việt support | ❌ Không | Tiếng Anh primary; some Vietnamese partner support |
| EKS Anywhere | ✅ Có | On-premises K8s với AWS-managed |
| EKS Auto Mode | ✅ Có | Managed nodes với ~12% management fee |
| Provisioned Control Plane | ✅ Có (mới 2025) | XL/2XL/4XL/8XL tiers cho high-throughput |
| EKS Capabilities (managed Argo CD, ACK, KRO) | ✅ Có (GA Nov 2025) | Pay per app/resource managed |
| Hybrid Nodes | ✅ Có (GA Dec 2024) | Connect on-prem hardware tới EKS control plane |

---

## 3. Pricing Summary

> Chi tiết pricing snapshot: `/memory/pricing/2026-05-20_aws-eks_pricing.md` (TBD).

**Highlights từ public pricing:**

### Control Plane
- **Standard Support (first 14 tháng):** $0.10/hr/cluster = $74/tháng (730h)
- **Extended Support (12 tháng sau):** $0.60/hr/cluster = $438/tháng — **6x increase, big cost trap**

### Provisioned Control Plane (optional, on top of standard)
- XL: $1.65/hr
- 2XL: $3.40/hr
- 4XL: $6.90/hr
- 8XL: $13.90/hr

### EKS Auto Mode
- ~12% management fee trên EC2 instance cost (per-second billing, 1-min minimum)
- Example m5.large: ~$0.01152/hr Auto Mode charge

### EKS Hybrid Nodes (per vCPU-hour, tiered)
- First 576k vCPU-hr/tháng: $0.020/vCPU/hr
- Next 576k: $0.014/vCPU/hr
- Lower tiers cho large volume

### EKS Capabilities (managed integrations)
- Argo CD: $0.02771/hr base + $0.00136/Application/hr
- ACK: $0.004482/hr base + $0.000045/resource/hr
- KRO: $0.004482/hr base + $0.000045/RGD/hr

### Compute (EC2 — separate from EKS fee)
- On-demand, Reserved (1Y/3Y, up to 75% off), Spot
- Savings Plans flexible across EC2/Fargate/Lambda

### Storage & Networking (hidden cost lớn)
- EBS gp3 (recommended): $0.08/GB-tháng (us-east-1)
- Cross-AZ data transfer: $0.01/GB each direction → đắt cho HA workload
- Egress internet: $0.09/GB tier đầu → đắt nhất ngành

---

## 4. Positioning & GTM

### Target segment
- **Toàn bộ spectrum:** Startup → SME → Enterprise → Government
- **Strong với:** Khách đã trong AWS ecosystem, enterprise multi-region, dev team đã có AWS skills

### Key messaging
- "The most secure, reliable, and scalable way to run Kubernetes"
- AWS service integration breadth (200+ services)
- Global region coverage
- Hybrid + multi-cloud (Anywhere, Hybrid Nodes)

### Differentiator họ claim
- AWS ecosystem integration (IRSA, VPC, IAM, secrets, observability)
- Karpenter native autoscaling
- Multi-region global presence
- Enterprise compliance (FedRAMP, GovCloud)
- Reserved/Spot/Savings Plans flexibility

### Sales channel
- Direct (AWS Sales) + Partner Network (APN)
- Marketplace (self-serve)
- PLG (free tier, console-driven adoption)

### Geographic strategy
- Global. **Không có AWS region tại VN.** Closest: Singapore (ap-southeast-1)
- Latency VN → Singapore: ~40-50ms (acceptable cho hầu hết workload trừ real-time)

---

## 5. GTM Signals (cho VN market)

| Signal | Observation | Implication |
|---|---|---|
| Không có region VN | Closest = Singapore | GreenNode có data residency advantage rõ ràng |
| Extended Support 6x pricing | $0.60/hr — pain point lớn | Khách compliance-heavy bị penalty nếu không upgrade thường xuyên |
| Provisioned Control Plane tiers mới (2025) | Targeting AI/ML, multi-tenant SaaS | High-end customer segment |
| EKS Capabilities (managed ArgoCD/ACK/KRO) | Đang push managed add-ons | AWS đang move up stack, lock-in deeper |
| Hybrid Nodes | Targeting on-prem khách hàng | Cạnh tranh với on-prem K8s solutions |
| Egress pricing không đổi (vẫn đắt) | $0.09/GB tier đầu | Big migration friction từ AWS ra ngoài |

---

## 6. Customer Evidence

- **Market share:** Market leader toàn cầu Kubernetes managed service (theo industry surveys)
- **VN customers:** [Cần check — nhiều VN startup/enterprise đang dùng]
- **Common praise (G2-style):** Ecosystem maturity, Karpenter, service integration
- **Common complaint:**
  - Extended Support cost shock
  - Cross-AZ data transfer hidden costs
  - Complexity của 4 cost layers (control plane, provisioned CP, worker, add-ons)
  - Steep learning curve cho team mới Kubernetes

---

## 7. SWOT (Góc Nhìn GreenNode)

### Strengths của AWS EKS (so với GreenNode)
- **Ecosystem maturity:** 200+ AWS services tích hợp
- **Karpenter (AWS-built):** Best-in-class node autoscaling
- **Global region presence:** 30+ regions cho khách multi-region
- **Compliance breadth:** ISO, SOC2, PCI-DSS, FedRAMP, HIPAA
- **Documentation + community:** Vô đối
- **Tooling ecosystem:** Terraform, Pulumi, CDK provider mature

### Weaknesses của AWS EKS (so với GreenNode)
- **Không có region VN:** Data residency Nghị định 13 không thỏa
- **Pricing trap:** Extended Support 6x, egress cao, cross-AZ
- **Tiếng Việt support hạn chế:** Phải qua phiên dịch hoặc partner
- **USD pricing:** FX risk cho khách VN
- **Latency từ VN → Singapore:** 40-50ms — không phù hợp real-time
- **Complexity:** 4 cost layers gây khó forecast cho SME
- **Enterprise sales heavy:** SME hard reach Support 24/7 (cần Business tier $)

### Opportunities GreenNode có thể khai thác
- **Data residency VN:** Push hard với regulated industry (banking, healthcare, gov)
- **VND pricing transparency:** No FX risk, predictable bills
- **Tiếng Việt 24/7:** Operational support cho khách VN team
- **TCO advantage:** Không có egress trap, support included thay vì tier-based
- **Migration playbook:** EKS → GreenNode (Velero, manifest portable)
- **Compliance Nghị định 13:** Mandate cho data nhạy cảm theo luật VN

### Threats từ AWS EKS
- **Khách Enterprise đa quốc gia:** Cần consistency multi-region toàn cầu → AWS thắng
- **Ecosystem lock-in:** Khách đã dùng RDS, S3, Lambda khó break out
- **Karpenter advantage:** AI startup developer prefer
- **EKS Anywhere/Hybrid:** Khách on-prem có thể chọn EKS Anywhere thay vì GreenNode
- **AWS Activate startup credits:** Free $100k credit dụ AI startup

---

## 8. Strategic Implications

| Finding | Impact | Cần action? | Bộ phận |
|---|---|---|---|
| AWS không có region VN — data residency advantage GreenNode rõ | High | Có — push Nghị định 13 positioning | Marketing |
| Extended Support 6x là pain point lớn | Medium | Có — promote GreenNode upgrade simplicity | Sales enablement |
| EKS egress đắt → TCO comparison favor GreenNode | High | Có — build TCO calculator visible | Marketing + Sales |
| Karpenter là gap nếu GreenNode chưa có | High | Có — assess Karpenter trong VKS roadmap | Engineering |
| EKS Anywhere/Hybrid Nodes cạnh tranh on-prem | Medium | Theo dõi — chưa cần action | Product |
| Tiếng Việt 24/7 là differentiator clear | High | Có — promote rõ trong sales materials | Marketing |

---

## 9. Recommendations

**P0 (must do):**
- Build TCO comparison calculator: GreenNode VKS vs EKS (bao gồm egress, cross-AZ, support)
- Build migration playbook EKS → GreenNode (parallel với playbook của VNG)
- Publish Nghị định 13 compliance evidence rõ ràng

**P1 (should do):**
- Assess Karpenter support — đây là default cho new AWS users
- Develop sales talk track về "Extended Support trap" và "egress trap"
- Build battlecard VKS vs EKS cho enterprise + AI startup segments

**P2 (nice to do):**
- Monitor EKS Capabilities pricing → có thể repurpose cho GreenNode managed add-ons
- Track Provisioned Control Plane adoption — signal cho high-end demand

---

## 10. Sources

| Nguồn | URL | Ngày truy cập | Confidence |
|---|---|---|---|
| AWS EKS Pricing | https://aws.amazon.com/eks/pricing/ | 2026-05-20 | High |
| EKS Extended Support pricing | https://aws.amazon.com/blogs/containers/amazon-eks-extended-support-for-kubernetes-versions-pricing/ | 2026-05-20 | High |
| EKS Provisioned Control Plane | https://docs.aws.amazon.com/eks/latest/userguide/eks-provisioned-control-plane.html | 2026-05-20 | High |
| EKS Pricing analysis (Cloud Burn) | https://cloudburn.io/blog/amazon-eks-pricing | 2026-05-20 | High |
| EKS Pricing breakdown (Cloudchipr) | https://cloudchipr.com/blog/eks-pricing | 2026-05-20 | Medium |
| EKS Cost optimization (ScaleOps) | https://scaleops.com/blog/what-is-amazon-eks-cost-optimization-and-how-to-actually-do-it/ | 2026-05-20 | Medium |
| EKS Guide 2026 (Sedai) | https://sedai.io/blog/guide-amazon-eks-managed-kubernetes-aws | 2026-05-20 | Medium |
| EKS Pricing Calculator | https://cloudburn.io/tools/amazon-eks-pricing-calculator | 2026-05-20 | High |

---

## Refresh Notes

**Next refresh due:** 2026-06-20 (Tier 2 = hàng tháng)

**Refresh triggers (ngoài lịch):**
- AWS announces VN region (KHẢ NĂNG GAME-CHANGER)
- Major pricing change (Extended Support, Auto Mode fee, egress)
- New EKS feature targeting AI workload (lớn)
- AWS reinvent annual announcements (cuối Nov mỗi năm)

**Open questions cần investigation:**
1. AWS có kế hoạch mở region VN không? (Nếu có → game changer)
2. Khách VN nào đang dùng EKS — cần customer reference research
3. Local partner AWS tại VN có cung cấp "Tiếng Việt support proxy" không?
4. EKS Anywhere uptake trong VN market

---

*Template based on `/skills/competitor-analysis.md` v1.0.0*
*Initial research từ public AWS docs và industry analysis. Confidence: High cho pricing/features, Medium cho VN market dynamics.*
