# Streaming and SSE Implementation

Guide to implementing real-time streaming with Pydantic AI agents.

## Overview

Streaming provides real-time responses as the LLM generates text, improving user experience. This pattern implements streaming with:

1. **Text streaming** - Stream response chunks as they're generated
2. **Tool call tracking** - Monitor tool execution in real-time
3. **SSE formatting** - Server-Sent Events for web clients
4. **Proper flushing** - Ensure immediate transmission

## Basic Streaming

### Simple Text Streaming

```python
async def stream_chat(self, prompt: str) -> AsyncIterable[str]:
    """Stream agent responses"""
    agent = self._create_agent()

    async with agent.run_stream(prompt) as result:
        async for chunk in result.stream_text(delta=True):
            if chunk:
                yield chunk
```

**Key Points**:
- `run_stream()` returns async context manager
- `stream_text(delta=True)` yields incremental chunks
- `delta=False` would yield accumulated text

### Accumulating Full Response

```python
async def stream_chat(self, prompt: str) -> AsyncIterable[str]:
    """Stream and save full response"""
    agent = self._create_agent()
    state = await self._load_state()

    async with agent.run_stream(prompt) as result:
        response_parts = []

        async for chunk in result.stream_text(delta=True):
            if chunk:
                response_parts.append(chunk)
                yield chunk

        # Save complete response
        full_response = "".join(response_parts)
        state.add_message("assistant", full_response)
        await state_store.save(state)
```

## Tool Call Tracking

Monitor tool execution during streaming:

```python
async def stream_chat(self, prompt: str) -> AsyncIterable[str]:
    """Stream with tool call tracking"""
    agent = self._create_agent()

    async with agent.run_stream(prompt) as result:
        last_message_count = 0
        response_parts = []

        async for chunk in result.stream_text(delta=True):
            # Check for new messages (tool calls)
            current_messages = result.all_messages()
            if len(current_messages) > last_message_count:
                # Process new messages
                for msg in current_messages[last_message_count:]:
                    if not hasattr(msg, 'parts'):
                        continue

                    for part in msg.parts:
                        part_type = type(part).__name__

                        if part_type == 'ToolCallPart':
                            # Tool execution started
                            yield f"[TOOL_START: {part.tool_name}]"

                        elif part_type == 'ToolReturnPart':
                            # Tool execution completed
                            yield f"[TOOL_END: {part.tool_name}]"

                last_message_count = len(current_messages)

            # Stream text
            if chunk:
                response_parts.append(chunk)
                yield chunk
```

**Message Parts**:
- `ToolCallPart` - Tool invocation with arguments
- `ToolReturnPart` - Tool result
- `TextPart` - Text content

## Server-Sent Events (SSE)

### SSE Message Types

Define structured message types:

```python
from enum import Enum
from typing import Literal
from pydantic import BaseModel

class SSEMessageType(str, Enum):
    STATUS = "status"
    CHUNK = "chunk"
    TOOL_CALL = "tool_call"
    ERROR = "error"

class SSEStatusMessage(BaseModel):
    type: Literal["status"] = "status"
    content: str
    step: str  # "init" | "done"
    conversation_id: str

class SSEChunkMessage(BaseModel):
    type: Literal["chunk"] = "chunk"
    content: str

class SSEToolCallMessage(BaseModel):
    type: Literal["tool_call"] = "tool_call"
    tool: str
    status: str  # "started" | "completed"
    timestamp: str

class SSEErrorMessage(BaseModel):
    type: Literal["error"] = "error"
    content: str
    conversation_id: str
```

### SSE Streaming Implementation

```python
import asyncio

async def stream_chat(self, prompt: str, conversation_id: str) -> AsyncIterable[str]:
    """Stream with SSE messages"""
    state = await self._load_or_create_state(conversation_id)

    # Send init status
    yield SSEStatusMessage(
        content="Initializing agent...",
        step="init",
        conversation_id=state.conversation_id
    ).model_dump_json()

    # Force flush
    await asyncio.sleep(0)

    agent = self._create_agent(state)

    try:
        async with agent.run_stream(prompt) as result:
            last_message_count = 0
            response_parts = []

            async for chunk in result.stream_text(delta=True):
                # Track tool calls
                current_messages = result.all_messages()
                if len(current_messages) > last_message_count:
                    for msg in current_messages[last_message_count:]:
                        if not hasattr(msg, 'parts'):
                            continue

                        for part in msg.parts:
                            if type(part).__name__ == 'ToolCallPart':
                                yield SSEToolCallMessage(
                                    tool=part.tool_name,
                                    status="started",
                                    timestamp=datetime.now().isoformat()
                                ).model_dump_json()
                                await asyncio.sleep(0)

                            elif type(part).__name__ == 'ToolReturnPart':
                                yield SSEToolCallMessage(
                                    tool=part.tool_name,
                                    status="completed",
                                    timestamp=datetime.now().isoformat()
                                ).model_dump_json()
                                await asyncio.sleep(0)

                    last_message_count = len(current_messages)

                # Stream text chunks
                if chunk:
                    response_parts.append(chunk)
                    yield SSEChunkMessage(content=chunk).model_dump_json()
                    await asyncio.sleep(0)

            # Save state
            full_response = "".join(response_parts)
            state.add_message("assistant", full_response)
            await state_store.save(state)

    except Exception as e:
        yield SSEErrorMessage(
            content=str(e),
            conversation_id=state.conversation_id
        ).model_dump_json()

    # Send completion status
    yield SSEStatusMessage(
        content="Complete",
        step="done",
        conversation_id=state.conversation_id
    ).model_dump_json()
```

### SSE Formatting Wrapper

```python
import json

async def wrap_sse_stream(source: AsyncIterable[str]) -> AsyncIterable[str]:
    """
    Wrap JSON messages in SSE format

    Expects chunks to be JSON strings from model_dump_json()
    """
    try:
        async for chunk in source:
            # Chunk is already JSON string
            if isinstance(chunk, str):
                if not chunk.startswith("data: "):
                    message = f"data: {chunk.rstrip()}\n\n"
                else:
                    message = chunk
            else:
                # Fallback for non-string chunks
                data = json.dumps(chunk)
                message = f"data: {data}\n\n"

            yield message
            await asyncio.sleep(0)  # Force flush

        yield "data: [DONE]\n\n"
    except Exception as e:
        yield f"data: {json.dumps({'error': str(e)})}\n\n"
```

## FastAPI Integration

### Basic Streaming Endpoint

```python
from fastapi import FastAPI
from fastapi.responses import StreamingResponse

app = FastAPI()

@app.post("/chat")
async def chat(prompt: str, conversation_id: str | None = None):
    """Chat endpoint with streaming"""
    service = AgentService()

    async def generate():
        async for chunk in service.stream_chat(prompt, conversation_id):
            yield chunk

    return StreamingResponse(
        generate(),
        media_type="text/plain"
    )
```

### SSE Streaming Endpoint

```python
@app.post("/chat")
async def chat(prompt: str, conversation_id: str | None = None):
    """Chat endpoint with SSE streaming"""
    service = AgentService()

    text_stream = service.stream_chat(prompt, conversation_id)
    sse_stream = wrap_sse_stream(text_stream)

    return StreamingResponse(
        sse_stream,
        media_type="text/event-stream",
        headers={
            "Content-Type": "text/event-stream",
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "Transfer-Encoding": "chunked",
            "X-Accel-Buffering": "no",  # Disable nginx buffering
            "X-Content-Type-Options": "nosniff"
        }
    )
```

## Proper Flushing

**Critical**: Use `await asyncio.sleep(0)` to force immediate transmission:

```python
async for chunk in result.stream_text(delta=True):
    if chunk:
        yield SSEChunkMessage(content=chunk).model_dump_json()
        await asyncio.sleep(0)  # Force flush
```

**Why This Works**:
- `asyncio.sleep(0)` yields control to event loop
- Allows buffered data to be transmitted
- Ensures real-time streaming experience

**Without Flushing**:
- Chunks may be buffered
- User sees delayed responses
- Poor streaming experience

## Client-Side Consumption

### JavaScript EventSource

```javascript
const eventSource = new EventSource('/chat?prompt=Hello&conversation_id=123');

eventSource.onmessage = (event) => {
    if (event.data === '[DONE]') {
        eventSource.close();
        return;
    }

    const message = JSON.parse(event.data);

    switch (message.type) {
        case 'status':
            console.log(`Status: ${message.content}`);
            break;
        case 'chunk':
            // Append text chunk to UI
            appendText(message.content);
            break;
        case 'tool_call':
            console.log(`Tool ${message.tool}: ${message.status}`);
            break;
        case 'error':
            console.error(`Error: ${message.content}`);
            break;
    }
};

eventSource.onerror = (error) => {
    console.error('SSE error:', error);
    eventSource.close();
};
```

### Python Client

```python
import httpx

async def consume_stream(prompt: str):
    """Consume SSE stream"""
    async with httpx.AsyncClient() as client:
        async with client.stream(
            "POST",
            "http://localhost:8000/chat",
            params={"prompt": prompt},
            timeout=60.0
        ) as response:
            async for line in response.aiter_lines():
                if line.startswith("data: "):
                    data = line[6:]  # Remove "data: " prefix
                    if data == "[DONE]":
                        break

                    message = json.loads(data)
                    if message["type"] == "chunk":
                        print(message["content"], end="", flush=True)
```

## Usage Limits

Prevent infinite tool loops:

```python
from pydantic_ai.usage import UsageLimits

async with agent.run_stream(
    prompt,
    usage_limits=UsageLimits(request_limit=10)
) as result:
    # Agent will stop after 10 LLM requests
    async for chunk in result.stream_text(delta=True):
        yield chunk
```

## Error Handling

```python
async def stream_chat(self, prompt: str) -> AsyncIterable[str]:
    """Stream with error handling"""
    try:
        async with agent.run_stream(prompt) as result:
            async for chunk in result.stream_text(delta=True):
                yield chunk

    except Exception as e:
        logger.error(f"Stream error: {e}", exc_info=True)

        # Send error message
        yield SSEErrorMessage(
            content=f"Error: {str(e)}",
            conversation_id=conversation_id
        ).model_dump_json()

        # Don't re-raise - stream is already started
```

## Best Practices

1. **Always flush after yielding** - Use `await asyncio.sleep(0)`
2. **Track tool calls** - Monitor `result.all_messages()`
3. **Accumulate full response** - Save complete text for history
4. **Handle errors gracefully** - Send error messages via stream
5. **Set usage limits** - Prevent infinite loops
6. **Use structured messages** - SSE with typed messages
7. **Proper headers** - Disable buffering for SSE
8. **Close streams properly** - Send `[DONE]` marker
