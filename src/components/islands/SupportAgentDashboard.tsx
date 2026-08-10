import React, { useState, useEffect } from 'react';
import { apiClient, type SupportTicket } from '../../lib/api-client';

const STATUS_COLORS: Record<string, string> = {
  open: '#2c84e0', in_progress: '#f7a501', pending: '#7c44a6',
  resolved: '#2c8c66', closed: '#6c6e63', reopened: '#cd4239',
};

const PRIORITY_COLORS: Record<string, string> = {
  low: '#6c6e63', medium: '#2c84e0', high: '#f7a501', urgent: '#cd4239', critical: '#dc2626',
};

export default function SupportAgentDashboard() {
  const [activeTab, setActiveTab] = useState<'my-tickets' | 'unassigned' | 'assigned'>('my-tickets');
  const [tickets, setTickets] = useState<SupportTicket[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const [selectedStatus, setSelectedStatus] = useState<string>('all');

  useEffect(() => {
    loadData();
  }, [activeTab]);

  const loadData = async () => {
    setLoading(true);
    setError(null);
    try {
      let data: SupportTicket[] = [];
      if (activeTab === 'my-tickets') {
        const status = selectedStatus !== 'all' ? selectedStatus : undefined;
        data = await apiClient.fetchMyTickets(status);
      } else if (activeTab === 'unassigned') {
        data = await apiClient.fetchUnassignedTickets();
      } else {
        data = await apiClient.fetchSupportTickets();
      }
      setTickets(Array.isArray(data) ? data : []);
    } catch (err: any) {
      setError(err.message || 'Failed to load data');
    } finally {
      setLoading(false);
    }
  };

  const handleAssign = async (ticketId: string) => {
    const updated = await apiClient.assignTicketToSelf(ticketId);
    if (updated) {
      setTickets(tickets.filter(t => t.id !== ticketId));
    }
  };

  const handleStatusChange = async (ticketId: string, newStatus: string) => {
    const updated = await apiClient.updateSupportTicket(ticketId, { status: newStatus });
    if (updated) {
      setTickets(tickets.map(t => t.id === ticketId ? updated : t));
    }
  };

  const handleStatusFilterChange = (status: string) => {
    setSelectedStatus(status);
    if (activeTab === 'my-tickets') {
      loadData();
    }
  };

  const openCount = tickets.filter(t => t.status === 'open' || t.status === 'in_progress').length;
  const resolvedCount = tickets.filter(t => t.status === 'resolved').length;

  return (
    <div className="space-y-6">
      <div className="flex items-center justify-between">
        <div>
          <h1 className="text-2xl font-bold" style={{ color: 'var(--color-foreground)' }}>Support Agent Dashboard</h1>
          <p className="text-sm mt-0.5" style={{ color: 'var(--color-muted-foreground)' }}>My assigned tickets, unassigned queue, and knowledge base assistance</p>
        </div>
        {error && (
          <div className="text-xs px-3 py-2 rounded" style={{ background: 'rgba(205,66,59,0.15)', color: '#cd4239' }}>
            {error}
          </div>
        )}
      </div>

      <div className="grid grid-cols-1 md:grid-cols-4 gap-4">
        <div className="p-4 rounded-xl" style={{ background: 'var(--color-card)', border: '1px solid var(--color-border)' }}>
          <div className="text-xs" style={{ color: 'var(--color-muted-foreground)' }}>Active Tickets</div>
          <div className="text-2xl font-bold mt-1" style={{ color: '#2c84e0' }}>{openCount}</div>
        </div>
        <div className="p-4 rounded-xl" style={{ background: 'var(--color-card)', border: '1px solid var(--color-border)' }}>
          <div className="text-xs" style={{ color: 'var(--color-muted-foreground)' }}>Resolved</div>
          <div className="text-2xl font-bold mt-1" style={{ color: '#2c8c66' }}>{resolvedCount}</div>
        </div>
        <div className="p-4 rounded-xl" style={{ background: 'var(--color-card)', border: '1px solid var(--color-border)' }}>
          <div className="text-xs" style={{ color: 'var(--color-muted-foreground)' }}>Escalated</div>
          <div className="text-2xl font-bold mt-1" style={{ color: '#cd4239' }}>{tickets.filter(t => t.is_escalated).length}</div>
        </div>
        <div className="p-4 rounded-xl" style={{ background: 'var(--color-card)', border: '1px solid var(--color-border)' }}>
          <div className="text-xs" style={{ color: 'var(--color-muted-foreground)' }}>Avg. Satisfaction</div>
          <div className="text-2xl font-bold mt-1" style={{ color: 'var(--color-foreground)' }}>
            {tickets.filter(t => t.satisfaction_score).length > 0
              ? (tickets.filter(t => t.satisfaction_score).reduce((s, t) => s + (t.satisfaction_score || 0), 0) /
                tickets.filter(t => t.satisfaction_score).length).toFixed(1)
              : '—'}
          </div>
        </div>
      </div>

      <div className="border-b" style={{ borderColor: 'var(--color-border)' }}>
        <div className="flex gap-6">
          {[
            { key: 'my-tickets', label: 'My Tickets' },
            { key: 'unassigned', label: 'Unassigned Queue' },
            { key: 'assigned', label: 'All Assigned' },
          ].map(tab => (
            <button
              key={tab.key}
              onClick={() => { setActiveTab(tab.key as any); setSelectedStatus('all'); }}
              className={`pb-3 px-1 text-sm font-medium transition-colors ${
                activeTab === tab.key ? 'border-b-2' : ''
              }`}
              style={{
                borderColor: activeTab === tab.key ? 'var(--color-primary)' : 'transparent',
                color: activeTab === tab.key ? 'var(--color-primary)' : 'var(--color-muted-foreground)',
              }}
            >
              {tab.label}
            </button>
          ))}
        </div>
        {activeTab === 'my-tickets' && (
          <div className="flex gap-4 mt-3">
            {['all', 'open', 'in_progress', 'resolved', 'closed'].map(s => (
              <button
                key={s}
                onClick={() => handleStatusFilterChange(s)}
                className={`pb-2 px-3 text-xs rounded capitalize transition-colors`}
                style={{
                  background: selectedStatus === s ? 'rgba(247,165,1,0.15)' : 'rgba(255,255,255,0.03)',
                  color: selectedStatus === s ? '#f7a501' : 'var(--color-muted-foreground)',
                }}
              >
                {s === 'all' ? 'All' : s}
              </button>
            ))}
          </div>
        )}
      </div>

      {loading ? (
        <div className="text-center py-8" style={{ color: 'var(--color-muted-foreground)' }}>Loading...</div>
      ) : (
        <div className="space-y-3">
          {tickets.map(t => (
            <div key={t.id} className="p-4 rounded-xl flex items-center justify-between"
              style={{ background: 'var(--color-card)', border: '1px solid var(--color-border)' }}>
              <div className="flex items-start gap-4">
                <div className="flex-1">
                  <div className="flex items-center gap-2">
                    <span className="text-xs font-semibold" style={{ color: 'var(--color-foreground)' }}>{t.title}</span>
                    <span className="text-xs px-1.5 py-0.5 rounded"
                      style={{ background: `${PRIORITY_COLORS[t.priority] || PRIORITY_COLORS.medium}20`, color: PRIORITY_COLORS[t.priority] || PRIORITY_COLORS.medium }}>
                      {t.priority}
                    </span>
                  </div>
                  <div className="text-xs mt-1" style={{ color: 'var(--color-muted-foreground)' }}>
                    {t.description.substring(0, 80)}...
                  </div>
                  <div className="flex items-center gap-4 mt-2 text-xs" style={{ color: 'var(--color-muted-foreground)' }}>
                    <span>Category: {t.category}</span>
                    <span>Created: {new Date(t.created_at).toLocaleDateString()}</span>
                  </div>
                </div>
              </div>
              <div className="flex items-center gap-3 flex-shrink-0">
                <select
                  value={t.status}
                  onChange={e => handleStatusChange(t.id, e.target.value)}
                  className="text-xs px-2 py-1 rounded border"
                  style={{ background: 'var(--color-background)', borderColor: 'var(--color-border)', color: 'var(--color-foreground)' }}
                >
                  <option value="open">Open</option>
                  <option value="in_progress">In Progress</option>
                  <option value="pending">Pending</option>
                  <option value="resolved">Resolved</option>
                  <option value="closed">Closed</option>
                  <option value="reopened">Reopened</option>
                </select>
                {t.assigned_to === null && (
                  <button
                    onClick={() => handleAssign(t.id)}
                    className="text-xs px-3 py-1.5 rounded"
                    style={{ background: 'var(--color-primary)', color: 'var(--color-on-primary)' }}
                  >
                    Assign to Me
                  </button>
                )}
              </div>
            </div>
          ))}
          {tickets.length === 0 && (
            <div className="text-center py-8" style={{ color: 'var(--color-muted-foreground)' }}>
              No tickets in this view
            </div>
          )}
        </div>
      )}
    </div>
  );
}
