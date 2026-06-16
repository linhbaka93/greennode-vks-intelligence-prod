"""Provider cho endpoint OpenAI-compatible (VNG AI Platform) — Gemma/Qwen/MiniMax.

Dùng `openai` client trỏ base_url về AI Platform. Map LLMRequest sang
chat.completions và trích token usage từ response.usage.

Xử lý thinking models:
- Qwen3 (qwen/qwen3-*): disable thinking qua chat_template_kwargs → content bình thường
- MiniMax (minimax/*): strip <think>...</think> khỏi content
- Gemma (google/gemma-*): chuẩn, không cần xử lý thêm
"""

from __future__ import annotations

import re
from collections.abc import Iterator

from vks_intelligence.llm.base import LLMRequest, LLMResponse

# Regex strip <think>...</think> blocks (MiniMax reasoning traces)
_THINK_RE = re.compile(r"<think>.*?</think>\s*", re.DOTALL)


def _strip_thinking(text: str) -> str:
    return _THINK_RE.sub("", text).strip()


def _extra_body(model: str) -> dict | None:
    """Qwen3 thinking models cần disable thinking để content không bị null."""
    if "qwen3" in model.lower():
        return {"chat_template_kwargs": {"enable_thinking": False}}
    return None


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
        extra = _extra_body(request.model)
        if extra:
            kwargs["extra_body"] = extra

        resp = client.chat.completions.create(**kwargs)
        msg = resp.choices[0].message
        # content=None xảy ra khi thinking model trả reasoning field thay vì content
        content = msg.content or getattr(msg, "reasoning", None) or ""
        text = _strip_thinking(content)
        usage = resp.usage

        return LLMResponse(
            text=text,
            model=request.model,
            input_tokens=usage.prompt_tokens if usage else 0,
            output_tokens=usage.completion_tokens if usage else 0,
        )

    def stream_complete(self, request: LLMRequest) -> Iterator[str]:
        """Yield text deltas as they arrive; không hỗ trợ response_json mode.

        Thinking models không nên dùng với stream_complete (QA path dùng gemma).
        Nếu gặp <think> delta thì skip cho đến khi gặp </think>.
        """
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
        extra = _extra_body(request.model)
        if extra:
            kwargs["extra_body"] = extra

        in_think = False
        buf = ""
        for chunk in client.chat.completions.create(**kwargs):
            if not (chunk.choices and chunk.choices[0].delta.content):
                continue
            delta = chunk.choices[0].delta.content
            buf += delta
            # Drain buffer yielding only content outside <think> blocks
            while True:
                if in_think:
                    end = buf.find("</think>")
                    if end == -1:
                        buf = ""
                        break
                    buf = buf[end + len("</think>"):].lstrip()
                    in_think = False
                else:
                    start = buf.find("<think>")
                    if start == -1:
                        yield buf
                        buf = ""
                        break
                    if start > 0:
                        yield buf[:start]
                    buf = buf[start + len("<think>"):]
                    in_think = True
