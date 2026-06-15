"""Tổng hợp observability từ artifact store cho dashboard.

Đọc metadata.json của các run dưới artifact_root và quy thành chỉ số: token usage,
phân bố quality score, số lần fallback, tỉ lệ publish/approval. Chỉ đọc, không
tính lại bằng model — dashboard phải rẻ và nhanh.
"""

from __future__ import annotations

import json
from pathlib import Path

from vks_intelligence.schemas import (
    AgentRunDetail,
    CostTrendPoint,
    DashboardSummary,
    QAActivitySummary,
    RunDetail,
    RunSummary,
)


def _load_metadata(run_dir: Path) -> dict | None:
    meta_path = run_dir / "metadata.json"
    if not meta_path.exists():
        return None
    try:
        return json.loads(meta_path.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return None


def list_runs(artifact_root: Path, limit: int = 50) -> list[RunSummary]:
    """Liệt kê các run gần nhất từ metadata.json, mới nhất trước."""
    if not artifact_root.exists():
        return []

    run_dirs = sorted(
        [d for d in artifact_root.iterdir() if d.is_dir()],
        key=lambda d: d.stat().st_mtime,
        reverse=True,
    )

    selected_dirs = run_dirs if limit <= 0 else run_dirs[:limit]

    summaries: list[RunSummary] = []
    for run_dir in selected_dirs:
        meta = _load_metadata(run_dir)
        if meta is None:
            continue
        fallback_count = len(meta.get("fallbacks", []))
        summaries.append(RunSummary(
            run_id=meta.get("run_id", run_dir.name),
            task_id=meta.get("task_id", ""),
            task_type=meta.get("task_type", ""),
            status=meta.get("status", ""),
            quality_score=meta.get("quality_score"),
            input_tokens=meta.get("input_tokens", 0),
            output_tokens=meta.get("output_tokens", 0),
            fallback_count=fallback_count,
            published=meta.get("published", False),
            finished_at=meta.get("finished_at", ""),
        ))

    return summaries


def summary(artifact_root: Path) -> DashboardSummary:
    """Gộp chỉ số toàn cục: tổng run, token, quality trung bình, fallback, publish."""
    runs = list_runs(artifact_root, limit=0)  # unlimited for summary

    if not runs:
        return DashboardSummary()

    total = len(runs)
    published = sum(1 for r in runs if r.published)
    blocked = sum(1 for r in runs if r.status == "blocked")
    needs_review = sum(1 for r in runs if r.status == "needs_review")
    total_in = sum(r.input_tokens for r in runs)
    total_out = sum(r.output_tokens for r in runs)
    fallback_runs = sum(1 for r in runs if r.fallback_count > 0)

    scores = [r.quality_score for r in runs if r.quality_score is not None]
    avg_q = round(sum(scores) / len(scores), 3) if scores else None

    by_type: dict[str, int] = {}
    for r in runs:
        by_type[r.task_type] = by_type.get(r.task_type, 0) + 1

    return DashboardSummary(
        total_runs=total,
        runs_published=published,
        runs_blocked=blocked,
        runs_needs_review=needs_review,
        total_input_tokens=total_in,
        total_output_tokens=total_out,
        avg_quality_score=avg_q,
        fallback_runs=fallback_runs,
        by_task_type=by_type,
    )


def cost_trend(artifact_root: Path, days: int = 14) -> list[CostTrendPoint]:
    """Token usage tổng hợp theo ngày từ metadata.json, cũ → mới, N ngày gần nhất."""
    runs = list_runs(artifact_root, limit=0)
    by_day: dict[str, CostTrendPoint] = {}
    for r in runs:
        day = (r.finished_at or "")[:10]
        if not day:
            continue
        point = by_day.get(day)
        if point is None:
            point = CostTrendPoint(date=day)
            by_day[day] = point
        point.input_tokens += r.input_tokens
        point.output_tokens += r.output_tokens
        point.runs += 1
    points = [by_day[d] for d in sorted(by_day.keys())]
    return points[-days:] if days > 0 else points


def run_detail(artifact_root: Path, run_id: str) -> RunDetail | None:
    """Đọc chi tiết một run từ outputs/runs/<run_id>/ cho drill-down. None nếu không thấy."""
    run_dir = artifact_root / run_id
    if not run_dir.is_dir():
        return None
    meta = _load_metadata(run_dir)
    if meta is None:
        return None

    models = meta.get("models", {}) or {}
    agents: list[AgentRunDetail] = []
    for name in meta.get("agents", []):
        agent_path = run_dir / f"{name}.json"
        if agent_path.exists():
            try:
                a = json.loads(agent_path.read_text(encoding="utf-8"))
            except (json.JSONDecodeError, OSError):
                a = {}
            agents.append(AgentRunDetail(
                agent=name,
                status=a.get("status", ""),
                model_used=a.get("model_used", "") or models.get(name, ""),
                input_tokens=a.get("input_tokens", 0),
                output_tokens=a.get("output_tokens", 0),
                json_parse_status=a.get("json_parse_status", ""),
                summary=(a.get("summary", "") or "")[:500],
            ))
        else:
            agents.append(AgentRunDetail(agent=name, model_used=models.get(name, "")))

    quality_verdict = ""
    quality_failures: list[str] = []
    quality_warnings: list[str] = []
    qp = run_dir / "quality.json"
    if qp.exists():
        try:
            q = json.loads(qp.read_text(encoding="utf-8"))
            quality_verdict = q.get("verdict", "")
            quality_failures = q.get("failures", []) or []
            quality_warnings = q.get("warnings", []) or []
        except (json.JSONDecodeError, OSError):
            pass

    preview = ""
    for fname in ("final.md", "synthesis.md"):
        fp = run_dir / fname
        if fp.exists():
            try:
                preview = fp.read_text(encoding="utf-8")[:1500]
            except OSError:
                preview = ""
            break

    fallbacks = [
        f"{f.get('from_model', '?')}→{f.get('to_model', '?')}"
        for f in meta.get("fallbacks", [])
    ]

    return RunDetail(
        run_id=meta.get("run_id", run_id),
        task_id=meta.get("task_id", ""),
        task_type=meta.get("task_type", ""),
        status=meta.get("status", ""),
        quality_score=meta.get("quality_score"),
        quality_verdict=quality_verdict,
        quality_failures=quality_failures,
        quality_warnings=quality_warnings,
        input_tokens=meta.get("input_tokens", 0),
        output_tokens=meta.get("output_tokens", 0),
        fallbacks=fallbacks,
        agents=agents,
        warnings=meta.get("warnings", []) or [],
        started_at=meta.get("started_at", ""),
        finished_at=meta.get("finished_at", ""),
        synthesis_preview=preview,
    )


def qa_activity(qa_log_root: Path, days: int = 14) -> QAActivitySummary:
    """Tổng hợp QA activity (volume, intent, latency, fallback) từ qa_log JSONL."""
    from vks_intelligence.tools import qa_log

    events = qa_log.read_events(qa_log_root, days=days)
    if not events:
        return QAActivitySummary()

    total = len(events)
    memory_lookup = sum(1 for e in events if e.get("intent") == "memory_lookup")
    current_research = sum(1 for e in events if e.get("intent") == "current_research")
    fallback = sum(1 for e in events if e.get("fallback"))

    latencies = [e["latency_ms"] for e in events if isinstance(e.get("latency_ms"), (int, float))]
    avg_latency = round(sum(latencies) / len(latencies), 1) if latencies else None

    by_day: dict[str, int] = {}
    by_routed_by: dict[str, int] = {}
    by_task_type: dict[str, int] = {}
    for e in events:
        day = str(e.get("ts", ""))[:10]
        if day:
            by_day[day] = by_day.get(day, 0) + 1
        routed = e.get("routed_by") or "unknown"
        by_routed_by[routed] = by_routed_by.get(routed, 0) + 1
        # task_type chỉ có nghĩa với current_research
        if e.get("intent") == "current_research":
            tt = e.get("task_type") or "unknown"
            by_task_type[tt] = by_task_type.get(tt, 0) + 1

    return QAActivitySummary(
        total_qa=total,
        memory_lookup=memory_lookup,
        current_research=current_research,
        fallback_count=fallback,
        avg_latency_ms=avg_latency,
        by_day=dict(sorted(by_day.items())),
        by_routed_by=dict(sorted(by_routed_by.items())),
        by_task_type=dict(sorted(by_task_type.items(), key=lambda kv: kv[1], reverse=True)),
    )
