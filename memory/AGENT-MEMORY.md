# Conversation Memory — AgentBase Memory Service

Cấu hình Memory Service cho Q&A. **Không commit secret thực** — resource ID dưới đây là
non-sensitive.

Phân biệt hai loại memory:

| Loại | Lưu ở | Dùng cho |
|---|---|---|
| **Workspace knowledge** | `memory/` (folder này) | tri thức validate, `tools/memory_tool.py` nạp làm context |
| **Conversation memory** | AgentBase Memory Service | fact per-user từ lịch sử Q&A, semantic search |

## Luồng Q&A có conversation memory

```
Telegram / POST /tasks/qa  (actor_id, session_id)
        ▼
QAAgent
  ├─ memory_tool.load_memory()          → workspace knowledge
  ├─ memory_service.get_user_context()  → semantic search fact của actor
  ├─ router.complete(workload=qa)       → Gemma/Qwen (fallback chéo)
  └─ memory_service.save_exchange()     → lưu Q&A; platform auto-extract fact (async)
```

`actor_id` = Telegram user_id; `session_id = "tg-{chat_id}-{YYYY-MM-DD}"` (session theo
ngày). Bot 1 user cố định: `actor_id = chat_id`.

## Platform resources

| Resource | Name | ID | Dùng cho |
|---|---|---|---|
| Memory Store (production) | `vks-intel-prod-memory` | `memory-c3af4781-4ef6-4065-be45-a42d2b5dc3f4` | **Production runtime** |
| Memory Store (prototype cũ) | `vks-intel-memory` | `memory-b5055a2d-4620-488d-a52b-7aa0b899968b` | Prototype — không dùng cho production |

**Production strategies** (vks-intel-prod-memory):
- `conversation-facts` (SEMANTIC): `ltms-bec4bd01-f45e-42f3-ac65-5e7917f0ddc6` — auto-generate, 90 ngày
- `user-interests` (CUSTOM): `ltms-a18c8ec2-7bdf-4a5a-92fb-4fdfc9ce6979` — extract competitor/pricing interests

## Env vars (AgentBase Runtime — production)

```env
MEMORY_ID=memory-c3af4781-4ef6-4065-be45-a42d2b5dc3f4
MEMORY_STRATEGY_SEMANTIC_ID=ltms-bec4bd01-f45e-42f3-ac65-5e7917f0ddc6
MEMORY_STRATEGY_CUSTOM_ID=ltms-a18c8ec2-7bdf-4a5a-92fb-4fdfc9ce6979
```

`GREENNODE_CLIENT_ID` / `GREENNODE_CLIENT_SECRET` được platform tự inject — không set thủ công.

## Retrieval

Semantic search (vector similarity): query = câu hỏi hiện tại; `scoreThreshold=0.5`;
`limit=5`/strategy (≤10 fact vào prompt). Record generate async sau khi lưu event — có
thể delay vài giây.

## Troubleshooting

| Triệu chứng | Nguyên nhân | Fix |
|---|---|---|
| Memory không hoạt động | `MEMORY_ID`/strategy IDs chưa set | Kiểm tra env vars runtime |
| Record rỗng sau Q&A | Auto-extract async chưa kịp | Đợi 5–10s |
| `GREENNODE credentials not available` | Chạy local không có credentials | Bình thường — memory disabled khi chạy local |
| 401 Unauthorized | IAM token hết hạn | Token tự refresh; nếu vẫn lỗi kiểm tra credentials |

## Quản lý qua portal

Memory console: https://aiplatform.console.vngcloud.vn/memory → `vks-intel-memory` → Browse.
Script tham khảo: `.claude/skills/agentbase/scripts/memory.sh`.
