"""
Ollama Qwen3 Frontend - FastAPI backend
Serves the HTML frontend and proxies chat requests to Ollama,
with SQLite memory + FTS5 context retrieval.
"""

import asyncio
import concurrent.futures
import hashlib
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
from fnmatch import fnmatch
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

try:
    from tree_sitter_language_pack import get_parser as ts_get_parser
    TREESITTER_AVAILABLE = True
except ImportError:
    try:
        from tree_sitter_languages import get_parser as ts_get_parser
        TREESITTER_AVAILABLE = True
    except ImportError:
        TREESITTER_AVAILABLE = False
        ts_get_parser = None

# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------
OLLAMA_BASE_URL   = os.getenv("OLLAMA_BASE_URL", "http://100.66.64.45:11434").rstrip("/")
OLLAMA_URL        = f"{OLLAMA_BASE_URL}/api/chat"
OLLAMA_HEALTH_URL = f"{OLLAMA_BASE_URL}/api/tags"
OLLAMA_OPENAI_URL = f"{OLLAMA_BASE_URL}/v1"
OLLAMA_AGENTIC_BASE_URL = os.getenv("OLLAMA_AGENTIC_BASE_URL", "http://100.66.64.45:11435").rstrip("/")
OLLAMA_AGENTIC_URL = f"{OLLAMA_AGENTIC_BASE_URL}/api/chat"
OLLAMA_AGENTIC_HEALTH_URL = f"{OLLAMA_AGENTIC_BASE_URL}/api/tags"
OLLAMA_NUM_CTX = int(os.getenv("OLLAMA_NUM_CTX", "128000"))
BRAVE_SEARCH_URL  = "https://api.search.brave.com/res/v1/web/search"
DEFAULT_MODEL     = os.getenv("DEFAULT_MODEL", "qwen3.5:9b-q8_0")
DEFAULT_AGENTIC_MODEL = "qwen3:4b"
DEFAULT_OPENAI_MODEL = os.getenv("DEFAULT_OPENAI_MODEL", "gpt-4.1-mini")
OPENAI_BASE_URL = os.getenv("OPENAI_BASE_URL", "https://api.openai.com/v1").rstrip("/")
OPENAI_MODEL_OPTIONS = [
    "gpt-5.1",
    "gpt-5.2",
    "gpt-5.3-codex",
    "gpt-5.4",
    "gpt-5.4-long-context",
    "gpt-4.1-mini",
    "gpt-4o-mini",
    "o4-mini",
    "o3",
]
DB_PATH           = Path(__file__).parent / "memory.db"
HTML_PATH         = Path(__file__).parent / "index.html"
CONFIG_PATH       = Path(__file__).parent / "config.json"
INDEXED_DOCS_ROOT = Path(__file__).parent / "indexed-docs"
GML_DOCS_ROOT     = INDEXED_DOCS_ROOT / "gml"
PS_DOCS_ROOT      = INDEXED_DOCS_ROOT / "ps-docs"
GML_EMBEDDINGS_DB  = Path(__file__).parent / "gml_embeddings"
PS_EMBEDDINGS_DB   = Path(__file__).parent / "ps_docs_embeddings"
CODEBASE_EMBEDDINGS_DB = Path(__file__).parent / "codebase_embeddings"
TOKEN_CAP              = 20_000  # max tokens kept in active context
FTS_RESULT_LIMIT       = 3       # past-memory snippets to inject when truncated
TOKEN_ESTIMATE_DIVISOR = 4       # chars / 4 ≈ tokens
EDITOR_CONTEXT_CHAR_LIMIT = 12_000
EDITOR_SELECTION_CHAR_LIMIT = 4_000
MAX_SEARCH_ITERATIONS  = 3       # max Brave searches per response
BRAVE_SEARCH_COUNT     = 5       # results to fetch per query
GML_RESULT_LIMIT       = 4       # local GML snippets to inject
PS_RESULT_LIMIT        = 4       # local PowerShell snippets to inject
GML_CHUNK_CHAR_LIMIT   = 1_400   # target chunk size for docs retrieval
HYBRID_CANDIDATE_MULTIPLIER = 3  # per-retriever candidate pool before fusion
HYBRID_FUSION_K        = 60.0    # reciprocal-rank-fusion damping constant
CODEBASE_RESULT_LIMIT  = 6
CODEBASE_MAX_FILES     = 3_000
CODEBASE_MAX_FILE_BYTES = 350_000
CODEBASE_CHUNK_CHAR_LIMIT = 1_600
SSE_HEARTBEAT_SECONDS = 5.0
BACKGROUND_WORKER_TIMEOUT_SECONDS = int(os.getenv("BACKGROUND_WORKER_TIMEOUT", "90"))
CODEBASE_INCLUDE_GLOBS = [
    "*.py", "*.js", "*.jsx", "*.ts", "*.tsx", "*.mjs", "*.cjs", "*.json", "*.md",
    "*.go", "*.rs", "*.java", "*.kt", "*.c", "*.cc", "*.cpp", "*.h", "*.hpp",
    "*.cs", "*.php", "*.rb", "*.swift", "*.scala", "*.sql", "*.yml", "*.yaml", "*.toml",
    "*.ini", "*.ps1", "*.psm1", "*.sh", "*.bash", "Dockerfile", "*.ipynb",
]
CODEBASE_EXCLUDE_PARTS = {
    ".git", ".venv", "venv", "node_modules", "dist", "build", "target", "bin",
    "obj", "coverage", "__pycache__", ".pytest_cache", ".mypy_cache", ".ruff_cache",
    ".idea", ".vscode", "gml_embeddings", "ps_docs_embeddings", "codebase_embeddings",
}
JWT_ALGORITHM          = "HS256"
ACCESS_TOKEN_HOURS     = 24

SEARCH_TAG_RE = re.compile(r'<search>(.*?)</search>', re.IGNORECASE | re.DOTALL)
GML_TOKEN_RE = re.compile(r"[a-zA-Z_][a-zA-Z0-9_]*")
THINK_TAG_RE = re.compile(r"<think>(.*?)</think>", re.IGNORECASE | re.DOTALL)
SMALLTALK_RE = re.compile(
    r"^\s*(?:hi|hello|hey|yo|sup|thanks|thank you|ok|okay|cool|nice|good morning|good night|how are you)\b[\s!?.]*$",
    re.IGNORECASE,
)
SEARCH_INTENT_RE = re.compile(
    r"\b(?:current|latest|today|news|recent|release date|version|price|weather|who is|what is|when did|web|search)\b",
    re.IGNORECASE,
)
FILE_INTENT_RE = re.compile(
    r"\b(?:file|folder|directory|workspace|repo|repository|codebase|read|write|edit|rename|refactor|grep|search files|list files|implement|fix|bug|error|traceback)\b",
    re.IGNORECASE,
)
GML_INTENT_RE = re.compile(
    r"\b(?:gml|gamemaker|sprite|object|room|instance|draw event|step event|manual)\b",
    re.IGNORECASE,
)
POWERSHELL_INTENT_RE = re.compile(
    r"\b(?:powershell|pwsh|cmdlet|script|module|pipeline|invoke-command|ps1)\b",
    re.IGNORECASE,
)
EXECUTION_INTENT_RE = re.compile(
    r"\b(?:run|execute|exec|compute|calculate|debug|automate)\b",
    re.IGNORECASE,
)
# Short-circuit: messages whose primary intent is writing/saving to a path.
# Background helpers are read-only and provide no value for pure write tasks.
WRITE_ONLY_RE = re.compile(
    r"(?:^|\n)\s*(?:(?:ok|okay|please|now|just|then|and|also|great|thanks|thank you|alright|all right|can you|could you)\b[\s,.:;\-]*){0,4}(?:save|write|store|put|output|create)\b[^\n]{0,250}?(?:\bas\b\s+)?(?:[a-zA-Z]:[/\\][\w./\\-]+|[/\\][\w./\\-]+|[\w.-]+\.[a-zA-Z0-9]{1,8}\b)",
    re.IGNORECASE,
)
TOOL_ERROR_RE = re.compile(
    r"^\s*(?:"
    r"\[(?:error|permission denied|timeout|exception)[:\]]|"
    r"error\s*:|permission\s+denied|traceback\s*\(|exception\s*:"
    r")",
    re.IGNORECASE,
)
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
    "Treat hostnames and computer names shown in docs/examples as placeholders unless the user provided them; "
    "do not execute remoting/network commands with placeholder targets and ask for or substitute a real target first. "
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

CODEBASE_INDEX_SYSTEM_PROMPT = (
    "You have access to codebase indexing tools. "
    "When asked about a folder, project area, architecture, or where functionality lives, "
    "call codebase_folder_overview first for structure and call codebase_index_search for deeper evidence. "
    "Ground your answer in returned files/snippets instead of saying you cannot inspect folders. "
    "When reporting results, explain what files do and include short relevant snippets; "
    "do not paste raw tool payloads, raw JSON trees, or unprocessed directory dumps unless explicitly requested."
)

TOOL_EXECUTION_CONTRACT_PROMPT = (
    "Execution-first contract for tool and MCP calls: "
    "If the user request is concrete and executable, do the work first and do not ask clarifying questions. "
    "CRITICAL: When a tool call is needed, make the tool call immediately as your first action — "
    "do NOT output any text, acknowledgment, plan, or preamble before the tool call. "
    "Do not write 'I'll examine...', 'I will check...', 'Let me look...', or any similar planning text before calling a tool. "
    "When a request combines a tool action with follow-up analysis (e.g., 'list files and describe oddities'), "
    "call the required tool(s) first, then synthesize results in your text response afterward. "
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

        # Ensure a signing secret exists (env var preferred, persisted fallback otherwise).
        get_jwt_secret()

        admin = await ensure_bootstrap_admin(db)
        await backfill_legacy_conversations(db, admin["id"])
    finally:
        await db.close()

    await ensure_gml_index_loaded(force=True)
    await ensure_ps_index_loaded(force=True)
    app.state.codebase_index = None
    app.state.codebase_embeddings_ready = False
    app.state.codebase_embeddings_building = False
    app.state.gml_embeddings_ready = False
    app.state.gml_embeddings_building = CHROMADB_AVAILABLE
    app.state.ps_embeddings_ready = False
    app.state.ps_embeddings_building = CHROMADB_AVAILABLE
    app.state.startup_tasks = []
    if CHROMADB_AVAILABLE:
        get_or_init_embedding_model()
        get_or_init_chroma_client("gml")
        get_or_init_chroma_client("ps")
        gml_task = asyncio.create_task(_build_gml_embeddings_background())
        ps_task = asyncio.create_task(_build_ps_embeddings_background())
        app.state.startup_tasks = [gml_task, ps_task]
    log.info("Database initialised at %s", DB_PATH)
    try:
        yield
    finally:
        startup_tasks = list(getattr(app.state, "startup_tasks", []) or [])
        pending_startup = [t for t in startup_tasks if not t.done()]
        if pending_startup:
            for task in pending_startup:
                task.cancel()
            await asyncio.gather(*pending_startup, return_exceptions=True)


app = FastAPI(title="Ollama Qwen3 Chat", lifespan=lifespan)
app.mount("/resources", StaticFiles(directory=Path(__file__).parent / "resources"), name="resources")
_ollama_start_lock = asyncio.Lock()
_gml_index_lock = asyncio.Lock()
_ps_index_lock = asyncio.Lock()
_codebase_index_lock = asyncio.Lock()
_auth_scheme = HTTPBearer(auto_error=False)
_pwd_context = CryptContext(schemes=["pbkdf2_sha256"], deprecated="auto")
_jwt_secret_cache: str | None = None

# Embeddings model (lazy-loaded)
_embedding_model: SentenceTransformerEmbeddingFunction | None = None
_gml_chroma_client = None  # chromadb.PersistentClient, typed loosely to avoid import quirks
_ps_chroma_client = None   # chromadb.PersistentClient, typed loosely to avoid import quirks
_codebase_chroma_client = None  # chromadb.PersistentClient for codebase index

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
    global _jwt_secret_cache

    if _jwt_secret_cache:
        return _jwt_secret_cache

    env_secret = os.environ.get("JWT_SECRET", "").strip()
    if env_secret:
        _jwt_secret_cache = env_secret
        return env_secret

    cfg = load_config()
    stored_secret = str(cfg.get("jwt_secret", "")).strip() if isinstance(cfg, dict) else ""
    if stored_secret:
        _jwt_secret_cache = stored_secret
        return stored_secret

    generated_secret = secrets.token_urlsafe(48)
    if not isinstance(cfg, dict):
        cfg = {}
    cfg["jwt_secret"] = generated_secret
    save_config(cfg)
    _jwt_secret_cache = generated_secret
    log.warning(
        "JWT_SECRET not set; generated persistent secret in config.json. "
        "Set JWT_SECRET in environment to override."
    )
    return generated_secret


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
    model_provider: str = "local"  # "local" (Ollama) | "openai" (ChatGPT API)
    agentic_model: str = DEFAULT_AGENTIC_MODEL  # Used for background tool execution on 11435
    surface: str = "main"
    think: bool = True
    use_search: bool = True
    use_gml_docs: bool = True
    use_ps_docs: bool = False
    use_file_tools: bool = False
    use_code_interpreter: bool = False  # Docker-based sandboxed Python execution
    use_powershell: bool = False  # Persistent PowerShell session (native or Docker)
    use_mcp_tools: bool = True  # Include initialised MCP server tools
    working_subdir: str = ""
    current_file_path: str = ""
    current_file_language: str = ""
    current_file_content: str = ""
    current_file_selection: str = ""
    current_file_cursor_line: int = 0
    current_file_cursor_column: int = 0
    current_file_is_dirty: bool = False


class SettingsUpdate(BaseModel):
    brave_api_key: str | None = None
    llm_provider: str | None = None
    openai_model: str | None = None


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
    default_model: str = DEFAULT_MODEL  # Default main/local model for chat requests
    agentic_endpoint_url: str = OLLAMA_AGENTIC_BASE_URL  # Routing: background tooling endpoint (11435)
    agentic_model: str = DEFAULT_AGENTIC_MODEL  # Model for background tool execution
    agentic_policy: str = "all_tooling"  # "all_tooling" | "heavy_only" (which tools trigger background stage)


class HybridDocsQueryRequest(BaseModel):
    query: str
    source: str = "both"  # "gml" | "ps" | "both"
    limit: int = CODEBASE_RESULT_LIMIT


class CodebaseIndexRebuildRequest(BaseModel):
    working_subdir: str = ""
    force: bool = True


class CodebaseQueryRequest(BaseModel):
    query: str
    limit: int = CODEBASE_RESULT_LIMIT
    working_subdir: str = ""


class FileToolsWriteRequest(BaseModel):
    path: str
    content: str
    working_subdir: str = ""


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


def should_dispatch_background_stage(
    *,
    message: str,
    use_search: bool,
    use_gml_docs: bool,
    use_ps_docs: bool,
    use_file_tools: bool,
    use_code_interpreter: bool,
    use_powershell: bool,
    use_mcp_tools: bool,
) -> tuple[bool, str]:
    """Return (should_dispatch, reason) for background helper stage.

    Goal: avoid spinning up helper/background passes for low-intent small-talk
    while preserving tool-assisted flows for technical/problem-solving prompts.
    """
    text = (message or "").strip()
    if not text:
        return False, "empty prompt"

    if len(text) <= 64 and SMALLTALK_RE.match(text):
        return False, "simple conversational prompt"

    # Early veto: pure write/save-to-path requests.
    # Background helpers are read-only and provide no research value for simple save tasks.
    if WRITE_ONLY_RE.search(text):
        return False, "write-only request (no background research needed)"

    # Execution tools: require actual execution intent in the message, not just
    # that the tool type is globally enabled.
    if use_code_interpreter and EXECUTION_INTENT_RE.search(text):
        return True, "code execution intent detected"
    # PowerShell: require BOTH a PS keyword AND an execution verb to avoid false positives
    # on messages that merely mention .ps1 files in passing (e.g. "save to /path/foo.ps1").
    if use_powershell and POWERSHELL_INTENT_RE.search(text) and EXECUTION_INTENT_RE.search(text):
        return True, "powershell execution intent detected"

    # File/codebase: only worth pre-reading for substantive requests.
    # Short messages (e.g. "save this", "write that") are pure write ops even if file_tools is on.
    if (use_file_tools or use_mcp_tools) and FILE_INTENT_RE.search(text) and len(text) >= 60:
        return True, "file/codebase intent detected"

    if use_gml_docs and GML_INTENT_RE.search(text):
        return True, "gml intent detected"

    if use_ps_docs and POWERSHELL_INTENT_RE.search(text):
        return True, "powershell intent detected"

    if use_search and SEARCH_INTENT_RE.search(text):
        return True, "search intent detected"

    return False, "no helper intent detected"


def _clip_editor_context(text: str, limit: int) -> tuple[str, bool]:
    compact = str(text or "")
    if len(compact) <= limit:
        return compact, False
    omitted = len(compact) - limit
    return compact[:limit].rstrip() + f"\n\n[... truncated {omitted} characters ...]", True


def build_editor_context_prompt(req: ChatRequest) -> str:
    file_path = (req.current_file_path or "").strip()
    if not file_path:
        return ""

    parts = [
        "You are operating from an editor side panel attached to the current file.",
        f"Focused file: {file_path}",
    ]

    language = (req.current_file_language or "").strip()
    if language:
        parts.append(f"Language: {language}")

    if req.current_file_cursor_line > 0:
        parts.append(
            "Cursor: "
            f"line {req.current_file_cursor_line}, column {max(1, req.current_file_cursor_column)}"
        )

    parts.append(f"Buffer state: {'unsaved changes present' if req.current_file_is_dirty else 'matches saved content'}")

    selection = (req.current_file_selection or "").strip()
    if selection:
        clipped_selection, selection_truncated = _clip_editor_context(
            selection,
            EDITOR_SELECTION_CHAR_LIMIT,
        )
        selection_note = "Selection (truncated):" if selection_truncated else "Selection:"
        parts.append(f"{selection_note}\n{clipped_selection}")

    content = (req.current_file_content or "").strip()
    if content:
        clipped_content, content_truncated = _clip_editor_context(content, EDITOR_CONTEXT_CHAR_LIMIT)
        content_label = "Current buffer excerpt (truncated):" if content_truncated else "Current buffer:"
        parts.append(f"{content_label}\n{clipped_content}")

    parts.append(
        "When proposing edits or analysis, prioritize this focused file context before exploring other files."
    )
    return "\n\n".join(parts)


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


def _should_include_code_file(path: Path) -> bool:
    name = path.name
    return any(fnmatch(name, pattern) for pattern in CODEBASE_INCLUDE_GLOBS)


def _chunk_code_content(content: str, limit: int = CODEBASE_CHUNK_CHAR_LIMIT) -> list[str]:
    compact = (content or "").strip()
    if not compact:
        return []
    paragraphs = [part.strip() for part in re.split(r"\n\s*\n", compact) if part.strip()]
    if not paragraphs:
        paragraphs = [compact]

    chunks: list[str] = []
    current = ""
    for paragraph in paragraphs:
        candidate = (current + "\n\n" + paragraph).strip() if current else paragraph
        if len(candidate) <= limit:
            current = candidate
            continue
        if current:
            chunks.append(current)
            current = ""
        if len(paragraph) <= limit:
            current = paragraph
            continue
        start = 0
        while start < len(paragraph):
            chunk = paragraph[start:start + limit].strip()
            if chunk:
                chunks.append(chunk)
            start += limit
    if current:
        chunks.append(current)
    return chunks


def _tree_sitter_language_for_path(path: Path) -> str | None:
    suffix = path.suffix.lower()
    mapping = {
        ".py": "python",
        ".js": "javascript",
        ".jsx": "javascript",
        ".ts": "typescript",
        ".tsx": "typescript",
        ".go": "go",
        ".rs": "rust",
        ".java": "java",
        ".c": "c",
        ".h": "c",
        ".cc": "cpp",
        ".cpp": "cpp",
        ".hpp": "cpp",
        ".cs": "c_sharp",
        ".rb": "ruby",
        ".php": "php",
        ".swift": "swift",
        ".kt": "kotlin",
    }
    return mapping.get(suffix)


def _extract_symbols_tree_sitter(path: Path, content: str) -> list[str]:
    if not TREESITTER_AVAILABLE or not ts_get_parser:
        return []
    language = _tree_sitter_language_for_path(path)
    if not language:
        return []
    try:
        parser = ts_get_parser(language)
        source_bytes = content.encode("utf-8", errors="ignore")
        tree = parser.parse(source_bytes)
    except Exception:
        return []

    symbols: list[str] = []

    def walk(node) -> None:
        node_type = str(getattr(node, "type", "") or "")
        if "identifier" in node_type or node_type in {
            "function_definition",
            "function_declaration",
            "method_definition",
            "class_definition",
            "type_identifier",
        }:
            start = int(getattr(node, "start_byte", 0) or 0)
            end = int(getattr(node, "end_byte", 0) or 0)
            if end > start:
                text = source_bytes[start:end].decode("utf-8", errors="ignore").strip()
                text = re.sub(r"\s+", " ", text)
                if 1 <= len(text) <= 80 and re.match(r"^[A-Za-z_][A-Za-z0-9_:\.\-]*$", text):
                    symbols.append(text)
        for child in getattr(node, "children", []) or []:
            walk(child)

    walk(getattr(tree, "root_node", None))
    if not symbols:
        return []
    return list(dict.fromkeys(symbols))[:80]


def _extract_symbols_regex(content: str) -> list[str]:
    patterns = [
        r"^\s*def\s+([A-Za-z_][A-Za-z0-9_]*)\s*\(",
        r"^\s*class\s+([A-Za-z_][A-Za-z0-9_]*)\b",
        r"^\s*function\s+([A-Za-z_][A-Za-z0-9_]*)\s*\(",
        r"^\s*(?:const|let|var)\s+([A-Za-z_][A-Za-z0-9_]*)\s*=\s*(?:async\s*)?\(",
    ]
    out: list[str] = []
    for pattern in patterns:
        out.extend(re.findall(pattern, content or "", flags=re.MULTILINE))
    if not out:
        return []
    return list(dict.fromkeys(out))[:80]


def build_codebase_index(root: Path) -> dict:
    stats = {
        "enabled": root.exists() and root.is_dir(),
        "root": str(root),
        "file_count": 0,
        "chunk_count": 0,
        "indexed_at": now_iso(),
        "chunks": [],
        "error": "",
        "treesitter_enabled": TREESITTER_AVAILABLE,
    }
    if not root.exists() or not root.is_dir():
        stats["error"] = f"Codebase root not found: {root}"
        return stats

    chunks: list[dict] = []
    files_seen = 0
    for file_path in sorted(root.rglob("*")):
        if files_seen >= CODEBASE_MAX_FILES:
            break
        if not file_path.is_file():
            continue
        if any(part in CODEBASE_EXCLUDE_PARTS for part in file_path.parts):
            continue
        if not _should_include_code_file(file_path):
            continue
        try:
            if file_path.stat().st_size > CODEBASE_MAX_FILE_BYTES:
                continue
            raw_text = file_path.read_text(encoding="utf-8", errors="ignore")
        except Exception:
            continue

        files_seen += 1
        rel_path = file_path.relative_to(root).as_posix()
        symbols = _extract_symbols_tree_sitter(file_path, raw_text)
        if not symbols:
            symbols = _extract_symbols_regex(raw_text)
        symbol_blob = " ".join(symbols[:50])
        heading = symbols[0] if symbols else file_path.stem

        for chunk_index, chunk_text in enumerate(_chunk_code_content(raw_text)):
            searchable = f"{rel_path}\n{heading}\n{symbol_blob}\n{chunk_text}"
            chunks.append(
                {
                    "path": rel_path,
                    "title": file_path.name,
                    "heading": heading,
                    "chunk_index": chunk_index,
                    "content": chunk_text,
                    "symbols": symbols,
                    "searchable": searchable.lower(),
                    "tokens": Counter(tokenize_search_text(searchable)),
                }
            )

        stats["file_count"] += 1

    stats["chunk_count"] = len(chunks)
    stats["chunks"] = chunks
    return stats


async def ensure_codebase_index_loaded(workspace_root: str, force: bool = False) -> dict:
    root = Path((workspace_root or "").strip() or Path(__file__).parent).resolve()
    current_index = getattr(app.state, "codebase_index", None)
    if (
        current_index is not None
        and not force
        and str(current_index.get("root", "")) == str(root)
    ):
        return current_index

    async with _codebase_index_lock:
        current_index = getattr(app.state, "codebase_index", None)
        if (
            current_index is not None
            and not force
            and str(current_index.get("root", "")) == str(root)
        ):
            return current_index

        codebase_index = await asyncio.to_thread(build_codebase_index, root)
        app.state.codebase_index = codebase_index
        app.state.codebase_embeddings_ready = False
        log.info(
            "Codebase index ready: root=%s files=%d chunks=%d",
            root,
            codebase_index.get("file_count", 0),
            codebase_index.get("chunk_count", 0),
        )
        if codebase_index.get("error"):
            log.warning("Codebase index warning: %s", codebase_index.get("error"))
        return codebase_index


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
    global _gml_chroma_client, _ps_chroma_client, _codebase_chroma_client

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

    if kind == "codebase":
        if _codebase_chroma_client is None:
            try:
                CODEBASE_EMBEDDINGS_DB.mkdir(parents=True, exist_ok=True)
                _codebase_chroma_client = chromadb.PersistentClient(path=str(CODEBASE_EMBEDDINGS_DB))
                log.info("Codebase Chroma persistent client initialized at %s", CODEBASE_EMBEDDINGS_DB)
            except Exception as exc:
                log.error("Failed to initialize Codebase Chroma client: %s", exc)
                return None
        return _codebase_chroma_client

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


def _codebase_collection_name(root: str) -> str:
    root_hash = hashlib.sha1((root or "").encode("utf-8", errors="ignore")).hexdigest()[:16]
    return f"codebase_docs_{root_hash}"


async def build_codebase_embeddings_collection(codebase_index: dict) -> dict:
    """Build embeddings for the active codebase index."""
    if not CHROMADB_AVAILABLE:
        return {
            "enabled": False,
            "error": "chromadb not available; install with: pip install chromadb sentence-transformers",
            "chunk_count": 0,
        }
    if not codebase_index or not codebase_index.get("chunks"):
        return {
            "enabled": False,
            "error": "Codebase index not found; cannot build embeddings",
            "chunk_count": 0,
        }
    root = str(codebase_index.get("root", ""))
    return await asyncio.to_thread(
        _chromadb_build_sync,
        codebase_index["chunks"],
        collection_name=_codebase_collection_name(root),
        source_label="Codebase",
        client_kind="codebase",
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


def search_codebase_docs(query: str, root: str, limit: int = CODEBASE_RESULT_LIMIT) -> list[dict]:
    """Search workspace codebase using vector embeddings (semantic search)."""
    return _search_docs(
        query,
        limit=limit,
        collection_name=_codebase_collection_name(root),
        source_label="Codebase",
        client_kind="codebase",
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


def _heuristic_search_docs(query: str, index: dict, limit: int) -> list[dict]:
    """Heuristic lexical retrieval that emphasizes token overlap and path/heading intent."""
    chunks = index.get("chunks", []) if isinstance(index, dict) else []
    if not chunks:
        return []

    query_compact = " ".join((query or "").lower().split())
    query_tokens = Counter(tokenize_search_text(query))
    if not query_tokens and not query_compact:
        return []

    scored: list[tuple[float, dict]] = []
    for chunk in chunks:
        chunk_tokens: Counter = chunk.get("tokens", Counter())
        searchable = str(chunk.get("searchable", "") or "")
        heading = str(chunk.get("heading", "") or "").lower()
        title = str(chunk.get("title", "") or "").lower()
        path = str(chunk.get("path", "") or "").lower()

        score = 0.0
        overlap = 0
        for token, qtf in query_tokens.items():
            ctf = float(chunk_tokens.get(token, 0))
            if ctf:
                overlap += 1
                score += min(ctf, 3.0) * float(qtf)
                if token in heading:
                    score += 0.9
                if token in title:
                    score += 0.7
                if token in path:
                    score += 0.5

        if query_compact:
            if query_compact in searchable:
                score += 5.0
            elif all(token in searchable for token in query_tokens):
                score += 2.0

        if query_tokens:
            score += (overlap / max(len(query_tokens), 1)) * 1.5

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
                "retrieval_sources": ["heuristic"],
            }
        )
    return selected


def _ripgrep_like_search_docs(query: str, index: dict, limit: int) -> list[dict]:
    """Ripgrep-style lexical retrieval over chunk text using regex + token overlap."""
    chunks = index.get("chunks", []) if isinstance(index, dict) else []
    if not chunks:
        return []

    query_text = (query or "").strip()
    if not query_text:
        return []
    query_tokens = Counter(tokenize_search_text(query_text))

    regex = None
    try:
        regex = re.compile(query_text, re.IGNORECASE)
    except re.error:
        regex = None

    scored: list[tuple[float, dict]] = []
    for chunk in chunks:
        searchable = str(chunk.get("searchable", "") or "")
        content = str(chunk.get("content", "") or "")
        chunk_tokens: Counter = chunk.get("tokens", Counter())

        score = 0.0
        if query_text.lower() in searchable:
            score += 4.0
        if regex is not None:
            match_count = len(regex.findall(content))
            if match_count:
                score += min(match_count, 6) * 1.3

        for token, qtf in query_tokens.items():
            ctf = float(chunk_tokens.get(token, 0))
            if ctf:
                score += min(ctf, 4.0) * float(qtf)

        if score > 0:
            scored.append((score, chunk))

    if not scored:
        return []

    scored.sort(key=lambda x: x[0], reverse=True)
    selected: list[dict] = []
    for score, chunk in scored[:limit]:
        selected.append(
            {
                "score": score,
                "path": chunk.get("path", ""),
                "heading": chunk.get("heading", ""),
                "content": chunk.get("content", ""),
                "retrieval_sources": ["ripgrep-like"],
            }
        )
    return selected


def _hybrid_merge_retrieval_results(
    semantic_results: list[dict],
    heuristic_results: list[dict],
    limit: int,
) -> list[dict]:
    """Fuse parallel retriever outputs into a single ranked list with source attribution."""
    if not semantic_results and not heuristic_results:
        return []

    fused: dict[tuple[str, str, str], dict] = {}

    semantic_max = max((max(0.0, float(r.get("score", 0.0))) for r in semantic_results), default=1.0)
    heuristic_max = max((max(0.0, float(r.get("score", 0.0))) for r in heuristic_results), default=1.0)

    def key_for(item: dict) -> tuple[str, str, str]:
        content = str(item.get("content", "") or "")
        return (
            str(item.get("path", "") or ""),
            str(item.get("heading", "") or ""),
            content[:220],
        )

    def upsert(
        ranked: list[dict],
        source: str,
        score_weight: float,
        score_max: float,
    ) -> None:
        for rank_idx, item in enumerate(ranked, 1):
            item_key = key_for(item)
            if item_key not in fused:
                fused[item_key] = {
                    "path": item.get("path", ""),
                    "heading": item.get("heading", ""),
                    "content": item.get("content", ""),
                    "score": 0.0,
                    "retrieval_sources": set(),
                }

            entry = fused[item_key]
            entry["retrieval_sources"].add(source)
            rrf = 1.0 / (HYBRID_FUSION_K + rank_idx)
            raw_score = max(0.0, float(item.get("score", 0.0)))
            norm_score = raw_score / score_max if score_max > 0 else 0.0
            entry["score"] += rrf + (norm_score * score_weight)

    # Slightly favor semantic ranking while still giving lexical retrieval strong influence.
    upsert(semantic_results, source="semantic", score_weight=0.65, score_max=semantic_max)
    upsert(heuristic_results, source="heuristic", score_weight=0.35, score_max=heuristic_max)

    merged = list(fused.values())
    merged.sort(key=lambda x: float(x.get("score", 0.0)), reverse=True)
    output: list[dict] = []
    for item in merged[:limit]:
        output.append(
            {
                "score": float(item.get("score", 0.0)),
                "path": item.get("path", ""),
                "heading": item.get("heading", ""),
                "content": item.get("content", ""),
                "retrieval_sources": sorted(item.get("retrieval_sources", set())),
            }
        )
    return output


def _run_hybrid_docs_retrieval(
    query: str,
    index: dict,
    *,
    semantic_search_fn,
    lexical_search_fn=_heuristic_search_docs,
    limit: int,
) -> list[dict]:
    """Execute semantic + heuristic retrieval in parallel and fuse their results."""
    candidate_limit = max(limit * HYBRID_CANDIDATE_MULTIPLIER, limit)

    semantic_results: list[dict] = []
    heuristic_results: list[dict] = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        semantic_future = executor.submit(semantic_search_fn, query, candidate_limit)
        heuristic_future = executor.submit(lexical_search_fn, query, index, candidate_limit)
        try:
            semantic_results = semantic_future.result(timeout=12)
        except Exception as exc:
            log.warning("Semantic retriever failed for query=%r: %s", query, exc)
        try:
            heuristic_results = heuristic_future.result(timeout=12)
        except Exception as exc:
            log.warning("Heuristic retriever failed for query=%r: %s", query, exc)

    return _hybrid_merge_retrieval_results(semantic_results, heuristic_results, limit)


def rag_search_gml_docs(query: str, limit: int = GML_RESULT_LIMIT) -> list[dict]:
    """Hybrid retrieval for GML docs: semantic + heuristic in parallel with rank fusion."""
    gml_index = getattr(app.state, "gml_index", None)
    if gml_index is None:
        gml_index = build_gml_index(GML_DOCS_ROOT, source_label="GML")
        app.state.gml_index = gml_index

    snippets = _run_hybrid_docs_retrieval(
        query,
        gml_index,
        semantic_search_fn=search_gml_docs,
        limit=limit,
    )
    if snippets:
        return snippets
    return _keyword_search_docs(query, gml_index, limit)


def rag_search_ps_docs(query: str, limit: int = PS_RESULT_LIMIT) -> list[dict]:
    """Hybrid retrieval for PowerShell docs: semantic + heuristic in parallel with rank fusion."""
    ps_index = getattr(app.state, "ps_index", None)
    if ps_index is None:
        ps_index = build_gml_index(PS_DOCS_ROOT, source_label="PowerShell")
        app.state.ps_index = ps_index

    snippets = _run_hybrid_docs_retrieval(
        query,
        ps_index,
        semantic_search_fn=search_ps_docs,
        limit=limit,
    )
    if snippets:
        return snippets
    return _keyword_search_docs(query, ps_index, limit)


async def rag_search_codebase_docs(query: str, workspace_root: str, limit: int = CODEBASE_RESULT_LIMIT) -> list[dict]:
    """Hybrid retrieval for workspace codebase: semantic + ripgrep-like lexical in parallel."""
    codebase_index = await ensure_codebase_index_loaded(workspace_root)
    if not codebase_index.get("chunks"):
        return []

    if CHROMADB_AVAILABLE and not getattr(app.state, "codebase_embeddings_ready", False):
        app.state.codebase_embeddings_building = True
        try:
            emb_result = await build_codebase_embeddings_collection(codebase_index)
            app.state.codebase_embeddings_ready = bool(emb_result.get("enabled"))
        finally:
            app.state.codebase_embeddings_building = False

    root = str(codebase_index.get("root", ""))

    def _semantic(query_text: str, query_limit: int) -> list[dict]:
        results = search_codebase_docs(query_text, root=root, limit=query_limit)
        for item in results:
            item["retrieval_sources"] = ["semantic"]
        return results

    hybrid = _run_hybrid_docs_retrieval(
        query,
        codebase_index,
        semantic_search_fn=_semantic,
        lexical_search_fn=_ripgrep_like_search_docs,
        limit=limit,
    )
    if hybrid:
        return hybrid
    return _ripgrep_like_search_docs(query, codebase_index, limit)


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


def format_codebase_snippets(snippets: list[dict]) -> str:
    lines = [
        "The following excerpts were retrieved from the current workspace codebase index.",
        "Use them as grounding context for project-specific APIs, symbols, and file structure.",
    ]
    for index, snippet in enumerate(snippets, 1):
        sources = ",".join(snippet.get("retrieval_sources", []))
        source_text = f" [{sources}]" if sources else ""
        lines.append(
            f"\n[{index}] {snippet.get('path', '')} :: {snippet.get('heading', '')}{source_text}\n{snippet.get('content', '')}"
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


def get_openai_api_key() -> str:
    """Return OpenAI API key from environment only (loaded from .env at startup)."""
    return os.environ.get("OPENAI_API_KEY", "")


def get_default_local_model() -> str:
    """Return default local chat model (env default overridable via config)."""
    cfg = load_config()
    model = str(cfg.get("default_model", DEFAULT_MODEL)).strip()
    if not model:
        model = DEFAULT_MODEL
    return normalize_model_name(model)


def save_default_local_model(model: str) -> str:
    """Persist default local chat model to config.json and return normalized value."""
    normalized = normalize_model_name(model)
    cfg = load_config()
    cfg["default_model"] = normalized
    save_config(cfg)
    return normalized


def get_llm_provider_config() -> dict:
    """Load LLM provider config from config.json."""
    cfg = load_config()
    saved = cfg.get("llm_provider", {}) if isinstance(cfg, dict) else {}

    provider = str(saved.get("provider", "local")).strip().lower()
    if provider not in {"local", "openai"}:
        provider = "local"

    openai_model = str(saved.get("openai_model", DEFAULT_OPENAI_MODEL)).strip()
    if not openai_model:
        openai_model = DEFAULT_OPENAI_MODEL

    return {
        "provider": provider,
        "openai_model": openai_model,
    }


def save_llm_provider_config(provider_config: dict) -> None:
    """Persist LLM provider config to config.json."""
    cfg = load_config()
    provider = str(provider_config.get("provider", "local")).strip().lower()
    if provider not in {"local", "openai"}:
        provider = "local"

    openai_model = str(provider_config.get("openai_model", DEFAULT_OPENAI_MODEL)).strip()
    if not openai_model:
        openai_model = DEFAULT_OPENAI_MODEL

    cfg["llm_provider"] = {
        "provider": provider,
        "openai_model": openai_model,
    }
    save_config(cfg)


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


async def is_ollama_endpoint_running(health_url: str, timeout_seconds: float = 1.5) -> bool:
    """Return True when an Ollama endpoint responds to /api/tags (generic health check)."""
    try:
        timeout = aiohttp.ClientTimeout(total=timeout_seconds)
        async with aiohttp.ClientSession(timeout=timeout) as session:
            async with session.get(health_url) as resp:
                return resp.status == 200
    except Exception:
        return False


async def select_available_helper_endpoints(
    endpoint_urls: list[str],
    timeout_seconds: float = 1.5,
) -> list[str]:
    """Return reachable helper endpoints in preferred order."""
    seen: set[str] = set()
    normalized: list[str] = []
    for url in endpoint_urls:
        base = str(url or "").strip().rstrip("/")
        if not base or base in seen:
            continue
        seen.add(base)
        normalized.append(base)

    if not normalized:
        return []

    checks = await asyncio.gather(
        *[
            is_ollama_endpoint_running(f"{base}/api/tags", timeout_seconds=timeout_seconds)
            for base in normalized
        ],
        return_exceptions=True,
    )

    available: list[str] = []
    for base, result in zip(normalized, checks):
        if isinstance(result, Exception):
            continue
        if result:
            available.append(base)
    return available


def get_model_routing_config() -> dict:
    """Load model routing config from config.json with defaults for dual-endpoint setup."""
    cfg = load_config()
    saved = cfg.get("model_routing", {}) if isinstance(cfg, dict) else {}
    
    endpoint_url = str(saved.get("agentic_endpoint_url", OLLAMA_AGENTIC_BASE_URL)).strip()
    if not endpoint_url:
        endpoint_url = OLLAMA_AGENTIC_BASE_URL
    
    model = str(saved.get("agentic_model", DEFAULT_AGENTIC_MODEL)).strip()
    if not model:
        model = DEFAULT_AGENTIC_MODEL
    
    policy = str(saved.get("agentic_policy", "all_tooling")).strip()
    if policy not in ("all_tooling", "heavy_only"):
        policy = "all_tooling"
    
    return {
        "agentic_endpoint_url": endpoint_url,
        "agentic_model": model,
        "agentic_policy": policy,
    }


def save_model_routing_config(routing: dict) -> None:
    """Persist model routing config to config.json."""
    cfg = load_config()
    
    endpoint_url = str(routing.get("agentic_endpoint_url", OLLAMA_AGENTIC_BASE_URL)).strip()
    if not endpoint_url:
        endpoint_url = OLLAMA_AGENTIC_BASE_URL
    
    model = str(routing.get("agentic_model", DEFAULT_AGENTIC_MODEL)).strip()
    if not model:
        model = DEFAULT_AGENTIC_MODEL
    
    policy = str(routing.get("agentic_policy", "all_tooling")).strip()
    if policy not in ("all_tooling", "heavy_only"):
        policy = "all_tooling"
    
    cfg["model_routing"] = {
        "agentic_endpoint_url": endpoint_url,
        "agentic_model": model,
        "agentic_policy": policy,
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


async def _fts_search_only(
    db: aiosqlite.Connection,
    conversation_id: str,
    query: str,
    current_user_id: str,
    limit: int,
) -> list[dict]:
    safe_query = " ".join(word for word in query.split() if word.isalnum() or len(word) > 2)
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
        return [
            {
                "content": row["content"],
                "score": float(limit - i),
                "retrieval_sources": ["fts"],
            }
            for i, row in enumerate(rows)
        ]
    except Exception as exc:
        log.warning("FTS search failed: %s", exc)
        return []


async def _lexical_memory_search(
    conversation_id: str,
    query: str,
    current_user_id: str,
    limit: int,
) -> list[dict]:
    query_tokens = Counter(tokenize_search_text(query))
    if not query_tokens:
        return []
    temp_db = await get_db()
    try:
        cursor = await temp_db.execute(
            """
            SELECT m.content
            FROM messages m
            JOIN conversations c ON c.id = m.conversation_id
            WHERE m.conversation_id != ?
              AND c.user_id = ?
            ORDER BY m.id DESC
            LIMIT 600
            """,
            (conversation_id, current_user_id),
        )
        rows = await cursor.fetchall()
    except Exception as exc:
        log.warning("Lexical memory search failed: %s", exc)
        await temp_db.close()
        return []

    scored: list[tuple[float, str]] = []
    for row in rows:
        content = str(row["content"] or "")
        tokens = Counter(tokenize_search_text(content))
        score = 0.0
        for token, qtf in query_tokens.items():
            ctf = float(tokens.get(token, 0))
            if ctf:
                score += min(ctf, 4.0) * float(qtf)
        if score > 0:
            scored.append((score, content))

    await temp_db.close()

    if not scored:
        return []
    scored.sort(key=lambda x: x[0], reverse=True)
    return [
        {
            "content": content,
            "score": score,
            "retrieval_sources": ["lexical"],
        }
        for score, content in scored[:limit]
    ]


def _merge_memory_results(fts_results: list[dict], lexical_results: list[dict], limit: int) -> list[str]:
    if not fts_results and not lexical_results:
        return []
    fused: dict[str, dict] = {}

    def ingest(items: list[dict], source: str) -> None:
        max_score = max((max(0.0, float(i.get("score", 0.0))) for i in items), default=1.0)
        for rank, item in enumerate(items, 1):
            content = str(item.get("content", "") or "").strip()
            if not content:
                continue
            entry = fused.setdefault(content, {"score": 0.0, "sources": set()})
            entry["sources"].add(source)
            rrf = 1.0 / (HYBRID_FUSION_K + rank)
            norm = max(0.0, float(item.get("score", 0.0))) / max_score if max_score > 0 else 0.0
            weight = 0.65 if source == "fts" else 0.35
            entry["score"] += rrf + (norm * weight)

    ingest(fts_results, "fts")
    ingest(lexical_results, "lexical")

    ranked = sorted(fused.items(), key=lambda pair: pair[1]["score"], reverse=True)
    return [content for content, _ in ranked[:limit]]


async def fts_search(
    db: aiosqlite.Connection,
    conversation_id: str,
    query: str,
    current_user_id: str,
    limit: int = FTS_RESULT_LIMIT,
) -> list[str]:
    """Hybrid memory retrieval: FTS + lexical search in parallel, then fused ranking."""
    fts_task = _fts_search_only(db, conversation_id, query, current_user_id, limit * HYBRID_CANDIDATE_MULTIPLIER)
    lexical_task = _lexical_memory_search(
        conversation_id,
        query,
        current_user_id,
        limit * HYBRID_CANDIDATE_MULTIPLIER,
    )
    fts_results, lexical_results = await asyncio.gather(fts_task, lexical_task)
    return _merge_memory_results(fts_results, lexical_results, limit)


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
    tooling = get_global_tool_toggles()
    routing = get_model_routing_config()
    return {
        **tooling,
        **routing,
        "default_model": get_default_local_model(),
    }


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

    default_model = save_default_local_model(body.default_model)
    
    # Save routing config for dual-endpoint setup
    routing_payload = {
        "agentic_endpoint_url": body.agentic_endpoint_url,
        "agentic_model": body.agentic_model,
        "agentic_policy": body.agentic_policy,
    }
    save_model_routing_config(routing_payload)
    
    return {
        "ok": True,
        **payload,
        "default_model": default_model,
        **routing_payload,
    }


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
    openai_key = get_openai_api_key()
    openai_masked = (
        (openai_key[:4] + "..." + openai_key[-4:])
        if len(openai_key) > 8
        else ("*" * len(openai_key) if openai_key else "")
    )
    llm_provider = get_llm_provider_config()
    gml_index = await ensure_gml_index_loaded()
    ps_index = await ensure_ps_index_loaded()

    gml_embeddings_enabled = CHROMADB_AVAILABLE and getattr(app.state, "gml_embeddings_ready", False)
    gml_embeddings_building = CHROMADB_AVAILABLE and getattr(app.state, "gml_embeddings_building", False)
    ps_embeddings_enabled = CHROMADB_AVAILABLE and getattr(app.state, "ps_embeddings_ready", False)
    ps_embeddings_building = CHROMADB_AVAILABLE and getattr(app.state, "ps_embeddings_building", False)
    codebase_index = getattr(app.state, "codebase_index", None) or {}
    codebase_embeddings_enabled = CHROMADB_AVAILABLE and getattr(app.state, "codebase_embeddings_ready", False)
    codebase_embeddings_building = CHROMADB_AVAILABLE and getattr(app.state, "codebase_embeddings_building", False)
    
    # Check dual-endpoint routing health
    chat_endpoint_online = await is_ollama_running(OLLAMA_HEALTH_URL)
    agentic_endpoint_online = await is_ollama_endpoint_running(OLLAMA_AGENTIC_HEALTH_URL)
    routing_config = get_model_routing_config()

    return {
        "brave_api_key_set": bool(key),
        "brave_api_key_masked": masked,
        "openai_api_key_set": bool(openai_key),
        "openai_api_key_masked": openai_masked,
        "openai_api_key_source": "env",
        "default_local_model": get_default_local_model(),
        "llm_provider": llm_provider,
        "openai_model_options": OPENAI_MODEL_OPTIONS,
        "openai_base_url": OPENAI_BASE_URL,
        "global_tool_toggles": get_global_tool_toggles(),
        "model_routing": routing_config,
        "chat_endpoint_url": OLLAMA_BASE_URL,
        "chat_endpoint_online": chat_endpoint_online,
        "agentic_endpoint_url": routing_config.get("agentic_endpoint_url", OLLAMA_AGENTIC_BASE_URL),
        "agentic_endpoint_online": agentic_endpoint_online,
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
        "codebase_index_enabled": bool(codebase_index.get("enabled")),
        "codebase_index_root": codebase_index.get("root", ""),
        "codebase_index_file_count": codebase_index.get("file_count", 0),
        "codebase_index_chunk_count": codebase_index.get("chunk_count", 0),
        "codebase_indexed_at": codebase_index.get("indexed_at", ""),
        "codebase_index_error": codebase_index.get("error", ""),
        "codebase_embeddings_enabled": codebase_embeddings_enabled,
        "codebase_embeddings_building": codebase_embeddings_building,
        "codebase_embeddings_model": "all-MiniLM-L6-v2" if codebase_embeddings_enabled else None,
        "treesitter_enabled": TREESITTER_AVAILABLE,
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

    if body.brave_api_key is not None:
        cfg["brave_api_key"] = body.brave_api_key.strip()

    # Security: OpenAI API key is env-only and must not be persisted to config.json.
    cfg.pop("openai_api_key", None)

    current_llm_provider = get_llm_provider_config()
    next_provider = body.llm_provider if body.llm_provider is not None else current_llm_provider["provider"]
    next_openai_model = body.openai_model if body.openai_model is not None else current_llm_provider["openai_model"]

    next_provider = str(next_provider or "local").strip().lower()
    if next_provider not in {"local", "openai"}:
        next_provider = "local"

    next_openai_model = str(next_openai_model or DEFAULT_OPENAI_MODEL).strip()
    if not next_openai_model:
        next_openai_model = DEFAULT_OPENAI_MODEL

    cfg["llm_provider"] = {
        "provider": next_provider,
        "openai_model": next_openai_model,
    }

    save_config(cfg)
    return {
        "ok": True,
        "llm_provider": cfg["llm_provider"],
    }


@app.post("/api/retrieval/docs/query")
async def hybrid_docs_query(body: HybridDocsQueryRequest, _: dict = Depends(get_current_user)):
    query = (body.query or "").strip()
    if not query:
        raise HTTPException(status_code=400, detail="query is required")

    source = (body.source or "both").strip().lower()
    if source not in {"gml", "ps", "both"}:
        raise HTTPException(status_code=400, detail="source must be one of: gml, ps, both")
    limit = max(1, min(int(body.limit or CODEBASE_RESULT_LIMIT), 20))

    gml_results: list[dict] = []
    ps_results: list[dict] = []
    if source in {"gml", "both"}:
        gml_results = rag_search_gml_docs(query, limit=limit)
    if source in {"ps", "both"}:
        ps_results = rag_search_ps_docs(query, limit=limit)

    combined = gml_results + ps_results
    return {
        "query": query,
        "source": source,
        "limit": limit,
        "gml_result_count": len(gml_results),
        "ps_result_count": len(ps_results),
        "result_count": len(combined),
        "results": combined,
    }


@app.get("/api/retrieval/diagnostics")
async def retrieval_diagnostics(current_user: dict = Depends(get_current_user)):
    gml_index = await ensure_gml_index_loaded()
    ps_index = await ensure_ps_index_loaded()
    codebase_index = getattr(app.state, "codebase_index", None) or {}
    effective_workspace_root = resolve_effective_workspace_root(
        current_user.get("workspace_root", ""),
        "",
    )
    return {
        "chromadb_available": CHROMADB_AVAILABLE,
        "treesitter_available": TREESITTER_AVAILABLE,
        "hybrid_candidate_multiplier": HYBRID_CANDIDATE_MULTIPLIER,
        "hybrid_fusion_k": HYBRID_FUSION_K,
        "gml": {
            "enabled": bool(gml_index.get("enabled")),
            "file_count": gml_index.get("file_count", 0),
            "chunk_count": gml_index.get("chunk_count", 0),
            "embeddings_ready": bool(getattr(app.state, "gml_embeddings_ready", False)),
            "embeddings_building": bool(getattr(app.state, "gml_embeddings_building", False)),
            "error": gml_index.get("error", ""),
        },
        "ps": {
            "enabled": bool(ps_index.get("enabled")),
            "file_count": ps_index.get("file_count", 0),
            "chunk_count": ps_index.get("chunk_count", 0),
            "embeddings_ready": bool(getattr(app.state, "ps_embeddings_ready", False)),
            "embeddings_building": bool(getattr(app.state, "ps_embeddings_building", False)),
            "error": ps_index.get("error", ""),
        },
        "codebase": {
            "configured_workspace_root": current_user.get("workspace_root", ""),
            "effective_workspace_root": effective_workspace_root,
            "enabled": bool(codebase_index.get("enabled")),
            "root": codebase_index.get("root", ""),
            "file_count": codebase_index.get("file_count", 0),
            "chunk_count": codebase_index.get("chunk_count", 0),
            "embeddings_ready": bool(getattr(app.state, "codebase_embeddings_ready", False)),
            "embeddings_building": bool(getattr(app.state, "codebase_embeddings_building", False)),
            "error": codebase_index.get("error", ""),
        },
    }


@app.post("/api/codebase/index/rebuild")
async def rebuild_codebase_index(body: CodebaseIndexRebuildRequest, current_user: dict = Depends(get_current_user)):
    base_root = current_user.get("workspace_root", "")
    effective_root = resolve_effective_workspace_root(base_root, body.working_subdir)
    if not effective_root:
        effective_root = str(Path(__file__).parent.resolve())

    codebase_index = await ensure_codebase_index_loaded(effective_root, force=bool(body.force))
    app.state.codebase_embeddings_building = True
    try:
        emb_result = await build_codebase_embeddings_collection(codebase_index)
        app.state.codebase_embeddings_ready = bool(emb_result.get("enabled"))
    finally:
        app.state.codebase_embeddings_building = False

    return {
        "ok": True,
        "root": codebase_index.get("root", ""),
        "file_count": codebase_index.get("file_count", 0),
        "chunk_count": codebase_index.get("chunk_count", 0),
        "treesitter_enabled": TREESITTER_AVAILABLE,
        "embeddings_enabled": bool(getattr(app.state, "codebase_embeddings_ready", False)),
        "error": codebase_index.get("error", ""),
    }


@app.post("/api/codebase/query")
async def query_codebase_index(body: CodebaseQueryRequest, current_user: dict = Depends(get_current_user)):
    query = (body.query or "").strip()
    if not query:
        raise HTTPException(status_code=400, detail="query is required")
    limit = max(1, min(int(body.limit or CODEBASE_RESULT_LIMIT), 20))

    base_root = current_user.get("workspace_root", "")
    effective_root = resolve_effective_workspace_root(base_root, body.working_subdir)
    if not effective_root:
        effective_root = str(Path(__file__).parent.resolve())

    results = await rag_search_codebase_docs(query, workspace_root=effective_root, limit=limit)
    return {
        "query": query,
        "limit": limit,
        "workspace_root": effective_root,
        "result_count": len(results),
        "results": results,
    }


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


@app.get("/api/file-tools/read")
async def file_tools_read(
    path: str = Query(...),
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
        target = resolve_sandboxed_path(effective_root, path)
        if not target.is_file():
            raise HTTPException(status_code=400, detail=f"Not a file or does not exist: {path}")

        content = ft_read_file(effective_root, path)
        stat = target.stat()
        return {
            "path": path,
            "working_subdir": working_subdir,
            "content": content,
            "byte_length": len(content.encode("utf-8")),
            "modified_at": datetime.fromtimestamp(stat.st_mtime, tz=timezone.utc).isoformat(),
        }
    except FileToolError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc
    except PermissionError as exc:
        raise HTTPException(status_code=403, detail=str(exc)) from exc


@app.post("/api/file-tools/write")
async def file_tools_write(body: FileToolsWriteRequest, current_user: dict = Depends(get_current_user)):
    if not bool(current_user.get("file_tools_enabled")):
        raise HTTPException(status_code=403, detail="File tools are disabled for this account")

    base_root = (current_user.get("workspace_root") or "").strip()
    if not base_root:
        raise HTTPException(status_code=400, detail="Workspace root is not configured by admin")

    try:
        effective_root = resolve_effective_workspace_root(base_root, body.working_subdir)
        result = ft_write_file(effective_root, body.path, body.content)
        target = resolve_sandboxed_path(effective_root, body.path)
        stat = target.stat()
        return {
            "ok": True,
            "path": body.path,
            "working_subdir": body.working_subdir,
            "message": result,
            "byte_length": len(body.content.encode("utf-8")),
            "modified_at": datetime.fromtimestamp(stat.st_mtime, tz=timezone.utc).isoformat(),
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

    provider_config = get_llm_provider_config()
    requested_provider = str(req.model_provider or provider_config.get("provider", "local")).strip().lower()
    if requested_provider not in {"local", "openai"}:
        requested_provider = "local"

    default_local_model = get_default_local_model()

    if requested_provider == "openai":
        fallback_openai_model = provider_config.get("openai_model", DEFAULT_OPENAI_MODEL)
        requested_model = str(req.model or fallback_openai_model).strip() or DEFAULT_OPENAI_MODEL
    else:
        requested_model = normalize_model_name(req.model or default_local_model)

    openai_api_key = get_openai_api_key()

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
            "chat[%s] start user=%s conv=%s surface=%s provider=%s model=%s toggles={search:%s,gml:%s,ps:%s,file:%s,code:%s,ps_exec:%s,mcp:%s} workspace=%s file=%s",
            stream_id,
            current_user.get("id"),
            req.conversation_id,
            req.surface,
            requested_provider,
            requested_model,
            req.use_search,
            use_gml_docs,
            use_ps_docs,
            use_file_tools,
            use_code_interpreter,
            use_powershell,
            use_mcp_tools,
            effective_workspace_root,
            (req.current_file_path or "").strip() or "-",
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
        codebase_snippet_count = 0
        seen_tool_call_ids: set[str] = set()
        fts_snippets: list[str] = []
        codebase_snippets: list[dict] = []
        tool_result_summaries: list[str] = []
        background_draft_excerpt = ""
        ollama_messages: list[dict] = []
        working_msgs: list[dict] = []
        db: aiosqlite.Connection | None = None
        strict_literal_recovery_attempted = False

        def _sse(payload: dict) -> str:
            return f"data: {json.dumps(payload)}\n\n"

        def _status_payload(key: str, status: str, message: str, **extra) -> dict:
            payload = {"type": "status", "key": key, "status": status, "message": message}
            payload.update(extra)
            return payload

        if requested_provider == "openai":
            yield _sse(_status_payload("endpoint_check", "running", f"Using OpenAI endpoint {OPENAI_BASE_URL}"))
            if not openai_api_key:
                detail = "OpenAI mode requires OPENAI_API_KEY in your .env (loaded at startup)."
                yield _sse(_status_payload("endpoint_check", "error", detail))
                yield _sse({"type": "error", "error_type": "auth_error", "message": detail})
                return
            yield _sse(_status_payload("endpoint_check", "done", "OpenAI key detected"))
        else:
            yield _sse(_status_payload("endpoint_check", "running", f"Checking chat endpoint {OLLAMA_BASE_URL}"))
            if not await ensure_ollama_running(wait_seconds=6):
                detail = (
                    f"Ollama is not available at {OLLAMA_BASE_URL}."
                    if not OLLAMA_IS_LOCAL
                    else f"Ollama is not available at {OLLAMA_BASE_URL} and auto-start failed. Start it with ollama serve."
                )
                yield _sse(_status_payload("endpoint_check", "error", detail))
                yield _sse({"type": "error", "error_type": "connection_error", "message": detail})
                return
            yield _sse(_status_payload("endpoint_check", "done", "Chat endpoint is online"))

        yield _sse(_status_payload("request_setup", "running", "Preparing request context"))

        db = await get_db()
        cursor = await db.execute(
            "SELECT id FROM conversations WHERE id=? AND user_id=?",
            (req.conversation_id, current_user["id"]),
        )
        if not await cursor.fetchone():
            yield _sse({"type": "error", "error_type": "conversation_error", "message": "Conversation not found"})
            return
        yield _sse(_status_payload("request_setup", "done", "Conversation loaded"))

        yield _sse(_status_payload("conversation_context", "running", "Loading conversation context"))
        history, was_truncated = await build_active_context(db, req.conversation_id, req.message)
        yield _sse(_status_payload("conversation_context", "done", f"Loaded {len(history)} context message(s)"))

        if was_truncated:
            yield _sse(_status_payload("memory_search", "running", "Searching long-term memory"))
            fts_snippets = await fts_search(db, req.conversation_id, req.message, current_user["id"])
            if fts_snippets:
                log.info("Injecting %d FTS snippet(s) for conv %s", len(fts_snippets), req.conversation_id)
            yield _sse(_status_payload("memory_search", "done", f"Long-term memory ready: {len(fts_snippets)} snippet(s)"))

        if effective_workspace_root and (use_file_tools or use_mcp_tools):
            yield _sse(_status_payload("codebase_retrieval", "running", f"Inspecting workspace {effective_workspace_root}"))
            codebase_task = asyncio.create_task(
                rag_search_codebase_docs(
                    req.message,
                    workspace_root=effective_workspace_root,
                    limit=4,
                )
            )
            codebase_heartbeat_count = 0
            while True:
                try:
                    codebase_snippets = await asyncio.wait_for(
                        asyncio.shield(codebase_task),
                        timeout=SSE_HEARTBEAT_SECONDS,
                    )
                    break
                except asyncio.TimeoutError:
                    codebase_heartbeat_count += 1
                    yield _sse({
                        "type": "heartbeat",
                        "phase": "codebase_retrieval",
                        "count": codebase_heartbeat_count,
                        "message": f"Still indexing and searching workspace ({int(codebase_heartbeat_count * SSE_HEARTBEAT_SECONDS)}s)",
                    })
            codebase_snippet_count = len(codebase_snippets)
            if codebase_snippets:
                log.info(
                    "Injecting %d codebase snippet(s) from %s",
                    len(codebase_snippets),
                    effective_workspace_root,
                )
            yield _sse(_status_payload("codebase_retrieval", "done", f"Workspace context ready: {codebase_snippet_count} snippet(s)"))

        yield _sse(_status_payload("prompt_build", "running", "Assembling prompt and tool policy"))
        system_prompt_parts: list[str] = []
        system_prompt_parts.append(ENGLISH_ONLY_SYSTEM_PROMPT)

        admin_persona_prompt = (current_user.get("persona_prompt") or "").strip()
        if current_user.get("role") == "admin" and admin_persona_prompt:
            system_prompt_parts.append(admin_persona_prompt)

        if use_gml_docs:
            system_prompt_parts.append(GML_SYSTEM_PROMPT)

        if use_ps_docs:
            system_prompt_parts.append(PS_SYSTEM_PROMPT)

        if use_file_tools:
            if use_mcp_tools:
                system_prompt_parts.append(MCP_FILE_TOOLS_SYSTEM_PROMPT)
            else:
                system_prompt_parts.append(FILE_TOOLS_SYSTEM_PROMPT)

        if use_file_tools or use_mcp_tools:
            system_prompt_parts.append(CODEBASE_INDEX_SYSTEM_PROMPT)
            if effective_workspace_root:
                working_subdir = (req.working_subdir or "").strip() or "."
                system_prompt_parts.append(
                    "Current working directory for this request: "
                    f"{effective_workspace_root} (subdir: {working_subdir}). "
                    "Treat this as the default root for relative paths and folder exploration."
                )

        editor_context_prompt = build_editor_context_prompt(req)
        if editor_context_prompt:
            system_prompt_parts.append(editor_context_prompt)

        if use_any_tooling:
            system_prompt_parts.append(TOOL_EXECUTION_CONTRACT_PROMPT)

        if fts_snippets:
            snippets_text = "\n\n---\n\n".join(fts_snippets)
            system_prompt_parts.append(
                "The following are relevant excerpts from your long-term memory "
                "(earlier conversations outside the active context window). "
                "Use them if relevant:\n\n" + snippets_text
            )

        if codebase_snippets:
            system_prompt_parts.append(format_codebase_snippets(codebase_snippets))

        if system_prompt_parts:
            ollama_messages.append({
                "role": "system",
                "content": "\n\n".join(part for part in system_prompt_parts if part),
            })

        ollama_messages.extend(history)
        ollama_messages.append({"role": "user", "content": req.message})
        working_msgs = list(ollama_messages)
        yield _sse(_status_payload("prompt_build", "done", "Prompt ready, starting model execution"))

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

        def _build_agent_function_list(include_mcp_tools: bool = True, stage: str = "main") -> list:
            """Build Qwen-Agent function_list based on enabled features.

            Strategy: when MCP is active, filesystem operations go through
            the MCP filesystem server.  Only local RAG doc-search tools
            (gml_docs_search, ps_docs_search), web_search and
            code_interpreter remain as native/local tools because they have
            no MCP equivalent.  When MCP is *off*, native file tools are
            used instead.
            """
            tools: list = []
            stage_mode = (stage or "main").strip().lower()
            is_background_stage = stage_mode == "background"
            # Web search — always local (Brave API, no MCP equivalent)
            if req.use_search and not is_background_stage:
                tools.append("web_search")
            # Filesystem tools — native only when MCP is disabled
            if use_file_tools and not use_mcp_tools:
                if is_background_stage:
                    # Keep helper stage read-only to avoid duplicated side effects
                    # when running multiple background workers in parallel.
                    tools.extend([
                        "read_file",
                        "list_dir",
                        "search_files",
                        "grep_search",
                    ])
                else:
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
            # Codebase index tools — local hybrid retrieval over workspace files
            if use_file_tools or use_mcp_tools:
                tools.append("codebase_folder_overview")
                tools.append("codebase_index_search")
            # Code interpreter — always local (Docker sandbox, no MCP equivalent)
            if (not is_background_stage) and use_code_interpreter and code_interpreter.is_available():
                tools.append("code_interpreter")
            # PowerShell — always local (native or Docker, no MCP equivalent)
            if (not is_background_stage) and use_powershell and is_ps_available(ps_mode):
                tools.append("run_powershell")
            # MCP servers — filesystem, memory, sqlite all handled here
            if include_mcp_tools and use_mcp_tools and not is_background_stage:
                try:
                    user_mcp_config = _load_user_mcp_config(
                        current_user.get("mcp_config", ""),
                        effective_workspace_root,
                    )
                    resolved_mcp_config = _resolve_and_validate_user_mcp_config(
                        user_mcp_config,
                        effective_workspace_root,
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

        async def _iter_with_heartbeat(response_iter, *, phase_key: str, phase_label: str):
            heartbeat_count = 0
            while True:
                next_task = asyncio.create_task(asyncio.to_thread(_next_from_iter, response_iter))
                while True:
                    try:
                        has_item, rsp = await asyncio.wait_for(
                            asyncio.shield(next_task),
                            timeout=SSE_HEARTBEAT_SECONDS,
                        )
                        break
                    except asyncio.TimeoutError:
                        heartbeat_count += 1
                        elapsed_seconds = int(heartbeat_count * SSE_HEARTBEAT_SECONDS)
                        yield {
                            "type": "heartbeat",
                            "phase": phase_key,
                            "count": heartbeat_count,
                            "message": f"{phase_label} ({elapsed_seconds}s)",
                        }
                if not has_item:
                    break
                yield {"type": "response", "rsp": rsp}

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

        def _execute_literal_tool_call(tool_name: str, args: dict) -> tuple[bool, str]:
            """Execute parsed literal tool markup as a fail-open compatibility path.

            Returns (handled, content). handled=False means the tool name was not mapped.
            """
            normalized_tool = str(tool_name or "").strip().lower()
            workspace_root_for_fallback = (
                effective_workspace_root
                or str(current_user.get("workspace_root") or "").strip()
                or str(Path(__file__).parent.resolve())
            )

            def _arg(*keys: str, default: str = "") -> str:
                for key in keys:
                    val = args.get(key)
                    if val is not None and str(val).strip():
                        return str(val).strip()
                return default

            def _safe_int(value, default: int) -> int:
                try:
                    return int(value)
                except Exception:
                    return default

            def _directory_tree_snapshot(path_value: str, max_depth: int = 2, max_entries: int = 250) -> str:
                target = (
                    Path(workspace_root_for_fallback).resolve()
                    if path_value in {"", "."}
                    else resolve_sandboxed_path(workspace_root_for_fallback, path_value)
                )
                if not target.is_dir():
                    raise FileToolError(f"Not a directory or does not exist: {target}")

                lines: list[str] = []
                root_depth = len(target.parts)
                stack: list[Path] = [target]
                while stack and len(lines) < max_entries:
                    current = stack.pop()
                    try:
                        rel = current.relative_to(target)
                        rel_str = "." if str(rel) == "." else rel.as_posix()
                    except ValueError:
                        rel_str = current.name
                    depth = max(0, len(current.parts) - root_depth)
                    indent = "  " * depth
                    marker = "/" if current.is_dir() else ""
                    lines.append(f"{indent}{rel_str}{marker}")
                    if current.is_dir() and depth < max_depth:
                        children = sorted(
                            list(current.iterdir()),
                            key=lambda p: (not p.is_dir(), p.name.lower()),
                        )
                        for child in reversed(children[:50]):
                            stack.append(child)

                if len(lines) >= max_entries:
                    lines.append("[tree truncated]")
                return "\n".join(lines)

            if tool_name == "code_interpreter":
                code = str(args.get("code") or "").strip()
                if not code:
                    return True, "[Error: code_interpreter requires a non-empty 'code' parameter]"
                if not (use_code_interpreter and code_interpreter.is_available()):
                    return True, "[Error: code_interpreter is disabled or unavailable]"
                return True, code_interpreter.call(code)

            if tool_name == "run_powershell":
                code = str(args.get("code") or "").strip()
                if not code:
                    return True, "[Error: run_powershell requires a non-empty 'code' parameter]"
                if not use_powershell:
                    return True, "[Error: run_powershell is disabled for this request]"
                if not is_ps_available(ps_mode):
                    return True, f"[Error: run_powershell mode '{ps_mode}' is unavailable]"
                try:
                    timeout = int(args.get("timeout") or 30)
                except Exception:
                    timeout = 30
                session_key = f"{current_user['id']}:{req.conversation_id}"
                session = get_or_create_ps_session(session_key, ps_mode)
                output, timed_out = session.execute(code, timeout=timeout)
                if timed_out:
                    return True, f"[Timeout after {timeout}s]" + (f"\n{output}" if output else "")
                return True, output or "(no output)"

            if normalized_tool in {"filesystem-list_allowed_directories", "filesystem-list-allowed-directories"}:
                allowed = [workspace_root_for_fallback]
                base_root = str(current_user.get("workspace_root") or "").strip()
                if base_root and base_root not in allowed:
                    allowed.append(base_root)
                return True, "\n".join(f"[DIR] {p}" for p in allowed)

            if normalized_tool in {"filesystem-list_directory", "filesystem-list-directory", "list_dir"}:
                path_arg = _arg("path", "directory", "dir", "target", default=".")
                return True, ft_list_dir(workspace_root_for_fallback, path_arg)

            if normalized_tool in {"filesystem-directory_tree", "filesystem-directory-tree"}:
                path_arg = _arg("path", "directory", "dir", "target", default=".")
                return True, _directory_tree_snapshot(path_arg)

            if normalized_tool in {"filesystem-read_file", "filesystem-read-file", "read_file"}:
                path_arg = _arg("path", "file_path", "target", default="")
                if not path_arg:
                    return True, "[Error: read_file requires a 'path' parameter]"
                start_line = _safe_int(args.get("start_line", 1), 1)
                end_raw = args.get("end_line")
                end_line = _safe_int(end_raw, 0) if end_raw not in (None, "") else None
                if end_line is not None and end_line <= 0:
                    end_line = None
                return True, ft_read_file(workspace_root_for_fallback, path_arg, start_line=start_line, end_line=end_line)

            if normalized_tool in {"filesystem-search_files", "filesystem-search-files", "search_files"}:
                pattern = _arg("pattern", "glob", "query", default="*")
                directory = _arg("directory", "path", "dir", default=".")
                return True, ft_search_files(workspace_root_for_fallback, pattern=pattern, directory=directory)

            if normalized_tool in {"filesystem-get_file_info", "filesystem-get-file-info"}:
                path_arg = _arg("path", "file_path", "target", default=".")
                target = (
                    Path(workspace_root_for_fallback).resolve()
                    if path_arg in {"", "."}
                    else resolve_sandboxed_path(workspace_root_for_fallback, path_arg)
                )
                if not target.exists():
                    return True, f"[Error: Path does not exist: {path_arg}]"
                stat = target.stat()
                return True, "\n".join([
                    f"path: {target}",
                    f"size: {stat.st_size}",
                    f"isDirectory: {target.is_dir()}",
                    f"isFile: {target.is_file()}",
                    f"modified: {datetime.fromtimestamp(stat.st_mtime, tz=timezone.utc).isoformat()}",
                ])

            return False, f"[Error: Unsupported literal fallback tool: {tool_name}]"

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

        def _compact_tool_summary(tool_name: str, tool_content: str, tool_ok: bool) -> str:
            """Produce concise, user-facing tool status text to avoid dumping raw payloads."""
            name = str(tool_name or "")
            content = str(tool_content or "")
            lowered_name = name.lower()

            # MCP filesystem tools often return very large JSON payloads.
            if lowered_name in {
                "filesystem-list_directory",
                "filesystem-directory_tree",
                "filesystem-read_file",
                "filesystem-search_files",
                "list_dir",
                "read_file",
                "search_files",
                "grep_search",
            }:
                if not tool_ok:
                    return f"{name} failed"
                if lowered_name.endswith("list_directory") or lowered_name == "list_dir":
                    return "Directory listing retrieved"
                if lowered_name.endswith("directory_tree"):
                    return "Directory tree retrieved"
                if lowered_name.endswith("read_file") or lowered_name == "read_file":
                    return "File content retrieved"
                if lowered_name.endswith("search_files") or lowered_name == "search_files":
                    return "File search results retrieved"
                if lowered_name == "grep_search":
                    return "Text search results retrieved"

            compact = re.sub(r"\s+", " ", content).strip()
            if not compact:
                return "ok" if tool_ok else "error"
            if len(compact) > 180:
                return compact[:180] + "..."
            return compact

        def _normalize_tool_parameters(parameters) -> dict:
            if isinstance(parameters, dict):
                schema = dict(parameters)
            elif isinstance(parameters, list):
                props: dict[str, dict] = {}
                required: list[str] = []
                for item in parameters:
                    if not isinstance(item, dict):
                        continue
                    param_name = str(item.get("name") or "").strip()
                    if not param_name:
                        continue
                    raw_type = str(item.get("type") or "string").strip().lower()
                    if raw_type in {"str"}:
                        raw_type = "string"
                    elif raw_type in {"int"}:
                        raw_type = "integer"
                    elif raw_type in {"float"}:
                        raw_type = "number"
                    elif raw_type in {"bool"}:
                        raw_type = "boolean"
                    elif raw_type in {"list"}:
                        raw_type = "array"
                    elif raw_type in {"dict"}:
                        raw_type = "object"
                    if raw_type not in {"string", "integer", "number", "boolean", "array", "object"}:
                        raw_type = "string"

                    prop: dict[str, object] = {
                        "type": raw_type,
                        "description": str(item.get("description") or ""),
                    }
                    enum_values = item.get("enum")
                    if isinstance(enum_values, list) and enum_values:
                        prop["enum"] = enum_values
                    props[param_name] = prop
                    if bool(item.get("required")):
                        required.append(param_name)

                schema = {
                    "type": "object",
                    "properties": props,
                    "required": required,
                }
            else:
                schema = {"type": "object", "properties": {}, "required": []}

            if schema.get("type") != "object":
                schema = {
                    "type": "object",
                    "properties": schema.get("properties", {}) if isinstance(schema.get("properties"), dict) else {},
                    "required": schema.get("required", []) if isinstance(schema.get("required"), list) else [],
                }
            if not isinstance(schema.get("properties"), dict):
                schema["properties"] = {}
            if not isinstance(schema.get("required"), list):
                schema["required"] = []
            return schema

        def _extract_openai_message_text(content_obj) -> str:
            if isinstance(content_obj, str):
                return content_obj
            if isinstance(content_obj, list):
                chunks: list[str] = []
                for part in content_obj:
                    if isinstance(part, str):
                        if part:
                            chunks.append(part)
                        continue
                    if not isinstance(part, dict):
                        continue
                    part_type = str(part.get("type") or "").strip().lower()
                    if part_type in {"text", "output_text"}:
                        text_value = part.get("text")
                        if isinstance(text_value, str) and text_value:
                            chunks.append(text_value)
                        elif isinstance(text_value, dict):
                            nested = text_value.get("value")
                            if isinstance(nested, str) and nested:
                                chunks.append(nested)
                return "".join(chunks)
            if content_obj is None:
                return ""
            return str(content_obj)

        async def _call_openai_chat_completion(messages_payload: list[dict], tool_schemas: list[dict] | None) -> dict:
            payload: dict[str, object] = {
                "model": requested_model,
                "messages": messages_payload,
            }
            if tool_schemas:
                payload["tools"] = tool_schemas
                payload["tool_choice"] = "auto"

            headers = {
                "Authorization": f"Bearer {openai_api_key}",
                "Content-Type": "application/json",
            }
            timeout = aiohttp.ClientTimeout(total=180)
            url = f"{OPENAI_BASE_URL}/chat/completions"
            async with aiohttp.ClientSession(timeout=timeout) as session:
                async with session.post(url, headers=headers, json=payload) as response:
                    raw_text = await response.text()
                    if response.status >= 400:
                        raise RuntimeError(
                            f"OpenAI chat/completions error {response.status}: {raw_text[:600]}"
                        )
                    try:
                        return json.loads(raw_text)
                    except Exception as exc:
                        raise RuntimeError(f"Invalid OpenAI JSON response: {exc}") from exc

        async def _execute_named_tool_call(
            tool_name: str,
            args_obj: dict,
            qwen_tool_registry: dict,
            mcp_tool_names: set[str],
        ) -> str:
            name = str(tool_name or "").strip()
            if not name:
                return "[Error: tool name is empty]"

            if name in mcp_tool_names:
                try:
                    from agent_tools import mcp_registry  # noqa: PLC0415

                    return await asyncio.to_thread(mcp_registry.call_tool, name, args_obj)
                except Exception as exc:
                    return f"[Error: MCP tool '{name}' failed: {exc}]"

            tool_entry = qwen_tool_registry.get(name)
            if tool_entry is not None:
                try:
                    tool_instance = tool_entry() if isinstance(tool_entry, type) else tool_entry
                    params_payload = json.dumps(args_obj, ensure_ascii=False)
                    return await asyncio.to_thread(tool_instance.call, params_payload)
                except Exception as exc:
                    return f"[Error: tool '{name}' failed: {exc}]"

            handled, fallback_content = await asyncio.to_thread(_execute_literal_tool_call, name, args_obj)
            if handled:
                return fallback_content
            return f"[Error: Unsupported tool '{name}']"

        def _make_agent(include_mcp_tools: bool, stage: str = "main"):
            function_list = _build_agent_function_list(include_mcp_tools=include_mcp_tools, stage=stage)
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

            def _build_generate_cfg(*, raw_api_mode: bool) -> dict:
                cfg: dict = {"use_raw_api": raw_api_mode}
                # fncall_prompt_type is for qwen-agent prompt-injection mode only.
                # In native raw-api mode, providing this can increase protocol drift
                # (model emitting literal <function=...> text instead of tool_calls).
                if (not raw_api_mode) and fncall_prompt_type:
                    cfg["fncall_prompt_type"] = fncall_prompt_type

                # OpenAI mode must avoid backend-specific payload fields such as
                # Ollama's `options`/`think` in `extra_body`.
                if requested_provider != "openai":
                    extra_body = {"options": {"num_ctx": OLLAMA_NUM_CTX}}
                    if req.think is not None:
                        extra_body["think"] = bool(req.think)
                    cfg["extra_body"] = extra_body
                return cfg

            generate_cfg = _build_generate_cfg(raw_api_mode=use_raw_api)
            log.info(
                "chat[%s] llm generate_cfg use_raw_api=%s fncall_prompt_type=%r provider=%s think=%s num_ctx=%s extra_body=%s",
                stream_id,
                use_raw_api,
                fncall_prompt_type,
                requested_provider,
                req.think,
                OLLAMA_NUM_CTX,
                "yes" if "extra_body" in generate_cfg else "no",
            )

            llm_cfg = {
                "model": requested_model,
                "model_server": OPENAI_BASE_URL if requested_provider == "openai" else OLLAMA_OPENAI_URL,
                "api_key": openai_api_key if requested_provider == "openai" else "EMPTY",
                "generate_cfg": generate_cfg,
            }

            include_mcp_for_run = True
            retried_prompt_injection_for_openai = False
            agent = None
            if requested_provider != "openai":
                try:
                    agent = _make_agent(include_mcp_tools=include_mcp_for_run, stage="main")
                except Exception as exc:
                    # Fail-open: if MCP startup fails (missing launcher, server boot failure, etc.),
                    # retry once without MCP so chat remains available.
                    if use_mcp_tools:
                        log.warning("chat[%s] assistant init with MCP failed; retrying without MCP tools: %s", stream_id, exc)
                        include_mcp_for_run = False
                        agent = _make_agent(include_mcp_tools=False, stage="main")
                    else:
                        raise

            retry_without_mcp_on_eof = bool(requested_provider != "openai" and use_mcp_tools and include_mcp_for_run)

            # Two-stage pipeline: background reasoning + tool execution on agentic endpoint (11435)
            # Strategy: detect heavy tooling, evaluate routing policy, conditionally run worker stage
            heavy_tooling_requested = any([
                use_file_tools,
                use_code_interpreter,
                use_powershell,
                use_mcp_tools,
            ])
            background_intent, background_intent_reason = should_dispatch_background_stage(
                message=req.message,
                use_search=req.use_search,
                use_gml_docs=use_gml_docs,
                use_ps_docs=use_ps_docs,
                use_file_tools=use_file_tools,
                use_code_interpreter=use_code_interpreter,
                use_powershell=use_powershell,
                use_mcp_tools=use_mcp_tools,
            )
            routing_config = get_model_routing_config()
            agentic_policy = routing_config.get("agentic_policy", "all_tooling")
            agentic_endpoint_base_url = routing_config.get("agentic_endpoint_url", OLLAMA_AGENTIC_BASE_URL).rstrip("/")
            agentic_endpoint_model = normalize_model_name(
                req.agentic_model or routing_config.get("agentic_model", DEFAULT_AGENTIC_MODEL)
            )
            helper_candidates = [agentic_endpoint_base_url]
            if requested_provider == "openai":
                # In OpenAI mode, keep both local GPUs available for helper work
                # and prefer 11434 first.
                helper_candidates = [OLLAMA_BASE_URL, agentic_endpoint_base_url]
            available_helper_endpoints = await select_available_helper_endpoints(helper_candidates, timeout_seconds=1.5)
            main_model_server = str(llm_cfg.get("model_server") or "")
            background_model_server = f"{available_helper_endpoints[0]}/v1" if available_helper_endpoints else f"{agentic_endpoint_base_url}/v1"
            background_server_label = ", ".join(available_helper_endpoints) if available_helper_endpoints else "offline"

            yield _sse(
                _status_payload(
                    "routing_summary",
                    "done",
                    (
                        f"Routing: main {requested_model} -> {main_model_server}; "
                        f"background {agentic_endpoint_model} -> {background_server_label} "
                        f"(policy={agentic_policy})"
                    ),
                )
            )
            log.info(
                "chat[%s] routing summary main_model=%s main_server=%s background_model=%s background_server=%s policy=%s intent=%s reason=%s",
                stream_id,
                requested_model,
                main_model_server,
                agentic_endpoint_model,
                background_server_label,
                agentic_policy,
                background_intent,
                background_intent_reason,
            )

            # Determine if background stage should run
            run_background_stage = (
                use_any_tooling
                and background_intent
                and (
                    agentic_policy == "all_tooling"
                    or (agentic_policy == "heavy_only" and heavy_tooling_requested)
                )
                and bool(available_helper_endpoints)
            )

            if run_background_stage:
                helper_targets = list(available_helper_endpoints)
                if requested_provider == "openai":
                    helper_targets = helper_targets[:2]
                else:
                    helper_targets = helper_targets[:1]

                yield f"data: {json.dumps({'type': 'status', 'key': 'background_stage', 'status': 'running', 'message': f'Background helper stage running on {len(helper_targets)} local endpoint(s): {', '.join(helper_targets)}'})}\n\n"
                log.info(
                    "chat[%s] triggering background stage: heavy_tooling=%s policy=%s endpoints=%s model=%s",
                    stream_id,
                    heavy_tooling_requested,
                    agentic_policy,
                    helper_targets,
                    agentic_endpoint_model,
                )
                try:
                    def _endpoint_port_label(endpoint_url: str) -> str:
                        parsed = urlparse(str(endpoint_url or "").strip())
                        port = parsed.port
                        if port is None:
                            port = 443 if parsed.scheme == "https" else 80
                        return str(port)

                    async def _run_background_worker(endpoint_url: str, worker_index: int) -> dict:
                        worker_llm_cfg = {
                            "model": agentic_endpoint_model,
                            "model_server": f"{endpoint_url}/v1",
                            "api_key": "EMPTY",
                            "generate_cfg": {
                                "use_raw_api": True,
                                "extra_body": {
                                    "think": True,
                                    "options": {"num_ctx": OLLAMA_NUM_CTX},
                                },
                            },
                        }
                        worker_agent = Assistant(
                            function_list=_build_agent_function_list(include_mcp_tools=False, stage="background"),
                            llm=get_chat_model(worker_llm_cfg),
                            system_message="",
                        )

                        worker_response_iter = worker_agent.run(messages=working_msgs, lang="en")
                        worker_reasoning = ""
                        worker_content = ""
                        worker_tool_msgs: list[dict] = []
                        seen_worker_tools = 0

                        try:
                            async for packet in _iter_with_heartbeat(
                                worker_response_iter,
                                phase_key=f"background_stage_{worker_index}",
                                phase_label=f"Background helper {worker_index} on {endpoint_url}",
                            ):
                                if packet.get("type") == "heartbeat":
                                    continue
                                rsp = packet.get("rsp")
                                if not isinstance(rsp, list):
                                    continue

                                for msg in rsp:
                                    if hasattr(msg, "get") and msg.get("role") == "assistant":
                                        reasoning = str(msg.get("reasoning_content") or msg.get("thinking") or "")
                                        content = str(msg.get("content") or "")
                                        if reasoning:
                                            worker_reasoning = reasoning
                                        if content:
                                            worker_content = content

                                tool_msgs = [
                                    m for m in rsp
                                    if hasattr(m, "get") and m.get("role") in ("function", "tool")
                                ]
                                if len(tool_msgs) > seen_worker_tools:
                                    for tool_msg in tool_msgs[seen_worker_tools:]:
                                        worker_tool_msgs.append(tool_msg)
                                        log.info(
                                            "chat[%s] background worker=%s endpoint=%s tool=%s",
                                            stream_id,
                                            worker_index,
                                            endpoint_url,
                                            tool_msg.get("name", "unknown"),
                                        )
                                    seen_worker_tools = len(tool_msgs)
                        except asyncio.CancelledError:
                            close_fn = getattr(worker_response_iter, "close", None)
                            if callable(close_fn):
                                try:
                                    await asyncio.to_thread(close_fn)
                                except Exception:
                                    pass
                            raise

                        return {
                            "worker_index": worker_index,
                            "endpoint": endpoint_url,
                            "reasoning": worker_reasoning,
                            "content": worker_content,
                            "tool_msgs": worker_tool_msgs,
                        }

                    worker_tasks: dict[asyncio.Task, tuple[int, str]] = {}
                    worker_summaries: list[dict] = []
                    for idx, endpoint in enumerate(helper_targets, start=1):
                        worker_key = f"background_worker_{idx}"
                        endpoint_port = _endpoint_port_label(endpoint)
                        yield _sse(_status_payload(
                            worker_key,
                            "running",
                            f"Background helper {idx} running on endpoint {endpoint_port} ({endpoint})",
                            worker_index=idx,
                            endpoint=endpoint,
                            endpoint_port=endpoint_port,
                        ))
                        task = asyncio.create_task(_run_background_worker(endpoint, idx))
                        worker_tasks[task] = (idx, endpoint)

                    worker_runs: list[dict | Exception] = []
                    pending = set(worker_tasks.keys())
                    heartbeat_count = 0
                    workers_timed_out = False
                    while pending:
                        done, pending = await asyncio.wait(
                            pending,
                            timeout=SSE_HEARTBEAT_SECONDS,
                            return_when=asyncio.FIRST_COMPLETED,
                        )

                        if not done:
                            heartbeat_count += 1
                            elapsed = int(heartbeat_count * SSE_HEARTBEAT_SECONDS)
                            # Hard-cancel all remaining workers if total timeout exceeded.
                            if elapsed >= BACKGROUND_WORKER_TIMEOUT_SECONDS:
                                workers_timed_out = True
                                log.warning(
                                    "chat[%s] background workers exceeded total timeout (%ds); cancelling %d remaining",
                                    stream_id,
                                    BACKGROUND_WORKER_TIMEOUT_SECONDS,
                                    len(pending),
                                )
                                for task in pending:
                                    idx, endpoint = worker_tasks[task]
                                    endpoint_port = _endpoint_port_label(endpoint)
                                    task.cancel()
                                    worker_summaries.append({
                                        "worker": idx,
                                        "endpoint": endpoint,
                                        "endpoint_port": endpoint_port,
                                        "status": "timeout",
                                        "tools": 0,
                                    })
                                    yield _sse(_status_payload(
                                        f"background_worker_{idx}",
                                        "error",
                                        f"Background helper {idx} cancelled after {BACKGROUND_WORKER_TIMEOUT_SECONDS}s timeout on endpoint {endpoint_port}",
                                        worker_index=idx,
                                        endpoint=endpoint,
                                        endpoint_port=endpoint_port,
                                    ))
                                await asyncio.gather(*pending, return_exceptions=True)
                                pending = set()
                                break
                            for task in pending:
                                idx, endpoint = worker_tasks[task]
                                endpoint_port = _endpoint_port_label(endpoint)
                                yield _sse({
                                    "type": "heartbeat",
                                    "phase": f"background_worker_{idx}",
                                    "count": heartbeat_count,
                                    "message": f"Background helper {idx} still running on endpoint {endpoint_port} ({elapsed}s)",
                                    "endpoint": endpoint,
                                    "endpoint_port": endpoint_port,
                                })
                            continue

                        for task in done:
                            idx, endpoint = worker_tasks[task]
                            worker_key = f"background_worker_{idx}"
                            endpoint_port = _endpoint_port_label(endpoint)
                            try:
                                result = task.result()
                                worker_runs.append(result)
                                tool_count = len(result.get("tool_msgs") or [])
                                worker_summaries.append({
                                    "worker": idx,
                                    "endpoint": endpoint,
                                    "endpoint_port": endpoint_port,
                                    "status": "ok",
                                    "tools": tool_count,
                                })
                                yield _sse(_status_payload(
                                    worker_key,
                                    "done",
                                    f"Background helper {idx} completed on endpoint {endpoint_port}",
                                    worker_index=idx,
                                    endpoint=endpoint,
                                    endpoint_port=endpoint_port,
                                    tool_count=tool_count,
                                ))
                            except Exception as exc:
                                worker_runs.append(exc)
                                worker_summaries.append({
                                    "worker": idx,
                                    "endpoint": endpoint,
                                    "endpoint_port": endpoint_port,
                                    "status": "error",
                                    "tools": 0,
                                    "error": str(exc)[:160],
                                })
                                yield _sse(_status_payload(
                                    worker_key,
                                    "error",
                                    f"Background helper {idx} failed on endpoint {endpoint_port}: {exc}",
                                    worker_index=idx,
                                    endpoint=endpoint,
                                    endpoint_port=endpoint_port,
                                ))

                    merged_reasoning_parts: list[str] = []
                    merged_draft_parts: list[str] = []
                    merged_tool_msgs: list[dict] = []

                    for run_result in worker_runs:
                        if isinstance(run_result, Exception):
                            log.warning("chat[%s] background helper task failed: %s", stream_id, run_result)
                            continue
                        endpoint_label = str(run_result.get("endpoint") or "local")
                        worker_reasoning = str(run_result.get("reasoning") or "").strip()
                        worker_content = str(run_result.get("content") or "").strip()
                        worker_tool_msgs = run_result.get("tool_msgs") or []
                        if worker_reasoning:
                            merged_reasoning_parts.append(f"[{endpoint_label}]\n{worker_reasoning}")
                        if worker_content:
                            compact_worker_content = worker_content
                            if len(compact_worker_content) > 1200:
                                compact_worker_content = compact_worker_content[:1200].rstrip() + "\n[... truncated ...]"
                            merged_draft_parts.append(f"[{endpoint_label}]\n{compact_worker_content}")
                        merged_tool_msgs.extend(worker_tool_msgs)

                    deduped_tool_msgs: list[dict] = []
                    dedupe_keys: set[str] = set()
                    duplicate_tool_results = 0
                    for tool_msg in merged_tool_msgs:
                        tool_name = str(tool_msg.get("name", "unknown"))
                        tool_content = str(tool_msg.get("content", ""))
                        fingerprint = hashlib.sha256(tool_content.encode("utf-8", errors="ignore")).hexdigest()
                        dedupe_key = f"{tool_name}:{fingerprint}"
                        if dedupe_key in dedupe_keys:
                            duplicate_tool_results += 1
                            continue
                        dedupe_keys.add(dedupe_key)
                        deduped_tool_msgs.append(tool_msg)
                    merged_tool_msgs = deduped_tool_msgs

                    # Inject background results into main stage context
                    if merged_reasoning_parts or merged_draft_parts or merged_tool_msgs:
                        background_context_parts: list[str] = [
                            "=== Background Analysis (from lightweight reasoning model) ===",
                        ]
                        if merged_reasoning_parts:
                            background_context_parts.append("Reasoning:\n" + "\n\n".join(merged_reasoning_parts))
                        if merged_draft_parts:
                            background_draft_excerpt = merged_draft_parts[0]
                            background_context_parts.append("Background draft:\n" + "\n\n".join(merged_draft_parts))
                        if merged_tool_msgs:
                            background_context_parts.append("Tool Results:")
                            for tool_msg in merged_tool_msgs:
                                tool_name = tool_msg.get("name", "unknown")
                                tool_content = str(tool_msg.get("content", "")).strip()
                                # Truncate extremely long tool outputs
                                if len(tool_content) > 500:
                                    tool_content = tool_content[:500] + "\n[... truncated ...]"
                                background_context_parts.append(f"• {tool_name}: {tool_content}")

                        background_context_text = "\n\n".join(background_context_parts)

                        # Inject into working_msgs: merge with existing system message or create new one
                        if working_msgs and working_msgs[0].get("role") == "system":
                            working_msgs[0]["content"] = (
                                working_msgs[0]["content"]
                                + "\n\n"
                                + background_context_text
                            )
                        else:
                            working_msgs.insert(0, {
                                "role": "system",
                                "content": background_context_text,
                            })

                        log.info(
                            "chat[%s] injected background context: workers=%d reasoning_parts=%d tool_count=%d deduped=%d",
                            stream_id,
                            len(helper_targets),
                            len(merged_reasoning_parts),
                            len(merged_tool_msgs),
                            duplicate_tool_results,
                        )

                    draft_chars = sum(len(part) for part in merged_draft_parts)
                    yield f"data: {json.dumps({'type': 'status', 'key': 'background_stage', 'status': 'done', 'message': f'Background stage complete: workers={len(helper_targets)}, tool_results={len(merged_tool_msgs)}, draft_chars={draft_chars}', 'worker_summary': worker_summaries})}\n\n"

                except Exception as exc:
                    log.warning(
                        "chat[%s] background stage failed; continuing with main stage only: %s",
                        stream_id,
                        exc,
                    )
                    yield f"data: {json.dumps({'type': 'status', 'key': 'background_stage', 'status': 'error', 'message': f'Background stage failed, continuing on main model: {exc}'})}\n\n"
            else:
                skip_reason = "policy/feature gating"
                if not use_any_tooling:
                    skip_reason = "no tooling requested"
                elif not background_intent:
                    skip_reason = background_intent_reason
                elif agentic_policy == "heavy_only" and not heavy_tooling_requested:
                    skip_reason = "heavy_only policy with light tooling"
                elif not available_helper_endpoints:
                    skip_reason = f"helper endpoints offline ({', '.join(helper_candidates)})"
                yield f"data: {json.dumps({'type': 'status', 'key': 'background_stage', 'status': 'done', 'message': f'Background stage skipped: {skip_reason}'})}\n\n"

            final_pass_active = requested_provider == "openai"
            if final_pass_active:
                yield _sse(_status_payload(
                    "final_pass",
                    "running",
                    "OpenAI final pass running (tool-capable)",
                    helpers_ran=run_background_stage,
                ))

            if requested_provider == "openai":
                qwen_tool_registry: dict = {}
                mcp_tool_names: set[str] = set()
                openai_tool_schemas: list[dict] = []
                seen_openai_tools: set[str] = set()

                try:
                    from qwen_agent.tools.base import TOOL_REGISTRY as _QWEN_TOOL_REGISTRY  # noqa: PLC0415

                    qwen_tool_registry = _QWEN_TOOL_REGISTRY
                except Exception as exc:
                    log.warning("chat[%s] qwen tool registry unavailable for OpenAI tool loop: %s", stream_id, exc)

                if use_any_tooling:
                    function_list = _build_agent_function_list(include_mcp_tools=include_mcp_for_run, stage="main")
                    for item in function_list:
                        if isinstance(item, str):
                            tool_name = str(item or "").strip()
                            if not tool_name or tool_name in seen_openai_tools:
                                continue
                            tool_entry = qwen_tool_registry.get(tool_name)
                            if tool_entry is None:
                                log.warning("chat[%s] OpenAI loop missing tool registry entry for %s", stream_id, tool_name)
                                continue
                            try:
                                if isinstance(tool_entry, type):
                                    description = str(getattr(tool_entry, "description", "") or "")
                                    parameters = getattr(tool_entry, "parameters", {})
                                else:
                                    description = str(getattr(tool_entry, "description", "") or "")
                                    parameters = getattr(tool_entry, "parameters", {})
                                    if not parameters and hasattr(tool_entry, "__class__"):
                                        parameters = getattr(tool_entry.__class__, "parameters", {})
                                openai_tool_schemas.append({
                                    "type": "function",
                                    "function": {
                                        "name": tool_name,
                                        "description": description,
                                        "parameters": _normalize_tool_parameters(parameters),
                                    },
                                })
                                seen_openai_tools.add(tool_name)
                            except Exception as exc:
                                log.warning("chat[%s] failed to build schema for tool %s: %s", stream_id, tool_name, exc)
                        elif isinstance(item, dict):
                            try:
                                from agent_tools import mcp_registry  # noqa: PLC0415

                                mcp_registry.initialize(item)
                                for schema in mcp_registry.get_schemas():
                                    fn = schema.get("function", {}) if isinstance(schema, dict) else {}
                                    mcp_name = str(fn.get("name") or "").strip()
                                    if not mcp_name or mcp_name in seen_openai_tools:
                                        continue
                                    openai_tool_schemas.append(schema)
                                    mcp_tool_names.add(mcp_name)
                                    seen_openai_tools.add(mcp_name)
                            except Exception as exc:
                                log.warning("chat[%s] failed to initialise MCP schemas for OpenAI loop: %s", stream_id, exc)

                openai_msgs = [
                    dict(m) if isinstance(m, dict) else m
                    for m in working_msgs
                ]
                openai_turn_limit = 10

                yield _sse(
                    _status_payload(
                        "main_stage",
                        "running",
                        f"OpenAI main stage running with native tools ({len(openai_tool_schemas)} available)",
                    )
                )

                for openai_turn in range(1, openai_turn_limit + 1):
                    response_data = await _call_openai_chat_completion(
                        openai_msgs,
                        openai_tool_schemas if openai_tool_schemas else None,
                    )
                    choices = response_data.get("choices") or []
                    if not choices or not isinstance(choices[0], dict):
                        raise RuntimeError("OpenAI response did not include choices[0]")

                    assistant_message = choices[0].get("message")
                    if not isinstance(assistant_message, dict):
                        raise RuntimeError("OpenAI response choices[0].message is missing")

                    assistant_content_obj = assistant_message.get("content")
                    assistant_content_text = _extract_openai_message_text(assistant_content_obj)
                    assistant_tool_calls = assistant_message.get("tool_calls")
                    if not isinstance(assistant_tool_calls, list):
                        assistant_tool_calls = []

                    if assistant_content_text:
                        if assistant_content_text.startswith(final_content):
                            content_delta = assistant_content_text[len(final_content):]
                        else:
                            content_delta = assistant_content_text
                        if content_delta:
                            yield f"data: {json.dumps({'type': 'content', 'delta': content_delta})}\n\n"
                        final_content = assistant_content_text

                    assistant_history_msg: dict[str, object] = {"role": "assistant"}
                    assistant_history_msg["content"] = assistant_content_text or ""
                    if assistant_tool_calls:
                        assistant_history_msg["tool_calls"] = assistant_tool_calls
                    openai_msgs.append(assistant_history_msg)

                    if not assistant_tool_calls:
                        break

                    for call_index, tool_call in enumerate(assistant_tool_calls, start=1):
                        if not isinstance(tool_call, dict):
                            continue
                        tool_call_id = str(tool_call.get("id") or f"call_{openai_turn}_{call_index}")
                        function_info = tool_call.get("function") if isinstance(tool_call.get("function"), dict) else {}
                        tool_name = str(function_info.get("name") or "").strip()
                        args_raw = function_info.get("arguments", "{}")
                        if isinstance(args_raw, str):
                            try:
                                args_obj = json.loads(args_raw) if args_raw.strip() else {}
                            except Exception:
                                args_obj = {"raw": args_raw}
                        elif isinstance(args_raw, dict):
                            args_obj = args_raw
                        else:
                            args_obj = {}

                        if not tool_name:
                            tool_name = "unknown_tool"

                        dedupe_key = tool_call_id or f"{tool_name}:{json.dumps(args_obj, sort_keys=True, ensure_ascii=False)}"
                        if dedupe_key not in seen_tool_call_ids:
                            seen_tool_call_ids.add(dedupe_key)
                            yield f"data: {json.dumps({'type': 'tool_call', 'name': tool_name, 'args': args_obj})}\n\n"

                        tool_output = await _execute_named_tool_call(
                            tool_name,
                            args_obj,
                            qwen_tool_registry,
                            mcp_tool_names,
                        )
                        tool_ok = not bool(TOOL_ERROR_RE.search(str(tool_output or "")))
                        tool_summary = _compact_tool_summary(tool_name, str(tool_output or ""), tool_ok)
                        tool_result_summaries.append(f"{tool_name}: {tool_summary}")
                        yield f"data: {json.dumps({'type': 'tool_result', 'name': tool_name, 'ok': tool_ok, 'summary': tool_summary})}\n\n"

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
                            gml_snippet_count += len(re.findall(r"^\[\d+\]", str(tool_output or ""), flags=re.MULTILINE))
                        elif tool_name == "ps_docs_search":
                            ps_snippet_count += len(re.findall(r"^\[\d+\]", str(tool_output or ""), flags=re.MULTILINE))

                        openai_msgs.append(
                            {
                                "role": "tool",
                                "tool_call_id": tool_call_id,
                                "name": tool_name,
                                "content": str(tool_output or ""),
                            }
                        )
                else:
                    yield _sse(
                        _status_payload(
                            "main_stage",
                            "error",
                            f"OpenAI tool loop reached turn limit ({openai_turn_limit}); returning best available answer",
                        )
                    )

                working_msgs = openai_msgs

            while requested_provider != "openai":
                yield _sse(
                    _status_payload(
                        "main_stage",
                        "running",
                        f"Main model {requested_model} is thinking on {main_model_server}",
                    )
                )
                response_iter = agent.run(messages=working_msgs, lang="en")
                prev_content = ""
                prev_thinking = ""
                seen_function_messages = 0
                emitted_output = False

                try:
                    async for packet in _iter_with_heartbeat(
                        response_iter,
                        phase_key="main_stage",
                        phase_label=f"Main model {requested_model} is thinking",
                    ):
                        if packet.get("type") == "heartbeat":
                            yield _sse(packet)
                            continue
                        rsp = packet.get("rsp")
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
                                tool_summary = _compact_tool_summary(tool_name, tool_content, tool_ok)
                                tool_result_summaries.append(f"{tool_name}: {tool_summary}")
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
                    if (
                        requested_provider == "openai"
                        and use_any_tooling
                        and not retried_prompt_injection_for_openai
                        and "tool_call_id" in exc_text
                    ):
                        retried_prompt_injection_for_openai = True
                        use_raw_api = False
                        llm_cfg["generate_cfg"] = _build_generate_cfg(raw_api_mode=False)
                        log.warning(
                            "chat[%s] OpenAI raw tool-call compatibility error; retrying once with prompt-injection mode: %s",
                            stream_id,
                            exc_text,
                        )
                        yield _sse(_status_payload(
                            "tool_compat_retry",
                            "running",
                            "Retrying tool phase with OpenAI compatibility mode",
                        ))
                        agent = _make_agent(include_mcp_tools=include_mcp_for_run, stage="main")
                        continue
                    if retry_without_mcp_on_eof and not emitted_output and "EOF" in exc_text:
                        retry_without_mcp_on_eof = False
                        include_mcp_for_run = False
                        log.warning(
                            "chat[%s] upstream EOF before output; retrying stream once without MCP tools: %s",
                            stream_id,
                            exc_text,
                        )
                        agent = _make_agent(include_mcp_tools=False, stage="main")
                        continue
                    raise

            if final_pass_active:
                yield _sse(_status_payload(
                    "final_pass",
                    "done",
                    "OpenAI final pass complete",
                ))

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
                yield f"data: {json.dumps({'type': 'tool_call', 'name': tool_name, 'args': args_obj})}\n\n"
                handled, tool_result = await asyncio.to_thread(_execute_literal_tool_call, tool_name, args_obj)
                if handled:
                    tool_ok = not bool(TOOL_ERROR_RE.search(tool_result))
                    tool_summary = re.sub(r"\s+", " ", tool_result).strip()[:300]
                    tool_result_summaries.append(f"{tool_name}: {tool_summary if tool_summary else ('ok' if tool_ok else 'error')}")
                    yield f"data: {json.dumps({'type': 'tool_result', 'name': tool_name, 'ok': tool_ok, 'summary': tool_summary if tool_summary else ('ok' if tool_ok else 'error')})}\n\n"
                    tools_called += 1
                    lowered_literal_tool = str(tool_name or "").lower()
                    if lowered_literal_tool == "code_interpreter":
                        code_runs += 1
                    elif lowered_literal_tool == "run_powershell":
                        powershell_runs += 1
                    elif "read_file" in lowered_literal_tool:
                        file_reads += 1
                    elif any(k in lowered_literal_tool for k in ["write_file", "replace_in_file", "create_directory"]):
                        file_writes += 1

                    cleaned_prefix = _strip_literal_tool_markup(final_content)
                    final_content = f"{cleaned_prefix}\n\n{tool_result}".strip() if cleaned_prefix else tool_result
                    yield f"data: {json.dumps({'type': 'content_replace', 'content': final_content})}\n\n"
                    token_count = estimate_tokens(final_content + all_thinking)
                else:
                    cleaned = _strip_literal_tool_markup(final_content)
                    if cleaned != final_content:
                        final_content = cleaned
                        yield f"data: {json.dumps({'type': 'content_replace', 'content': final_content})}\n\n"
                    summary = (
                        f"Protocol mismatch: model emitted literal markup for '{tool_name}' "
                        "instead of native tool_calls."
                    )
                    yield f"data: {json.dumps({'type': 'tool_result', 'name': tool_name, 'ok': False, 'summary': summary})}\n\n"

                    if not strict_literal_recovery_attempted:
                        strict_literal_recovery_attempted = True
                        yield _sse(_status_payload("strict_recovery", "running", "Literal tool markup could not be mapped; running strict recovery pass"))
                        recovery_messages = [dict(m) if isinstance(m, dict) else m for m in working_msgs]
                        strict_instruction = (
                            "Recovery mode: your previous response emitted literal tool markup. "
                            "Do not emit <function=...> tags. Do not call tools in this pass. "
                            "Using the provided conversation context and background analysis, "
                            "produce the best direct answer for the user now."
                        )
                        if recovery_messages and isinstance(recovery_messages[0], dict) and recovery_messages[0].get("role") == "system":
                            recovery_messages[0]["content"] = str(recovery_messages[0].get("content") or "") + "\n\n" + strict_instruction
                        else:
                            recovery_messages.insert(0, {"role": "system", "content": strict_instruction})

                        recovery_agent = Assistant(
                            function_list=[],
                            llm=get_chat_model(llm_cfg),
                            system_message="",
                        )
                        recovery_iter = recovery_agent.run(messages=recovery_messages, lang="en")
                        recovery_content = ""
                        recovery_thinking = ""
                        async for packet in _iter_with_heartbeat(
                            recovery_iter,
                            phase_key="strict_recovery",
                            phase_label=f"Strict recovery on {requested_model}",
                        ):
                            if packet.get("type") == "heartbeat":
                                yield _sse(packet)
                                continue
                            rsp = packet.get("rsp")
                            if not isinstance(rsp, list):
                                continue
                            for msg in rsp:
                                if not (hasattr(msg, "get") and msg.get("role") == "assistant"):
                                    continue
                                c = str(msg.get("content") or "")
                                t = str(msg.get("reasoning_content") or msg.get("thinking") or "")
                                if c:
                                    recovery_content = c
                                if t:
                                    recovery_thinking = t

                        if recovery_content.strip():
                            final_content = recovery_content.strip()
                            if recovery_thinking.strip():
                                all_thinking = recovery_thinking.strip()
                            yield f"data: {json.dumps({'type': 'content_replace', 'content': final_content})}\n\n"
                            token_count = estimate_tokens(final_content + all_thinking)
                            yield _sse(_status_payload("strict_recovery", "done", "Strict recovery produced a final answer"))
                        else:
                            yield _sse(_status_payload("strict_recovery", "error", "Strict recovery produced no assistant content"))

            if not str(final_content or "").strip():
                synthesized_parts: list[str] = [
                    "I could not produce a direct final answer from the model output, but here is what I gathered:",
                ]
                if background_draft_excerpt:
                    synthesized_parts.append("Background draft:\n" + background_draft_excerpt[:900])
                if tool_result_summaries:
                    compact_summaries = tool_result_summaries[:6]
                    synthesized_parts.append("Tool observations:\n" + "\n".join(f"- {line}" for line in compact_summaries))
                if codebase_snippet_count:
                    synthesized_parts.append(f"Retrieved {codebase_snippet_count} codebase snippet(s) for context.")
                if len(synthesized_parts) == 1:
                    synthesized_parts.append("No tool outputs or background draft were available.")
                final_content = "\n\n".join(synthesized_parts).strip()
                yield f"data: {json.dumps({'type': 'content_replace', 'content': final_content})}\n\n"
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
            yield _sse(_status_payload("main_stage", "done", "Main model response complete"))
            yield f"data: {json.dumps({'type': 'done', 'token_count': token_count, 'fts_used': bool(fts_snippets), 'tools_called': tools_called, 'searches_done': searches_done, 'commands_run': code_runs, 'code_runs': code_runs, 'powershell_runs': powershell_runs, 'file_reads': file_reads, 'file_writes': file_writes, 'gml_used': gml_snippet_count > 0, 'gml_snippet_count': gml_snippet_count, 'ps_docs_used': ps_snippet_count > 0, 'ps_docs_snippet_count': ps_snippet_count, 'codebase_used': codebase_snippet_count > 0, 'codebase_snippet_count': codebase_snippet_count, 'main_model': requested_model, 'main_model_server': main_model_server, 'background_model': agentic_endpoint_model, 'background_model_server': background_model_server})}\n\n"
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
            if db is not None and (final_content or all_thinking):
                try:
                    await save_messages(db, req.conversation_id, req.message, final_content, all_thinking)
                except Exception as exc:
                    log.error("chat[%s] failed to save messages: %s", stream_id, exc)
            log.info("chat[%s] stream closed", stream_id)
            if db is not None:
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

    # Auto-reload is disabled by default because ChromaDB/SQLite embedding files
    # live inside the project tree and trigger constant reloads, crashing the server.
    # Set UVICORN_RELOAD=1 to re-enable hot reload during front-end-only development.
    _reload = (os.getenv("UVICORN_RELOAD", "0") or "0").strip().lower() in {"1", "true", "yes", "on"}

    uvicorn.run(
        "server:app",
        host="0.0.0.0",
        port=42069,
        reload=_reload,
        reload_excludes=[
            # Embedding vector databases (ChromaDB writes these constantly)
            "gml_embeddings/*",
            "gml_embeddings/**",
            "ps_docs_embeddings/*",
            "ps_docs_embeddings/**",
            "codebase_embeddings/*",
            "codebase_embeddings/**",
            "workspace_embeddings/*",
            "workspace_embeddings/**",
            # SQLite WAL/SHM journal files (written on every DB transaction)
            "**/*.sqlite3",
            "**/*.sqlite3-wal",
            "**/*.sqlite3-shm",
            # Code-interpreter kernel temp files
            "workspace/tools/code_interpreter/*",
            "workspace/tools/code_interpreter/**",
            "**/launch_kernel_*.py",
            "**/kernel_connection_file_*",
        ],
    )
