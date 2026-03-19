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
import subprocess
import uuid
from collections import Counter
from contextlib import asynccontextmanager
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import AsyncGenerator

from dotenv import load_dotenv

load_dotenv(Path(__file__).parent / ".env")

import aiohttp
import aiosqlite
from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from fastapi.responses import HTMLResponse, StreamingResponse
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
OLLAMA_URL        = "http://localhost:11434/api/chat"
OLLAMA_HEALTH_URL = "http://127.0.0.1:11434/api/tags"
BRAVE_SEARCH_URL  = "https://api.search.brave.com/res/v1/web/search"
DEFAULT_MODEL     = "huihui_ai/qwen3-abliterated:8b"
DB_PATH           = Path(__file__).parent / "memory.db"
HTML_PATH         = Path(__file__).parent / "index.html"
CONFIG_PATH       = Path(__file__).parent / "config.json"
GML_DOCS_ROOT     = Path(__file__).parent / "gml"
GML_EMBEDDINGS_DB = Path(__file__).parent / "gml_embeddings"
TOKEN_CAP              = 20_000  # max tokens kept in active context
FTS_RESULT_LIMIT       = 3       # past-memory snippets to inject when truncated
TOKEN_ESTIMATE_DIVISOR = 4       # chars / 4 ≈ tokens
MAX_SEARCH_ITERATIONS  = 3       # max Brave searches per response
BRAVE_SEARCH_COUNT     = 5       # results to fetch per query
GML_RESULT_LIMIT       = 4       # local GML manual snippets to inject
GML_CHUNK_CHAR_LIMIT   = 1_400   # target chunk size for manual retrieval
JWT_ALGORITHM          = "HS256"
ACCESS_TOKEN_HOURS     = 24

SEARCH_TAG_RE = re.compile(r'<search>(.*?)</search>', re.IGNORECASE | re.DOTALL)
GML_TOKEN_RE = re.compile(r"[a-zA-Z_][a-zA-Z0-9_]*")

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
    "If local GameMaker manual excerpts are provided, use them as your primary source. "
    "If the excerpts do not fully answer the question, say what is missing instead of inventing APIs or behavior."
)

FILE_TOOLS_SYSTEM_PROMPT = (
    "You have access to local file operations tools for reading, writing, and searching files. "
    "The workspace is sandboxed to a specific root directory configured by your admin. "
    "You can use these tools to analyze code, make edits, and validate your work. "
    "Command execution (execute_command tool) is always gated: you will receive a permission prompt before any command runs. "
    "Provide complete, correct tool calls; the user will handle permission dialogs. "
    "If you show a tool call in assistant-visible text, always surround it with a markdown fenced code block."
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
    app.state.embeddings_ready = False
    app.state.embeddings_building = CHROMADB_AVAILABLE
    if CHROMADB_AVAILABLE:
        get_or_init_embedding_model()
        get_or_init_chroma_client()
        asyncio.create_task(_build_embeddings_background())
    log.info("Database initialised at %s", DB_PATH)
    yield


app = FastAPI(title="Ollama Qwen3 Chat", lifespan=lifespan)
_ollama_start_lock = asyncio.Lock()
_gml_index_lock = asyncio.Lock()
_auth_scheme = HTTPBearer(auto_error=False)
_pwd_context = CryptContext(schemes=["pbkdf2_sha256"], deprecated="auto")

# Command approval state: {cmd_id: (event, user_id, result, command)}
_pending_approvals: dict[str, tuple[asyncio.Event, str, bool, str]] = {}
_pending_approvals_lock = asyncio.Lock()

# Embeddings model (lazy-loaded)
_embedding_model: SentenceTransformerEmbeddingFunction | None = None
_chroma_client = None  # chromadb.PersistentClient, typed loosely to avoid import quirks

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
    db = await aiosqlite.connect(DB_PATH)
    db.row_factory = aiosqlite.Row
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
    """Migrate users table to add file tools columns if missing."""
    cursor = await db.execute("PRAGMA table_info(users)")
    rows = await cursor.fetchall()
    cols = {row["name"] for row in rows}
    if "file_tools_enabled" not in cols:
        await db.execute("ALTER TABLE users ADD COLUMN file_tools_enabled INTEGER NOT NULL DEFAULT 0")
    if "workspace_root" not in cols:
        await db.execute("ALTER TABLE users ADD COLUMN workspace_root TEXT NOT NULL DEFAULT ''")
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


async def backfill_legacy_conversations(db: aiosqlite.Connection, fallback_user_id: str) -> None:
    await db.execute(
        "UPDATE conversations SET user_id = ? WHERE user_id IS NULL OR TRIM(user_id) = ''",
        (fallback_user_id,),
    )
    await db.commit()


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
            "SELECT id, username, role, is_active, file_tools_enabled, workspace_root, created_at FROM users WHERE id=?",
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
    use_file_tools: bool = False


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


class CommandApprovalRequest(BaseModel):
    cmd_id: str
    approved: bool


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


def build_gml_index(root: Path) -> dict:
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
        stats["error"] = f"GML docs folder not found: {root}"
        return stats

    chunks: list[dict] = []
    for md_path in sorted(root.rglob("*.md")):
        try:
            raw_text = md_path.read_text(encoding="utf-8", errors="ignore")
        except Exception as exc:
            log.warning("Failed to read GML doc %s: %s", md_path, exc)
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

        gml_index = build_gml_index(GML_DOCS_ROOT)
        app.state.gml_index = gml_index
        log.info(
            "GML doc index ready: %d files, %d chunks",
            gml_index.get("file_count", 0),
            gml_index.get("chunk_count", 0),
        )
        if gml_index.get("error"):
            log.warning("GML doc index warning: %s", gml_index["error"])
        return gml_index


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


def get_or_init_chroma_client():
    global _chroma_client
    if not CHROMADB_AVAILABLE:
        return None
    if _chroma_client is None:
        try:
            GML_EMBEDDINGS_DB.mkdir(parents=True, exist_ok=True)
            _chroma_client = chromadb.PersistentClient(path=str(GML_EMBEDDINGS_DB))
            log.info("Chroma persistent client initialized at %s", GML_EMBEDDINGS_DB)
        except Exception as exc:
            log.error("Failed to initialize Chroma client: %s", exc)
            return None
    return _chroma_client


def _chromadb_build_sync(chunks: list[dict]) -> dict:
    """Synchronous chromadb upsert — intended for thread-pool execution.

    Skips the full rebuild when a persisted collection already contains the
    exact same number of chunks (i.e. the GML docs haven't changed since the
    last run).  Delete GML_EMBEDDINGS_DB to force a full rebuild.
    """
    embedding_fn = get_or_init_embedding_model()
    client = get_or_init_chroma_client()
    if not embedding_fn or not client:
        return {
            "enabled": False,
            "error": "Failed to initialize embeddings or Chroma client",
            "chunk_count": 0,
        }
    collection_name = "gml_docs"
    try:
        # Check if a valid cached collection already exists.
        existing = client.get_or_create_collection(
            name=collection_name,
            embedding_function=embedding_fn,
            metadata={"hnsw:space": "cosine"},
        )
        if existing.count() == len(chunks):
            log.info(
                "GML embeddings cache hit: %d chunks already indexed, skipping rebuild",
                len(chunks),
            )
            return {"enabled": True, "chunk_count": len(chunks), "collection_name": collection_name}

        # Count mismatch — docs changed, rebuild from scratch.
        log.info(
            "GML embeddings cache miss (%d stored vs %d current), rebuilding…",
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
        log.info("Built GML embeddings collection: %d chunks indexed", len(ids))
        return {"enabled": True, "chunk_count": len(ids), "collection_name": collection_name}
    except Exception as exc:
        log.error("Failed to build GML embeddings collection: %s", exc)
        return {"enabled": False, "error": str(exc), "chunk_count": 0}


async def _build_embeddings_background() -> None:
    """Background task: builds Chroma embeddings without blocking the event loop."""
    try:
        gml_index = getattr(app.state, "gml_index", None)
        if not gml_index or not gml_index.get("chunks"):
            log.warning("GML embeddings: index not ready, skipping build")
            app.state.embeddings_ready = False
            return
        result = await asyncio.to_thread(_chromadb_build_sync, gml_index["chunks"])
        app.state.embeddings_ready = result.get("enabled", False)
        if result.get("enabled"):
            log.info("GML embeddings collection ready: %d chunks", result["chunk_count"])
        else:
            log.warning("GML embeddings not available: %s", result.get("error", "unknown"))
    except Exception as exc:
        log.error("GML embeddings background task failed: %s", exc)
        app.state.embeddings_ready = False
    finally:
        app.state.embeddings_building = False


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
    return await asyncio.to_thread(_chromadb_build_sync, gml_index["chunks"])


def search_gml_docs(query: str, limit: int = GML_RESULT_LIMIT) -> list[dict]:
    """Search GML docs using vector embeddings (semantic search)."""
    if not CHROMADB_AVAILABLE:
        log.warning("Chroma not available; cannot perform semantic search")
        return []
    
    client = get_or_init_chroma_client()
    if not client:
        return []
    
    try:
        collection = client.get_collection(name="gml_docs")
    except Exception as exc:
        log.warning("GML embeddings collection not found: %s. Falling back to empty results.", exc)
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
        log.error("GML semantic search failed: %s", exc)
        return []


def format_gml_snippets(snippets: list[dict]) -> str:
    lines = [
        "The following excerpts were retrieved from the local GameMaker markdown manual under /gml.",
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

MAX_TOOL_ITERATIONS = 15
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
    if path == "" or path == ".":
        target = Path(workspace_root).resolve()
    else:
        target = resolve_sandboxed_path(workspace_root, path)
    
    if not target.is_dir():
        raise FileToolError(f"Not a directory or does not exist: {target}")
    
    entries = []
    try:
        items = sorted(target.iterdir())
    except PermissionError:
        raise FileToolError(f"Permission denied reading directory: {target}")
    
    if len(items) > 500:
        items = items[:500]
        entries.append("[listing truncated at 500 entries]")
    
    for item in items:
        if item.is_dir():
            entries.append(f"{item.name}/")
        else:
            entries.append(item.name)
    
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
            "SELECT id, username, password_hash, role, is_active, file_tools_enabled, workspace_root, created_at FROM users WHERE username=?",
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
        "created_at": current_user["created_at"],
    }


@app.get("/api/admin/users")
async def admin_list_users(_: dict = Depends(require_admin)):
    db = await get_db()
    try:
        cursor = await db.execute(
            "SELECT id, username, role, is_active, file_tools_enabled, workspace_root, created_at FROM users ORDER BY created_at ASC"
        )
        rows = await cursor.fetchall()
        return [dict(r) for r in rows]
    finally:
        await db.close()


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
            "SELECT id, username, role, is_active, file_tools_enabled, workspace_root, created_at FROM users WHERE id=?",
            (user_id,),
        )
        user = await cursor.fetchone()
        return dict(user) if user else {"ok": True}
    finally:
        await db.close()


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
    embeddings_enabled = CHROMADB_AVAILABLE and getattr(app.state, "embeddings_ready", False)
    embeddings_building = CHROMADB_AVAILABLE and getattr(app.state, "embeddings_building", False)
    return {
        "brave_api_key_set": bool(key),
        "brave_api_key_masked": masked,
        "gml_docs_enabled": bool(gml_index.get("enabled")),
        "gml_docs_file_count": gml_index.get("file_count", 0),
        "gml_docs_chunk_count": gml_index.get("chunk_count", 0),
        "gml_docs_indexed_at": gml_index.get("indexed_at", ""),
        "gml_docs_error": gml_index.get("error", ""),
        "gml_embeddings_enabled": embeddings_enabled,
        "gml_embeddings_building": embeddings_building,
        "gml_embeddings_model": "all-MiniLM-L6-v2" if embeddings_enabled else None,
    }


@app.post("/api/settings")
async def update_settings(body: SettingsUpdate, _: dict = Depends(get_current_user)):
    cfg = load_config()
    cfg["brave_api_key"] = body.brave_api_key.strip()
    save_config(cfg)
    return {"ok": True}


@app.post("/api/chat/command-approval")
async def command_approval(
    body: CommandApprovalRequest,
    current_user: dict = Depends(get_current_user),
):
    """
    Handle user approval/denial of command execution.
    
    The frontend calls this when the user clicks [Approve] or [Deny] on a permission prompt.
    We look up the pending approval by cmd_id, verify it belongs to this user's session,
    then set the event + result so the streaming loop can continue.
    """
    cmd_id = body.cmd_id
    async with _pending_approvals_lock:
        if cmd_id not in _pending_approvals:
            raise HTTPException(
                status_code=404,
                detail="Command approval request not found or already processed",
            )
        event, user_id, _, command = _pending_approvals[cmd_id]
        
        # Security: ensure this approval belongs to the requesting user
        if user_id != current_user["id"]:
            raise HTTPException(
                status_code=403,
                detail="Cannot approve another user's command",
            )
        
        # Update the result and signal the waiting stream
        _pending_approvals[cmd_id] = (event, user_id, body.approved, command)
        event.set()
    
    return {"ok": True, "approved": body.approved}


# ---------------------------------------------------------------------------
# Tool Schemas — Ollama native function calling
# ---------------------------------------------------------------------------

def get_web_search_tool() -> dict:
    """Web search tool schema."""
    return {
        "type": "function",
        "function": {
            "name": "web_search",
            "description": "Search the web using Brave Search API for current information and facts.",
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "The search query (e.g., 'latest AI news' or 'Python asyncio best practices')",
                    }
                },
                "required": ["query"],
            },
        },
    }


def get_file_tools_schemas() -> list[dict]:
    """Return all file operation tool schemas."""
    return [
        {
            "type": "function",
            "function": {
                "name": "read_file",
                "description": "Read a file with optional line range limits. Automatically truncates if file is too large.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "path": {
                            "type": "string",
                            "description": "Relative path to the file (relative to workspace root)",
                        },
                        "start_line": {
                            "type": "integer",
                            "description": "Starting line number (1-indexed, default 1)",
                        },
                        "end_line": {
                            "type": "integer",
                            "description": "Ending line number (1-indexed, default to end of file)",
                        },
                    },
                    "required": ["path"],
                },
            },
        },
        {
            "type": "function",
            "function": {
                "name": "write_file",
                "description": "Write or overwrite a file. Creates parent directories if needed.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "path": {
                            "type": "string",
                            "description": "Relative path to the file (relative to workspace root)",
                        },
                        "content": {
                            "type": "string",
                            "description": "The complete file content to write",
                        },
                    },
                    "required": ["path", "content"],
                },
            },
        },
        {
            "type": "function",
            "function": {
                "name": "replace_in_file",
                "description": "Replace exactly one occurrence of a string in a file. Errors if match count != 1.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "path": {
                            "type": "string",
                            "description": "Relative path to the file",
                        },
                        "old_str": {
                            "type": "string",
                            "description": "The exact string to find and replace",
                        },
                        "new_str": {
                            "type": "string",
                            "description": "The replacement string",
                        },
                    },
                    "required": ["path", "old_str", "new_str"],
                },
            },
        },
        {
            "type": "function",
            "function": {
                "name": "list_dir",
                "description": "List directory contents. Directories are suffixed with '/'.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "path": {
                            "type": "string",
                            "description": "Relative path to the directory (default: workspace root)",
                        },
                    },
                },
            },
        },
        {
            "type": "function",
            "function": {
                "name": "search_files",
                "description": "Search for files matching a glob pattern under a directory.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "pattern": {
                            "type": "string",
                            "description": "Glob pattern (e.g., '*.py' or '**/test_*.py')",
                        },
                        "directory": {
                            "type": "string",
                            "description": "Search directory (default: current workspace root)",
                        },
                    },
                    "required": ["pattern"],
                },
            },
        },
        {
            "type": "function",
            "function": {
                "name": "grep_search",
                "description": "Search for a text query in file(s). Can search a single file or recursively in a directory.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "query": {
                            "type": "string",
                            "description": "Text or regex pattern to search for",
                        },
                        "path": {
                            "type": "string",
                            "description": "File or directory path to search in",
                        },
                        "is_regex": {
                            "type": "boolean",
                            "description": "If true, treat query as regex pattern (default: false)",
                        },
                    },
                    "required": ["query", "path"],
                },
            },
        },
        {
            "type": "function",
            "function": {
                "name": "create_directory",
                "description": "Create a directory (including parent directories).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "path": {
                            "type": "string",
                            "description": "Relative path to the directory to create",
                        },
                    },
                    "required": ["path"],
                },
            },
        },
    ]


def get_execute_command_tool() -> dict:
    """Execute shell command tool schema. Always requires user approval."""
    return {
        "type": "function",
        "function": {
            "name": "execute_command",
            "description": (
                "Execute a shell command. This always requires user approval before execution. "
                "The user will see a confirmation prompt in the chat UI."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "command": {
                        "type": "string",
                        "description": "The shell command to execute (e.g., 'python -m py_compile server.py')",
                    },
                    "cwd": {
                        "type": "string",
                        "description": "Working directory for the command (default: workspace root)",
                    },
                },
                "required": ["command"],
            },
        },
    }


# ---------------------------------------------------------------------------
# Tool Execution Helpers
# ---------------------------------------------------------------------------

async def execute_tool(
    tool_name: str,
    tool_args: dict,
    current_user: dict,
    session_user_id: str,  # for command approval tracking
    cmd_id: str | None = None,
) -> tuple[bool, str]:
    """
    Execute a tool and return (success, result_text).
    For execute_command, this will wait for user approval before running.
    """
    workspace_root = current_user.get("workspace_root", "")
    if not workspace_root:
        return False, "[Error: workspace root not configured]"
    
    try:
        if tool_name == "web_search":
            query = tool_args.get("query", "")
            if not query:
                return False, "[Error: query is required]"
            api_key = get_brave_api_key()
            if not api_key:
                return False, "[Error: No Brave API key configured]"
            results = await brave_search(query, api_key)
            return True, format_search_results(query, results)
        
        elif tool_name == "read_file":
            path = tool_args.get("path", "")
            start_line = tool_args.get("start_line", 1)
            end_line = tool_args.get("end_line")
            result = await asyncio.to_thread(
                ft_read_file, workspace_root, path, start_line, end_line
            )
            return True, result
        
        elif tool_name == "write_file":
            path = tool_args.get("path", "")
            content = tool_args.get("content", "")
            result = await asyncio.to_thread(ft_write_file, workspace_root, path, content)
            return True, result
        
        elif tool_name == "replace_in_file":
            path = tool_args.get("path", "")
            old_str = tool_args.get("old_str", "")
            new_str = tool_args.get("new_str", "")
            result = await asyncio.to_thread(
                ft_replace_in_file, workspace_root, path, old_str, new_str
            )
            return True, result
        
        elif tool_name == "list_dir":
            path = tool_args.get("path", "")
            result = await asyncio.to_thread(ft_list_dir, workspace_root, path)
            return True, result
        
        elif tool_name == "search_files":
            pattern = tool_args.get("pattern", "")
            directory = tool_args.get("directory", ".")
            result = await asyncio.to_thread(
                ft_search_files, workspace_root, pattern, directory
            )
            return True, result
        
        elif tool_name == "grep_search":
            query = tool_args.get("query", "")
            path = tool_args.get("path", "")
            is_regex = tool_args.get("is_regex", False)
            result = await asyncio.to_thread(
                ft_grep_search, workspace_root, query, path, is_regex
            )
            return True, result
        
        elif tool_name == "create_directory":
            path = tool_args.get("path", "")
            result = await asyncio.to_thread(ft_create_directory, workspace_root, path)
            return True, result
        
        elif tool_name == "execute_command":
            command = tool_args.get("command", "")
            cwd = tool_args.get("cwd")
            if not command:
                return False, "[Error: command is required]"
            return await _wait_for_command_approval_and_execute(
                command, cwd or workspace_root, session_user_id, cmd_id
            )
        
        else:
            return False, f"[Error: unknown tool '{tool_name}']"
    
    except FileToolError as exc:
        return False, f"[Error: {str(exc)}]"
    except PermissionError as exc:
        return False, f"[Permission denied: {str(exc)}]"
    except Exception as exc:
        log.exception("Tool execution error for %s", tool_name)
        return False, f"[Error: {str(exc)}]"


async def _wait_for_command_approval_and_execute(
    command: str, cwd: str, user_id: str, cmd_id: str | None
) -> tuple[bool, str]:
    """
    Create a pending approval entry, wait for user approval, then execute or deny.
    Returns (success, output).
    """
    if not cmd_id:
        cmd_id = str(uuid.uuid4())
    event = asyncio.Event()
    
    async with _pending_approvals_lock:
        _pending_approvals[cmd_id] = (event, user_id, False, command)
    
    try:
        # Wait up to 120 seconds for approval (emit permission_required event happens in event_stream)
        await asyncio.wait_for(event.wait(), timeout=120.0)
    except asyncio.TimeoutError:
        async with _pending_approvals_lock:
            if cmd_id in _pending_approvals:
                del _pending_approvals[cmd_id]
        return False, "[Command timed out waiting for user approval (120 seconds)]"
    
    # Get the approval result
    async with _pending_approvals_lock:
        if cmd_id not in _pending_approvals:
            return False, "[Command approval state lost]"
        _, _, approved, _ = _pending_approvals[cmd_id]
        del _pending_approvals[cmd_id]
    
    if not approved:
        return False, "[User denied command execution]"
    
    # Execute the command
    try:
        proc = await asyncio.create_subprocess_shell(
            command,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
            cwd=cwd,
            limit=10_000,
        )
        try:
            stdout, stderr = await asyncio.wait_for(
                proc.communicate(), timeout=30.0
            )
        except asyncio.TimeoutError:
            proc.kill()
            _ = await proc.wait()
            return False, "[Command execution timed out (30 seconds)]"
        
        exit_code = proc.returncode
        output = stdout.decode("utf-8", errors="replace")
        error = stderr.decode("utf-8", errors="replace")
        
        result = f"Exit code: {exit_code}\n"
        if output:
            result += f"\nStdout:\n{output[:5000]}"
        if error:
            result += f"\nStderr:\n{error[:5000]}"
        return exit_code == 0, result
    
    except Exception as exc:
        log.exception("Command execution failed: %s", command)
        return False, f"[Command execution error: {str(exc)}]"


# ---------------------------------------------------------------------------
# Chat — streaming SSE with native tool calling
# ---------------------------------------------------------------------------

@app.post("/api/chat")
async def chat(req: ChatRequest, current_user: dict = Depends(get_current_user)):
    if not await ensure_ollama_running(wait_seconds=6):
        raise HTTPException(
            status_code=503,
            detail="Ollama is not available on port 11434 and auto-start failed. Start it with `ollama serve`.",
        )

    # Validate file tools permission
    use_file_tools = req.use_file_tools and bool(current_user.get("file_tools_enabled"))

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

        gml_snippets: list[dict] = []
        if req.use_gml_docs:
            await ensure_gml_index_loaded()
            gml_snippets = search_gml_docs(req.message)
            if gml_snippets:
                log.info("Injecting %d GML snippet(s) for conv %s", len(gml_snippets), req.conversation_id)

        # Build base message list
        ollama_messages: list[dict] = []

        # System prompts based on requested features
        if req.use_gml_docs:
            ollama_messages.append({"role": "system", "content": GML_SYSTEM_PROMPT})
            if gml_snippets:
                ollama_messages.append({
                    "role": "system",
                    "content": format_gml_snippets(gml_snippets),
                })

        if use_file_tools:
            ollama_messages.append({"role": "system", "content": FILE_TOOLS_SYSTEM_PROMPT})

        # Long-term memory injection
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
        all_thinking = ""
        final_content = ""
        tools_called = 0
        commands_run = 0
        file_reads = 0
        file_writes = 0
        working_msgs = list(ollama_messages)
        
        def _build_tools_list() -> list[dict]:
            """Build tool list based on enabled features."""
            tools = []
            if req.use_search:
                tools.append(get_web_search_tool())
            if use_file_tools:
                tools.extend(get_file_tools_schemas())
                tools.append(get_execute_command_tool())
            return tools

        def _payload(msgs: list[dict]) -> dict:
            payload = {
                "model": requested_model,
                "messages": msgs,
                "think": req.think,
                "stream": True,
            }
            tools = _build_tools_list()
            if tools:
                payload["tools"] = tools
            return payload

        try:
            async with aiohttp.ClientSession() as session:
                for iteration in range(MAX_TOOL_ITERATIONS):
                    turn_content = ""
                    turn_thinking = ""
                    turn_tool_calls: list[dict] = []

                    async with session.post(OLLAMA_URL, json=_payload(working_msgs)) as resp:
                        if resp.status != 200:
                            body = await resp.text()
                            yield f"data: {json.dumps({'type': 'error', 'message': body})}\n\n"
                            return

                        # Accumulate all chunks first to get tool_calls which come in the final chunk
                        all_chunks = []
                        async for raw_line in resp.content:
                            line = raw_line.decode("utf-8").strip()
                            if not line:
                                continue
                            try:
                                chunk = json.loads(line)
                                all_chunks.append(chunk)
                            except json.JSONDecodeError:
                                continue

                    # Process accumulated chunks
                    for chunk in all_chunks:
                        msg_chunk = chunk.get("message", {})
                        td = msg_chunk.get("thinking", "")
                        cd = msg_chunk.get("content", "")

                        if td:
                            turn_thinking += td
                            all_thinking += td
                            yield f"data: {json.dumps({'type': 'thinking', 'delta': td})}\n\n"

                        if cd:
                            turn_content += cd
                            final_content += cd
                            yield f"data: {json.dumps({'type': 'content', 'delta': cd})}\n\n"

                        # Tool calls come at the end, but check each chunk
                        if "tool_calls" in msg_chunk:
                            turn_tool_calls.extend(msg_chunk.get("tool_calls", []))

                    # ── Turn complete ──
                    if not turn_tool_calls:
                        # No tools — answer is complete
                        break

                    # Execute tool calls and inject results
                    for tool_call in turn_tool_calls:
                        tool_name = tool_call.get("function", {}).get("name", "")
                        raw_tool_args = tool_call.get("function", {}).get("arguments", {})
                        if isinstance(raw_tool_args, str):
                            try:
                                tool_args = json.loads(raw_tool_args) if raw_tool_args.strip() else {}
                            except json.JSONDecodeError:
                                tool_args = {}
                        elif isinstance(raw_tool_args, dict):
                            tool_args = raw_tool_args
                        else:
                            tool_args = {}
                        approval_cmd_id = tool_call.get("id", "") or str(uuid.uuid4())
                        
                        tools_called += 1
                        
                        if tool_name == "execute_command":
                            commands_run += 1
                            # Emit permission_required event
                            yield f"data: {json.dumps({'type': 'permission_required', 'cmd_id': approval_cmd_id, 'command': tool_args.get('command', ''), 'cwd': tool_args.get('cwd', '')})}\n\n"
                        elif tool_name in ("read_file",):
                            file_reads += 1
                        elif tool_name in ("write_file", "replace_in_file", "create_directory"):
                            file_writes += 1
                        
                        # Emit tool_call event
                        yield f"data: {json.dumps({'type': 'tool_call', 'name': tool_name, 'args': tool_args})}\n\n"
                        
                        # Execute the tool
                        success, result = await execute_tool(
                            tool_name,
                            tool_args,
                            current_user,
                            current_user["id"],
                            approval_cmd_id if tool_name == "execute_command" else None,
                        )
                        
                        # Emit tool_result event
                        summary = result[:200] if len(result) > 200 else result
                        yield f"data: {json.dumps({'type': 'tool_result', 'name': tool_name, 'ok': success, 'summary': summary})}\n\n"
                        
                        # Inject tool result into conversation
                        working_msgs.append({
                            "role": "assistant",
                            "content": turn_content,
                            "tool_calls": [tool_call],
                            **({"thinking": turn_thinking} if turn_thinking else {}),
                        })
                        working_msgs.append({
                            "role": "tool",
                            "content": result,
                            "tool_call_id": tool_call.get("id", ""),
                        })

                    # If we handled tool calls, loop to next turn
                    if turn_tool_calls:
                        # Reset content accumulators for next turn
                        turn_content = ""
                        turn_thinking = ""
                        turn_tool_calls = []
                        continue

            # Stream completed successfully
            token_count = estimate_tokens(final_content + all_thinking)
            yield f"data: {json.dumps({'type': 'done', 'token_count': token_count, 'fts_used': bool(fts_snippets), 'tools_called': tools_called, 'commands_run': commands_run, 'file_reads': file_reads, 'file_writes': file_writes, 'gml_used': bool(gml_snippets), 'gml_snippet_count': len(gml_snippets)})}\n\n"

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
