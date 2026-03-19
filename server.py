"""
Ollama Qwen3 Frontend - FastAPI backend
Serves the HTML frontend and proxies chat requests to Ollama,
with SQLite memory + FTS5 context retrieval.
"""

import asyncio
import json
import logging
import os
import re
import shutil
import subprocess
import uuid
from datetime import datetime, timezone
from pathlib import Path
from typing import AsyncGenerator

from dotenv import load_dotenv

load_dotenv(Path(__file__).parent / ".env")

import aiohttp
import aiosqlite
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse, StreamingResponse
from pydantic import BaseModel

# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------
OLLAMA_URL        = "http://localhost:11434/api/chat"
OLLAMA_HEALTH_URL = "http://127.0.0.1:11434/api/tags"
BRAVE_SEARCH_URL  = "https://api.search.brave.com/res/v1/web/search"
DEFAULT_MODEL     = "huihui_ai/qwen3-abliterated:8b"
DB_PATH           = Path(__file__).parent / "memory.db"
HTML_PATH         = Path(__file__).parent / "index.html"
CONFIG_PATH       = Path(__file__).parent / "config.json"
TOKEN_CAP              = 20_000  # max tokens kept in active context
FTS_RESULT_LIMIT       = 3       # past-memory snippets to inject when truncated
TOKEN_ESTIMATE_DIVISOR = 4       # chars / 4 ≈ tokens
MAX_SEARCH_ITERATIONS  = 3       # max Brave searches per response
BRAVE_SEARCH_COUNT     = 5       # results to fetch per query

SEARCH_TAG_RE = re.compile(r'<search>(.*?)</search>', re.IGNORECASE | re.DOTALL)

SEARCH_SYSTEM_PROMPT = (
    "You have access to a live web search tool. "
    "When you need current information, specific facts, recent events, or anything you are uncertain about, "
    "request a search using this exact format on its own line:\n\n"
    "<search>your search query here</search>\n\n"
    "You will receive the search results and should then provide a complete, accurate answer. "
    "You may search up to 3 times per response. Only search when genuinely needed."
)

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
log = logging.getLogger(__name__)

app = FastAPI(title="Ollama Qwen3 Chat")
_ollama_start_lock = asyncio.Lock()

# ---------------------------------------------------------------------------
# Database
# ---------------------------------------------------------------------------

_DDL_STATEMENTS = [
    "PRAGMA journal_mode=WAL",
    """
    CREATE TABLE IF NOT EXISTS conversations (
        id         TEXT PRIMARY KEY,
        title      TEXT NOT NULL DEFAULT 'New Chat',
        created_at TEXT NOT NULL
    )
    """,
    """
    CREATE TABLE IF NOT EXISTS messages (
        id              INTEGER PRIMARY KEY AUTOINCREMENT,
        conversation_id TEXT    NOT NULL REFERENCES conversations(id) ON DELETE CASCADE,
        role            TEXT    NOT NULL,
        content         TEXT    NOT NULL DEFAULT '',
        thinking        TEXT    NOT NULL DEFAULT '',
        token_count     INTEGER NOT NULL DEFAULT 0,
        created_at      TEXT    NOT NULL
    )
    """,
    "CREATE INDEX IF NOT EXISTS idx_messages_conv ON messages(conversation_id, id)",
    """
    CREATE VIRTUAL TABLE IF NOT EXISTS messages_fts USING fts5(
        content,
        message_id UNINDEXED,
        conversation_id UNINDEXED
    )
    """,
    """
    CREATE TRIGGER IF NOT EXISTS messages_fts_insert
    AFTER INSERT ON messages
    BEGIN
        INSERT INTO messages_fts(content, message_id, conversation_id)
        VALUES (NEW.content, NEW.id, NEW.conversation_id);
    END
    """,
    """
    CREATE TRIGGER IF NOT EXISTS messages_fts_delete
    AFTER DELETE ON messages
    BEGIN
        DELETE FROM messages_fts WHERE message_id = OLD.id;
    END
    """,
]


async def get_db() -> aiosqlite.Connection:
    """Return a connected database connection (row_factory set)."""
    db = await aiosqlite.connect(DB_PATH)
    db.row_factory = aiosqlite.Row
    await db.execute("PRAGMA foreign_keys = ON")
    return db


async def is_ollama_running(timeout_seconds: float = 1.5) -> bool:
    """Return True when Ollama responds on port 11434."""
    try:
        timeout = aiohttp.ClientTimeout(total=timeout_seconds)
        async with aiohttp.ClientSession(timeout=timeout) as session:
            async with session.get(OLLAMA_HEALTH_URL) as resp:
                return resp.status == 200
    except Exception:
        return False


def start_ollama_service() -> bool:
    """Try to launch `ollama serve` in a detached process."""
    ollama_bin = shutil.which("ollama")
    if not ollama_bin:
        log.warning("Ollama binary not found in PATH; cannot auto-start service.")
        return False

    popen_kwargs = {
        "stdout": subprocess.DEVNULL,
        "stderr": subprocess.DEVNULL,
    }
    if os.name == "nt":
        popen_kwargs["creationflags"] = (
            getattr(subprocess, "DETACHED_PROCESS", 0)
            | getattr(subprocess, "CREATE_NEW_PROCESS_GROUP", 0)
        )
    else:
        popen_kwargs["start_new_session"] = True

    try:
        subprocess.Popen([ollama_bin, "serve"], **popen_kwargs)
        log.info("Attempted to start Ollama service: %s serve", ollama_bin)
        return True
    except Exception as exc:
        log.warning("Failed to start Ollama automatically: %s", exc)
        return False


async def ensure_ollama_running(wait_seconds: int = 8) -> bool:
    """Ensure Ollama is reachable; auto-start it when missing."""
    if await is_ollama_running():
        return True

    async with _ollama_start_lock:
        if await is_ollama_running():
            return True

        log.warning("No service detected on port 11434. Attempting to start Ollama.")
        if not start_ollama_service():
            return False

        for _ in range(wait_seconds):
            await asyncio.sleep(1)
            if await is_ollama_running():
                log.info("Ollama became available on port 11434.")
                return True

        log.warning("Ollama did not become ready after %s seconds.", wait_seconds)
        return False


@app.on_event("startup")
async def startup():
    if not await ensure_ollama_running():
        log.warning("Continuing startup without Ollama; /api/chat will retry auto-start.")

    db = await get_db()
    try:
        for stmt in _DDL_STATEMENTS:
            await db.execute(stmt.strip())
        await db.commit()
    finally:
        await db.close()
    log.info("Database initialised at %s", DB_PATH)


# ---------------------------------------------------------------------------
# Pydantic models
# ---------------------------------------------------------------------------

class ConversationCreate(BaseModel):
    title: str = "New Chat"


class ConversationRename(BaseModel):
    title: str


class ChatRequest(BaseModel):
    conversation_id: str
    message: str
    model: str = DEFAULT_MODEL
    think: bool = True
    use_search: bool = True


class SettingsUpdate(BaseModel):
    brave_api_key: str = ""


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def estimate_tokens(text: str) -> int:
    return max(1, len(text) // TOKEN_ESTIMATE_DIVISOR)


def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def normalize_model_name(model: str) -> str:
    """Normalise known model aliases to explicit Ollama tags."""
    cleaned = (model or "").strip()
    if not cleaned:
        return DEFAULT_MODEL
    if cleaned == "huihui_ai/qwen3-abliterated":
        return DEFAULT_MODEL
    return cleaned


# ---------------------------------------------------------------------------
# Config helpers
# ---------------------------------------------------------------------------

def load_config() -> dict:
    if CONFIG_PATH.exists():
        try:
            return json.loads(CONFIG_PATH.read_text(encoding="utf-8"))
        except Exception:
            pass
    return {}


def save_config(data: dict) -> None:
    CONFIG_PATH.write_text(json.dumps(data, indent=2), encoding="utf-8")


def get_brave_api_key() -> str:
    """Return Brave API key from env var or config.json (env takes priority)."""
    return os.environ.get("BRAVE_API_KEY") or load_config().get("brave_api_key", "")


# ---------------------------------------------------------------------------
# Brave Search helpers
# ---------------------------------------------------------------------------

async def brave_search(query: str, api_key: str) -> list[dict]:
    """Call Brave Web Search API and return simplified result list."""
    headers = {
        "Accept": "application/json",
        "Accept-Encoding": "gzip",
        "X-Subscription-Token": api_key,
    }
    params = {"q": query, "count": BRAVE_SEARCH_COUNT, "text_decorations": "false"}
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(
                BRAVE_SEARCH_URL,
                headers=headers,
                params=params,
                timeout=aiohttp.ClientTimeout(total=10),
            ) as resp:
                if resp.status != 200:
                    body = await resp.text()
                    log.warning("Brave Search API %d: %s", resp.status, body[:300])
                    return []
                data = await resp.json(content_type=None)
        results = []
        for item in data.get("web", {}).get("results", []):
            results.append({
                "title": item.get("title", ""),
                "url": item.get("url", ""),
                "description": item.get("description", ""),
            })
        return results
    except Exception as exc:
        log.warning("Brave search failed: %s", exc)
        return []


def format_search_results(query: str, results: list[dict]) -> str:
    if not results:
        return f"No results found for: {query}"
    lines = [f"Web search results for '{query}':"]
    for i, r in enumerate(results, 1):
        lines.append(f"\n{i}. {r['title']}")
        lines.append(f"   {r['url']}")
        if r["description"]:
            lines.append(f"   {r['description']}")
    return "\n".join(lines)


def extract_search_queries(content: str) -> list[str]:
    return [m.strip() for m in SEARCH_TAG_RE.findall(content) if m.strip()]


def strip_search_tags(content: str) -> str:
    return SEARCH_TAG_RE.sub("", content).strip()


async def build_active_context(db: aiosqlite.Connection, conversation_id: str, new_user_msg: str) -> tuple[list[dict], bool]:
    """
    Return (messages_for_ollama, was_truncated).

    Loads all messages for the conversation newest-first, accumulates token
    counts until TOKEN_CAP is reached, then reverses to chronological order.
    The new user message is NOT included; caller appends it.
    """
    cursor = await db.execute(
        """
        SELECT role, content, thinking, token_count
        FROM messages
        WHERE conversation_id = ?
        ORDER BY id DESC
        """,
        (conversation_id,),
    )
    rows = await cursor.fetchall()

    budget = TOKEN_CAP - estimate_tokens(new_user_msg)
    included: list[dict] = []
    truncated = False

    for row in rows:
        tc = row["token_count"] or estimate_tokens(row["content"])
        if budget - tc < 0:
            truncated = True
            break
        budget -= tc
        msg: dict = {"role": row["role"], "content": row["content"]}
        if row["thinking"]:
            msg["thinking"] = row["thinking"]
        included.append(msg)

    included.reverse()  # back to chronological
    return included, truncated


async def fts_search(db: aiosqlite.Connection, conversation_id: str, query: str, limit: int = FTS_RESULT_LIMIT) -> list[str]:
    """Search messages_fts for snippets relevant to query, excluding current conversation."""
    # Sanitise FTS query: remove special chars, keep words
    safe_query = " ".join(
        word for word in query.split() if word.isalnum() or len(word) > 2
    )
    if not safe_query:
        return []
    try:
        cursor = await db.execute(
            """
            SELECT f.content
            FROM messages_fts f
            WHERE messages_fts MATCH ?
              AND f.conversation_id != ?
            ORDER BY rank
            LIMIT ?
            """,
            (safe_query, conversation_id, limit),
        )
        rows = await cursor.fetchall()
        return [row["content"] for row in rows]
    except Exception as exc:
        log.warning("FTS search failed: %s", exc)
        return []


async def save_messages(
    db: aiosqlite.Connection,
    conversation_id: str,
    user_content: str,
    assistant_content: str,
    assistant_thinking: str,
):
    ts = now_iso()
    await db.execute(
        "INSERT INTO messages(conversation_id,role,content,thinking,token_count,created_at) VALUES(?,?,?,?,?,?)",
        (conversation_id, "user", user_content, "", estimate_tokens(user_content), ts),
    )
    await db.execute(
        "INSERT INTO messages(conversation_id,role,content,thinking,token_count,created_at) VALUES(?,?,?,?,?,?)",
        (
            conversation_id,
            "assistant",
            assistant_content,
            assistant_thinking,
            estimate_tokens(assistant_content + assistant_thinking),
            ts,
        ),
    )
    # Auto-set conversation title from first user message (first 60 chars)
    cursor = await db.execute(
        "SELECT COUNT(*) AS cnt FROM messages WHERE conversation_id=? AND role='user'",
        (conversation_id,),
    )
    row = await cursor.fetchone()
    if row and row["cnt"] == 1:
        title = user_content[:60].strip().replace("\n", " ")
        await db.execute(
            "UPDATE conversations SET title=? WHERE id=? AND title='New Chat'",
            (title, conversation_id),
        )
    await db.commit()


# ---------------------------------------------------------------------------
# Routes — conversations
# ---------------------------------------------------------------------------

@app.get("/", response_class=HTMLResponse)
async def index():
    return HTMLResponse(HTML_PATH.read_text(encoding="utf-8"))


@app.get("/api/conversations")
async def list_conversations():
    db = await get_db()
    try:
        cursor = await db.execute(
            "SELECT id, title, created_at FROM conversations ORDER BY created_at DESC"
        )
        rows = await cursor.fetchall()
        return [dict(r) for r in rows]
    finally:
        await db.close()


@app.post("/api/conversations", status_code=201)
async def create_conversation(body: ConversationCreate):
    conv_id = str(uuid.uuid4())
    db = await get_db()
    try:
        await db.execute(
            "INSERT INTO conversations(id,title,created_at) VALUES(?,?,?)",
            (conv_id, body.title, now_iso()),
        )
        await db.commit()
        return {"id": conv_id, "title": body.title}
    finally:
        await db.close()


@app.patch("/api/conversations/{conv_id}")
async def rename_conversation(conv_id: str, body: ConversationRename):
    db = await get_db()
    try:
        await db.execute("UPDATE conversations SET title=? WHERE id=?", (body.title, conv_id))
        await db.commit()
        return {"ok": True}
    finally:
        await db.close()


@app.delete("/api/conversations/{conv_id}")
async def delete_conversation(conv_id: str):
    db = await get_db()
    try:
        await db.execute("DELETE FROM conversations WHERE id=?", (conv_id,))
        await db.commit()
        return {"ok": True}
    finally:
        await db.close()


@app.get("/api/conversations/{conv_id}/messages")
async def get_messages(conv_id: str):
    db = await get_db()
    try:
        cursor = await db.execute(
            "SELECT role, content, thinking, created_at FROM messages WHERE conversation_id=? ORDER BY id ASC",
            (conv_id,),
        )
        rows = await cursor.fetchall()
        return [dict(r) for r in rows]
    finally:
        await db.close()


# ---------------------------------------------------------------------------
# Settings routes
# ---------------------------------------------------------------------------

@app.get("/api/settings")
async def get_settings():
    key = get_brave_api_key()
    masked = (key[:4] + "..." + key[-4:]) if len(key) > 8 else ("*" * len(key) if key else "")
    return {"brave_api_key_set": bool(key), "brave_api_key_masked": masked}


@app.post("/api/settings")
async def update_settings(body: SettingsUpdate):
    cfg = load_config()
    cfg["brave_api_key"] = body.brave_api_key.strip()
    save_config(cfg)
    return {"ok": True}


# ---------------------------------------------------------------------------
# Chat — streaming SSE with agentic Brave Search loop
# ---------------------------------------------------------------------------

@app.post("/api/chat")
async def chat(req: ChatRequest):
    if not await ensure_ollama_running(wait_seconds=6):
        raise HTTPException(
            status_code=503,
            detail="Ollama is not available on port 11434 and auto-start failed. Start it with `ollama serve`.",
        )

    db = await get_db()
    try:
        cursor = await db.execute("SELECT id FROM conversations WHERE id=?", (req.conversation_id,))
        if not await cursor.fetchone():
            raise HTTPException(status_code=404, detail="Conversation not found")

        history, was_truncated = await build_active_context(db, req.conversation_id, req.message)

        fts_snippets: list[str] = []
        if was_truncated:
            fts_snippets = await fts_search(db, req.conversation_id, req.message)
            if fts_snippets:
                log.info("Injecting %d FTS snippet(s) for conv %s", len(fts_snippets), req.conversation_id)

        # Build base message list
        ollama_messages: list[dict] = []

        # 1. Search capability system prompt (always included when search is on)
        if req.use_search:
            ollama_messages.append({"role": "system", "content": SEARCH_SYSTEM_PROMPT})

        # 2. Long-term memory injection
        if fts_snippets:
            snippets_text = "\n\n---\n\n".join(fts_snippets)
            ollama_messages.append({
                "role": "system",
                "content": (
                    "The following are relevant excerpts from your long-term memory "
                    "(earlier conversations outside the active context window). "
                    "Use them if relevant:\n\n" + snippets_text
                ),
            })

        # 3. Conversation history + new user message
        ollama_messages.extend(history)
        ollama_messages.append({"role": "user", "content": req.message})

    except HTTPException:
        await db.close()
        raise
    except Exception as exc:
        await db.close()
        raise HTTPException(status_code=500, detail=str(exc)) from exc

    requested_model = normalize_model_name(req.model)

    async def event_stream() -> AsyncGenerator[str, None]:
        all_thinking = ""   # accumulated across all iterations
        final_content = ""  # the last iteration's clean answer
        searches_done = 0
        working_msgs = list(ollama_messages)

        def _payload(msgs: list[dict]) -> dict:
            return {"model": requested_model, "messages": msgs, "think": req.think, "stream": True}

        try:
            async with aiohttp.ClientSession() as session:
                for iteration in range(MAX_SEARCH_ITERATIONS + 1):
                    is_last_allowed = (iteration == MAX_SEARCH_ITERATIONS)
                    turn_content = ""
                    turn_thinking = ""

                    async with session.post(OLLAMA_URL, json=_payload(working_msgs)) as resp:
                        if resp.status != 200:
                            body = await resp.text()
                            yield f"data: {json.dumps({'type': 'error', 'message': body})}\n\n"
                            return

                        async for raw_line in resp.content:
                            line = raw_line.decode("utf-8").strip()
                            if not line:
                                continue
                            try:
                                chunk = json.loads(line)
                            except json.JSONDecodeError:
                                continue

                            msg_chunk = chunk.get("message", {})
                            td = msg_chunk.get("thinking", "")
                            cd = msg_chunk.get("content", "")

                            if td:
                                turn_thinking += td
                                all_thinking += td
                                yield f"data: {json.dumps({'type': 'thinking', 'delta': td})}\n\n"

                            if cd:
                                turn_content += cd
                                # Stream content live only on the final iteration
                                if is_last_allowed:
                                    final_content += cd
                                    yield f"data: {json.dumps({'type': 'content', 'delta': cd})}\n\n"

                    # ── Turn complete ──────────────────────────────────────
                    if not is_last_allowed:
                        queries = extract_search_queries(turn_content) if req.use_search else []

                        if not queries:
                            # Model answered without searching — emit content and finish
                            final_content = strip_search_tags(turn_content)
                            if final_content:
                                yield f"data: {json.dumps({'type': 'content', 'delta': final_content})}\n\n"
                            break

                        # Model wants to search — annotate the thinking block
                        hint = f"\n\n[Searching: {', '.join(repr(q) for q in queries)}]\n"
                        all_thinking += hint
                        yield f"data: {json.dumps({'type': 'thinking', 'delta': hint})}\n\n"

                        # Execute searches
                        result_blocks: list[str] = []
                        api_key = get_brave_api_key()
                        for query in queries:
                            if not api_key:
                                yield f"data: {json.dumps({'type': 'search_start', 'query': query, 'error': 'No Brave API key configured'})}\n\n"
                                result_blocks.append(
                                    f"[Search skipped — no Brave API key configured. Query was: {query}]"
                                )
                                continue
                            searches_done += 1
                            log.info("Brave search [%d]: %s", searches_done, query)
                            yield f"data: {json.dumps({'type': 'search_start', 'query': query})}\n\n"
                            results = await brave_search(query, api_key)
                            yield f"data: {json.dumps({'type': 'search_done', 'query': query, 'count': len(results)})}\n\n"
                            result_blocks.append(format_search_results(query, results))

                        # Inject results for next Ollama turn
                        working_msgs.append({
                            "role": "assistant",
                            "content": turn_content,
                            **({"thinking": turn_thinking} if turn_thinking else {}),
                        })
                        working_msgs.append({
                            "role": "user",
                            "content": (
                                "Here are the search results:\n\n"
                                + "\n\n---\n\n".join(result_blocks)
                                + "\n\nPlease provide your complete answer now."
                            ),
                        })
                    # else: is_last_allowed — content already streamed live above

            token_count = estimate_tokens(final_content + all_thinking)
            yield f"data: {json.dumps({'type': 'done', 'token_count': token_count, 'fts_used': bool(fts_snippets), 'searches_done': searches_done})}\n\n"

        except aiohttp.ClientConnectorError:
            yield f"data: {json.dumps({'type': 'error', 'message': 'Cannot connect to Ollama. Is it running? (ollama serve)'})}\n\n"
        except Exception as exc:
            log.exception("Streaming error")
            yield f"data: {json.dumps({'type': 'error', 'message': str(exc)})}\n\n"
        finally:
            if final_content or all_thinking:
                try:
                    await save_messages(db, req.conversation_id, req.message, final_content, all_thinking)
                except Exception as exc:
                    log.error("Failed to save messages: %s", exc)
            await db.close()

    return StreamingResponse(
        event_stream(),
        media_type="text/event-stream",
        headers={"Cache-Control": "no-cache", "X-Accel-Buffering": "no"},
    )


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("server:app", host="0.0.0.0", port=42069, reload=True)
