from vks_intelligence.contracts import TaskType
from vks_intelligence.llm.base import LLMResponse
from vks_intelligence.orchestrator import route


class FakeRouter:
    def __init__(self, text: str | None = None, raise_exc: bool = False):
        self._text = text
        self._raise = raise_exc

    def complete_once(self, workload, request):
        if self._raise:
            raise RuntimeError("model down")
        return LLMResponse(text=self._text or "", model="fake")


def _kw_intent(q):
    return "current_research"


def _kw_task(q):
    return (TaskType.COMPETITOR_MONITOR, 3)


def _kw_force(q):
    return True


def test_route_falls_back_to_keyword_on_llm_error():
    d = route(
        "câu hỏi",
        FakeRouter(raise_exc=True),
        keyword_intent=_kw_intent,
        keyword_task=_kw_task,
        keyword_force=_kw_force,
    )
    assert d.routed_by == "keyword"
    assert d.intent == "current_research"
    assert d.task_type == TaskType.COMPETITOR_MONITOR
    assert d.force_refresh is True


def test_route_uses_llm_decision():
    text = '{"intent":"current_research","task_type":"battlecard","force_refresh":true,"reasoning":"x"}'
    d = route(
        "mở research battlecard",
        FakeRouter(text=text),
        keyword_intent=lambda q: "memory_lookup",
        keyword_task=lambda q: (TaskType.DAILY_INTELLIGENCE, 1),
        keyword_force=lambda q: False,
    )
    assert d.routed_by == "llm"
    assert d.intent == "current_research"
    assert d.task_type == TaskType.BATTLECARD
    assert d.force_refresh is True


def test_route_invalid_task_type_defaults_daily():
    text = '{"intent":"current_research","task_type":"khong-co-that","force_refresh":false}'
    d = route(
        "câu hỏi",
        FakeRouter(text=text),
        keyword_intent=lambda q: "memory_lookup",
        keyword_task=lambda q: (TaskType.WEEKLY_DIGEST, 7),
        keyword_force=lambda q: False,
    )
    assert d.routed_by == "llm"
    assert d.task_type == TaskType.DAILY_INTELLIGENCE


def test_route_unknown_intent_defaults_memory_lookup():
    text = '{"intent":"linh tinh","task_type":"daily-intelligence"}'
    d = route(
        "câu hỏi",
        FakeRouter(text=text),
        keyword_intent=lambda q: "current_research",
        keyword_task=lambda q: (TaskType.DAILY_INTELLIGENCE, 1),
        keyword_force=lambda q: False,
    )
    assert d.intent == "memory_lookup"
