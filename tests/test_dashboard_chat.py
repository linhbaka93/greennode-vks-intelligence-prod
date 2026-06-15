import json

from fastapi.testclient import TestClient

from vks_intelligence.api import app


def test_dashboard_chat_streams_sse(monkeypatch, tmp_path):
    from vks_intelligence.config import Settings

    s = Settings(_env_file=None, workspace_path=tmp_path)
    monkeypatch.setattr("vks_intelligence.config.get_settings", lambda: s)

    def fake_stream(self, question, session_history=""):
        assert question == "VKS là gì?"
        yield "VKS là "
        yield "managed Kubernetes."

    monkeypatch.setattr(
        "vks_intelligence.specialists.qa_agent.QAAgent.stream_answer_text", fake_stream
    )

    client = TestClient(app)
    resp = client.post(
        "/dashboard/chat",
        json={"message": "VKS là gì?", "history": [{"role": "user", "text": "hi"}]},
    )

    assert resp.status_code == 200
    assert resp.headers["content-type"].startswith("text/event-stream")
    events = [
        json.loads(line[6:])
        for line in resp.text.split("\n")
        if line.startswith("data: ")
    ]
    deltas = "".join(e.get("delta", "") for e in events)
    assert deltas == "VKS là managed Kubernetes."
    assert events[-1] == {"done": True}


def test_dashboard_chat_rejects_empty_message():
    client = TestClient(app)
    resp = client.post("/dashboard/chat", json={"message": "   "})
    assert resp.status_code == 422
