# docker/ — Control plane (DEPRECATED — đã park 2026-06-12)

> **⚠️ DEPRECATED:** Stack này cần host docker 24/7 mà hiện không có. Scheduling đã
> chuyển vào runtime (`scheduler.py`) + GitHub Actions backup. Xem `../n8n/README.md`.

Stack control plane chỉ chứa n8n + Postgres (state cho n8n) + Caddy (reverse proxy,
TLS). Runtime multi-agent (Python) **không** nằm trong stack này — nó được deploy
lên AgentBase và n8n gọi tới qua `AGENTBASE_BASE_URL`. Tách hai nơi để không chạy
agent runtime ở hai chỗ cùng lúc.

## Chạy

```bash
cp .env.example .env   # điền secret
docker compose up -d
```

n8n: `https://$N8N_HOST` (sau Caddy). Workflow build trực tiếp trên UI n8n, gọi
HTTP tới AgentBase. Xem hợp đồng endpoint ở `../n8n/README.md`.

## Timeout

n8n workflow timeout phải lớn hơn AgentBase task timeout ít nhất 60s. AgentBase task
timeout lớn hơn supervisor timeout ít nhất 30s.
