# GreenNode VKS Intelligence — AgentBase Production Runtime
#
# Runtime contract:
#   GET  /health      → PingStatus.HEALTHY (AgentBase SDK or FastAPI)
#   POST /invocations → task routing handler
#   GET/POST /tasks/* → full production API surface
#   PORT 8080
#
# GPU: không cần — tất cả model call qua VNG AI Platform API (remote)
# Flavor khuyến nghị: 1 vCPU / 2 GB RAM

FROM python:3.13-slim

ARG APP_BUILD_IMAGE=""
ARG APP_BUILD_TAG=""
ARG APP_BUILD_SHA=""
ARG APP_BUILD_TIME=""

LABEL org.opencontainers.image.title="greennode-vks-intelligence" \
      org.opencontainers.image.ref.name="${APP_BUILD_TAG}" \
      org.opencontainers.image.revision="${APP_BUILD_SHA}" \
      org.opencontainers.image.created="${APP_BUILD_TIME}" \
      org.opencontainers.image.source="${APP_BUILD_IMAGE}"

# Install uv — fast Python package manager
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/uv

WORKDIR /app

# ── Layer 1: External dependencies only (cached — rebuild khi pyproject.toml/uv.lock đổi)
COPY pyproject.toml uv.lock ./
RUN uv sync --frozen --no-dev --no-install-project

# ── Layer 2: Application source code + README (cần để build package)
COPY src/ ./src/
COPY README.md ./
RUN uv sync --frozen --no-dev

# ── Layer 3: Agent prompts (system prompts tiếng Việt)
COPY prompts/ ./prompts/

# ── Layer 4: Workspace knowledge base (memory/ — thay đổi thường xuyên)
COPY memory/ ./memory/

# ── Layer 5: Workspace root marker
COPY CLAUDE.md ./

# ── Runtime config
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONPATH=/app/src \
    WORKSPACE_PATH=/app \
    APP_BUILD_IMAGE="${APP_BUILD_IMAGE}" \
    APP_BUILD_TAG="${APP_BUILD_TAG}" \
    APP_BUILD_SHA="${APP_BUILD_SHA}" \
    APP_BUILD_TIME="${APP_BUILD_TIME}" \
    PATH="/app/.venv/bin:$PATH"

# ── Artifact store — mount persistent volume ở đây nếu có
RUN mkdir -p /app/outputs/runs

EXPOSE 8080

# ── Secrets injected tại AgentBase Runtime qua env file — KHÔNG bake vào image:
#   AI_PLATFORM_API_KEY     VNG AI Platform (Gemma/Qwen)
#   ANTHROPIC_API_KEY       Claude fallback (optional)
#   TELEGRAM_BOT_TOKEN      Telegram bot
#   TELEGRAM_CHAT_ID        Channel/group ID
#   GREENNODE_CLIENT_ID     Auto-injected bởi runtime
#   GREENNODE_CLIENT_SECRET Auto-injected bởi runtime
#   GREENNODE_AGENT_IDENTITY Auto-injected bởi runtime

CMD ["python", "-m", "vks_intelligence"]
