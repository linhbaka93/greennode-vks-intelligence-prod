# memory/executive-briefs — Briefs đã gửi Leadership

Audit trail các executive brief đã gửi leadership: giữ lịch sử, track decision rationale,
reference cho follow-up, onboarding leadership mới.

## outputs/ vs memory/

| Thư mục | Mục đích |
|---|---|
| `outputs/executive-briefs/` | Brief mới generate, sắp gửi |
| `memory/executive-briefs/` | Brief đã gửi + đã được leadership đọc/quyết định |

Lifecycle: generate ở `outputs/` → gửi → copy sang `memory/` với status "đã gửi" →
cập nhật outcome khi có decision.

## Cấu trúc file

```
# <Tiêu đề>
**Date sent / Prepared for / Prepared by / Reading time / Status (Sent|Discussed|Decided)**
## Situation
## What's happening
## Why it matters to GreenNode
## Recommended action
## If we do nothing
---
## Outcome (cập nhật sau khi gửi)
**Decision date / Decision (Approved|Rejected|Deferred|Modified) / Follow-up / Notes**
```

Format brief: theo "Executive Brief" trong `prompts/_report_templates.md`.

## Naming

```
YYYY-MM-DD_<topic-slug>_brief.md
```

Ví dụ: `sovereign-ai-opportunity_brief.md`, `q2-strategic-priorities_brief.md`.

## Quy tắc

- ✅ Mọi brief gửi leadership phải copy vào đây; cập nhật outcome sau decision.
- ✅ Executive-readable (<3 phút), có recommended action cụ thể, không chỉ "FYI".
- ❌ Không xóa brief cũ (audit trail bắt buộc); draft chưa gửi để ở `outputs/`.

## Retention

Giữ tất cả. Volume lớn thì tổ chức theo năm: `2026/`, `2027/`...
