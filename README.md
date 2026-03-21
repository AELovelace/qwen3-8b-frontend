# Ollama Qwen3 Coder Frontend

A lightweight local chat application with:

- FastAPI backend
- Single-page HTML/CSS/JS frontend
- Ollama chat streaming (SSE)
- SQLite conversation memory with FTS5 retrieval
- Optional Brave web search integration
- Invite-only authentication with admin-managed users

## Features

- Multi-conversation chat UI (create, list, delete)
- Login and invite-token signup
- Centered admin control panel modal with two columns (tooling/model controls on the left, user management on the right)
- Admin persona prompt box for hot-loading the assistant system prompt on the fly
- Per-user conversation isolation
- Streaming assistant responses with separate reasoning/thinking display
- Markdown rendering in responses with syntax highlighting for code blocks
- Optional web-search loop using `<search>...</search>` tags from the model
- Long-term memory retrieval from older conversations when active context is truncated
- Local GameMaker manual retrieval from `/indexed-docs/gml/**/*.md` for GML-specific coding help
- Local PowerShell docs retrieval from `/indexed-docs/ps-docs/**/*.md` for PowerShell-specific guidance
- Auto-start attempt for `ollama serve` when Ollama is configured locally and not running
- Persistent settings for Brave API key in `config.json`

## Tech Stack

- Backend: FastAPI, aiohttp, aiosqlite, Pydantic
- Frontend: Vanilla HTML/CSS/JavaScript
- Database: SQLite + FTS5 virtual table and triggers
- Model runtime: Ollama (`/api/chat`)

## Requirements

- Python 3.10+
- Ollama installed and available in `PATH`
- A pulled Ollama model compatible with chat
- Optional: Brave Search API key for live web search

Python dependencies are listed in `requirements.txt`.

## Quick Start

1. Create and activate a virtual environment.
2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Start Ollama (if not already running):

```bash
ollama serve
```

4. Ensure your model is available in Ollama on `MONOLITH-III` (example):

```bash
ollama pull qwen3-coder:30b
```

5. Run the app:

```bash
python server.py
```

6. Open:

- `http://127.0.0.1:8000`

## Remote Ollama Startup Script

Use the helper script to start Ollama on `MONOLITH-III`, ensure `qwen3-coder:30b` is pulled, and verify local connectivity to `100.66.64.45:11434`:

```powershell
.\scripts\start-remote-qwen3-server.ps1
```

With explicit remoting credentials:

```powershell
$cred = Get-Credential
.\scripts\start-remote-qwen3-server.ps1 -Credential $cred
```

If WinRM trust errors occur (`ServerNotTrusted`), add the host/IP to TrustedHosts and retry in one step:

```powershell
.\scripts\start-remote-qwen3-server.ps1 -AddToTrustedHosts
```

If TrustedHosts update fails because WinRM is not configured locally, run an elevated PowerShell and use:

```powershell
.\scripts\start-remote-qwen3-server.ps1 -ConfigureLocalWinRM -AddToTrustedHosts
```

Optional overrides:

```powershell
.\scripts\start-remote-qwen3-server.ps1 -RemoteHost MONOLITH-III -RemoteIp 100.66.64.45 -Model qwen3-coder:30b -Port 11434
```

The script attempts WinRM to `-RemoteHost` first and automatically retries using `-RemoteIp` if the hostname path fails.

### Run Directly On Monolith-III

If you have remote desktop/session access to Monolith-III, run the local helper script on that machine (no WinRM needed):

```powershell
.\scripts\start-local-qwen3-server.ps1
```

By default, this script starts Ollama with bind host `0.0.0.0` on port `11434`.

Optional Tailscale reachability check from Monolith-III itself:

```powershell
.\scripts\start-local-qwen3-server.ps1 -VerifyTailscaleEndpoint -TailscaleIp 100.66.64.45
```

Note: checking `100.66.64.45` from Monolith-III itself can fail on some setups even when remote clients can connect. The script now warns in that case; confirm from a different machine for final validation.

If clients cannot reach Ollama from other machines, run with network bind + firewall rule:

```powershell
.\scripts\start-local-qwen3-server.ps1 -RestartOllama -BindHost 0.0.0.0 -EnsureFirewallRule -VerifyTailscaleEndpoint
```

Keep `qwen3-coder:30b` warm in memory:

```powershell
.\scripts\start-local-qwen3-server.ps1 -KeepAlive -1
```

Notes:
- `-KeepAlive -1` requests indefinite model residency in memory.
- The script sends a warm-up request after `ollama pull` unless `-SkipWarmup` is used.

## Configuration

### Model

- The frontend model input is sent in each chat request as `model`.
- Backend default model (if omitted) is `qwen3-coder:30b`.

### Ollama endpoint

- The backend defaults to the Tailscale Ollama host at `http://100.66.64.45:11434`.
- Override this with the `OLLAMA_BASE_URL` environment variable if the host changes.
- Local `ollama serve` auto-start is only attempted when `OLLAMA_BASE_URL` points to a local address such as `127.0.0.1` or `localhost`.

### Tool-calling mode

- `QWEN_AGENT_USE_RAW_API` controls whether raw OpenAI-style tool-calling is used (`0` by default).
- `QWEN_AGENT_FNCALL_PROMPT_TYPE` controls qwen-agent function-call prompting style (`nous` by default).
- For Ollama builds where the model prints pseudo tool tags instead of executing tools, keep `QWEN_AGENT_USE_RAW_API=0`.
- If your backend and model support native OpenAI `tool_calls` reliably, set `QWEN_AGENT_USE_RAW_API=1`.

### Brave API key

You can configure this in either of two ways:

1. Environment variable (highest priority):

```bash
BRAVE_API_KEY=your_key
```

2. In-app settings panel (saved to `config.json`).

The backend resolves keys in this order:

1. `BRAVE_API_KEY` environment variable
2. `config.json` value

### Authentication

Set these values in `.env` before first run:

```bash
JWT_SECRET=replace-with-a-long-random-secret
ADMIN_USERNAME=admin
ADMIN_PASSWORD=replace-with-a-strong-password
```

Notes:

- On first startup, if no users exist, the backend creates the bootstrap admin from env vars.
- Signup is invite-only. Admins can generate invite tokens from the UI.
- All conversation and message APIs are scoped to the authenticated user.

## API Overview

### UI and conversation management

- `GET /` - serves `index.html`
- `GET /api/conversations` - list conversations
- `POST /api/conversations` - create conversation
- `PATCH /api/conversations/{conv_id}` - rename conversation
- `DELETE /api/conversations/{conv_id}` - delete conversation
- `GET /api/conversations/{conv_id}/messages` - fetch ordered message history

All routes above require a bearer token.

### Authentication and admin

- `POST /api/auth/login` - login with username/password
- `POST /api/auth/signup` - create account with username/password/invite token
- `GET /api/auth/me` - return current authenticated user
- `GET /api/admin/users` - list users (admin only)
- `POST /api/admin/users` - create user (admin only)
- `POST /api/admin/invites` - generate invite token (admin only)
- `PATCH /api/admin/users/{user_id}` - update file-tools access and workspace root (admin only)
- `POST /api/admin/persona` - save admin persona/system prompt (hot-loaded in next chat request)
- `DELETE /api/admin/users/{user_id}` - delete user (admin only)

### Settings

- `GET /api/settings` - key status + masked display
- `POST /api/settings` - save Brave key to `config.json`
- `GET /api/mcp-config` - get current user's MCP server configuration
- `POST /api/mcp-config` - save current user's MCP server configuration
- `GET /api/code-interpreter/status` - return Docker code interpreter availability

### Chat

- `POST /api/chat` - streams Server-Sent Events from model output

Chat request payload:

```json
{
  "conversation_id": "uuid",
  "message": "user message",
  "model": "qwen3-coder:30b",
  "think": true,
  "use_search": true,
  "use_gml_docs": true,
  "use_ps_docs": true,
  "use_file_tools": false,
  "use_code_interpreter": false,
  "use_mcp_tools": true
}
```

When `use_gml_docs` is enabled, the backend scans Markdown files under `indexed-docs/gml/` at startup, chunks them for retrieval, and injects the most relevant local GameMaker manual excerpts into the model prompt for each chat request.

When `use_ps_docs` is enabled, the backend scans Markdown files under `indexed-docs/ps-docs/` at startup, chunks them for retrieval, and injects the most relevant local PowerShell documentation excerpts into the model prompt for each chat request.

SSE event types include:

- `thinking` - reasoning delta
- `content` - response delta
- `tool_call` - tool invocation started
- `tool_result` - tool invocation completed
- `done` - stream finished with metadata
- `error` - runtime or upstream error

## Data Storage

The app creates `memory.db` on startup.

Main tables:

- `users(id, username, role, file_tools_enabled, workspace_root, persona_prompt, mcp_config, ...)`
- `conversations(id, title, created_at)`
- `messages(id, conversation_id, role, content, thinking, token_count, created_at)`
- `messages_fts` (FTS5 virtual table indexing message content)

Triggers keep `messages_fts` in sync for inserts/deletes.

## Notes and Troubleshooting

- If Ollama is down, the backend attempts to auto-start it.
- If auto-start fails, `/api/chat` returns HTTP 503 with guidance.
- Web search requires a valid Brave API key.
- FTS retrieval is used only when active token budget is exceeded.
- `code_interpreter` requires Docker to be running locally.
- MCP servers are stored per user and validated before launch.

## Project Files

- `server.py` - backend app, data layer, Qwen-Agent chat streaming, MCP + RAG orchestration
- `index.html` - UI and browser-side app logic
- `agent_tools.py` - Qwen-Agent BaseTool registrations, MCP helpers, Docker code interpreter wrapper
- `convert_manual_html_to_md.py` - converts manual HTML pages to Markdown
- `requirements.txt` - Python dependencies
- `memory.db` - runtime SQLite data (generated)
- `config.json` - optional runtime settings (generated)

## Convert GameMaker Manual To Markdown

Use this script to convert all `.htm` and `.html` files under `indexed-docs/gml/Manual` to `.md` files for AI ingestion:

```bash
python convert_manual_html_to_md.py --input-dir indexed-docs/gml/Manual --output-dir indexed-docs/gml/Manual_md --overwrite
```

For cleaner RAG/embedding text that strips images and common nav/footer boilerplate:

```bash
python convert_manual_html_to_md.py --input-dir indexed-docs/gml/Manual --output-dir indexed-docs/gml/Manual_md_ai --overwrite --ai-clean
```

Notes:

- The converter mirrors the folder structure in the output directory.
- Local links ending in `.htm`/`.html` are rewritten to `.md`.
- Raw HTML tags are removed in the generated Markdown output.
- `--ai-clean` is equivalent to `--strip-images --strip-boilerplate`.
