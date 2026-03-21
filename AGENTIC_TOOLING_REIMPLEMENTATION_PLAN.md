# Qwen3-Coder Agentic Tooling Reimplementation Plan

**Status**: In Progress (Partially Implemented; updated with current-state audit)  
**Date**: March 21, 2026  
**Root Cause (Current Understanding)**: Remaining reliability issues are primarily stream contract consistency and observability gaps, not missing qwen3-coder base configuration.

---

## Executive Summary

The original diagnosis correctly identified several possible failure points, but the codebase has already implemented many core fixes. Current findings:

- **LLM tool config is present**: `use_raw_api` + `fncall_prompt_type` are already wired in `server.py`.
- **OpenAI-compatible endpoint is present**: backend uses `OLLAMA_OPENAI_URL = .../v1`.
- **Tool schema conversion + JSON validation is present** in `agent_tools.py` (`qwen_params_to_json_schema`).
- **MCP fail-open retry is present** (retry once without MCP when initialization/EOF fails).
- **Recently fixed (Mar 21)**: backend now emits `tool_call`/`tool_result` SSE events, emits `searches_done` in `done`, and classifies stream errors with `error_type`.

### What's Needed
1. Keep dependency/runtime compatibility stable (qwen-agent + Ollama versions)
2. Add/automate diagnostics to verify tool event flow end-to-end after upgrades
3. Strengthen observability (structured counters + failure categories)
4. Convert remaining "proposal" items in this doc into verified test cases

---

## Current Implementation Snapshot (Audit: March 21, 2026)

### Already Implemented

- `server.py` includes admin/environment-controlled tool mode selection (`use_raw_api`, `fncall_prompt_type`).
- `server.py` builds mixed tool lists (native + MCP config dict) with feature gating and per-user permissions.
- `server.py` tracks function/tool messages in stream and aggregates usage counters (`tools_called`, `file_reads`, `file_writes`, etc.).
- `agent_tools.py` registers native tools via `BaseTool`, converts list-style params to strict JSON schema, and validates serializability.
- `agent_tools.py` overrides built-in `web_search` with Brave-backed implementation and supports per-request context via `ContextVar`.

### Implemented in This Iteration

- SSE now emits `tool_call` with name/args when assistant `tool_calls` (or legacy `function_call`) appear.
- SSE now emits `tool_result` when function/tool role results are appended.
- `done` event now includes `searches_done` to match frontend expectations.
- `error` event now includes `error_type` classification (`tool_error`, `mcp_error`, `connection_error`, `unknown_error`).

### Known Follow-ups

- Add a lightweight integration test that validates SSE event contract (`content`, `thinking`, `tool_call`, `tool_result`, `done`, `error`).
- Optionally pin an upper/lower `qwen-agent` range once validated in your deployment environment.
- Add a startup/runtime self-check endpoint for tool availability diagnostics.

---

## Phase 1: Diagnosis & Validation (Prerequisite)

### Step 1.1: Check qwen-agent Version
**File**: `requirements.txt`

Current spec:
```
qwen-agent[rag,code_interpreter,mcp]
```

**Issue**: No version pinned. May be using incompatible version.

**Action Required**:
- Verify installed version: `pip show qwen-agent | grep Version`
- **Required**: qwen-agent ≥ 0.0.26 (released May 29, 2025 with qwen3-coder support)
- Update requirements.txt to pin version: `qwen-agent[rag,code_interpreter,mcp]==0.0.28+` (latest stable)

### Step 1.2: Verify Ollama Endpoint Configuration
**File**: `server.py` (lines 55-62)

Current config:
```python
OLLAMA_BASE_URL   = os.getenv("OLLAMA_BASE_URL", "http://100.66.64.45:11434").rstrip("/")
OLLAMA_URL        = f"{OLLAMA_BASE_URL}/api/chat"
OLLAMA_OPENAI_URL = f"{OLLAMA_BASE_URL}/v1"
```

**Status**: ✅ Correct (using `/v1` OpenAI-compatible endpoint)

### Step 1.3: Test Tool Calling with Direct Ollama API
**Script**: Create a diagnostic test script

Create `test_qwen3_tools.py`:
```python
#!/usr/bin/env python3
"""Diagnostic test for qwen3-coder tool calling via Ollama."""

import json
import requests

OLLAMA_BASE = "http://100.66.64.45:11434"
MODEL = "qwen3-coder:30b"

def test_direct_ollama_tools():
    """Test tool calling directly via Ollama /api/chat endpoint."""
    
    tools = [{
        "type": "function",
        "function": {
            "name": "web_search",
            "description": "Search the web for information",
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {"type": "string", "description": "Search query"}
                },
                "required": ["query"]
            }
        }
    }]
    
    payload = {
        "model": MODEL,
        "messages": [
            {
                "role": "user",
                "content": "Search the web for current Python packages trending in March 2025"
            }
        ],
        "tools": tools,
        "stream": False
    }
    
    print("🔍 Testing Ollama /api/chat with tools...")
    print(f"Payload: {json.dumps(payload, indent=2)}")
    
    try:
        resp = requests.post(f"{OLLAMA_BASE}/api/chat", json=payload, timeout=30)
        print(f"Status: {resp.status_code}")
        print(f"Response: {json.dumps(resp.json(), indent=2)}")
        
        msg = resp.json().get("message", {})
        if "tool_calls" in msg:
            print("✅ Tool calls detected in response!")
            return True
        else:
            print("❌ No tool_calls in response - model may not support tools")
            return False
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def test_qwen_agent():
    """Test qwen3-coder tool calling via qwen-agent."""
    try:
        from qwen_agent.agents import Assistant
        from qwen_agent.llm import get_chat_model
        
        llm_cfg = {
            'model': MODEL,
            'model_server': f"{OLLAMA_BASE}/v1",
            'api_key': 'EMPTY',
            'generate_cfg': {
                'fncall_prompt_type': 'nous',
            }
        }
        
        print("\n🔍 Testing qwen-agent Assistant with web_search...")
        
        agent = Assistant(
            function_list=["web_search"],
            llm=get_chat_model(llm_cfg),
            system_message="You are a helpful assistant with web search ability.",
        )
        
        response_iter = agent.run(
            messages=[
                {
                    "role": "user",
                    "content": "Search for Python packaging trends March 2025"
                }
            ],
            lang="en"
        )
        
        for i, response in enumerate(response_iter):
            print(f"Response {i}: {response}")
            if i > 5:
                print("(truncated)")
                break
        
        print("✅ qwen-agent test completed")
        return True
        
    except Exception as e:
        print(f"❌ qwen-agent test failed: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    print("=" * 60)
    print("QWEN3-CODER TOOL CALLING DIAGNOSTIC TEST")
    print("=" * 60)
    
    direct_ok = test_direct_ollama_tools()
    agent_ok = test_qwen_agent()
    
    print("\n" + "=" * 60)
    print("DIAGNOSTIC SUMMARY")
    print("=" * 60)
    print(f"✅ Direct Ollama API: {'PASS' if direct_ok else 'FAIL'}")
    print(f"✅ qwen-agent Library: {'PASS' if agent_ok else 'FAIL'}")
    
    if direct_ok and not agent_ok:
        print("\n🔴 Issue: Ollama supports tools, but qwen-agent doesn't invoke them")
        print("   → Likely: qwen-agent version too old or configuration incorrect")
    elif not direct_ok:
        print("\n🔴 Issue: Ollama doesn't recognize tool definitions")
        print("   → Likely: qwen3-coder model doesn't support tools, or schema format wrong")
```

**Action**: Run this diagnostic to identify exact failure point

---

## Phase 2: Code Issues & Configuration Changes

### Issue 2.1: Missing Tool-Parsing Configuration

**File**: `server.py` (line 2350-2362)

**Current Code**:
```python
llm_cfg = {
    "model": requested_model,
    "model_server": OLLAMA_OPENAI_URL,
    "api_key": os.getenv("OPENAI_API_KEY", "EMPTY"),
    "generate_cfg": generate_cfg,
}
```

**Problem**: 
- No explicit tool parsing configuration for qwen3-coder
- Missing `fncall_prompt_type` which controls how tools are formatted
- No explicit control over whether to use raw API or qwen-agent's internal parsing

**Fix**:
```python
llm_cfg = {
    "model": requested_model,
    "model_server": OLLAMA_OPENAI_URL,
    "api_key": os.getenv("OPENAI_API_KEY", "EMPTY"),
    "generate_cfg": {
        **(generate_cfg or {}),
        # Explicit tool parsing configuration for qwen3-coder
        "fncall_prompt_type": "nous",  # Qwen3 coder uses Nous template
        "use_raw_api": True,  # Prefer OpenAI-style native tool_calls path
    },
}
```

### Issue 2.2: Tool Schema Validation

**File**: `agent_tools.py` (lines 41-62)

**Current Code**: `qwen_params_to_json_schema()` function doesn't validate output

**Problem**:
- Invalid JSON schemas silently fail
- No error messages when conversion fails
- Ollama might reject malformed tool definitions

**Fix**: Add validation and error reporting:
```python
def qwen_params_to_json_schema(parameters) -> dict:
    """..."""
    # ... existing code ...
    schema: dict = {"type": "object", "properties": props}
    if required:
        schema["required"] = required
    
    # VALIDATE: Ensure this is valid JSON and proper schema
    try:
        json.dumps(schema)  # Validate JSON serializability
        # Validate against OpenAI schema requirements
        if not isinstance(schema.get("properties"), dict):
            raise ValueError("properties must be a dict")
    except (TypeError, ValueError) as e:
        log.error(f"Invalid tool schema for tool: {e}")
        raise
    
    return schema
```

### Issue 2.3: Response Parsing for Tool Calls

**File**: `server.py` (lines 2418-2472)

**Current Code**: Looks for messages with `role in ("function", "tool")`

**Problem**:
- qwen3-coder's Assistant.run() may use
 different message format
- Tool invocation result handling may be incompatible
- No explicit handling for `tool_calls` array in assistant messages

**Fix**: Update response parsing with better tool message detection:

```python
# Enhanced tool message detection
function_msgs = [
    m for m in rsp
    if isinstance(m, dict) and m.get("role") in ("function", "tool")
]

# Also check for tool_calls in assistant messages
for msg in rsp:
    if isinstance(msg, dict) and msg.get("role") == "assistant":
        if tool_calls := msg.get("tool_calls"):
            log.debug(f"Assistant generated {len(tool_calls)} tool calls")
            # These will be handled by qwen-agent's agent.run() loop
```

### Issue 2.4: Error Reporting for Tool Failures

**File**: `server.py` (line 2500-2510)

**Current Code**:
```python
except Exception as exc:
    log.exception("Streaming error")
    yield f"data: {json.dumps({'type': 'error', 'message': str(exc)})}\n\n"
```

**Problem**:
- Generic error message
- No differentiation between tool errors vs. model errors
- Users don't know why tools stopped working

**Fix**: Better error classification:
```python
except Exception as exc:
    error_msg = str(exc)
    error_type = "unknown_error"
    
    if "tool" in error_msg.lower() or "function" in error_msg.lower():
        error_type = "tool_error"
    elif "assistant" in error_msg.lower():
        error_type = "agent_error"
    elif "ollama" in error_msg.lower() or "connection" in error_msg.lower():
        error_type = "connection_error"
    
    log.exception(f"Streaming error [{error_type}]")
    yield f"data: {json.dumps({
        'type': 'error',
        'error_type': error_type,
        'message': error_msg
    })}\n\n"
```

---

## Phase 3: Implementation Steps

### Step 3.1: Update Dependencies
```bash
# Update qwen-agent to minimum version supporting qwen3-coder
pip install --upgrade "qwen-agent[rag,code_interpreter,mcp]>=0.0.26"
```

Update `requirements.txt`:
```
qwen-agent[rag,code_interpreter,mcp]>=0.0.26
```

### Step 3.2: Update Configuration in server.py
- Add explicit `fncall_prompt_type` and `use_raw_api` to LLM config
- Ensure OLLAMA_OPENAI_URL points to `/v1` endpoint (already correct)

### Step 3.3: Enhance agent_tools.py
- Add schema validation in `qwen_params_to_json_schema()`
- Add logging for tool registration
- Validate tool name conflicts

### Step 3.4: Improve Error Handling in server.py
- Add detailed error classification
- Log tool invocation requests/responses
- Add timeout handling for tool execution

### Step 3.5: Add Diagnostic Logging
- Log Assistant initialization parameters
- Log function_list passed to Assistant
- Log tool invocation requests from model
- Log tool execution results

---

## Phase 4: Validation & Testing

### Test 4.1: Unit Test Tool Registration
```python
# Test that all tools register correctly
from agent_tools import (
    _FILE_TOOLS, _WEB_SEARCH_TOOL, _GML_DOCS_TOOL, _PS_DOCS_TOOL,
    get_file_tool_schemas, get_web_search_schema
)

def test_tool_schemas():
    """Validate all tool schemas are valid JSON and proper format."""
    all_tools = [_WEB_SEARCH_TOOL, _GML_DOCS_TOOL, _PS_DOCS_TOOL] + _FILE_TOOLS
    
    for tool in all_tools:
        schema = tool_to_ollama_schema(tool)
        assert schema["type"] == "function"
        assert "function" in schema
        func = schema["function"]
        assert "name" in func
        assert "description" in func
        assert "parameters" in func
        
        # Validate can be JSON serialized
        json_str = json.dumps(schema)
        assert len(json_str) > 0
        
        print(f"✅ {func['name']} schema valid")
```

### Test 4.2: Integration Test Tool Calling
```python
# Test that qwen3-coder can actually invoke tools
# (Use test_qwen3_tools.py diagnostic)
```

### Test 4.3: Chat Interface Test
- Clear conversation history
- Ask model to use a specific tool (e.g., "search the web for...")
- Verify tool is invoked
- Verify tool result is used in response
- Check admin panel metrics show tool was called

---

## Phase 5: Fallback & Graceful Degradation

If tool calling cannot be fixed:

### Option A: Disable Tool Calling (Fallback)
Add environment variable to disable tools:
```python
USE_AGENT_TOOLS = os.getenv("USE_AGENT_TOOLS", "true").lower() == "true"

# In _build_agent_function_list():
if USE_AGENT_TOOLS and req.use_search:
    tools.append("web_search")
# ... etc
```

### Option B: Use Non-Agent Chat Mode
If Assistant completely broken, fall back to simple chat:
```python
# If Assistant fails, use direct Ollama chat without tools
if not QWEN_AGENT_RUNTIME_AVAILABLE or not USE_AGENT_TOOLS:
    # Use aiohttp to call Ollama /api/chat directly
    # Stream responses without tool invocation
```

---

## Timeline & Deliverables

| Phase | Tasks | Effort | Output |
|-------|-------|--------|--------|
| **Phase 1** | Diagnosis + Validation | 2-3 hours | test_qwen3_tools.py + diagnosis report |
| **Phase 2** | Code Analysis + Fixes | 2-3 hours | Code diffs + explanation |
| **Phase 3** | Implementation | 1-2 hours | Updated files + version bump |
| **Phase 4** | Testing & Validation | 1-2 hours | Test results + chat verification |
| **Phase 5** | If needed: Fallback | 1-2 hours | Graceful degradation options |

**Total**: 7-12 hours for complete solution

---

## Risk Assessment

### High Risk Issues
1. ❌ qwen-agent version incompatibility with qwen3-coder → Mitigate: Pin version ≥0.0.26
2. ❌ Ollama model doesn't support tools → Mitigate: Direct API test first
3. ❌ Schema format incompatibility → Mitigate: Validate schemas before sending

### Medium Risk Issues
1. ⚠️ Tool execution takes too long → Mitigate: Add timeout handling
2. ⚠️ Partial MCP compatibility → Mitigate: Fail gracefully, continue without MCP

### Low Risk Issues
1. ℹ️ Error messages unclear → Mitigate: Enhanced logging

---

## Success Criteria

✅ **Tool calling works end-to-end**:
- Model correctly identifies when tools should be used
- Tool schemas are properly formatted and accepted by Ollama
- Tools execute and return results to model
- Model uses tool results in final response

✅ **Configuration is explicit**:
- LLM cfg includes tool parsing settings for qwen3-coder
- Code comments explain qwen3-coder-specific configuration

✅ **Errors are actionable**:
- Error messages indicate whether issue is: model, tools, Ollama, or qwen-agent
- Logs capture tool invocation requests/responses for debugging

✅ **Backward compatibility maintained**:
- Code still works with older Qwen models if qwen-agent supports them
- Fallback mode works if tool calling fails

---

## Next Action

**Recommended immediate next actions**:
1. Run a single end-to-end chat that triggers at least one tool call and confirm frontend indicators update from live SSE events.
2. Add a small automated regression test for the SSE tool-event contract.
3. Re-baseline this document by marking obsolete "missing configuration" items as historical context only.

Then continue with targeted reliability hardening from Phases 3-4 (tests + observability).
