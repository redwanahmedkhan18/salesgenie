"""SalesGenie AI Evaluation Framework - Model quality, drift detection, and performance monitoring"""

import logging
import re
from dataclasses import dataclass, field
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Any
from collections import defaultdict
import statistics

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("ai-evaluation")

@dataclass
class EvaluationMetric:
    """Single evaluation metric"""
    name: str
    value: float
    threshold: float
    direction: str  # "higher_is_better" or "lower_is_better"
    score: float = field(init=False)
    status: str = field(init=False)
    
    def __post_init__(self):
        if self.direction == "higher_is_better":
            self.score = min(1.0, self.value / self.threshold)
        else:
            self.score = max(0.0, 1.0 - (self.value / self.threshold))
        self.status = "pass" if self.score >= 0.8 else "fail"

@dataclass
class ConversationEvaluation:
    """Evaluation of a single conversation"""
    conversation_id: str
    agent_id: str
    model_version: str
    metrics: Dict[str, float]
    timestamp: datetime
    user_satisfaction: float = 0.0
    agent_response_time: float = 0.0
    context_relevance: float = 0.0
    factual_accuracy: float = 0.0
    toxicity_score: float = 0.0
    hallucination_score: float = 0.0
    cost_usd: float = 0.0

class ModelMonitor:
    """Monitor model performance and detect drift"""
    
    def __init__(self):
        self.model_stats: Dict[str, List[ConversationEvaluation]] = defaultdict(list)
        self.drift_threshold = 0.1
        self.performance_window_hours = 24
    
    async def evaluate_conversation(self, conv_id: str, agent_id: str, 
                                    user_input: str, agent_response: str,
                                    system_prompt: str, metrics: Optional[Dict] = None) -> ConversationEvaluation:
        """Evaluate a conversation turn"""
        
        evaluation = ConversationEvaluation(
            conversation_id=conv_id,
            agent_id=agent_id,
            model_version=os.environ.get('MODEL_VERSION', 'gpt-4'),
            metrics=metrics or {},
            timestamp=datetime.now(),
            agent_response_time=metrics.get('response_time', 0.0),
            context_relevance=self._calculate_relevance(user_input, agent_response),
            factual_accuracy=self._check_factual_accuracy(agent_response),
            toxicity_score=self._detect_toxicity(agent_response),
            hallucination_score=self._detect_hallucination(user_input, agent_response, system_prompt),
            cost_usd=metrics.get('cost', 0.0)
        )
        
        self.model_stats[agent_id].append(evaluation)
        return evaluation
    
    def _calculate_relevance(self, user_input: str, response: str) -> float:
        """Calculate response relevance"""
        user_words = set(user_input.lower().split())
        response_words = set(response.lower().split())
        
        if not user_words:
            return 1.0
        
        overlap = len(user_words & response_words)
        return min(1.0, overlap / len(user_words))
    
    def _check_factual_accuracy(self, response: str) -> float:
        """Check for factual accuracy indicators"""
        low_confidence_indicators = [
            'i think', 'maybe', 'possibly', 'seems like', 'might be',
            'according to my knowledge', 'as far as i know'
        ]
        
        response_lower = response.lower()
        low_confidence_count = sum(1 for ind in low_confidence_indicators if ind in response_lower)
        
        return max(0.0, 1.0 - (low_confidence_count * 0.1))
    
    def _detect_toxicity(self, response: str) -> float:
        """Simple toxicity detection"""
        toxic_patterns = [
            r'\b(hate|kill|destroy)\b',
            r'\b(die|stupid|idiot)\b',
            r'\b(shut up|go away)\b'
        ]
        
        toxic_count = 0
        for pattern in toxic_patterns:
            if re.search(pattern, response.lower()):
                toxic_count += 1
        
        return min(1.0, toxic_count * 0.3)
    
    def _detect_hallucination(self, user_input: str, response: str, system_prompt: str) -> float:
        """Detect potential hallucinations"""
        hallucination_indicators = [
            'i found', 'i searched', 'i checked', 'according to my database',
            'i have access to', 'looking at my records'
        ]
        
        response_lower = response.lower()
        user_lower = user_input.lower()
        
        if any(ind in response_lower for ind in hallucination_indicators):
            if 'knowledge base' not in user_lower and 'search' not in user_lower:
                return 0.7
        
        return 0.0

class ModelEvaluator:
    """Evaluate model performance across multiple dimensions"""
    
    def __init__(self, monitor: ModelMonitor):
        self.monitor = monitor
    
    def calculate_metrics(self, agent_id: str, window_hours: int = 24) -> Dict[str, Any]:
        """Calculate performance metrics for an agent"""
        evaluations = self.monitor.model_stats.get(agent_id, [])
        
        if not evaluations:
            return {'status': 'no_data'}
        
        cutoff = datetime.now() - timedelta(hours=window_hours)
        recent_evals = [e for e in evaluations if e.timestamp > cutoff]
        
        if not recent_evals:
            return {'status': 'no_recent_data'}
        
        avg_response_time = statistics.mean(e.agent_response_time for e in recent_evals)
        avg_relevance = statistics.mean(e.context_relevance for e in recent_evals)
        avg_accuracy = statistics.mean(e.factual_accuracy for e in recent_evals)
        max_toxicity = max(e.toxicity_score for e in recent_evals)
        avg_hallucination = statistics.mean(e.hallucination_score for e in recent_evals)
        total_cost = sum(e.cost_usd for e in recent_evals)
        
        return {
            'agent_id': agent_id,
            'evaluation_count': len(recent_evals),
            'avg_response_time_ms': avg_response_time,
            'avg_context_relevance': avg_relevance,
            'avg_factual_accuracy': avg_accuracy,
            'max_toxicity': max_toxicity,
            'avg_hallucination_score': avg_hallucination,
            'total_cost_usd': total_cost,
            'status': 'healthy' if avg_accuracy > 0.7 and max_toxicity < 0.3 else 'at_risk'
        }
    
    def detect_drift(self, agent_id: str) -> bool:
        """Detect performance drift"""
        evaluations = self.monitor.model_stats.get(agent_id, [])
        
        if len(evaluations) < 10:
            return False
        
        window_1 = evaluations[-20:-10]
        window_2 = evaluations[-10:]
        
        if not window_1 or not window_2:
            return False
        
        avg_relevance_1 = statistics.mean(e.context_relevance for e in window_1)
        avg_relevance_2 = statistics.mean(e.context_relevance for e in window_2)
        
        drift = abs(avg_relevance_2 - avg_relevance_1)
        return drift > self.monitor.drift_threshold
    
    def recommend_model(self, agent_id: str) -> str:
        """Recommend model version based on performance"""
        evals = self.monitor.model_stats.get(agent_id, [])
        
        if len(evals) < 5:
            return os.environ.get('DEFAULT_MODEL', 'gpt-4')
        
        recent = evals[-10:]
        avg_acc = statistics.mean(e.factual_accuracy for e in recent)
        
        if avg_acc < 0.6:
            return 'gpt-4-turbo'  # More accurate
        elif avg_acc > 0.9:
            return 'gpt-3.5-turbo'  # More cost-effective
        
        return os.environ.get('CURRENT_MODEL', 'gpt-4')

class QualityGate:
    """Quality gate for model deployments"""
    
    def __init__(self):
        self.min_accuracy = 0.85
        self.max_toxicity = 0.15
        self.max_hallucination = 0.10
        self.min_satisfaction = 4.0
    
    def pass_gate(self, metrics: Dict[str, Any]) -> bool:
        """Check if metrics pass quality gate"""
        checks = [
            ('accuracy', metrics.get('avg_factual_accuracy', 0) >= self.min_accuracy),
            ('toxicity', metrics.get('max_toxicity', 1) <= self.max_toxicity),
            ('hallucination', metrics.get('avg_hallucination_score', 1) <= self.max_hallucination),
        ]
        
        failed = [name for name, passed in checks if not passed]
        if failed:
            logger.warning("Quality gate failed: %s", failed)
            return False
        
        return True

# FastAPI Application
def create_app():
    from fastapi import FastAPI, HTTPException
    
    app = FastAPI(title="AI Evaluation Framework", version="1.0.0")
    monitor = ModelMonitor()
    evaluator = ModelEvaluator(monitor)
    gate = QualityGate()
    
    @app.post("/evaluate/conversation")
    async def evaluate(conv_id: str, agent_id: str, user_input: str, 
                      agent_response: str, system_prompt: str):
        eval_result = await monitor.evaluate_conversation(
            conv_id, agent_id, user_input, agent_response, system_prompt
        )
        return {'conversation_id': conv_id, 'metrics': eval_result.metrics}
    
    @app.get("/metrics/{agent_id}")
    async def get_metrics(agent_id: str, hours: int = 24):
        metrics = evaluator.calculate_metrics(agent_id, hours)
        return metrics
    
    @app.get("/health")
    async def health():
        return {"status": "healthy", "service": "ai-evaluation", "version": "1.0.0"}
    
    @app.get("/health/{agent_id}")
    async def health_check(agent_id: str):
        metrics = evaluator.calculate_metrics(agent_id)
        if 'status' in metrics and metrics['status'] == 'no_data':
            raise HTTPException(status_code=404, detail="Agent not found")
        return {'healthy': metrics['status'] != 'at_risk', 'metrics': metrics}
    
    @app.get("/drift/{agent_id}")
    async def check_drift(agent_id: str):
        return {'agent_id': agent_id, 'drift_detected': evaluator.detect_drift(agent_id)}
    
    @app.post("/gate/check")
    async def check_gate(metrics: Dict[str, Any]):
        return {'passed': gate.pass_gate(metrics)}
    
    return app

if __name__ == "__main__":
    import os
    app = create_app()
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8029)