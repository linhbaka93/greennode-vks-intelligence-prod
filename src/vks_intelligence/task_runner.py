"""Chạy specialist agent trong giới hạn budget và timeout của run.

Bọc mỗi lần chạy agent bằng agent timeout, bắt lỗi để biến thành AgentResult
status=failed thay vì làm sập run, và hỗ trợ chạy song song các agent độc lập.
"""

from __future__ import annotations

import concurrent.futures
import logging
import time

from vks_intelligence.contracts import AgentResult, AgentStatus, AgentTask
from vks_intelligence.llm.router import ModelRouter
from vks_intelligence.run_context import RunContext

log = logging.getLogger(__name__)


def run_agent(
    task: AgentTask,
    context: RunContext,
    router: ModelRouter,
) -> AgentResult:
    """Chạy một agent với agent_deadline; lỗi/timeout → AgentResult failed/partial."""
    import vks_intelligence.registry as registry

    if not context.can_spawn_agent():
        return AgentResult(
            agent=task.agent,
            task_id=task.task_id,
            status=AgentStatus.FAILED,
            summary="Bị huỷ: vượt trần max_agents của run.",
        )

    remaining = context.remaining_seconds()
    if remaining <= 0:
        return AgentResult(
            agent=task.agent,
            task_id=task.task_id,
            status=AgentStatus.FAILED,
            summary="Bị huỷ: run đã hết thời gian.",
        )

    context.agents_used += 1
    specialist_cls = registry.get(task.agent)
    specialist = specialist_cls(router)

    deadline = context.agent_deadline()
    timeout_secs = max(1.0, deadline - time.monotonic())

    try:
        with concurrent.futures.ThreadPoolExecutor(max_workers=1) as ex:
            fut = ex.submit(specialist.run, task, context)
            return fut.result(timeout=timeout_secs)
    except concurrent.futures.TimeoutError:
        log.warning("Agent %s vượt timeout %.0fs", task.agent, timeout_secs)
        return AgentResult(
            agent=task.agent,
            task_id=task.task_id,
            status=AgentStatus.PARTIAL,
            summary=f"Timeout sau {timeout_secs:.0f}s.",
        )
    except Exception as exc:
        log.error("Agent %s lỗi: %s", task.agent, exc, exc_info=True)
        return AgentResult(
            agent=task.agent,
            task_id=task.task_id,
            status=AgentStatus.FAILED,
            summary=f"Lỗi: {type(exc).__name__}: {exc}",
        )


def run_agents(
    tasks: list[AgentTask],
    context: RunContext,
    router: ModelRouter,
) -> list[AgentResult]:
    """Chạy nhiều agent song song, tôn trọng run deadline."""
    if not tasks:
        return []

    with concurrent.futures.ThreadPoolExecutor(max_workers=len(tasks)) as pool:
        futs = {
            pool.submit(run_agent, task, context, router): task
            for task in tasks
        }
        results: list[AgentResult] = []
        remaining = context.remaining_seconds()
        try:
            for fut in concurrent.futures.as_completed(futs, timeout=max(1.0, remaining)):
                results.append(fut.result())
        except concurrent.futures.TimeoutError:
            for fut, task in futs.items():
                if not fut.done():
                    results.append(AgentResult(
                        agent=task.agent,
                        task_id=task.task_id,
                        status=AgentStatus.PARTIAL,
                        summary="Timeout run-level.",
                    ))
                elif not any(r.task_id == task.task_id for r in results):
                    try:
                        results.append(fut.result())
                    except Exception:
                        pass

    return results
