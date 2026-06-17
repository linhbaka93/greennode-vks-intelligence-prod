# GreenNode VKS Intelligence — Kiến trúc hệ thống

> Tài liệu mô tả cấu trúc tầng, luồng dữ liệu, và liên kết giữa các module.
> Cập nhật: 2026-06-17. Source of truth: code; doc này là bản đồ tra cứu.

---

## 1. Tổng quan tầng (Layer Map)

```
┌─────────────────────────────────────────────────────────────────┐
│  TẦNG 0 — Control Plane (ngoài Python runtime)                  │
│  n8n cron → POST /tasks/*   │   Telegram Bot → POST /webhook    │
└────────────────────┬────────────────────────┬───────────────────┘
                     │                        │
┌────────────────────▼────────────────────────▼───────────────────┐
│  TẦNG 1 — HTTP Entry Points                                     │
│  api.py: /tasks/*, /telegram/webhook, /health, /dashboard/*     │
│  platform.py: /health, /invocations (AgentBase lifecycle)       │
└────────────────────────────┬────────────────────────────────────┘
                             │
┌────────────────────────────▼────────────────────────────────────┐
│  TẦNG 2 — Intent Routing (api.py)                               │
│  classify_intent()  →  MEMORY_LOOKUP | CURRENT_RESEARCH         │
│  _force_refresh_question()  →  bypass cache                     │
│  _research_task_for_question()  →  TaskType                     │
│  _is_affirmative() + _PENDING_RESEARCH  →  context reroute      │
└──────────┬────────────────────────────────┬─────────────────────┘
           │ MEMORY_LOOKUP                  │ CURRENT_RESEARCH
           │                               │
┌──────────▼───────────┐      ┌────────────▼────────────────────┐
│  TẦNG 3a — Streaming │      │  TẦNG 3b — Supervisor Pipeline  │
│  QAAgent.stream_     │      │  supervisor.py: Supervisor.run() │
│  answer_text()       │      │  task_runner.py: run_agents()    │
│  → Telegram edits    │      │  → background thread            │
└──────────────────────┘      └────────────┬────────────────────┘
                                           │
┌──────────────────────────────────────────▼────────────────────┐
│  TẦNG 4 — Evidence Collection  (supervisor._collect_evidence)  │
│  evidence_tool.py: collect()                                   │
│  ├── memory_tool.py: load_memory()        [Workspace]          │
│  ├── news_tool.py: fetch_fresh_news()     [RSS]                │
│  └── source_tool.py: fetch_source()       [Scrape/Social]      │
└──────────────────────────────┬────────────────────────────────┘
                               │ EvidenceBundle
┌──────────────────────────────▼────────────────────────────────┐
│  TẦNG 5 — Specialist Agents  (specialists/)                    │
│  Chạy song song qua ThreadPoolExecutor, giới hạn bởi RunContext│
│  Base: Specialist.run() → load_prompt() → router.complete()    │
│  → parse_into(AgentResult)                                      │
└──────────────────────────────┬────────────────────────────────┘
                               │ list[AgentResult]
┌──────────────────────────────▼────────────────────────────────┐
│  TẦNG 6 — LLM Layer  (llm/)                                    │
│  router.py: ModelRouter.complete() / stream_complete()         │
│  ├── anthropic_provider.py: Claude via Anthropic SDK           │
│  ├── openai_compatible.py: Gemma/Qwen via VNG AI Platform      │
│  ├── retries.py: with_retry() — chỉ retry lỗi tạm thời        │
│  ├── json_guard.py: parse_into() — repair JSON + validate      │
│  └── budgets.py: WorkloadBudget per TaskType                   │
└──────────────────────────────┬────────────────────────────────┘
                               │ LLMResponse
┌──────────────────────────────▼────────────────────────────────┐
│  TẦNG 7 — Synthesis & Quality Gate                             │
│  synthesis.py: synthesize(task_type, results) → markdown       │
│  quality.py: validate_output(content) → QualityResult          │
│  → verdict: pass | needs_review | revise | blocked             │
└──────────────────────────────┬────────────────────────────────┘
                               │ synthesis.md + QualityResult
┌──────────────────────────────▼────────────────────────────────┐
│  TẦNG 8 — Persistence                                          │
│  task_store.py: outputs/runs/<run_id>/                         │
│  agentbase_memory_tool.py: AgentBase Memory Service (per-user) │
└──────────────────────────────┬────────────────────────────────┘
                               │
┌──────────────────────────────▼────────────────────────────────┐
│  TẦNG 9 — Delivery                                             │
│  telegram_tool.py: send_message / edit_message / stream_and_   │
│  edit_message → Telegram Bot API                               │
└───────────────────────────────────────────────────────────────┘
```

---

## 2. Entry Points — `api.py` + `platform.py`

### `api.py` — FastAPI surface

| Endpoint | Handler | Mô tả |
|---|---|---|
| `POST /tasks/qa` | `task_qa()` | Q&A từ memory + AgentBase memory; có current_research path |
| `POST /tasks/daily-intelligence` | `task_daily_intelligence()` | Daily brief |
| `POST /tasks/weekly-digest` | `task_weekly_digest()` | Weekly digest |
| `POST /tasks/competitor-monitor` | `task_competitor_monitor()` | Competitor analysis |
| `POST /tasks/pricing-analysis` | `task_pricing_analysis()` | Pricing/TCO |
| `POST /tasks/battlecard` | `task_battlecard()` | Battlecard generation |
| `POST /tasks/memory-maintenance` | `task_memory_maintenance()` | Memory curator |
| `POST /telegram/webhook` | `telegram_webhook()` | Telegram bot handler |
| `POST /telegram/set-webhook` | `telegram_set_webhook()` | Register Telegram webhook |
| `GET /tasks/{task_id}` | `get_task_status()` | Task status check |
| `GET /dashboard/summary` | — | Observability |
| `GET /dashboard/runs` | — | Run list |
| `GET /dashboard/cost-trend` | — | Token usage theo ngày |
| `GET /dashboard/qa-activity` | — | QA activity từ Telegram |
| `GET /dashboard/evaluation` | — | Evaluation loop stats (revise rate, citation warnings) |
| `GET /dashboard/ui/` | — | Static HTML dashboard |
| `GET /health` | — | Liveness probe |

### `platform.py` — AgentBase lifecycle

- `POST /health` → liveness probe, trả `{"status": "ok", "build_tag": ...}`
- `POST /invocations` → route sang `api.py` handlers theo `task_type` trong body

---

## 3. Intent Routing — `api.py` (Tầng 2)

### Flow `telegram_webhook`

```
message nhận về
  │
  ├─ _GREETINGS → greeting reply (không qua pipeline)
  ├─ _HELP_CMDS → help message
  │
  ├─ [Phase 2] save_event() → AgentBase memory
  ├─ [Phase 2] _is_affirmative() + _PENDING_RESEARCH → reroute text nếu user xác nhận research
  ├─ [Phase 2] search_user_memory() → _session_history cho context
  │
  ├─ classify_intent(text)
  │     ├─ CURRENT_RESEARCH → _force_refresh_question()? → cache check → live research (background thread)
  │     └─ MEMORY_LOOKUP   → stream_answer_text() → stream_and_edit_message() → Telegram
  │
  └─ [sau streaming] save_event(assistant) + generate_records() + _contains_research_offer() → _PENDING_RESEARCH
```

### Hàm routing quan trọng

| Hàm | File | Mục đích |
|---|---|---|
| `classify_intent(text)` | `specialists/qa_agent.py` | Keyword matching → MEMORY_LOOKUP / CURRENT_RESEARCH |
| `_force_refresh_question(q)` | `api.py` | Bypass cache khi user dùng explicit refresh intent |
| `_research_task_for_question(q)` | `api.py` | Keyword → TaskType (battlecard / competitor / pricing / weekly / daily) |
| `_is_affirmative(text)` | `api.py` | Detect "có/ok/yes" xác nhận research |
| `_contains_research_offer(text)` | `api.py` | Detect khi bot đề xuất mở research → lưu pending |

**Gap hiện tại:** `_research_task_for_question()` dùng keyword matching → brittle. Plan: thay bằng LLM classify (Hướng 1).

---

## 4. Supervisor Pipeline — `supervisor.py`

### `_PLAN_MAP` — agent assignment per task type

| TaskType | Agents (critical=True*) | Evidence fetch | Budget |
|---|---|---|---|
| `QA` | qa_agent* | ❌ | 1 agent / 30s |
| `DAILY_INTELLIGENCE` | daily_intelligence_agent*, competitor_agent | ✅ 1 ngày | 3 agents / 180s |
| `WEEKLY_DIGEST` | market_trend_agent*, competitor_agent*, pricing_agent, regulatory_agent, positioning_agent | ✅ 7 ngày | 5 agents / 480s |
| `MONTHLY_BRIEF` | market_trend_agent*, competitor_agent*, pricing_agent, regulatory_agent, positioning_agent | ✅ 30 ngày | 6 agents / 720s |
| `COMPETITOR_MONITOR` | competitor_agent*, pricing_agent | ✅ 3 ngày | 4 agents / 300s |
| `PRICING_ANALYSIS` | pricing_agent*, competitor_agent | ✅ 14 ngày | 3 agents / 300s |
| `BATTLECARD` | competitor_agent*, pricing_agent, battlecard_agent* | ❌ | 3 agents / 300s |
| `MEMORY_MAINTENANCE` | memory_curator_agent*, quality_critic_agent | ❌ | 3 agents / 360s |

**Gap hiện tại:**
- `BATTLECARD` không collect fresh evidence → chạy hoàn toàn từ workspace memory
- `regulatory_agent` chỉ có trong WEEKLY/MONTHLY → không được gọi khi user hỏi ad-hoc về pháp lý
- Cần thêm `regulatory_agent` vào `COMPETITOR_MONITOR` + `BATTLECARD`, và thêm `BATTLECARD` vào `needs_fresh`

### Vòng đời run trong `Supervisor.run()`

```
TaskRequest
  → _collect_evidence()       # RSS + scrape theo task type
  → build_plan()              # _PLAN_MAP → list[AgentTask]
  → run_agents()              # parallel ThreadPoolExecutor
  → synthesize()              # list[AgentResult] → markdown
  → validate_output()         # deterministic quality gate
  → citation_grader (enabled) # HEAD-check URLs → 4xx = dead; network err = benefit of doubt
  → revise loop (REVISE)      # max 1 attempt; inject failures as revise_hint → re-synthesize → re-validate
  → _decide_publish()         # pass/needs_review/blocked
  → TaskStore.save_*()        # artifact audit trail
  → RunMetadata               # trả về caller
```

---

## 5. Evidence Collection — `evidence_tool.py` + sources

### Luồng `collect()` trong supervisor

```
_collect_evidence(request, workspace_path)
  │
  ├─ needs_fresh check (DAILY/WEEKLY/MONTHLY/COMPETITOR/PRICING)
  │
  ├─ days window theo task type (1/7/30/3/14 ngày)
  │
  ├─ scrape_targets theo task type:
  │   DAILY_INTELLIGENCE  → social_scrape_targets("daily")
  │   WEEKLY_DIGEST       → social_scrape_targets("all")
  │   COMPETITOR_MONITOR  → ["viettel-idc","fpt-fke","bizfly-bke"] + social("all")
  │   PRICING_ANALYSIS    → ["aws-eks-pricing","gke-pricing"] + social("hyperscalers")
  │
  └─ evidence_tool.collect() → EvidenceBundle
       ├─ memory_tool.load_memory()     [Workspace] — phân tầng ưu tiên
       ├─ news_tool.fetch_fresh_news()  [RSS] — Google News + đối thủ VN
       └─ source_tool.fetch_source()    [Scrape/Social] — allowlist only
```

### `memory_tool.load_memory()` — thứ tự ưu tiên folder

```
greennode/ → competitors/ → pricing/ → regulatory/ → market-trends/
→ battlecards/ → feature-gaps/ → executive-briefs/
```

Trong mỗi folder: file `current-*` trước, sau đó sắp giảm dần theo ngày tên file.
Stale detection: tier1 (Viettel/FPT) >7 ngày, market-trends >90 ngày, GPU pricing >14 ngày.

### `source_tool.py` — scrape allowlist

| Key | URL | Category |
|---|---|---|
| `viettel-idc` | viettelidc.com.vn/viettel-kubernetes-service | Competitor K8s (VKS + vOKS) |
| `fpt-fke` | fptcloud.com/kubernetes | Competitor K8s |
| `bizfly-bke` | bizflycloud.vn/kubernetes | Competitor K8s |
| `aws-eks-pricing` | aws.amazon.com/eks/pricing | Pricing |
| `gke-pricing` | cloud.google.com/kubernetes-engine/pricing | Pricing |
| `*-linkedin`, `*-facebook`, `*-x` | Social pages | Social/Competitor |

---

## 6. Specialist Agents — `specialists/`

Tất cả agents kế thừa `Specialist` (base.py). Khi Supervisor init, `specialists/__init__.py` import toàn bộ → `@register` decorator tự đăng ký vào `registry.py`.

| Agent | File | Workload | Prompt | Vai trò |
|---|---|---|---|---|
| `qa_agent` | `qa_agent.py` | QA | `qa_agent.md` | Q&A từ memory; có `answer()`, `stream_answer_text()`, `classify_intent()` |
| `daily_intelligence_agent` | `daily_intelligence_agent.py` | RESEARCH | `daily_intelligence_agent.md` | Tổng hợp tín hiệu market 24-48h |
| `market_trend_agent` | `market_trend_agent.py` | RESEARCH | `market_trend_agent.md` | Kubernetes/AI infra market trends |
| `competitor_agent` | `competitor_agent.py` | RESEARCH | `competitor_agent.md` | Động thái Viettel/FPT/Bizfly/AWS |
| `pricing_agent` | `pricing_agent.py` | RESEARCH | `pricing_agent.md` | Pricing TCO/hidden cost |
| `regulatory_agent` | `regulatory_agent.py` | RESEARCH | `regulatory_agent.md` | BVDLCN 2025, Nghị định 356, compliance |
| `positioning_agent` | `positioning_agent.py` | SYNTHESIS | `positioning_agent.md` | GreenNode strengths/weaknesses |
| `battlecard_agent` | `battlecard_agent.py` | SYNTHESIS | `battlecard_agent.md` | Head-to-head battlecard |
| `memory_curator_agent` | `memory_curator_agent.py` | RESEARCH | `memory_curator_agent.md` | Detect stale/dup memory, đề xuất patch |
| `quality_critic_agent` | `quality_critic_agent.py` | CRITIC | `quality_critic_agent.md` | LLM-level hallucination check |

### `Specialist.run()` — vòng đời base

```
AgentTask, RunContext, ModelRouter
  → load_prompt()            # _output_policy.md + _social_sources.md + <agent>.md
  → load_memory()            # workspace memory làm context
  → LLMRequest(response_json=True)
  → router.complete(workload, req, context)
  → parse_into(response.text, AgentResult)  # json_guard
  → AgentResult
```

`QAAgent` override `run()` + có thêm `answer()` (sync) và `stream_answer_text()` (streaming).

---

## 7. LLM Layer — `llm/`

### `ModelRouter` — `router.py`

```
complete(workload, request, context)
  │
  ├─ model_for(workload, policy) → model id từ Settings
  │     QA → model_qa (Gemma 4-31B)
  │     RESEARCH → model_research (Qwen 2.5-72B)
  │     SYNTHESIS → model_synthesis (Gemma 4-31B)
  │     CRITIC → model_critic (Qwen 2.5-72B)
  │     PREMIUM → model_premium (Claude Sonnet 4.6)
  │
  ├─ _provider_for(model) → AnthropicProvider | OpenAICompatibleProvider
  │     "claude" in model → AnthropicProvider
  │     else → OpenAICompatibleProvider (VNG AI Platform)
  │
  ├─ with_retry(lambda: provider.complete(req), max_retries)
  │
  └─ fallback: primary fail → model_fallback → raise RuntimeError

stream_complete(workload, request)   # không có RunContext, không budget tracking
  → provider.stream_complete(req) → Iterator[str]
```

### Providers

| Provider | File | Backend | Stream |
|---|---|---|---|
| `AnthropicProvider` | `anthropic_provider.py` | Anthropic SDK | `client.messages.stream()` |
| `OpenAICompatibleProvider` | `openai_compatible.py` | OpenAI SDK → VNG AI Platform | `stream=True` |

### `retries.py` — retry policy

Chỉ retry lỗi tạm thời: `timeout`, `rate limit`, `429`, `503`, `connection`.
Không retry: prompt sai, JSON validation fail, quality blocked.

### `json_guard.py` — JSON repair pipeline

```
raw text → parse trực tiếp → extract JSON object lớn nhất → 1 lần repair prompt → schema validate
```
Không cho synthesis đọc JSON chưa validate.

### `budgets.py` — giới hạn per task type

| TaskType | max_agents | run_timeout | agent_timeout | max_input_tokens |
|---|---|---|---|---|
| QA | 1 | 30s | 20s | 20K |
| DAILY_INTELLIGENCE | 3 | 180s | 90s | 80K |
| WEEKLY_DIGEST | 5 | 480s | 120s | 160K |
| COMPETITOR_MONITOR | 4 | 300s | 90s | 120K |
| BATTLECARD | 3 | 300s | 120s | 120K |

---

## 8. Synthesis & Quality Gate

### `synthesis.py` — `synthesize(task_type, results) → markdown`

Template output theo task type:

| TaskType | Template function | Sections |
|---|---|---|
| `DAILY_INTELLIGENCE` | `_daily_intelligence()` | TL;DR / Tin xác nhận / Cần xác minh / Dự đoán / Action / Sources |
| `WEEKLY_DIGEST` | `_weekly_digest()` | TL;DR / Key Findings / Phân tích / Rủi ro / Action / Sources |
| `COMPETITOR_MONITOR` | `_competitor_monitor()` | Động thái đối thủ / Rủi ro / Action / Sources |
| `BATTLECARD` / `PRICING_ANALYSIS` | `_single_agent_report()` | TL;DR / Key Findings / Phân tích / Rủi ro / Action / Sources |

Chỉ dùng `AgentResult.claims` đã structured. Claim thiếu nguồn không được promote thành confirmed finding.

### `quality.py` — `validate_output(content) → QualityResult`

Chấm điểm deterministic, 4 verdict:

| Điểm | Verdict |
|---|---|
| ≥ 0.80 | `PASS` |
| ≥ 0.65 | `NEEDS_REVIEW` |
| ≥ 0.45 | `REVISE` |
| < 0.45 | `BLOCKED` |

Các deduction: output quá ngắn (-0.5), placeholder chưa fill (-0.3), thiếu section (-0.15), Search/Scrape claim thiếu URL/ngày (-0.25), pricing không có ngày (-0.2).

### Citation grader — `citation_grader.py`

Chạy sau `validate_output()`, trước `_decide_publish()`. HEAD-check các URL trong synthesis output.

- 4xx response → dead link (ghi vào `metadata.warnings` dạng `"Citation grader: N link chết"`)
- Network error / timeout → benefit of doubt (không penalize)
- 5s timeout/URL, max 4 workers concurrent
- Controlled by `config.citation_grader_enabled` (default: `True` từ v20260617)

Verdict `REVISE` (0.45–0.65) → supervisor inject `revise_hint` (danh sách failures) vào `synthesize()` call tiếp theo, re-validate. Tối đa 1 revise attempt; nếu vẫn thấp → `NEEDS_REVIEW`.

---

## 9. Persistence — Artifact + Memory

### `task_store.py` — `outputs/runs/<run_id>/`

Mỗi run ghi tăng dần:

```
outputs/runs/<timestamp>_<task_type>_<request_id>/
  request.json        # TaskRequest input
  plan.json           # TaskPlan + danh sách agent
  evidence.json       # EvidenceBundle
  <agent_name>.json   # AgentResult từng agent
  synthesis.md        # output tổng hợp
  quality.json        # QualityResult + score
  final.md            # output publish
  metadata.json       # RunMetadata (status, tokens, models, fallbacks)
  fallback_trace.json # nếu có model fallback
  errors.json         # nếu run fail
```

### `agentbase_memory_tool.py` — per-user conversation memory

Memory ID: `memory-c3af4781-4ef6-4065-be45-a42d2b5dc3f4`

| Method | Khi nào dùng | Mô tả |
|---|---|---|
| `save_event(actor, session, role, message)` | Mỗi turn hội thoại | Lưu user/assistant message |
| `search_user_memory(actor, query, limit)` | Trước khi generate | Semantic search facts của user |
| `generate_records(actor, session)` | Sau mỗi turn hoàn chỉnh | Trigger fact extraction → long-term memory |

`session_id` = `"tg-{chat_id}-{YYYY-MM-DD}"` — scope theo ngày.
`actor_id` = Telegram `user_id` hoặc `username` hoặc `chat_id`.

Auto-disabled nếu thiếu `GREENNODE_CLIENT_ID/SECRET` hoặc `MEMORY_ID`.

---

## 10. Delivery — `telegram_tool.py`

| Hàm | Mục đích |
|---|---|
| `send_message(token, chat_id, text, ...)` | Gửi message mới; retry 2 lần |
| `edit_message(token, chat_id, msg_id, text, ...)` | Edit message đã gửi in-place |
| `send_action(token, chat_id)` | Typing indicator |
| `stream_and_edit_message(token, chat_id, iter, ...)` | Streaming: gửi placeholder ⏳, edit mỗi 200 chars / 0.8s |
| `format_telegram_html_messages(markdown, max_chars)` | Convert markdown → Telegram HTML, split chunks |
| `markdown_to_telegram_html(markdown)` | Convert markdown subset → HTML tags |

Streaming flow:
```
placeholder_id = send_message("⏳")
for chunk in text_iter:
    accumulated += chunk
    if chars > 200 or time > 0.8s:
        edit_message(placeholder_id, accumulated)
return (accumulated, placeholder_id)
→ caller: edit_message(placeholder_id, html_formatted, parse_mode="HTML")
```

---

## 11. Data Contracts — `contracts.py`

### Luồng schema chính

```
TaskRequest → TaskPlan → AgentTask → AgentResult → QualityResult → RunMetadata
                                         │
                                     list[Claim]
                                         │
                                     EvidenceItem (trong EvidenceBundle)
```

### Enum quan trọng

| Enum | Values |
|---|---|
| `TaskType` | QA, DAILY_INTELLIGENCE, WEEKLY_DIGEST, MONTHLY_BRIEF, COMPETITOR_MONITOR, PRICING_ANALYSIS, BATTLECARD, MEMORY_MAINTENANCE |
| `AgentStatus` | OK, PARTIAL, FAILED |
| `QualityVerdict` | PASS, NEEDS_REVIEW, REVISE, BLOCKED |
| `EvidenceType` | MEMORY, RSS, SCRAPE, SOCIAL, SEARCH, MANUAL |
| `Confidence` | HIGH, MEDIUM, LOW |
| `ModelPolicy` | FAST, BALANCED, PREMIUM |

---

## 12. Config — `config.py`

Tất cả config nạp từ env qua `pydantic_settings.BaseSettings`. Singleton qua `@lru_cache`.

Key settings:

| Setting | Mô tả |
|---|---|
| `MODEL_QA/RESEARCH/SYNTHESIS/CRITIC/PREMIUM/FALLBACK` | Model routing |
| `AI_PLATFORM_BASE_URL/API_KEY` | VNG AI Platform endpoint |
| `ANTHROPIC_API_KEY` | Claude fallback |
| `TELEGRAM_BOT_TOKEN/CHAT_ID` | Bot delivery |
| `MEMORY_ID/STRATEGY_*_ID` | AgentBase memory |
| `MEMORY_AUTO_WRITE_ENABLED` | Auto-write memory patch (mặc định false) |
| `RUN_TIMEOUT_QA/WEEKLY/MONTHLY_SECONDS` | Task timeout |
| `QUALITY_MIN_SCORE_PUBLISH/APPROVAL` | Quality gate threshold |

---

## 13. Gaps đã biết & Plan

| Gap | Mô tả | Plan |
|---|---|---|
| **RC2+RC3** Routing brittle | `_research_task_for_question()` keyword → miss edge case | Thay bằng LLM classify (Hướng 1) |
| **BATTLECARD** không có fresh evidence | `needs_fresh` không include BATTLECARD → chạy từ memory cũ | Thêm BATTLECARD vào `needs_fresh` + scrape regulatory sources |
| **regulatory_agent** under-utilized | Chỉ trong WEEKLY/MONTHLY, không trigger khi user hỏi ad-hoc về pháp lý | Thêm `regulatory_agent` vào COMPETITOR_MONITOR + BATTLECARD plan |
| **Memory auto-write** tắt | `MEMORY_AUTO_WRITE_ENABLED=false` → memory files không tự cập nhật | Bật sau khi approval workflow ổn định |
| **No regulatory scrape sources** | `_SCRAPE_ALLOWLIST` không có thuvienphapluat.vn hay vanban.chinhphu.vn | Thêm nguồn pháp lý vào allowlist |
| **Search adapter** chưa bật | `include_search=False` default | Tích hợp paid search API sau khi budget approve |
