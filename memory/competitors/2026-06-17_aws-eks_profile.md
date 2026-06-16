# Competitor Profile: AWS EKS

## Metadata

- **Competitor:** Amazon Web Services
- **Service:** Elastic Kubernetes Service (EKS)
- **URL chính thức:** https://aws.amazon.com/eks/
- **Threat Level:** 🟡 TRUNG BÌNH (direct VN compete) / 🔴 CAO (AI/ML narrative)
- **Profile date:** 2026-06-17
- **Last updated:** 2026-06-17
- **Confidence:** High (AWS public announcements và pricing page verified)

---

## TL;DR

AWS EKS tiếp tục mở rộng AI-native Kubernetes capabilities với tốc độ nhanh hơn bất kỳ local provider nào — SageMaker container caching (06/2026), P-EAGLE speculative decoding (06/2026), EKS Auto Mode, EKS Hybrid Nodes. Tuy nhiên GreenNode vẫn có lợi thế với khách hàng VN: VND billing, data residency, tiếng Việt support, và egress cost giảm đáng kể. AWS threat level với VN SME/startup ở mức trung bình; với enterprise AI workload ở mức cao.

---

## 1. Product Profile — Cập nhật 2026

| Mục | Trạng thái | Ghi chú |
|---|---|---|
| EKS Control Plane Standard | $0.10/hr ($73/month) | Không đổi từ 2020 |
| EKS Extended Support | $0.60/hr ($438/month) | Áp dụng sau 14 tháng standard, không thay đổi |
| EKS Provisioned Control Plane | GA từ 11/2025 | XL → 8XL tiers |
| EKS Auto Mode | GA, ~12% EC2 on-demand fee | Xem chi tiết trong pricing file |
| EKS Hybrid Nodes | GA từ 12/2024 | On-prem hardware → EKS control plane |
| EKS Capabilities (Argo CD/ACK/KRO) | GA từ 11/2025 | Managed Kubernetes add-ons |
| SageMaker container image caching | ✅ Mới — 2026-06-16 | Tăng tốc scale-out AI models 2× |
| P-EAGLE speculative decoding | ✅ Mới — 2026-06-16 | Tối ưu inference realtime trên SageMaker AI |
| EKS Pod Identity session policies | ✅ Mới 2026 | Dynamic IAM scope-down per pod |
| Enhanced network policy | ✅ Mới 2026 | Improved K8s network security |

---

## 2. AI/ML Positioning (2026)

AWS đang dịch chuyển từ hạ tầng K8s thuần túy sang **AI-native Kubernetes runtime**:

- **Container caching:** Pull image một lần, scale instantly → giải quyết cold-start problem cho LLM deployment
- **P-EAGLE speculative decoding:** Parallel inference optimization → giảm latency realtime inference
- **SageMaker ↔ EKS integration:** AI workflows ngày càng tích hợp sâu với EKS cluster

Đây là gap lớn: AWS đang build AI-specific K8s optimizations mà GreenNode và local providers chưa có equivalent.

---

## 3. Điểm Mạnh (vs GreenNode)

- **AI-native features vượt trội:** SageMaker container caching, P-EAGLE — tốc độ innovation > local providers
- **Global infrastructure:** Multi-region, low-latency đến global customers; nearest VN region: ap-southeast-1 (Singapore)
- **Ecosystem sâu nhất:** IAM, EKS Pod Identity, ACK, KRO, Argo CD managed — full GitOps stack
- **EKS Auto Mode:** Self-managing nodes — giảm operational burden đáng kể
- **Hybrid Nodes:** On-prem K8s workload → EKS control plane, hấp dẫn enterprise hybrid
- **Spot + Reserved pricing:** Flexibility lớn cho cost optimization

## 4. Điểm Yếu / Cơ hội cho GreenNode

- **USD billing + FX risk:** 1 USD ≈ 26,200 VND (06/2026) — VND depreciation tăng chi phí thực tế cho khách VN
- **Egress trap:** 5TB/month internet egress ≈ $441 — GreenNode có thể win hard trên TCO nếu egress rẻ hơn
- **Extended Support 6×:** Khách không upgrade K8s kịp → $438/month/cluster (vs $73) — phức tạp cost planning
- **Data residency:** AWS không có data center tại VN → ap-southeast-1 Singapore = latency + compliance issue
- **Không có tiếng Việt support:** Business support không có VI — enterprise VN cần local support
- **No business hours VN:** Production incident → English-only ticket system
- **Business Support tối thiểu $100/month hoặc 10% bill:** Dễ reach $1000+/month

---

## 5. Threat Assessment

| Phân khúc | Mức độ đe dọa | Lý do |
|---|---|---|
| VN SME/Startup | 🟡 Trung bình | AWS Activate credits hút startup nhưng VND pricing + compliance + egress tạo churn |
| Enterprise VN | 🟡 Trung bình | Data residency và compliance là blocker ngày càng mạnh (BVDLCN 2025) |
| AI/ML workload | 🔴 Cao | Container caching + P-EAGLE + SageMaker ecosystem = AWS pull mạnh nhất 2026 |
| Government VN | 🟢 Thấp | Data sovereignty requirements chặn AWS gần hoàn toàn |

---

## 6. Signals cần theo dõi

- AWS mở **data center tại VN** (nếu xảy ra, threat level tăng mạnh toàn diện)
- AWS announce **Vietnam billing / VND support** hoặc local invoice
- Thêm **AI-native EKS features** (container caching chỉ là bước đầu — sẽ còn nhiều hơn)
- **Luật BVDLCN 2025 enforcement** tăng cường → block AWS cho regulated industry
- **Egress pricing giảm** — thu hẹp TCO gap với GreenNode

---

## 7. GreenNode Positioning vs AWS

| Dimension | AWS EKS | GreenNode VKS | GreenNode Win? |
|---|---|---|---|
| Data residency VN | ❌ Singapore | ✅ Vietnam | ✅ Compliance win |
| VND billing | ❌ USD billing | ✅ VND | ✅ FX risk removed |
| Tiếng Việt support 24/7 | ❌ | ✅ | ✅ Qualitative win |
| AI container caching | ✅ SageMaker | ❌ Chưa có | ❌ AWS win |
| TCO (5TB egress cluster) | ~$2,600-2,640/month | [TBD — verify] | Likely ✅ nếu egress rẻ hơn |
| Extended Support risk | ❌ 6× cost trap | N/A | ✅ Simplicity win |
| Enterprise ecosystem | ✅ Sâu nhất | 🟡 Đang xây | ❌ AWS win |

---

## Refresh Notes

- **Next refresh:** 2026-06-24
- **Trigger:** Thêm AI-native EKS feature, AWS Vietnam DC announcement, BVDLCN enforcement updates
