import { useState, useRef, useEffect } from 'react';
import { ErrorBoundary } from '../ui/ErrorBoundary';
import { useAuth } from '../../auth/AuthProvider';
import { apiClient } from '../../lib/api-client';
import { get_structured_logger } from '../../lib/logger';

const logger = get_structured_logger('salesgenie.ai', 'AIAssistant');

interface Message {
  id: string;
  role: 'user' | 'assistant' | 'system';
  content: string;
  timestamp: Date;
  tool_calls?: ToolCall[];
  action_required?: boolean;
  action_type?: 'suspend_org' | 'create_org' | 'delete_org' | 'export_data' | 'change_billing';
  requires_approval?: boolean;
  approval_id?: string;
}

interface ToolCall {
  id: string;
  name: string;
  arguments: Record<string, unknown>;
  status: 'pending' | 'completed' | 'failed';
}

interface PlanningResult {
  steps: Array<{
    step: number;
    description: string;
    action: string;
    risk_level: 'low' | 'medium' | 'high';
    requires_approval: boolean;
    status: 'pending' | 'approved' | 'completed' | 'failed';
  }>;
  summary: string;
}

export function AIAssistantInner() {
  const { user } = useAuth();
  const [messages, setMessages] = useState<Message[]>([]);
  const [input, setInput] = useState('');
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [pendingApproval, setPendingApproval] = useState<PlanningResult | null>(null);
  const messagesEndRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    scrollToBottom();
  }, [messages]);

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  };

  const sendMessage = async () => {
    if (!input.trim()) return;

    const userMessage: Message = {
      id: Date.now().toString(),
      role: 'user',
      content: input,
      timestamp: new Date(),
    };

    setMessages(prev => [...prev, userMessage]);
    setInput('');

    setLoading(true);
    setError(null);

    try {
      const response = await apiClient.chat({
        messages: messages.map(m => ({ role: m.role, content: m.content })),
        model: 'gpt-4o-mini',
      });
      const assistantMessage: Message = {
        id: Date.now().toString() + '-assistant',
        role: 'assistant',
        content: response.choices[0]?.message?.content ?? 'No response received.',
        timestamp: new Date(),
      };
      setMessages(prev => [...prev, assistantMessage]);
    } catch (error) {
      logger.error('AI processing error', { error: String(error) });
      setError(error instanceof Error ? error.message : 'Failed to process AI request. Please try again.');
    } finally {
      setLoading(false);
    }
  };

  const handleApproval = (approved: boolean) => {
    if (!pendingApproval) return;

    if (approved) {
      setMessages(prev => [...prev, {
        id: Date.now().toString() + '-approved',
        role: 'assistant',
        content: 'Action approved. Executing via backend orchestration engine...',
        timestamp: new Date(),
      }]);
    } else {
      setMessages(prev => [...prev, {
        id: Date.now().toString() + '-rejected',
        role: 'assistant',
        content: '❌ Action cancelled by user.',
        timestamp: new Date(),
      }]);
    }
    
    setPendingApproval(null);
  };

  return (
    <div className="flex flex-col h-full">
      {/* Messages */}
      <div className="flex-1 overflow-y-auto p-4 space-y-4">
        {messages.length === 0 ? (
          <div className="text-center py-8">
            <div className="mb-4">
              <h3 className="font-bold text-lg" style={{ color: 'var(--color-foreground)' }}>AI Operations Assistant</h3>
              <p className="text-sm" style={{ color: 'var(--color-muted-foreground)' }}>
                Ask me to manage your platform, organizations, AI agents, and more.
              </p>
            </div>
            <div className="grid gap-2 max-w-md mx-auto">
              <button 
                onClick={() => setInput("Show me organizations with payment issues")}
                className="text-left text-sm p-2 rounded border"
                style={{ borderColor: 'var(--color-border)', color: 'var(--color-foreground)' }}
              >
                📊 Show organizations with payment issues
              </button>
              <button 
                onClick={() => setInput("Create a new Enterprise organization")}
                className="text-left text-sm p-2 rounded border"
                style={{ borderColor: 'var(--color-border)', color: 'var(--color-foreground)' }}
              >
                ✨ Create a new organization
              </button>
              <button 
                onClick={() => setInput("Why is Redis memory high?")}
                className="text-left text-sm p-2 rounded border"
                style={{ borderColor: 'var(--color-border)', color: 'var(--color-foreground)' }}
              >
                🔍 Diagnose performance issue
              </button>
              <button 
                onClick={() => setInput("Reduce OpenAI costs by 20%")}
                className="text-left text-sm p-2 rounded border"
                style={{ borderColor: 'var(--color-border)', color: 'var(--color-foreground)' }}
              >
                💰 Optimize AI costs
              </button>
            </div>
          </div>
        ) : (
          messages.map(msg => (
            <div key={msg.id} className="max-w-3xl">
              <div className="flex gap-3">
                <div className={`w-8 h-8 rounded-full flex items-center justify-center text-sm ${
                  msg.role === 'user' 
                    ? 'ml-auto bg-secondary/10' 
                    : 'bg-primary/10'
                }`}>
                  {msg.role === 'user' ? '👤' : '🤖'}
                </div>
                <div className={`flex-1 rounded-lg p-3 ${
                  msg.role === 'user' 
                    ? 'ml-auto bg-secondary/5' 
                    : 'bg-card'
                }`}>
                  <div className="whitespace-pre-wrap text-sm" style={{ color: 'var(--color-foreground)' }}>
                    {msg.content}
                  </div>
                  {msg.action_required && (
                    <div className="mt-3 p-3 rounded border" style={{ borderColor: '#f59e0b', backgroundColor: '#fffbeb' }}>
                      <div className="flex gap-2">
                        <button 
                          onClick={() => handleApproval(true)}
                          className="text-xs px-2 py-1 rounded"
                          style={{ backgroundColor: '#10b981', color: 'white' }}
                        >
                          Approve
                        </button>
                        <button 
                          onClick={() => handleApproval(false)}
                          className="text-xs px-2 py-1 rounded"
                          style={{ backgroundColor: '#ef4444', color: 'white' }}
                        >
                          Cancel
                        </button>
                      </div>
                    </div>
                  )}
                </div>
              </div>
            </div>
          ))
        )}
        {error && (
          <div className="bg-red-50 border border-red-200 rounded-lg p-3 mb-4">
            <p className="text-sm text-red-700">{error}</p>
          </div>
        )}
        {loading && (
          <div className="flex gap-3">
            <div className="w-8 h-8 rounded-full flex items-center justify-center bg-primary/10">
              🤖
            </div>
            <div className="bg-card rounded-lg p-3">
              <div className="flex gap-1">
                <span>•</span>
                <span className="animate-pulse">•</span>
                <span className="animate-pulse">•</span>
              </div>
            </div>
          </div>
        )}
        <div ref={messagesEndRef} />
      </div>

      {/* Input */}
      <div className="p-4 border-t" style={{ borderColor: 'var(--color-border)' }}>
        <form onSubmit={(e) => { e.preventDefault(); sendMessage(); }} className="flex gap-2">
          <input
            type="text"
            value={input}
            onChange={(e) => setInput(e.target.value)}
            placeholder="Ask me anything about your platform..."
            className="flex-1 px-3 py-2 rounded border text-sm"
            style={{ background: 'var(--color-card)', color: 'var(--color-foreground)', borderColor: 'var(--color-border)' }}
            disabled={loading}
          />
          <button
            type="submit"
            disabled={loading || !input.trim()}
            className="px-4 py-2 rounded text-sm font-semibold"
            style={{ background: 'var(--color-primary)', color: 'var(--color-on-primary)' }}
          >
            Send
          </button>
        </form>
        <div className="text-xs mt-2" style={{ color: 'var(--color-muted-foreground)' }}>
          AI can help with platform ops, but high-risk actions require approval. You're operating as {user?.email || 'Admin'}.
        </div>
      </div>
    </div>
  );
}

export default function AIAssistant() {
  return (
    <ErrorBoundary componentName="AIAssistant" fallback={<div className="p-4 text-center" style={{ color: 'var(--color-muted-foreground)' }}>AI Assistant unavailable</div>}>
      <AIAssistantInner />
    </ErrorBoundary>
  );
}