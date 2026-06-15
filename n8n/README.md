# n8n/ — Production workflow (DEPRECATED — đã park 2026-06-12)

> **⚠️ DEPRECATED:** Control plane n8n đã được thay bằng **scheduler nội bộ trong
> runtime** (`src/vks_intelligence/scheduler.py`, cron 15:00 ICT) + **GitHub Actions
> backup** (`.github/workflows/scheduled-reports.yml`, 15:30 ICT). Lý do: không có
> host docker chạy 24/7 nên các workflow ở đây chưa bao giờ được activate
> (`"active": false` toàn bộ), và AgentBase runtime không host được n8n (contract
> `/invocations`, không persistent volume). Telegram Q&A không cần n8n — webhook
> trỏ thẳng `/telegram/webhook` của runtime.
> Giữ thư mục này làm tham khảo nếu sau này có host 24/7; nếu dùng lại, lưu ý
> cron trong JSON viết theo UTC nhưng `GENERIC_TIMEZONE=Asia/Ho_Chi_Minh` →
> phải đổi cron sang giờ ICT trước khi activate.

Workflow được build trực tiếp trên UI n8n rồi export JSON về thư mục này để version.
n8n chỉ điều phối; mọi reasoning nằm trong AgentBase. Mỗi node HTTP gọi tới
`AGENTBASE_BASE_URL` + path dưới đây.

## Hợp đồng endpoint

| Endpoint | Method | Body chính | Trả về |
|---|---|---|---|
| `/health` | GET | — | status + model đang bật |
| `/tasks/qa` | POST | `{question, actor_id, session_id}` | `{answer, confidence, escalated}` |
| `/tasks/daily-intelligence` | POST | `DailyIntelligenceRequestBody` | `TaskResponse` |
| `/tasks/weekly-digest` | POST | `TaskRequestBody` (`dry_run` được) | `TaskResponse` |
| `/tasks/monthly-brief` | POST | `TaskRequestBody` + human approval mặc định | `TaskResponse` |
| `/tasks/competitor-monitor` | POST | `TaskRequestBody` | `TaskResponse` |
| `/tasks/pricing-analysis` | POST | `TaskRequestBody` | `TaskResponse` |
| `/tasks/battlecard` | POST | `TaskRequestBody` + `payload.competitor` | `TaskResponse` |
| `/tasks/memory-maintenance` | POST | `TaskRequestBody` | `TaskResponse` |
| `/tasks/{task_id}` | GET | — | `TaskResponse` |
| `/quality/check` | POST | `{content}` | verdict + score |
| `/dashboard/summary` | GET | — | chỉ số tổng |

`TaskResponse` gồm: `status`, `quality_passed`, `quality_score`, `artifact_path`,
`telegram_preview`, `requires_approval`, `fallbacks_used`, `warnings`.

## Workflow cần build

### weekly-digest-production
```
Cron thứ 6 09:00 ICT
-> POST /tasks/weekly-digest   (workflow timeout > task timeout + 60s)
-> nếu quality_passed=false: báo owner, dừng
-> gửi telegram_preview cho approver
-> chờ approval (webhook/button)
-> nếu approved: publish message cuối lên Telegram
-> lưu/commit metadata, báo thành công
```

### daily-competitor-monitor
```
Cron hằng ngày
-> POST /tasks/competitor-monitor
-> timeout: retry 1 lần, rồi báo owner
-> không có thay đổi đáng kể: lưu run, không thông báo
-> severity medium/high: gửi Telegram alert
```

### monthly-executive-brief
```
Cron thứ 6 cuối tháng -> POST /tasks/monthly-brief -> bắt buộc human approval -> publish -> lưu artifact
```

### qa-escalation
```
Telegram message -> POST /tasks/qa
-> confidence cao: trả lời ngay
-> escalated=true: tạo research task, báo owner, lưu câu hỏi chưa trả lời được
```

### battlecard-automation
```
Trigger (manual/cron/Telegram) -> POST /tasks/battlecard {payload:{competitor}}
-> quality gate -> nếu pass: lưu memory/battlecards + outputs/battlecards
-> gửi battlecard cho sales channel
```

### memory-maintenance
```
Cron tuần/tháng -> POST /tasks/memory-maintenance
-> patch auto-applied (confidence cao + quality đạt ngưỡng): commit
-> patch còn lại: gửi preview cho approver -> commit khi approved
```

## Quy tắc timeout

n8n workflow timeout > AgentBase task timeout (≥ 60s). Đặt retry ở tầng n8n cho lỗi
mạng; không retry khi `quality_passed=false`.

---

## Workflow JSON — Import Guide

6 file JSON hiện có trong thư mục này có thể import trực tiếp vào n8n:

| File | Mô tả | Trigger | Cron (UTC) |
|---|---|---|---|
| `daily-intelligence-production.json` | Daily brief Mon–Fri | Cron | `0 0 * * 1-5` (07:00 ICT) |
| `weekly-digest-production.json` | Weekly digest + approval | Cron | `0 2 * * 5` (09:00 ICT Fri) |
| `daily-competitor-monitor.json` | Competitor monitor silent | Cron | `0 23 * * *` (06:00 ICT) |
| `qa-telegram.json` | Q&A bot Telegram | Telegram Trigger | — |
| `battlecard-automation.json` | Battlecard on-demand | Webhook POST | — |
| `memory-maintenance.json` | Memory patch weekly | Cron | `0 3 * * 0` (10:00 ICT Sun) |

Workflow JSON riêng cho `monthly-executive-brief` và `pricing-analysis` chưa có trong
checkpoint này. API endpoint đã sẵn sàng; có thể tạo thêm workflow bằng cùng pattern
HTTP Request → quality/approval → Telegram publish.

### Cách import

1. Mở n8n UI → **Workflows** → **Import from File**.
2. Chọn file `.json` → Import.
3. Cấu hình credentials (Telegram) và environment variables.
4. Set **active = true** khi sẵn sàng production.

### Environment variables cần set trong n8n

| Biến | Giá trị |
|---|---|
| `AGENTBASE_BASE_URL` | URL AgentBase, vd `http://localhost:8080` hoặc URL production |
| `TELEGRAM_CHAT_ID` | Chat ID channel/group nhận báo cáo công khai |
| `TELEGRAM_OWNER_CHAT_ID` | Chat ID owner/approver nhận alert + approval request |

### Credentials cần tạo trong n8n

- **Telegram API**: tạo mới với `Bot Token` từ `.env` → dùng cho tất cả Telegram nodes.
- Không cần credential riêng cho HTTP Request (AgentBase nếu internal network).

### Lưu ý về approval flow

`weekly-digest-production.json` dùng **Wait node 24h** — owner nhận Telegram preview,
review `artifact_path/final.md`, rồi **resume workflow thủ công** qua n8n UI
(Executions → Resume). Sau này có thể nâng cấp thành inline keyboard button.

`battlecard-automation.json` dùng **Webhook trigger** — gọi từ Telegram bot hoặc tool
nội bộ với body `{"competitor": "aws-eks"}` để trigger on-demand.
