# Architecture Reference

Complete architectural patterns for Pydantic AI agents with layered architecture.

## Table of Contents

1. [Layered Architecture](#layered-architecture)
2. [Component Responsibilities](#component-responsibilities)
3. [Data Flow](#data-flow)
4. [Design Patterns](#design-patterns)
5. [Extension Points](#extension-points)

## Layered Architecture

```
┌─────────────────────────────────────┐
│   Presentation Layer (Router/CLI)   │  ← Entry points
├─────────────────────────────────────┤
│      Service Layer (Service)        │  ← Business logic
├─────────────────────────────────────┤
│   Agent Layer (Factory + Agent)     │  ← Agent creation
├─────────────────────────────────────┤
│   Tool Layer (Registry + Tools)     │  ← Tool management
├─────────────────────────────────────┤
│   State Layer (State + Store)       │  ← Persistence
└─────────────────────────────────────┘
```

### Layer Responsibilities

**Presentation Layer**: User input/output, HTTP/CLI interfaces, response formatting

**Service Layer**: Orchestrates agent lifecycle, manages dependencies, error handling

**Agent Layer**: Creates configured agents, builds system prompts, filters tools

**Tool Layer**: Registers tools, injects dependencies, tracks metadata

**State Layer**: Manages conversation history, persists state, handles cleanup

## Component Responsibilities

### AgentFactory

**Purpose**: Create configured agents using the Factory pattern

**Key Methods**:
```python
create_agent(agent_type, model, tools, state) -> Agent
register_config(config: AgentConfig)
_build_system_prompt(config, state) -> str
_filter_tools(tools, allowed_names) -> List
```

**Responsibilities**:
- Store agent configurations (system prompts, tool filters, settings)
- Build system prompts with context injection
- Filter tools based on agent type
- Create Agent instances

### AgentService

**Purpose**: Orchestrate agent operations

**Key Methods**:
```python
chat(prompt, conversation_id) -> str
stream_chat(prompt, conversation_id) -> AsyncIterable[str]
_create_model() -> Model
_create_tools() -> ToolCollection
```

**Responsibilities**:
- Create and configure models
- Initialize tool collections
- Load/create conversation state
- Execute agent runs
- Persist state after completion

### ToolRegistry

**Purpose**: Centralized tool registration

**Key Methods**:
```python
register(name, category, description) -> decorator
get_all_tools() -> List[Callable]
get_tools_by_category(category) -> List[Callable]
```

**Responsibilities**:
- Register tools with metadata
- Store tool configurations
- Provide tool discovery
- Validate dependencies

### ToolCollection

**Purpose**: Manage tools with dependency injection

**Key Methods**:
```python
get_all_tools() -> List[Callable]
_bind_service(tool_func, service) -> Callable
_needs_service(tool_func, service_type) -> bool
```

**Responsibilities**:
- Detect service dependencies via signature inspection
- Bind service instances to tool functions
- Remove service parameters from signatures
- Provide bound tools to agents

## Data Flow

### Non-Streaming Chat

```
User Request
    ↓
Service.chat(prompt, conversation_id)
    ↓
├─ Load/Create AgentState
├─ Add user message to state
├─ Create Model (via ModelProvider)
├─ Create Tools (ToolCollection with DI)
└─ Create Agent (via AgentFactory)
    ↓
Agent.run(prompt)
    ↓
├─ LLM processes prompt
├─ Calls tools as needed
└─ Returns final response
    ↓
Add assistant message to state
    ↓
StateStore.save(state)
    ↓
Return response
```

### Streaming Chat

```
User Request
    ↓
Service.stream_chat(prompt, conversation_id)
    ↓
├─ Load/Create AgentState
├─ Create Model, Tools, Agent
└─ Agent.run_stream(prompt)
    ↓
async with result.stream_text(delta=True):
    ↓
    ├─ Monitor result.all_messages() for tool calls
    ├─ Yield text chunks as they arrive
    └─ Track tool execution events
    ↓
Accumulate full response
    ↓
Add assistant message to state
    ↓
StateStore.save(state)
```

## Design Patterns

### 1. Factory Pattern (AgentFactory)

**Purpose**: Encapsulate agent creation logic

**Benefits**:
- Centralized configuration
- Easy to add new agent types
- Consistent initialization
- Testable in isolation

**Usage**:
```python
agent = agent_factory.create_agent(
    agent_type=AgentType.GENERAL,
    model=model,
    tools=tools,
    state=state
)
```

### 2. Registry Pattern (ToolRegistry)

**Purpose**: Centralized tool registration

**Benefits**:
- Declarative registration
- Metadata management
- Tool filtering
- Permission control

**Usage**:
```python
@tool_registry.register(
    name="my_tool",
    category=ToolCategory.UTILITY,
    description="Does something useful"
)
async def my_tool(param: str) -> str:
    return f"Result: {param}"
```

### 3. Dependency Injection (ToolCollection)

**Purpose**: Inject service dependencies into tools

**Benefits**:
- Clean separation of concerns
- Service dependencies hidden from LLM
- Testable tools
- Flexible composition

**Implementation**:
```python
# Tool with service dependency
async def my_tool(db_service: DatabaseService, query: str) -> str:
    return await db_service.query(query)

# ToolCollection binds db_service
bound_tool = tool_collection._bind_service(my_tool, db_service_instance)

# Pydantic AI only sees: my_tool(query: str)
```

### 4. Strategy Pattern (ModelProvider)

**Purpose**: Abstract provider differences

**Benefits**:
- Unified interface
- Easy provider switching
- Provider-specific optimizations
- Configuration flexibility

**Usage**:
```python
provider = ModelProvider.ANTHROPIC
model = provider.create(
    model_name="claude-3-5-sonnet-20241022",
    api_key=api_key
)
```

### 5. Repository Pattern (StateStore)

**Purpose**: Abstract state persistence

**Benefits**:
- Storage flexibility
- Easy testing
- Production-ready
- Consistent interface

**Usage**:
```python
await state_store.save(state)
state = await state_store.load(conversation_id)
```

## Extension Points

### Adding New Agent Types

```python
# 1. Define enum value
class AgentType(str, Enum):
    GENERAL = "general"
    SPECIALIZED = "specialized"

# 2. Register configuration
agent_factory.register_config(AgentConfig(
    agent_type=AgentType.SPECIALIZED,
    system_prompt="You are a specialized assistant...",
    tool_names=["tool1", "tool2"],
    model_settings={"temperature": 0.0}
))
```

### Adding New Tools

```python
# Simple tool
@tool_registry.register(
    name="new_tool",
    category=ToolCategory.DATA,
    description="Performs data operation"
)
async def new_tool(param: str) -> str:
    return f"Processed: {param}"

# Tool with service dependency
@tool_registry.register(...)
async def new_tool(service: MyService, param: str) -> str:
    return await service.process(param)
```

### Adding New Providers

```python
class ModelProvider(Enum):
    CUSTOM = "custom"

    def create(self, model_name, base_url, api_key, settings):
        providers = {
            ModelProvider.CUSTOM: (
                CustomModel,
                CustomProvider(**kwargs)
            ),
        }
        # ... implementation
```

### Custom State Storage

```python
class RedisStateStore(StateStore):
    def __init__(self, redis_client):
        self.redis = redis_client

    async def save(self, state: AgentState):
        await self.redis.set(
            state.conversation_id,
            state.to_json(),
            ex=86400
        )

    async def load(self, conversation_id: str):
        data = await self.redis.get(conversation_id)
        return AgentState.from_json(data) if data else None
```
