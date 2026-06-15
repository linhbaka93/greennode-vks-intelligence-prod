"""Format và gửi message Telegram.

Render markdown report sang Telegram HTML để link nguồn gọn, heading dễ scan,
nhưng không compact hoặc bỏ bớt nội dung report.
"""

from __future__ import annotations

import html
import logging
import re
import time
from collections.abc import Iterator
from urllib.parse import urlparse

import httpx

log = logging.getLogger(__name__)

_TG_API = "https://api.telegram.org/bot{token}/{method}"
_RETRY_DELAY = (1, 3)   # giây, 2 lần retry
_MD_LINK_RE = re.compile(r"\[([^\]]+)\]\((https?://[^)\s]+)\)")
_BARE_URL_RE = re.compile(r"(?<![\"'=])(https?://[^\s<>)]+)")
_HEADING_ICONS = {
    "tl;dr": "🎯",
    "key findings": "🔎",
    "tin đã xác nhận": "✅",
    "cần xác minh": "🔍",
    "dự đoán / suy luận": "🧭",
    "rủi ro cần theo dõi": "⚠️",
    "action items": "⚡",
    "phân tích chi tiết": "🧠",
    "sources": "📚",
    "nguồn": "📚",
}


# ──────────────────────────────────────────────────────────────────
# Public API
# ──────────────────────────────────────────────────────────────────

def send_message(
    token: str,
    chat_id: str,
    text: str,
    parse_mode: str = "Markdown",
    reply_to: int | None = None,
    disable_preview: bool = True,
) -> int | None:
    """Gửi một message; trả message_id hoặc None nếu lỗi."""
    payload: dict = {
        "chat_id": chat_id,
        "text": text,
        "parse_mode": parse_mode,
        "disable_web_page_preview": disable_preview,
    }
    if reply_to:
        payload["reply_to_message_id"] = reply_to

    for attempt, delay in enumerate([0, *_RETRY_DELAY]):
        if delay:
            time.sleep(delay)
        try:
            resp = httpx.post(
                _TG_API.format(token=token, method="sendMessage"),
                json=payload,
                timeout=15,
            )
            if resp.status_code == 200:
                return resp.json().get("result", {}).get("message_id")
            if resp.status_code == 400:
                # Bad request — parse_mode issue, thử lại không format
                if attempt == 0 and parse_mode != "":
                    payload["parse_mode"] = ""
                    continue
            log.warning("Telegram sendMessage HTTP %s: %s", resp.status_code, resp.text[:200])
        except httpx.TimeoutException:
            log.warning("Telegram sendMessage timeout (attempt %d)", attempt + 1)
        except Exception as exc:
            log.error("Telegram sendMessage error: %s", exc)
    return None


def edit_message(
    token: str,
    chat_id: str,
    message_id: int,
    text: str,
    parse_mode: str = "",
) -> bool:
    """Edit a bot-sent message in-place. Returns True on success."""
    payload: dict = {
        "chat_id": chat_id,
        "message_id": message_id,
        "text": text,
        "disable_web_page_preview": True,
    }
    if parse_mode:
        payload["parse_mode"] = parse_mode
    try:
        resp = httpx.post(
            _TG_API.format(token=token, method="editMessageText"),
            json=payload,
            timeout=10,
        )
        return resp.status_code == 200
    except Exception as exc:
        log.warning("Telegram editMessage error: %s", exc)
        return False


def stream_and_edit_message(
    token: str,
    chat_id: str,
    text_iter: Iterator[str],
    reply_to: int | None = None,
    edit_interval_chars: int = 200,
    edit_interval_secs: float = 0.8,
) -> tuple[str, int | None]:
    """Stream LLM text chunks hiển thị dần trong Telegram qua editMessage.

    Gửi placeholder "⏳", sau đó edit message mỗi ~edit_interval_chars ký tự hoặc
    ~edit_interval_secs giây. Trả (accumulated_text, message_id) để caller có thể
    thực hiện final edit với HTML đã format đầy đủ.
    """
    placeholder_id = send_message(token, chat_id, "⏳", reply_to=reply_to, parse_mode="")
    accumulated = ""
    last_edit_len = 0
    last_edit_time = time.monotonic()

    for chunk in text_iter:
        accumulated += chunk
        now = time.monotonic()
        chars_since = len(accumulated) - last_edit_len
        time_since = now - last_edit_time
        if (chars_since >= edit_interval_chars or time_since >= edit_interval_secs) and accumulated.strip():
            if placeholder_id:
                edit_message(token, chat_id, placeholder_id, accumulated[:3900])
            last_edit_len = len(accumulated)
            last_edit_time = now

    return accumulated, placeholder_id


def send_action(token: str, chat_id: str, action: str = "typing") -> None:
    """Best-effort typing indicator — không raise."""
    try:
        httpx.post(
            _TG_API.format(token=token, method="sendChatAction"),
            json={"chat_id": chat_id, "action": action},
            timeout=5,
        )
    except Exception:
        pass


def markdown_to_telegram_html(markdown: str) -> str:
    """Convert a safe markdown subset to Telegram HTML with compact source links."""
    placeholders: list[str] = []

    def keep(value: str) -> str:
        placeholders.append(value)
        return f"@@TGHTML{len(placeholders) - 1}@@"

    text = html.escape(markdown, quote=False)

    def link_repl(match: re.Match[str]) -> str:
        label = html.escape(match.group(1).strip(), quote=False)
        url = html.escape(match.group(2).strip(), quote=True)
        return keep(f'<a href="{url}">{label}</a>')

    text = _MD_LINK_RE.sub(link_repl, text)

    def bare_url_repl(match: re.Match[str]) -> str:
        url = match.group(1).rstrip(".,;:")
        suffix = match.group(1)[len(url):]
        host = urlparse(url).netloc.replace("www.", "") or "source"
        link = keep(f'<a href="{html.escape(url, quote=True)}">{html.escape(host)}</a>')
        return link + suffix

    text = _BARE_URL_RE.sub(bare_url_repl, text)

    def heading_repl(match: re.Match[str]) -> str:
        marks = match.group(1)
        title = match.group(2).strip()
        icon = _HEADING_ICONS.get(title.lower(), "📌" if len(marks) == 1 else "▪️")
        prefix = "" if len(marks) == 1 else "\n"
        return f"{prefix}<b>{icon} {title}</b>"

    text = re.sub(r"^(#{1,6})\s+(.+)$", heading_repl, text, flags=re.MULTILINE)
    text = re.sub(r"\*\*([^*\n]+)\*\*", r"<b>\1</b>", text)
    text = re.sub(r"`([^`\n]+)`", r"<code>\1</code>", text)
    text = re.sub(r"(?<!\*)_([^_\n]+)_(?!_)", r"<i>\1</i>", text)
    text = re.sub(r"^\s*[-*]\s+", "• ", text, flags=re.MULTILINE)

    for idx, value in enumerate(placeholders):
        text = text.replace(f"@@TGHTML{idx}@@", value)
    return text


def _split_long_line(markdown_line: str, max_chars: int) -> list[str]:
    chunks: list[str] = []
    remaining = markdown_line
    while remaining:
        step = min(len(remaining), max(1, max_chars - 200))
        while step > 1 and len(markdown_to_telegram_html(remaining[:step])) > max_chars:
            step = max(1, step // 2)
        chunks.append(remaining[:step])
        remaining = remaining[step:]
    return chunks


def format_digest(markdown: str, header: str, footer: str, max_chars: int) -> list[str]:
    """Tách digest thành danh sách message, mỗi cái <= max_chars."""
    full = f"{header}\n\n{markdown}\n\n{footer}" if header or footer else markdown
    if len(full) <= max_chars:
        return [full]

    # Split theo section (## heading) khi vượt giới hạn
    parts: list[str] = []
    current: list[str] = []
    current_len = 0

    for line in full.splitlines(keepends=True):
        line_len = len(line)
        if line_len > max_chars:
            if current:
                parts.append("".join(current).rstrip())
                current = []
                current_len = 0
            for i in range(0, line_len, max_chars):
                parts.append(line[i : i + max_chars].rstrip())
            continue
        if current_len + line_len > max_chars and current:
            parts.append("".join(current).rstrip())
            current = []
            current_len = 0
        current.append(line)
        current_len += line_len

    if current:
        parts.append("".join(current).rstrip())

    return [p for p in parts if p.strip()]


def format_telegram_html_messages(markdown: str, max_chars: int) -> list[str]:
    """Render full markdown to Telegram HTML chunks without dropping content."""
    chunks: list[str] = []
    current: list[str] = []

    def render(lines: list[str]) -> str:
        return markdown_to_telegram_html("".join(lines).strip())

    def flush() -> None:
        if not current:
            return
        rendered = render(current)
        if rendered:
            chunks.append(rendered)
        current.clear()

    for line in markdown.splitlines(keepends=True):
        if len(markdown_to_telegram_html(line)) > max_chars:
            flush()
            chunks.extend(markdown_to_telegram_html(part) for part in _split_long_line(line, max_chars))
            continue

        candidate = [*current, line]
        if len(render(candidate)) <= max_chars:
            current.append(line)
        else:
            flush()
            current.append(line)

    flush()
    return chunks or [""]


def send(messages: list[str], chat_id: str, bot_token: str) -> list[int]:
    """Gửi lần lượt các message, retry khi lỗi, trả danh sách message_id."""
    sent: list[int] = []
    for msg in messages:
        mid = send_message(bot_token, chat_id, msg)
        if mid:
            sent.append(mid)
        else:
            log.error("Gửi message thất bại sau retry — chat_id=%s preview=%s", chat_id, msg[:60])
    return sent
