# GreenNode VKS Intelligence — AgentBase Production

## Mô tả use case

**Vấn đề:** Đội ngũ sản phẩm và kinh doanh tại GreenNode cần theo dõi liên tục thị trường Managed Kubernetes Việt Nam — bao gồm pricing, tính năng mới, chiến lược GTM và động thái đối thủ (Viettel vOKS, FPT FKE, Bizfly BKE, CMC Cloud và các hyperscaler AWS/GCP/Azure). Việc thu thập thủ công từ nhiều nguồn mỗi ngày tốn hàng giờ, dễ bỏ sót tín hiệu quan trọng, và kết quả không nhất quán giữa các thành viên.

**Người dùng:** Product manager, business development và ban lãnh đạo kỹ thuật tại GreenNode — những người cần insight nhanh để ra quyết định về định giá, ưu tiên roadmap và định vị sản phẩm, nhưng không có thời gian tự research mỗi ngày.

**Giải pháp:** Hệ thống multi-agent tự động chạy trên VNG Cloud AgentBase. Mỗi ngày lúc 8 giờ sáng, Supervisor Core kích hoạt các specialist agent song song — `competitor_agent` theo dõi profile và tín hiệu đối thủ, `pricing_agent` phân tích cấu trúc giá và TCO, `regulatory_agent` cập nhật chính sách pháp lý, `market_trend_agent` theo dõi xu hướng AI/GPU trên cloud Việt Nam. Kết quả được tổng hợp, kiểm tra quality tự động (score ≥ 0.80), rồi gửi báo cáo về Telegram. Ngoài báo cáo định kỳ, người dùng có thể nhắn trực tiếp cho Lin Lin — QA agent — để hỏi bất kỳ câu hỏi nào về thị trường và nhận câu trả lời trong vài giây từ knowledge base, hoặc kích hoạt research mới nếu cần dữ liệu cập nhật.

**Giá trị mang lại:** Tiết kiệm 2–3 giờ research thủ công mỗi ngày. Không bỏ sót động thái cạnh tranh quan trọng. Mọi claim đều có nguồn và timestamp rõ ràng, có thể audit qua artifact store. Toàn bộ dữ liệu xử lý trong hạ tầng VNG Cloud, tuân thủ data sovereignty theo Luật BVDLCN 2025 — không có thông tin nào ra ngoài lãnh thổ Việt Nam.

---

## Sơ đồ kiến trúc

![System Architecture](assets/architecture.svg)

**Luồng chính:**
- **Người dùng** gửi câu hỏi qua Telegram hoặc REST API; **Scheduler** (APScheduler) trigger tự động 8h sáng / thứ 6 / mùng 1 hàng tháng
- **Orchestrator** (Gemma) phân loại `intent`: `memory_lookup` → Lin Lin Q&A trả lời nhanh; `current_research` → Supervisor pipeline
- **Supervisor Core** lập plan, dispatch specialist agents song song, collect evidence, synthesize, gọi Quality Gate
- **Quality Gate** kiểm score deterministic (≥ 0.80 publish; < 0.80 → revise 1 lần → `needs_review` alert)
- **Memory & Storage**: load workspace memory trước mỗi run; write-back kết quả mới dưới `outputs/runs/<run_id>/` và commit dated `.md` lên GitHub

**Model pool:** Gemma-4-31b-it (fast — QA, orchestrator, synthesis) · Qwen3-5-27b (reasoning — research, critic)

n8n không chứa reasoning — reasoning nằm trong AgentBase.

---

## Bắt đầu

```bash
uv sync --extra dev          # tạo .venv từ uv.lock
cp .env.example .env         # điền API key + model id
uv run pytest -q             # smoke test
uv run python -m vks_intelligence
```

## Cấu trúc

```text
src/vks_intelligence/   package runtime (app, orchestration, llm, specialists, tools, evals)
prompts/                system prompt tiếng Việt cho từng agent
memory/                 knowledge base (versioned)
outputs/runs/           artifact mỗi run (audit trail)
docker/                 control plane n8n + Postgres + Caddy
n8n/                    workflow export + hợp đồng endpoint
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
GET  /dashboard/summary | /dashboard/runs | /dashboard/evaluation | /dashboard/ui
```

## Trạng thái

Runtime ACTIVE — `v20260617`. Quality gate, revise loop, citation grader, Telegram bot, dashboard observability (overview, runs, QA, cost, eval tab) đã hoạt động production.

## Tài liệu

> Thư mục `docs/` là local-only (gitignored).

| File | Nội dung |
|---|---|
| `docs/architecture-visual.html` | Sơ đồ kiến trúc tương tác — 7-node flow diagram (mở bằng browser) |
| `docs/architecture.md` | Bản đồ đầy đủ: layer map, supervisor pipeline, agent registry, LLM router, data contracts |
| `CLAUDE.md` | Quy ước repo, deploy workflow, commit policy |
