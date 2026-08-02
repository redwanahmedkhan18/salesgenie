import React, { useState, useEffect } from 'react';
import { apiClient } from '../../lib/api-client';
import type { AIAgent } from '../../lib/types';

interface AIWorkflowManagerProps {
  tenantId: string;
}

export default function AIWorkflowManager({ tenantId }: AIWorkflowManagerProps) {
  const [agents, setAgents] = useState<AIAgent[]>([]);
  const [loading, setLoading] = useState(true);
  const [showAddAgent, setShowAddAgent] = useState(false);
  const [newAgent, setNewAgent] = useState({
    name: '',
    type: 'support' as const,
    model: 'groq' as const,
    temperature: 0.7,
  });

  useEffect(() => {
    loadData();
  }, [tenantId]);

  const loadData = async () => {
    setLoading(true);
    try {
      const agentsRes = await apiClient.fetchAIAgents(tenantId);
      if (agentsRes) setAgents(agentsRes);
    } catch (error) {
      console.error('Failed to load AI agents:', error);
    } finally {
      setLoading(false);
    }
  };

  const handleAddAgent = async () => {
    if (!newAgent.name) return;
    
    try {
      await apiClient.createAIAgent({
        ...newAgent,
        tenant_id: tenantId,
      });
      setShowAddAgent(false);
      setNewAgent({ name: '', type: 'support', model: 'groq', temperature: 0.7 });
      loadData();
    } catch (error) {
      console.error('Failed to add AI agent:', error);
    }
  };

  if (loading) {
    return <div className="text-center py-8">Loading AI agents...</div>;
  }

  return (
    <div className="space-y-4">
      <div className="flex items-center justify-between">
        <h3 className="font-semibold text-sm" style={{ color: 'var(--color-foreground)' }}>AI Agents</h3>
        <button
          onClick={() => setShowAddAgent(true)}
          className="text-xs px-3 py-1 rounded"
          style={{ background: 'var(--color-primary)', color: 'var(--color-on-primary)' }}
        >
          Create Agent
        </button>
      </div>

      {/* Add Agent Modal */}
      {showAddAgent && (
        <div className="rounded-xl p-4" style={{ background: 'var(--color-card)', border: '1px solid var(--color-border)' }}>
          <h4 className="font-semibold mb-3">Create New AI Agent</h4>
          <div className="space-y-3">
            <input
              type="text"
              placeholder="Agent Name"
              value={newAgent.name}
              onChange={e => setNewAgent({ ...newAgent, name: e.target.value })}
              className="w-full px-3 py-2 rounded border"
              style={{ background: 'var(--color-card)', color: 'var(--color-foreground)', borderColor: 'var(--color-border)' }}
            />
            <select
              value={newAgent.type}
              onChange={e => setNewAgent({ ...newAgent, type: e.target.value as any })}
              className="w-full px-3 py-2 rounded border"
              style={{ background: 'var(--color-card)', color: 'var(--color-foreground)', borderColor: 'var(--color-border)' }}
            >
              <option value="support">Customer Support</option>
              <option value="sales">Sales Assistant</option>
              <option value="refund">Refund Agent</option>
              <option value="booking">Appointment Booking</option>
              <option value="hr">HR Assistant</option>
            </select>
            <select
              value={newAgent.model}
              onChange={e => setNewAgent({ ...newAgent, model: e.target.value as any })}
              className="w-full px-3 py-2 rounded border"
              style={{ background: 'var(--color-card)', color: 'var(--color-foreground)', borderColor: 'var(--color-border)' }}
            >
              <option value="groq">Groq</option>
              <option value="google">Google AI</option>
              <option value="mistral">Mistral AI</option>
            </select>
            <div>
              <label className="text-xs" style={{ color: 'var(--color-muted-foreground)' }}>Temperature: {newAgent.temperature}</label>
              <input
                type="range"
                min="0"
                max="1"
                step="0.1"
                value={newAgent.temperature}
                onChange={e => setNewAgent({ ...newAgent, temperature: parseFloat(e.target.value) })}
                className="w-full mt-1"
              />
            </div>
          </div>
          <div className="mt-4 flex gap-2">
            <button onClick={handleAddAgent} style={{ color: 'var(--color-on-primary)' }}>Create</button>
            <button onClick={() => setShowAddAgent(false)} style={{ color: 'var(--color-muted-foreground)' }}>Cancel</button>
          </div>
        </div>
      )}

      {/* Agents List */}
      <div className="rounded-xl border" style={{ background: 'var(--color-card)', borderColor: 'var(--color-border)' }}>
        <div className="p-4 border-b" style={{ borderColor: 'var(--color-border)' }}>
          <h4 className="font-semibold text-sm" style={{ color: 'var(--color-foreground)' }}>Agents</h4>
        </div>
        <div className="p-4">
          {agents.length > 0 ? (
            <div className="grid gap-3">
              {agents.map(agent => (
                <div key={agent.id} className="p-3 rounded" style={{ background: 'var(--color-card)', border: '1px solid var(--color-border)' }}>
                  <div className="flex items-center justify-between">
                    <div>
                      <div className="font-semibold text-sm" style={{ color: 'var(--color-foreground)' }}>{agent.name}</div>
                      <div className="text-xs" style={{ color: 'var(--color-muted-foreground)' }}>
                        {agent.type} • {agent.model} • Temp: {agent.temperature}
                      </div>
                    </div>
                    <span className={`px-2 py-0.5 text-xs rounded ${agent.is_active ? 'text-green-500' : 'text-red-500'}`}>
                      {agent.is_active ? 'Active' : 'Inactive'}
                    </span>
                  </div>
                </div>
              ))}
            </div>
          ) : (
            <p className="text-sm" style={{ color: 'var(--color-muted-foreground)' }}>No AI agents created yet.</p>
          )}
        </div>
      </div>
    </div>
  );
}