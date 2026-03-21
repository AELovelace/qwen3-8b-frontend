"""
Qwen-Agent BaseTool registrations, schema utilities, and MCP tool management.

Responsibilities:
  1. Register all native tools as BaseTool subclasses with working call()
     implementations; schemas also double as Ollama-compatible function schemas.
  2. BraveWebSearchTool replaces the default qwen_agent web_search in
     TOOL_REGISTRY to use the project's Brave Search API key.
  3. File tools (read_file / write_file / …) delegate to ft_* functions in
     server.py via lazy imports; they read workspace_root from a per-request
     ContextVar set by set_request_context().
  4. GmlDocsSearchTool / PsDocsSearchTool query local ChromaDB indices for
     GameMaker and PowerShell documentation.
  5. Expose MCPToolRegistry and CodeInterpreterWrapper for the streaming loop.
"""

import base64
import json
import logging
import os
import queue
import shutil
import subprocess
import tempfile
import threading
from contextvars import ContextVar
from pathlib import Path
from typing import Union

log = logging.getLogger(__name__)

try:
    from qwen_agent.tools.base import BaseTool, register_tool, TOOL_REGISTRY as _TOOL_REGISTRY
    QWEN_AGENT_AVAILABLE = True
except ImportError:
    QWEN_AGENT_AVAILABLE = False
    log.warning("qwen-agent not available; agent_tools using stub implementations.")

# ---------------------------------------------------------------------------
# Schema helpers
# ---------------------------------------------------------------------------

_TYPE_MAP = {
    "string": "string", "str": "string",
    "integer": "integer", "int": "integer",
    "number": "number", "float": "number",
    "boolean": "boolean", "bool": "boolean",
    "array": "array", "list": "array",
    "object": "object", "dict": "object",
}


def qwen_params_to_json_schema(parameters) -> dict:
    """Convert Qwen-Agent list-format *or* dict-format parameters to JSON schema.

    Qwen-Agent stores parameters either as:
      - a list: [{'name': ..., 'type': ..., 'description': ..., 'required': bool}]
      - a dict: already a valid JSON schema (type=object)
    Ollama (and OpenAI) expect the dict/JSON-schema form.
    """
    if isinstance(parameters, dict):
        return parameters  # already JSON schema

    props: dict = {}
    required: list = []
    for p in parameters:
        name = p["name"]
        type_str = p.get("type", "string")
        prop: dict = {
            "type": _TYPE_MAP.get(type_str, type_str),
            "description": p.get("description", ""),
        }
        if "enum" in p:
            prop["enum"] = p["enum"]
        props[name] = prop
        if p.get("required", False):
            required.append(name)

    # qwen-agent's internal validator expects an explicit `required` key
    # even when no parameters are required.
    schema: dict = {"type": "object", "properties": props, "required": required}
    try:
        json.dumps(schema)
    except (TypeError, ValueError) as exc:
        log.error("Tool schema is not JSON-serializable: %s", exc)
        raise
    return schema


def tool_to_ollama_schema(tool) -> dict:
    """Convert a BaseTool instance to an Ollama-compatible function schema."""
    return {
        "type": "function",
        "function": {
            "name": tool.name,
            "description": tool.description,
            "parameters": qwen_params_to_json_schema(tool.parameters),
        },
    }


# ---------------------------------------------------------------------------
# Per-request context — set once per streaming request by server.py
# ---------------------------------------------------------------------------

_workspace_root: ContextVar[str] = ContextVar("workspace_root", default="")
_brave_api_key: ContextVar[str] = ContextVar("brave_api_key", default="")
_ps_session_key: ContextVar[str] = ContextVar("ps_session_key", default="")
_ps_mode: ContextVar[str] = ContextVar("ps_mode", default="off")


def set_request_context(
    workspace_root: str = "",
    brave_api_key: str = "",
    ps_session_key: str = "",
    ps_mode: str = "off",
) -> None:
    """Set per-request ContextVar values so BaseTool.call() can access
    user-specific configuration without explicit argument threading.

    Call once at the top of event_stream() in server.py.  ContextVar values are
    isolated per asyncio Task — concurrent requests do not interfere.
    They also propagate to threads spawned by asyncio.to_thread().
    """
    _workspace_root.set(workspace_root)
    _brave_api_key.set(brave_api_key)
    _ps_session_key.set(ps_session_key)
    _ps_mode.set(ps_mode)


def _patch_qwen_code_interpreter_dockerfile() -> None:
    """Ensure qwen-agent's global DOCKER_IMAGE_FILE points to an existing file.

    Important: Chat currently references the registered `code_interpreter` tool
    by name, which instantiates qwen-agent's tool class directly from
    TOOL_REGISTRY. Therefore this patch must happen at import-time so all
    code paths (not only our wrapper) get a valid Dockerfile path.
    """
    if not QWEN_AGENT_AVAILABLE:
        return
    try:
        import qwen_agent.tools.code_interpreter as ci  # noqa: PLC0415
    except Exception as exc:
        log.warning("Unable to import qwen-agent code_interpreter for Dockerfile patch: %s", exc)
        return

    current = Path(str(getattr(ci, "DOCKER_IMAGE_FILE", "") or ""))
    if current.exists():
        return

    env_override_raw = (os.getenv("QWEN_CODE_INTERPRETER_DOCKERFILE", "") or "").strip()
    env_override = Path(env_override_raw) if env_override_raw else None
    local_fallback = Path(__file__).parent / "resources" / "code_interpreter_image.dockerfile"
    packaged_default = Path(ci.__file__).resolve().parent / "resource" / "code_interpreter_image.dockerfile"

    if env_override is not None and env_override.exists():
        chosen = env_override
    elif local_fallback.exists():
        chosen = local_fallback
    elif packaged_default.exists():
        chosen = packaged_default
    else:
        log.warning(
            "No usable Dockerfile found for qwen-agent code_interpreter. "
            "Checked current=%s env=%s local=%s packaged=%s",
            current,
            env_override,
            local_fallback,
            packaged_default,
        )
        return

    ci.DOCKER_IMAGE_FILE = str(chosen)
    log.warning(
        "Patched qwen-agent code_interpreter Dockerfile path: %s -> %s",
        current,
        chosen,
    )


def _patch_qwen_code_interpreter_image_name() -> None:
    """Force a stable, configurable image tag so dependency fixes rebuild cleanly."""
    if not QWEN_AGENT_AVAILABLE:
        return
    try:
        import qwen_agent.tools.code_interpreter as ci  # noqa: PLC0415
    except Exception as exc:
        log.warning("Unable to import qwen-agent code_interpreter for image-name patch: %s", exc)
        return

    if getattr(ci.CodeInterpreter, "_frontend_image_patch_applied", False):
        return

    original_init = ci.CodeInterpreter.__init__

    def _patched_init(self, cfg=None):
        original_init(self, cfg)
        configured_name = (os.getenv("QWEN_CODE_INTERPRETER_IMAGE", "") or "").strip()
        self.docker_image_name = configured_name or "code-interpreter:frontend-v2"

    ci.CodeInterpreter.__init__ = _patched_init
    ci.CodeInterpreter._frontend_image_patch_applied = True
    log.info(
        "Patched qwen-agent CodeInterpreter image tag default to %s",
        (os.getenv("QWEN_CODE_INTERPRETER_IMAGE", "") or "").strip() or "code-interpreter:frontend-v2",
    )


def _ensure_code_interpreter_work_dir() -> None:
    """Set a stable code interpreter work dir outside hot-reload watch paths.

    qwen-agent defaults to `<workspace>/workspace/tools/code_interpreter`, which
    can trigger uvicorn reloads during tool execution in development mode.
    """
    current = (os.getenv("M6_CODE_INTERPRETER_WORK_DIR", "") or "").strip()
    if current:
        return

    fallback_dir = Path(tempfile.gettempdir()) / "frontend_code_interpreter_workspace"
    os.environ["M6_CODE_INTERPRETER_WORK_DIR"] = str(fallback_dir)
    log.info("Set M6_CODE_INTERPRETER_WORK_DIR=%s", fallback_dir)


# ---------------------------------------------------------------------------
# Native tool registrations — call() delegates to server.py ft_* functions
# ---------------------------------------------------------------------------

if QWEN_AGENT_AVAILABLE:
    _ensure_code_interpreter_work_dir()
    _patch_qwen_code_interpreter_dockerfile()
    _patch_qwen_code_interpreter_image_name()

    # ── Web search ────────────────────────────────────────────────────────
    # BraveWebSearchTool replaces qwen_agent's built-in web_search.
    # @register_tool("web_search") raises ValueError (name already registered)
    # so we override _TOOL_REGISTRY directly after class definition.

    class BraveWebSearchTool(BaseTool):
        name = "web_search"
        description = (
            "Search the web using Brave Search API for current information and facts."
        )
        parameters = [
            {
                "name": "query",
                "type": "string",
                "description": "The search query",
                "required": True,
            }
        ]

        def call(self, params: Union[str, dict], **kwargs) -> str:
            import requests as _requests  # noqa: PLC0415
            p = self._verify_json_format_args(params)
            query = p["query"]
            api_key = (
                kwargs.get("brave_api_key")
                or _brave_api_key.get()
                or os.environ.get("BRAVE_API_KEY", "")
            )
            if not api_key:
                return "[Error: No Brave API key configured. Set BRAVE_API_KEY in .env]"
            try:
                resp = _requests.get(
                    "https://api.search.brave.com/res/v1/web/search",
                    headers={
                        "Accept": "application/json",
                        "Accept-Encoding": "gzip",
                        "X-Subscription-Token": api_key,
                    },
                    params={"q": query, "count": 5, "text_decorations": "false"},
                    timeout=10,
                )
                if resp.status_code != 200:
                    return f"[Search API error {resp.status_code}: {resp.text[:200]}]"
                data = resp.json()
                results = [
                    {
                        "title": item.get("title", ""),
                        "url": item.get("url", ""),
                        "description": item.get("description", ""),
                    }
                    for item in data.get("web", {}).get("results", [])
                ]
                if not results:
                    return f"No results found for: {query}"
                lines = [f"Web search results for '{query}':"]
                for i, r in enumerate(results, 1):
                    lines.append(f"\n{i}. {r['title']}")
                    lines.append(f"   {r['url']}")
                    if r["description"]:
                        lines.append(f"   {r['description']}")
                return "\n".join(lines)
            except Exception as exc:
                return f"[Search error: {exc}]"

    # Override built-in qwen_agent web_search with our Brave implementation
    _TOOL_REGISTRY["web_search"] = BraveWebSearchTool

    # ── File tools ────────────────────────────────────────────────────────
    # Each call() lazily imports the corresponding ft_* function from
    # server.py.  Lazy imports inside the function body break the circular
    # import cycle safely (server.py is fully loaded before any call() runs).

    @register_tool("read_file")
    class ReadFileTool(BaseTool):
        description = (
            "Read a file with optional line range limits. "
            "Automatically truncates if file is too large."
        )
        parameters = [
            {
                "name": "path",
                "type": "string",
                "description": "Relative path to the file (relative to workspace root)",
                "required": True,
            },
            {
                "name": "start_line",
                "type": "integer",
                "description": "Starting line number (1-indexed, default 1)",
                "required": False,
            },
            {
                "name": "end_line",
                "type": "integer",
                "description": "Ending line number (1-indexed, default end of file)",
                "required": False,
            },
        ]

        def call(self, params: Union[str, dict], **kwargs) -> str:
            from server import ft_read_file, FileToolError  # noqa: PLC0415
            p = self._verify_json_format_args(params)
            ws = kwargs.get("workspace_root") or _workspace_root.get()
            if not ws:
                return "[Error: workspace_root not configured for this session]"
            try:
                return ft_read_file(ws, p["path"], p.get("start_line", 1), p.get("end_line"))
            except FileToolError as exc:
                return f"[Error: {exc}]"
            except PermissionError as exc:
                return f"[Permission denied: {exc}]"
            except Exception as exc:
                return f"[Error: {exc}]"

    @register_tool("write_file")
    class WriteFileTool(BaseTool):
        description = "Write or overwrite a file. Creates parent directories if needed."
        parameters = [
            {
                "name": "path",
                "type": "string",
                "description": "Relative path to the file (relative to workspace root)",
                "required": True,
            },
            {
                "name": "content",
                "type": "string",
                "description": "The complete file content to write",
                "required": True,
            },
        ]

        def call(self, params: Union[str, dict], **kwargs) -> str:
            from server import ft_write_file, FileToolError  # noqa: PLC0415
            p = self._verify_json_format_args(params)
            ws = kwargs.get("workspace_root") or _workspace_root.get()
            if not ws:
                return "[Error: workspace_root not configured for this session]"
            try:
                return ft_write_file(ws, p["path"], p["content"])
            except FileToolError as exc:
                return f"[Error: {exc}]"
            except PermissionError as exc:
                return f"[Permission denied: {exc}]"
            except Exception as exc:
                return f"[Error: {exc}]"

    @register_tool("replace_in_file")
    class ReplaceInFileTool(BaseTool):
        description = (
            "Replace exactly one occurrence of a string in a file. "
            "Errors if the match count is not exactly 1."
        )
        parameters = [
            {
                "name": "path",
                "type": "string",
                "description": "Relative path to the file",
                "required": True,
            },
            {
                "name": "old_str",
                "type": "string",
                "description": "The exact string to find and replace",
                "required": True,
            },
            {
                "name": "new_str",
                "type": "string",
                "description": "The replacement string",
                "required": True,
            },
        ]

        def call(self, params: Union[str, dict], **kwargs) -> str:
            from server import ft_replace_in_file, FileToolError  # noqa: PLC0415
            p = self._verify_json_format_args(params)
            ws = kwargs.get("workspace_root") or _workspace_root.get()
            if not ws:
                return "[Error: workspace_root not configured for this session]"
            try:
                return ft_replace_in_file(ws, p["path"], p["old_str"], p["new_str"])
            except FileToolError as exc:
                return f"[Error: {exc}]"
            except PermissionError as exc:
                return f"[Permission denied: {exc}]"
            except Exception as exc:
                return f"[Error: {exc}]"

    @register_tool("list_dir")
    class ListDirTool(BaseTool):
        description = "List directory contents. Directories are suffixed with '/'."
        parameters = [
            {
                "name": "path",
                "type": "string",
                "description": "Relative path to directory (default: workspace root)",
                "required": False,
            }
        ]

        def call(self, params: Union[str, dict], **kwargs) -> str:
            from server import ft_list_dir, FileToolError  # noqa: PLC0415
            p = self._verify_json_format_args(params)
            ws = kwargs.get("workspace_root") or _workspace_root.get()
            if not ws:
                log.warning("list_dir call rejected: workspace_root not configured")
                return "[Error: workspace_root not configured for this session]"
            req_path = p.get("path", "")
            log.info("list_dir call start: workspace_root=%s path=%r", ws, req_path)
            try:
                result = ft_list_dir(ws, req_path)
                log.info("list_dir call success: path=%r bytes=%d", req_path, len(result))
                return result
            except FileToolError as exc:
                log.warning("list_dir call file-tool error: path=%r error=%s", req_path, exc)
                return f"[Error: {exc}]"
            except PermissionError as exc:
                log.warning("list_dir call permission denied: path=%r error=%s", req_path, exc)
                return f"[Permission denied: {exc}]"
            except Exception as exc:
                log.exception("list_dir call unexpected error: path=%r", req_path)
                return f"[Error: {exc}]"

    @register_tool("search_files")
    class SearchFilesTool(BaseTool):
        description = "Search for files matching a glob pattern under a directory."
        parameters = [
            {
                "name": "pattern",
                "type": "string",
                "description": "Glob pattern (e.g. '*.py' or '**/test_*.py')",
                "required": True,
            },
            {
                "name": "directory",
                "type": "string",
                "description": "Search directory (default: workspace root)",
                "required": False,
            },
        ]

        def call(self, params: Union[str, dict], **kwargs) -> str:
            from server import ft_search_files, FileToolError  # noqa: PLC0415
            p = self._verify_json_format_args(params)
            ws = kwargs.get("workspace_root") or _workspace_root.get()
            if not ws:
                return "[Error: workspace_root not configured for this session]"
            try:
                return ft_search_files(ws, p["pattern"], p.get("directory", "."))
            except FileToolError as exc:
                return f"[Error: {exc}]"
            except PermissionError as exc:
                return f"[Permission denied: {exc}]"
            except Exception as exc:
                return f"[Error: {exc}]"

    @register_tool("grep_search")
    class GrepSearchTool(BaseTool):
        description = (
            "Search for a text query in file(s). "
            "Can search a single file or recursively in a directory."
        )
        parameters = [
            {
                "name": "query",
                "type": "string",
                "description": "Text or regex pattern to search for",
                "required": True,
            },
            {
                "name": "path",
                "type": "string",
                "description": "File or directory path to search in",
                "required": True,
            },
            {
                "name": "is_regex",
                "type": "boolean",
                "description": "If true, treat query as a regex pattern (default: false)",
                "required": False,
            },
        ]

        def call(self, params: Union[str, dict], **kwargs) -> str:
            from server import ft_grep_search, FileToolError  # noqa: PLC0415
            p = self._verify_json_format_args(params)
            ws = kwargs.get("workspace_root") or _workspace_root.get()
            if not ws:
                return "[Error: workspace_root not configured for this session]"
            try:
                return ft_grep_search(ws, p["query"], p["path"], p.get("is_regex", False))
            except FileToolError as exc:
                return f"[Error: {exc}]"
            except PermissionError as exc:
                return f"[Permission denied: {exc}]"
            except Exception as exc:
                return f"[Error: {exc}]"

    @register_tool("create_directory")
    class CreateDirectoryTool(BaseTool):
        description = "Create a directory (including parent directories)."
        parameters = [
            {
                "name": "path",
                "type": "string",
                "description": "Relative path to the directory to create",
                "required": True,
            }
        ]

        def call(self, params: Union[str, dict], **kwargs) -> str:
            from server import ft_create_directory, FileToolError  # noqa: PLC0415
            p = self._verify_json_format_args(params)
            ws = kwargs.get("workspace_root") or _workspace_root.get()
            if not ws:
                return "[Error: workspace_root not configured for this session]"
            try:
                return ft_create_directory(ws, p["path"])
            except FileToolError as exc:
                return f"[Error: {exc}]"
            except PermissionError as exc:
                return f"[Permission denied: {exc}]"
            except Exception as exc:
                return f"[Error: {exc}]"

    # ── Docs search tools ─────────────────────────────────────────────────

    @register_tool("gml_docs_search")
    class GmlDocsSearchTool(BaseTool):
        description = (
            "Search the local GameMaker Language (GML) manual. "
            "Returns relevant documentation snippets for GML functions, events, and engine behaviour."
        )
        parameters = [
            {
                "name": "query",
                "type": "string",
                "description": "What to look up in the GameMaker manual (e.g. 'instance_create_layer parameters')",
                "required": True,
            }
        ]

        def call(self, params: Union[str, dict], **kwargs) -> str:
            from server import rag_search_gml_docs  # noqa: PLC0415
            p = self._verify_json_format_args(params)
            snippets = rag_search_gml_docs(p["query"])
            if not snippets:
                return "No GML documentation found for that query."
            parts = []
            for i, s in enumerate(snippets, 1):
                parts.append(
                    f"[{i}] {s.get('path', '?')} \u2014 {s.get('heading', '')}\n"
                    f"{s.get('content', '')}"
                )
            return "\n\n".join(parts)

    @register_tool("ps_docs_search")
    class PsDocsSearchTool(BaseTool):
        description = (
            "Search the local PowerShell documentation. "
            "Returns relevant documentation snippets for PowerShell commands, parameters, and scripting patterns."
        )
        parameters = [
            {
                "name": "query",
                "type": "string",
                "description": "What to look up in the PowerShell docs (e.g. 'Get-ChildItem recursive filter')",
                "required": True,
            }
        ]

        def call(self, params: Union[str, dict], **kwargs) -> str:
            from server import rag_search_ps_docs  # noqa: PLC0415
            p = self._verify_json_format_args(params)
            snippets = rag_search_ps_docs(p["query"])
            if not snippets:
                return "No PowerShell documentation found for that query."
            parts = []
            for i, s in enumerate(snippets, 1):
                parts.append(
                    f"[{i}] {s.get('path', '?')} \u2014 {s.get('heading', '')}\n"
                    f"{s.get('content', '')}"
                )
            return "\n\n".join(parts)

    @register_tool("run_powershell")
    class PowerShellTool(BaseTool):
        description = (
            "Execute PowerShell code in a persistent stateful session. "
            "Variables, functions, and imported modules remain available across "
            "subsequent calls within the same conversation. "
            "Use for system administration, automation, file management, and scripting."
        )
        parameters = [
            {
                "name": "code",
                "type": "string",
                "description": "The PowerShell code to execute",
                "required": True,
            },
            {
                "name": "timeout",
                "type": "integer",
                "description": "Execution timeout in seconds (default: 30)",
                "required": False,
            },
        ]

        def call(self, params: Union[str, dict], **kwargs) -> str:
            p = self._verify_json_format_args(params)
            code = p.get("code", "")
            timeout = int(p.get("timeout") or 30)
            session_key = _ps_session_key.get()
            mode = _ps_mode.get()
            if not mode or mode == "off":
                return "[Error: PowerShell tool is not enabled for this session]"
            if not session_key:
                return "[Error: ps_session_key not set — context not initialized]"
            try:
                session = get_or_create_ps_session(session_key, mode)
                output, timed_out = session.execute(code, timeout=timeout)
                if timed_out:
                    return (
                        f"[Timeout after {timeout}s]\n{output}" if output
                        else f"[Timeout after {timeout}s]"
                    )
                return output if output else "(no output)"
            except Exception as exc:
                return f"[Error: {exc}]"

    # Raw API tool-calling path sends BaseTool.function.parameters directly.
    # Convert our legacy list-format parameter declarations to strict JSON schema
    # objects so Ollama /v1 accepts `tools[].function.parameters`.
    for _tool_cls in (
        BraveWebSearchTool,
        ReadFileTool,
        WriteFileTool,
        ReplaceInFileTool,
        ListDirTool,
        SearchFilesTool,
        GrepSearchTool,
        CreateDirectoryTool,
        GmlDocsSearchTool,
        PsDocsSearchTool,
        PowerShellTool,
    ):
        if isinstance(_tool_cls.parameters, list):
            _tool_cls.parameters = qwen_params_to_json_schema(_tool_cls.parameters)

    # ── Instantiate for schema generation ─────────────────────────────────

    _WEB_SEARCH_TOOL = BraveWebSearchTool()
    _FILE_TOOLS = [
        ReadFileTool(),
        WriteFileTool(),
        ReplaceInFileTool(),
        ListDirTool(),
        SearchFilesTool(),
        GrepSearchTool(),
        CreateDirectoryTool(),
    ]
    _GML_DOCS_TOOL = GmlDocsSearchTool()
    _PS_DOCS_TOOL = PsDocsSearchTool()
    _PS_TOOL = PowerShellTool()

    def get_web_search_schema() -> dict:
        return tool_to_ollama_schema(_WEB_SEARCH_TOOL)

    def get_file_tool_schemas() -> list[dict]:
        return [tool_to_ollama_schema(t) for t in _FILE_TOOLS]

    def get_gml_docs_search_schema() -> dict:
        return tool_to_ollama_schema(_GML_DOCS_TOOL)

    def get_ps_docs_search_schema() -> dict:
        return tool_to_ollama_schema(_PS_DOCS_TOOL)

else:
    # Graceful fallback stubs when qwen-agent is not importable

    def set_request_context(workspace_root: str = "", brave_api_key: str = "", ps_session_key: str = "", ps_mode: str = "off") -> None:  # type: ignore[misc]
        pass

    def get_web_search_schema() -> dict:  # type: ignore[misc]
        return {
            "type": "function",
            "function": {
                "name": "web_search",
                "description": "Search the web for current information.",
                "parameters": {
                    "type": "object",
                    "properties": {"query": {"type": "string", "description": "Search query"}},
                    "required": ["query"],
                },
            },
        }

    def get_file_tool_schemas() -> list[dict]:  # type: ignore[misc]
        return []

    def get_gml_docs_search_schema() -> dict:  # type: ignore[misc]
        return {
            "type": "function",
            "function": {
                "name": "gml_docs_search",
                "description": "Search GML documentation.",
                "parameters": {
                    "type": "object",
                    "properties": {"query": {"type": "string", "description": "Search query"}},
                    "required": ["query"],
                },
            },
        }

    def get_ps_docs_search_schema() -> dict:  # type: ignore[misc]
        return {
            "type": "function",
            "function": {
                "name": "ps_docs_search",
                "description": "Search PowerShell documentation.",
                "parameters": {
                    "type": "object",
                    "properties": {"query": {"type": "string", "description": "Search query"}},
                    "required": ["query"],
                },
            },
        }

    def get_run_powershell_schema() -> dict:  # type: ignore[misc]
        return {
            "type": "function",
            "function": {
                "name": "run_powershell",
                "description": "Execute PowerShell code in a persistent stateful session.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "code": {"type": "string", "description": "The PowerShell code to execute"},
                        "timeout": {"type": "integer", "description": "Execution timeout in seconds (default: 30)"},
                    },
                    "required": ["code"],
                },
            },
        }

# ---------------------------------------------------------------------------
# PowerShell session management — stateful per-conversation PS sessions
# ---------------------------------------------------------------------------

_ps_sessions: dict[str, "PSSession"] = {}
_ps_sessions_lock = threading.Lock()


class PSSession:
    """Persistent PowerShell session backed by a subprocess pipe.

    Runs either natively (``pwsh`` / ``powershell.exe``) or inside
    ``mcr.microsoft.com/powershell:latest`` depending on *mode*.

    Each ``execute()`` call base64-encodes the script and dot-sources it so
    that multi-line code works without triggering ``>>`` continuation prompts
    and variables/functions persist across calls within the same conversation.

    Thread-safe: a ``threading.Lock`` serialises concurrent ``execute()`` calls.
    A background reader thread drains stdout into a ``queue.Queue``.
    """

    _SENTINEL = "___PS_DONE_0xDEADBEEF___"

    def __init__(self, mode: str) -> None:
        self.mode = mode
        self._lock = threading.Lock()
        self._proc: subprocess.Popen | None = None
        self._q: queue.Queue = queue.Queue()
        self._start()

    def _reader(self) -> None:
        """Background thread: drain subprocess stdout into the queue."""
        try:
            assert self._proc and self._proc.stdout
            for line in self._proc.stdout:
                self._q.put(line.rstrip("\n\r"))
        except Exception:
            pass
        finally:
            self._q.put(None)  # signals stream end to execute()

    def _start(self) -> None:
        if self.mode == "docker":
            cmd = [
                "docker", "run", "--rm", "-i",
                "mcr.microsoft.com/powershell:latest",
                "pwsh", "-NonInteractive", "-NoProfile", "-Command", "-",
            ]
        else:
            exe = shutil.which("pwsh") or shutil.which("powershell")
            if not exe:
                raise RuntimeError(
                    "PowerShell executable (pwsh / powershell.exe) not found in PATH"
                )
            cmd = [exe, "-NonInteractive", "-NoProfile", "-Command", "-"]

        # Drain any stale items left from a previous session on the same queue
        while not self._q.empty():
            try:
                self._q.get_nowait()
            except queue.Empty:
                break

        self._proc = subprocess.Popen(
            cmd,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            bufsize=0,
        )
        t = threading.Thread(
            target=self._reader,
            daemon=True,
            name=f"ps-reader-{id(self)}",
        )
        t.start()

    def is_alive(self) -> bool:
        return self._proc is not None and self._proc.poll() is None

    def execute(self, code: str, timeout: int = 30) -> tuple[str, bool]:
        """Execute *code* and return ``(stdout_text, timed_out)``.

        The script is base64-encoded and dot-sourced so that multi-line code
        works without ``>>`` continuation prompts and variables persist.
        A sentinel line written after the script marks end-of-output.
        """
        import time as _time

        with self._lock:
            if not self.is_alive():
                self._start()

            b64 = base64.b64encode(code.encode("utf-8")).decode("ascii")
            invocation = (
                f"try {{ . ([ScriptBlock]::Create("
                f"[System.Text.Encoding]::UTF8.GetString("
                f"[System.Convert]::FromBase64String('{b64}')))) }}"
                f" catch {{ Write-Error $_.Exception.Message }}"
            )
            sentinel_cmd = f"Write-Output '{self._SENTINEL}'"

            try:
                assert self._proc and self._proc.stdin
                self._proc.stdin.write(invocation + "\n")
                self._proc.stdin.write(sentinel_cmd + "\n")
                self._proc.stdin.flush()
            except OSError:
                # Process died; restart and retry once
                self._start()
                assert self._proc and self._proc.stdin
                self._proc.stdin.write(invocation + "\n")
                self._proc.stdin.write(sentinel_cmd + "\n")
                self._proc.stdin.flush()

            lines: list[str] = []
            deadline = _time.monotonic() + timeout
            timed_out = False

            while True:
                remaining = deadline - _time.monotonic()
                if remaining <= 0:
                    timed_out = True
                    break
                try:
                    line = self._q.get(timeout=min(remaining, 1.0))
                except queue.Empty:
                    if deadline - _time.monotonic() <= 0:
                        timed_out = True
                        break
                    continue
                if line is None:
                    # Process exited unexpectedly
                    break
                if line == self._SENTINEL:
                    break
                lines.append(line)

            return "\n".join(lines), timed_out

    def close(self) -> None:
        proc = self._proc
        self._proc = None
        if proc is None:
            return
        try:
            proc.stdin.close()
        except Exception:
            pass
        try:
            proc.terminate()
            proc.wait(timeout=3)
        except Exception:
            try:
                proc.kill()
            except Exception:
                pass


def get_or_create_ps_session(session_key: str, mode: str) -> PSSession:
    """Return an existing live session or start a fresh one."""
    with _ps_sessions_lock:
        sess = _ps_sessions.get(session_key)
        if sess is not None:
            if sess.is_alive() and sess.mode == mode:
                return sess
            # Stale or mode changed — close and replace
            try:
                sess.close()
            except Exception:
                pass
        sess = PSSession(mode)
        _ps_sessions[session_key] = sess
        return sess


def release_ps_session(session_key: str) -> None:
    """Close and remove a session.  Call on conversation deletion."""
    with _ps_sessions_lock:
        sess = _ps_sessions.pop(session_key, None)
    if sess is not None:
        try:
            sess.close()
        except Exception:
            log.debug("PS session close error for key=%s", session_key)


def is_ps_available(mode: str) -> bool:
    """Return True when PowerShell is usable in the given *mode*."""
    if not mode or mode == "off":
        return False
    if mode == "docker":
        try:
            result = subprocess.run(
                ["docker", "info"],
                capture_output=True,
                timeout=5,
            )
            return result.returncode == 0
        except Exception:
            return False
    # native
    return bool(shutil.which("pwsh") or shutil.which("powershell"))


# ---------------------------------------------------------------------------
# Code interpreter wrapper
# ---------------------------------------------------------------------------

class CodeInterpreterWrapper:
    """
    Thin wrapper around Qwen-Agent's Docker-based CodeInterpreter tool.

    Lazy-initialised: the Docker image is not pulled/built until first use.
    Only available when qwen-agent[code_interpreter] is installed and Docker
    is running.
    """

    def __init__(self):
        self._tool = None
        self._available: bool | None = None  # None = not yet checked
        self._fallback_dockerfile = Path(__file__).parent / "resources" / "code_interpreter_image.dockerfile"

    def is_available(self) -> bool:
        if self._available is None:
            self._available = self._check_availability()
        return self._available

    def _check_availability(self) -> bool:
        if not QWEN_AGENT_AVAILABLE:
            return False
        try:
            import subprocess
            result = subprocess.run(
                ["docker", "info"],
                capture_output=True,
                timeout=5,
            )
            return result.returncode == 0
        except Exception:
            return False

    def get_tool(self):
        if self._tool is None:
            import qwen_agent.tools.code_interpreter as ci  # noqa: PLC0415
            dockerfile_path = Path(getattr(ci, "DOCKER_IMAGE_FILE", "") or "")
            if not dockerfile_path.exists():
                if self._fallback_dockerfile.exists():
                    ci.DOCKER_IMAGE_FILE = str(self._fallback_dockerfile)
                    log.warning(
                        "qwen-agent code interpreter Dockerfile missing at %s; using fallback %s",
                        dockerfile_path,
                        self._fallback_dockerfile,
                    )
                else:
                    raise RuntimeError(
                        "Code interpreter Dockerfile is missing from qwen-agent and fallback Dockerfile "
                        f"was not found at: {self._fallback_dockerfile}"
                    )
            CodeInterpreter = ci.CodeInterpreter
            self._tool = CodeInterpreter()
        return self._tool

    def get_schema(self) -> dict:
        # Hardcode the schema to avoid triggering a Docker availability check
        # (the check happens in CodeInterpreter.__init__)
        return {
            "type": "function",
            "function": {
                "name": "code_interpreter",
                "description": "Python code sandbox. Execute Python code in a Docker container.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "code": {
                            "type": "string",
                            "description": "The Python code to execute.",
                        }
                    },
                    "required": ["code"],
                },
            },
        }

    def call(self, code: str) -> str:
        t = self.get_tool()
        return t.call(json.dumps({"code": code}))


code_interpreter = CodeInterpreterWrapper()


# ---------------------------------------------------------------------------
# MCP Tool Registry
# ---------------------------------------------------------------------------

class MCPToolRegistry:
    """
    Manages connections to external MCP servers and exposes their tools.

    Usage:
        registry = MCPToolRegistry()
        registry.initialize(mcp_config)        # call once at startup
        schemas = registry.get_schemas()       # Ollama-compatible schemas
        result  = registry.call_tool(name, args)
        registry.has_tool(name)
    """

    def __init__(self):
        self._tools: list = []
        self._initialized = False

    def initialize(self, mcp_config: dict) -> None:
        """Initialize MCP tools from a config dict with 'mcpServers' key."""
        if not mcp_config or not mcp_config.get("mcpServers"):
            log.info("MCP: initialize skipped (no configured servers)")
            return
        if not QWEN_AGENT_AVAILABLE:
            log.warning("qwen-agent not available; MCP tools cannot be initialised.")
            return
        try:
            from qwen_agent.tools.mcp_manager import MCPManager
            manager = MCPManager()
            tools = manager.initConfig(mcp_config)
            self._tools = tools or []
            self._initialized = True
            log.info(
                "MCP: initialised %d tool(s) from %d server(s)",
                len(self._tools),
                len(mcp_config["mcpServers"]),
            )
        except Exception as exc:
            log.warning("MCP initialisation failed: %s", exc)

    @property
    def tools(self) -> list:
        return self._tools

    def get_schemas(self) -> list[dict]:
        return [tool_to_ollama_schema(t) for t in self._tools]

    def is_mcp_tool(self, name: str) -> bool:
        return any(t.name == name for t in self._tools)

    def call_tool(self, name: str, args: dict) -> str:
        log.info("MCP: call requested tool=%s args_keys=%s", name, sorted((args or {}).keys()))
        for tool in self._tools:
            if tool.name == name:
                try:
                    result = tool.call(json.dumps(args))
                    preview = str(result).replace("\n", " ")[:240]
                    log.info("MCP: call success tool=%s result_preview=%r", name, preview)
                    return result
                except Exception:
                    log.exception("MCP: call failed tool=%s", name)
                    raise
        log.warning("MCP: call failed; tool not found name=%s available=%s", name, [t.name for t in self._tools])
        raise KeyError(f"MCP tool not found: {name!r}")


# Singleton — shared across all requests
mcp_registry = MCPToolRegistry()
