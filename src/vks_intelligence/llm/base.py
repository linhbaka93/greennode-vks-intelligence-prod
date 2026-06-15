"""Interface chung cho mọi model provider.

Một provider nhận LLMRequest và trả LLMResponse kèm token usage, để router và
run_context theo dõi budget bất kể provider nào ở dưới.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Protocol


@dataclass
class LLMRequest:
    model: str
    system: str
    user: str
    max_output_tokens: int = 4_000
    temperature: float = 0.2
    timeout_seconds: int = 60
    response_json: bool = False
    stop: list[str] = field(default_factory=list)


@dataclass
class LLMResponse:
    text: str
    model: str
    input_tokens: int = 0
    output_tokens: int = 0


class LLMProvider(Protocol):
    name: str

    def complete(self, request: LLMRequest) -> LLMResponse:
        """Gọi model một lần; raise lỗi provider để retries/fallback xử lý."""
        ...
