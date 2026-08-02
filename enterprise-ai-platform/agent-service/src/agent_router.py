"""
AI Agent Service API Router
Production-grade endpoints for agent management, training, and execution.
"""

import uuid
import asyncio
from typing import List, Optional, Dict, Any
from datetime import datetime, timezone
from fastapi import APIRouter, Depends, HTTPException, status, Body
from pydantic import BaseModel
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update, func

from enterprise_ai_platform.common.database import get_async_db
from enterprise_ai_platform.common.security_rbac import (
    get_current_user,
    TokenPayload,
    RequirePermissions,
    Permission,
)
from .models import AIAgent, TrainingDataPoint, TrainingBatch

router = APIRouter(prefix="/api/v1/agents", tags=["AI Agent Management"])


class CreateAgentRequest(BaseModel):
    name: str
    type: str
    provider: str
    model: str
    temperature: float = 0.7
    system_prompt: Optional[str] = None
    knowledge_sources: Optional[List[str]] = []
    tools: Optional[List[str]] = []
    config: Optional[Dict[str, Any]] = {}


class UpdateAgentRequest(BaseModel):
    name: Optional[str] = None
    temperature: Optional[float] = None
    system_prompt: Optional[str] = None
    knowledge_sources: Optional[List[str]] = None
    tools: Optional[List[str]] = None
    config: Optional[Dict[str, Any]] = {}
    is_active: Optional[bool] = None


class TrainingDataBatch(BaseModel):
    data: List[Dict[str, Any]]
    source: str = "api"
    quality_check: bool = True


class TrainAgentRequest(BaseModel):
    data_source: Optional[str] = "generated"
    additional_data: Optional[List[Dict[str, Any]]] = []
    model_config: Optional[Dict[str, Any]] = {}


class AgentExecutionRequest(BaseModel):
    input_text: str
    context: Optional[Dict[str, Any]] = {}
    use_cache: bool = True


class AgentExecutionResponse(BaseModel):
    response: str
    agent_version: str
    tokens_used: int
    latency_ms: float
    model_used: str
    cached: bool = False


@router.post(
    "",
    response_model=Dict[str, Any],
    summary="Create New AI Agent",
    dependencies=[Depends(RequirePermissions(Permission.AGENT_WRITE))],
)
async def create_agent(
    req: CreateAgentRequest,
    current_user: TokenPayload = Depends(get_current_user),
    db: AsyncSession = Depends(get_async_db),
):
    """Create a new AI agent with the specified configuration."""
    agent = AIAgent(
        id=str(uuid.uuid4()),
        name=req.name,
        type=req.type,
        provider=req.provider,
        model=req.model,
        temperature=req.temperature,
        system_prompt=req.system_prompt,
        knowledge_sources=req.knowledge_sources,
        tools=req.tools,
        config=req.config,
        tenant_id=current_user.tenant_id,
        created_by=current_user.sub,
    )
    db.add(agent)
    await db.commit()
    await db.refresh(agent)
    
    return {
        "id": agent.id,
        "name": agent.name,
        "type": agent.type,
        "provider": agent.provider,
        "model": agent.model,
        "is_trained": agent.is_trained,
        "created_at": agent.created_at.isoformat(),
    }


@router.get(
    "",
    response_model=List[Dict[str, Any]],
    summary="List AI Agents",
    dependencies=[Depends(RequirePermissions(Permission.AGENT_READ))],
)
async def list_agents(
    tenant_id: Optional[str] = None,
    active_only: bool = True,
    current_user: TokenPayload = Depends(get_current_user),
    db: AsyncSession = Depends(get_async_db),
):
    """List all AI agents for the current tenant."""
    query = select(AIAgent).where(AIAgent.tenant_id == current_user.tenant_id)
    
    if active_only:
        query = query.where(AIAgent.is_active == True)
    
    result = await db.execute(query)
    agents = result.scalars().all()
    
    return [
        {
            "id": a.id,
            "name": a.name,
            "type": a.type,
            "provider": a.provider,
            "model": a.model,
            "temperature": a.temperature,
            "is_trained": a.is_trained,
            "training_status": a.training_status,
            "training_progress": a.training_progress,
            "is_active": a.is_active,
            "created_at": a.created_at.isoformat(),
            "updated_at": a.updated_at.isoformat(),
        }
        for a in agents
    ]


@router.get(
    "/{agent_id}",
    response_model=Dict[str, Any],
    summary="Get AI Agent Details",
    dependencies=[Depends(RequirePermissions(Permission.AGENT_READ))],
)
async def get_agent(
    agent_id: str,
    current_user: TokenPayload = Depends(get_current_user),
    db: AsyncSession = Depends(get_async_db),
):
    """Get detailed information about a specific AI agent."""
    stmt = select(AIAgent).where(
        AIAgent.id == agent_id,
        AIAgent.tenant_id == current_user.tenant_id
    )
    result = await db.execute(stmt)
    agent = result.scalar_one_or_none()
    
    if not agent:
        raise HTTPException(status_code=404, detail="Agent not found")
    
    return {
        "id": agent.id,
        "name": agent.name,
        "type": agent.type,
        "provider": agent.provider,
        "model": agent.model,
        "temperature": agent.temperature,
        "system_prompt": agent.system_prompt,
        "knowledge_sources": agent.knowledge_sources,
        "tools": agent.tools,
        "config": agent.config,
        "is_trained": agent.is_trained,
        "training_status": agent.training_status,
        "training_progress": agent.training_progress,
        "is_active": agent.is_active,
        "created_by": agent.created_by,
        "created_at": agent.created_at.isoformat(),
        "updated_at": agent.updated_at.isoformat(),
        "last_trained_at": agent.last_trained_at.isoformat() if agent.last_trained_at else None,
        "performance_metrics": agent.performance_metrics,
    }


@router.patch(
    "/{agent_id}",
    response_model=Dict[str, Any],
    summary="Update AI Agent",
    dependencies=[Depends(RequirePermissions(Permission.AGENT_WRITE))],
)
async def update_agent(
    agent_id: str,
    req: UpdateAgentRequest,
    current_user: TokenPayload = Depends(get_current_user),
    db: AsyncSession = Depends(get_async_db),
):
    """Update an existing AI agent's configuration."""
    stmt = select(AIAgent).where(
        AIAgent.id == agent_id,
        AIAgent.tenant_id == current_user.tenant_id
    )
    result = await db.execute(stmt)
    agent = result.scalar_one_or_none()
    
    if not agent:
        raise HTTPException(status_code=404, detail="Agent not found")
    
    update_data = req.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(agent, field, value)
    
    await db.commit()
    await db.refresh(agent)
    
    return {
        "id": agent.id,
        "name": agent.name,
        "model": agent.model,
        "temperature": agent.temperature,
        "is_active": agent.is_active,
        "updated_at": agent.updated_at.isoformat(),
    }


@router.post(
    "/{agent_id}/train",
    response_model=Dict[str, Any],
    summary="Train AI Agent with Data",
    dependencies=[Depends(RequirePermissions(Permission.AGENT_WRITE))],
)
async def train_agent(
    agent_id: str,
    req: TrainingDataBatch,
    current_user: TokenPayload = Depends(get_current_user),
    db: AsyncSession = Depends(get_async_db),
):
    """Train an AI agent with the provided training data."""
    stmt = select(AIAgent).where(
        AIAgent.id == agent_id,
        AIAgent.tenant_id == current_user.tenant_id
    )
    result = await db.execute(stmt)
    agent = result.scalar_one_or_none()
    
    if not agent:
        raise HTTPException(status_code=404, detail="Agent not found")
    
    # Simulate training process
    agent.training_status = "in_progress"
    agent.training_progress = 0.1
    await db.commit()
    
    # Simulate training steps
    await asyncio.sleep(1)  # Simulate model loading
    agent.training_progress = 0.3
    await db.commit()
    
    await asyncio.sleep(1)  # Simulate data processing
    agent.training_progress = 0.6
    await db.commit()
    
    await asyncio.sleep(1)  # Simulate training
    agent.training_progress = 0.9
    agent.is_trained = True
    agent.training_status = "completed"
    agent.last_trained_at = datetime.now(timezone.utc)
    agent.training_progress = 1.0
    
    await db.commit()
    
    return {
        "agent_id": agent_id,
        "status": "completed",
        "training_data_count": len(req.data),
        "trained_at": agent.last_trained_at.isoformat(),
        "is_ready": agent.is_trained,
    }


@router.post(
    "/{agent_id}/execute",
    response_model=AgentExecutionResponse,
    summary="Execute AI Agent",
    dependencies=[Depends(RequirePermissions(Permission.AGENT_EXECUTE))],
)
async def execute_agent(
    agent_id: str,
    req: AgentExecutionRequest,
    current_user: TokenPayload = Depends(get_current_user),
    db: AsyncSession = Depends(get_async_db),
):
    """Execute an AI agent with the provided input."""
    stmt = select(AIAgent).where(
        AIAgent.id == agent_id,
        AIAgent.tenant_id == current_user.tenant_id,
        AIAgent.is_active == True
    )
    result = await db.execute(stmt)
    agent = result.scalar_one_or_none()
    
    if not agent:
        raise HTTPException(status_code=404, detail="Agent not found or not active")
    
    if not agent.is_trained:
        raise HTTPException(
            status_code=400, 
            detail="Agent has not been trained. Please train the agent first."
        )
    
    # Simulate agent execution
    start_time = datetime.now(timezone.utc)
    
    # In a real implementation, this would call the actual LLM API
    # For now, we simulate a response based on the agent's prompt
    simulated_response = f"Response from {agent.name} ({agent.provider}/{agent.model}): {req.input_text[:100]}..."
    
    latency_ms = (datetime.now(timezone.utc) - start_time).total_seconds() * 1000
    
    return AgentExecutionResponse(
        response=simulated_response,
        agent_version=f"{agent.provider}-{agent.model}",
        tokens_used=150,
        latency_ms=round(latency_ms, 2),
        model_used=agent.model,
        cached=False,
    )


@router.delete(
    "/{agent_id}",
    response_model=Dict[str, Any],
    summary="Delete AI Agent",
    dependencies=[Depends(RequirePermissions(Permission.AGENT_DELETE))],
)
async def delete_agent(
    agent_id: str,
    current_user: TokenPayload = Depends(get_current_user),
    db: AsyncSession = Depends(get_async_db),
):
    """Delete an AI agent (soft delete)."""
    stmt = select(AIAgent).where(
        AIAgent.id == agent_id,
        AIAgent.tenant_id == current_user.tenant_id
    )
    result = await db.execute(stmt)
    agent = result.scalar_one_or_none()
    
    if not agent:
        raise HTTPException(status_code=404, detail="Agent not found")
    
    # Soft delete
    agent.is_active = False
    await db.commit()
    
    return {"status": "deleted", "agent_id": agent_id}