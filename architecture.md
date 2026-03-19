# Architecture

## Overview

This project is a local-first chat application with a thin frontend and a FastAPI backend.

- Frontend renders conversation UI and consumes streaming SSE events.
- Backend orchestrates model calls, memory retrieval, optional web search, and persistence.
- Authentication layer secures API access with bearer tokens and role checks.
- Ollama provides model inference.
- SQLite stores conversations/messages and provides FTS5 retrieval.

## High-Level Components

1. Browser client (`index.html`)
2. FastAPI application (`server.py`)
3. Ollama HTTP API (`/api/chat`, `/api/tags`)
4. SQLite database (`memory.db`)
5. Optional Brave Search API
6. Invite-only account onboarding and admin user management

## Backend Module Responsibilities

### Startup and health

- Loads `.env` from project directory.
- Ensures Ollama is reachable.
- Attempts auto-start of `ollama serve` when unavailable.
- Initializes SQLite schema and triggers.

### Conversation APIs

- CRUD operations for conversations.
- Message history retrieval by conversation, ordered ascending.
- User ownership checks for all conversation operations.

### Auth and admin APIs

- JWT-based auth with username/password login.
- Invite-token signup flow for restricted access.
- Bootstrap admin created from environment variables when users table is empty.
- Admin-only user management (list, create, delete, invite generation).

### Settings APIs

- Reads/writes Brave API key status.
- Priority order: environment variable, then `config.json`.

### Chat orchestration (`POST /api/chat`)

- Validates conversation existence.
- Builds active context with token budgeting.
- Optionally injects FTS snippets when history is truncated.
- Executes streaming calls to Ollama.
- Detects `<search>query</search>` tags in model output.
- Calls Brave API for search results and feeds them back into follow-up model turns.
- Streams event deltas to frontend over SSE.
- Persists final user/assistant turn including thinking text.

## Data Model

### `conversations`

- `id` (TEXT, PK, UUID)
- `user_id` (TEXT, owner)
- `title` (TEXT)
- `created_at` (TEXT, ISO timestamp)

### `users`

- `id` (TEXT, PK, UUID)
- `username` (TEXT, unique)
- `password_hash` (TEXT)
- `role` (`user` or `admin`)
- `is_active` (INTEGER)
- `created_at` (TEXT, ISO timestamp)

### `invite_tokens`

- `id` (TEXT, PK, UUID)
- `token` (TEXT, unique)
- `created_by` (TEXT user id)
- `expires_at` (TEXT, nullable)
- `used_by` (TEXT, nullable)
- `used_at` (TEXT, nullable)
- `created_at` (TEXT, ISO timestamp)

### `messages`

- `id` (INTEGER, PK)
- `conversation_id` (TEXT FK)
- `role` (`user` or `assistant`)
- `content` (TEXT)
- `thinking` (TEXT)
- `token_count` (INTEGER)
- `created_at` (TEXT, ISO timestamp)

### `messages_fts` (FTS5)

- Indexes `content` for retrieval.
- Includes `message_id` and `conversation_id` as unindexed metadata.
- Trigger-driven sync on insert/delete of `messages`.

## Context and Memory Strategy

1. Estimate tokens as `len(text) / 4`.
2. Build active context from newest messages backwards until token budget is full.
3. Reverse included set to chronological order for model input.
4. If truncated, run FTS query against older conversations (excluding current conversation).
5. Inject snippets as a system message before current conversation history.

## Search Loop Strategy

- Search capability is advertised in a system prompt.
- Model can request search using exact `<search>...</search>` tags.
- Backend runs up to 3 search iterations.
- For each query, backend emits `search_start` and `search_done` events.
- Search results are re-injected as a user message asking for final answer.
- If no tags are requested, backend emits direct answer and ends loop.

## Streaming Protocol (SSE)

The backend sends newline-delimited SSE `data:` JSON payloads:

- `thinking`: incremental reasoning text
- `content`: incremental assistant answer text
- `search_start`: query started or skipped
- `search_done`: query complete + result count
- `done`: final metadata (`token_count`, `fts_used`, `searches_done`)
- `error`: runtime/upstream failure message

The frontend keeps one assistant message shell open and updates it incrementally.

## Request Flow

1. User enters a message in browser.
2. Frontend ensures session by validating token (`/api/auth/me`).
3. Frontend ensures conversation exists under current user.
4. Frontend POSTs to `/api/chat` with bearer token.
5. Backend authorizes conversation ownership, assembles context, and calls Ollama.
6. Backend relays SSE deltas to browser.
7. Optional search loop runs if model emits search tags.
8. Backend saves user + assistant messages to SQLite.
9. Frontend updates badges (FTS used, search count) and refreshes conversation list.

## Reliability and Failure Handling

- Ollama connection failure returns SSE `error` or HTTP 503.
- Brave API failures are logged and represented as empty/skipped results.
- Database operations are committed per request and closed in `finally` paths.
- Streaming errors do not prevent best-effort persistence of partial final output.

## Security and Trust Boundaries

- App is intended for local use (`localhost` Ollama and local DB/files).
- API access requires bearer token authentication.
- Signup is invite-only to support limited sharing.
- Role-based authorization gates admin management endpoints.
- Conversations and messages are isolated by owner (`user_id`).
- Brave key is stored in plaintext `config.json` if set through UI.
- Inputs are user-provided text and model-generated content; UI renders as plain text to avoid HTML injection.

## Scalability Notes

- Single-process FastAPI deployment by default.
- SQLite with WAL supports moderate local concurrency.
- Token estimation is heuristic, not tokenizer-accurate.
- Search loop and streaming are sequential per request.

## Key Runtime Artifacts

- `memory.db` (SQLite)
- `config.json` (settings, optional)
- `.env` (optional environment config)
