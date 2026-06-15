# memory/battlecards — Active Battlecards

Lưu battlecard đang active (đã field-test) cho Sales/Presales. `BattlecardAgent` sinh,
supervisor promote vào đây sau khi qua quality gate.

## memory/battlecards vs outputs/battlecards

| Thư mục | Mục đích |
|---|---|
| `memory/battlecards/` | Current version — đã field-test, đang dùng |
| `memory/battlecards/archive/` | Version cũ — giữ lịch sử evolution |
| `outputs/battlecards/` | Mới generate từ `/tasks/battlecard`, chưa field-test |

Lifecycle: generate → `outputs/battlecards/YYYY-MM-DD_...md` → field-test với Sales ~2
tuần → promote `memory/battlecards/<competitor>_<segment>_current.md` → version cũ sang
`archive/`.

## Naming

```
<competitor-slug>_<segment>_current.md
archive/<competitor-slug>_<segment>_vX.Y_YYYY-MM-DD.md
```

Segment chuẩn: `enterprise` · `sme` · `ai-startup` · `gov` · `migration`.
Ví dụ: `bizfly-bke_sme_current.md`, `aws-eks_ai-startup_current.md`.

## Quy tắc

- ✅ Chỉ battlecard đã field-test mới vào đây; mỗi competitor×segment 1 file `_current.md`.
- ✅ Version cũ phải archive, không xóa; bump version khi sửa.
- ❌ Không lưu draft/WIP ở đây — để ở `outputs/battlecards/`.

## Refresh trigger

| Trigger | Action |
|---|---|
| Pricing competitor đổi >10% | refresh trong 5 ngày |
| Competitor ra feature lớn | refresh trong 7 ngày |
| VKS ra feature mới | refresh differentiator trong 7 ngày |
| Định kỳ | review mỗi quý, full refresh mỗi 6 tháng |

## Retention

`_current.md` luôn giữ; `archive/` giữ 4 version gần nhất.

## Liên kết

- Agent: `prompts/battlecard_agent.md` (`BattlecardAgent`)
- Nguồn dữ liệu: `memory/competitors/`, `memory/pricing/` · Output mới: `outputs/battlecards/`
