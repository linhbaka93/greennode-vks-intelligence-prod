# Pricing Snapshot: AWS EKS

## Metadata

- **Provider:** Amazon Web Services
- **Service:** Elastic Kubernetes Service (EKS)
- **Timestamp:** 2026-05-20 10:00 ICT
- **Region:** us-east-1 (N. Virginia) — baseline; ap-southeast-1 (Singapore) cho VN customers
- **Currency:** USD (AWS niêm yết USD, chưa VAT)
- **FX rate dùng:** 1 USD = ~25,200 VND (Vietcombank giữa 2026-05-20) — verify trước production use
- **Nguồn pricing:** https://aws.amazon.com/eks/pricing/
- **Prepared by:** Kubernetes Market Analyst Agent
- **Next refresh:** 2026-06-20 (Tier 2 = hàng tháng)

---

## Control Plane

- **Loại:** Fully Managed
- **Phí (Standard Support — first 14 tháng):** $0.10/giờ/cluster = ~$74/tháng (730h)
- **Phí (Extended Support — 12 tháng sau):** $0.60/giờ/cluster = ~$438/tháng (6x increase)
- **HA mặc định:** Có (multi-AZ)
- **SLA control plane:** 99.95% standard, 99.99% Provisioned Control Plane
- **Ghi chú:** Big cost trap — khách phải upgrade K8s version trong 14 tháng để tránh penalty 6x

---

## Provisioned Control Plane (optional, on top of standard)

| Tier | $/giờ | $/tháng (730h) |
|---|---|---|
| Standard (default) | $0 extra | $0 |
| XL | $1.65 | $1,205 |
| 2XL | $3.40 | $2,482 |
| 4XL | $6.90 | $5,037 |
| 8XL | $13.90 | $10,147 |

**Use case:** Targeting AI/ML training clusters, multi-tenant SaaS, high API call volumes.

---

## Compute — On-Demand (us-east-1, sample instances cho K8s nodes)

| Instance | vCPU | RAM | $/giờ | VND/tháng (730h) |
|---|---|---|---|---|
| m5.large | 2 | 8 | $0.096 | ~1.77M |
| m5.xlarge | 4 | 16 | $0.192 | ~3.53M |
| m5.2xlarge | 8 | 32 | $0.384 | ~7.07M |
| m5.4xlarge | 16 | 64 | $0.768 | ~14.13M |
| c5.large (compute optimized) | 2 | 4 | $0.085 | ~1.56M |

> **Note:** Pricing tại ap-southeast-1 (Singapore) thường +10-15% so với us-east-1. Verify cho VN customer specific.

---

## Compute — Reserved (Standard, 1-year, No Upfront)

| Instance | On-demand | RI 1Y | Discount |
|---|---|---|---|
| m5.large | $0.096 | ~$0.057 | ~41% |
| m5.xlarge | $0.192 | ~$0.114 | ~41% |

**RI 3-year All Upfront:** Up to 75% discount.

**Savings Plans:** Flexible across EC2/Fargate/Lambda — typically 30-50% off, no instance family lock-in.

---

## Compute — Spot

- **Khả dụng:** Có (EC2 Spot)
- **Discount range:** 50-90% off on-demand (theo demand)
- **Eviction notice:** 2 phút
- **Region available:** Tất cả regions

---

## GPU (P series — AI/ML workloads)

| GPU Instance | GPU | VRAM | $/giờ on-demand (us-east-1) |
|---|---|---|---|
| g4dn.xlarge | 1× T4 | 16GB | ~$0.526 |
| g6.xlarge | 1× L4 | 24GB | ~$0.805 |
| p4d.24xlarge | 8× A100 40GB | 320GB total | ~$32.77 |
| p5.48xlarge | 8× H100 80GB | 640GB total | ~$98.32 |

> **Note 1:** p5 chỉ bán theo cluster 8× H100 (không tách 1×). Cụm bao gồm NVLink, 192 vCPU, 2 TB RAM.
> **Note 2:** Capacity Blocks cho ML — reserve trước trong block 1-14 ngày, có discount.

---

## Storage

| Loại | Đơn giá (us-east-1) |
|---|---|
| EBS gp3 (default cho K8s) | $0.08/GB/tháng |
| EBS gp2 (legacy) | $0.10/GB/tháng |
| EBS io2 | $0.125/GB/tháng + IOPS phí |
| EBS Snapshot | $0.05/GB/tháng (incremental) |
| S3 Standard | $0.023/GB/tháng |
| EFS Standard | $0.30/GB/tháng |

---

## Networking — Hidden Costs

| Component | Đơn giá |
|---|---|
| Network Load Balancer | $0.0225/hr + $0.006/LCU |
| Application Load Balancer | $0.0225/hr + $0.008/LCU |
| NAT Gateway | $0.045/hr + $0.045/GB processed |
| Public IPv4 (charge từ 2024) | $0.005/hr idle |
| VPC Peering | Trong region: free; cross-region: $0.02/GB |

---

## Egress (Big Cost Driver)

| Loại | Đơn giá |
|---|---|
| Inter-AZ (same region) | $0.01/GB each direction → effectively $0.02/GB round-trip |
| Inter-region | $0.02/GB (varies) |
| Internet egress (first 100 GB/tháng) | Free (new in 2023) |
| Internet egress (next 10 TB) | $0.09/GB |
| Internet egress (next 40 TB) | $0.085/GB |
| Internet egress (next 100 TB) | $0.07/GB |
| Internet egress (> 150 TB) | $0.05/GB |

> **Key insight:** Egress là cost trap lớn nhất khi migrate ra ngoài AWS. Khách cần factor vào TCO comparison.

---

## EKS Auto Mode (mới)

- ~12% management fee trên EC2 instance cost
- Per-second billing, 1-min minimum
- Example: m5.large = $0.096 + ~$0.01152 Auto Mode charge = $0.10752/giờ effective

---

## EKS Hybrid Nodes (mới — GA Dec 2024)

Connect on-prem hardware tới EKS control plane, billed per vCPU-hour:

| Tier (monthly vCPU-hours) | $/vCPU/hr |
|---|---|
| First 576,000 | $0.020 |
| Next 576,000 | $0.014 |
| Next 4,608,000 | $0.010 |
| Next 5,760,000 | $0.008 |
| Over 11,520,000 | $0.006 |

---

## EKS Capabilities (managed Argo CD, ACK, KRO — GA Nov 2025)

| Capability | Base hourly | Usage charge |
|---|---|---|
| Argo CD | $0.02771/hr | $0.00136 per Application/hr |
| ACK (AWS Controllers for K8s) | $0.004482/hr | $0.000045 per resource/hr |
| KRO (Kubernetes Resource Orchestrator) | $0.004482/hr | $0.000045 per RGD/hr |

---

## Support Tier

| Tier | Giá | SLA response | 24/7? | Tiếng Việt? |
|---|---|---|---|---|
| Basic / Free | $0 | Best effort | Không | Không |
| Developer | $29/tháng min | 12-24h business hours | Không | Không |
| Business | $100/tháng or 10% AWS bill (whichever higher) | 1-4 hours, prod down 1h | Có | Không |
| Enterprise | $15,000/tháng or 10% bill | 15 min cho prod down | Có + TAM | Không |

---

## Free Tier / Credit

- **AWS Activate (startup credits):** Up to $100k credit cho qualified startups
- **Always Free:** EC2 t2.micro 750 hours/tháng (12 tháng đầu), một số service free tier
- **EKS-specific:** Không có free tier cho EKS control plane

---

## TCO Example — Mid Production Cluster (Scenario S2)

**Cấu hình:** 6× m5.2xlarge (8vCPU/32GB) + 500GB EBS + 2× ALB + 5TB egress/tháng + Business Support

| Component | Đơn giá | Số lượng | Thành tiền (USD/tháng) |
|---|---|---|---|
| EKS Control Plane (Standard) | $0.10/hr | 730h | $73 |
| Compute m5.2xlarge | $0.384/hr | 6 × 730h | $1,683 |
| EBS gp3 storage | $0.08/GB/tháng | 500GB | $40 |
| ALB | $0.0225/hr + $0.008/LCU | 2 × 730h + 100 LCU | $113 |
| Egress 5TB internet | $0.09/GB (after 100GB free) | 4,900 GB | $441 |
| Cross-AZ traffic (estimated 1TB) | $0.01/GB × 2 | 1,000 GB | $20 |
| Snapshot (250GB) | $0.05/GB/tháng | 250GB | $13 |
| Business Support (10% bill) | 10% | — | ~$238 |
| **Total** | | | **~$2,621/tháng** |

**Quy đổi VND:** ~66 triệu VND/tháng

---

## Hidden Cost Flags

⚠️ **Top 3 hidden costs cho EKS:**

1. **Extended Support 6x:** Nếu không upgrade K8s trong 14 tháng, control plane jump $74 → $438/tháng (per cluster). HA setup với 3 clusters = $1,314/tháng extra.

2. **Egress trap:** 5TB egress = $441/tháng. So với GreenNode VKS (giả định không charge egress hoặc rất rẻ), đây là $4-5k/năm khác biệt cho cluster vừa.

3. **Business Support gần như bắt buộc:** Production workload không thể chạy với Basic support → +10% bill minimum.

---

## Comparison vs GreenNode VKS

| Component | AWS EKS (us-east-1) | GreenNode VKS | Gap |
|---|---|---|---|
| Control plane | $74/tháng standard, $438 extended | [TBD — verify] | [TBD] |
| Compute 4vCPU/8GB | ~$140/tháng (m5.xlarge) | [TBD] | [TBD] |
| Egress 1TB | $90 | [TBD — likely lower or free] | Potentially huge |
| Support cho production | +10% bill ($200+) | [TBD — likely included] | Potentially significant |
| Tiếng Việt support | Không | Có | Qualitative win |
| Data residency VN | Không (closest SG) | Có | Compliance win |
| FX risk | USD billing | VND billing | Qualitative win |

> **Action cho GreenNode team:** Hoàn thiện pricing snapshot của VKS song song để có TCO comparison thực tế.

---

## Sources

| Nguồn | URL | Ngày |
|---|---|---|
| AWS EKS Pricing (official) | https://aws.amazon.com/eks/pricing/ | 2026-05-20 |
| EKS Extended Support pricing | https://aws.amazon.com/blogs/containers/amazon-eks-extended-support-for-kubernetes-versions-pricing/ | 2026-05-20 |
| EKS Provisioned Control Plane | https://docs.aws.amazon.com/eks/latest/userguide/eks-provisioned-control-plane.html | 2026-05-20 |
| Cloud Burn pricing analysis | https://cloudburn.io/blog/amazon-eks-pricing | 2026-05-20 |
| Cloudchipr EKS pricing | https://cloudchipr.com/blog/eks-pricing | 2026-05-20 |
| Medium analysis (Tania Fedirko) | https://medium.com/@taniafedirko/understanding-amazon-eks-pricing-43041f9d2c51 | 2026-05-20 |

---

*Template based on `/skills/pricing-analysis.md` v1.0.0*
*Pricing có thể thay đổi. Verify pricing page trước khi dùng cho deal cụ thể.*
