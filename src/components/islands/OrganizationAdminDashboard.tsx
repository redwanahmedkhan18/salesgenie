import React, { useState, useEffect } from 'react';
import { useAuth } from '../../auth/AuthProvider';
import { apiClient } from '../../lib/api-client';
import KnowledgeBaseManager from './KnowledgeBaseManager';
import AIWorkflowManager from './AIWorkflowManager';
import ChannelIntegrator from './ChannelIntegrator';
import CRMApiManager from './CRMApiManager';

interface OrganizationAdminDashboardProps {
  initialTab?: string;
}

export default function OrganizationAdminDashboard({ initialTab = 'dashboard' }: OrganizationAdminDashboardProps) {
  const { user } = useAuth();
  const tenantId = user?.tenant_id;
  const [activeTab, setActiveTab] = useState(initialTab);
  const [loading, setLoading] = useState(true);
  const [tenantMetrics, setTenantMetrics] = useState<any>(null);

  useEffect(() => {
    if (tenantId) {
      loadData();
    }
  }, [tenantId]);

  const loadData = async () => {
    if (!tenantId) return;
    setLoading(true);
    try {
      const metrics = await apiClient.getTenantMetrics(tenantId);
      setTenantMetrics(metrics);
    } catch (error) {
      console.error('Failed to load tenant metrics:', error);
    } finally {
      setLoading(false);
    }
  };

  const tabs = [
    { id: 'dashboard', label: 'Dashboard', icon: '📊' },
    { id: 'tickets', label: 'Inbox', icon: '🎫' },
    { id: 'ai-agents', label: 'AI Agents', icon: '🤖' },
    { id: 'knowledge', label: 'Knowledge Base', icon: '📚' },
    { id: 'leads', label: 'Lead Intelligence', icon: '👤' },
    { id: 'crm', label: 'Sales CRM', icon: '💼' },
    { id: 'channels', label: 'Channels', icon: '🔗' },
    { id: 'workflows', label: 'Workflows', icon: '⚙️' },
    { id: 'analytics', label: 'Analytics', icon: '📈' },
    { id: 'team', label: 'Team Management', icon: '👥' },
    { id: 'roles', label: 'Roles & Permissions', icon: '🔐' },
    { id: 'integrations', label: 'Integrations', icon: '🔌' },
    { id: 'billing', label: 'Billing', icon: '💰' },
    { id: 'settings', label: 'Settings', icon: '⚙️' },
  ];

  if (loading) {
    return (
      <div className="flex h-screen items-center justify-center" style={{ background: 'var(--color-background)' }}>
        <div className="text-center">Loading organization dashboard...</div>
      </div>
    );
  }

  const renderContent = () => {
    switch (activeTab) {
      case 'dashboard':
        return (
          <div className="space-y-6">
            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4">
              <div className="p-4 rounded-xl" style={{ background: 'var(--color-card)', border: '1px solid var(--color-border)' }}>
                <div className="text-xs" style={{ color: 'var(--color-muted-foreground)' }}>Total Conversations</div>
                <div className="text-2xl font-bold" style={{ color: 'var(--color-foreground)' }}>{tenantMetrics?.total_conversations || 0}</div>
              </div>
              <div className="p-4 rounded-xl" style={{ background: 'var(--color-card)', border: '1px solid var(--color-border)' }}>
                <div className="text-xs" style={{ color: 'var(--color-muted-foreground)' }}>Active Conversations</div>
                <div className="text-2xl font-bold text-green-500">{tenantMetrics?.active_conversations || 0}</div>
              </div>
              <div className="p-4 rounded-xl" style={{ background: 'var(--color-card)', border: '1px solid var(--color-border)' }}>
                <div className="text-xs" style={{ color: 'var(--color-muted-foreground)' }}>AI Cost (Today)</div>
                <div className="text-2xl font-bold" style={{ color: 'var(--color-foreground)' }}>${tenantMetrics?.ai_cost_usd?.toFixed(2) || '0.00'}</div>
              </div>
              <div className="p-4 rounded-xl" style={{ background: 'var(--color-card)', border: '1px solid var(--color-border)' }}>
                <div className="text-xs" style={{ color: 'var(--color-muted-foreground)' }}>AI Accuracy</div>
                <div className="text-2xl font-bold text-blue-500">{tenantMetrics?.ai_accuracy_rate?.toFixed(1) || '0'}%</div>
              </div>
            </div>
          </div>
        );
      case 'knowledge':
        return <KnowledgeBaseManager tenantId={tenantId!} />;
      case 'ai-agents':
        return <AIWorkflowManager tenantId={tenantId!} />;
      case 'channels':
        return <ChannelIntegrator tenantId={tenantId!} />;
      case 'crm':
        return <CRMApiManager tenantId={tenantId!} />;
      default:
        return (
          <div className="rounded-xl p-6" style={{ background: 'var(--color-card)', border: '1px solid var(--color-border)' }}>
            <h3 className="font-semibold text-sm mb-3" style={{ color: 'var(--color-foreground)' }}>{tabs.find(t => t.id === activeTab)?.label}</h3>
            <p className="text-sm" style={{ color: 'var(--color-muted-foreground)' }}>
              Configuration page for {activeTab}. Feature will be implemented shortly.
            </p>
          </div>
        );
    }
  };

  return (
    <div className="flex h-screen overflow-hidden" style={{ background: 'var(--color-background)' }}>
      {/* Sidebar */}
      <div className="w-64 flex-shrink-0 border-r flex flex-col" 
        style={{ background: 'var(--color-card)', borderColor: 'var(--color-border)' }}>
        <div className="px-4 py-3 border-b" style={{ borderColor: 'var(--color-border)' }}>
          <h2 className="font-bold text-sm" style={{ color: 'var(--color-foreground)' }}>Organization Admin</h2>
        </div>
        <nav className="flex-1 overflow-y-auto p-3 space-y-1">
          {tabs.map(tab => (
            <button
              key={tab.id}
              onClick={() => setActiveTab(tab.id)}
              className={`w-full text-left flex items-center gap-3 px-3 py-2 text-sm rounded-lg transition-colors ${
                activeTab === tab.id ? 'bg-secondary/10' : 'hover:bg-secondary/5'
              }`}
              style={{ color: 'var(--color-foreground)' }}
            >
              <span>{tab.icon}</span>
              {tab.label}
            </button>
          ))}
        </nav>
      </div>

      {/* Main Content */}
      <main className="flex-1 overflow-y-auto">
        <div className="p-6 space-y-6">
          <div>
            <h1 className="text-2xl font-bold" style={{ color: 'var(--color-foreground)' }}>
              Organization Administration
            </h1>
            <p className="text-sm" style={{ color: 'var(--color-muted-foreground)' }}>
              Workspace: {user?.email || 'Admin'}
            </p>
          </div>

          {renderContent()}
        </div>
      </main>
    </div>
  );
}