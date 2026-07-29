"""
Workflow Service API Router
Endpoints for creating, managing, and executing n8n-style automation workflows.
"""

from typing import List, Dict, Any
from fastapi import APIRouter, Depends, HTTPException, status

from enterprise_ai_platform.common.security_rbac import (
    get_current_user,
    TokenPayload,
    RequirePermissions,
    Permission,
)
from .workflow_engine import (
    workflow_engine,
    WorkflowGraphDTO,
    WorkflowNodeDTO,
    WorkflowEdgeDTO,
    NodeType,
)

router = APIRouter(prefix="/api/v1/workflows", tags=["Workflow Automation Engine"])


@router.post(
    "/execute",
    summary="Execute n8n Automation Workflow Graph",
    dependencies=[Depends(RequirePermissions(Permission.WORKFLOW_MANAGE))],
)
async def execute_workflow(trigger_payload: Dict[str, Any]):
    """Execute n8n DAG node workflow."""
    mock_graph = WorkflowGraphDTO(
        id="wf-lead-onboarding",
        name="Automated Lead Qualification & CRM Sync",
        nodes=[
            WorkflowNodeDTO(id="n1", type=NodeType.START, title="Lead Form Submission"),
            WorkflowNodeDTO(id="n2", type=NodeType.LLM, title="AI Lead Score Evaluator"),
            WorkflowNodeDTO(id="n3", type=NodeType.CONDITION, title="Score >= 70 Check"),
            WorkflowNodeDTO(id="n4", type=NodeType.CRM, title="HubSpot / Salesforce Sync"),
            WorkflowNodeDTO(id="n5", type=NodeType.EMAIL, title="Send Demo Invite Email"),
            WorkflowNodeDTO(id="n6", type=NodeType.END, title="Workflow Complete"),
        ],
        edges=[
            WorkflowEdgeDTO(source_node_id="n1", target_node_id="n2"),
            WorkflowEdgeDTO(source_node_id="n2", target_node_id="n3"),
            WorkflowEdgeDTO(source_node_id="n3", target_node_id="n4", condition_branch="true"),
            WorkflowEdgeDTO(source_node_id="n4", target_node_id="n5"),
            WorkflowEdgeDTO(source_node_id="n5", target_node_id="n6"),
        ],
    )

    result = await workflow_engine.execute_workflow(mock_graph, trigger_payload)
    return result
