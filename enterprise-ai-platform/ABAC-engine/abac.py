"""
SalesGenie Attribute-Based Access Control (ABAC) Engine
Fine-grained permissions based on user attributes, resource attributes, and environmental context
"""

import logging
from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from typing import Dict, List, Optional, Set, Any, Callable
from functools import wraps

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("salesgenie.abac")

class ActionType(Enum):
    READ = "read"
    WRITE = "write"
    CREATE = "create"
    UPDATE = "update"
    DELETE = "delete"
    EXECUTE = "execute"
    ADMIN = "admin"

class Environment(Enum):
    PRODUCTION = "production"
    STAGING = "staging"
    DEVELOPMENT = "development"
    MAINTENANCE = "maintenance"

@dataclass
class Attribute:
    """Represents an attribute that can be evaluated"""
    name: str
    value: Any
    operator: str = "eq"
    
    def evaluate(self) -> bool:
        return True

@dataclass
class Policy:
    """ABAC Policy Definition"""
    id: str
    name: str
    effect: str  # "allow" or "deny"
    priority: int
    conditions: List[Dict[str, Any]]
    action: List[str]
    resource_type: str
    enabled: bool = True
    created_at: datetime = field(default_factory=datetime.now)

class ABACEngine:
    """Attribute-Based Access Control Engine"""
    
    def __init__(self):
        self.policies: Dict[str, Policy] = {}
        self.user_attributes: Dict[str, Dict] = {}
        self.resource_attributes: Dict[str, Dict] = {}
        self.environment_attributes: Dict[str, Any] = {}
    
    def add_policy(self, policy: Policy):
        """Add a policy to the engine"""
        self.policies[policy.id] = policy
        logger.info(f"Added policy: {policy.name}")
    
    def set_user_attributes(self, user_id: str, attributes: Dict[str, Any]):
        """Set attributes for a user"""
        self.user_attributes[user_id] = attributes
    
    def set_resource_attributes(self, resource_id: str, resource_type: str, attributes: Dict):
        """Set attributes for a resource"""
        key = f"{resource_type}:{resource_id}"
        self.resource_attributes[key] = attributes
    
    def set_environment(self, env_attrs: Dict[str, Any]):
        """Set environment attributes"""
        self.environment_attributes.update(env_attrs)
    
    def check(self, subject: str, action: str, resource_type: str, resource_id: str, 
              context: Optional[Dict] = None) -> bool:
        """
        Check if subject can perform action on resource
        
        Context example:
        {
            'time_of_day': 'business_hours',
            'ip_address': '10.0.0.1',
            'location': 'us-east-1',
            'mfa_verified': True
        }
        """
        user_attrs = self.user_attributes.get(subject, {})
        resource_key = f"{resource_type}:{resource_id}"
        resource_attrs = self.resource_attributes.get(resource_key, {})
        effective_context = {**self.environment_attributes, **(context or {})}
        
        matching_policies = []
        
        for policy in self.policies.values():
            if not policy.enabled:
                continue
            
            if resource_type != policy.resource_type and policy.resource_type != '*':
                continue
            
            if action not in policy.action and '*' not in policy.action:
                continue
            
            if self._evaluate_conditions(policy.conditions, user_attrs, resource_attrs, effective_context):
                matching_policies.append(policy)
        
        if not matching_policies:
            return False
        
        matching_policies.sort(key=lambda p: p.priority, reverse=True)
        
        for policy in matching_policies:
            if policy.effect == "allow":
                return True
            if policy.effect == "deny":
                return False
        
        return False
    
    def _evaluate_conditions(self, conditions: List[Dict], user_attrs: Dict, 
                             resource_attrs: Dict, context: Dict) -> bool:
        """Evaluate policy conditions"""
        if not conditions:
            return True
        
        for condition in conditions:
            if not self._evaluate_single_condition(condition, user_attrs, resource_attrs, context):
                return False
        
        return True
    
    def _evaluate_single_condition(self, condition: Dict, user_attrs: Dict,
                                   resource_attrs: Dict, context: Dict) -> bool:
        """Evaluate a single condition"""
        left_attr = condition.get('left')
        op = condition.get('operator', 'eq')
        right_value = condition.get('right')
        attr_source = condition.get('source', 'user')
        
        if attr_source == 'user':
            left_val = user_attrs.get(left_attr)
        elif attr_source == 'resource':
            left_val = resource_attrs.get(left_attr)
        elif attr_source == 'context':
            left_val = context.get(left_attr)
        else:
            return False
        
        if left_val is None:
            return False
        
        if op == 'eq':
            return left_val == right_value
        elif op == 'neq':
            return left_val != right_value
        elif op == 'gt':
            return left_val > right_value
        elif op == 'gte':
            return left_val >= right_value
        elif op == 'lt':
            return left_val < right_value
        elif op == 'lte':
            return left_val <= right_value
        elif op == 'in':
            return left_val in right_value
        elif op == 'contains':
            return right_value in left_val
        elif op == 'regex':
            import re
            return bool(re.search(right_value, str(left_val)))
        
        return True
    
    def reload_policies(self):
        """Reload policies from database"""
        pass

class PermissionDecorator:
    """Decorator for permission checking on functions"""
    
    def __init__(self, engine: ABACEngine):
        self.engine = engine
    
    def require(self, action: str, resource_type: str):
        """Decorator requiring specific permission"""
        def decorator(func: Callable):
            @wraps(func)
            async def wrapper(*args, **kwargs):
                user_id = kwargs.get('user_id') or (args[0] if args else None)
                resource_id = kwargs.get('resource_id')
                context = kwargs.get('context', {})
                
                if not user_id:
                    raise PermissionError("User not authenticated")
                
                allowed = self.engine.check(user_id, action, resource_type, resource_id, context)
                if not allowed:
                    raise PermissionError(f"Access denied: {action} on {resource_type}")
                
                return await func(*args, **kwargs) if asyncio.iscoroutinefunction(func) else func(*args, **kwargs)
            return wrapper
        return decorator

# Default policies for SalesGenie
def create_default_policies() -> List[Policy]:
    """Create default ABAC policies for SalesGenie"""
    return [
        Policy(
            id="admin_full_access",
            name="Admin Full Access",
            effect="allow",
            priority=100,
            action=["*"],
            resource_type="*",
            conditions=[{'left': 'role', 'operator': 'eq', 'right': 'admin', 'source': 'user'}]
        ),
        Policy(
            id="owner_resource_access",
            name="Resource Owner Access",
            effect="allow",
            priority=90,
            action=["read", "write", "delete"],
            resource_type="*",
            conditions=[{'left': 'organization_id', 'operator': 'eq', 'right': 'user.organization_id', 'source': 'user'},
                       {'left': 'owner_id', 'operator': 'eq', 'right': 'user.id', 'source': 'resource'}]
        ),
        Policy(
            id="member_read_access",
            name="Member Read Access",
            effect="allow",
            priority=50,
            action=["read"],
            resource_type="*",
            conditions=[{'left': 'status', 'operator': 'eq', 'right': 'active', 'source': 'user'}]
        ),
        Policy(
            id="restrict_admin_hours",
            name="Restrict Admin Actions to Business Hours",
            effect="deny",
            priority=80,
            action=["delete", "admin"],
            resource_type="*",
            conditions=[{'left': 'is_admin_action', 'operator': 'eq', 'right': True, 'source': 'context'},
                       {'left': 'time_of_day', 'operator': 'notin', 'right': ['business_hours'], 'source': 'context'}]
        ),
        Policy(
            id="mfa_required_sensitive",
            name="MFA Required for Sensitive Operations",
            effect="deny",
            priority=70,
            action=["admin", "delete"],
            resource_type="*",
            conditions=[{'left': 'mfa_verified', 'operator': 'eq', 'right': False, 'source': 'context'}]
        )
    ]

if __name__ == "__main__":
    engine = ABACEngine()
    
    for policy in create_default_policies():
        engine.add_policy(policy)
    
    engine.set_user_attributes("user_123", {
        "id": "user_123",
        "organization_id": "org_456",
        "role": "member",
        "department": "sales",
        "region": "us-east-1"
    })
    
    engine.set_user_attributes("user_789", {
        "id": "user_789",
        "organization_id": "org_456",
        "role": "admin",
        "department": "it",
        "region": "us-east-1"
    })
    
    engine.set_resource_attributes("cust_123", "customers", {
        "id": "cust_123",
        "owner_id": "user_123",
        "organization_id": "org_456",
        "classification": "public"
    })
    
    engine.set_environment({
        "environment": "production",
        "time_of_day": "business_hours"
    })
    
    print("ABAC Engine Initialized")
    print("=" * 50)
    
    print(f"User can read customer: {engine.check('user_123', 'read', 'customers', 'cust_123')}")
    print(f"User can delete customer: {engine.check('user_123', 'delete', 'customers', 'cust_123')}")
    print(f"Admin can delete customer: {engine.check('user_789', 'delete', 'customers', 'cust_123')}")
    print(f"User can read unknown: {engine.check('user_123', 'read', 'tickets', 'ticket_xyz')}")