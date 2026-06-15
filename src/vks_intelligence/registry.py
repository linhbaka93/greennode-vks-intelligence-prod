"""Đăng ký specialist agent theo tên để supervisor tra cứu.

Mỗi specialist tự đăng ký một lần lúc import. Supervisor lấy class theo tên khi
dựng plan, không import trực tiếp từng agent.
"""

from __future__ import annotations

from typing import Any

_REGISTRY: dict[str, type[Any]] = {}


def register(name: str):
    """Decorator gắn một Specialist class vào registry dưới `name`."""
    def decorator(cls):
        _REGISTRY[name] = cls
        return cls
    return decorator


def get(name: str) -> type[Any]:
    """Lấy class specialist theo tên; raise KeyError nếu chưa đăng ký."""
    if name not in _REGISTRY:
        raise KeyError(
            f"Specialist '{name}' chưa đăng ký. Có sẵn: {available()}"
        )
    return _REGISTRY[name]


def available() -> list[str]:
    return list(_REGISTRY.keys())
