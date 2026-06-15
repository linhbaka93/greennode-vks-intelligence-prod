# GreenNode VKS Intelligence — AgentBase Production

Runtime multi-agent production cho competitive intelligence mảng Managed Kubernetes
tại Việt Nam. Project độc lập, Vietnamese-first cho output người dùng, tiếng Anh cho
code/schema/API.

## Kiến trúc

```text
n8n / Docker        control plane: schedule, retry, approval, notification
AgentBase (Python)  runtime multi-agent: supervisor + specialist + model router
Model pool          Gemma / Qwen (OpenAI-compatible) + Claude (fallback/premium)
GitHub repo         versioned memory + audit trail
Telegram            delivery, Q&A, approval
```

n8n không chứa reasoning — reasoning nằm trong AgentBase.

## Bắt đầu

```bash
uv sync --extra dev          # tạo .venv từ uv.lock
cp .env.example .env         # điền API key + model id
uv run pytest -q             # smoke test vỏ
uv run python -m vks_intelligence
```

## Cấu trúc

Xem `CLAUDE.md` (quy ước repo) và `BUILD.md` (lộ trình implement + bản đồ tri thức).

```text
src/vks_intelligence/   package runtime (app, orchestration, llm, specialists, tools, evals)
prompts/                system prompt tiếng Việt cho từng agent
memory/                 knowledge base (versioned)
outputs/runs/           artifact mỗi run (audit trail)
docker/                 control plane n8n + Postgres + Caddy
n8n/                    workflow export + hợp đồng endpoint
docs/                   plan, kiến trúc
tests/                  smoke test
```

## API surface

```text
GET  /health
POST /tasks/qa
POST /tasks/daily-intelligence
POST /tasks/weekly-digest
POST /tasks/monthly-brief
POST /tasks/competitor-monitor
POST /tasks/pricing-analysis
POST /tasks/battlecard
POST /tasks/memory-maintenance
GET  /tasks/{task_id}
POST /quality/check
GET  /dashboard/summary | /dashboard/runs | /dashboard/ui
```

## Trạng thái

Đang ở checkpoint **runtime foundation đã chạy được**: FastAPI endpoints, supervisor,
specialist registry, model router, evidence bundle, artifact store, Telegram webhook,
dashboard summary và n8n workflow JSON nền đã có. Phần cần harden tiếp là async task
queue đầy đủ, auth/approval production, source registry mở rộng và eval coverage.

## Tài liệu

- [Kế hoạch xây dựng multi-agent production](docs/ke-hoach-xay-dung-multi-agent-production.md)
- [Production multi-agent AgentBase plan](docs/production-multi-agent-agentbase-plan.md)
- [Sơ đồ kiến trúc (SVG)](docs/production-multi-agent-architecture-sample.svg)
