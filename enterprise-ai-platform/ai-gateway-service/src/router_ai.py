"""
AI Gateway Service API Router
Endpoints for chat completions, agent configurations, system prompts, and tool calling.
"""

import uuid
from typing import List, Dict, Any, Optional
from pydantic import BaseModel, Field
from fastapi import APIRouter, Depends, HTTPException, status

from enterprise_ai_platform.common.security_rbac import (
    get_current_user,
    TokenPayload,
    RequirePermissions,
    Permission,
)
from enterprise_ai_platform.common.subscription_guard import require_active_subscription
from .agent_orchestrator import agent_orchestrator, AgentState
from .prompts import SYSTEM_PROMPTS

router = APIRouter(prefix="/api/v1/ai", tags=["AI Gateway & Agent Orchestration"])


class ChatMessageDTO(BaseModel):
    role: str  # 'user', 'assistant', 'system'
    content: str


class ChatCompletionRequest(BaseModel):
    session_id: str
    messages: List[ChatMessageDTO]
    agent_type: Optional[str] = None
    temperature: Optional[float] = 0.7


class ChatCompletionResponse(BaseModel):
    session_id: str
    active_agent: str
    response: str
    provider: str
    model: str
    tokens_used: int
    ai_confidence: float
    suggested_actions: List[str]
    estimated_cost_usd: float = 0.0
    input_tokens: int = 0
    output_tokens: int = 0


@router.post(
    "/chat",
    response_model=ChatCompletionResponse,
    summary="Multi-Agent Chat Completion Loop",
    dependencies=[Depends(RequirePermissions(Permission.AGENT_EXECUTE)), Depends(require_active_subscription)],
)
async def ai_chat_completion(
    req: ChatCompletionRequest,
    current_user: TokenPayload = Depends(get_current_user),
):
    """Executes multi-agent LangGraph turn for conversational AI chat responses."""
    state = AgentState(
        session_id=req.session_id,
        tenant_id=current_user.tenant_id,
        user_id=current_user.sub,
        messages=[{"role": m.role, "content": m.content} for m in req.messages],
    )

    result = await agent_orchestrator.execute_turn(state)

    return ChatCompletionResponse(
        session_id=result["session_id"],
        active_agent=result["active_agent"],
        response=result["response"],
        provider=result["provider"],
        model=result["model"],
        tokens_used=result["tokens_used"],
        ai_confidence=result["ai_confidence"],
        suggested_actions=result["suggested_actions"],
        estimated_cost_usd=result.get("estimated_cost_usd", 0.0),
        input_tokens=result.get("input_tokens", 0),
        output_tokens=result.get("output_tokens", 0),
    )


@router.get("/agents", summary="List Platform AI Agents")
async def list_agents():
    """List available AI agents and capabilities."""
    return [
        {"id": "sales_agent", "name": "AI Sales Agent", "description": "Lead qualification, recommendations, and calendar bookings"},
        {"id": "support_agent", "name": "AI Support Agent", "description": "Knowledge search, ticket escalation, and order tracking"},
        {"id": "memory_agent", "name": "Episodic Memory Agent", "description": "User preference and conversation history tracking"},
        {"id": "search_agent", "name": "Knowledge Search Agent", "description": "Vector document retrieval and BAAI re-ranking"},
        {"id": "analytics_agent", "name": "AI Analytics Agent", "description": "Accuracy evaluation and hallucination detection"},
    ]
