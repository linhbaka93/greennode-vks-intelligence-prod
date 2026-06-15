"""Provider cho Claude qua Anthropic API — premium/fallback path.

Map LLMRequest sang messages.create với system tách riêng, trích token usage từ
response.usage.
"""

from __future__ import annotations

from collections.abc import Iterator

from vks_intelligence.llm.base import LLMRequest, LLMResponse


class AnthropicProvider:
    name = "anthropic"

    def __init__(self, api_key: str) -> None:
        self.api_key = api_key
        self._client = None

    def _client_instance(self):
        if self._client is None:
            import anthropic
            self._client = anthropic.Anthropic(api_key=self.api_key)
        return self._client

    def complete(self, request: LLMRequest) -> LLMResponse:
        """Gọi messages.create; raise lỗi provider cho tầng retries."""
        client = self._client_instance()

        resp = client.messages.create(
            model=request.model,
            max_tokens=request.max_output_tokens,
            temperature=request.temperature,
            system=request.system,
            messages=[{"role": "user", "content": request.user}],
            timeout=request.timeout_seconds,
        )

        text = resp.content[0].text if resp.content else ""
        return LLMResponse(
            text=text,
            model=request.model,
            input_tokens=resp.usage.input_tokens,
            output_tokens=resp.usage.output_tokens,
        )

    def stream_complete(self, request: LLMRequest) -> Iterator[str]:
        """Yield text deltas as they arrive from the model."""
        client = self._client_instance()
        with client.messages.stream(
            model=request.model,
            max_tokens=request.max_output_tokens,
            temperature=request.temperature,
            system=request.system,
            messages=[{"role": "user", "content": request.user}],
            timeout=request.timeout_seconds,
        ) as stream:
            yield from stream.text_stream
