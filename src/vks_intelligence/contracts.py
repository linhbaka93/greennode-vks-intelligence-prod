"""Schema dữ liệu nội bộ cho mọi task production.

Một task luôn có: request → plan → các AgentResult → QualityResult → artifact +
RunMetadata. Supervisor chỉ được synthesis từ claim đã structured và validate.
"""

from __future__ import annotations

from enum import Enum
from typing import Any

from pydantic import BaseModel, ConfigDict, Field

SCHEMA_VERSION = "1.0"


class _Model(BaseModel):
    model_config = ConfigDict(protected_namespaces=())


class TaskType(str, Enum):
    QA = "qa"
    DAILY_INTELLIGENCE = "daily-intelligence"
    WEEKLY_DIGEST = "weekly-digest"
    MONTHLY_BRIEF = "monthly-brief"
    COMPETITOR_MONITOR = "competitor-monitor"
    PRICING_ANALYSIS = "pricing-analysis"
    BATTLECARD = "battlecard"
    MEMORY_MAINTENANCE = "memory-maintenance"


class TaskStatus(str, Enum):
    PENDING = "pending"
    RUNNING = "running"
    COMPLETED = "completed"
    NEEDS_REVIEW = "needs_review"
    BLOCKED = "blocked"
    FAILED = "failed"


class AgentStatus(str, Enum):
    OK = "ok"
    PARTIAL = "partial"
    FAILED = "failed"


class QualityVerdict(str, Enum):
    PASS = "pass"
    NEEDS_REVIEW = "needs_review"
    REVISE = "revise"
    BLOCKED = "blocked"


class Confidence(str, Enum):
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"


class EvidenceType(str, Enum):
    MEMORY = "memory"
    RSS = "rss"
    SCRAPE = "scrape"
    SOCIAL = "social"
    SEARCH = "search"
    MANUAL = "manual"


class ModelPolicy(str, Enum):
    FAST = "fast"
    BALANCED = "balanced"
    PREMIUM = "premium"


class BudgetPolicy(BaseModel):
    max_agents: int = 5
    max_agent_seconds: int = 120
    max_retries: int = 2
    max_input_tokens: int = 80_000
    max_output_tokens: int = 4_000


class TaskRequest(_Model):
    request_id: str
    task_type: TaskType
    source: str = "n8n"
    payload: dict[str, Any] = Field(default_factory=dict)
    dry_run: bool = False
    notify: bool = False
    save_output: bool = True
    human_approval_required: bool = False
    model_policy: ModelPolicy = ModelPolicy.BALANCED
    timeout_seconds: int | None = None
    budget_policy: BudgetPolicy = Field(default_factory=BudgetPolicy)


class AgentTask(BaseModel):
    agent: str
    task_id: str
    instruction: str
    inputs: dict[str, Any] = Field(default_factory=dict)
    critical: bool = False


class TaskPlan(BaseModel):
    task_id: str
    task_type: TaskType
    agent_tasks: list[AgentTask] = Field(default_factory=list)
    parallel: bool = True


class Claim(BaseModel):
    claim: str
    source: str = ""
    confidence: Confidence = Confidence.MEDIUM
    evidence_type: EvidenceType = EvidenceType.MEMORY


class EvidenceItem(BaseModel):
    title: str
    url: str = ""
    published_at: str = ""
    retrieved_at: str = ""
    publisher: str = ""
    snippet: str = ""
    evidence_type: EvidenceType = EvidenceType.MANUAL
    confidence: Confidence = Confidence.MEDIUM
    source_label: str = ""
    content_hash: str = ""
    query: str = ""


class EvidenceBundle(BaseModel):
    """Tập hợp evidence đã chuẩn hóa cho một run — đầu vào duy nhất của agent."""
    query: str = ""
    generated_at: str = ""
    items: list[EvidenceItem] = Field(default_factory=list)
    memory_context: str = ""
    collected_at: str = ""
    days_window: int = 7
    sources_used: list[str] = Field(default_factory=list)
    source_counts: dict[str, int] = Field(default_factory=dict)
    dedupe_stats: dict[str, int] = Field(default_factory=dict)
    warnings: list[str] = Field(default_factory=list)

    @property
    def has_fresh_data(self) -> bool:
        return any(
            i.evidence_type in (EvidenceType.RSS, EvidenceType.SCRAPE, EvidenceType.SEARCH)
            or i.evidence_type == EvidenceType.SOCIAL
            for i in self.items
        )


class QAEscalationIntent(str, Enum):
    """Phân loại intent câu hỏi Q&A để quyết định fast-path hay current-research."""
    MEMORY_LOOKUP = "memory_lookup"      # trả từ workspace memory
    CURRENT_RESEARCH = "current_research"  # cần dữ liệu mới nhất / latest


class AgentResult(_Model):
    schema_version: str = SCHEMA_VERSION
    agent: str
    task_id: str
    status: AgentStatus = AgentStatus.OK
    summary: str = ""
    key_findings: list[str] = Field(default_factory=list)
    claims: list[Claim] = Field(default_factory=list)
    risks: list[str] = Field(default_factory=list)
    gaps: list[str] = Field(default_factory=list)
    recommended_actions: list[str] = Field(default_factory=list)
    model_used: str = ""
    input_tokens: int = 0
    output_tokens: int = 0
    retry_count: int = 0
    fallback_used: bool = False
    json_parse_status: str = "valid"


class QualityResult(BaseModel):
    verdict: QualityVerdict = QualityVerdict.PASS
    score: float = 1.0
    failures: list[str] = Field(default_factory=list)
    warnings: list[str] = Field(default_factory=list)

    @property
    def passed(self) -> bool:
        return self.verdict == QualityVerdict.PASS


class MemoryPatchOp(str, Enum):
    CREATE = "create"
    UPDATE = "update"
    ARCHIVE = "archive"


class MemoryPatch(BaseModel):
    op: MemoryPatchOp
    path: str
    reason: str
    content: str = ""
    confidence: Confidence = Confidence.MEDIUM
    auto_applied: bool = False
    approved_by: str = ""


class FallbackTrace(BaseModel):
    agent: str
    from_model: str
    to_model: str
    reason: str


class RunMetadata(BaseModel):
    task_id: str
    run_id: str
    task_type: TaskType
    status: TaskStatus = TaskStatus.PENDING
    trigger_source: str = "n8n"
    agents: list[str] = Field(default_factory=list)
    models: dict[str, str] = Field(default_factory=dict)
    input_tokens: int = 0
    output_tokens: int = 0
    fallbacks: list[FallbackTrace] = Field(default_factory=list)
    quality_score: float | None = None
    source_count: int = 0
    approval_required: bool = False
    published: bool = False
    started_at: str = ""
    finished_at: str = ""
    warnings: list[str] = Field(default_factory=list)
