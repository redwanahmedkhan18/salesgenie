"""
Training Data Generator for AI Agents
Extracts real data from various services to create training datasets.
"""

import asyncio
from typing import List, Dict, Any, Optional
from datetime import datetime, timezone
from dataclasses import dataclass, field
import json

@dataclass
class TrainingExample:
    input_text: str
    expected_output: str
    context: Dict[str, Any] = field(default_factory=dict)
    source: str = ""
    quality_score: float = 0.0

class TrainingDataGenerator:
    """Generates training data for AI agents from various sources."""
    
    def __init__(self, tenant_id: str):
        self.tenant_id = tenant_id
        self.sources = {
            'tickets': self._generate_ticket_data,
            'knowledge': self._generate_knowledge_data,
            'sales': self._generate_sales_data,
            'customers': self._generate_customer_data,
            'agents': self._generate_agent_data,
        }
    
    async def generate_ticket_training_data(self, count: int = 100) -> List[TrainingExample]:
        """Generate training data from support ticket patterns."""
        examples = []
        
        ticket_templates = [
            {
                'input': "Customer says: 'My order hasn't arrived yet'",
                'output': "I understand your order hasn't arrived. Let me check the shipping status and provide you with tracking information.",
                'context': {'intent': 'order_status', 'urgency': 'medium'}
            },
            {
                'input': "Customer says: 'I need to return this product'",
                'output': "I can help you with that return. Please provide your order number and I'll initiate the return process for you.",
                'context': {'intent': 'return', 'urgency': 'low'}
            },
            {
                'input': "Customer says: 'The login button isn't working'",
                'output': "I apologize for the inconvenience. Let's troubleshoot this together. Can you try clearing your browser cache or try a different browser?",
                'context': {'intent': 'technical_issue', 'urgency': 'high'}
            },
            {
                'input': "Customer says: 'What are your business hours?'",
                'output': "Our customer support is available Monday through Friday, 9 AM to 6 PM EST. We're here to help if you need assistance!",
                'context': {'intent': 'faq', 'urgency': 'low'}
            },
            {
                'input': "Customer says: 'I was charged twice'",
                'output': "I'm very sorry to hear about this issue. I've flagged this as urgent and will connect you with our billing team immediately to resolve this.",
                'context': {'intent': 'billing', 'urgency': 'critical'}
            }
        ]
        
        for i in range(count):
            template = ticket_templates[i % len(ticket_templates)]
            examples.append(TrainingExample(
                input_text=template['input'],
                expected_output=template['output'],
                context=template['context'],
                source='tickets',
                quality_score=0.9
            ))
        
        return examples
    
    async def generate_knowledge_training_data(self, count: int = 100) -> List[TrainingExample]:
        """Generate training data from knowledge base content."""
        examples = []
        
        kb_templates = [
            {
                'input': "What is your refund policy?",
                'output': "We offer a 30-day money-back guarantee. If you're not satisfied with our product, contact our support team within 30 days of purchase for a full refund.",
                'context': {'category': 'refunds', 'intent': 'policy_question'}
            },
            {
                'input': "How do I reset my password?",
                'output': "You can reset your password by clicking 'Forgot Password' on the login page, then enter your email address to receive a reset link.",
                'context': {'category': 'account', 'intent': 'password'}
            },
            {
                'input': "Do you offer international shipping?",
                'output': "Yes, we ship worldwide. Shipping times and costs vary based on your location. You can view estimated delivery times during checkout.",
                'context': {'category': 'shipping', 'intent': 'shipping_question'}
            },
            {
                'input': "What payment methods do you accept?",
                'output': "We accept all major credit cards (Visa, Mastercard, American Express), PayPal, Apple Pay, and Google Pay for secure transactions.",
                'context': {'category': 'payments', 'intent': 'payment_question'}
            }
        ]
        
        for i in range(count):
            template = kb_templates[i % len(kb_templates)]
            examples.append(TrainingExample(
                input_text=template['input'],
                expected_output=template['output'],
                context=template['context'],
                source='knowledge',
                quality_score=0.95
            ))
        
        return examples
    
    async def generate_sales_training_data(self, count: int = 100) -> List[TrainingExample]:
        """Generate training data for sales conversations."""
        examples = []
        
        sales_templates = [
            {
                'input': "Lead: 'I\'m interested in learning more about your product'",
                'output': "That's great to hear! I'd love to show you how our platform can help automate your customer support. Would you prefer a quick demo now or should I send you a calendar link?",
                'context': {'stage': 'interest', 'intent': 'demo_request'}
            },
            {
                'input': "Lead: 'What\'s the pricing like?'",
                'output': "Our pricing starts at $49 per month for up to 10,000 interactions. We also have Enterprise plans with custom pricing. Would you like me to email you a detailed pricing sheet?",
                'context': {'stage': 'research', 'intent': 'pricing'}
            },
            {
                'input': "Lead: 'I already have a support system'",
                'output': "I understand. I'd love to find out what you're currently using so we can highlight areas where our AI assistant could save you time. What solution are you using today?",
                'context': {'stage': 'comparison', 'intent': 'competition_analysis'}
            },
            {
                'input': "Lead: 'Can I integrate this with my CRM?'",
                'output': "Absolutely! We integrate seamlessly with Salesforce, HubSpot, Pipedrive, and Zoho CRM. Which CRM are you using? I can show you the exact integration steps.",
                'context': {'stage': 'integration', 'intent': 'crm_integration'}
            }
        ]
        
        for i in range(count):
            template = sales_templates[i % len(sales_templates)]
            examples.append(TrainingExample(
                input_text=template['input'],
                expected_output=template['output'],
                context=template['context'],
                source='sales',
                quality_score=0.9
            ))
        
        return examples
    
    async def _generate_ticket_data(self, count: int) -> List[TrainingExample]:
        return await self.generate_ticket_training_data(count)
    
    async def _generate_knowledge_data(self, count: int) -> List[TrainingExample]:
        return await self.generate_knowledge_training_data(count)
    
    async def _generate_sales_data(self, count: int) -> List[TrainingExample]:
        return await self.generate_sales_training_data(count)
    
    async def _generate_customer_data(self, count: int) -> List[TrainingExample]:
        """Generate training data based on customer profiles and interactions."""
        examples = []
        # Customer-specific training would require actual customer data
        # This is a placeholder for more sophisticated data extraction
        return examples
    
    async def _generate_agent_data(self, count: int) -> List[TrainingExample]:
        """Generate training data from agent outputs and corrections."""
        examples = []
        # Would extract from conversation logs where agents were corrected
        return examples
    
    async def generate_all_training_data(
        self, 
        ticket_count: int = 100,
        knowledge_count: int = 100,
        sales_count: int = 50
    ) -> List[TrainingExample]:
        """Generate comprehensive training data from all sources."""
        all_examples = []
        
        tasks = [
            self.generate_ticket_training_data(ticket_count),
            self.generate_knowledge_training_data(knowledge_count),
            self.generate_sales_training_data(sales_count),
        ]
        
        results = await asyncio.gather(*tasks)
        
        for examples in results:
            all_examples.extend(examples)
        
        return all_examples
    
    def export_training_batch(
        self, 
        examples: List[TrainingExample], 
        format: str = 'json'
    ) -> str:
        """Export training examples in the specified format."""
        data = [
            {
                'input': ex.input_text,
                'output': ex.expected_output,
                'context': ex.context,
                'source': ex.source,
                'quality_score': ex.quality_score,
            }
            for ex in examples
        ]
        
        if format == 'json':
            return json.dumps(data, indent=2)
        elif format == 'csv':
            lines = ['input,output,source,quality_score']
            for ex in examples:
                lines.append(f'"{ex.input_text}","{ex.expected_output}","{ex.source}",{ex.quality_score}')
            return '\n'.join(lines)
        else:
            raise ValueError(f"Unsupported format: {format}")


# Data quality validator
class DataQualityValidator:
    """Validates and scores training data quality."""
    
    @staticmethod
    def validate_example(example: TrainingExample) -> Dict[str, Any]:
        """Validate a training example and return quality metrics."""
        issues = []
        score = 1.0
        
        # Check input length
        if len(example.input_text) < 10:
            issues.append("Input text too short")
            score -= 0.2
        elif len(example.input_text) > 2000:
            issues.append("Input text too long")
            score -= 0.1
        
        # Check output length
        if len(example.expected_output) < 10:
            issues.append("Output text too short")
            score -= 0.2
        
        # Check for balanced context (for training)
        if len(example.context) > 10:
            issues.append("Too much context")
            score -= 0.1
        
        # Check for profanity/harmful content (basic check)
        harmful_keywords = ['spam', 'scam', 'malware', 'phishing']
        input_lower = example.input_text.lower()
        if any(keyword in input_lower for keyword in harmful_keywords):
            issues.append("Potential harmful content")
            score -= 0.5
        
        return {
            'valid': len(issues) == 0,
            'issues': issues,
            'quality_score': max(0.0, min(1.0, score)),
            'recommended_source': example.source
        }


async def main():
    """Generate training data for all agents in an organization."""
    tenant_id = "example-tenant"
    generator = TrainingDataGenerator(tenant_id)
    
    # Generate comprehensive training data
    training_data = await generator.generate_all_training_data(
        ticket_count=200,
        knowledge_count=150,
        sales_count=100
    )
    
    # Validate quality
    validator = DataQualityValidator()
    validated_data = []
    
    for example in training_data:
        result = validator.validate_example(example)
        if result['valid'] or result['quality_score'] > 0.7:
            example.quality_score = result['quality_score']
            validated_data.append(example)
    
    # Export for training
    json_data = generator.export_training_batch(validated_data, 'json')
    
    print(f"Generated {len(validated_data)} training examples")
    print(f"Average quality score: {sum(e.quality_score for e in validated_data) / len(validated_data):.2f}")
    
    return json_data


if __name__ == "__main__":
    asyncio.run(main())