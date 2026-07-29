# Model Provider Guide

Complete guide to supporting multiple LLM providers with Pydantic AI.

## Supported Providers

- **OpenAI** - GPT-4, GPT-3.5, etc.
- **Anthropic** - Claude 3.5 Sonnet, Claude 3 Opus, etc.
- **Google** - Gemini Pro, Gemini Flash
- **Ollama** - Local models (Llama, Mistral, etc.)

## Provider Abstraction

### ModelProvider Enum

```python
from enum import Enum
from pydantic_ai.models.openai import OpenAIChatModel
from pydantic_ai.models.anthropic import AnthropicModel
from pydantic_ai.models.google import GoogleModel
from pydantic_ai.providers.openai import OpenAIProvider
from pydantic_ai.providers.anthropic import AnthropicProvider
from pydantic_ai.providers.ollama import OllamaProvider
from pydantic_ai.providers.google import GoogleProvider

class ModelProvider(Enum):
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
    ):
        """Create model instance"""
        settings = settings or {"temperature": 0.1}

        providers = {
            ModelProvider.OLLAMA: (
                OpenAIChatModel,
                OllamaProvider(base_url=base_url or "http://localhost:11434/v1")
            ),
            ModelProvider.GOOGLE: (
                GoogleModel,
                GoogleProvider(api_key=api_key)
            ),
            ModelProvider.OPENAI: (
                OpenAIChatModel,
                OpenAIProvider(api_key=api_key, base_url=base_url)
            ),
            ModelProvider.ANTHROPIC: (
                AnthropicModel,
                AnthropicProvider(api_key=api_key)
            ),
        }

        model_cls, provider = providers[self]
        return model_cls(model_name, provider=provider, settings=settings)

    @classmethod
    def from_string(cls, provider_name: str | None):
        """Create from string"""
        try:
            return cls(provider_name.lower()) if provider_name else cls.OLLAMA
        except ValueError:
            return cls.OLLAMA
```

## Usage Examples

### OpenAI

```python
provider = ModelProvider.OPENAI
model = provider.create(
    model_name="gpt-4",
    api_key="sk-...",
    settings={"temperature": 0.7}
)
```

**Models**:
- `gpt-4` - Most capable
- `gpt-4-turbo` - Faster, cheaper
- `gpt-3.5-turbo` - Fast, economical

### Anthropic

```python
provider = ModelProvider.ANTHROPIC
model = provider.create(
    model_name="claude-3-5-sonnet-20241022",
    api_key="sk-ant-...",
    settings={"temperature": 0.1}
)
```

**Models**:
- `claude-3-5-sonnet-20241022` - Best balance
- `claude-3-opus-20240229` - Most capable
- `claude-3-haiku-20240307` - Fastest, cheapest

### Google

```python
provider = ModelProvider.GOOGLE
model = provider.create(
    model_name="gemini-1.5-pro",
    api_key="...",
    settings={"temperature": 0.5}
)
```

**Models**:
- `gemini-1.5-pro` - Most capable
- `gemini-1.5-flash` - Fast, efficient

### Ollama (Local)

```python
provider = ModelProvider.OLLAMA
model = provider.create(
    model_name="llama3.2",
    base_url="http://localhost:11434/v1",
    settings={"temperature": 0.1}
)
```

**Models**:
- `llama3.2` - Meta's Llama 3.2
- `mistral` - Mistral 7B
- `codellama` - Code-specialized
- Any model from Ollama library

## Configuration

### Environment Variables

```python
import os

class Config:
    LLM_PROVIDER = os.getenv("LLM_PROVIDER", "ollama")
    LLM_MODEL_NAME = os.getenv("LLM_MODEL_NAME", "llama3.2")
    LLM_API_KEY = os.getenv("LLM_API_KEY")
    LLM_BASE_URL = os.getenv("LLM_BASE_URL")
    LLM_TEMPERATURE = float(os.getenv("LLM_TEMPERATURE", "0.1"))

config = Config()
```

### Service Integration

```python
class AgentService:
    def __init__(
        self,
        provider: str | None = None,
        model_name: str | None = None,
        api_key: str | None = None,
        base_url: str | None = None,
        temperature: float = 0.1
    ):
        self.provider = ModelProvider.from_string(
            provider or config.LLM_PROVIDER
        )
        self.model_name = model_name or config.LLM_MODEL_NAME
        self.api_key = api_key or config.LLM_API_KEY
        self.base_url = base_url or config.LLM_BASE_URL
        self.temperature = temperature

    def _create_model(self):
        """Create model from configuration"""
        return self.provider.create(
            model_name=self.model_name,
            base_url=self.base_url,
            api_key=self.api_key,
            settings={"temperature": self.temperature}
        )
```

## Model Settings

### Temperature

Controls randomness:
- `0.0` - Deterministic, focused
- `0.1-0.3` - Slightly creative
- `0.7-0.9` - More creative
- `1.0+` - Very random

```python
settings = {"temperature": 0.1}
```

### Max Tokens

Limit response length:

```python
settings = {
    "temperature": 0.1,
    "max_tokens": 1000
}
```

### Top P (Nucleus Sampling)

Alternative to temperature:

```python
settings = {
    "top_p": 0.9,
    "temperature": 1.0
}
```

## Provider-Specific Features

### OpenAI: Function Calling

OpenAI has excellent function calling support:

```python
model = ModelProvider.OPENAI.create(
    model_name="gpt-4",
    api_key=api_key,
    settings={
        "temperature": 0.1,
        "function_call": "auto"  # Let model decide
    }
)
```

### Anthropic: Extended Context

Claude supports very long contexts:

```python
model = ModelProvider.ANTHROPIC.create(
    model_name="claude-3-5-sonnet-20241022",
    api_key=api_key,
    settings={
        "temperature": 0.1,
        "max_tokens": 4096  # Up to 200k context
    }
)
```

### Ollama: Local Deployment

Run models locally without API keys:

```bash
# Install Ollama
curl -fsSL https://ollama.com/install.sh | sh

# Pull a model
ollama pull llama3.2

# Run Ollama server
ollama serve
```

```python
model = ModelProvider.OLLAMA.create(
    model_name="llama3.2",
    base_url="http://localhost:11434/v1"
)
```

## Switching Providers

### Runtime Switching

```python
class AgentService:
    def set_provider(self, provider: str, model_name: str):
        """Switch provider at runtime"""
        self.provider = ModelProvider.from_string(provider)
        self.model_name = model_name

# Usage
service = AgentService()
service.set_provider("anthropic", "claude-3-5-sonnet-20241022")
```

### Per-Request Provider

```python
async def chat(
    self,
    prompt: str,
    provider: str | None = None,
    model_name: str | None = None
) -> str:
    """Chat with optional provider override"""
    if provider:
        model_provider = ModelProvider.from_string(provider)
        model = model_provider.create(
            model_name=model_name or "default",
            api_key=self.api_key
        )
    else:
        model = self._create_model()

    # ... rest of chat logic
```

## Cost Optimization

### Model Selection by Task

```python
class AgentService:
    def _select_model_for_task(self, task_type: str):
        """Select appropriate model based on task"""
        if task_type == "simple":
            # Use cheaper model
            return ModelProvider.OPENAI.create(
                model_name="gpt-3.5-turbo",
                api_key=self.api_key
            )
        elif task_type == "complex":
            # Use more capable model
            return ModelProvider.ANTHROPIC.create(
                model_name="claude-3-5-sonnet-20241022",
                api_key=self.api_key
            )
        else:
            return self._create_model()
```

### Fallback Strategy

```python
async def chat_with_fallback(self, prompt: str) -> str:
    """Try primary provider, fallback to secondary"""
    try:
        # Try primary (e.g., Anthropic)
        model = ModelProvider.ANTHROPIC.create(...)
        result = await agent.run(prompt)
        return result.data
    except Exception as e:
        logger.warning(f"Primary provider failed: {e}")

        # Fallback to secondary (e.g., OpenAI)
        model = ModelProvider.OPENAI.create(...)
        result = await agent.run(prompt)
        return result.data
```

## Testing

### Mock Provider

```python
class MockProvider:
    """Mock provider for testing"""

    def create(self, model_name, **kwargs):
        return MockModel()

class MockModel:
    async def run(self, prompt):
        return MockResult(data="Mock response")

# Use in tests
service = AgentService()
service.provider = MockProvider()
```

### Provider-Specific Tests

```python
@pytest.mark.parametrize("provider,model", [
    ("openai", "gpt-3.5-turbo"),
    ("anthropic", "claude-3-haiku-20240307"),
    ("ollama", "llama3.2"),
])
async def test_provider(provider, model):
    """Test each provider"""
    service = AgentService(provider=provider, model_name=model)
    result = await service.chat("Hello")
    assert result
```

## Best Practices

1. **Use environment variables** - Don't hardcode API keys
2. **Set reasonable defaults** - Ollama for development
3. **Handle provider failures** - Implement fallbacks
4. **Choose appropriate models** - Balance cost and capability
5. **Test with multiple providers** - Ensure compatibility
6. **Monitor costs** - Track API usage
7. **Cache responses** - Reduce redundant calls
8. **Use local models for development** - Ollama is free
