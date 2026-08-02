"""
AI Agent Service - Production Grade
Training data generation, model management, and agent lifecycle.
"""

import uuid
from datetime import datetime, timezone
from typing import List, Optional, Dict, Any
from pydantic import BaseModel, Field
from sqlalchemy import Column, String, Integer, Boolean, DateTime, JSON, Float, Text, Enum
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import declarative_base
from sqlalchemy.dialects.postgresql import UUID as PGUUID
import json

Base = declarative_base()

class AIAgent(Base):
    """AI Agent model for storing agent configurations and metadata."""
    __tablename__ = "ai_agents"
    
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    name = Column(String, nullable=False)
    type = Column(String, nullable=False)  # support, sales, refund, booking, hr, custom
    provider = Column(String, nullable=False)  # groq, google, mistral
    model = Column(String, nullable=False)
    temperature = Column(Float, default=0.7)
    
    # Training configuration
    is_trained = Column(Boolean, default=False)
    training_data_source = Column(String, nullable=True)
    training_status = Column(String, default="not_started")  # not_started, in_progress, completed, failed
    training_progress = Column(Float, default=0.0)
    
    # Prompt templates
    system_prompt = Column(Text, nullable=True)
    user_prompt_template = Column(Text, nullable=True)
    
    # Configuration
    config = Column(JSON, default=dict)
    knowledge_sources = Column(JSON, default=list)
    tools = Column(JSON, default=list)
    
    # Ownership
    tenant_id = Column(String, nullable=False, index=True)
    created_by = Column(String, nullable=False)
    
    # Metadata
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    last_trained_at = Column(DateTime, nullable=True)
    performance_metrics = Column(JSON, default=dict)
    
    is_active = Column(Boolean, default=True)

class TrainingDataPoint(BaseModel):
    """Training data representation for AI agents."""
    id: Optional[str] = None
    agent_id: str
    input_text: str
    expected_output: str
    context: Optional[Dict[str, Any]] = None
    metadata: Optional[Dict[str, Any]] = None
    source: str = "manual"  # manual, api, generated
    quality_score: Optional[float] = None
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

class TrainingBatch(BaseModel):
    """Batch of training data for an agent."""
    batch_id: Optional[str] = None
    agent_id: str
    data_points: List[TrainingDataPoint]
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    status: str = "pending"  # pending, processing, completed, failed
    model_version: Optional[str] = None
    metrics: Optional[Dict[str, float]] = None