"""
SalesGenie ABAC Engine API Server
Attribute-Based Access Control with REST endpoints
"""

import os
from typing import Dict, Any, Optional, List
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from enterprise_ai_platform.common.config import settings

from abac import ABACEngine, Policy, create_default_policies

app = FastAPI(
    title="SalesGenie ABAC Engine",
    description="Attribute-Based Access Control Engine with policy management",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.BACKEND_CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

engine = ABACEngine()
policy_store: Dict[str, Policy] = {}

@app.on_event("startup")
async def startup_event():
    global engine, policy_store
    for policy in create_default_policies():
        engine.add_policy(policy)
        policy_store[policy.id] = policy
    print("ABAC Engine initialized with default policies")

@app.get("/health")
async def health_check():
    return {"status": "healthy", "service": "abac-engine", "policies_loaded": len(policy_store)}

@app.get("/policies")
async def list_policies():
    return {"policies": list(policy_store.keys()), "count": len(policy_store)}

@app.post("/policies")
async def add_policy(name: str, effect: str, priority: int, resource_type: str, 
                     action: List[str], conditions: List[Dict] = []):
    policy_id = f"policy_{len(policy_store) + 1}"
    policy = Policy(
        id=policy_id,
        name=name,
        effect=effect,
        priority=priority,
        action=action,
        resource_type=resource_type,
        conditions=conditions
    )
    engine.add_policy(policy)
    policy_store[policy_id] = policy
    return {"status": "created", "policy_id": policy_id, "name": policy.name}

@app.delete("/policies/{policy_id}")
async def remove_policy(policy_id: str):
    if policy_id in policy_store:
        del policy_store[policy_id]
        return {"status": "removed", "policy_id": policy_id}
    raise HTTPException(status_code=404, detail="Policy not found")

@app.post("/users/{user_id}/attributes")
async def set_user_attributes(user_id: str, attributes: Dict[str, Any]):
    engine.set_user_attributes(user_id, attributes)
    return {"status": "updated", "user_id": user_id}

@app.post("/resources/{resource_type}/{resource_id}/attributes")
async def set_resource_attributes(resource_type: str, resource_id: str, attributes: Dict[str, Any]):
    engine.set_resource_attributes(resource_id, resource_type, attributes)
    return {"status": "updated", "resource": f"{resource_type}:{resource_id}"}

@app.post("/check")
async def check_access(subject: str, action: str, resource_type: str, resource_id: str,
                       context: Optional[Dict] = None):
    allowed = engine.check(subject, action, resource_type, resource_id, context)
    return {"subject": subject, "action": action, "resource": f"{resource_type}:{resource_id}", "allowed": allowed}

@app.post("/environment")
async def set_environment(env_attrs: Dict[str, Any]):
    engine.set_environment(env_attrs)
    return {"status": "updated", "environment": env_attrs}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("ABAC_PORT", 8030)))