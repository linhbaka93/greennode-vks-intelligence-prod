"""Provider cho endpoint OpenAI-compatible (VNG AI Platform) — Gemma/Qwen.

Dùng `openai` client trỏ base_url về AI Platform. Map LLMRequest sang
chat.completions và trích token usage từ response.usage.
"""

from __future__ import annotations

from collections.abc import Iterator

from vks_intelligence.llm.base import LLMRequest, LLMResponse


class OpenAICompatibleProvider:
    name = "openai_compatible"

    def __init__(self, base_url: str, api_key: str) -> None:
        self.base_url = base_url
        self.api_key = api_key
        self._client = None

    def _client_instance(self):
        if self._client is None:
            from openai import OpenAI
            self._client = OpenAI(
                base_url=self.base_url,
                api_key=self.api_key,
            )
        return self._client

    def complete(self, request: LLMRequest) -> LLMResponse:
        """Gọi chat.completions; raise lỗi mạng/timeout cho tầng retries."""
        client = self._client_instance()

        kwargs: dict = {
            "model": request.model,
            "messages": [
                {"role": "system", "content": request.system},
                {"role": "user", "content": request.user},
            ],
            "max_tokens": request.max_output_tokens,
            "temperature": request.temperature,
            "timeout": request.timeout_seconds,
        }
        if request.response_json:
            kwargs["response_format"] = {"type": "json_object"}
        if request.stop:
            kwargs["stop"] = request.stop

        resp = client.chat.completions.create(**kwargs)
        text = resp.choices[0].message.content or ""
        usage = resp.usage

        return LLMResponse(
            text=text,
            model=request.model,
            input_tokens=usage.prompt_tokens if usage else 0,
            output_tokens=usage.completion_tokens if usage else 0,
        )

    def stream_complete(self, request: LLMRequest) -> Iterator[str]:
        """Yield text deltas as they arrive; không hỗ trợ response_json mode."""
        client = self._client_instance()
        kwargs: dict = {
            "model": request.model,
            "messages": [
                {"role": "system", "content": request.system},
                {"role": "user", "content": request.user},
            ],
            "max_tokens": request.max_output_tokens,
            "temperature": request.temperature,
            "timeout": request.timeout_seconds,
            "stream": True,
        }
        if request.stop:
            kwargs["stop"] = request.stop
        for chunk in client.chat.completions.create(**kwargs):
            if chunk.choices and chunk.choices[0].delta.content:
                yield chunk.choices[0].delta.content
