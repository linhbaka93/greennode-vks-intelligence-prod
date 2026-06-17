# GreenNode VKS Intelligence — AgentBase Production

Runtime multi-agent production cho competitive intelligence mảng Managed Kubernetes tại Việt Nam. Đây là một project độc lập, đọc và bảo trì như một codebase production tự chứa.

## Quy trình làm việc với Claude

**Plan trước, code sau.** Với mọi thay đổi có từ 2 files trở lên hoặc ảnh hưởng đến behavior hệ thống, Claude phải trình bày kế hoạch trước (files cần sửa, lý do, risk/trade-off) và đợi xác nhận trước khi implement. Không tự ý implement mà không có plan đã được duyệt.

## Git & Code Push Policy (bắt buộc)

### Identity — CHỈ dùng tài khoản này cho project

```
user.name  = linhbaka93
user.email = linhbaka93@gmail.com
remote     = https://github.com/linhbaka93/greennode-vks-intelligence-prod.git
```

Claude **phải verify** `git config user.name` và `git config user.email` đúng trước MỌI lần commit.
Nếu sai → chạy hai lệnh sau trước khi commit:
```powershell
git config user.name "linhbaka93"
git config user.email "linhbaka93@gmail.com"
```

### Checklist bắt buộc trước mỗi commit & push

1. `uv run ruff check src tests` — phải sạch (0 errors)
2. `uv run pytest tests/ -q` — phải xanh (0 failures)
3. Scan staging: không có `.env`, `*-credentials.json`, `.greennode.json`, `docs/`
4. Verify `git config user.name` = `linhbaka93` và `user.email` = `linhbaka93@gmail.com`
5. Commit message tuân thủ format bên dưới

### Commit message rules

- Tiếng Anh, imperative mood: `Add ...`, `Fix ...`, `Update ...`
- Ngắn, generic — **không nhắc** tên client, tên công ty, tên cá nhân
- Không dùng suffix `_v2`, `_new`, `_final` trong tên file hoặc nội dung commit
- Khi Claude viết code, thêm footer: `Co-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>`

### Không bao giờ commit các file sau

| File/pattern | Lý do |
|---|---|
| `.env`, `.env.*` (trừ `.env.example`) | Secrets runtime |
| `*-credentials.json`, `registry-credentials.json` | vCR / API credentials |
| `docs/ROADMAP.md`, `docs/deploy-workflow.md`, `docs/agent-redesign.md`, `docs/*-plan.md` | Planning/progress docs — giữ local-only |
| `outputs/runs/*/` | Runtime artifacts — ephemeral |
| `docker/.n8n/`, `docker/postgres-data/`, `docker/caddy-data/` | Data volumes |

## Nguyên tắc bất biến

1. **Vietnamese-first cho output người dùng.** Báo cáo, Telegram Q&A, alert, approval message mặc định tiếng Việt. Tên module, schema, API path, biến code giữ tiếng Anh.
2. **Code sạch, không provenance.** Không viết comment kiểu "lấy từ bản cũ" / "wrap file X". Lịch sử kế thừa nằm trong `BUILD.md`, không nằm trong source.
3. **Comment chỉ khi cần.** Docstring mô tả trách nhiệm/contract của module-class-function để dev hiểu. Không chú thích tường thuật, không TODO mồ côi.
4. **Mọi model call là dependency mạng không tin cậy.** Luôn có timeout, retry có chọn lọc, fallback, và JSON guard.
5. **Không publish im lặng.** Output phải qua quality gate. Điểm thấp → `needs_review`/`blocked`, không tự gửi.
6. **Mọi run sinh artifact.** Lưu dưới `outputs/runs/<run_id>/` để audit.

## Runtime đang chạy (2026-06-17)

```
Endpoint : https://endpoint-c55e9dec-fbc3-4621-a921-d31c349c3002.agentbase-runtime.aiplatform.vngcloud.vn
Image    : vcr.vngcloud.vn/98510-greennode-vks-intelligence/vks-intelligence:v20260617112511
Status   : ACTIVE — /health trả ok, Telegram token + chat_id đã set
```

**Deploy:** `.\scripts\deploy.ps1` (tests → build → push → PATCH runtime → poll → health).
**Debug:** `.\scripts\runtime-status.ps1` | **vCR login fail:** `.\scripts\refresh-vcr-credentials.ps1`

## Phân tầng

```
n8n / Docker        control plane: schedule, retry, approval, notification
AgentBase (Python)  runtime multi-agent: supervisor + specialist + router
Model pool          Gemma / Qwen (OpenAI-compatible) + Claude (fallback/premium)
GitHub repo         versioned memory + audit trail
Telegram            delivery, Q&A, approval
```

n8n không chứa reasoning. Reasoning nằm trong Python/AgentBase.

## Quy trình deploy (Windows PowerShell)

```powershell
# Full deploy (khuyến nghị)
.\scripts\deploy.ps1

# Không chạy tests
.\scripts\deploy.ps1 -SkipTests

# Chỉ xem status
.\scripts\runtime-status.ps1

# Login vCR fail → refresh secret
.\scripts\refresh-vcr-credentials.ps1
```

**Lưu ý bắt buộc:**
- `docker build` phải có `--platform linux/amd64`
- `docker login` dùng `-p` flag, phải `docker logout` trước (credential cache issue trên Windows)
- Deploy script tự merge env vars từ runtime hiện tại + `.env` → không mất TELEGRAM_* khi redeploy
- Nếu runtime ERROR sau deploy do service account mới: `PATCH .../reset-service-account` rồi deploy lại
- Bash scripts trong `.claude/skills/agentbase/scripts/` không chạy được trên Windows PS (BOM encoding)

## Build plan & tiến độ

**Đọc [`docs/ROADMAP.md`](docs/ROADMAP.md) TRƯỚC ở mỗi session** — master plan, phase status, dashboard plan, và progress log (mỗi session ghi lại đã làm gì để session sau tiếp tục). Cuối session phải thêm entry vào progress log.

## Kiến trúc hệ thống

Xem **[`docs/ARCHITECTURE.md`](docs/ARCHITECTURE.md)** để có bản đồ đầy đủ:
- Layer map (9 tầng từ entry point → delivery)
- Supervisor pipeline + `_PLAN_MAP` per task type
- Agent registry + prompt file mapping
- Evidence collection flow + scrape allowlist
- LLM router + provider + budget per task type
- Synthesis template + quality gate thresholds
- Data contracts (TaskRequest → AgentResult → RunMetadata)
- Gaps đã biết + plan

**[`docs/agent-redesign.md`](docs/agent-redesign.md)** — plan nâng cấp 5 phase dựa trên Anthropic cookbook patterns (orchestration động, evaluation loop, tool scoping, prompt versioning, user preference). Model-agnostic, áp dụng được với Qwen/Gemma.

## Cấu trúc

src-layout, một package duy nhất `vks_intelligence`.

```
src/vks_intelligence/
  __main__.py          entrypoint: python -m vks_intelligence
  platform.py          AgentBase app: /health, /invocations
  api.py               FastAPI: /tasks/*, /quality/*, /dashboard/*
  schemas.py           request/response schema cho API
  config.py            settings nạp từ env (budget, model, timeout, flags)
  contracts.py         schema nội bộ: TaskRequest, AgentResult, MemoryPatch...
  run_context.py       state + budget cho một run
  task_store.py        ghi/đọc artifact outputs/runs/*
  supervisor.py        phân loại task, lập plan, chọn agent, synthesis
  registry.py          đăng ký specialist theo tên
  task_runner.py       chạy agent theo budget/timeout
  synthesis.py         gộp AgentResult thành output cuối
  quality.py           deterministic quality gate
  dashboard.py         tổng hợp observability từ artifact store
  llm/                 base, openai_compatible, anthropic_provider, router,
                       budgets, retries, json_guard
  specialists/         qa, market_trend, competitor, pricing, regulatory,
                       positioning, battlecard, memory_curator, quality_critic
  tools/               memory, news, source, telegram, github, output
  evals/               eval cases + quality_rubric
  static/              dashboard.html
prompts/               system prompt tiếng Việt cho từng agent
memory/                knowledge base (versioned)
outputs/runs/          artifact mỗi run
docker/                control plane n8n + Postgres + Caddy
n8n/                   workflow export
tests/                 smoke test
docs/                  plan, kiến trúc
```

## Template output báo cáo (8 phần)

`TL;DR → Key Findings → Detailed Analysis → Comparison Table → Strategic Implications → Recommendations → Next Actions → Sources`

## Nhãn claim bắt buộc

- `[Workspace]` thông tin từ memory đã validate
- `[Suy luận]` kết luận logic, ghi rõ cơ sở
- `[Chưa xác minh]` thông tin chưa có trong workspace
