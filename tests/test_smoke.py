"""Smoke test: vỏ project import sạch và contract/budget/route nhất quán."""

import importlib
import pkgutil

import vks_intelligence as pkg


def test_all_modules_import():
    for module in pkgutil.walk_packages(pkg.__path__, pkg.__name__ + "."):
        importlib.import_module(module.name)


def test_budget_table_covers_all_task_types():
    from vks_intelligence.contracts import TaskType
    from vks_intelligence.llm.budgets import budget_for

    for task_type in TaskType:
        assert budget_for(task_type).max_agents >= 1


def test_api_routes_registered():
    from vks_intelligence.api import app

    paths = {getattr(r, "path", "") for r in app.routes}
    for path in (
        "/health",
        "/tasks/qa",
        "/tasks/daily-intelligence",
        "/tasks/weekly-digest",
        "/tasks/monthly-brief",
        "/tasks/competitor-monitor",
        "/tasks/pricing-analysis",
        "/tasks/battlecard",
        "/tasks/memory-maintenance",
        "/dashboard/summary",
        "/runtime/info",
    ):
        assert path in paths


def test_settings_defaults():
    from vks_intelligence.config import get_settings

    settings = get_settings()
    assert settings.model_qa
    assert settings.quality_min_score_publish > settings.quality_min_score_approval
    assert hasattr(settings, "app_build_tag")


def test_runtime_info_has_non_secret_build_metadata():
    from vks_intelligence.api import _runtime_info

    info = _runtime_info()

    assert "build_image" in info
    assert "build_tag" in info
    assert "optimizer" in info
    assert info["features"]["artifact_fast_path"] is True
