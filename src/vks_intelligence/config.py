"""Cấu hình runtime nạp từ biến môi trường.

Tập trung mọi model id, budget, timeout và ngưỡng quality về một nơi để agent
không hardcode. Đọc một lần lúc khởi động qua `get_settings()`.
"""

from __future__ import annotations

from functools import lru_cache
from pathlib import Path

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


def _find_workspace_root() -> Path:
    """Đi lên từ file này đến khi gặp CLAUDE.md để xác định gốc workspace."""
    current = Path(__file__).resolve().parent
    for _ in range(8):
        if (current / "CLAUDE.md").exists():
            return current
        current = current.parent
    return Path(__file__).resolve().parent.parent.parent


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env", extra="ignore", protected_namespaces=()
    )

    # Model providers
    ai_platform_base_url: str = "https://maas-llm-aiplatform-hcm.api.vngcloud.vn/v1"
    ai_platform_api_key: str = ""
    anthropic_api_key: str = ""

    # Model routing — 2 self-hosted models: gemma-4-31b-it (fast) | qwen3-5-27b (reasoning)
    model_qa: str = "google/gemma-4-31b-it"
    model_research: str = "qwen/qwen3-5-27b"
    model_synthesis: str = "google/gemma-4-31b-it"
    model_critic: str = "qwen/qwen3-5-27b"
    model_premium: str = "qwen/qwen3-5-27b"
    model_fallback: str = "google/gemma-4-31b-it"

    # Telegram
    telegram_bot_token: str = ""
    telegram_chat_id: str = ""
    telegram_owner_chat_id: str = ""
    telegram_max_chars_per_message: int = 3900

    # Scheduler nội bộ (cron theo scheduler_timezone; thay control plane n8n)
    scheduler_enabled: bool = True
    scheduler_timezone: str = "Asia/Ho_Chi_Minh"
    scheduler_trigger_token: str = ""
    # Day-of-week dùng TÊN (fri/sun...) — APScheduler đếm 0=Monday, khác cron chuẩn 0=Sunday
    cron_daily_intelligence: str = "0 8 * * *"
    cron_weekly_digest: str = "0 15 * * fri"
    cron_monthly_brief: str = "0 15 1 * *"
    cron_competitor_monitor: str = "0 6 * * *"
    cron_memory_maintenance: str = "0 10 * * sun"

    # Social scrape (Facebook/LinkedIn...) — park mặc định: login wall chặn fetch tĩnh
    enable_social_scrape: bool = False

    # Google News: resolve link redirect về URL bài gốc của publisher
    google_news_resolve_links: bool = True
    google_news_resolve_max: int = 10

    # Workspace & memory
    workspace_path: Path = Field(default_factory=_find_workspace_root)
    github_repo: str = ""
    github_branch: str = "main"
    github_token: str = ""

    # Timeout (giây)
    run_timeout_qa_seconds: int = 30
    run_timeout_weekly_seconds: int = 480
    run_timeout_monthly_seconds: int = 720
    agent_timeout_seconds: int = 120
    model_timeout_seconds: int = 60

    # Evidence / interactive performance
    evidence_rss_timeout_seconds: int = 8
    evidence_web_timeout_seconds: int = 10
    evidence_social_timeout_seconds: int = 5
    evidence_fetch_max_workers: int = 6
    evidence_interactive_max_targets: int = 6
    evidence_cache_ttl_seconds: int = 3600
    social_negative_cache_ttl_seconds: int = 21600
    qa_current_research_cache_ttl_seconds: int = 21600
    max_live_research_workers: int = 2

    # Retry / JSON repair
    model_retry_limit: int = 2
    model_json_repair_limit: int = 1

    # Budget agent / token
    max_agents_weekly: int = 5
    max_agents_qa_escalated: int = 3
    max_input_tokens_worker: int = 80_000
    max_output_tokens_worker: int = 6_000
    max_output_tokens_synthesis: int = 6_000

    # Quality gate
    quality_min_score_publish: float = 0.80
    quality_min_score_approval: float = 0.65

    # Freshness threshold (ngày) — memory_tool flag dữ liệu cũ
    tier1_freshness_days: int = 7
    tier2_freshness_days: int = 7
    tier3_freshness_days: int = 7
    market_trends_freshness_days: int = 7
    gpu_pricing_freshness_days: int = 7

    # Memory auto-write (curator patch apply)
    memory_auto_write_enabled: bool = False
    memory_auto_write_min_confidence: str = "high"
    memory_auto_write_min_quality: float = 0.85

    # Memory write-back: ghi key_findings từ research run thành dated .md files
    memory_write_back_enabled: bool = True

    # Battlecard auto-write: True → ghi thẳng memory/battlecards/; False → memory/_proposed/ chờ duyệt
    battlecard_auto_write: bool = False

    # Citation grader: HEAD-check URLs sau synthesis, đánh dấu dead links vào warnings
    citation_grader_enabled: bool = True

    # Dashboard
    dashboard_enabled: bool = True

    # Artifact store
    artifact_root: Path = Path("outputs/runs")

    # Runtime
    log_level: str = "INFO"
    port: int = 8080
    app_build_image: str = ""
    app_build_tag: str = ""
    app_build_sha: str = ""
    app_build_time: str = ""


@lru_cache
def get_settings() -> Settings:
    return Settings()
