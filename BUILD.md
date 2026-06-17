# BUILD — Lộ trình dựng runtime multi-agent

Sổ tay build: trạng thái hiện tại của vỏ, thứ tự implement, và bản đồ tri thức kế
thừa. Mọi tham chiếu tới prototype chỉ tồn tại ở đây, không nằm trong source code.

Module path dưới đây tương đối với package `src/vks_intelligence/`.

## 0. Trạng thái hiện tại — Checkpoint 2026-06-17

Đang ở checkpoint **production hoàn chỉnh — deadline project**. Toàn bộ tính năng core đã
implement và deploy. Dashboard có 6 tab, citation grader bật, evaluation loop hoạt động,
Telegram bot streaming + research pipeline đầy đủ.

### Runtime info (cập nhật 2026-06-17)

- **Runtime ID:** `runtime-0e2018c3-4cd4-420a-a3aa-14c80b76183b`
- **Endpoint URL:** `https://endpoint-c55e9dec-fbc3-4621-a921-d31c349c3002.agentbase-runtime.aiplatform.vngcloud.vn`
- **Image hiện tại:** `vcr.vngcloud.vn/98510-greennode-vks-intelligence/vks-intelligence:v20260617104425`
- **vCR repo:** `98510-greennode-vks-intelligence` / robot: `98510-vks-intelligence-deploy` (uuid: `ra-1d54750b-9311-44c4-abba-67606ec2756b`)
- **Flavor:** `runtime-s2-general-2x4` (2 vCPU / 4 GB)
- **Scripts:** `scripts/deploy.ps1`, `scripts/runtime-status.ps1`, `scripts/refresh-vcr-credentials.ps1`

### Đã hoàn thành trong session 2026-06-17

| # | Tính năng | Files |
|---|---|---|
| M2b | Citation grader enabled (`citation_grader_enabled = True`) | `config.py` |
| D5 | Eval dashboard tab — revise rate, citation warnings, recent failures | `dashboard.py`, `schemas.py`, `api.py` |
| D4 | Auto-refresh toggle 30s + time-range selector 7/14/30d | `static/index.html` |
| UX | Pink color theme (#FCF8F8 → #F5AFAF) + markdown rendering (preview + chat) | `static/index.html` |
| DOC | Architecture docs promoted to committed: `ARCHITECTURE.md`, `ARCHITECTURE-VISUAL.html`, `SOURCES.md` | `docs/`, `.gitignore`, `docs/.gitignore` |
| DOC | `ARCHITECTURE.md` updated: 4 dashboard endpoints, citation grader, revise loop | `docs/ARCHITECTURE.md` |
| DOC | Architecture diagram nâng cấp 4-lane (1800×1180) | `assets/architecture.svg` |
| DOC | README: use case description tiếng Việt (Vấn đề / Người dùng / Giải pháp / Giá trị) | `README.md` |
| FIX | Brand naming: VNG Cloud → GreenNode throughout codebase + memory files | `README.md`, `memory/` |
| FIX | SWOT section trong product overview reframed từ competitor profile thành self-assessment | `memory/greennode/` |
| CLN | api.py: xóa dead code `if resp is not None: pass`, thêm module logger, bỏ narrative comments | `api.py` |

### Deploy workflow

```
uv run pytest tests/ -q
docker build --platform linux/amd64 -t <image>:<tag> .
docker logout vcr.vngcloud.vn && docker login vcr.vngcloud.vn -u <user> -p <pass>
docker push <image>:<tag>
PATCH /runtime/agent-runtimes/{id}  ← merge env vars từ runtime + .env
Poll ACTIVE → health check /health
```

Xem chi tiết: `docs/deploy-workflow.md`.

### Incidents đã gặp và fix (2026-06-03)

| Incident | Root cause | Fix |
|---|---|---|
| Runtime ERROR ngay sau deploy | imageUrl corrupt — tag chứa `docker pull vcr...` lặp lại | PATCH với imageUrl đúng |
| `docker login` unauthorized | Robot account secret stale + Docker credential cache cũ | Refresh secret qua `GET /v1/user/{uuid}/refresh` + `docker logout` trước login |
| Sau khi xóa IAM service account, version mới ERROR | Runtime service account bị broken khi parent SA xóa | `PATCH /agent-runtimes/{id}/reset-service-account` rồi redeploy |
| Deploy overwrite TELEGRAM_BOT_TOKEN | deploy.ps1 chỉ đọc `.env`, ghi đè mất key set thủ công trên runtime | Fetch current runtime env vars làm base, overlay với `.env` |

### Bash scripts encoding issue trên Windows

Scripts trong `.claude/skills/agentbase/scripts/` có BOM encoding, không chạy được từ
PowerShell. Workaround: dùng các PowerShell scripts trong `scripts/` hoặc gọi API trực tiếp
qua `Invoke-RestMethod`.

### Đã hoàn thành

- `contracts.py`, `schemas.py`, `llm/budgets.py` bao phủ các task chính:
  `qa`, `daily-intelligence`, `weekly-digest`, `monthly-brief`, `competitor-monitor`,
  `pricing-analysis`, `battlecard`, `memory-maintenance`.
- `supervisor.py` chạy lifecycle request → evidence → plan → agents → synthesis → quality →
  metadata, có artifact audit trong `outputs/runs/<run_id>/`.
- `specialists/` đã boot registry explicit cho 10 specialist agents; `daily_intelligence_agent`
  có prompt riêng.
- `specialists/base.py` load đúng `prompts/` của project và nối `_output_policy.md` vào system
  prompt cho mọi agent.
- `tools/evidence_tool.py` gom workspace/RSS/scrape/search optional thành `EvidenceBundle`,
  validate web evidence, dedupe URL/hash/title, ghi source counts/dedupe stats.
- `quality.py` đã tính `[Search]` và bắt lỗi `[Search]/[Scrape]` thiếu URL/ngày.
- `/tasks/*` đã có endpoint cho QA, daily, weekly, monthly, competitor, pricing, battlecard,
  memory maintenance; `/telegram/webhook` hỗ trợ Q&A và background current-research reply.
- `dashboard.summary()` đọc toàn bộ run đúng khi cần summary tổng.
- Test/lint checkpoint: `uv run ruff check src tests` sạch; `uv run pytest -q` xanh.

### Deploy checklist trước mỗi lần push

```
[ ] uv run pytest tests/ -q  → xanh
[ ] docker build --platform linux/amd64  (bắt buộc amd64)
[ ] registry-credentials.json còn valid? Nếu login fail → .\scripts\refresh-vcr-credentials.ps1
[ ] deploy.ps1 merge env từ runtime trước khi PATCH (giữ TELEGRAM_* và key secret khác)
[ ] Sau deploy: kiểm tra build_tag trong /health response khớp tag vừa push
[ ] Nếu runtime ERROR sau PATCH: check statusReason, thử reset-service-account nếu SA mới
```

### Còn phải harden trước production thật

1. **Auth/approval:** thêm API key/HMAC cho `/tasks/*`, Telegram secret token, approval button
   thay cho resume thủ công ở n8n.
2. **Async task queue:** thay background thread tạm bằng task queue/persistent worker hoặc
   AgentBase task async chính thức để không phụ thuộc lifecycle của web worker.
3. **Source registry:** mở rộng RSS/Atom allowlist, resolve Google News RSS về publisher URL khi
   có thể, thêm snapshot store cho scrape diff.
4. **Evidence artifact:** lưu raw source snapshots đầy đủ hơn, tách `evidence.json` và
   `source_snapshots/` khi scrape/search lớn.
5. **Eval coverage:** thêm eval Q&A/digest/battlecard/pricing theo fixture cố định và mock model.
6. **n8n workflows:** bổ sung JSON cho `monthly-executive-brief` và `pricing-analysis` nếu muốn
   chạy schedule riêng.

Cần trước khi chạy model thật: `AI_PLATFORM_API_KEY` + model id Gemma/Qwen thật,
`ANTHROPIC_API_KEY` nếu dùng Claude fallback, token/chat_id Telegram, AgentBase credentials.
Paid search API không bắt buộc cho milestone đầu.

## 0a. Quy chuẩn dự án (bắt buộc tuân thủ khi build tiếp)

1. **Vietnamese-first output, English code.** Output người dùng tiếng Việt; tên
   module/schema/API/biến tiếng Anh. Thuật ngữ kỹ thuật giữ tiếng Anh.
2. **Code sạch, độc lập — KHÔNG tham chiếu prototype cũ trong source/comment.** Mọi
   provenance/lịch sử kế thừa chỉ ở `BUILD.md`. Project đọc như một codebase tự chứa.
3. **Comment chỉ khi cần.** Docstring mô tả trách nhiệm/contract để dev hiểu. Không
   comment tường thuật, không TODO mồ côi, không chú thích "lấy từ X".
4. **Không tối giản agent spec.** Giữ chuẩn 11-section chi tiết; mỗi specialist có
   Output Contract JSON rõ ràng. Khi cải tiến từ tri thức cũ, tăng độ rõ contract/source/
   budget, không rút gọn domain rule đã hữu ích.
5. **Output phải theo `_output_policy.md` + `_report_templates.md`:** nhãn nguồn inline
   (`[Workspace]/[RSS]/[Scrape]/[Search]/[Suy luận]/[Chưa xác minh]`), mỗi finding có dòng
   so-what (Tác động GreenNode → GreenNode nên), trung thực data-gap (block ⚠️, không
   bịa), action item 4 trường (Priority|Action|Owner|Deadline), framing thời gian, no-hype.
6. **Mọi model call là dependency không tin cậy:** timeout + retry chọn lọc + fallback +
   JSON guard. Không publish im lặng — qua quality gate.
7. **Config-driven:** budget/timeout/model/freshness lấy từ `config.Settings`, không hardcode.
8. **Mọi run sinh artifact** dưới `outputs/runs/<run_id>/` để audit.
9. **Memory auto-write mặc định tắt;** chỉ bật sau khi approval workflow ổn định.
10. **Sau mỗi thay đổi code:** `uv run pytest -q` phải xanh; không để pydantic warning.

## 1. Thứ tự implement (ít rủi ro nhất)

| # | Module | Mục tiêu | Done khi |
|---:|---|---|---|
| 1 | `contracts.py` + `schemas.py` | Khoá schema dữ liệu nội bộ + current intelligence | Validate TaskRequest/AgentResult/QualityResult/MemoryPatch/EvidenceBundle và QA adaptive response |
| 2 | `llm/budgets.py` + `config.py` | Budget/config cho daily/current research | Có budget cho mọi TaskType; paid search disabled default |
| 3 | `tools/evidence_tool.py` | Gom memory/RSS/scrape/search optional thành EvidenceBundle | Dedupe URL/hash/title; drop/warn search/scrape thiếu URL/ngày |
| 4 | `tools/news_tool.py`, `source_tool.py` | Nguồn tin/scrape miễn phí | RSS/Atom + scraper snapshot có nguồn/ngày |
| 5 | `registry.py` + specialist registration | Registry không rỗng khi task_runner chạy | `available()` có agent names; `registry.get()` không fail với plan hợp lệ |
| 6 | `supervisor.py` | Run lifecycle deterministic | request→evidence→plan→agents→synthesis→quality→metadata |
| 7 | `specialists/qa_agent.py` | Q&A adaptive + confidence | Câu hỏi thường trả nhanh; câu hỏi latest route current research |
| 8 | `api.py` /tasks/qa | Endpoint Q&A | n8n gọi được; response có sources/artifact khi research_used |
| 9 | `specialists/daily_intelligence_agent.py` | Daily intelligence | Tạo daily brief/alert từ EvidenceBundle |
| 10 | `api.py` /tasks/daily-intelligence | Endpoint daily | Dry run sinh artifact và telegram_preview |
| 11 | `llm/openai_compatible.py` | Gọi Gemma/Qwen qua VNG AI Platform | Smoke test trả text + token usage |
| 12 | `llm/anthropic_provider.py` | Gọi Claude | Smoke test trả text |
| 13 | `llm/router.py` | Chọn provider theo policy + fallback | Đổi model bằng config, fallback có log |
| 14 | `llm/retries.py` + `json_guard.py` | Retry chọn lọc + repair JSON | JSON hỏng repair 1 lần rồi schema-validate |
| 15 | `specialists/{market_trend,competitor,pricing}_agent.py` | Worker weekly | Mỗi agent trả AgentResult hợp lệ từ EvidenceBundle |
| 16 | `synthesis.py` | Gộp claim → markdown | Sinh synthesis.md từ nhiều AgentResult |
| 17 | `quality.py` + `specialists/quality_critic_agent.py` | Gate + critic | Search/scrape claim thiếu URL/ngày bị block/review |
| 18 | `api.py` /tasks/weekly-digest (dry run) | Endpoint weekly | Dry run sinh đủ artifact |
| 19 | `tools/telegram_tool.py` | Format + split + send | Preview ≤ giới hạn ký tự |
| 20 | `dashboard.py` + /dashboard/* | Observability | UI đọc summary/runs từ artifact |
| 21 | `specialists/battlecard_agent.py` + /tasks/battlecard | Battlecard automation | Battlecard tự sinh → quality → proposed memory/output |
| 22 | `specialists/memory_curator_agent.py` + apply_patch auto | Memory governance | Patch confidence cao mới auto-eligible, còn lại chờ approval |
| 23 | `platform.py` + `__main__.py` | Harden entrypoint AgentBase | /health + /invocations chạy trên AgentBase |
| 24 | n8n workflow (trên web) | Control plane gọi AgentBase | Cron → task → approval → publish |

## 2. Bản đồ tri thức kế thừa

Logic dưới đây đã được prototype chứng minh khả thi. Khi implement, tái hiện
*behavior* (không copy nguyên trạng), bọc sau contract mới.

| Behavior đã chứng minh | Module đích | Ghi chú implement |
|---|---|---|
| Nạp memory phân tầng (VN Tier 1 trước, cắt theo context cap) | `tools/memory_tool.py` | Giữ thứ tự ưu tiên đối thủ, freshness threshold |
| Q&A từ memory + nhãn claim + giới hạn 250 từ | `specialists/qa_agent.py` | Thêm confidence + escalation flag |
| Quality gate deterministic (required section, placeholder, source count, pricing timestamp) | `quality.py` | Mở rộng 4 trạng thái pass/needs_review/revise/blocked |
| Telegram HTML format + split ≤ giới hạn ký tự | `tools/telegram_tool.py` | Thêm retry khi gửi |
| RSS news aggregator (Google News, query đối thủ VN) | `tools/news_tool.py` | Chuẩn hoá source, dedupe |
| Scrape pricing/feature đối thủ + diff snapshot | `tools/source_tool.py` | Giữ confidence |
| Evidence bundle trước khi agent suy luận | `tools/evidence_tool.py` | Chuẩn hóa `[Workspace]/[RSS]/[Scrape]/[Search]`, dedupe, cite URL/ngày |
| Pricing TCO/hidden cost reasoning | `specialists/pricing_agent.py` | Prompt: `prompts/pricing_agent.md` |
| Competitor profile + battlecard | `specialists/{competitor,battlecard}_agent.py` | Prompt tương ứng trong `prompts/` |
| Market trend monitoring + priority matrix | `specialists/market_trend_agent.py` | Prompt: `prompts/market_trend_agent.md` |
| Versioned memory + commit output | `tools/github_tool.py` | Audit trail |
| Entrypoint AgentBase /health + /invocations | `platform.py` | Bỏ scheduler local, schedule chuyển sang n8n |

## 3. Chỗ nên viết Python (gợi ý, chưa code)

- **`llm/openai_compatible.py`**: dùng `openai` SDK trỏ `base_url=AI_PLATFORM_BASE_URL`,
  gọi `chat.completions`, trích `usage` để ghi token.
- **`llm/router.py`**: bảng route theo `model_policy` (fast/balanced/premium) ánh xạ
  workload → env `MODEL_*`. Fallback 4 cấp: stricter prompt → khác model cùng provider
  → khác provider → degraded deterministic.
- **`llm/json_guard.py`**: parse trực tiếp → trích JSON object lớn nhất → 1 lần repair
  prompt → schema validate. Không cho synthesis đọc JSON chưa validate.
- **`tools/evidence_tool.py`**: nhận query/scope/days, gọi memory/news/source/search
  optional, chuẩn hóa EvidenceBundle, dedupe URL/hash/title, warning/drop nguồn thiếu
  URL/ngày, và không ghi memory.
- **`task_store.py`**: mỗi run một thư mục `outputs/runs/<run_id>/`, ghi tăng dần.
- **`supervisor.py`**: phân loại task → `TaskPlan` → chạy specialist song song trong
  budget → synthesis → quality → quyết định publish/approval. Huỷ agent quá hạn, sinh
  partial result nếu đủ evidence. Supervisor không scrape/gọi model/gửi Telegram trực tiếp.
- **`dashboard.py`**: chỉ đọc `metadata.json` các run; không gọi model.
- **`tools/memory_tool.py` auto-write**: `apply_patch(auto=True)` chỉ ghi khi
  `Settings.memory_auto_write_enabled` và patch đạt ngưỡng confidence + quality.

## 4. Knowledge base

`memory/` đã nạp sẵn (competitors, pricing, regulatory, greennode, market-trends).
`memory_tool.py` đọc trực tiếp; khi nối GitHub, dùng repo này làm nguồn versioned memory.

## 5. Quy ước artifact run

Xem `outputs/runs/README.md`.
