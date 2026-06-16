# Pricing Snapshot: AWS EKS

## Metadata

- **Provider:** Amazon Web Services
- **Service:** Elastic Kubernetes Service (EKS)
- **Timestamp:** 2026-06-17 ICT
- **Region:** us-east-1 (N. Virginia) — baseline; ap-southeast-1 (Singapore) cho VN customers (+10-15%)
- **Currency:** USD (AWS niêm yết USD, chưa VAT)
- **FX rate dùng:** 1 USD = ~26,200 VND (Vietcombank mid-rate, 2026-06-17: buy 26,130 / sell 26,410)
- **Nguồn pricing:** https://aws.amazon.com/eks/pricing/ (verified 2026-06-17)
- **Prepared by:** Competitive Intelligence — GreenNode VKS
- **Next refresh:** 2026-06-24

---

## Control Plane

- **Loại:** Fully Managed
- **Standard Support (first 14 tháng):** $0.10/giờ/cluster = **~$73/tháng** (730h)
- **Extended Support (tháng 15-26):** $0.60/giờ/cluster = **~$438/tháng** (6× increase)
- **HA mặc định:** Có (multi-AZ)
- **SLA control plane:** 99.95% standard, 99.99% Provisioned Control Plane
- **Cost trap:** Không upgrade K8s version trong 14 tháng → penalty 6× — HA setup với 3 clusters = $1,314/tháng extra

---

## EKS Provisioned Control Plane (GA tháng 11/2025)

| Tier | $/giờ | $/tháng (730h) | Use case |
|---|---|---|---|
| Standard (default) | $0 extra | $0 | General workloads |
| XL | $1.65 | $1,205 | High API call volumes |
| 2XL | $3.40 | $2,482 | AI/ML training clusters |
| 4XL | $6.90 | $5,037 | Multi-tenant SaaS |
| 8XL | $13.90 | $10,147 | Largest production clusters |

---

## EKS Auto Mode

- **Fee:** ~12% management fee trên EC2 instance on-demand price
- **Billing:** Per-second, 1-min minimum
- **Example:** m5.large ($0.096/hr) + Auto Mode (~$0.01152/hr) = $0.10752/hr effective
- **Lưu ý:** Savings Plans không discount phần Auto Mode fee — chỉ discount EC2 portion

---

## EKS Hybrid Nodes (GA tháng 12/2024)

Connect on-prem hardware tới EKS control plane:

| Tier (monthly vCPU-hours) | $/vCPU/hr |
|---|---|
| First 576,000 | $0.020 |
| Next 576,000 | $0.014 |
| Next 4,608,000 | $0.010 |
| Next 5,760,000 | $0.008 |
| Over 11,520,000 | $0.006 |

---

## EKS Capabilities (GA tháng 11/2025)

| Capability | Base $/capability-hour | Usage charge |
|---|---|---|
| Argo CD | $0.03/hr | $0.0015/application/hr |
| ACK (AWS Controllers for K8s) | $0.005/hr | $0.00005/resource/hr |
| KRO (Kubernetes Resource Orchestrator) | $0.005/hr | $0.00005/RGD instance/hr |

---

## Compute — On-Demand (us-east-1)

| Instance | vCPU | RAM | $/giờ | VND/tháng (730h) |
|---|---|---|---|---|
| m5.large | 2 | 8GB | $0.096 | ~1.84M |
| m5.xlarge | 4 | 16GB | $0.192 | ~3.68M |
| m5.2xlarge | 8 | 32GB | $0.384 | ~7.36M |
| m5.4xlarge | 16 | 64GB | $0.768 | ~14.72M |
| m5a.xlarge | 4 | 16GB | $0.172 | ~3.30M |
| m5a.2xlarge | 8 | 32GB | $0.344 | ~6.60M |
| c5.large (compute opt.) | 2 | 4GB | $0.085 | ~1.63M |

> **ap-southeast-1 (Singapore) +10-15%** so với us-east-1.

---

## Compute — Reserved (Standard, 1-year, No Upfront, us-east-1)

| Instance | On-demand | RI 1Y | Discount |
|---|---|---|---|
| m5.large | $0.096 | ~$0.057 | ~41% |
| m5.xlarge | $0.192 | ~$0.114 | ~41% |
| m5.2xlarge | $0.384 | ~$0.228 | ~41% |

**RI 3-year All Upfront:** Up to 75% discount.
**Savings Plans:** 30-50% off, flexible across EC2/Fargate/Lambda.

---

## Compute — Spot

- **Discount:** 50-90% off on-demand (theo demand thực tế)
- **Eviction notice:** 2 phút
- **Khả dụng:** Tất cả regions

---

## GPU — On-Demand (us-east-1, AI/ML workloads)

| GPU Instance | GPU | VRAM | $/giờ on-demand | VND/giờ |
|---|---|---|---|---|
| g4dn.xlarge | 1× T4 | 16GB | ~$0.526 | ~13,800 |
| g6.xlarge | 1× L4 | 24GB | ~$0.805 | ~21,100 |
| p4d.24xlarge | 8× A100 40GB | 320GB | ~$32.77 | ~859,000 |
| p5.48xlarge | 8× H100 80GB | 640GB | ~$98.32 | ~2,576,000 |

> p5 chỉ bán theo cluster 8× H100 (không tách 1×). Capacity Blocks cho ML: reserve block 1-14 ngày.

---

## Storage (us-east-1)

| Loại | Đơn giá |
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
| NAT Gateway | $0.045/hr ($32.85/month) + $0.045/GB processed |
| Public IPv4 (từ 02/2024) | $0.005/hr idle ($3.60/month) |
| Cross-AZ (same region) | $0.01/GB mỗi chiều → $0.02/GB round-trip |
| VPC Peering in-region | Free; cross-region $0.02/GB |

---

## Egress (Internet Out — Cost Trap Lớn Nhất)

| Loại | Đơn giá |
|---|---|
| First 100GB/tháng | **Free** |
| Next 10TB | $0.09/GB |
| Next 40TB | $0.085/GB |
| Next 100TB | $0.07/GB |
| > 150TB | $0.05/GB |

> **Key insight:** 5TB/month egress = ~$441/tháng. So với GreenNode VKS (egress rẻ hơn hoặc miễn phí nội địa), đây là $4-5k/năm khác biệt cho cluster mid-size.

---

## Support Tiers

| Tier | Giá | SLA Response | 24/7? | Tiếng Việt? |
|---|---|---|---|---|
| Basic | $0 | Best effort | ❌ | ❌ |
| Developer | $29/tháng min | 12-24h business hours | ❌ | ❌ |
| Business | $100/tháng **hoặc 10% AWS bill** (lấy cao hơn) | 1-4h, prod down 1h | ✅ | ❌ |
| Enterprise | $15,000/tháng **hoặc 10% bill** | 15 min prod down, TAM | ✅ | ❌ |

---

## Free Tier / Credit

- **AWS Activate (startup):** Lên đến $100k credit cho qualified startups
- **Always Free:** EC2 t2.micro 750h/tháng (12 tháng đầu)
- **EKS-specific:** **Không có free tier** cho EKS control plane

---

## TCO Example — Mid Production Cluster (Scenario S2)

**Cấu hình:** 6× m5.2xlarge (8vCPU/32GB) + 500GB EBS gp3 + 2× ALB + 5TB egress/tháng + Business Support

| Component | Đơn giá | Số lượng | USD/tháng |
|---|---|---|---|
| EKS Control Plane (Standard) | $0.10/hr | 730h | $73 |
| Compute m5.2xlarge | $0.384/hr | 6 × 730h | $1,683 |
| EBS gp3 storage | $0.08/GB | 500GB | $40 |
| ALB (2×) | $0.0225/hr + LCU | 2 × 730h + ~100 LCU | ~$113 |
| Egress 5TB internet | $0.09/GB (sau 100GB free) | ~4,900 GB | $441 |
| Cross-AZ traffic (est. 1TB) | $0.01/GB × 2 | 1,000 GB | $20 |
| EBS Snapshot (250GB) | $0.05/GB | 250GB | $13 |
| Business Support (10%) | 10% | — | ~$238 |
| **Total** | | | **~$2,621/tháng** |

**Quy đổi VND (FX 26,200):** **~68,670,000 VND/tháng**

---

## Hidden Cost Flags

⚠️ **Top 3 cost traps cho EKS khách VN:**

1. **Extended Support 6×:** Không upgrade K8s trong 14 tháng → $73 → $438/tháng/cluster. Production setup 3 clusters = $1,314/tháng extra.

2. **Egress trap:** 5TB egress = $441/tháng. GreenNode VKS với egress trong nước rẻ hơn → $4-5k/năm lợi thế TCO.

3. **Business Support gần như bắt buộc:** Production không thể chạy Basic → +10% bill minimum. Với cluster $2,000+/tháng = $200+/tháng chỉ cho support.

4. **FX risk VND:** USD billing — VND depreciation (hiện 26,200/USD, 2024 là ~25,200) tăng bill thực tế ~4% chỉ trong 1 năm.

---

## So sánh vs GreenNode VKS

| Component | AWS EKS (us-east-1) | GreenNode VKS | Gap |
|---|---|---|---|
| Control plane fee | $73/tháng standard; $438 extended | [TBD] | [TBD] |
| Compute 4vCPU/16GB | $140/tháng (m5.xlarge) | [TBD] | [TBD] |
| Egress 1TB | $90 | [TBD — likely lower/free nội địa] | Potentially $90+/TB |
| Support production | +10% bill ($200+) | [TBD — likely included] | Potentially significant |
| Tiếng Việt support | ❌ | ✅ | Qualitative win |
| Data residency VN | ❌ Singapore | ✅ | Compliance win |
| VND billing | ❌ USD + FX risk | ✅ | ~4%+/year savings |

> **Action:** Hoàn thiện GreenNode VKS pricing snapshot để có TCO comparison thực tế.

---

## Pricing Changes từ 2026-05-20

- **EKS Capabilities Argo CD:** Base rate cập nhật $0.03/hr (từ $0.02771/hr) — tăng nhẹ
- **EKS Capabilities ACK/KRO:** Base rate cập nhật $0.005/hr (từ $0.004482/hr) — tăng nhẹ
- Tất cả các mức giá khác (control plane, EC2, storage, egress): **Không có thay đổi**

---

## Sources

| Nguồn | URL | Ngày |
|---|---|---|
| AWS EKS Pricing (official) | https://aws.amazon.com/eks/pricing/ | 2026-06-17 |
| Cloud Burn EKS Pricing Guide | https://cloudburn.io/blog/amazon-eks-pricing | 2026-06-17 |
| EKS Extended Support | https://sedai.io/blog/understanding-aws-eks-kubernetes-pricing-and-costs | 2026-06-17 |
| AWS Pricing Changes 2026 | https://spendark.com/blog/aws-pricing-changes-2026/ | 2026-06-17 |
| CloudZero EKS Pricing 2026 | https://www.cloudzero.com/blog/eks-pricing/ | 2026-06-17 |
| Vietcombank FX (06/2026) | vietnam.vn + vietnamplus.vn | 2026-06-17 |

---

*Pricing có thể thay đổi. Verify aws.amazon.com/eks/pricing/ trước khi dùng cho deal cụ thể.*
