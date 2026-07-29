# Dependency Injection Pattern

Deep dive into the dependency injection pattern for Pydantic AI tools.

## The Problem

Pydantic AI tools need access to services (databases, APIs, etc.), but:

1. **LLM shouldn't see service parameters** - The model should only see user-facing parameters
2. **Services need lifecycle management** - Database connections, API clients need proper initialization
3. **Tools should be testable** - Easy to mock services for testing
4. **Clean separation** - Business logic separate from infrastructure

## The Solution: Signature Manipulation

This pattern uses **signature manipulation** to inject dependencies while hiding them from Pydantic AI.

### How It Works

```python
# 1. Define tool with service parameter
async def query_database(db_service: DatabaseService, query: str) -> str:
    """Query the database"""
    return await db_service.execute(query)

# 2. ToolCollection detects the dependency
def _needs_service(self, tool_func, service_type):
    sig = inspect.signature(tool_func)
    params = list(sig.parameters.values())
    return params[0].annotation is service_type

# 3. Bind the service instance
def _bind_service(self, tool_func, service_instance):
    # Get original signature
    original_sig = inspect.signature(tool_func)
    params = list(original_sig.parameters.values())

    # Remove first parameter (the service)
    new_params = params[1:]
    new_sig = original_sig.replace(parameters=new_params)

    # Create wrapper that injects service
    @wraps(tool_func)
    async def bound_tool(*args, **kwargs):
        return await tool_func(service_instance, *args, **kwargs)

    # Update signature so Pydantic AI doesn't see service
    bound_tool.__signature__ = new_sig
    return bound_tool

# 4. Pydantic AI sees: query_database(query: str)
#    But actually calls: query_database(db_service, query)
```

## Complete Example

### Step 1: Define Your Service

```python
from dataclasses import dataclass

@dataclass
class DatabaseService:
    """Database service"""
    connection_string: str

    async def execute(self, query: str) -> str:
        # Execute query logic
        return f"Results for: {query}"

    async def close(self):
        # Cleanup logic
        pass
```

### Step 2: Register Tools with Service Dependency

```python
from .tool_registry import tool_registry, ToolCategory

@tool_registry.register(
    name="query_database",
    category=ToolCategory.DATA,
    description="Query the database with SQL"
)
async def query_database(db_service: DatabaseService, query: str) -> str:
    """
    Execute a database query

    Args:
        db_service: Database service (injected, not visible to LLM)
        query: SQL query to execute (visible to LLM)
    """
    return await db_service.execute(query)

@tool_registry.register(
    name="list_tables",
    category=ToolCategory.DATA,
    description="List all database tables"
)
async def list_tables(db_service: DatabaseService) -> str:
    """List all tables in the database"""
    return await db_service.execute("SHOW TABLES")
```

### Step 3: Update ToolCollection

```python
from dataclasses import dataclass
import inspect
from typing import List, Callable
from functools import wraps

@dataclass
class ToolCollection:
    """Tool collection with dependency injection"""

    # Declare your services
    database_service: DatabaseService

    def _needs_database_service(self, tool_func: Callable) -> bool:
        """Check if tool needs database service"""
        try:
            sig = inspect.signature(tool_func)
            params = list(sig.parameters.values())
            if not params:
                return False
            return params[0].annotation is DatabaseService
        except Exception:
            return False

    def _bind_database_service(self, tool_func: Callable) -> Callable:
        """Bind database service to tool"""
        db_service = self.database_service

        # Remove first parameter from signature
        original_sig = inspect.signature(tool_func)
        params = list(original_sig.parameters.values())
        new_params = params[1:] if params else []
        new_sig = original_sig.replace(parameters=new_params)

        @wraps(tool_func)
        async def bound_tool(*args, **kwargs):
            return await tool_func(db_service, *args, **kwargs)

        # Critical: Update signature
        bound_tool.__signature__ = new_sig
        bound_tool.__name__ = tool_func.__name__
        return bound_tool

    def get_all_tools(self) -> List[Callable]:
        """Get all tools with bound dependencies"""
        bound_tools = []
        all_tools = tool_registry.get_all_tools()

        for tool_func in all_tools:
            if self._needs_database_service(tool_func):
                bound_tools.append(self._bind_database_service(tool_func))
            else:
                bound_tools.append(tool_func)

        return bound_tools
```

### Step 4: Use in Service

```python
class AgentService:
    def __init__(self, db_connection_string: str):
        self.db_connection_string = db_connection_string

    def _create_tools(self) -> ToolCollection:
        """Create tool collection with services"""
        db_service = DatabaseService(
            connection_string=self.db_connection_string
        )

        return ToolCollection(database_service=db_service)

    async def chat(self, prompt: str) -> str:
        tools = self._create_tools()
        model = self._create_model()
        agent = agent_factory.create_agent(
            agent_type=AgentType.GENERAL,
            model=model,
            tools=tools.get_all_tools(),  # Bound tools
            state=None
        )

        result = await agent.run(prompt)
        return result.data
```

## Multiple Services

Handle multiple service types:

```python
@dataclass
class ToolCollection:
    database_service: DatabaseService
    api_service: APIService
    cache_service: CacheService

    def _needs_service(self, tool_func: Callable, service_type: type) -> bool:
        """Generic service detection"""
        try:
            sig = inspect.signature(tool_func)
            params = list(sig.parameters.values())
            if not params:
                return False
            return params[0].annotation is service_type
        except Exception:
            return False

    def _bind_service(self, tool_func: Callable, service_instance: Any) -> Callable:
        """Generic service binding"""
        original_sig = inspect.signature(tool_func)
        params = list(original_sig.parameters.values())
        new_params = params[1:] if params else []
        new_sig = original_sig.replace(parameters=new_params)

        @wraps(tool_func)
        async def bound_tool(*args, **kwargs):
            return await tool_func(service_instance, *args, **kwargs)

        bound_tool.__signature__ = new_sig
        bound_tool.__name__ = tool_func.__name__
        return bound_tool

    def get_all_tools(self) -> List[Callable]:
        """Bind all services"""
        bound_tools = []
        all_tools = tool_registry.get_all_tools()

        for tool_func in all_tools:
            if self._needs_service(tool_func, DatabaseService):
                bound_tools.append(self._bind_service(tool_func, self.database_service))
            elif self._needs_service(tool_func, APIService):
                bound_tools.append(self._bind_service(tool_func, self.api_service))
            elif self._needs_service(tool_func, CacheService):
                bound_tools.append(self._bind_service(tool_func, self.cache_service))
            else:
                bound_tools.append(tool_func)

        return bound_tools
```

## Testing

Dependency injection makes testing easy:

```python
import pytest
from unittest.mock import AsyncMock

@pytest.mark.asyncio
async def test_query_database_tool():
    # Create mock service
    mock_db = AsyncMock(spec=DatabaseService)
    mock_db.execute.return_value = "Mock results"

    # Create tool collection with mock
    tools = ToolCollection(database_service=mock_db)
    bound_tools = tools.get_all_tools()

    # Find the query_database tool
    query_tool = next(t for t in bound_tools if t.__name__ == "query_database")

    # Call tool (service is injected automatically)
    result = await query_tool(query="SELECT * FROM users")

    # Verify
    assert result == "Mock results"
    mock_db.execute.assert_called_once_with("SELECT * FROM users")
```

## Key Benefits

1. **Clean Tool Signatures**: LLM only sees user-facing parameters
2. **Service Lifecycle**: Services managed at service layer, not in tools
3. **Testability**: Easy to mock services for unit tests
4. **Flexibility**: Add/remove services without changing tool signatures
5. **Type Safety**: Full type checking with mypy/pyright
6. **Reusability**: Same tool works with different service implementations

## Common Patterns

### Pattern 1: Optional Services

```python
@dataclass
class ToolCollection:
    database_service: DatabaseService | None = None

    def get_all_tools(self) -> List[Callable]:
        bound_tools = []
        for tool_func in tool_registry.get_all_tools():
            if self._needs_service(tool_func, DatabaseService):
                if self.database_service:
                    bound_tools.append(self._bind_service(tool_func, self.database_service))
                # Skip tools that need unavailable services
            else:
                bound_tools.append(tool_func)
        return bound_tools
```

### Pattern 2: Service Factory

```python
@dataclass
class ToolCollection:
    service_factory: ServiceFactory

    def get_all_tools(self) -> List[Callable]:
        # Create services on-demand
        db_service = self.service_factory.create_database_service()
        api_service = self.service_factory.create_api_service()

        # Bind services
        # ...
```

### Pattern 3: Context Manager

```python
class ToolCollection:
    async def __aenter__(self):
        # Initialize services
        self.db_service = await DatabaseService.connect()
        return self

    async def __aexit__(self, *args):
        # Cleanup services
        await self.db_service.close()
```
