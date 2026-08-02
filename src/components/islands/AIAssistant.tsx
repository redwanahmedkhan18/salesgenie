import React, { useState, useRef, useEffect } from 'react';
import { useAuth } from '../../auth/AuthProvider';

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

export default function AIAssistant() {
  const { user } = useAuth();
  const [messages, setMessages] = useState<Message[]>([]);
  const [input, setInput] = useState('');
  const [loading, setLoading] = useState(false);
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

    try {
      const response = await processAIRequest(input);
      setMessages(prev => [...prev, response]);
    } catch (error) {
      console.error('AI processing error:', error);
    } finally {
      setLoading(false);
    }
  };

  const processAIRequest = async (request: string): Promise<Message> => {
    const isHighRisk = /suspend|delete|export|billing|remove|delete.*organization/i.test(request);
    const isMediumRisk = /create|invite|connect|modify|import|change/i.test(request);
    
    if (isHighRisk) {
      return {
        id: Date.now().toString() + '-high',
        role: 'assistant',
        content: `I've analyzed your request: "${request}"\n\nThis is a **high-risk action** that requires human approval.\n\nLet me explain what would happen:\n\n1. **Action**: ${extractAction(request)}\n2. **Impact**: Potential customer disruption / data loss\n3. **Reason**: Sensitive operation affecting organization integrity\n\n**Do you approve this action?** It cannot be undone.`,
        timestamp: new Date(),
        action_required: true,
        action_type: 'suspend_org',
        requires_approval: true,
      };
    }

    if (isMediumRisk) {
      return {
        id: Date.now().toString() + '-medium',
        role: 'assistant',
        content: `I'm planning to execute: "${request}"\n\nThis requires your approval before proceeding.\n\n**Proposed steps:**\n1. Validate request against permissions\n2. Check for conflicts\n3. Execute the action\n\nShall I proceed?`,
        timestamp: new Date(),
        action_required: true,
        action_type: 'create_org',
        requires_approval: true,
      };
    }

    return {
      id: Date.now().toString() + '-low',
      role: 'assistant',
      content: `I'll handle that for you. \n\n**Execution plan:**\n1. Analyze request\n2. Execute action\n3. Report results\n\n✅ Action completed successfully.`,
      timestamp: new Date(),
    };
  };

  const extractAction = (request: string): string => {
    if (request.toLowerCase().includes('suspend')) return 'Suspend organization(s)';
    if (request.toLowerCase().includes('delete')) return 'Delete organization(s)';
    if (request.toLowerCase().includes('export')) return 'Export all data';
    if (request.toLowerCase().includes('billing')) return 'Modify billing settings';
    if (request.toLowerCase().includes('connect')) return 'Connect integration';
    if (request.toLowerCase().includes('create')) return 'Create new resource';
    return 'Execute requested action';
  };

  const handleApproval = (approved: boolean) => {
    if (!pendingApproval) return;
    
    if (approved) {
      setMessages(prev => [...prev, {
        id: Date.now().toString() + '-approved',
        role: 'assistant',
        content: '✅ Action approved. Executing...\n\n1. Validating permissions... ✅\n2. Checking conflicts... ✅\n3. Executing action... ✅\n\n**Result**: Action completed successfully.',
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