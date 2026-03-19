# Ollama Qwen3 Frontend

A lightweight local chat application with:

- FastAPI backend
- Single-page HTML/CSS/JS frontend
- Ollama chat streaming (SSE)
- SQLite conversation memory with FTS5 retrieval
- Optional Brave web search integration

## Features

- Multi-conversation chat UI (create, list, delete)
- Streaming assistant responses with separate reasoning/thinking display
- Optional web-search loop using `<search>...</search>` tags from the model
- Long-term memory retrieval from older conversations when active context is truncated
- Auto-start attempt for `ollama serve` when Ollama is not running
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

4. Ensure your model is available in Ollama (example):

```bash
ollama pull huihui_ai/qwen3-abliterated:8b
```

5. Run the app:

```bash
python server.py
```

6. Open:

- `http://127.0.0.1:8000`

## Configuration

### Model

- The frontend model input is sent in each chat request as `model`.
- Backend default model (if omitted) is `huihui_ai/qwen3-abliterated:8b`.

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

## API Overview

### UI and conversation management

- `GET /` - serves `index.html`
- `GET /api/conversations` - list conversations
- `POST /api/conversations` - create conversation
- `PATCH /api/conversations/{conv_id}` - rename conversation
- `DELETE /api/conversations/{conv_id}` - delete conversation
- `GET /api/conversations/{conv_id}/messages` - fetch ordered message history

### Settings

- `GET /api/settings` - key status + masked display
- `POST /api/settings` - save Brave key to `config.json`

### Chat

- `POST /api/chat` - streams Server-Sent Events from model output

Chat request payload:

```json
{
  "conversation_id": "uuid",
  "message": "user message",
  "model": "huihui_ai/qwen3-abliterated:8b",
  "think": true,
  "use_search": true
}
```

SSE event types include:

- `thinking` - reasoning delta
- `content` - response delta
- `search_start` - web search started (or skipped)
- `search_done` - search completed
- `done` - stream finished with metadata
- `error` - runtime or upstream error

## Data Storage

The app creates `memory.db` on startup.

Main tables:

- `conversations(id, title, created_at)`
- `messages(id, conversation_id, role, content, thinking, token_count, created_at)`
- `messages_fts` (FTS5 virtual table indexing message content)

Triggers keep `messages_fts` in sync for inserts/deletes.

## Notes and Troubleshooting

- If Ollama is down, the backend attempts to auto-start it.
- If auto-start fails, `/api/chat` returns HTTP 503 with guidance.
- Web search requires a valid Brave API key.
- FTS retrieval is used only when active token budget is exceeded.

## Project Files

- `server.py` - backend app, data layer, chat streaming, search loop
- `index.html` - UI and browser-side app logic
- `requirements.txt` - Python dependencies
- `memory.db` - runtime SQLite data (generated)
- `config.json` - optional runtime settings (generated)
