"""HEAD-check URLs trong synthesis output để phát hiện dead links.

Chạy song song (ThreadPoolExecutor) vì HEAD requests là I/O-bound.
Mặc định timeout 5s/URL; lỗi mạng không tính là dead (benefit of doubt).
Enabled/disabled qua config.citation_grader_enabled.
"""

from __future__ import annotations

import re
from concurrent.futures import ThreadPoolExecutor, as_completed

import httpx

_URL_RE = re.compile(r"https?://[^\s)\]>\"]+")
_MAX_WORKERS = 4
_DEFAULT_TIMEOUT = 5.0


def grade_citations(markdown: str, timeout: float = _DEFAULT_TIMEOUT) -> list[str]:
    """HEAD-check mọi URL trong markdown. Trả danh sách dead URLs (HTTP 4xx)."""
    urls = list(dict.fromkeys(_URL_RE.findall(markdown)))
    if not urls:
        return []

    dead: list[str] = []
    with ThreadPoolExecutor(max_workers=_MAX_WORKERS) as pool:
        futures = {pool.submit(_head_check, url, timeout): url for url in urls}
        for fut in as_completed(futures):
            url = futures[fut]
            try:
                alive = fut.result()
            except Exception:
                alive = True  # lỗi mạng → benefit of doubt, không đánh dấu dead
            if not alive:
                dead.append(url)
    return dead


def _head_check(url: str, timeout: float) -> bool:
    """Trả True nếu URL trả 2xx/3xx. False nếu 4xx. Exception → caller xử lý."""
    try:
        with httpx.Client(timeout=timeout, follow_redirects=True) as client:
            resp = client.head(url)
            return resp.status_code < 400
    except httpx.TimeoutException:
        return True  # timeout không có nghĩa là dead
    except Exception:
        return True  # DNS/connect error → không penalize
