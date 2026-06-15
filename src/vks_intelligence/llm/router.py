"""Model router — chọn provider/model theo workload và model_policy, có fallback.

Ánh xạ (workload, model_policy) → model id từ Settings. Khi model chính lỗi, đi
qua 4 cấp fallback: stricter prompt → model khác cùng provider → provider khác →
degraded deterministic. Mỗi bước fallback ghi vào RunContext.
"""

from __future__ import annotations

import logging
from collections.abc import Iterator
from enum import Enum

from vks_intelligence.contracts import FallbackTrace, ModelPolicy
from vks_intelligence.llm.base import LLMRequest, LLMResponse
from vks_intelligence.run_context import RunContext

log = logging.getLogger(__name__)


class Workload(str, Enum):
    QA = "qa"
    RESEARCH = "research"
    SYNTHESIS = "synthesis"
    CRITIC = "critic"
    ORCHESTRATOR = "orchestrator"


class ModelRouter:
    def __init__(self) -> None:
        self._oai = None
        self._ant = None

    # ------------------------------------------------------------------
    # Lazy provider init
    # ------------------------------------------------------------------
    def _oai_provider(self):
        if self._oai is None:
            from vks_intelligence.config import get_settings
            from vks_intelligence.llm.openai_compatible import OpenAICompatibleProvider
            s = get_settings()
            self._oai = OpenAICompatibleProvider(s.ai_platform_base_url, s.ai_platform_api_key)
        return self._oai

    def _ant_provider(self):
        if self._ant is None:
            from vks_intelligence.config import get_settings
            from vks_intelligence.llm.anthropic_provider import AnthropicProvider
            s = get_settings()
            self._ant = AnthropicProvider(s.anthropic_api_key)
        return self._ant

    def _provider_for(self, model: str):
        return self._ant_provider() if "claude" in model.lower() else self._oai_provider()

    # ------------------------------------------------------------------
    # Model selection
    # ------------------------------------------------------------------
    def model_for(self, workload: Workload, policy: ModelPolicy) -> str:
        """Trả model id phù hợp với workload và policy."""
        from vks_intelligence.config import get_settings
        s = get_settings()
        if policy == ModelPolicy.PREMIUM:
            return s.model_premium
        _map = {
            Workload.QA: s.model_qa,
            Workload.RESEARCH: s.model_research,
            Workload.SYNTHESIS: s.model_synthesis,
            Workload.CRITIC: s.model_critic,
            Workload.ORCHESTRATOR: s.model_qa,
        }
        return _map.get(workload, s.model_fallback)

    # ------------------------------------------------------------------
    # Routing + 2-level fallback
    # ------------------------------------------------------------------
    def complete(
        self,
        workload: Workload,
        request: LLMRequest,
        context: RunContext,
    ) -> LLMResponse:
        """Route → gọi provider qua retries → fallback nếu cần; ghi usage/fallback."""
        from vks_intelligence.config import get_settings
        from vks_intelligence.llm.retries import with_retry

        s = get_settings()
        primary = self.model_for(workload, context.request.model_policy)
        timeout = min(
            request.timeout_seconds or s.model_timeout_seconds,
            s.model_timeout_seconds,
        )
        req = LLMRequest(
            model=primary,
            system=request.system,
            user=request.user,
            max_output_tokens=request.max_output_tokens,
            temperature=request.temperature,
            timeout_seconds=timeout,
            response_json=request.response_json,
            stop=request.stop,
        )

        # Level 1 — primary model
        primary_err: Exception | None = None
        try:
            resp = with_retry(
                lambda: self._provider_for(primary).complete(req),
                s.model_retry_limit,
            )
            context.record_usage(resp.input_tokens, resp.output_tokens)
            return resp
        except Exception as exc:
            primary_err = exc
            log.warning("Primary model %s thất bại: %s", primary, exc)

        # Level 2 — fallback model
        fallback = s.model_fallback if primary != s.model_fallback else s.model_research
        if fallback and fallback != primary:
            context.record_fallback(FallbackTrace(
                agent=workload.value,
                from_model=primary,
                to_model=fallback,
                reason=str(primary_err),
            ))
            req_fb = LLMRequest(
                model=fallback,
                system=request.system,
                user=request.user,
                max_output_tokens=request.max_output_tokens,
                temperature=request.temperature,
                timeout_seconds=timeout,
                response_json=request.response_json,
                stop=request.stop,
            )
            try:
                resp = with_retry(
                    lambda: self._provider_for(fallback).complete(req_fb),
                    1,
                )
                context.record_usage(resp.input_tokens, resp.output_tokens)
                return resp
            except Exception as fb_err:
                log.error("Fallback model %s cũng thất bại: %s", fallback, fb_err)
                raise RuntimeError(
                    f"Tất cả model thất bại — primary: {primary_err}; fallback: {fb_err}"
                ) from fb_err

        raise RuntimeError(f"Primary model thất bại: {primary_err}") from primary_err

    def stream_complete(self, workload: Workload, request: LLMRequest) -> Iterator[str]:
        """Stream text deltas cho fast-path QA; không có RunContext nên bỏ budget tracking.

        Chỉ dùng cho Telegram direct reply — không đi qua supervisor pipeline.
        """
        from vks_intelligence.config import get_settings

        s = get_settings()
        model = self.model_for(workload, ModelPolicy.BALANCED)
        timeout = min(
            request.timeout_seconds or s.model_timeout_seconds,
            s.model_timeout_seconds,
        )
        req = LLMRequest(
            model=model,
            system=request.system,
            user=request.user,
            max_output_tokens=request.max_output_tokens,
            temperature=request.temperature,
            timeout_seconds=timeout,
            response_json=False,
            stop=request.stop,
        )
        yield from self._provider_for(model).stream_complete(req)

    def complete_once(self, workload: Workload, request: LLMRequest) -> LLMResponse:
        """Gọi model 1 lần (có retry), không RunContext — cho fast-path như orchestrator.

        Không track budget/fallback vì dùng ngoài supervisor pipeline. Lỗi → raise
        cho caller fallback (vd orchestrator fallback sang keyword).
        """
        from vks_intelligence.config import get_settings
        from vks_intelligence.llm.retries import with_retry

        s = get_settings()
        model = self.model_for(workload, ModelPolicy.BALANCED)
        timeout = min(
            request.timeout_seconds or s.model_timeout_seconds,
            s.model_timeout_seconds,
        )
        req = LLMRequest(
            model=model,
            system=request.system,
            user=request.user,
            max_output_tokens=request.max_output_tokens,
            temperature=request.temperature,
            timeout_seconds=timeout,
            response_json=request.response_json,
            stop=request.stop,
        )
        return with_retry(lambda: self._provider_for(model).complete(req), s.model_retry_limit)
