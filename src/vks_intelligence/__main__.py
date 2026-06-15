"""Entry point: `python -m vks_intelligence` hoặc console script `vks-intelligence`."""

from __future__ import annotations


def main() -> None:
    """Khởi động AgentBase runtime (/health, /invocations) và serve HTTP."""
    from vks_intelligence.platform import run
    run()


if __name__ == "__main__":
    main()
