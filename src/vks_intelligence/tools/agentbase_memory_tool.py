"""AgentBase Conversation Memory — lưu và recall hội thoại theo actor/session.

Tách biệt hoàn toàn khỏi workspace memory (memory/ folder):
  - Workspace memory: tri thức validate đọc từ file
  - Conversation memory: fact per-user từ lịch sử Q&A qua Memory Service

actor_id  = Telegram user_id hoặc chat_id (không để LLM tự quyết)
session_id = "tg-{chat_id}-{YYYY-MM-DD}" (session theo ngày)

Auto-disabled nếu GREENNODE credentials không có (local dev) hoặc MEMORY_ID chưa set.
"""

from __future__ import annotations

import logging
import os
import time
from functools import lru_cache
from urllib.parse import quote

log = logging.getLogger(__name__)

_MEM_API = "https://agentbase.api.vngcloud.vn/memory"
_TOKEN_CACHE: dict[str, str | float] = {"token": "", "expires_at": 0.0}


# ──────────────────────────────────────────────────────────────────
# Token helper — dùng IAM credentials (auto-injected trên runtime)
# ──────────────────────────────────────────────────────────────────

def _get_token() -> str | None:
    """Lấy IAM bearer token. Trả None nếu thiếu credentials."""
    client_id = os.environ.get("GREENNODE_CLIENT_ID", "")
    client_secret = os.environ.get("GREENNODE_CLIENT_SECRET", "")
    if not client_id or not client_secret:
        return None
    cached_token = str(_TOKEN_CACHE.get("token", ""))
    expires_at = float(_TOKEN_CACHE.get("expires_at", 0.0))
    if cached_token and expires_at - 30 > time.time():
        return cached_token
    try:
        import base64
        import httpx
        creds = base64.b64encode(f"{client_id}:{client_secret}".encode()).decode()
        resp = httpx.post(
            "https://iam.api.vngcloud.vn/accounts-api/v2/auth/token",
            headers={"Authorization": f"Basic {creds}", "Content-Type": "application/x-www-form-urlencoded"},
            data="grant_type=client_credentials",
            timeout=10,
        )
        resp.raise_for_status()
        payload = resp.json()
        token = payload.get("access_token")
        if token:
            expires_in = float(payload.get("expires_in", 300))
            _TOKEN_CACHE["token"] = token
            _TOKEN_CACHE["expires_at"] = time.time() + expires_in
        return token
    except Exception as exc:
        log.debug("AgentBase token fetch failed: %s", exc)
        return None


# ──────────────────────────────────────────────────────────────────
# Main tool class
# ──────────────────────────────────────────────────────────────────

class AgentBaseMemoryTool:
    """Wrapper nhẹ quanh Memory Service REST API."""

    def __init__(self, memory_id: str, semantic_strategy_id: str, custom_strategy_id: str) -> None:
        self.memory_id = memory_id
        self.semantic_strategy_id = semantic_strategy_id
        self.custom_strategy_id = custom_strategy_id

    def is_enabled(self) -> bool:
        return bool(
            self.memory_id
            and os.environ.get("GREENNODE_CLIENT_ID")
            and os.environ.get("GREENNODE_CLIENT_SECRET")
        )

    # ──────────────────────────────────────────────────────
    # Event operations
    # ──────────────────────────────────────────────────────

    def save_event(
        self,
        actor_id: str,
        session_id: str,
        role: str,
        message: str,
    ) -> str | None:
        """Lưu một turn hội thoại; trả event_id hoặc None nếu lỗi."""
        if not self.is_enabled() or not actor_id:
            return None
        token = _get_token()
        if not token:
            return None
        try:
            import httpx
            actor = quote(actor_id, safe="")
            session = quote(session_id, safe="")
            url = f"{_MEM_API}/memories/{self.memory_id}/actors/{actor}/sessions/{session}/events"
            resp = httpx.post(
                url,
                json={"payload": {"type": "conversational", "role": role, "message": message[:4000]}},
                headers={"Authorization": f"Bearer {token}"},
                timeout=8,
            )
            if resp.status_code in (200, 201):
                return resp.json().get("id")
            log.debug("save_event HTTP %s: %s", resp.status_code, resp.text[:200])
        except Exception as exc:
            log.debug("save_event failed: %s", exc)
        return None

    # ──────────────────────────────────────────────────────
    # Search memory records (semantic similarity)
    # ──────────────────────────────────────────────────────

    def search_user_memory(
        self,
        actor_id: str,
        query: str,
        limit: int = 5,
        score_threshold: float = 0.5,
    ) -> list[str]:
        """Semantic search fact của actor; trả list text snippet."""
        if not self.is_enabled() or not actor_id:
            return []
        token = _get_token()
        if not token:
            return []
        results: list[str] = []
        for strategy_id in (self.semantic_strategy_id, self.custom_strategy_id):
            if not strategy_id:
                continue
            namespace = f"/strategies/{strategy_id}/actors/{actor_id}"
            try:
                import httpx
                url = f"{_MEM_API}/memories/{self.memory_id}/memory-records:search"
                resp = httpx.post(
                    url,
                    params={"namespace": namespace},
                    json={"query": query, "limit": limit, "scoreThreshold": score_threshold},
                    headers={"Authorization": f"Bearer {token}"},
                    timeout=8,
                )
                if resp.status_code == 200:
                    for rec in resp.json():
                        mem_text = rec.get("memory", "")
                        if mem_text and mem_text not in results:
                            results.append(mem_text)
            except Exception as exc:
                log.debug("search_user_memory strategy=%s failed: %s", strategy_id, exc)
        return results[:limit]

    # ──────────────────────────────────────────────────────
    # Generate memory records từ session (async trên platform)
    # ──────────────────────────────────────────────────────

    def generate_records(self, actor_id: str, session_id: str) -> None:
        """Trigger fact extraction từ session (best-effort, không block)."""
        if not self.is_enabled() or not actor_id:
            return
        token = _get_token()
        if not token:
            return
        for strategy_id in (self.semantic_strategy_id, self.custom_strategy_id):
            if not strategy_id:
                continue
            try:
                import httpx
                url = f"{_MEM_API}/memories/{self.memory_id}/memory-records:generate-from-session"
                httpx.post(
                    url,
                    params={
                        "actorId": actor_id,
                        "sessionId": session_id,
                        "longTermMemoryStrategyId": strategy_id,
                    },
                    headers={"Authorization": f"Bearer {token}"},
                    timeout=5,
                )
            except Exception as exc:
                log.debug("generate_records strategy=%s failed: %s", strategy_id, exc)


# ──────────────────────────────────────────────────────────────────
# Singleton factory — lazy init từ Settings
# ──────────────────────────────────────────────────────────────────

@lru_cache(maxsize=1)
def get_memory_tool() -> AgentBaseMemoryTool:
    memory_id = os.environ.get("MEMORY_ID", "")
    semantic_id = os.environ.get("MEMORY_STRATEGY_SEMANTIC_ID", "")
    custom_id = os.environ.get("MEMORY_STRATEGY_CUSTOM_ID", "")
    return AgentBaseMemoryTool(memory_id, semantic_id, custom_id)
