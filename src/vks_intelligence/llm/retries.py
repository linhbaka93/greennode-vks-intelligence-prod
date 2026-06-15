"""Retry có chọn lọc cho model call.

Chỉ retry lỗi tạm thời: HTTP transient, provider timeout, rate limit, JSON hỏng
khi text thô vẫn dùng được. Không retry lỗi prompt sai, thiếu input, hay
validation fail từ quality critic.
"""

from __future__ import annotations

import time
from collections.abc import Callable

from vks_intelligence.llm.base import LLMResponse

RETRYABLE_HINTS = ("timeout", "rate limit", "429", "503", "connection")


def is_retryable(error: Exception) -> bool:
    msg = str(error).lower()
    return any(hint in msg for hint in RETRYABLE_HINTS)


def with_retry(call: Callable[[], LLMResponse], max_retries: int) -> LLMResponse:
    last_exc: Exception = RuntimeError("no attempt made")
    for attempt in range(max_retries + 1):
        try:
            return call()
        except Exception as exc:
            last_exc = exc
            if not is_retryable(exc) or attempt == max_retries:
                raise
            time.sleep(2**attempt)
    raise last_exc  # unreachable
