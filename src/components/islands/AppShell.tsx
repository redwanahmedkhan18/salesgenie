import React, { useState, useEffect, useRef, useCallback } from 'react';
import type { NavItem } from '../../lib/types';
import { useAuth } from '../../auth/AuthProvider';

const NAV_ITEMS: NavItem[] = [
  { id: 'dashboard',    label: 'Dashboard',        icon: '⊡', href: '/app/dashboard' },
  { id: 'inbox',        label: 'Conversation Inbox',icon: '💬', href: '/app/conversations',   badge: 12 },
  { id: 'agents',       label: 'AI Agent Builder',  icon: '🤖', href: '/app/agents' },
  { id: 'knowledge',    label: 'Knowledge Base',    icon: '📚', href: '/app/knowledge' },
  { id: 'tickets',      label: 'Ticket Center',     icon: '🎫', href: '/app/support',  badge: 3 },
  { id: 'leads',        label: 'Lead Intelligence', icon: '🔍', href: '/app/leads' },
  { id: 'sales',        label: 'Sales CRM',         icon: '💼', href: '/app/sales' },
  { id: 'analytics',   label: 'Analytics',          icon: '📊', href: '/app/analytics' },
  { id: 'workflows',    label: 'Workflow Automation',icon: '⚡', href: '/app/workflows' },
  { id: 'integrations', label: 'Integrations',      icon: '🔗', href: '/app/integrations' },
  { id: 'channels',     label: 'Channels',          icon: '📡', href: '/app/channels' },
  { id: 'widget',       label: 'Chat Widget',        icon: '💡', href: '/app/widget' },
  { id: 'billing',      label: 'Billing & Usage',   icon: '💳', href: '/app/billing' },
  { id: 'team',         label: 'Team & Roles',      icon: '👥', href: '/app/team' },
  { id: 'profile',      label: 'My Profile',        icon: '👤', href: '/app/profile' },
  { id: 'settings',     label: 'Settings',           icon: '⚙️', href: '/app/settings' },
];

interface SidebarProps {
  activeRoute: string;
  onRouteChange: (id: string) => void;
}

export function Sidebar({ activeRoute, onRouteChange }: SidebarProps) {
  const [collapsed, setCollapsed] = useState(false);
  const { user } = useAuth();

  return (
    <aside
      className={`flex flex-col h-full transition-all duration-300 ${collapsed ? 'w-16' : 'w-60'}`}
      style={{ background: 'var(--color-surface-dark)', borderRight: '1px solid rgba(255,255,255,0.08)' }}
    >
      {/* Logo */}
      <div className="flex items-center gap-3 px-4 py-5 border-b" style={{ borderColor: 'rgba(255,255,255,0.08)' }}>
        <div className="w-8 h-8 rounded-lg flex items-center justify-center text-sm font-bold flex-shrink-0"
          style={{ background: 'var(--color-primary)', color: 'var(--color-on-primary)' }}>
          SG
        </div>
        {!collapsed && (
          <div>
            <div className="text-white font-bold text-sm leading-tight">SalesGenie</div>
            <div className="text-xs" style={{ color: 'rgba(255,255,255,0.45)' }}>Enterprise AI Platform</div>
          </div>
        )}
        <button
          onClick={() => setCollapsed(!collapsed)}
          className="ml-auto text-white/40 hover:text-white/80 transition-colors"
          aria-label={collapsed ? 'Expand sidebar' : 'Collapse sidebar'}
        >
          {collapsed ? '→' : '←'}
        </button>
      </div>

      {/* Navigation */}
      <nav className="flex-1 overflow-y-auto px-2 py-3 space-y-0.5" role="navigation" aria-label="Main navigation">
        {NAV_ITEMS.map((item) => (
          <a
            key={item.id}
            href={item.href}
            className={`nav-item w-full text-left flex items-center gap-3 px-2 py-1.5 rounded transition-colors ${activeRoute === item.id ? 'active bg-secondary/10' : 'hover:bg-secondary/5'}`}
            title={collapsed ? item.label : undefined}
          >
            <span className="text-base flex-shrink-0">{item.icon}</span>
            {!collapsed && (
              <>
                <span className="flex-1 truncate">{item.label}</span>
                {item.badge !== undefined && item.badge > 0 && (
                  <span className="text-xs px-1.5 py-0.5 rounded-full font-bold flex-shrink-0"
                    style={{ background: 'var(--color-primary)', color: 'var(--color-on-primary)' }}>
                    {item.badge}
                  </span>
                )}
              </>
            )}
          </a>
        ))}
      </nav>

      {/* User Footer */}
      {!collapsed && (
        <div className="px-3 py-4 border-t" style={{ borderColor: 'rgba(255,255,255,0.08)' }}>
          <div className="flex items-center gap-3">
            <div className="w-8 h-8 rounded-full flex items-center justify-center text-xs font-bold flex-shrink-0"
              style={{ background: 'var(--color-primary)', color: 'var(--color-on-primary)' }}>
              {user?.email ? user.email[0].toUpperCase() : 'A'}
            </div>
            <div className="flex-1 min-w-0">
              <div className="text-white text-xs font-semibold truncate">
                {user?.full_name || user?.email || 'Admin User'}
              </div>
              <div className="text-xs truncate" style={{ color: 'rgba(255,255,255,0.45)' }}>
                {user?.email || 'admin@salesgenie.ai'}
              </div>
            </div>
          </div>
        </div>
      )}
    </aside>
  );
}

/* ─── Command Palette ─── */
interface CommandPaletteProps {
  open: boolean;
  onClose: () => void;
  onNavigate: (id: string) => void;
}

export function CommandPalette({ open, onClose, onNavigate }: CommandPaletteProps) {
  const [query, setQuery] = useState('');
  const inputRef = useRef<HTMLInputElement>(null);

  const filtered = NAV_ITEMS.filter(i =>
    i.label.toLowerCase().includes(query.toLowerCase())
  );

  useEffect(() => {
    if (open) {
      setTimeout(() => inputRef.current?.focus(), 50);
    } else {
      setQuery('');
    }
  }, [open]);

  if (!open) return null;

  return (
    <div className="command-palette" role="dialog" aria-label="Command palette" onClick={onClose}>
      <div
        className="w-full max-w-xl rounded-2xl shadow-2xl overflow-hidden"
        style={{ background: 'var(--color-surface-dark)', border: '1px solid rgba(255,255,255,0.12)' }}
        onClick={e => e.stopPropagation()}
      >
        <div className="flex items-center gap-3 px-4 py-4 border-b" style={{ borderColor: 'rgba(255,255,255,0.08)' }}>
          <span className="text-white/40">🔍</span>
          <input
            ref={inputRef}
            id="command-palette-input"
            type="text"
            placeholder="Search pages, actions, settings..."
            value={query}
            onChange={e => setQuery(e.target.value)}
            className="flex-1 bg-transparent text-white placeholder-white/40 outline-none text-sm"
          />
          <kbd className="text-xs px-2 py-0.5 rounded" style={{ background: 'rgba(255,255,255,0.08)', color: 'rgba(255,255,255,0.4)' }}>ESC</kbd>
        </div>
        <div className="max-h-80 overflow-y-auto py-2">
          {filtered.length === 0 ? (
            <p className="text-center py-6 text-sm" style={{ color: 'rgba(255,255,255,0.4)' }}>No results found</p>
          ) : (
            filtered.map(item => (
              <a
                key={item.id}
                href={item.href}
                onClick={onClose}
                className="w-full flex items-center gap-3 px-4 py-2.5 text-sm text-left hover:bg-white/6 transition-colors"
                style={{ color: 'rgba(255,255,255,0.75)' }}
              >
                <span>{item.icon}</span>
                <span>{item.label}</span>
              </a>
            ))
          )}
        </div>
      </div>
    </div>
  );
}
