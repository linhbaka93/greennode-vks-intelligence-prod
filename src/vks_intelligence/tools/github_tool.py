"""Đồng bộ và commit workspace/output lên GitHub — versioned memory + audit trail.

Pull memory mới nhất trước khi chạy task; commit output đã publish để lưu vết.
Memory đã approve mới được commit; proposed patch chờ approval.

Khi GITHUB_TOKEN chưa set hoặc GITHUB_REPO rỗng, mọi hàm log warning và trả
chuỗi rỗng — không crash run.
"""

from __future__ import annotations

import logging
from pathlib import Path

log = logging.getLogger(__name__)


def sync_workspace(repo: str, branch: str, token: str, target: Path) -> str:
    """Pull repo về target, trả commit sha hiện tại. No-op nếu thiếu credentials."""
    if not token or not repo:
        log.warning("github_tool.sync_workspace: GITHUB_TOKEN hoặc GITHUB_REPO chưa set — bỏ qua")
        return ""
    try:
        import git
        repo_url = f"https://oauth2:{token}@github.com/{repo}.git"
        if (target / ".git").exists():
            grepo = git.Repo(str(target))
            grepo.remotes.origin.pull(branch)
        else:
            target.mkdir(parents=True, exist_ok=True)
            git.Repo.clone_from(repo_url, str(target), branch=branch, depth=1)
        sha = git.Repo(str(target)).head.commit.hexsha[:8]
        log.info("github_tool: synced %s@%s → %s", repo, branch, sha)
        return sha
    except Exception as exc:
        log.error("github_tool.sync_workspace failed: %s", exc)
        return ""


def commit_output(repo: str, branch: str, token: str, path: str, content: str, message: str) -> str:
    """Commit một file lên GitHub qua API, trả commit sha. No-op nếu thiếu credentials."""
    if not token or not repo:
        log.warning("github_tool.commit_output: GITHUB_TOKEN hoặc GITHUB_REPO chưa set — bỏ qua")
        return ""
    try:
        import base64
        import httpx

        api = f"https://api.github.com/repos/{repo}/contents/{path}"
        headers = {
            "Authorization": f"Bearer {token}",
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
        }

        # Lấy SHA của file nếu đã tồn tại (cần để update)
        existing_sha: str | None = None
        get_resp = httpx.get(f"{api}?ref={branch}", headers=headers, timeout=10)
        if get_resp.status_code == 200:
            existing_sha = get_resp.json().get("sha")

        payload: dict = {
            "message": message,
            "content": base64.b64encode(content.encode()).decode(),
            "branch": branch,
        }
        if existing_sha:
            payload["sha"] = existing_sha

        put_resp = httpx.put(api, headers=headers, json=payload, timeout=15)
        put_resp.raise_for_status()
        sha = put_resp.json().get("commit", {}).get("sha", "")[:8]
        log.info("github_tool: committed %s → %s", path, sha)
        return sha
    except Exception as exc:
        log.error("github_tool.commit_output failed: %s", exc)
        return ""
