"""
LangGraph Multi-Agent Orchestration Engine
Reroutes conversation state across Sales, Support, Memory, Search, and Analytics agents.
"""

from typing import Any, Dict, List, Optional

from pydantic import BaseModel, Field

from enterprise_ai_platform.common.cost_management import TaskComplexity
from enterprise_ai_platform.common.logging import get_structured_logger

from .llm_provider import llm_provider
from .prompts import build_agent_system_prompt

logger = get_structured_logger("salesgenie.ai.agent", "ai-gateway-service")


class AgentState(BaseModel):
    """LangGraph Shared State across multi-agent graph execution nodes."""
    session_id: str
    tenant_id: str
    user_id: str
    messages: List[Dict[str, str]]
    active_agent: str = "router"
    retrieved_knowledge: Optional[str] = None
    intent_category: Optional[str] = None
    ai_confidence: float = 0.95
    suggested_actions: List[str] = Field(default_factory=list)


class MultiAgentOrchestrator:
    """LangGraph Graph Router routing intents between specialized domain agents."""

    @staticmethod
    def classify_intent(user_message: str) -> str:
        """Intent classifier routing message to Sales, Support, or Knowledge Search."""
        msg_lower = user_message.lower()
        if any(w in msg_lower for w in ["buy", "price", "pricing", "discount", "demo", "cost", "quote", "sales", "coupon"]):
            return "sales_agent"
        elif any(w in msg_lower for w in ["help", "ticket", "refund", "track", "order", "status", "shipment", "issue"]):
            return "support_agent"
        elif any(w in msg_lower for w in ["search", "document", "pdf", "policy", "faq", "how to"]):
            return "search_agent"
        return "support_agent"

    async def execute_turn(self, state: AgentState) -> Dict[str, Any]:
        """
        Executes a multi-agent graph turn:
        1. Classifies intent & selects target agent node.
        2. Injects system prompt & episodic memory context.
        3. Invokes LLM execution engine.
        4. Calculates AI response confidence score.
        """
        import time as _time
        turn_start = _time.time()
        last_user_msg = state.messages[-1]["content"] if state.messages else ""
        target_agent = self.classify_intent(last_user_msg)
        state.active_agent = target_agent

        logger.info(
            "Agent turn starting",
            extra={
                "session_id": state.session_id,
                "tenant_id": state.tenant_id,
                "user_id": state.user_id,
                "target_agent": target_agent,
                "message_count": len(state.messages),
            }
        )

        # Build System Prompt
        system_prompt = build_agent_system_prompt(
            agent_type=target_agent,
            extra_context=state.retrieved_knowledge or "Standard SalesGenie Enterprise KB Grounding",
        )

        # Determine task complexity based on agent type and message length
        msg_len = len(last_user_msg)
        if target_agent == "search_agent" and msg_len < 100:
            complexity = TaskComplexity.LOW
        elif target_agent == "analytics_agent" and msg_len > 500:
            complexity = TaskComplexity.HIGH
        else:
            complexity = TaskComplexity.MEDIUM

        # Generate Completion
        res = await llm_provider.generate_response(
            messages=state.messages,
            system_prompt=system_prompt,
            task_complexity=complexity.value,
            tenant_id=state.tenant_id,
        )

        # Calculate AI confidence based on provider quality
        ai_confidence = 0.5 if res.get("provider") == "fallback" else 0.95

        # Actions & Next Steps
        actions = []
        if target_agent == "sales_agent":
            actions = ["Book Demo Meeting", "View Recommended Products", "Apply Coupon 'SAVE15'"]
        elif target_agent == "support_agent":
            actions = ["Track Order Shipment", "Request Refund", "Talk to Human Agent"]

        duration_ms = round((_time.time() - turn_start) * 1000, 2)
        logger.info(
            "Agent turn completed",
            extra={
                "session_id": state.session_id,
                "tenant_id": state.tenant_id,
                "user_id": state.user_id,
                "target_agent": target_agent,
                "provider": res["provider"],
                "model": res["model"],
                "tokens_used": res["tokens_used"],
                "ai_confidence": ai_confidence,
                "duration_ms": duration_ms,
            }
        )

        return {
            "session_id": state.session_id,
            "active_agent": target_agent,
            "response": res["content"],
            "provider": res["provider"],
            "model": res.get("model", ""),
            "tokens_used": res.get("tokens_used", 0),
            "ai_confidence": ai_confidence,
            "suggested_actions": actions,
            "estimated_cost_usd": res.get("estimated_cost_usd", 0.0),
            "input_tokens": res.get("input_tokens", 0),
            "output_tokens": res.get("output_tokens", 0),
        }


agent_orchestrator = MultiAgentOrchestrator()
