# Report Templates (cho synthesis — weekly digest & monthly brief)

Synthesis nạp file này để gộp claim từ specialist thành output cuối. Cấu trúc dưới đây
distill từ các báo cáo đã được leadership đọc — giữ đúng thứ tự section và format.

Áp dụng `_output_policy.md`: nhãn nguồn inline, dòng so-what, trung thực về data gap.

---

## Weekly Digest

Thứ tự section (khớp block Telegram):

```
# Báo Cáo Thị Trường Kubernetes — Tuần <từ> đến <đến>

### TÓM TẮT TUẦN NÀY
3 điểm quan trọng nhất, mỗi điểm: [Nhãn] **tiêu đề tín hiệu** — tác động ngắn — Nguồn

### ĐỘNG THÁI ĐỐI THỦ
Theo từng đối thủ, có severity + tier: #### <Tên> (🔴 CAO — Tier 1)
- [Nhãn] động thái (hoặc "[Không có tin mới] Dựa trên hồ sơ workspace:…")
  **GreenNode nên:** <action> — Nguồn

### TÍN HIỆU THỊ TRƯỜNG
- [Nhãn] **tín hiệu** — Tác động trực tiếp: … — Nguồn

### VIỆC CẦN LÀM NGAY
<emoji> <P0/P1/P2> | <action> | <Owner> | <Deadline>

### THEO DÕI THÊM
- **<chủ đề>:** theo dõi gì + lý do + nơi check (URL/repo cụ thể)

*Footer: timestamp ICT | giải thích nhãn | nêu rõ nếu thiếu loại nguồn nào*
```

Quy ước:
- Severity đối thủ: 🔴 cao · 🟡 trung bình · 🟢 thấp; luôn kèm Tier.
- Priority action: 🔴 P0 · 🟡 P1 · 🟢 P2.
- Action item bắt buộc đủ 4 trường (Priority | Action | Owner | Deadline).

---

## Daily Brief

Thứ tự section cho Q&A current-research và `/tasks/daily-intelligence`:

```
# GreenNode VKS Intelligence — Daily Brief

## TL;DR
1-3 điểm ngắn nhất, ưu tiên claim đã xác nhận.

## Tin đã xác nhận
- [RSS]/[Social]/[Scrape]/[Workspace] **tín hiệu** — Tác động tới GreenNode: ... — GreenNode nên: ... — Nguồn/ngày

## Cần xác minh
- Nguồn bị thiếu URL/ngày, social bị login wall, hoặc headline chưa đọc được nội dung.

## Dự đoán / Suy luận
- [Suy luận] nhận định logic từ các claim đã xác nhận, ghi rõ cơ sở.

## Action Items
Priority | Action | Owner | Deadline

## Sources
Danh sách nguồn đã dùng.
```

Quy ước:
- Social post public chỉ đưa vào "Tin đã xác nhận" khi đọc được nội dung + có URL + ngày fetch/post.
- Nếu chỉ biết có link social nhưng chưa đọc được nội dung, đưa vào "Cần xác minh".
- Không đổ JSON thô của agent vào brief.

---

## Monthly Brief

```
# Monthly Strategic Summary — <YYYY-MM>
*Tổng hợp từ N weekly digests: <ngày> | Đọc < 15 phút*

## 1. TL;DR — Top 3 Strategic Takeaways
Mỗi takeaway: **tiêu đề in đậm:** diễn giải + framing thời gian.

## 2. Competitor Moves
- "Ai move mạnh nhất tháng?" — narrative phân tích, không chỉ list.
- "Pattern nổi bật xuyên tháng" — pattern across weeks (dùng [Suy luận], nêu cơ sở).

## 3. Market Signals
Theo trend, mỗi trend gắn màu mức độ + framing "cửa sổ cơ hội có thời hạn".

## 4. Pricing Intelligence
Nếu không có data: mở đầu bằng block ⚠️ Giới hạn dữ liệu, rồi nêu điểm [Workspace] còn giá trị.

## 5. GreenNode VKS Positioning
Bảng so sánh đa chiều, ký hiệu: ✅ mạnh · ❓ chưa xác minh · 🔨 đang build · ❌ thiếu.

## 6. Strategic Recommendations
Mỗi rec: emoji priority + **Owner gợi ý** + **Deadline** + rationale đầy đủ (vì sao + impact).

## 7. Next Month Watch List
Bảng: | Ưu tiên | Điều cần theo dõi | Lý do |
```

---

## Nguyên tắc chung cho cả hai

- Không tự thêm số liệu ngoài claim đã validate của specialist.
- Mọi recommendation truy được về claim có nguồn; không có claim → không có recommendation.
- Đối thủ chưa có data: dùng ❓/[Chưa xác minh], không suy diễn thành fact.
