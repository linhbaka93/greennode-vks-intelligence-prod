"""Request/response schema cho API surface /tasks/*.

Đây là contract HTTP ổn định mà n8n gọi. Tách khỏi schema nội bộ trong
`contracts` để có thể đổi internal mà không phá vỡ hợp đồng với n8n.
"""

from __future__ import annotations

from typing import Any

from pydantic import BaseModel, ConfigDict, Field

from vks_intelligence.contracts import BudgetPolicy, ModelPolicy, TaskType


class HealthResponse(BaseModel):
    status: str
    timestamp: str
    version: str
    models_enabled: list[str] = Field(default_factory=list)
    build_image: str = ""
    build_tag: str = ""
    build_sha: str = ""
    build_time: str = ""


class TaskRequestBody(BaseModel):
    model_config = ConfigDict(protected_namespaces=())

    request_id: str
    source: str = "n8n"
    payload: dict[str, Any] = Field(default_factory=dict)
    dry_run: bool = False
    notify: bool = False
    save_output: bool = True
    human_approval_required: bool = False
    model_policy: ModelPolicy = ModelPolicy.BALANCED
    timeout_seconds: int | None = None
    budget_policy: BudgetPolicy | None = None


class TaskResponse(BaseModel):
    task_id: str
    status: str
    quality_passed: bool = False
    quality_score: float | None = None
    artifact_path: str = ""
    telegram_preview: str = ""
    requires_approval: bool = False
    fallbacks_used: list[str] = Field(default_factory=list)
    warnings: list[str] = Field(default_factory=list)


class QARequestBody(BaseModel):
    question: str
    actor_id: str = ""
    session_id: str = ""
    task_type_override: str = ""   # orchestrator decision; rỗng → keyword routing
    force_refresh: bool = False    # bypass cache khi orchestrator quyết refresh


class QAResponse(BaseModel):
    answer: str
    confidence: str = "medium"
    escalated: bool = False
    research_used: bool = False
    sources: list[str] = Field(default_factory=list)
    session_id: str = ""
    artifact_path: str = ""


class DailyIntelligenceRequestBody(BaseModel):
    model_config = ConfigDict(protected_namespaces=())

    request_id: str
    source: str = "n8n"
    days_window: int = 1
    dry_run: bool = False
    notify: bool = False
    save_output: bool = True
    human_approval_required: bool = False
    model_policy: ModelPolicy = ModelPolicy.BALANCED


class QualityCheckRequest(BaseModel):
    content: str
    task_type: TaskType | None = None


class QualityCheckResponse(BaseModel):
    verdict: str
    score: float = Field(..., ge=0.0, le=1.0)
    failures: list[str] = Field(default_factory=list)
    warnings: list[str] = Field(default_factory=list)


class RunSummary(BaseModel):
    run_id: str
    task_id: str
    task_type: str
    status: str
    quality_score: float | None = None
    input_tokens: int = 0
    output_tokens: int = 0
    fallback_count: int = 0
    published: bool = False
    finished_at: str = ""


class DashboardSummary(BaseModel):
    total_runs: int = 0
    runs_published: int = 0
    runs_blocked: int = 0
    runs_needs_review: int = 0
    total_input_tokens: int = 0
    total_output_tokens: int = 0
    avg_quality_score: float | None = None
    fallback_runs: int = 0
    by_task_type: dict[str, int] = Field(default_factory=dict)


class QAActivitySummary(BaseModel):
    """Tổng hợp QA activity từ Telegram (streaming + current research)."""
    total_qa: int = 0
    memory_lookup: int = 0
    current_research: int = 0
    fallback_count: int = 0
    avg_latency_ms: float | None = None
    by_day: dict[str, int] = Field(default_factory=dict)
    by_routed_by: dict[str, int] = Field(default_factory=dict)
    by_task_type: dict[str, int] = Field(default_factory=dict)


class CostTrendPoint(BaseModel):
    """Token usage tổng hợp theo ngày cho cost trend chart."""
    date: str
    input_tokens: int = 0
    output_tokens: int = 0
    runs: int = 0


class AgentRunDetail(BaseModel):
    """Chi tiết một agent trong một run (đọc từ <agent>.json)."""
    model_config = {"protected_namespaces": ()}

    agent: str
    status: str = ""
    model_used: str = ""
    input_tokens: int = 0
    output_tokens: int = 0
    json_parse_status: str = ""
    summary: str = ""


class RunDetail(BaseModel):
    """Chi tiết drill-down một run cho dashboard."""
    run_id: str
    task_id: str = ""
    task_type: str = ""
    status: str = ""
    quality_score: float | None = None
    quality_verdict: str = ""
    quality_failures: list[str] = Field(default_factory=list)
    quality_warnings: list[str] = Field(default_factory=list)
    input_tokens: int = 0
    output_tokens: int = 0
    fallbacks: list[str] = Field(default_factory=list)
    agents: list[AgentRunDetail] = Field(default_factory=list)
    warnings: list[str] = Field(default_factory=list)
    started_at: str = ""
    finished_at: str = ""
    synthesis_preview: str = ""
