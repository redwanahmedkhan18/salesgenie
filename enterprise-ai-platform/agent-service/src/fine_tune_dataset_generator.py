"""
Comprehensive Training Data Generator for SalesGenie AI Agents
Creates diverse datasets for customer support, sales, and technical support scenarios.
"""

import asyncio
import json
from typing import List, Dict, Any, Optional
from datetime import datetime, timezone
from dataclasses import dataclass, field, asdict
import random

@dataclass
class TrainingExample:
    id: Optional[str] = None
    agent_type: str = "support_agent"  # support_agent, sales_agent, technical_agent
    role: str = "customer"  # customer, sales_prospect, technical_user
    input_text: str = ""
    expected_output: str = ""
    context: Dict[str, Any] = field(default_factory=dict)
    intent: str = ""
    entities: Dict[str, str] = field(default_factory=dict)
    confidence_required: float = 0.8  # Confidence threshold before human handoff
    handoff_triggers: List[str] = field(default_factory=list)
    source_documentation: Optional[str] = None
    quality_score: float = 0.0

class SalesGenieTrainingDataGenerator:
    """Generates comprehensive training data for all AI agent types."""
    
    def __init__(self, tenant_id: str = "salesgenie"):
        self.tenant_id = tenant_id
        self.agents = {
            'support_agent': self._generate_support_data,
            'sales_agent': self._generate_sales_data,
            'technical_agent': self._generate_technical_data,
        }
        
        # Define handoff triggers - phrases that require human escalation
        self.handoff_triggers = [
            "I want to speak to a manager",
            "I need to cancel my subscription",
            "chargeback",
            "lawsuit",
            "legal action",
            "attorney",
            "complaint about billing",
            "not happy with refund",
            "dispute the charge",
            "report to BBB",
        ]
    
    async def generate_all_data(
        self,
        support_count: int = 500,
        sales_count: int = 300,
        technical_count: int = 200
    ) -> Dict[str, List[TrainingExample]]:
        """Generate all training data for all agent types."""
        
        tasks = [
            self._generate_support_data(support_count),
            self._generate_sales_data(sales_count),
            self._generate_technical_data(technical_count),
        ]
        
        results = await asyncio.gather(*tasks)
        
        return {
            'support_agent': results[0],
            'sales_agent': results[1],
            'technical_agent': results[2],
        }
    
    async def _generate_support_data(self, count: int) -> List[TrainingExample]:
        """Generate customer support training data."""
        examples = []
        
        # Ticket escalation scenarios
        ticket_scenarios = [
            {
                'input': "I've been waiting on hold for 2 hours!",
                'output': "I sincerely apologize for the long wait time. I've flagged this as urgent and will escalate to our management team. Can I have your account details so I can prioritize your case?",
                'intent': 'escalation_request',
                'handoff': True,
                'confidence_required': 0.9
            },
            {
                'input': "This product is broken and you refuse to fix it!",
                'output': "I understand your frustration. I want to make this right. Let me connect you with our quality assurance team who can provide immediate assistance with a return or replacement.",
                'intent': 'complaint_handoff',
                'handoff': True,
                'confidence_required': 0.95
            },
            {
                'input': "I need to cancel my account and get a refund.",
                'output': "I can help with that cancellation and refund request. Before I process this, may I ask what issues you've experienced? This helps us improve. I'll also connect you with our billing specialist to ensure this is handled properly.",
                'intent': 'account_cancellation',
                'handoff': True,
                'confidence_required': 0.95
            }
        ]
        
        # General support scenarios
        general_support = [
            {
                'input': "How do I reset my password?",
                'output': "You can reset your password by clicking 'Forgot Password' on the login page. Enter your email address and we'll send you a reset link. If you don't receive it within 10 minutes, check your spam folder or let me know and I can help manually.",
                'intent': 'password_reset',
                'handoff': False,
                'confidence_required': 0.8
            },
            {
                'input': "When will my order arrive?",
                'output': "I can check that for you! Can you provide your order number or tracking number? It usually starts with OR- or TRK-. Alternatively, you can log into your account to see the current status.",
                'intent': 'order_status',
                'handoff': False,
                'confidence_required': 0.7
            }
        ]
        
        # Combine scenarios
        all_scenarios = ticket_scenarios + general_support
        
        for i in range(count):
            scenario = all_scenarios[i % len(all_scenarios)]
            examples.append(TrainingExample(
                id=f"support_{i}_{datetime.now().isoformat()}",
                agent_type="support_agent",
                role="customer",
                input_text=scenario['input'],
                expected_output=scenario['output'],
                context={
                    'urgency': 'high' if scenario.get('handoff') else 'normal',
                    'category': scenario['intent'],
                    'channel': 'chat'
                },
                intent=scenario['intent'],
                handoff_triggers=['manager', 'cancel', 'refund', 'complaint'] if scenario.get('handoff') else [],
                confidence_required=scenario.get('confidence_required', 0.8),
                quality_score=0.95 if scenario.get('handoff') else 0.85
            ))
        
        # Add MCP server data extraction examples
        mcp_scenarios = [
            {
                'input': "Can you pull my usage data from our database?",
                'output': "I can help you access your usage data. I'll need to know which date range you're interested in. Would you like to see your usage from this month, last month, or a custom range?",
                'intent': 'data_extraction_request',
                'handoff': False,
                'confidence_required': 0.8
            }
        ]
        
        for scenario in mcp_scenarios:
            examples.append(TrainingExample(
                id=f"mcp_{datetime.now().isoformat()}",
                agent_type="support_agent",
                role="customer",
                input_text=scenario['input'],
                expected_output=scenario['output'],
                context={'mcp_access': True, 'requires_human': False},
                intent=scenario['intent'],
                confidence_required=scenario.get('confidence_required', 0.8),
                quality_score=0.9
            ))
        
        return examples
    
    async def _generate_sales_data(self, count: int) -> List[TrainingExample]:
        """Generate sales prospect training data."""
        examples = []
        
        sales_scenarios = [
            {
                'input': "I'm interested in learning more about your pricing.",
                'output': "Great question! We have several pricing tiers. Our Starter plan starts at $49/month for up to 10,000 interactions, and our Enterprise plan includes custom features. Would you like me to email you a detailed pricing sheet, or can I schedule a quick call to discuss what would work best for your needs?",
                'intent': 'pricing_inquiry',
                'lead_score': 0.8,
                'next_step': 'send_pricing'
            },
            {
                'input': "Do you integrate with Salesforce?",
                'output': "Yes! We have a native Salesforce integration that syncs contacts, deals, and leads automatically. We also integrate with HubSpot, Pipedrive, and Zoho CRM. Would you like me to send you setup instructions for Salesforce?",
                'intent': 'integration_inquiry',
                'lead_score': 0.75,
                'next_step': 'send_integration_guide'
            },
            {
                'input': "How does your AI help with sales automation?",
                'output': "Our AI automates lead qualification, follows up with warm leads, generates personalized emails, schedules demos, and tracks purchase intent signals. Companies like yours typically see a 3x improvement in follow-up rate and 40% faster deal closure. Would you like to see a quick demo?",
                'intent': 'value_proposition',
                'lead_score': 0.9,
                'next_step': 'schedule_demo'
            }
        ]
        
        for i in range(count):
            scenario = sales_scenarios[i % len(sales_scenarios)]
            examples.append(TrainingExample(
                id=f"sales_{i}_{datetime.now().isoformat()}",
                agent_type="sales_agent",
                role="sales_prospect",
                input_text=scenario['input'],
                expected_output=scenario['output'],
                context={
                    'lead_score': scenario.get('lead_score', 0.5),
                    'stage': 'interest',
                    'channel': 'website_chat'
                },
                intent=scenario['intent'],
                handoff_triggers=['schedule', 'call', 'meeting'] if scenario.get('next_step') == 'schedule_demo' else [],
                confidence_required=0.85,
                quality_score=0.9
            ))
        
        return examples
    
    async def _generate_technical_data(self, count: int) -> List[TrainingExample]:
        """Generate technical support training data."""
        examples = []
        
        technical_scenarios = [
            {
                'input': "I'm getting a 'Connection Timeout' error when logging in.",
                'output': "A connection timeout error usually indicates network connectivity issues. Try these steps: 1) Refresh the page, 2) Check your internet connection, 3) Try a different browser, 4) Clear your browser cache and cookies. If the problem persists, it might be related to firewall settings on your network. Would you like me to check if there are any known service issues?",
                'intent': 'connectivity_issue',
                'severity': 'medium',
                'handoff': False,
                'confidence_required': 0.7
            },
            {
                'input': "Why am I getting rate limit errors?",
                'output': "Rate limit errors occur when too many API requests are made in a short period. Here's what you can do: 1) Implement exponential backoff in your requests, 2) Cache responses where appropriate, 3) Contact support to request a higher rate limit for your plan. What's the volume of requests you're expecting to make?",
                'intent': 'rate_limit_error',
                'severity': 'medium',
                'handoff': True,
                'confidence_required': 0.9
            }
        ]
        
        for i in range(count):
            scenario = technical_scenarios[i % len(technical_scenarios)]
            examples.append(TrainingExample(
                id=f"tech_{i}_{datetime.now().isoformat()}",
                agent_type="technical_agent",
                role="technical_user",
                input_text=scenario['input'],
                expected_output=scenario['output'],
                context={
                    'severity': scenario.get('severity', 'low'),
                    'requires_human': scenario.get('handoff', False),
                    'error_code_detected': True
                },
                intent=scenario['intent'],
                confidence_required=scenario.get('confidence_required', 0.7),
                quality_score=0.9
            ))
        
        return examples
    
    def export_training_dataset(
        self, 
        data: Dict[str, List[TrainingExample]], 
        format: str = 'json'
    ) -> str:
        """Export training data in various formats."""
        
        export_data = {
            'metadata': {
                'generated_at': datetime.now(timezone.utc).isoformat(),
                'tenant_id': self.tenant_id,
                'format': format
            },
            'datasets': {}
        }
        
        for agent_type, examples in data.items():
            if format == 'json':
                export_data['datasets'][agent_type] = [
                    {
                        'id': ex.id,
                        'agent_type': ex.agent_type,
                        'role': ex.role,
                        'input_text': ex.input_text,
                        'expected_output': ex.expected_output,
                        'context': ex.context,
                        'intent': ex.intent,
                        'entities': ex.entities,
                        'confidence_required': ex.confidence_required,
                        'handoff_triggers': ex.handoff_triggers,
                        'quality_score': ex.quality_score
                    }
                    for ex in examples
                ]
            elif format == 'jsonl':
                lines = [
                    json.dumps({
                        'input': ex.input_text,
                        'output': ex.expected_output,
                        'context': ex.context,
                        'agent_type': ex.agent_type,
                        'intent': ex.intent,
                        'handoff_required': len(ex.handoff_triggers) > 0
                    })
                    for ex in examples
                ]
                return '\n'.join(lines)
        
        return json.dumps(export_data, indent=2)


# Human fallback handler
class HumanFallbackHandler:
    """Handles escalation to human agents when AI confidence is low."""
    
    @staticmethod
    def should_escalate(
        confidence_score: float, 
        required_confidence: float,
        user_request: str
    ) -> Dict[str, Any]:
        """Determine if escalation to human is needed."""
        
        escalation_keywords = [
            'complain', 'cancel', 'refund', 'complaint', 'manager',
            'supervisor', 'billing dispute', 'legal', 'lawsuit',
            'attorney', 'chargeback', 'dispute'
        ]
        
        needs_escalation = (
            confidence_score < required_confidence or
            any(keyword in user_request.lower() for keyword in escalation_keywords)
        )
        
        return {
            'should_escalate': needs_escalation,
            'reason': 'low_confidence' if confidence_score < required_confidence else 'escalation_keyword',
            'estimated_wait_time': '2-5 minutes' if needs_escalation else None,
            'handoff_message': "I'd like to connect you with a human specialist who can better assist with this specific case." if needs_escalation else None
        }


async def main():
    """Generate comprehensive training dataset."""
    generator = SalesGenieTrainingDataGenerator()
    
    print("Generating training data...")
    data = await generator.generate_all_data(
        support_count=300,
        sales_count=150,
        technical_count=100
    )
    
    total_examples = sum(len(examples) for examples in data.values())
    print(f"Generated {total_examples} training examples:")
    
    for agent_type, examples in data.items():
        handoff_count = sum(1 for e in examples if e.handoff_triggers)
        print(f"  - {agent_type}: {len(examples)} examples ({handoff_count} require human handoff)")
    
    # Export dataset
    json_data = generator.export_training_dataset(data, 'json')
    
    with open('/tmp/salesgenie_training_data.json', 'w') as f:
        f.write(json_data)
    
    print(f"\nDataset exported to /tmp/salesgenie_training_data.json")
    print(f"Total quality score average: {sum(e.quality_score for examples in data.values() for e in examples) / total_examples:.2f}")
    
    return data


if __name__ == "__main__":
    asyncio.run(main())