"""SSE contract regression test for /api/chat.

This script runs an in-process test against FastAPI app with mocked runtime
components so it does not require Ollama/qwen-agent/network access.

Checks:
- Streams `content` and `thinking` events
- Streams `tool_call` and `tool_result` events
- `done` includes `searches_done` and tool counters
- Search tool invocation increments `searches_done`

Run:
    python scripts/test_sse_contract.py
"""

from __future__ import annotations

import json
import os
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))


os.environ.setdefault("JWT_SECRET", "dev-test-secret")
os.environ.setdefault("ADMIN_USERNAME", "admin")
os.environ.setdefault("ADMIN_PASSWORD", "password123")

import server  # noqa: E402
from fastapi.testclient import TestClient  # noqa: E402


class _FakeCursor:
    async def fetchone(self) -> dict[str, Any]:
        return {"id": "conv-1"}


class _FakeDB:
    async def execute(self, _query: str, _params: tuple[Any, ...] | None = None) -> _FakeCursor:
        return _FakeCursor()

    async def close(self) -> None:
        return None


class _FakeAssistant:
    def __init__(self, function_list: list[Any], llm: Any, system_message: str):
        self.function_list = function_list
        self.llm = llm
        self.system_message = system_message

    def run(self, messages: list[dict[str, Any]], lang: str = "en"):
        _ = (messages, lang)
        yield [
            {
                "role": "assistant",
                "reasoning_content": "Thinking about searching.",
                "tool_calls": [
                    {
                        "id": "call_1",
                        "type": "function",
                        "function": {
                            "name": "web_search",
                            "arguments": json.dumps({"query": "sse contract"}),
                        },
                    }
                ],
            }
        ]
        yield [
            {
                "role": "function",
                "name": "web_search",
                "content": "Web search results for 'sse contract':\n1. Example",
            }
        ]
        yield [
            {
                "role": "assistant",
                "content": "Final answer based on tool result.",
            }
        ]


def _fake_get_chat_model(_cfg: dict[str, Any]) -> object:
    return object()


async def _fake_get_db() -> _FakeDB:
    return _FakeDB()


async def _fake_build_active_context(_db: _FakeDB, _conversation_id: str, _message: str):
    return [], False


async def _fake_fts_search(_db: _FakeDB, _conversation_id: str, _query: str, _user_id: str):
    return []


async def _fake_save_messages(_db: _FakeDB, _conversation_id: str, _user_message: str, _assistant_content: str, _assistant_thinking: str):
    return None


async def _fake_current_user() -> dict[str, Any]:
    return {
        "id": "user-1",
        "username": "tester",
        "role": "admin",
        "is_active": 1,
        "file_tools_enabled": 1,
        "workspace_root": ".",
        "persona_prompt": "",
        "mcp_config": "",
        "created_at": "2026-03-21T00:00:00Z",
    }


def main() -> None:
    original = {
        "QWEN_AGENT_RUNTIME_AVAILABLE": server.QWEN_AGENT_RUNTIME_AVAILABLE,
        "Assistant": getattr(server, "Assistant", None),
        "get_chat_model": getattr(server, "get_chat_model", None),
        "ensure_ollama_running": server.ensure_ollama_running,
        "get_db": server.get_db,
        "build_active_context": server.build_active_context,
        "fts_search": server.fts_search,
        "save_messages": server.save_messages,
        "get_global_tool_toggles": server.get_global_tool_toggles,
        "dependency_overrides": dict(server.app.dependency_overrides),
    }

    async def _fake_ensure_ollama_running(wait_seconds: int = 8) -> bool:  # noqa: ARG001
        return True

    try:
        server.QWEN_AGENT_RUNTIME_AVAILABLE = True
        server.Assistant = _FakeAssistant
        server.get_chat_model = _fake_get_chat_model
        server.ensure_ollama_running = _fake_ensure_ollama_running
        server.get_db = _fake_get_db
        server.build_active_context = _fake_build_active_context
        server.fts_search = _fake_fts_search
        server.save_messages = _fake_save_messages
        server.get_global_tool_toggles = lambda: {
            "use_gml_docs": False,
            "use_ps_docs": False,
            "use_file_tools": False,
            "use_code_interpreter": False,
            "use_mcp_tools": False,
            "use_raw_api": True,
        }
        server.app.dependency_overrides[server.get_current_user] = _fake_current_user

        client = TestClient(server.app)
        response = client.post(
            "/api/chat",
            json={
                "conversation_id": "conv-1",
                "message": "Please search and summarize",
                "model": "qwen3-coder:30b",
                "think": True,
                "use_search": True,
                "use_gml_docs": False,
                "use_ps_docs": False,
                "use_file_tools": False,
                "use_code_interpreter": False,
                "use_mcp_tools": False,
                "working_subdir": "",
            },
        )

        assert response.status_code == 200, response.text

        events: list[dict[str, Any]] = []
        for line in response.text.splitlines():
            if not line.startswith("data: "):
                continue
            payload = line[len("data: ") :].strip()
            if not payload:
                continue
            events.append(json.loads(payload))

        event_types = [evt.get("type") for evt in events]

        assert "thinking" in event_types, f"missing thinking event: {event_types}"
        assert "content" in event_types, f"missing content event: {event_types}"
        assert "tool_call" in event_types, f"missing tool_call event: {event_types}"
        assert "tool_result" in event_types, f"missing tool_result event: {event_types}"
        assert "done" in event_types, f"missing done event: {event_types}"

        done_event = next(evt for evt in events if evt.get("type") == "done")
        assert isinstance(done_event.get("searches_done"), int), done_event
        assert done_event.get("searches_done", 0) >= 1, done_event
        assert done_event.get("tools_called", 0) >= 1, done_event

        print("PASS: SSE contract includes tool_call/tool_result and done.searches_done")

    finally:
        server.QWEN_AGENT_RUNTIME_AVAILABLE = original["QWEN_AGENT_RUNTIME_AVAILABLE"]
        server.Assistant = original["Assistant"]
        server.get_chat_model = original["get_chat_model"]
        server.ensure_ollama_running = original["ensure_ollama_running"]
        server.get_db = original["get_db"]
        server.build_active_context = original["build_active_context"]
        server.fts_search = original["fts_search"]
        server.save_messages = original["save_messages"]
        server.get_global_tool_toggles = original["get_global_tool_toggles"]
        server.app.dependency_overrides = original["dependency_overrides"]


if __name__ == "__main__":
    main()
