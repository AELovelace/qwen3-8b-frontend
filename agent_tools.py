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

import json
import logging
import os
from contextvars import ContextVar
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


def set_request_context(workspace_root: str = "", brave_api_key: str = "") -> None:
    """Set per-request ContextVar values so BaseTool.call() can access
    user-specific configuration without explicit argument threading.

    Call once at the top of event_stream() in server.py.  ContextVar values are
    isolated per asyncio Task — concurrent requests do not interfere.
    They also propagate to threads spawned by asyncio.to_thread().
    """
    _workspace_root.set(workspace_root)
    _brave_api_key.set(brave_api_key)


# ---------------------------------------------------------------------------
# Native tool registrations — call() delegates to server.py ft_* functions
# ---------------------------------------------------------------------------

if QWEN_AGENT_AVAILABLE:
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
                return "[Error: workspace_root not configured for this session]"
            try:
                return ft_list_dir(ws, p.get("path", ""))
            except FileToolError as exc:
                return f"[Error: {exc}]"
            except PermissionError as exc:
                return f"[Permission denied: {exc}]"
            except Exception as exc:
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

    def set_request_context(workspace_root: str = "", brave_api_key: str = "") -> None:  # type: ignore[misc]
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
            from qwen_agent.tools.code_interpreter import CodeInterpreter
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
        for tool in self._tools:
            if tool.name == name:
                return tool.call(json.dumps(args))
        raise KeyError(f"MCP tool not found: {name!r}")


# Singleton — shared across all requests
mcp_registry = MCPToolRegistry()
