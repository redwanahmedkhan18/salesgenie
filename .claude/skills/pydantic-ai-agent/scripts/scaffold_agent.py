#!/usr/bin/env python3
"""
Scaffold a Pydantic AI Agent Project

Generates a complete agent project structure with layered architecture.
"""

import argparse
import os
from pathlib import Path
from typing import List


TEMPLATES = {
    "agent_factory.py": '''"""
Agent Factory

Factory pattern for creating AI agents with different configurations.
"""

from enum import Enum
from typing import Dict, List, Any, TYPE_CHECKING
from dataclasses import dataclass
import logging

from pydantic_ai import Agent

if TYPE_CHECKING:
    from .agent_state import AgentState

logger = logging.getLogger(__name__)


class AgentType(str, Enum):
    """Agent type enumeration"""
    GENERAL = "general"
    # Add more types as needed:
    # SPECIALIZED = "specialized"


@dataclass
class AgentConfig:
    """Agent configuration"""
    agent_type: AgentType
    system_prompt: str
    tool_names: List[str] | None  # None means use all tools
    model_settings: Dict[str, Any]


class AgentFactory:
    """Factory for creating configured agents"""

    def __init__(self):
        self._configs: Dict[AgentType, AgentConfig] = {}
        self._register_default_configs()

    def _register_default_configs(self):
        """Register default agent configurations"""
        self._configs[AgentType.GENERAL] = AgentConfig(
            agent_type=AgentType.GENERAL,
            system_prompt="You are a helpful AI assistant.",
            tool_names=None,  # Use all tools
            model_settings={"temperature": 0.1}
        )

    def get_config(self, agent_type: AgentType) -> AgentConfig:
        """Get agent configuration"""
        config = self._configs.get(agent_type)
        if not config:
            raise ValueError(f"Unsupported agent type: {agent_type}")
        return config

    def create_agent(
        self,
        agent_type: AgentType,
        model: Any,
        tools: List,
        state: "AgentState" = None
    ) -> Agent:
        """
        Create Agent instance

        Args:
            agent_type: Agent type
            model: LLM model instance
            tools: Available tools list
            state: Optional conversation state

        Returns:
            Configured Agent instance
        """
        config = self.get_config(agent_type)
        selected_tools = self._filter_tools(tools, config.tool_names)
        system_prompt = self._build_system_prompt(config, state)

        agent = Agent(
            model,
            tools=selected_tools,
            system_prompt=system_prompt,
        )

        logger.info(f"Created agent: type={agent_type}, tools={len(selected_tools)}")
        return agent

    def _filter_tools(self, tools: List, allowed_tool_names: List[str] | None) -> List:
        """Filter tools based on configuration"""
        if allowed_tool_names is None:
            return tools
        return [tool for tool in tools if tool.__name__ in allowed_tool_names]

    def _build_system_prompt(self, config: AgentConfig, state: "AgentState" = None) -> str:
        """Build system prompt with optional context"""
        base_prompt = config.system_prompt

        if state and state.messages:
            recent = state.get_recent_context(3)
            if recent:
                context_lines = [f"{m.role}: {m.content[:100]}..." for m in recent]
                context = "\\n".join(context_lines)
                return f"{base_prompt}\\n\\nRecent context:\\n{context}"

        return base_prompt

    def register_config(self, config: AgentConfig):
        """Register custom agent configuration"""
        self._configs[config.agent_type] = config
        logger.info(f"Registered agent config: {config.agent_type}")


# Global factory instance
agent_factory = AgentFactory()
''',

    "agent_state.py": '''"""
Agent State Management

Manages conversation history and context for AI agents.
"""

from dataclasses import dataclass, field
from typing import List, Optional, Dict, Any
from datetime import datetime
from uuid import UUID, uuid4


@dataclass
class ConversationMessage:
    """Single conversation message"""
    role: str  # "user" | "assistant" | "system" | "tool"
    content: str
    timestamp: datetime = field(default_factory=datetime.now)
    tool_calls: Optional[List[Dict[str, Any]]] = None
    metadata: Dict[str, Any] = field(default_factory=dict)


@dataclass
class AgentState:
    """Agent runtime state"""
    conversation_id: str = field(default_factory=lambda: str(uuid4()))
    user_id: Optional[UUID] = None
    messages: List[ConversationMessage] = field(default_factory=list)
    context: Dict[str, Any] = field(default_factory=dict)
    created_at: datetime = field(default_factory=datetime.now)
    updated_at: datetime = field(default_factory=datetime.now)

    def add_message(
        self,
        role: str,
        content: str,
        tool_calls: Optional[List[Dict]] = None,
        metadata: Optional[Dict] = None
    ):
        """Add message to history"""
        self.messages.append(
            ConversationMessage(
                role=role,
                content=content,
                tool_calls=tool_calls,
                metadata=metadata or {}
            )
        )
        self.updated_at = datetime.now()

    def get_recent_context(self, n: int = 5) -> List[ConversationMessage]:
        """Get the most recent n messages"""
        return self.messages[-n:] if self.messages else []

    def get_tool_history(self) -> List[ConversationMessage]:
        """Get all tool call history"""
        return [m for m in self.messages if m.tool_calls]

    def clear_history(self):
        """Clear conversation history"""
        self.messages.clear()
        self.updated_at = datetime.now()

    def to_dict(self) -> Dict[str, Any]:
        """Serialize to dictionary"""
        return {
            "conversation_id": self.conversation_id,
            "user_id": str(self.user_id) if self.user_id else None,
            "message_count": len(self.messages),
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
        }
''',

    "tool_registry.py": '''"""
Tool Registry

Explicit tool registration with metadata and categorization.
"""

from typing import Callable, Dict, List, Optional, Set
from dataclasses import dataclass, field
from enum import Enum
import logging

logger = logging.getLogger(__name__)


class ToolCategory(str, Enum):
    """Tool categories"""
    UTILITY = "utility"
    DATA = "data"
    SYSTEM = "system"
    # Add more categories as needed


@dataclass
class ToolMetadata:
    """Tool metadata"""
    name: str
    func: Callable
    description: str
    category: ToolCategory
    requires_approval: bool = False
    tags: Set[str] = field(default_factory=set)
    version: str = "1.0.0"

    def to_dict(self) -> dict:
        return {
            "name": self.name,
            "description": self.description,
            "category": self.category.value,
            "requires_approval": self.requires_approval,
            "tags": list(self.tags),
            "version": self.version,
        }


class ToolRegistry:
    """Tool registry"""

    def __init__(self):
        self._tools: Dict[str, ToolMetadata] = {}
        self._categories: Dict[ToolCategory, List[str]] = {
            cat: [] for cat in ToolCategory
        }

    def register(
        self,
        name: str,
        category: ToolCategory,
        description: str = None,
        requires_approval: bool = False,
        tags: Optional[Set[str]] = None,
        version: str = "1.0.0"
    ):
        """Decorator: register a tool"""
        def decorator(func: Callable):
            metadata = ToolMetadata(
                name=name,
                func=func,
                description=description or func.__doc__ or "",
                category=category,
                requires_approval=requires_approval,
                tags=tags or set(),
                version=version
            )

            self._tools[name] = metadata
            self._categories[category].append(name)

            logger.info(f"Registered tool '{name}' in category '{category.value}'")
            return func

        return decorator

    def get_tool(self, name: str) -> Optional[ToolMetadata]:
        """Get tool metadata"""
        return self._tools.get(name)

    def get_tools_by_category(self, category: ToolCategory) -> List[Callable]:
        """Get tools by category"""
        tool_names = self._categories.get(category, [])
        return [self._tools[name].func for name in tool_names]

    def get_all_tools(self) -> List[Callable]:
        """Get all tool functions"""
        return [meta.func for meta in self._tools.values()]

    def get_tool_metadata(self) -> List[dict]:
        """Get all tool metadata"""
        return [meta.to_dict() for meta in self._tools.values()]


# Global registry instance
tool_registry = ToolRegistry()
''',

    "tools.py": '''"""
Tools with Dependency Injection

Tool collection with automatic service dependency injection.
"""

from dataclasses import dataclass
import inspect
import logging
from typing import List, Callable
from functools import wraps

from .tool_registry import tool_registry, ToolCategory

logger = logging.getLogger(__name__)


# Example tool registration
@tool_registry.register(
    name="get_available_tools",
    category=ToolCategory.UTILITY,
    description="Get a list of all available tools",
    tags={"meta", "help"}
)
async def get_available_tools() -> str:
    """Get list of available tools"""
    metadata = tool_registry.get_tool_metadata()

    tools_by_category = {}
    for meta in metadata:
        cat = meta["category"]
        if cat not in tools_by_category:
            tools_by_category[cat] = []
        tools_by_category[cat].append(meta)

    result = ["Available Tools:\\n"]
    for category, tools in tools_by_category.items():
        result.append(f"\\n{category.upper()}:")
        for tool in tools:
            approval = " [Requires Approval]" if tool["requires_approval"] else ""
            result.append(f"  - {tool['name']}{approval}")
            result.append(f"    {tool['description']}")

    return "\\n".join(result)


@dataclass
class ToolCollection:
    """
    Tool collection with dependency injection

    Automatically binds service dependencies to tools based on function signatures.
    """

    # Add your service dependencies here
    # Example: database_service: DatabaseService

    def _needs_service(self, tool_func: Callable, service_type: type) -> bool:
        """Check if tool needs a specific service"""
        try:
            sig = inspect.signature(tool_func)
            params = list(sig.parameters.values())
            if not params:
                return False
            return params[0].annotation is service_type
        except Exception as e:
            logger.warning(f"Failed to inspect {tool_func.__name__}: {e}")
            return False

    def _bind_service(self, tool_func: Callable, service_instance: Any) -> Callable:
        """Bind service to tool function"""
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
        """Return all tool functions with bound dependencies"""
        bound_tools = []
        all_tools = tool_registry.get_all_tools()

        for tool_func in all_tools:
            # Add service binding logic here
            # Example:
            # if self._needs_service(tool_func, DatabaseService):
            #     bound_tools.append(self._bind_service(tool_func, self.database_service))
            # else:
            bound_tools.append(tool_func)

        return bound_tools
''',

    "model_provider.py": '''"""
Model Provider Abstraction

Unified interface for multiple LLM providers.
"""

from enum import Enum
from typing import Any

from pydantic_ai.models.openai import OpenAIChatModel
from pydantic_ai.models.anthropic import AnthropicModel
from pydantic_ai.models.google import GoogleModel
from pydantic_ai.providers.openai import OpenAIProvider
from pydantic_ai.providers.anthropic import AnthropicProvider
from pydantic_ai.providers.ollama import OllamaProvider
from pydantic_ai.providers.google import GoogleProvider


def _build_provider_kwargs(api_key: str | None, base_url: str | None) -> dict:
    """Build provider kwargs, filtering out None values"""
    kwargs = {}
    if api_key:
        kwargs["api_key"] = api_key
    if base_url:
        kwargs["base_url"] = base_url
    return kwargs


class ModelProvider(Enum):
    """LLM provider enumeration"""
    OLLAMA = "ollama"
    GOOGLE = "google"
    OPENAI = "openai"
    ANTHROPIC = "anthropic"

    def create(
        self,
        model_name: str,
        base_url: str | None = None,
        api_key: str | None = None,
        settings: dict = None,
    ) -> Any:
        """Create model instance"""
        kwargs = _build_provider_kwargs(api_key, base_url)
        settings = settings or {"temperature": 0.1}

        providers = {
            ModelProvider.OLLAMA: (
                OpenAIChatModel,
                OllamaProvider(base_url=base_url or "http://localhost:11434/v1")
            ),
            ModelProvider.GOOGLE: (GoogleModel, GoogleProvider(**kwargs)),
            ModelProvider.OPENAI: (OpenAIChatModel, OpenAIProvider(**kwargs)),
            ModelProvider.ANTHROPIC: (AnthropicModel, AnthropicProvider(**kwargs)),
        }

        model_cls, provider = providers[self]
        return model_cls(model_name, provider=provider, settings=settings)

    @classmethod
    def from_string(cls, provider_name: str | None) -> "ModelProvider":
        """Create provider from string"""
        try:
            return cls(provider_name.lower()) if provider_name else cls.OLLAMA
        except ValueError:
            return cls.OLLAMA
''',

    "state_store.py": '''"""
State Store

In-memory state persistence with TTL support.
Extend to Redis/DB for production.
"""

from typing import Optional, Dict
from datetime import datetime, timedelta
import logging

from .agent_state import AgentState

logger = logging.getLogger(__name__)


class StateStore:
    """State storage interface"""

    def __init__(self, ttl_hours: int = 24):
        self._store: Dict[str, AgentState] = {}
        self._ttl = timedelta(hours=ttl_hours)

    async def save(self, state: AgentState):
        """Save state"""
        self._store[state.conversation_id] = state
        logger.info(f"Saved state for conversation {state.conversation_id}")

    async def load(self, conversation_id: str) -> Optional[AgentState]:
        """Load state"""
        state = self._store.get(conversation_id)
        if state:
            if datetime.now() - state.updated_at > self._ttl:
                await self.delete(conversation_id)
                return None
        return state

    async def delete(self, conversation_id: str):
        """Delete state"""
        if conversation_id in self._store:
            del self._store[conversation_id]
            logger.info(f"Deleted state for conversation {conversation_id}")

    async def cleanup_expired(self):
        """Clean up expired states"""
        now = datetime.now()
        expired = [
            cid for cid, state in self._store.items()
            if now - state.updated_at > self._ttl
        ]
        for cid in expired:
            await self.delete(cid)
        if expired:
            logger.info(f"Cleaned up {len(expired)} expired conversations")


# Global instance
state_store = StateStore()
''',

    "service.py": '''"""
Agent Service

Main service layer for agent operations.
"""

import logging
from typing import Optional, AsyncIterable
from uuid import uuid4

from pydantic_ai.usage import UsageLimits

from .agent_factory import agent_factory, AgentType
from .agent_state import AgentState
from .state_store import state_store
from .tools import ToolCollection
from .model_provider import ModelProvider

logger = logging.getLogger(__name__)


class AgentService:
    """Agent service for managing agent lifecycle"""

    def __init__(
        self,
        provider: str = "ollama",
        model_name: str = "llama3.2",
        api_key: str | None = None,
        base_url: str | None = None
    ):
        self.provider = ModelProvider.from_string(provider)
        self.model_name = model_name
        self.api_key = api_key
        self.base_url = base_url

    def _create_model(self):
        """Create LLM model"""
        return self.provider.create(
            model_name=self.model_name,
            base_url=self.base_url,
            api_key=self.api_key,
        )

    def _create_tools(self) -> ToolCollection:
        """Create tool collection"""
        return ToolCollection()

    async def _load_or_create_state(
        self,
        conversation_id: Optional[str],
        user_id: str | None = None
    ) -> AgentState:
        """Load or create conversation state"""
        if conversation_id:
            state = await state_store.load(conversation_id)
            if state:
                logger.info(f"Loaded existing state: {conversation_id}")
                return state

        state = AgentState(
            conversation_id=conversation_id or str(uuid4()),
            user_id=user_id
        )
        logger.info(f"Created new state: {state.conversation_id}")
        return state

    async def chat(
        self,
        prompt: str,
        conversation_id: Optional[str] = None,
        user_id: str | None = None
    ) -> str:
        """
        Simple chat (non-streaming)

        Args:
            prompt: User's input message
            conversation_id: Optional conversation ID
            user_id: Optional user ID

        Returns:
            Agent's response
        """
        state = await self._load_or_create_state(conversation_id, user_id)
        state.add_message("user", prompt)

        tools = self._create_tools()
        model = self._create_model()
        agent = agent_factory.create_agent(
            agent_type=AgentType.GENERAL,
            model=model,
            tools=tools.get_all_tools(),
            state=state
        )

        try:
            result = await agent.run(prompt)
            response = result.data

            state.add_message("assistant", response)
            await state_store.save(state)

            return response

        except Exception as e:
            logger.error(f"Chat error: {e}", exc_info=True)
            raise

    async def stream_chat(
        self,
        prompt: str,
        conversation_id: Optional[str] = None,
        user_id: str | None = None
    ) -> AsyncIterable[str]:
        """
        Streaming chat

        Args:
            prompt: User's input message
            conversation_id: Optional conversation ID
            user_id: Optional user ID

        Yields:
            Text chunks from agent
        """
        state = await self._load_or_create_state(conversation_id, user_id)
        state.add_message("user", prompt)

        tools = self._create_tools()
        model = self._create_model()
        agent = agent_factory.create_agent(
            agent_type=AgentType.GENERAL,
            model=model,
            tools=tools.get_all_tools(),
            state=state
        )

        try:
            usage_limits = UsageLimits(request_limit=10)
            async with agent.run_stream(prompt, usage_limits=usage_limits) as result:
                assistant_response = []

                async for chunk in result.stream_text(delta=True):
                    if chunk:
                        assistant_response.append(chunk)
                        yield chunk

                full_response = "".join(assistant_response)
                state.add_message("assistant", full_response)
                await state_store.save(state)

        except Exception as e:
            logger.error(f"Stream chat error: {e}", exc_info=True)
            raise
''',

    "__init__.py": '''"""
Pydantic AI Agent Package
"""

from .agent_factory import agent_factory, AgentType
from .agent_state import AgentState
from .service import AgentService
from .tool_registry import tool_registry, ToolCategory
from .model_provider import ModelProvider

__all__ = [
    "agent_factory",
    "AgentType",
    "AgentState",
    "AgentService",
    "tool_registry",
    "ToolCategory",
    "ModelProvider",
]
''',

    "requirements.txt": '''# Core dependencies
pydantic-ai>=0.0.14
pydantic>=2.0.0

# LLM Providers (install as needed)
openai>=1.0.0
anthropic>=0.18.0
google-generativeai>=0.3.0

# Optional: FastAPI for web services
fastapi>=0.104.0
uvicorn>=0.24.0
''',

    "example_cli.py": '''#!/usr/bin/env python3
"""
Example CLI Application

Simple command-line interface for the agent.
"""

import asyncio
import sys
from pathlib import Path

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent))

from service import AgentService


async def main():
    """Run interactive CLI"""
    print("Pydantic AI Agent CLI")
    print("Type 'exit' to quit\\n")

    service = AgentService(
        provider="ollama",  # Change as needed
        model_name="llama3.2"
    )

    conversation_id = None

    while True:
        try:
            prompt = input("You: ").strip()
            if not prompt:
                continue
            if prompt.lower() in ["exit", "quit"]:
                break

            print("Agent: ", end="", flush=True)
            async for chunk in service.stream_chat(prompt, conversation_id):
                print(chunk, end="", flush=True)
            print()  # New line after response

            # Get conversation ID from state for continuity
            if not conversation_id:
                # In a real app, you'd get this from the service
                pass

        except KeyboardInterrupt:
            print("\\nExiting...")
            break
        except Exception as e:
            print(f"\\nError: {e}")


if __name__ == "__main__":
    asyncio.run(main())
''',

    "example_fastapi.py": '''#!/usr/bin/env python3
"""
Example FastAPI Application

REST API with SSE streaming support.
"""

from typing import Optional
from fastapi import FastAPI, Query
from fastapi.responses import StreamingResponse
import asyncio

from service import AgentService

app = FastAPI(title="Pydantic AI Agent API")

# Initialize service
service = AgentService(
    provider="ollama",
    model_name="llama3.2"
)


@app.post("/chat")
async def chat(
    prompt: str,
    conversation_id: Optional[str] = Query(None)
):
    """Chat endpoint with SSE streaming"""

    async def generate():
        try:
            async for chunk in service.stream_chat(prompt, conversation_id):
                # SSE format
                yield f"data: {chunk}\\n\\n"
                await asyncio.sleep(0)  # Force flush
            yield "data: [DONE]\\n\\n"
        except Exception as e:
            yield f"data: Error: {str(e)}\\n\\n"

    return StreamingResponse(
        generate(),
        media_type="text/event-stream",
        headers={
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
        }
    )


@app.get("/health")
async def health():
    """Health check endpoint"""
    return {"status": "ok"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
''',
}


def create_file(path: Path, content: str):
    """Create a file with content"""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content)
    print(f"✅ Created: {path}")


def scaffold_agent(output_dir: str, files: List[str]):
    """Scaffold agent project"""
    base_path = Path(output_dir)

    print(f"🚀 Scaffolding Pydantic AI Agent in: {base_path}\n")

    # Create directory
    base_path.mkdir(parents=True, exist_ok=True)

    # Create files
    for file_name in files:
        if file_name in TEMPLATES:
            file_path = base_path / file_name
            create_file(file_path, TEMPLATES[file_name])

    print(f"\n✅ Scaffolding complete!")
    print(f"\nNext steps:")
    print(f"1. cd {output_dir}")
    print(f"2. pip install -r requirements.txt")
    print(f"3. Customize the generated files for your use case")
    print(f"4. Run example_cli.py or example_fastapi.py to test")


def main():
    parser = argparse.ArgumentParser(
        description="Scaffold a Pydantic AI Agent project"
    )
    parser.add_argument(
        "output_dir",
        help="Output directory for the agent project"
    )
    parser.add_argument(
        "--minimal",
        action="store_true",
        help="Generate minimal core files only"
    )
    parser.add_argument(
        "--web",
        action="store_true",
        help="Include FastAPI web service example"
    )
    parser.add_argument(
        "--cli",
        action="store_true",
        help="Include CLI example"
    )

    args = parser.parse_args()

    # Determine which files to generate
    core_files = [
        "agent_factory.py",
        "agent_state.py",
        "tool_registry.py",
        "tools.py",
        "model_provider.py",
        "state_store.py",
        "service.py",
        "__init__.py",
        "requirements.txt",
    ]

    files = core_files.copy()

    if not args.minimal:
        # Include examples by default
        if args.cli or (not args.web and not args.cli):
            files.append("example_cli.py")
        if args.web or (not args.web and not args.cli):
            files.append("example_fastapi.py")

    scaffold_agent(args.output_dir, files)


if __name__ == "__main__":
    main()
