import React from 'react';
import { useAuth } from '../auth/AuthProvider';
import Dashboard from '../components/islands/Dashboard';
import ConversationInbox from '../components/islands/ConversationInbox';
import SalesCRM from '../components/islands/SalesCRM';
import SupportTickets from '../components/islands/SupportTickets';
import KnowledgeBase from '../components/islands/KnowledgeBase';
import AgentBuilder from '../components/islands/AgentBuilder';
import AnalyticsDashboard from '../components/islands/AnalyticsDashboard';
import WorkflowBuilder from '../components/islands/WorkflowBuilder';
import SettingsAdmin from '../components/islands/SettingsAdmin';
import AuditLogs from '../components/islands/AuditLogs';
import PlatformDashboard from '../components/islands/SuperAdminDashboard';
import OrganizationDashboard from '../components/islands/OrganizationAdminDashboard';
import type { PlatformRole } from '../lib/types';

export function RoleDashboard() {
  const { roles, hasAnyRole, user } = useAuth();

  const renderDashboardByRole = (): React.ReactNode => {
    if (hasAnyRole(['super_admin', 'workspace_admin'])) {
      return <PlatformDashboard />;
    }

if (hasAnyRole(['org_admin'])) {
      return <OrganizationDashboard />;
    }

    if (hasAnyRole(['sales_manager', 'sales_agent'])) {
      return <SalesDashboard />;
    }

    if (hasAnyRole(['support_manager', 'support_agent'])) {
      return <SupportDashboard />;
    }

    if (hasAnyRole(['knowledge_manager'])) {
      return <KnowledgeDashboard />;
    }

    if (hasAnyRole(['auditor'])) {
      return <AuditorDashboard />;
    }

    return <EndUserDashboard />;
  };

  return (
    <div className="flex h-screen overflow-hidden" style={{ background: 'var(--color-background)' }}>
      <RoleBasedSidebar roles={roles} />
      <main className="flex-1 overflow-y-auto">
        {renderDashboardByRole()}
      </main>
    </div>
  );
}

function RoleBasedSidebar({ roles }: { roles: PlatformRole[] }) {
  const sidebarItems: Record<string, { label: string; icon: string; href: string; minRole: PlatformRole[] }[]> = {
    admin: [
      { label: 'Dashboard', icon: '⊡', href: '/app/dashboard', minRole: ['super_admin', 'workspace_admin', 'org_admin'] },
      { label: 'AI Agents', icon: '🤖', href: '/app/agents', minRole: ['super_admin', 'workspace_admin', 'org_admin', 'sales_manager', 'support_manager'] },
      { label: 'Analytics', icon: '📊', href: '/app/analytics', minRole: ['super_admin', 'workspace_admin', 'org_admin', 'sales_manager', 'support_manager', 'auditor'] },
      { label: 'Team & Roles', icon: '👥', href: '/app/team', minRole: ['super_admin', 'workspace_admin', 'org_admin'] },
      { label: 'Settings', icon: '⚙️', href: '/app/settings', minRole: ['super_admin', 'workspace_admin', 'org_admin'] },
      { label: 'Audit Logs', icon: '🔍', href: '/app/audit', minRole: ['super_admin', 'workspace_admin', 'auditor'] },
    ],
    sales: [
      { label: 'Sales Dashboard', icon: '⊡', href: '/app/dashboard', minRole: ['sales_manager', 'sales_agent'] },
      { label: 'Leads & CRM', icon: '💼', href: '/app/sales', minRole: ['sales_manager', 'sales_agent'] },
      { label: 'AI Agents', icon: '🤖', href: '/app/agents', minRole: ['sales_manager', 'sales_agent'] },
      { label: 'Knowledge Base', icon: '📚', href: '/app/knowledge', minRole: ['sales_manager', 'sales_agent'] },
      { label: 'Analytics', icon: '📊', href: '/app/analytics', minRole: ['sales_manager'] },
    ],
    support: [
      { label: 'Support Dashboard', icon: '⊡', href: '/app/dashboard', minRole: ['support_manager', 'support_agent'] },
      { label: 'Inbox', icon: '💬', href: '/app/conversations', minRole: ['support_manager', 'support_agent'] },
      { label: 'Tickets', icon: '🎫', href: '/app/support', minRole: ['support_manager', 'support_agent'] },
      { label: 'Knowledge Base', icon: '📚', href: '/app/knowledge', minRole: ['support_manager', 'support_agent'] },
      { label: 'Analytics', icon: '📊', href: '/app/analytics', minRole: ['support_manager'] },
    ],
  };

  const getVisibleItems = () => {
    const items: typeof sidebarItems.admin = [];
    if (roles.some(r => ['super_admin', 'workspace_admin', 'org_admin'].includes(r))) {
      items.push(...sidebarItems.admin);
    }
    if (roles.some(r => ['sales_manager', 'sales_agent'].includes(r))) {
      items.push(...sidebarItems.sales);
    }
    if (roles.some(r => ['support_manager', 'support_agent'].includes(r))) {
      items.push(...sidebarItems.support);
    }
    return items.filter(item => roles.some(r => item.minRole.includes(r)));
  };

  const visibleItems = getVisibleItems();

  return (
    <aside className="w-60 flex-shrink-0 border-r flex flex-col"
      style={{ background: 'var(--color-card)', borderRight: '1px solid var(--color-border)' }}>
      <div className="px-4 py-5 border-b" style={{ borderColor: 'var(--color-border)' }}>
        <div className="w-8 h-8 rounded-lg flex items-center justify-center text-sm font-bold"
          style={{ background: 'var(--color-primary)', color: 'var(--color-on-primary)' }}>SG</div>
        <div className="text-white font-bold text-sm mt-2">SalesGenie</div>
        <div className="text-xs mt-0.5" style={{ color: 'var(--color-muted-foreground)' }}>
          {roles.join(', ')}
        </div>
      </div>
      <nav className="flex-1 overflow-y-auto px-2 py-3 space-y-0.5">
        {visibleItems.map(item => (
          <a key={item.href} href={item.href}
            className="nav-item flex items-center gap-3 px-3 py-2 rounded-lg text-sm transition-colors"
            style={{ color: 'var(--color-foreground)' }}>
            <span>{item.icon}</span>
            <span>{item.label}</span>
          </a>
        ))}
      </nav>
    </aside>
  );
}

function SuperAdminDashboard() {
  return (
    <div className="p-6 space-y-6">
      <div className="flex items-center justify-between">
        <div>
          <h1 className="text-2xl font-bold" style={{ color: 'var(--color-foreground)' }}>Super Admin Dashboard</h1>
          <p className="text-sm mt-0.5" style={{ color: 'var(--color-muted-foreground)' }}>Full platform oversight and management</p>
        </div>
      </div>
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4">
        <div className="p-4 rounded-xl" style={{ background: 'var(--color-card)', border: '1px solid var(--color-border)' }}>
          <div className="text-2xl mb-2">🏢</div>
          <div className="text-xl font-bold" style={{ color: 'var(--color-foreground)' }}>12</div>
          <div className="text-xs" style={{ color: 'var(--color-muted-foreground)' }}>Active Organizations</div>
        </div>
        <div className="p-4 rounded-xl" style={{ background: 'var(--color-card)', border: '1px solid var(--color-border)' }}>
          <div className="text-2xl mb-2">👥</div>
          <div className="text-xl font-bold" style={{ color: 'var(--color-foreground)' }}>4,281</div>
          <div className="text-xs" style={{ color: 'var(--color-muted-foreground)' }}>Total Users</div>
        </div>
        <div className="p-4 rounded-xl" style={{ background: 'var(--color-card)', border: '1px solid var(--color-border)' }}>
          <div className="text-2xl mb-2">🤖</div>
          <div className="text-xl font-bold" style={{ color: 'var(--color-foreground)' }}>99.99%</div>
          <div className="text-xs" style={{ color: 'var(--color-muted-foreground)' }}>Platform Uptime</div>
        </div>
        <div className="p-4 rounded-xl" style={{ background: 'var(--color-card)', border: '1px solid var(--color-border)' }}>
          <div className="text-2xl mb-2">💰</div>
          <div className="text-xl font-bold" style={{ color: 'var(--color-foreground)' }}>$2.4M</div>
          <div className="text-xs" style={{ color: 'var(--color-muted-foreground)' }}>Monthly Revenue</div>
        </div>
      </div>
    </div>
  );
}

function OrgAdminDashboard() {
  return (
    <div className="flex-1 overflow-y-auto">
      <OrganizationDashboard />
    </div>
  );
}

function SalesDashboard() {
  return (
    <div className="p-6 space-y-6">
      <div className="flex items-center justify-between">
        <div>
          <h1 className="text-2xl font-bold" style={{ color: 'var(--color-foreground)' }}>Sales Dashboard</h1>
          <p className="text-sm mt-0.5" style={{ color: 'var(--color-muted-foreground)' }}>Track performance, manage leads, and close deals</p>
        </div>
      </div>
      <SalesCRM />
    </div>
  );
}

function SupportDashboard() {
  return (
    <div className="p-6 space-y-6">
      <div className="flex items-center justify-between">
        <div>
          <h1 className="text-2xl font-bold" style={{ color: 'var(--color-foreground)' }}>Support Dashboard</h1>
          <p className="text-sm mt-0.5" style={{ color: 'var(--color-muted-foreground)' }}>Manage tickets, provide assistance, track satisfaction</p>
        </div>
      </div>
      <SupportTickets />
    </div>
  );
}

function KnowledgeDashboard() {
  return (
    <div className="p-6 space-y-6">
      <div className="flex items-center justify-between">
        <div>
          <h1 className="text-2xl font-bold" style={{ color: 'var(--color-foreground)' }}>Knowledge Management</h1>
          <p className="text-sm mt-0.5" style={{ color: 'var(--color-muted-foreground)' }}>Manage documents, embeddings, and search indexes</p>
        </div>
      </div>
      <KnowledgeBase />
    </div>
  );
}

function AuditorDashboard() {
  return (
    <div className="p-6 space-y-6">
      <div className="flex items-center justify-between">
        <div>
          <h1 className="text-2xl font-bold" style={{ color: 'var(--color-foreground)' }}>Security Audit Dashboard</h1>
          <p className="text-sm mt-0.5" style={{ color: 'var(--color-muted-foreground)' }}>Audit logs, compliance reports, and security monitoring</p>
        </div>
      </div>
      <AuditLogs />
    </div>
  );
}

function EndUserDashboard() {
  return (
    <div className="p-6 space-y-6">
      <div className="flex items-center justify-between">
        <div>
          <h1 className="text-2xl font-bold" style={{ color: 'var(--color-foreground)' }}>Customer Portal</h1>
          <p className="text-sm mt-0.5" style={{ color: 'var(--color-muted-foreground)' }}>Access support, knowledge base, and AI assistance</p>
        </div>
      </div>
      <ConversationInbox />
    </div>
  );
}
