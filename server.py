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
import secrets
import shutil
import sqlite3
import subprocess
import sys
import uuid
from collections import Counter
from contextlib import asynccontextmanager
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import AsyncGenerator
from urllib.parse import urlparse

from dotenv import load_dotenv

load_dotenv(Path(__file__).parent / ".env")

# Qwen-Agent integration — import after dotenv so any env vars are set
from agent_tools import (
    set_request_context,
    code_interpreter,
    get_or_create_ps_session,
    is_ps_available,
    release_ps_session,
)

try:
    from qwen_agent.agents import Assistant
    from qwen_agent.llm import get_chat_model
    QWEN_AGENT_RUNTIME_AVAILABLE = True
except ImportError:
    QWEN_AGENT_RUNTIME_AVAILABLE = False

import aiohttp
import aiosqlite
from fastapi import Depends, FastAPI, HTTPException, Query, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from fastapi.responses import HTMLResponse, StreamingResponse
from fastapi.staticfiles import StaticFiles
from jose import JWTError, jwt
from passlib.context import CryptContext
from pydantic import BaseModel

try:
    import chromadb
    import chromadb.config
    from chromadb.utils.embedding_functions import SentenceTransformerEmbeddingFunction
    CHROMADB_AVAILABLE = True
except ImportError:
    CHROMADB_AVAILABLE = False
    log = logging.getLogger(__name__)  # early reference for error handling

# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------
OLLAMA_BASE_URL   = os.getenv("OLLAMA_BASE_URL", "http://100.66.64.45:11434").rstrip("/")
OLLAMA_URL        = f"{OLLAMA_BASE_URL}/api/chat"
OLLAMA_HEALTH_URL = f"{OLLAMA_BASE_URL}/api/tags"
OLLAMA_OPENAI_URL = f"{OLLAMA_BASE_URL}/v1"
BRAVE_SEARCH_URL  = "https://api.search.brave.com/res/v1/web/search"
DEFAULT_MODEL     = "qwen3-coder:30b"
DB_PATH           = Path(__file__).parent / "memory.db"
HTML_PATH         = Path(__file__).parent / "index.html"
CONFIG_PATH       = Path(__file__).parent / "config.json"
INDEXED_DOCS_ROOT = Path(__file__).parent / "indexed-docs"
GML_DOCS_ROOT     = INDEXED_DOCS_ROOT / "gml"
PS_DOCS_ROOT      = INDEXED_DOCS_ROOT / "ps-docs"
GML_EMBEDDINGS_DB  = Path(__file__).parent / "gml_embeddings"
PS_EMBEDDINGS_DB   = Path(__file__).parent / "ps_docs_embeddings"
TOKEN_CAP              = 20_000  # max tokens kept in active context
FTS_RESULT_LIMIT       = 3       # past-memory snippets to inject when truncated
TOKEN_ESTIMATE_DIVISOR = 4       # chars / 4 ≈ tokens
MAX_SEARCH_ITERATIONS  = 3       # max Brave searches per response
BRAVE_SEARCH_COUNT     = 5       # results to fetch per query
GML_RESULT_LIMIT       = 4       # local GML snippets to inject
PS_RESULT_LIMIT        = 4       # local PowerShell snippets to inject
GML_CHUNK_CHAR_LIMIT   = 1_400   # target chunk size for docs retrieval
JWT_ALGORITHM          = "HS256"
ACCESS_TOKEN_HOURS     = 24

SEARCH_TAG_RE = re.compile(r'<search>(.*?)</search>', re.IGNORECASE | re.DOTALL)
GML_TOKEN_RE = re.compile(r"[a-zA-Z_][a-zA-Z0-9_]*")
THINK_TAG_RE = re.compile(r"<think>(.*?)</think>", re.IGNORECASE | re.DOTALL)
TOOL_ERROR_RE = re.compile(r"\[(?:error|permission denied):|\berror\b|\bexception\b", re.IGNORECASE)
LITERAL_TOOL_CALL_RE = re.compile(
    r"<\s*function\s*=\s*([a-zA-Z0-9_:\-]+)\s*>(.*?)<\s*/\s*function\s*>",
    re.IGNORECASE | re.DOTALL,
)
LITERAL_PARAM_RE = re.compile(
    r"<\s*parameter\s*=\s*([a-zA-Z0-9_:\-]+)\s*>(.*?)<\s*/\s*parameter\s*>",
    re.IGNORECASE | re.DOTALL,
)


_ollama_endpoint = urlparse(OLLAMA_BASE_URL)
OLLAMA_HOST = (_ollama_endpoint.hostname or "").lower()
OLLAMA_PORT = _ollama_endpoint.port or (443 if _ollama_endpoint.scheme == "https" else 80)
OLLAMA_IS_LOCAL = OLLAMA_HOST in {"127.0.0.1", "localhost", "::1"}

SEARCH_SYSTEM_PROMPT = (
    "You have access to a live web search tool. "
    "When you need current information, specific facts, recent events, or anything you are uncertain about, "
    "request a search using this exact format on its own line:\n\n"
    "<search>your search query here</search>\n\n"
    "You will receive the search results and should then provide a complete, accurate answer. "
    "You may search up to 3 times per response. Only search when genuinely needed."
)

GML_SYSTEM_PROMPT = (
    "You are assisting with GameMaker programming in GML. "
    "Prefer accurate GameMaker terminology, explain engine-specific behavior clearly, "
    "and provide practical code examples when useful. "
    "Use the gml_docs_search tool whenever authoritative manual details are needed. "
    "If retrieved excerpts do not fully answer the question, say what is missing instead of inventing APIs or behavior."
)

PS_SYSTEM_PROMPT = (
    "You are assisting with PowerShell scripting and automation. "
    "Prefer accurate PowerShell terminology and explain shell-specific behavior clearly. "
    "Use the ps_docs_search tool whenever authoritative documentation details are needed. "
    "If retrieved excerpts do not fully answer the question, say what is missing instead of inventing commands, parameters, or behavior."
)

ENGLISH_ONLY_SYSTEM_PROMPT = (
    "You must respond only in English. "
    "Do not use other languages, including mixed-language output, unless explicitly asked to translate quoted text."
)

FILE_TOOLS_SYSTEM_PROMPT = (
    "You have access to local file operations tools for reading, writing, and searching files. "
    "The workspace is sandboxed to a specific root directory configured by your admin. "
    "You can use these tools to analyze code, make edits, and validate your work. "
    "For code execution, use the code_interpreter tool, which runs inside a Docker sandbox mounted to the workspace only. "
    "Do not ask for shell command execution; it is not available. "
    "When the user asks to list files or directories, call list_dir and return the exact directory entries from the tool output, "
    "one per line, without summarizing, grouping, or omitting entries unless the tool itself reports truncation."
)

MCP_FILE_TOOLS_SYSTEM_PROMPT = (
    "You have access to MCP filesystem tools for reading, writing, and searching files. "
    "The workspace is sandboxed to a specific root directory configured by your admin. "
    "Use the MCP filesystem server tools to analyze code, make edits, and validate your work. "
    "For code execution, use the code_interpreter tool, which runs inside a Docker sandbox mounted to the workspace only. "
    "Do not ask for shell command execution; it is not available. "
    "When the user asks to list files or directories, call the appropriate directory listing tool and return "
    "the exact entries from the tool output, one per line, without summarizing, grouping, or omitting entries "
    "unless the tool itself reports truncation."
)

TOOL_EXECUTION_CONTRACT_PROMPT = (
    "Execution-first contract for tool and MCP calls: "
    "If the user request is concrete and executable, do the work first and do not ask clarifying questions. "
    "Never replace requested output with a high-level summary unless explicitly asked. "
    "Never stop early due to response length; if output is large, split into batches and continue until complete. "
    "Ask follow-up questions only for true blockers such as missing path, permission denied, unavailable command, or contradictory constraints. "
    "For file inventory requests, include every discovered file and provide one concise line per file; include binary/unreadable files with that label. "
    "Before finishing, verify scope coverage and that output count matches discovered items. "
    "If a tool call fails, retry with an equivalent method; if still blocked, report what was tried and return partial results clearly labeled PARTIAL. "
    "Only mark completion when all requested items are delivered. "
    "Do not output literal tool markup such as <function=...>, <tool_call>, or <parameter=...>; "
    "invoke tools only through native OpenAI-style tool_calls."
)

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
log = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    if not await ensure_ollama_running():
        log.warning("Continuing startup without Ollama; /api/chat will retry auto-start.")

    db = await get_db()
    try:
        for stmt in _DDL_STATEMENTS:
            await db.execute(stmt.strip())
        await db.commit()
        await ensure_conversations_user_column(db)
        await ensure_user_tools_columns(db)

        if not get_jwt_secret():
            raise RuntimeError("JWT_SECRET is required in environment before startup")

        admin = await ensure_bootstrap_admin(db)
        await backfill_legacy_conversations(db, admin["id"])
    finally:
        await db.close()

    await ensure_gml_index_loaded(force=True)
    await ensure_ps_index_loaded(force=True)
    app.state.gml_embeddings_ready = False
    app.state.gml_embeddings_building = CHROMADB_AVAILABLE
    app.state.ps_embeddings_ready = False
    app.state.ps_embeddings_building = CHROMADB_AVAILABLE
    if CHROMADB_AVAILABLE:
        get_or_init_embedding_model()
        get_or_init_chroma_client("gml")
        get_or_init_chroma_client("ps")
        asyncio.create_task(_build_gml_embeddings_background())
        asyncio.create_task(_build_ps_embeddings_background())
    log.info("Database initialised at %s", DB_PATH)
    yield


app = FastAPI(title="Ollama Qwen3 Chat", lifespan=lifespan)
app.mount("/resources", StaticFiles(directory=Path(__file__).parent / "resources"), name="resources")
_ollama_start_lock = asyncio.Lock()
_gml_index_lock = asyncio.Lock()
_ps_index_lock = asyncio.Lock()
_auth_scheme = HTTPBearer(auto_error=False)
_pwd_context = CryptContext(schemes=["pbkdf2_sha256"], deprecated="auto")

# Embeddings model (lazy-loaded)
_embedding_model: SentenceTransformerEmbeddingFunction | None = None
_gml_chroma_client = None  # chromadb.PersistentClient, typed loosely to avoid import quirks
_ps_chroma_client = None   # chromadb.PersistentClient, typed loosely to avoid import quirks

# ---------------------------------------------------------------------------
# Database
# ---------------------------------------------------------------------------

_DDL_STATEMENTS = [
    "PRAGMA journal_mode=WAL",
    """
    CREATE TABLE IF NOT EXISTS users (
        id                  TEXT PRIMARY KEY,
        username            TEXT NOT NULL UNIQUE,
        password_hash       TEXT NOT NULL,
        role                TEXT NOT NULL DEFAULT 'user',
        is_active           INTEGER NOT NULL DEFAULT 1,
        file_tools_enabled  INTEGER NOT NULL DEFAULT 0,
        workspace_root      TEXT NOT NULL DEFAULT '',
        persona_prompt      TEXT NOT NULL DEFAULT '',
        mcp_config          TEXT NOT NULL DEFAULT '',
        created_at          TEXT NOT NULL
    )
    """,
    "CREATE INDEX IF NOT EXISTS idx_users_username ON users(username)",
    """
    CREATE TABLE IF NOT EXISTS invite_tokens (
        id         TEXT PRIMARY KEY,
        token      TEXT NOT NULL UNIQUE,
        created_by TEXT NOT NULL REFERENCES users(id) ON DELETE CASCADE,
        expires_at TEXT,
        used_by    TEXT REFERENCES users(id) ON DELETE SET NULL,
        used_at    TEXT,
        created_at TEXT NOT NULL
    )
    """,
    "CREATE INDEX IF NOT EXISTS idx_invites_token ON invite_tokens(token)",
    """
    CREATE TABLE IF NOT EXISTS conversations (
        id         TEXT PRIMARY KEY,
        user_id    TEXT NOT NULL REFERENCES users(id) ON DELETE CASCADE,
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
    db = await aiosqlite.connect(DB_PATH, timeout=30)
    db.row_factory = aiosqlite.Row
    await db.execute("PRAGMA busy_timeout = 30000")
    await db.execute("PRAGMA foreign_keys = ON")
    return db


def get_jwt_secret() -> str:
    return os.environ.get("JWT_SECRET", "").strip()


def hash_password(password: str) -> str:
    return _pwd_context.hash(password)


def verify_password(password: str, password_hash: str) -> bool:
    return _pwd_context.verify(password, password_hash)


def create_access_token(user_id: str) -> str:
    secret = get_jwt_secret()
    if not secret:
        raise HTTPException(status_code=500, detail="JWT secret is not configured")
    now = datetime.now(timezone.utc)
    payload = {
        "sub": user_id,
        "iat": int(now.timestamp()),
        "exp": int((now + timedelta(hours=ACCESS_TOKEN_HOURS)).timestamp()),
    }
    return jwt.encode(payload, secret, algorithm=JWT_ALGORITHM)


def parse_iso(value: str | None) -> datetime | None:
    if not value:
        return None
    try:
        normalized = value.replace("Z", "+00:00")
        return datetime.fromisoformat(normalized)
    except Exception:
        return None


def validate_username(username: str) -> str:
    normalized = (username or "").strip().lower()
    if len(normalized) < 3 or len(normalized) > 32:
        raise HTTPException(status_code=400, detail="Username must be 3-32 characters")
    if not re.fullmatch(r"[a-z0-9_.-]+", normalized):
        raise HTTPException(
            status_code=400,
            detail="Username can only contain letters, numbers, dot, underscore, and dash",
        )
    return normalized


def validate_password_strength(password: str) -> str:
    candidate = (password or "").strip()
    if len(candidate) < 8:
        raise HTTPException(status_code=400, detail="Password must be at least 8 characters")
    return candidate


async def ensure_conversations_user_column(db: aiosqlite.Connection) -> None:
    cursor = await db.execute("PRAGMA table_info(conversations)")
    rows = await cursor.fetchall()
    cols = {row["name"] for row in rows}
    if "user_id" not in cols:
        await db.execute("ALTER TABLE conversations ADD COLUMN user_id TEXT")
    await db.execute("CREATE INDEX IF NOT EXISTS idx_conversations_user ON conversations(user_id, created_at)")
    await db.commit()


async def ensure_user_tools_columns(db: aiosqlite.Connection) -> None:
    """Migrate users table to add per-user tooling/profile columns if missing."""
    cursor = await db.execute("PRAGMA table_info(users)")
    rows = await cursor.fetchall()
    cols = {row["name"] for row in rows}
    if "file_tools_enabled" not in cols:
        await db.execute("ALTER TABLE users ADD COLUMN file_tools_enabled INTEGER NOT NULL DEFAULT 0")
    if "workspace_root" not in cols:
        await db.execute("ALTER TABLE users ADD COLUMN workspace_root TEXT NOT NULL DEFAULT ''")
    if "persona_prompt" not in cols:
        await db.execute("ALTER TABLE users ADD COLUMN persona_prompt TEXT NOT NULL DEFAULT ''")
    if "mcp_config" not in cols:
        await db.execute("ALTER TABLE users ADD COLUMN mcp_config TEXT NOT NULL DEFAULT ''")
    await db.commit()


async def ensure_bootstrap_admin(db: aiosqlite.Connection) -> dict:
    raw_username = os.environ.get("ADMIN_USERNAME", "").strip().lower()
    raw_password = os.environ.get("ADMIN_PASSWORD", "")

    cursor = await db.execute("SELECT COUNT(*) AS cnt FROM users")
    row = await cursor.fetchone()
    if row and row["cnt"] > 0:
        # Recovery path: if env admin creds are set and user exists, keep it admin/active and sync password.
        if raw_username and raw_password:
            admin_username = validate_username(raw_username)
            admin_password = validate_password_strength(raw_password)
            cursor = await db.execute(
                "SELECT id, username, password_hash, role, is_active FROM users WHERE username=?",
                (admin_username,),
            )
            env_user = await cursor.fetchone()
            if env_user:
                updated = False
                if env_user["role"] != "admin":
                    await db.execute("UPDATE users SET role='admin' WHERE id=?", (env_user["id"],))
                    updated = True
                if not env_user["is_active"]:
                    await db.execute("UPDATE users SET is_active=1 WHERE id=?", (env_user["id"],))
                    updated = True
                if not verify_password(admin_password, env_user["password_hash"]):
                    await db.execute(
                        "UPDATE users SET password_hash=? WHERE id=?",
                        (hash_password(admin_password), env_user["id"]),
                    )
                    updated = True
                if updated:
                    await db.commit()
                    log.warning("Synchronized admin credentials for '%s' from environment.", admin_username)
                return {"id": env_user["id"], "username": env_user["username"], "role": "admin"}

        cursor = await db.execute("SELECT id, username, role FROM users WHERE role='admin' ORDER BY created_at ASC LIMIT 1")
        admin = await cursor.fetchone()
        if admin:
            return dict(admin)

        # If no admin exists but env credentials are provided, create one.
        if raw_username and raw_password:
            admin_username = validate_username(raw_username)
            admin_password = validate_password_strength(raw_password)
            admin_id = str(uuid.uuid4())
            await db.execute(
                """
                INSERT INTO users(id, username, password_hash, role, is_active, created_at)
                VALUES(?, ?, ?, 'admin', 1, ?)
                """,
                (admin_id, admin_username, hash_password(admin_password), now_iso()),
            )
            await db.commit()
            log.warning("Created missing admin user '%s' from environment.", admin_username)
            return {"id": admin_id, "username": admin_username, "role": "admin"}

        raise RuntimeError("No admin user found. Set ADMIN_USERNAME and ADMIN_PASSWORD to recover access.")

    if not raw_username:
        raise RuntimeError("ADMIN_USERNAME is required before first startup")
    if not raw_password:
        raise RuntimeError("ADMIN_PASSWORD is required before first startup")

    admin_username = validate_username(raw_username)
    admin_password = validate_password_strength(raw_password)
    admin_id = str(uuid.uuid4())
    await db.execute(
        """
        INSERT INTO users(id, username, password_hash, role, is_active, created_at)
        VALUES(?, ?, ?, 'admin', 1, ?)
        """,
        (admin_id, admin_username, hash_password(admin_password), now_iso()),
    )
    await db.commit()
    log.warning("Bootstrap admin created from environment for username '%s'", admin_username)
    return {"id": admin_id, "username": admin_username, "role": "admin"}


async def backfill_legacy_conversations(db: aiosqlite.Connection, fallback_user_id: str) -> bool:
    max_attempts = 8
    for attempt in range(1, max_attempts + 1):
        try:
            await db.execute(
                "UPDATE conversations SET user_id = ? WHERE user_id IS NULL OR TRIM(user_id) = ''",
                (fallback_user_id,),
            )
            await db.commit()
            return True
        except sqlite3.OperationalError as exc:
            is_locked = "database is locked" in str(exc).lower()
            if not is_locked:
                raise
            if attempt >= max_attempts:
                log.warning(
                    "Skipping legacy conversation backfill after %d locked attempts; startup will continue",
                    max_attempts,
                )
                return False
            delay = min(0.25 * attempt, 2.0)
            log.warning(
                "DB locked during legacy conversation backfill (attempt %d/%d); retrying in %.2fs",
                attempt,
                max_attempts,
                delay,
            )
            await asyncio.sleep(delay)
    return False


async def get_current_user(
    credentials: HTTPAuthorizationCredentials | None = Depends(_auth_scheme),
) -> dict:
    if not credentials or credentials.scheme.lower() != "bearer":
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Missing authentication token")

    token = credentials.credentials
    secret = get_jwt_secret()
    if not secret:
        raise HTTPException(status_code=500, detail="JWT secret is not configured")

    try:
        payload = jwt.decode(token, secret, algorithms=[JWT_ALGORITHM])
    except JWTError as exc:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid authentication token") from exc

    user_id = payload.get("sub")
    if not user_id:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid authentication token")

    db = await get_db()
    try:
        cursor = await db.execute(
            "SELECT id, username, role, is_active, file_tools_enabled, workspace_root, persona_prompt, mcp_config, created_at FROM users WHERE id=?",
            (user_id,),
        )
        row = await cursor.fetchone()
        if not row or not row["is_active"]:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="User is not active")
        return dict(row)
    finally:
        await db.close()


async def require_admin(current_user: dict = Depends(get_current_user)) -> dict:
    if current_user.get("role") != "admin":
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Admin access required")
    return current_user


async def is_ollama_running(timeout_seconds: float = 1.5) -> bool:
    """Return True when the configured Ollama endpoint responds."""
    try:
        timeout = aiohttp.ClientTimeout(total=timeout_seconds)
        async with aiohttp.ClientSession(timeout=timeout) as session:
            async with session.get(OLLAMA_HEALTH_URL) as resp:
                return resp.status == 200
    except Exception:
        return False


def start_ollama_service() -> bool:
    """Try to launch `ollama serve` in a detached process."""
    if not OLLAMA_IS_LOCAL:
        log.info("Skipping local Ollama auto-start because endpoint is remote: %s", OLLAMA_BASE_URL)
        return False

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
    """Ensure Ollama is reachable; auto-start it only for local endpoints."""
    if await is_ollama_running():
        return True

    if not OLLAMA_IS_LOCAL:
        log.warning("Configured remote Ollama endpoint is unavailable: %s", OLLAMA_BASE_URL)
        return False

    async with _ollama_start_lock:
        if await is_ollama_running():
            return True

        log.warning("No local Ollama service detected at %s. Attempting to start Ollama.", OLLAMA_BASE_URL)
        if not start_ollama_service():
            return False

        for _ in range(wait_seconds):
            await asyncio.sleep(1)
            if await is_ollama_running():
                log.info("Ollama became available at %s.", OLLAMA_BASE_URL)
                return True

        log.warning("Ollama did not become ready at %s after %s seconds.", OLLAMA_BASE_URL, wait_seconds)
        return False





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
    use_gml_docs: bool = True
    use_ps_docs: bool = False
    use_file_tools: bool = False
    use_code_interpreter: bool = False  # Docker-based sandboxed Python execution
    use_powershell: bool = False  # Persistent PowerShell session (native or Docker)
    use_mcp_tools: bool = True  # Include initialised MCP server tools
    working_subdir: str = ""


class SettingsUpdate(BaseModel):
    brave_api_key: str = ""


class LoginRequest(BaseModel):
    username: str
    password: str


class SignupRequest(BaseModel):
    username: str
    password: str
    invite_token: str


class AdminCreateUserRequest(BaseModel):
    username: str
    password: str
    role: str = "user"


class AdminCreateInviteRequest(BaseModel):
    expires_in_days: int = 7


class AdminPersonaUpdateRequest(BaseModel):
    persona_prompt: str = ""


class AdminGlobalToolingUpdateRequest(BaseModel):
    use_gml_docs: bool = True
    use_ps_docs: bool = True
    use_file_tools: bool = True
    use_code_interpreter: bool = True
    use_powershell: str = "off"  # "off" | "native" | "docker"
    use_mcp_tools: bool = True
    use_raw_api: bool = True


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
    if cleaned in {
        "huihui_ai/qwen3-abliterated",
        "huihui_ai/qwen3-abliterated:8b",
        "goekdenizguelmez/JOSIEFIED-Qwen3:8b",
        "goekdenizguelmez/JOSIEFIED-Qwen3:8b-q8_0",
    }:
        return DEFAULT_MODEL
    return cleaned


def tokenize_search_text(text: str) -> list[str]:
    return [token.lower() for token in GML_TOKEN_RE.findall(text or "") if len(token) >= 2]


def split_gml_markdown(content: str) -> list[tuple[str, str]]:
    lines = content.splitlines()
    sections: list[tuple[str, str]] = []
    current_heading = "Document Overview"
    current_lines: list[str] = []

    def flush_section() -> None:
        nonlocal current_lines
        text = "\n".join(current_lines).strip()
        if text:
            sections.append((current_heading, text))
        current_lines = []

    for line in lines:
        stripped = line.strip()
        if stripped.startswith("#"):
            flush_section()
            current_heading = stripped.lstrip("#").strip() or "Document Overview"
            current_lines.append(line)
            continue
        current_lines.append(line)

    flush_section()
    if sections:
        return sections

    fallback = content.strip()
    return [("Document Overview", fallback)] if fallback else []


def chunk_gml_section(heading: str, content: str, limit: int = GML_CHUNK_CHAR_LIMIT) -> list[str]:
    compact = content.strip()
    if not compact:
        return []

    paragraphs = [part.strip() for part in re.split(r"\n\s*\n", compact) if part.strip()]
    if not paragraphs:
        paragraphs = [compact]

    chunks: list[str] = []
    current = f"Section: {heading}\n\n"
    for paragraph in paragraphs:
        candidate = current + paragraph + "\n\n"
        if len(candidate) <= limit:
            current = candidate
            continue

        if current.strip() != f"Section: {heading}":
            chunks.append(current.strip())
            current = f"Section: {heading}\n\n"

        if len(paragraph) <= limit:
            current += paragraph + "\n\n"
            continue

        start = 0
        while start < len(paragraph):
            slice_end = min(start + limit, len(paragraph))
            snippet = paragraph[start:slice_end].strip()
            if snippet:
                chunks.append(f"Section: {heading}\n\n{snippet}")
            start = slice_end

    if current.strip() != f"Section: {heading}":
        chunks.append(current.strip())
    return chunks


def build_gml_index(root: Path, source_label: str = "GML") -> dict:
    stats = {
        "enabled": root.exists(),
        "root": str(root),
        "file_count": 0,
        "chunk_count": 0,
        "indexed_at": now_iso(),
        "chunks": [],
        "error": "",
    }
    if not root.exists():
        stats["error"] = f"{source_label} docs folder not found: {root}"
        return stats

    chunks: list[dict] = []
    for md_path in sorted(root.rglob("*.md")):
        try:
            raw_text = md_path.read_text(encoding="utf-8", errors="ignore")
        except Exception as exc:
            log.warning("Failed to read %s doc %s: %s", source_label, md_path, exc)
            continue

        rel_path = md_path.relative_to(root.parent).as_posix()
        title = md_path.stem.replace("_", " ")
        for heading, section_text in split_gml_markdown(raw_text):
            for chunk_index, chunk_text in enumerate(chunk_gml_section(heading, section_text)):
                searchable = f"{rel_path}\n{title}\n{heading}\n{chunk_text}"
                chunks.append({
                    "path": rel_path,
                    "title": title,
                    "heading": heading,
                    "chunk_index": chunk_index,
                    "content": chunk_text,
                    "searchable": searchable.lower(),
                    "tokens": Counter(tokenize_search_text(searchable)),
                })

        stats["file_count"] += 1

    stats["chunk_count"] = len(chunks)
    stats["chunks"] = chunks
    return stats


async def ensure_gml_index_loaded(force: bool = False) -> dict:
    current_index = getattr(app.state, "gml_index", None)
    if current_index is not None and not force:
        return current_index

    async with _gml_index_lock:
        current_index = getattr(app.state, "gml_index", None)
        if current_index is not None and not force:
            return current_index

        gml_index = build_gml_index(GML_DOCS_ROOT, source_label="GML")
        app.state.gml_index = gml_index
        log.info(
            "GML docs index ready: %d files, %d chunks",
            gml_index.get("file_count", 0),
            gml_index.get("chunk_count", 0),
        )
        if gml_index.get("error"):
            log.warning("GML docs index warning: %s", gml_index["error"])
        return gml_index


async def ensure_ps_index_loaded(force: bool = False) -> dict:
    current_index = getattr(app.state, "ps_index", None)
    if current_index is not None and not force:
        return current_index

    async with _ps_index_lock:
        current_index = getattr(app.state, "ps_index", None)
        if current_index is not None and not force:
            return current_index

        ps_index = build_gml_index(PS_DOCS_ROOT, source_label="PowerShell")
        app.state.ps_index = ps_index
        log.info(
            "PowerShell docs index ready: %d files, %d chunks",
            ps_index.get("file_count", 0),
            ps_index.get("chunk_count", 0),
        )
        if ps_index.get("error"):
            log.warning("PowerShell docs index warning: %s", ps_index["error"])
        return ps_index


def get_or_init_embedding_model() -> SentenceTransformerEmbeddingFunction | None:
    global _embedding_model
    if not CHROMADB_AVAILABLE:
        return None
    if _embedding_model is None:
        try:
            _embedding_model = SentenceTransformerEmbeddingFunction(
                model_name="all-MiniLM-L6-v2"
            )
            log.info("Embedding model initialized: all-MiniLM-L6-v2")
        except Exception as exc:
            log.error("Failed to initialize embedding model: %s", exc)
            return None
    return _embedding_model


def get_or_init_chroma_client(kind: str):
    global _gml_chroma_client, _ps_chroma_client

    if not CHROMADB_AVAILABLE:
        return None

    if kind == "gml":
        if _gml_chroma_client is None:
            try:
                GML_EMBEDDINGS_DB.mkdir(parents=True, exist_ok=True)
                _gml_chroma_client = chromadb.PersistentClient(path=str(GML_EMBEDDINGS_DB))
                log.info("GML Chroma persistent client initialized at %s", GML_EMBEDDINGS_DB)
            except Exception as exc:
                log.error("Failed to initialize GML Chroma client: %s", exc)
                return None
        return _gml_chroma_client

    if kind == "ps":
        if _ps_chroma_client is None:
            try:
                PS_EMBEDDINGS_DB.mkdir(parents=True, exist_ok=True)
                _ps_chroma_client = chromadb.PersistentClient(path=str(PS_EMBEDDINGS_DB))
                log.info("PowerShell Chroma persistent client initialized at %s", PS_EMBEDDINGS_DB)
            except Exception as exc:
                log.error("Failed to initialize PowerShell Chroma client: %s", exc)
                return None
        return _ps_chroma_client

    return None


def _chromadb_build_sync(
    chunks: list[dict],
    *,
    collection_name: str,
    source_label: str,
    client_kind: str,
) -> dict:
    """Synchronous chromadb upsert — intended for thread-pool execution."""
    embedding_fn = get_or_init_embedding_model()
    client = get_or_init_chroma_client(client_kind)
    if not embedding_fn or not client:
        return {
            "enabled": False,
            "error": "Failed to initialize embeddings or Chroma client",
            "chunk_count": 0,
        }

    try:
        existing = client.get_or_create_collection(
            name=collection_name,
            embedding_function=embedding_fn,
            metadata={"hnsw:space": "cosine"},
        )
        if existing.count() == len(chunks):
            log.info(
                "%s embeddings cache hit: %d chunks already indexed, skipping rebuild",
                source_label,
                len(chunks),
            )
            return {"enabled": True, "chunk_count": len(chunks), "collection_name": collection_name}

        log.info(
            "%s embeddings cache miss (%d stored vs %d current), rebuilding…",
            source_label,
            existing.count(),
            len(chunks),
        )
        client.delete_collection(name=collection_name)
        collection = client.get_or_create_collection(
            name=collection_name,
            embedding_function=embedding_fn,
            metadata={"hnsw:space": "cosine"},
        )

        ids = [f"chunk_{i}" for i in range(len(chunks))]
        documents = [c["content"] for c in chunks]
        metadatas = [
            {"path": c["path"], "heading": c["heading"], "chunk_index": str(c["chunk_index"])}
            for c in chunks
        ]
        if ids:
            batch_size = 5000
            for i in range(0, len(ids), batch_size):
                collection.upsert(
                    ids=ids[i:i + batch_size],
                    documents=documents[i:i + batch_size],
                    metadatas=metadatas[i:i + batch_size],
                )
        log.info("Built %s embeddings collection: %d chunks indexed", source_label, len(ids))
        return {"enabled": True, "chunk_count": len(ids), "collection_name": collection_name}
    except Exception as exc:
        log.error("Failed to build %s embeddings collection: %s", source_label, exc)
        return {"enabled": False, "error": str(exc), "chunk_count": 0}


async def _build_gml_embeddings_background() -> None:
    """Background task: builds GML Chroma embeddings without blocking the event loop."""
    try:
        gml_index = getattr(app.state, "gml_index", None)
        if not gml_index or not gml_index.get("chunks"):
            log.warning("GML embeddings: index not ready, skipping build")
            app.state.gml_embeddings_ready = False
            return
        result = await asyncio.to_thread(
            _chromadb_build_sync,
            gml_index["chunks"],
            collection_name="gml_docs",
            source_label="GML",
            client_kind="gml",
        )
        app.state.gml_embeddings_ready = result.get("enabled", False)
        if result.get("enabled"):
            log.info("GML embeddings collection ready: %d chunks", result["chunk_count"])
        else:
            log.warning("GML embeddings not available: %s", result.get("error", "unknown"))
    except Exception as exc:
        log.error("GML embeddings background task failed: %s", exc)
        app.state.gml_embeddings_ready = False
    finally:
        app.state.gml_embeddings_building = False


async def _build_ps_embeddings_background() -> None:
    """Background task: builds PowerShell docs Chroma embeddings without blocking the event loop."""
    try:
        ps_index = getattr(app.state, "ps_index", None)
        if not ps_index or not ps_index.get("chunks"):
            log.warning("PowerShell docs embeddings: index not ready, skipping build")
            app.state.ps_embeddings_ready = False
            return
        result = await asyncio.to_thread(
            _chromadb_build_sync,
            ps_index["chunks"],
            collection_name="ps_docs",
            source_label="PowerShell docs",
            client_kind="ps",
        )
        app.state.ps_embeddings_ready = result.get("enabled", False)
        if result.get("enabled"):
            log.info("PowerShell docs embeddings collection ready: %d chunks", result["chunk_count"])
        else:
            log.warning("PowerShell docs embeddings not available: %s", result.get("error", "unknown"))
    except Exception as exc:
        log.error("PowerShell docs embeddings background task failed: %s", exc)
        app.state.ps_embeddings_ready = False
    finally:
        app.state.ps_embeddings_building = False


async def build_gml_embeddings_collection() -> dict:
    """Async wrapper used outside of the background startup task."""
    if not CHROMADB_AVAILABLE:
        return {
            "enabled": False,
            "error": "chromadb not available; install with: pip install chromadb sentence-transformers",
            "chunk_count": 0,
        }
    gml_index = getattr(app.state, "gml_index", None)
    if not gml_index or not gml_index.get("chunks"):
        return {
            "enabled": False,
            "error": "GML index not found; cannot build embeddings",
            "chunk_count": 0,
        }
    return await asyncio.to_thread(
        _chromadb_build_sync,
        gml_index["chunks"],
        collection_name="gml_docs",
        source_label="GML",
        client_kind="gml",
    )


async def build_ps_embeddings_collection() -> dict:
    """Async wrapper used outside of the background startup task."""
    if not CHROMADB_AVAILABLE:
        return {
            "enabled": False,
            "error": "chromadb not available; install with: pip install chromadb sentence-transformers",
            "chunk_count": 0,
        }
    ps_index = getattr(app.state, "ps_index", None)
    if not ps_index or not ps_index.get("chunks"):
        return {
            "enabled": False,
            "error": "PowerShell docs index not found; cannot build embeddings",
            "chunk_count": 0,
        }
    return await asyncio.to_thread(
        _chromadb_build_sync,
        ps_index["chunks"],
        collection_name="ps_docs",
        source_label="PowerShell docs",
        client_kind="ps",
    )


def _search_docs(
    query: str,
    *,
    limit: int,
    collection_name: str,
    source_label: str,
    client_kind: str,
) -> list[dict]:
    if not CHROMADB_AVAILABLE:
        log.warning("Chroma not available; cannot perform semantic search")
        return []

    client = get_or_init_chroma_client(client_kind)
    if not client:
        return []

    try:
        collection = client.get_collection(name=collection_name)
    except Exception as exc:
        log.warning("%s embeddings collection not found: %s. Falling back to empty results.", source_label, exc)
        return []

    try:
        results = collection.query(
            query_texts=[query],
            n_results=limit,
        )

        selected = []
        if results and results["ids"] and len(results["ids"]) > 0:
            for i, doc_id in enumerate(results["ids"][0]):
                if i < len(results["metadatas"][0]) and i < len(results["documents"][0]):
                    metadata = results["metadatas"][0][i]
                    document = results["documents"][0][i]
                    distance = results["distances"][0][i] if results.get("distances") else 0

                    selected.append({
                        "score": 1.0 - distance,
                        "path": metadata.get("path", ""),
                        "heading": metadata.get("heading", ""),
                        "content": document,
                    })

        return selected
    except Exception as exc:
        log.error("%s semantic search failed: %s", source_label, exc)
        return []


def search_gml_docs(query: str, limit: int = GML_RESULT_LIMIT) -> list[dict]:
    """Search GML docs using vector embeddings (semantic search)."""
    return _search_docs(
        query,
        limit=limit,
        collection_name="gml_docs",
        source_label="GML",
        client_kind="gml",
    )


def search_ps_docs(query: str, limit: int = PS_RESULT_LIMIT) -> list[dict]:
    """Search PowerShell docs using vector embeddings (semantic search)."""
    return _search_docs(
        query,
        limit=limit,
        collection_name="ps_docs",
        source_label="PowerShell docs",
        client_kind="ps",
    )


def _keyword_search_docs(query: str, index: dict, limit: int) -> list[dict]:
    """Keyword fallback retrieval over pre-chunked docs when vector search is unavailable."""
    chunks = index.get("chunks", []) if isinstance(index, dict) else []
    if not chunks:
        return []

    query_tokens = Counter(tokenize_search_text(query))
    if not query_tokens:
        return []

    scored: list[tuple[float, dict]] = []
    for chunk in chunks:
        chunk_tokens: Counter = chunk.get("tokens", Counter())
        score = 0.0
        for token, qtf in query_tokens.items():
            ctf = float(chunk_tokens.get(token, 0))
            if ctf:
                score += ctf * float(qtf)
        if score > 0:
            scored.append((score, chunk))

    if not scored:
        return []

    scored.sort(key=lambda x: x[0], reverse=True)
    selected = []
    for score, chunk in scored[:limit]:
        selected.append(
            {
                "score": score,
                "path": chunk.get("path", ""),
                "heading": chunk.get("heading", ""),
                "content": chunk.get("content", ""),
            }
        )
    return selected


def rag_search_gml_docs(query: str, limit: int = GML_RESULT_LIMIT) -> list[dict]:
    """Hybrid retrieval for GML docs: Chroma semantic first, keyword fallback."""
    gml_index = getattr(app.state, "gml_index", None)
    if gml_index is None:
        gml_index = build_gml_index(GML_DOCS_ROOT, source_label="GML")
        app.state.gml_index = gml_index

    snippets = search_gml_docs(query, limit=limit)
    if snippets:
        return snippets
    return _keyword_search_docs(query, gml_index, limit)


def rag_search_ps_docs(query: str, limit: int = PS_RESULT_LIMIT) -> list[dict]:
    """Hybrid retrieval for PowerShell docs: Chroma semantic first, keyword fallback."""
    ps_index = getattr(app.state, "ps_index", None)
    if ps_index is None:
        ps_index = build_gml_index(PS_DOCS_ROOT, source_label="PowerShell")
        app.state.ps_index = ps_index

    snippets = search_ps_docs(query, limit=limit)
    if snippets:
        return snippets
    return _keyword_search_docs(query, ps_index, limit)


def format_gml_snippets(snippets: list[dict]) -> str:
    lines = [
        "The following excerpts were retrieved from the local GameMaker markdown manual under /indexed-docs/gml.",
        "Use them to ground your answer when they are relevant.",
    ]
    for index, snippet in enumerate(snippets, 1):
        lines.append(
            f"\n[{index}] {snippet['path']} :: {snippet['heading']}\n{snippet['content']}"
        )
    return "\n".join(lines)


def format_ps_snippets(snippets: list[dict]) -> str:
    lines = [
        "The following excerpts were retrieved from local PowerShell markdown docs under /indexed-docs/ps-docs.",
        "Use them to ground your answer when they are relevant.",
    ]
    for index, snippet in enumerate(snippets, 1):
        lines.append(
            f"\n[{index}] {snippet['path']} :: {snippet['heading']}\n{snippet['content']}"
        )
    return "\n".join(lines)


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


def get_global_tool_toggles() -> dict:
    cfg = load_config()
    saved = cfg.get("global_tool_toggles", {}) if isinstance(cfg, dict) else {}
    ps_mode = saved.get("use_powershell", "off")
    if ps_mode not in ("off", "native", "docker"):
        ps_mode = "off"
    return {
        "use_gml_docs": bool(saved.get("use_gml_docs", True)),
        "use_ps_docs": bool(saved.get("use_ps_docs", True)),
        "use_file_tools": bool(saved.get("use_file_tools", True)),
        "use_code_interpreter": bool(saved.get("use_code_interpreter", True)),
        "use_powershell": ps_mode,
        "use_mcp_tools": bool(saved.get("use_mcp_tools", True)),
        "use_raw_api": True,
    }


def save_global_tool_toggles(toggles: dict) -> None:
    cfg = load_config()
    ps_mode = str(toggles.get("use_powershell", "off"))
    if ps_mode not in ("off", "native", "docker"):
        ps_mode = "off"
    cfg["global_tool_toggles"] = {
        "use_gml_docs": bool(toggles.get("use_gml_docs", True)),
        "use_ps_docs": bool(toggles.get("use_ps_docs", True)),
        "use_file_tools": bool(toggles.get("use_file_tools", True)),
        "use_code_interpreter": bool(toggles.get("use_code_interpreter", True)),
        "use_powershell": ps_mode,
        "use_mcp_tools": bool(toggles.get("use_mcp_tools", True)),
        # OpenAI-style tool_calls is enforced globally for consistency.
        "use_raw_api": True,
    }
    save_config(cfg)


def _default_user_mcp_config(workspace_root: str) -> dict:
    cfg = {
        "mcpServers": {
            "memory": {
                "command": "npx",
                "args": ["-y", "@modelcontextprotocol/server-memory"],
            },
        }
    }
    if shutil.which("uvx"):
        cfg["mcpServers"]["sqlite"] = {
            "command": "uvx",
            "args": ["mcp-server-sqlite", "--db-path", "memory.db"],
        }
    if workspace_root:
        cfg["mcpServers"]["filesystem"] = {
            "command": "npx",
            "args": ["-y", "@modelcontextprotocol/server-filesystem", "<workspace_root>"],
        }
    return cfg


def _load_user_mcp_config(raw_json: str, workspace_root: str) -> dict:
    if not (raw_json or "").strip():
        return _default_user_mcp_config(workspace_root)
    try:
        data = json.loads(raw_json)
    except json.JSONDecodeError as exc:
        raise HTTPException(status_code=400, detail=f"Invalid stored MCP config JSON: {exc}") from exc
    if not isinstance(data, dict):
        raise HTTPException(status_code=400, detail="MCP config must be a JSON object")
    servers = data.get("mcpServers", {})
    if servers is None:
        servers = {}
    if not isinstance(servers, dict):
        raise HTTPException(status_code=400, detail="mcpServers must be an object")
    return {"mcpServers": servers}


def _resolve_and_validate_user_mcp_config(config: dict, workspace_root: str) -> dict:
    if not isinstance(config, dict):
        raise HTTPException(status_code=400, detail="MCP config must be a JSON object")
    servers = config.get("mcpServers", {})
    if servers is None:
        servers = {}
    if not isinstance(servers, dict):
        raise HTTPException(status_code=400, detail="mcpServers must be an object")

    allowed_commands = {"npx", "uvx"}
    blocked_commands = {"cmd", "powershell", "pwsh", "bash", "sh", "zsh"}

    resolved = {"mcpServers": {}}
    for server_name, server_cfg in servers.items():
        if not isinstance(server_name, str) or not server_name.strip():
            raise HTTPException(status_code=400, detail="mcpServers keys must be non-empty strings")
        if not isinstance(server_cfg, dict):
            raise HTTPException(status_code=400, detail=f"mcpServers.{server_name} must be an object")

        command = str(server_cfg.get("command", "")).strip()
        args = server_cfg.get("args", [])
        if not command:
            raise HTTPException(status_code=400, detail=f"mcpServers.{server_name}.command is required")
        if not isinstance(args, list) or any(not isinstance(x, str) for x in args):
            raise HTTPException(status_code=400, detail=f"mcpServers.{server_name}.args must be a string array")

        cmd_name = Path(command).name.lower()
        if cmd_name in blocked_commands:
            raise HTTPException(status_code=400, detail=f"Command '{command}' is not allowed for MCP servers")
        if cmd_name not in allowed_commands:
            raise HTTPException(
                status_code=400,
                detail=f"Command '{command}' is not allowed. Allowed commands: {sorted(allowed_commands)}",
            )
        if shutil.which(command) is None and shutil.which(cmd_name) is None:
            raise HTTPException(
                status_code=400,
                detail=(
                    f"MCP server '{server_name}' command '{command}' is not on PATH. "
                    "Install the command or update mcp-config."
                ),
            )

        resolved_args: list[str] = []
        for arg in args:
            v = arg.replace("<workspace_root>", workspace_root or "")
            v = v.replace("<db_path>", str(DB_PATH.resolve()))
            if "<workspace_root>" in arg and not workspace_root:
                raise HTTPException(
                    status_code=400,
                    detail=(
                        f"mcpServers.{server_name} references <workspace_root>, "
                        "but this user has no workspace_root configured"
                    ),
                )
            resolved_args.append(v)

        if "@modelcontextprotocol/server-filesystem" in resolved_args:
            if not workspace_root:
                raise HTTPException(
                    status_code=400,
                    detail="filesystem MCP server requires workspace_root to be configured by admin",
                )
            # Enforce exactly one allowed root for filesystem server sandboxing.
            resolved_args = ["-y", "@modelcontextprotocol/server-filesystem", str(Path(workspace_root).resolve())]

        if "mcp-server-sqlite" in resolved_args:
            # Restrict SQLite MCP access to the local application memory DB.
            resolved_args = ["mcp-server-sqlite", "--db-path", str(DB_PATH.resolve())]

        resolved["mcpServers"][server_name] = {
            "command": command,
            "args": resolved_args,
        }
    return resolved


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


async def fts_search(
    db: aiosqlite.Connection,
    conversation_id: str,
    query: str,
    current_user_id: str,
    limit: int = FTS_RESULT_LIMIT,
) -> list[str]:
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
                        JOIN conversations c ON c.id = f.conversation_id
            WHERE messages_fts MATCH ?
              AND f.conversation_id != ?
                            AND c.user_id = ?
            ORDER BY rank
            LIMIT ?
            """,
                        (safe_query, conversation_id, current_user_id, limit),
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
# File Tools — sandboxed local file operations
# ---------------------------------------------------------------------------

MAX_FILE_READ_LINES = 500
MAX_FILE_READ_BYTES = 50_000
MAX_FILE_WRITE_BYTES = 500_000
MAX_GREP_RESULTS = 100


class FileToolError(Exception):
    """Raised by file tools when an operation fails or violates constraints."""
    pass


def resolve_sandboxed_path(workspace_root: str, requested_path: str) -> Path:
    """
    Resolve a requested path relative to workspace_root, with security checks.
    
    Raises PermissionError if the resolved path is outside the root (including symlink escapes).
    Raises FileToolError for other validation failures.
    """
    if not workspace_root or not workspace_root.strip():
        raise FileToolError("Workspace root is not configured")
    
    if not requested_path or not requested_path.strip():
        raise FileToolError("Requested path is empty")
    
    if "\x00" in requested_path:
        raise FileToolError("Path contains null bytes")
    
    root = Path(workspace_root).resolve()
    if not root.exists():
        raise FileToolError(f"Workspace root does not exist: {root}")
    
    target = (root / requested_path).resolve()
    
    # Ensure target is under root (prevents ../ traversal and symlink escapes via resolve())
    try:
        target.relative_to(root)
    except ValueError:
        raise PermissionError(f"Path is outside workspace root: {target}")
    
    return target


def ft_read_file(workspace_root: str, path: str, start_line: int = 1, end_line: int | None = None) -> str:
    """Read a file with line/size limits. Returns truncation notice if limits exceeded."""
    target = resolve_sandboxed_path(workspace_root, path)
    if not target.is_file():
        raise FileToolError(f"Not a file or does not exist: {target}")
    
    content = target.read_text(encoding="utf-8", errors="ignore")
    lines = content.splitlines(keepends=True)
    
    start_idx = max(0, start_line - 1)
    end_idx = end_line if end_line else len(lines)
    
    selected = lines[start_idx:end_idx]
    result = "".join(selected)
    
    # Check size/line limits
    if len(selected) >= MAX_FILE_READ_LINES:
        result += f"\n\n[truncated at {MAX_FILE_READ_LINES} lines]"
    if len(result) >= MAX_FILE_READ_BYTES:
        result = result[:MAX_FILE_READ_BYTES] + f"\n\n[truncated at {MAX_FILE_READ_BYTES} bytes]"
    
    return result


def ft_write_file(workspace_root: str, path: str, content: str) -> str:
    """Write content to a file. Creates parent directories. Returns status message."""
    target = resolve_sandboxed_path(workspace_root, path)
    
    if len(content) > MAX_FILE_WRITE_BYTES:
        raise FileToolError(f"Content exceeds {MAX_FILE_WRITE_BYTES} bytes")
    
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(content, encoding="utf-8")
    return f"Successfully wrote {len(content)} bytes to {target.name}"


def ft_replace_in_file(workspace_root: str, path: str, old_str: str, new_str: str) -> str:
    """Replace exact string in file. Errors if match count != 1."""
    target = resolve_sandboxed_path(workspace_root, path)
    if not target.is_file():
        raise FileToolError(f"Not a file or does not exist: {target}")
    
    content = target.read_text(encoding="utf-8", errors="ignore")
    count = content.count(old_str)
    
    if count == 0:
        raise FileToolError(f"String to replace not found in file")
    if count > 1:
        raise FileToolError(f"String to replace appears {count} times (expected exactly 1)")
    
    new_content = content.replace(old_str, new_str, 1)
    target.write_text(new_content, encoding="utf-8")
    return f"Successfully replaced 1 occurrence in {target.name}"


def ft_list_dir(workspace_root: str, path: str) -> str:
    """List directory contents. Returns names with '/' suffix for directories."""
    requested_path = path
    if path == "" or path == ".":
        target = Path(workspace_root).resolve()
    else:
        target = resolve_sandboxed_path(workspace_root, path)

    log.info("list_dir request: workspace_root=%s requested_path=%r resolved_target=%s", workspace_root, requested_path, target)
    
    if not target.is_dir():
        raise FileToolError(f"Not a directory or does not exist: {target}")
    
    entries = []
    try:
        items = sorted(target.iterdir())
    except PermissionError:
        log.warning("list_dir permission denied: target=%s", target)
        raise FileToolError(f"Permission denied reading directory: {target}")
    
    if len(items) > 500:
        items = items[:500]
        entries.append("[listing truncated at 500 entries]")
    
    for item in items:
        if item.is_dir():
            entries.append(f"{item.name}/")
        else:
            entries.append(item.name)

    log.info("list_dir success: target=%s entries=%d truncated=%s", target, len(items), len(items) >= 500)
    
    return "\n".join(entries)


def ft_search_files(workspace_root: str, pattern: str, directory: str = ".") -> str:
    """Search for files matching a glob pattern. Max 200 results."""
    if not directory or directory == ".":
        search_root = Path(workspace_root).resolve()
    else:
        search_root = resolve_sandboxed_path(workspace_root, directory)
    
    if not search_root.is_dir():
        raise FileToolError(f"Not a directory: {search_root}")
    
    try:
        matches = sorted(search_root.rglob(pattern))[:200]
    except Exception as exc:
        raise FileToolError(f"Glob search failed: {exc}")
    
    if not matches:
        return f"No files matching '{pattern}' found under {directory}"
    
    result_lines = [f"Found {len(matches)} matches for '{pattern}':"]
    for match in matches:
        try:
            rel = match.relative_to(search_root)
            result_lines.append(str(rel))
        except ValueError:
            result_lines.append(str(match))
    
    return "\n".join(result_lines)


def ft_grep_search(workspace_root: str, query: str, path: str, is_regex: bool = False) -> str:
    """Search for query in file(s). Max 100 matches."""
    import re as regex_module
    
    target = resolve_sandboxed_path(workspace_root, path)
    
    if target.is_file():
        files = [target]
    elif target.is_dir():
        files = list(target.rglob("*"))
        files = [f for f in files if f.is_file()]
    else:
        raise FileToolError(f"Not a file or directory: {target}")
    
    matches = []
    for file in files:
        try:
            content = file.read_text(encoding="utf-8", errors="ignore")
        except Exception:
            continue
        
        lines = content.splitlines()
        for line_num, line in enumerate(lines, 1):
            try:
                if is_regex:
                    if regex_module.search(query, line):
                        matches.append(f"{file.name}:{line_num}: {line[:100]}")
                else:
                    if query.lower() in line.lower():
                        matches.append(f"{file.name}:{line_num}: {line[:100]}")
            except Exception:
                continue
            
            if len(matches) >= MAX_GREP_RESULTS:
                matches.append(f"[truncated at {MAX_GREP_RESULTS} matches]")
                return "\n".join(matches)
    
    if not matches:
        return f"No matches for '{query}' found"
    return "\n".join(matches)


def ft_create_directory(workspace_root: str, path: str) -> str:
    """Create a directory (including parents). Returns status message."""
    target = resolve_sandboxed_path(workspace_root, path)
    target.mkdir(parents=True, exist_ok=True)
    return f"Successfully created directory: {target.name}"


def clamp_workspace_subdir(base_workspace_root: str, working_subdir: str) -> Path:
    """
    Resolve a user-selected subdirectory, clamped to workspace root on invalid/escape paths.
    This is the shared guard for user-facing directory selectors.
    """
    base = Path((base_workspace_root or "").strip()).resolve()
    if not str(base_workspace_root or "").strip() or not base.exists():
        return base

    subdir = (working_subdir or "").strip()
    if not subdir:
        return base

    try:
        candidate = resolve_sandboxed_path(str(base), subdir)
        return candidate if candidate.is_dir() else base
    except (PermissionError, FileToolError):
        return base


def clamp_relative_path_or_root(effective_workspace_root: str, path: str) -> Path:
    """
    Resolve a path under effective workspace root, clamping to root if invalid/escape/not-dir.
    """
    root = Path(effective_workspace_root).resolve()
    requested = (path or ".").strip()
    if requested in {"", "."}:
        return root
    try:
        candidate = resolve_sandboxed_path(str(root), requested)
        return candidate if candidate.is_dir() else root
    except (PermissionError, FileToolError):
        return root


def resolve_effective_workspace_root(base_workspace_root: str, working_subdir: str) -> str:
    base = (base_workspace_root or "").strip()
    if not base:
        return base
    return str(clamp_workspace_subdir(base, working_subdir))


# ---------------------------------------------------------------------------
# Routes — auth
# ---------------------------------------------------------------------------

@app.post("/api/auth/login")
async def login(body: LoginRequest):
    username = validate_username(body.username)
    password = validate_password_strength(body.password)

    db = await get_db()
    try:
        cursor = await db.execute(
            "SELECT id, username, password_hash, role, is_active, file_tools_enabled, workspace_root, persona_prompt, mcp_config, created_at FROM users WHERE username=?",
            (username,),
        )
        user = await cursor.fetchone()
        if not user or not verify_password(password, user["password_hash"]):
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid username or password")
        if not user["is_active"]:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="User is inactive")

        token = create_access_token(user["id"])
        return {
            "access_token": token,
            "token_type": "bearer",
            "user": {
                "id": user["id"],
                "username": user["username"],
                "role": user["role"],
                "file_tools_enabled": bool(user["file_tools_enabled"]),
                "workspace_root": user["workspace_root"],
                "persona_prompt": user["persona_prompt"],
                "mcp_config": user["mcp_config"],
                "created_at": user["created_at"],
            },
        }
    finally:
        await db.close()


@app.post("/api/auth/signup")
async def signup(body: SignupRequest):
    username = validate_username(body.username)
    password = validate_password_strength(body.password)
    invite_token = (body.invite_token or "").strip()
    if len(invite_token) < 8:
        raise HTTPException(status_code=400, detail="Invite token is required")

    db = await get_db()
    try:
        cursor = await db.execute(
            """
            SELECT id, token, expires_at, used_by
            FROM invite_tokens
            WHERE token=?
            """,
            (invite_token,),
        )
        invite = await cursor.fetchone()
        if not invite:
            raise HTTPException(status_code=400, detail="Invalid invite token")
        if invite["used_by"]:
            raise HTTPException(status_code=400, detail="Invite token has already been used")

        expiry = parse_iso(invite["expires_at"])
        if expiry and expiry < datetime.now(timezone.utc):
            raise HTTPException(status_code=400, detail="Invite token has expired")

        cursor = await db.execute("SELECT id FROM users WHERE username=?", (username,))
        if await cursor.fetchone():
            raise HTTPException(status_code=409, detail="Username is already taken")

        user_id = str(uuid.uuid4())
        now = now_iso()
        await db.execute(
            """
            INSERT INTO users(id, username, password_hash, role, is_active, created_at)
            VALUES(?, ?, ?, 'user', 1, ?)
            """,
            (user_id, username, hash_password(password), now),
        )
        await db.execute(
            "UPDATE invite_tokens SET used_by=?, used_at=? WHERE id=?",
            (user_id, now, invite["id"]),
        )
        await db.commit()

        token = create_access_token(user_id)
        return {
            "access_token": token,
            "token_type": "bearer",
            "user": {
                "id": user_id,
                "username": username,
                "role": "user",
                "file_tools_enabled": False,
                "workspace_root": "",
                "persona_prompt": "",
                "mcp_config": "",
                "created_at": now,
            },
        }
    finally:
        await db.close()


@app.get("/api/auth/me")
async def auth_me(current_user: dict = Depends(get_current_user)):
    return {
        "id": current_user["id"],
        "username": current_user["username"],
        "role": current_user["role"],
        "file_tools_enabled": bool(current_user["file_tools_enabled"]),
        "workspace_root": current_user["workspace_root"],
        "persona_prompt": current_user.get("persona_prompt", ""),
        "mcp_config": current_user.get("mcp_config", ""),
        "created_at": current_user["created_at"],
    }


@app.get("/api/admin/users")
async def admin_list_users(_: dict = Depends(require_admin)):
    db = await get_db()
    try:
        cursor = await db.execute(
            "SELECT id, username, role, is_active, file_tools_enabled, workspace_root, persona_prompt, mcp_config, created_at FROM users ORDER BY created_at ASC"
        )
        rows = await cursor.fetchall()
        return [dict(r) for r in rows]
    finally:
        await db.close()


@app.get("/api/admin/fs/list")
async def admin_list_filesystem(path: str = Query(""), _: dict = Depends(require_admin)):
    requested = (path or "").strip()

    if not requested:
        if os.name == "nt":
            entries = []
            for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
                drive = Path(f"{letter}:/")
                if drive.exists():
                    entries.append({
                        "name": f"{letter}:/",
                        "is_dir": True,
                        "path": str(drive.resolve()),
                    })
            return {
                "current_path": "",
                "parent_path": "",
                "entries": entries,
            }

        root = Path("/").resolve()
        requested = str(root)

    try:
        target = Path(requested).expanduser()
        if not target.is_absolute():
            target = (Path.cwd() / target).resolve()
        else:
            target = target.resolve()

        if target.is_file():
            target = target.parent
        if not target.exists() or not target.is_dir():
            raise HTTPException(status_code=400, detail=f"Directory does not exist: {target}")

        children = []
        for item in target.iterdir():
            try:
                children.append((not item.is_dir(), item.name.lower(), item))
            except Exception:
                continue

        entries = []
        for _, _, item in sorted(children):
            try:
                entries.append({
                    "name": item.name,
                    "is_dir": item.is_dir(),
                    "path": str(item.resolve()),
                })
            except Exception:
                continue

        parent_path = ""
        try:
            if target.parent != target:
                parent_path = str(target.parent.resolve())
        except Exception:
            parent_path = ""

        return {
            "current_path": str(target),
            "parent_path": parent_path,
            "entries": entries,
        }
    except HTTPException:
        raise
    except PermissionError as exc:
        raise HTTPException(status_code=403, detail=str(exc)) from exc
    except Exception as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc


@app.post("/api/admin/users", status_code=201)
async def admin_create_user(body: AdminCreateUserRequest, _: dict = Depends(require_admin)):
    username = validate_username(body.username)
    password = validate_password_strength(body.password)
    role = (body.role or "user").strip().lower()
    if role not in {"user", "admin"}:
        raise HTTPException(status_code=400, detail="Role must be 'user' or 'admin'")

    db = await get_db()
    try:
        cursor = await db.execute("SELECT id FROM users WHERE username=?", (username,))
        if await cursor.fetchone():
            raise HTTPException(status_code=409, detail="Username is already taken")

        user_id = str(uuid.uuid4())
        ts = now_iso()
        await db.execute(
            """
            INSERT INTO users(id, username, password_hash, role, is_active, created_at)
            VALUES(?, ?, ?, ?, 1, ?)
            """,
            (user_id, username, hash_password(password), role, ts),
        )
        await db.commit()
        return {
            "id": user_id,
            "username": username,
            "role": role,
            "is_active": 1,
            "file_tools_enabled": False,
            "workspace_root": "",
            "persona_prompt": "",
            "mcp_config": "",
            "created_at": ts,
        }
    finally:
        await db.close()


@app.post("/api/admin/invites", status_code=201)
async def admin_create_invite(body: AdminCreateInviteRequest, current_user: dict = Depends(require_admin)):
    days = max(1, min(body.expires_in_days, 30))
    token = secrets.token_urlsafe(16)
    expires = datetime.now(timezone.utc) + timedelta(days=days)
    invite_id = str(uuid.uuid4())

    db = await get_db()
    try:
        await db.execute(
            """
            INSERT INTO invite_tokens(id, token, created_by, expires_at, created_at)
            VALUES(?, ?, ?, ?, ?)
            """,
            (invite_id, token, current_user["id"], expires.isoformat(), now_iso()),
        )
        await db.commit()
        return {"token": token, "expires_at": expires.isoformat()}
    finally:
        await db.close()


@app.delete("/api/admin/users/{user_id}")
async def admin_delete_user(user_id: str, current_user: dict = Depends(require_admin)):
    if user_id == current_user["id"]:
        raise HTTPException(status_code=400, detail="Admins cannot delete their own account")

    db = await get_db()
    try:
        cursor = await db.execute("SELECT id, role FROM users WHERE id=?", (user_id,))
        target = await cursor.fetchone()
        if not target:
            raise HTTPException(status_code=404, detail="User not found")

        if target["role"] == "admin":
            cursor = await db.execute("SELECT COUNT(*) AS cnt FROM users WHERE role='admin' AND is_active=1")
            row = await cursor.fetchone()
            if row and row["cnt"] <= 1:
                raise HTTPException(status_code=400, detail="Cannot delete the last active admin")

        await db.execute("DELETE FROM conversations WHERE user_id=?", (user_id,))
        await db.execute("DELETE FROM users WHERE id=?", (user_id,))
        await db.commit()
        return {"ok": True}
    finally:
        await db.close()


class AdminUpdateUserToolsRequest(BaseModel):
    file_tools_enabled: bool
    workspace_root: str


@app.patch("/api/admin/users/{user_id}")
async def admin_update_user(
    user_id: str,
    body: AdminUpdateUserToolsRequest,
    current_user: dict = Depends(require_admin),
):
    """Update file tool settings for a user."""
    db = await get_db()
    try:
        cursor = await db.execute("SELECT id FROM users WHERE id=?", (user_id,))
        if not await cursor.fetchone():
            raise HTTPException(status_code=404, detail="User not found")

        workspace_root = (body.workspace_root or "").strip()
        await db.execute(
            "UPDATE users SET file_tools_enabled=?, workspace_root=? WHERE id=?",
            (int(body.file_tools_enabled), workspace_root, user_id),
        )
        await db.commit()

        # Return updated user
        cursor = await db.execute(
            "SELECT id, username, role, is_active, file_tools_enabled, workspace_root, persona_prompt, mcp_config, created_at FROM users WHERE id=?",
            (user_id,),
        )
        user = await cursor.fetchone()
        return dict(user) if user else {"ok": True}
    finally:
        await db.close()


@app.post("/api/admin/persona")
async def admin_update_persona(
    body: AdminPersonaUpdateRequest,
    current_user: dict = Depends(require_admin),
):
    persona_prompt = (body.persona_prompt or "").strip()
    if len(persona_prompt) > 8000:
        raise HTTPException(status_code=400, detail="Persona prompt is too long (max 8000 characters)")

    db = await get_db()
    try:
        await db.execute(
            "UPDATE users SET persona_prompt=? WHERE id=?",
            (persona_prompt, current_user["id"]),
        )
        await db.commit()
        return {"ok": True, "persona_prompt": persona_prompt}
    finally:
        await db.close()


@app.get("/api/admin/global-tooling")
async def get_admin_global_tooling(_: dict = Depends(require_admin)):
    return get_global_tool_toggles()


@app.post("/api/admin/global-tooling")
async def update_admin_global_tooling(
    body: AdminGlobalToolingUpdateRequest,
    _: dict = Depends(require_admin),
):
    payload = {
        "use_gml_docs": body.use_gml_docs,
        "use_ps_docs": body.use_ps_docs,
        "use_file_tools": body.use_file_tools,
        "use_code_interpreter": body.use_code_interpreter,
        "use_powershell": body.use_powershell,
        "use_mcp_tools": body.use_mcp_tools,
        "use_raw_api": True,
    }
    save_global_tool_toggles(payload)
    return {"ok": True, **payload}


# ---------------------------------------------------------------------------
# Routes — conversations
# ---------------------------------------------------------------------------

@app.get("/", response_class=HTMLResponse)
async def index():
    return HTMLResponse(HTML_PATH.read_text(encoding="utf-8"))


@app.get("/api/conversations")
async def list_conversations(current_user: dict = Depends(get_current_user)):
    db = await get_db()
    try:
        cursor = await db.execute(
            "SELECT id, title, created_at FROM conversations WHERE user_id=? ORDER BY created_at DESC",
            (current_user["id"],),
        )
        rows = await cursor.fetchall()
        return [dict(r) for r in rows]
    finally:
        await db.close()


@app.post("/api/conversations", status_code=201)
async def create_conversation(body: ConversationCreate, current_user: dict = Depends(get_current_user)):
    conv_id = str(uuid.uuid4())
    db = await get_db()
    try:
        await db.execute(
            "INSERT INTO conversations(id,user_id,title,created_at) VALUES(?,?,?,?)",
            (conv_id, current_user["id"], body.title, now_iso()),
        )
        await db.commit()
        return {"id": conv_id, "title": body.title}
    finally:
        await db.close()


@app.patch("/api/conversations/{conv_id}")
async def rename_conversation(conv_id: str, body: ConversationRename, current_user: dict = Depends(get_current_user)):
    db = await get_db()
    try:
        cursor = await db.execute(
            "UPDATE conversations SET title=? WHERE id=? AND user_id=?",
            (body.title, conv_id, current_user["id"]),
        )
        if cursor.rowcount == 0:
            raise HTTPException(status_code=404, detail="Conversation not found")
        await db.commit()
        return {"ok": True}
    finally:
        await db.close()


@app.delete("/api/conversations/{conv_id}")
async def delete_conversation(conv_id: str, current_user: dict = Depends(get_current_user)):
    db = await get_db()
    try:
        cursor = await db.execute("DELETE FROM conversations WHERE id=? AND user_id=?", (conv_id, current_user["id"]))
        if cursor.rowcount == 0:
            raise HTTPException(status_code=404, detail="Conversation not found")
        await db.commit()
        # Release any active PowerShell session for this conversation
        release_ps_session(f"{current_user['id']}:{conv_id}")
        return {"ok": True}
    finally:
        await db.close()


@app.get("/api/conversations/{conv_id}/messages")
async def get_messages(conv_id: str, current_user: dict = Depends(get_current_user)):
    db = await get_db()
    try:
        cursor = await db.execute("SELECT id FROM conversations WHERE id=? AND user_id=?", (conv_id, current_user["id"]))
        if not await cursor.fetchone():
            raise HTTPException(status_code=404, detail="Conversation not found")

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
async def get_settings(_: dict = Depends(get_current_user)):
    key = get_brave_api_key()
    masked = (key[:4] + "..." + key[-4:]) if len(key) > 8 else ("*" * len(key) if key else "")
    gml_index = await ensure_gml_index_loaded()
    ps_index = await ensure_ps_index_loaded()

    gml_embeddings_enabled = CHROMADB_AVAILABLE and getattr(app.state, "gml_embeddings_ready", False)
    gml_embeddings_building = CHROMADB_AVAILABLE and getattr(app.state, "gml_embeddings_building", False)
    ps_embeddings_enabled = CHROMADB_AVAILABLE and getattr(app.state, "ps_embeddings_ready", False)
    ps_embeddings_building = CHROMADB_AVAILABLE and getattr(app.state, "ps_embeddings_building", False)

    return {
        "brave_api_key_set": bool(key),
        "brave_api_key_masked": masked,
        "global_tool_toggles": get_global_tool_toggles(),
        "gml_docs_enabled": bool(gml_index.get("enabled")),
        "gml_docs_file_count": gml_index.get("file_count", 0),
        "gml_docs_chunk_count": gml_index.get("chunk_count", 0),
        "gml_docs_indexed_at": gml_index.get("indexed_at", ""),
        "gml_docs_error": gml_index.get("error", ""),
        "gml_embeddings_enabled": gml_embeddings_enabled,
        "gml_embeddings_building": gml_embeddings_building,
        "gml_embeddings_model": "all-MiniLM-L6-v2" if gml_embeddings_enabled else None,
        "ps_docs_enabled": bool(ps_index.get("enabled")),
        "ps_docs_file_count": ps_index.get("file_count", 0),
        "ps_docs_chunk_count": ps_index.get("chunk_count", 0),
        "ps_docs_indexed_at": ps_index.get("indexed_at", ""),
        "ps_docs_error": ps_index.get("error", ""),
        "ps_embeddings_enabled": ps_embeddings_enabled,
        "ps_embeddings_building": ps_embeddings_building,
        "ps_embeddings_model": "all-MiniLM-L6-v2" if ps_embeddings_enabled else None,
    }


@app.get("/api/mcp-config")
async def get_mcp_config(current_user: dict = Depends(get_current_user)):
    """Return the current user's MCP server configuration and runtime-resolved status."""
    stored_cfg = _load_user_mcp_config(
        current_user.get("mcp_config", ""),
        current_user.get("workspace_root", ""),
    )
    resolved_cfg = _resolve_and_validate_user_mcp_config(
        stored_cfg,
        current_user.get("workspace_root", ""),
    )
    server_names = sorted(resolved_cfg.get("mcpServers", {}).keys())
    tools_active = [
        {"name": f"mcp:{name}", "description": "Configured MCP server"}
        for name in server_names
    ]
    return {
        "config": stored_cfg,
        "resolved_config": resolved_cfg,
        "tools_active": tools_active,
        "tools_count": len(server_names),
    }


@app.post("/api/mcp-config")
async def update_mcp_config(body: dict, current_user: dict = Depends(get_current_user)):
    """
    Replace the current user's MCP server configuration.

    Body must be a JSON object matching the mcpServers format, e.g.:
    {
      "mcpServers": {
        "memory": {"command": "npx", "args": ["-y", "@modelcontextprotocol/server-memory"]},
        "filesystem": {"command": "npx", "args": ["-y", "@modelcontextprotocol/server-filesystem", "/path"]}
      }
    }
    Pass an empty object {} or {"mcpServers": {}} to clear all MCP servers.
    Use <workspace_root> token for filesystem roots when needed.
    """
    if not isinstance(body, dict):
        raise HTTPException(status_code=400, detail="Body must be a JSON object")

    # Validate + resolve against the authenticated user's sandbox before saving.
    _ = _resolve_and_validate_user_mcp_config(body, current_user.get("workspace_root", ""))

    db = await get_db()
    try:
        await db.execute(
            "UPDATE users SET mcp_config=? WHERE id=?",
            (json.dumps(body, ensure_ascii=True), current_user["id"]),
        )
        await db.commit()
    finally:
        await db.close()

    saved_server_names = sorted((body.get("mcpServers") or {}).keys())
    return {
        "ok": True,
        "tools_count": len(saved_server_names),
        "tools": saved_server_names,
    }


@app.get("/api/code-interpreter/status")
async def code_interpreter_status(_: dict = Depends(get_current_user)):
    """Return whether the Docker-based code interpreter is available."""
    available = await asyncio.to_thread(code_interpreter.is_available)
    return {"available": available}


@app.get("/api/powershell/status")
async def powershell_status(_: dict = Depends(get_current_user)):
    """Return the configured PowerShell execution mode and its availability."""
    toggles = get_global_tool_toggles()
    mode = toggles.get("use_powershell", "off")
    if mode == "off":
        return {"mode": "off", "available": False, "executable": None}
    available = await asyncio.to_thread(is_ps_available, mode)
    if mode == "native" and available:
        import shutil
        exe = shutil.which("pwsh") or shutil.which("powershell")
    else:
        exe = "mcr.microsoft.com/powershell:latest" if mode == "docker" else None
    return {"mode": mode, "available": available, "executable": exe}


@app.post("/api/settings")
async def update_settings(body: SettingsUpdate, _: dict = Depends(get_current_user)):
    cfg = load_config()
    cfg["brave_api_key"] = body.brave_api_key.strip()
    save_config(cfg)
    return {"ok": True}


@app.get("/api/file-tools/list")
async def file_tools_list(
    path: str = Query("."),
    working_subdir: str = Query(""),
    current_user: dict = Depends(get_current_user),
):
    if not bool(current_user.get("file_tools_enabled")):
        raise HTTPException(status_code=403, detail="File tools are disabled for this account")

    base_root = (current_user.get("workspace_root") or "").strip()
    if not base_root:
        raise HTTPException(status_code=400, detail="Workspace root is not configured by admin")

    try:
        effective_root = resolve_effective_workspace_root(base_root, working_subdir)
        root_path = Path(effective_root).resolve()
        target = clamp_relative_path_or_root(effective_root, path)

        entries = []
        for item in sorted(target.iterdir(), key=lambda p: (not p.is_dir(), p.name.lower())):
            entries.append({
                "name": item.name,
                "is_dir": item.is_dir(),
                "path": item.relative_to(root_path).as_posix(),
            })

        current_rel = target.relative_to(root_path).as_posix() if target != root_path else "."
        base_path = Path(base_root).resolve()
        normalized_subdir = ""
        try:
            rel_to_base = root_path.relative_to(base_path)
            normalized_subdir = "" if str(rel_to_base) == "." else rel_to_base.as_posix()
        except ValueError:
            normalized_subdir = ""
        return {
            "working_subdir": normalized_subdir,
            "cwd": current_rel,
            "entries": entries,
        }
    except FileToolError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc
    except PermissionError as exc:
        raise HTTPException(status_code=403, detail=str(exc)) from exc


# ---------------------------------------------------------------------------
# Chat — streaming SSE with native tool calling
# ---------------------------------------------------------------------------

@app.post("/api/chat")
async def chat(req: ChatRequest, current_user: dict = Depends(get_current_user)):
    if not await ensure_ollama_running(wait_seconds=6):
        detail = (
            f"Ollama is not available at {OLLAMA_BASE_URL}."
            if not OLLAMA_IS_LOCAL
            else f"Ollama is not available at {OLLAMA_BASE_URL} and auto-start failed. Start it with `ollama serve`."
        )
        raise HTTPException(
            status_code=503,
            detail=detail,
        )

    global_toggles = get_global_tool_toggles()

    # Effective toggles: admin global switch AND per-request user switch
    use_gml_docs = req.use_gml_docs and global_toggles["use_gml_docs"]
    use_ps_docs = req.use_ps_docs and global_toggles["use_ps_docs"]
    use_file_tools = (
        req.use_file_tools
        and global_toggles["use_file_tools"]
        and bool(current_user.get("file_tools_enabled"))
    )
    use_code_interpreter = req.use_code_interpreter and global_toggles["use_code_interpreter"]
    ps_mode = global_toggles.get("use_powershell", "off")
    use_powershell = req.use_powershell and ps_mode != "off"
    use_mcp_tools = req.use_mcp_tools and global_toggles["use_mcp_tools"]
    effective_workspace_root = resolve_effective_workspace_root(
        current_user.get("workspace_root", ""),
        req.working_subdir,
    )

    use_any_tooling = any([
        req.use_search,
        use_gml_docs,
        use_ps_docs,
        use_file_tools,
        use_code_interpreter,
        use_powershell,
        use_mcp_tools,
    ])

    db = await get_db()
    try:
        cursor = await db.execute(
            "SELECT id FROM conversations WHERE id=? AND user_id=?",
            (req.conversation_id, current_user["id"]),
        )
        if not await cursor.fetchone():
            raise HTTPException(status_code=404, detail="Conversation not found")

        history, was_truncated = await build_active_context(db, req.conversation_id, req.message)

        fts_snippets: list[str] = []
        if was_truncated:
            fts_snippets = await fts_search(db, req.conversation_id, req.message, current_user["id"])
            if fts_snippets:
                log.info("Injecting %d FTS snippet(s) for conv %s", len(fts_snippets), req.conversation_id)

        # Build base message list
        ollama_messages: list[dict] = []
        system_prompt_parts: list[str] = []

        # Global output policy
        system_prompt_parts.append(ENGLISH_ONLY_SYSTEM_PROMPT)

        # Admin persona prompt (hot-loaded from DB per request)
        admin_persona_prompt = (current_user.get("persona_prompt") or "").strip()
        if current_user.get("role") == "admin" and admin_persona_prompt:
            system_prompt_parts.append(admin_persona_prompt)

        # System prompts based on requested features
        if use_gml_docs:
            system_prompt_parts.append(GML_SYSTEM_PROMPT)

        if use_ps_docs:
            system_prompt_parts.append(PS_SYSTEM_PROMPT)

        if use_file_tools:
            if use_mcp_tools:
                system_prompt_parts.append(MCP_FILE_TOOLS_SYSTEM_PROMPT)
            else:
                system_prompt_parts.append(FILE_TOOLS_SYSTEM_PROMPT)

        # Enforce stronger compliance when any tool/MCP path is enabled.
        if use_any_tooling:
            system_prompt_parts.append(TOOL_EXECUTION_CONTRACT_PROMPT)

        # Long-term memory injection
        if fts_snippets:
            snippets_text = "\n\n---\n\n".join(fts_snippets)
            system_prompt_parts.append(
                "The following are relevant excerpts from your long-term memory "
                "(earlier conversations outside the active context window). "
                "Use them if relevant:\n\n" + snippets_text
            )

        if system_prompt_parts:
            ollama_messages.append({
                "role": "system",
                "content": "\n\n".join(part for part in system_prompt_parts if part),
            })

        # Conversation history + new user message
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
        stream_id = uuid.uuid4().hex[:8]
        user_message_preview = re.sub(r"\s+", " ", str(req.message or "")).strip()[:300]
        # Wire per-request context for BaseTool.call() implementations
        set_request_context(
            workspace_root=effective_workspace_root,
            brave_api_key=get_brave_api_key(),
            ps_session_key=f"{current_user['id']}:{req.conversation_id}",
            ps_mode=ps_mode if use_powershell else "off",
        )
        log.info(
            "chat[%s] start user=%s conv=%s model=%s toggles={search:%s,gml:%s,ps:%s,file:%s,code:%s,ps_exec:%s,mcp:%s} workspace=%s",
            stream_id,
            current_user.get("id"),
            req.conversation_id,
            requested_model,
            req.use_search,
            use_gml_docs,
            use_ps_docs,
            use_file_tools,
            use_code_interpreter,
            use_powershell,
            use_mcp_tools,
            effective_workspace_root,
        )
        log.info("chat[%s] user_message=%r", stream_id, user_message_preview)

        all_thinking = ""
        final_content = ""
        tools_called = 0
        searches_done = 0
        code_runs = 0
        powershell_runs = 0
        file_reads = 0
        file_writes = 0
        file_content_writes = 0
        gml_snippet_count = 0
        ps_snippet_count = 0
        seen_tool_call_ids: set[str] = set()
        working_msgs = list(ollama_messages)

        # Some backends require at most one system message and require it first.
        # Collapse any stray system messages from history/tool traces into one.
        collapsed_system_parts: list[str] = []
        non_system_msgs: list[dict] = []
        for msg in working_msgs:
            if isinstance(msg, dict) and msg.get("role") == "system":
                content = str(msg.get("content") or "").strip()
                if content:
                    collapsed_system_parts.append(content)
            else:
                non_system_msgs.append(msg)
        if collapsed_system_parts:
            working_msgs = [{
                "role": "system",
                "content": "\n\n".join(collapsed_system_parts),
            }] + non_system_msgs
        else:
            working_msgs = non_system_msgs

        def _build_agent_function_list(include_mcp_tools: bool = True) -> list:
            """Build Qwen-Agent function_list based on enabled features.

            Strategy: when MCP is active, filesystem operations go through
            the MCP filesystem server.  Only local RAG doc-search tools
            (gml_docs_search, ps_docs_search), web_search and
            code_interpreter remain as native/local tools because they have
            no MCP equivalent.  When MCP is *off*, native file tools are
            used instead.
            """
            tools: list = []
            # Web search — always local (Brave API, no MCP equivalent)
            if req.use_search:
                tools.append("web_search")
            # Filesystem tools — native only when MCP is disabled
            if use_file_tools and not use_mcp_tools:
                tools.extend([
                    "read_file",
                    "write_file",
                    "replace_in_file",
                    "list_dir",
                    "search_files",
                    "grep_search",
                    "create_directory",
                ])
            # Local RAG doc search tools — always local (ChromaDB, no MCP equivalent)
            if use_gml_docs:
                tools.append("gml_docs_search")
            if use_ps_docs:
                tools.append("ps_docs_search")
            # Code interpreter — always local (Docker sandbox, no MCP equivalent)
            if use_code_interpreter and code_interpreter.is_available():
                tools.append("code_interpreter")
            # PowerShell — always local (native or Docker, no MCP equivalent)
            if use_powershell and is_ps_available(ps_mode):
                tools.append("run_powershell")
            # MCP servers — filesystem, memory, sqlite all handled here
            if include_mcp_tools and use_mcp_tools:
                try:
                    user_mcp_config = _load_user_mcp_config(
                        current_user.get("mcp_config", ""),
                        current_user.get("workspace_root", ""),
                    )
                    resolved_mcp_config = _resolve_and_validate_user_mcp_config(
                        user_mcp_config,
                        current_user.get("workspace_root", ""),
                    )
                    if resolved_mcp_config.get("mcpServers"):
                        log.info(
                            "chat[%s] MCP enabled with servers=%s",
                            stream_id,
                            sorted((resolved_mcp_config.get("mcpServers") or {}).keys()),
                        )
                        tools.append(resolved_mcp_config)
                except HTTPException as exc:
                    log.warning(
                        "chat[%s] skipping MCP tools for user %s: %s",
                        stream_id,
                        current_user.get("id"),
                        exc.detail,
                    )
                except Exception as exc:
                    log.warning(
                        "chat[%s] skipping MCP tools for user %s: %s",
                        stream_id,
                        current_user.get("id"),
                        exc,
                    )
            return tools

        def _next_from_iter(it):
            try:
                return True, next(it)
            except StopIteration:
                return False, None

        def _parse_literal_tool_markup(text: str) -> tuple[str, dict] | None:
            """Parse legacy literal tool markup from assistant content.

            Example:
                <function=run_powershell><parameter=code>Get-Location</parameter></function></tool_call>
            """
            if not text:
                return None
            match = LITERAL_TOOL_CALL_RE.search(text)
            if not match:
                return None
            tool_name = (match.group(1) or "").strip()
            body = match.group(2) or ""
            if not tool_name:
                return None
            args: dict[str, object] = {}
            for pm in LITERAL_PARAM_RE.finditer(body):
                key = (pm.group(1) or "").strip()
                value = (pm.group(2) or "").strip()
                if key:
                    args[key] = value
            if not args:
                raw = body.strip()
                if raw:
                    args = {"code": raw}
            return tool_name, args

        def _strip_literal_tool_markup(text: str) -> str:
            if not text:
                return ""
            cleaned = LITERAL_TOOL_CALL_RE.sub("", text)
            cleaned = re.sub(r"</?\s*tool_call\s*>", "", cleaned, flags=re.IGNORECASE)
            return cleaned.strip()

        def _execute_literal_tool_call(tool_name: str, args: dict) -> str:
            """Execute parsed literal tool markup as a fail-open compatibility path."""
            if tool_name == "code_interpreter":
                code = str(args.get("code") or "").strip()
                if not code:
                    return "[Error: code_interpreter requires a non-empty 'code' parameter]"
                if not (use_code_interpreter and code_interpreter.is_available()):
                    return "[Error: code_interpreter is disabled or unavailable]"
                return code_interpreter.call(code)

            if tool_name == "run_powershell":
                code = str(args.get("code") or "").strip()
                if not code:
                    return "[Error: run_powershell requires a non-empty 'code' parameter]"
                if not use_powershell:
                    return "[Error: run_powershell is disabled for this request]"
                if not is_ps_available(ps_mode):
                    return f"[Error: run_powershell mode '{ps_mode}' is unavailable]"
                try:
                    timeout = int(args.get("timeout") or 30)
                except Exception:
                    timeout = 30
                session_key = f"{current_user['id']}:{req.conversation_id}"
                session = get_or_create_ps_session(session_key, ps_mode)
                output, timed_out = session.execute(code, timeout=timeout)
                if timed_out:
                    return f"[Timeout after {timeout}s]" + (f"\n{output}" if output else "")
                return output or "(no output)"

            return f"[Error: Unsupported literal fallback tool: {tool_name}]"

        def _build_function_list_labels(function_list: list) -> list[str]:
            labels: list[str] = []
            for tool_item in function_list:
                if isinstance(tool_item, str):
                    labels.append(tool_item)
                elif isinstance(tool_item, dict):
                    server_names = sorted((tool_item.get("mcpServers") or {}).keys())
                    labels.append(f"mcp_config:{','.join(server_names) if server_names else 'none'}")
                else:
                    labels.append(type(tool_item).__name__)
            return labels

        def _make_agent(include_mcp_tools: bool):
            function_list = _build_agent_function_list(include_mcp_tools=include_mcp_tools)
            log.info("chat[%s] function_list=%s", stream_id, _build_function_list_labels(function_list))
            return Assistant(
                function_list=function_list,
                llm=get_chat_model(llm_cfg),
                system_message="",
            )

        try:
            if not QWEN_AGENT_RUNTIME_AVAILABLE:
                yield f"data: {json.dumps({'type': 'error', 'message': 'qwen-agent runtime is not installed; cannot start Assistant.run()'})}\n\n"
                return

            # Tool-call mode: enforce native OpenAI-style tool_calls for consistent compatibility.
            raw_api_env = (os.getenv("QWEN_AGENT_USE_RAW_API", "") or "").strip().lower()
            if raw_api_env in {"0", "false", "no", "off"}:
                log.warning(
                    "chat[%s] QWEN_AGENT_USE_RAW_API=%r requested prompt-injection mode but raw API is enforced",
                    stream_id,
                    raw_api_env,
                )
            use_raw_api = True
            fncall_prompt_type = (os.getenv("QWEN_AGENT_FNCALL_PROMPT_TYPE", "nous") or "").strip()

            generate_cfg: dict = {"use_raw_api": use_raw_api}
            # fncall_prompt_type is for qwen-agent prompt-injection mode only.
            # In native raw-api mode, providing this can increase protocol drift
            # (model emitting literal <function=...> text instead of tool_calls).
            if (not use_raw_api) and fncall_prompt_type:
                generate_cfg["fncall_prompt_type"] = fncall_prompt_type

            # OpenAI-compatible clients reject unknown top-level args like `think`.
            # Pass reasoning toggle via extra_body for backends (e.g. Ollama) that support it.
            if req.think is not None:
                generate_cfg["extra_body"] = {"think": bool(req.think)}
            log.info(
                "chat[%s] llm generate_cfg use_raw_api=%s fncall_prompt_type=%r think=%s",
                stream_id,
                use_raw_api,
                fncall_prompt_type,
                req.think,
            )

            llm_cfg = {
                "model": requested_model,
                "model_server": OLLAMA_OPENAI_URL,
                "api_key": os.getenv("OPENAI_API_KEY", "EMPTY"),
                "generate_cfg": generate_cfg,
            }

            include_mcp_for_run = True
            try:
                agent = _make_agent(include_mcp_tools=include_mcp_for_run)
            except Exception as exc:
                # Fail-open: if MCP startup fails (missing launcher, server boot failure, etc.),
                # retry once without MCP so chat remains available.
                if use_mcp_tools:
                    log.warning("chat[%s] assistant init with MCP failed; retrying without MCP tools: %s", stream_id, exc)
                    include_mcp_for_run = False
                    agent = _make_agent(include_mcp_tools=False)
                else:
                    raise

            retry_without_mcp_on_eof = bool(use_mcp_tools and include_mcp_for_run)

            while True:
                response_iter = agent.run(messages=working_msgs, lang="en")
                prev_content = ""
                prev_thinking = ""
                seen_function_messages = 0
                emitted_output = False

                try:
                    while True:
                        has_item, rsp = await asyncio.to_thread(_next_from_iter, response_iter)
                        if not has_item:
                            break
                        if not isinstance(rsp, list):
                            continue

                        # Stream content + reasoning deltas.
                        # Scan forward through all messages so the LAST non-empty value wins.
                        # With use_raw_api=True qwen-agent emits separate Message objects for
                        # reasoning_content and response content (not combined), so a single
                        # reversed-lookup would miss one of them.  Both plain dicts and qwen-agent
                        # Message objects (BaseModelCompatibleDict) expose a .get() method.
                        content_now = prev_content
                        thinking_now = prev_thinking
                        for msg in rsp:
                            if not (hasattr(msg, "get") and msg.get("role") == "assistant"):
                                continue
                            c = str(msg.get("content") or "")
                            t = str(msg.get("reasoning_content") or msg.get("thinking") or "")
                            if c:
                                content_now = c
                            if t:
                                thinking_now = t

                        # Some models return reasoning inside <think>...</think> tags in content
                        # instead of reasoning_content. Surface that in the UI thinking stream.
                        tagged_thinking = [
                            m.group(1).strip()
                            for m in THINK_TAG_RE.finditer(content_now)
                            if m.group(1).strip()
                        ]
                        if tagged_thinking:
                            content_now = THINK_TAG_RE.sub("", content_now).strip()
                            tagged_text = "\n\n".join(tagged_thinking)
                            if thinking_now.strip():
                                thinking_now = f"{thinking_now.strip()}\n\n{tagged_text}"
                            else:
                                thinking_now = tagged_text

                        if content_now.startswith(prev_content):
                            content_delta = content_now[len(prev_content):]
                        else:
                            content_delta = content_now
                        if content_delta:
                            emitted_output = True
                            yield f"data: {json.dumps({'type': 'content', 'delta': content_delta})}\n\n"

                        if thinking_now.startswith(prev_thinking):
                            thinking_delta = thinking_now[len(prev_thinking):]
                        else:
                            thinking_delta = thinking_now
                        if thinking_delta:
                            emitted_output = True
                            yield f"data: {json.dumps({'type': 'thinking', 'delta': thinking_delta})}\n\n"

                        prev_content = content_now
                        prev_thinking = thinking_now
                        final_content = content_now
                        all_thinking = thinking_now

                        # Emit tool_call events when assistant tool calls appear in stream snapshots.
                        # qwen-agent may surface these as either `tool_calls` or a legacy `function_call`.
                        for msg in rsp:
                            if not (hasattr(msg, "get") and msg.get("role") == "assistant"):
                                continue

                            tool_calls = msg.get("tool_calls")
                            if isinstance(tool_calls, list):
                                for tc in tool_calls:
                                    if not isinstance(tc, dict):
                                        continue
                                    call_id = str(tc.get("id") or "")
                                    function_info = tc.get("function") if isinstance(tc.get("function"), dict) else {}
                                    tool_name = str(function_info.get("name") or tc.get("name") or "")
                                    args_raw = function_info.get("arguments", tc.get("arguments", {}))
                                    if isinstance(args_raw, str):
                                        try:
                                            args_obj = json.loads(args_raw)
                                        except Exception:
                                            args_obj = {"raw": args_raw}
                                    elif isinstance(args_raw, dict):
                                        args_obj = args_raw
                                    else:
                                        args_obj = {}

                                    if not tool_name:
                                        continue
                                    dedupe_key = call_id or f"{tool_name}:{json.dumps(args_obj, sort_keys=True, ensure_ascii=False)}"
                                    if dedupe_key in seen_tool_call_ids:
                                        continue
                                    seen_tool_call_ids.add(dedupe_key)
                                    yield f"data: {json.dumps({'type': 'tool_call', 'name': tool_name, 'args': args_obj})}\n\n"

                            function_call = msg.get("function_call")
                            if isinstance(function_call, dict):
                                tool_name = str(function_call.get("name") or "")
                                args_raw = function_call.get("arguments", {})
                                if isinstance(args_raw, str):
                                    try:
                                        args_obj = json.loads(args_raw)
                                    except Exception:
                                        args_obj = {"raw": args_raw}
                                elif isinstance(args_raw, dict):
                                    args_obj = args_raw
                                else:
                                    args_obj = {}
                                if tool_name:
                                    dedupe_key = f"legacy:{tool_name}:{json.dumps(args_obj, sort_keys=True, ensure_ascii=False)}"
                                    if dedupe_key not in seen_tool_call_ids:
                                        seen_tool_call_ids.add(dedupe_key)
                                        yield f"data: {json.dumps({'type': 'tool_call', 'name': tool_name, 'args': args_obj})}\n\n"

                        # Track tool execution counts from appended function messages.
                        # Use hasattr(.get) instead of isinstance(dict) so qwen-agent Message
                        # objects (returned by the use_raw_api path) are also detected.
                        function_msgs = [
                            m for m in rsp
                            if hasattr(m, "get") and m.get("role") in ("function", "tool")
                        ]
                        if len(function_msgs) > seen_function_messages:
                            for fm in function_msgs[seen_function_messages:]:
                                tool_name = fm.get("name", "")
                                tool_content = str(fm.get("content") or "")
                                tool_preview = re.sub(r"\s+", " ", tool_content).strip()[:300]
                                log.info(
                                    "chat[%s] tool_result name=%s bytes=%d preview=%r",
                                    stream_id,
                                    tool_name,
                                    len(tool_content),
                                    tool_preview,
                                )
                                if TOOL_ERROR_RE.search(tool_content):
                                    log.warning(
                                        "chat[%s] tool_result indicates error name=%s content=%r",
                                        stream_id,
                                        tool_name,
                                        tool_preview,
                                    )
                                tool_ok = not bool(TOOL_ERROR_RE.search(tool_content))
                                tool_summary = tool_preview if tool_preview else ("ok" if tool_ok else "error")
                                yield f"data: {json.dumps({'type': 'tool_result', 'name': tool_name, 'ok': tool_ok, 'summary': tool_summary})}\n\n"
                                emitted_output = True
                                tools_called += 1
                                if tool_name == "web_search":
                                    searches_done += 1
                                if tool_name == "code_interpreter":
                                    code_runs += 1
                                elif tool_name == "run_powershell":
                                    powershell_runs += 1
                                elif tool_name == "read_file":
                                    file_reads += 1
                                elif tool_name in ("write_file", "replace_in_file", "create_directory"):
                                    file_writes += 1
                                if tool_name in ("write_file", "replace_in_file"):
                                    file_content_writes += 1
                                elif tool_name == "gml_docs_search":
                                    gml_snippet_count += len(re.findall(r"^\[\d+\]", tool_content, flags=re.MULTILINE))
                                elif tool_name == "ps_docs_search":
                                    ps_snippet_count += len(re.findall(r"^\[\d+\]", tool_content, flags=re.MULTILINE))
                            seen_function_messages = len(function_msgs)

                    break
                except Exception as exc:
                    exc_text = str(exc)
                    if retry_without_mcp_on_eof and not emitted_output and "EOF" in exc_text:
                        retry_without_mcp_on_eof = False
                        include_mcp_for_run = False
                        log.warning(
                            "chat[%s] upstream EOF before output; retrying stream once without MCP tools: %s",
                            stream_id,
                            exc_text,
                        )
                        agent = _make_agent(include_mcp_tools=False)
                        continue
                    raise

            # Stream completed successfully
            token_count = estimate_tokens(final_content + all_thinking)
            literal_fallback = _parse_literal_tool_markup(final_content) if tools_called == 0 else None
            if literal_fallback is not None:
                tool_name, args_obj = literal_fallback
                preview = re.sub(r"\s+", " ", final_content).strip()[:280]
                log.warning(
                    "chat[%s] model returned literal tool markup without tool_calls: %r",
                    stream_id,
                    preview,
                )
                if tool_name in {"code_interpreter", "run_powershell"}:
                    yield f"data: {json.dumps({'type': 'tool_call', 'name': tool_name, 'args': args_obj})}\n\n"
                    tool_result = await asyncio.to_thread(_execute_literal_tool_call, tool_name, args_obj)
                    tool_ok = not bool(TOOL_ERROR_RE.search(tool_result))
                    tool_summary = re.sub(r"\s+", " ", tool_result).strip()[:300]
                    yield f"data: {json.dumps({'type': 'tool_result', 'name': tool_name, 'ok': tool_ok, 'summary': tool_summary if tool_summary else ('ok' if tool_ok else 'error')})}\n\n"
                    tools_called += 1
                    if tool_name == "code_interpreter":
                        code_runs += 1
                    elif tool_name == "run_powershell":
                        powershell_runs += 1
                    cleaned_prefix = _strip_literal_tool_markup(final_content)
                    final_content = f"{cleaned_prefix}\n\n{tool_result}".strip() if cleaned_prefix else tool_result
                    fallback_delta = "\n\n" + tool_result
                    yield f"data: {json.dumps({'type': 'content', 'delta': fallback_delta})}\n\n"
                    token_count = estimate_tokens(final_content + all_thinking)
            final_content_preview = re.sub(r"\s+", " ", final_content).strip()[:400]
            final_thinking_preview = re.sub(r"\s+", " ", all_thinking).strip()[:250]
            log.info("chat[%s] final_content=%r", stream_id, final_content_preview)
            if final_thinking_preview:
                log.info("chat[%s] final_thinking=%r", stream_id, final_thinking_preview)
            log.info(
                "chat[%s] done tokens=%d tools=%d code_runs=%d powershell_runs=%d file_reads=%d file_writes=%d",
                stream_id,
                token_count,
                tools_called,
                code_runs,
                powershell_runs,
                file_reads,
                file_writes,
            )
            yield f"data: {json.dumps({'type': 'done', 'token_count': token_count, 'fts_used': bool(fts_snippets), 'tools_called': tools_called, 'searches_done': searches_done, 'commands_run': code_runs, 'code_runs': code_runs, 'powershell_runs': powershell_runs, 'file_reads': file_reads, 'file_writes': file_writes, 'gml_used': gml_snippet_count > 0, 'gml_snippet_count': gml_snippet_count, 'ps_docs_used': ps_snippet_count > 0, 'ps_docs_snippet_count': ps_snippet_count})}\n\n"
        except Exception as exc:
            log.exception("chat[%s] streaming error", stream_id)
            error_text = str(exc)
            error_type = "unknown_error"
            lowered = error_text.lower()
            if "permission" in lowered or "workspace" in lowered or "file" in lowered:
                error_type = "tool_error"
            elif "tool" in lowered or "function" in lowered:
                error_type = "tool_error"
            elif "mcp" in lowered:
                error_type = "mcp_error"
            elif "ollama" in lowered or "connection" in lowered or "eof" in lowered:
                error_type = "connection_error"
            yield f"data: {json.dumps({'type': 'error', 'error_type': error_type, 'message': error_text})}\n\n"
        finally:
            if final_content or all_thinking:
                try:
                    await save_messages(db, req.conversation_id, req.message, final_content, all_thinking)
                except Exception as exc:
                    log.error("chat[%s] failed to save messages: %s", stream_id, exc)
            log.info("chat[%s] stream closed", stream_id)
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
    uvicorn.run(
        "server:app",
        host="0.0.0.0",
        port=42069,
        reload=True,
        reload_excludes=[
            "workspace/tools/code_interpreter/*",
            "workspace/tools/code_interpreter/**",
            "**/launch_kernel_*.py",
            "**/kernel_connection_file_*",
        ],
    )
