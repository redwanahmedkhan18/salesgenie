import React, { useState, useEffect } from 'react';
import { apiClient, type SupportTicket, type TicketAnalytics, type TicketNote } from '../../lib/api-client';

const STATUS_COLORS: Record<string, string> = {
  open: '#2c84e0', in_progress: '#f7a501', pending: '#7c44a6',
  resolved: '#2c8c66', closed: '#6c6e63', reopened: '#cd4239',
};

const PRIORITY_COLORS: Record<string, string> = {
  low: '#6c6e63', medium: '#2c84e0', high: '#f7a501', urgent: '#cd4239', critical: '#dc2626',
};

export default function SupportManagerDashboard() {
  const [activeTab, setActiveTab] = useState<'overview' | 'tickets' | 'team'>('overview');
  const [tickets, setTickets] = useState<SupportTicket[]>([]);
  const [analytics, setAnalytics] = useState<TicketAnalytics | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const [search, setSearch] = useState('');
  const [selectedTicket, setSelectedTicket] = useState<SupportTicket | null>(null);
  const [notes, setNotes] = useState<TicketNote[]>([]);

  useEffect(() => {
    loadData();
  }, []);

  const loadData = async () => {
    setLoading(true);
    setError(null);
    try {
      const [ticketData, analyticsData] = await Promise.all([
        apiClient.fetchSupportTickets(),
        apiClient.fetchTeamMetrics(),
      ]);
      setTickets(Array.isArray(ticketData) ? ticketData : []);
      setAnalytics(analyticsData);
    } catch (err: any) {
      setError(err.message || 'Failed to load data');
    } finally {
      setLoading(false);
    }
  };

  const handleStatusChange = async (ticketId: string, newStatus: string) => {
    const updated = await apiClient.updateSupportTicket(ticketId, { status: newStatus });
    if (updated) {
      setTickets(tickets.map(t => t.id === ticketId ? updated : t));
      if (selectedTicket?.id === ticketId) setSelectedTicket(updated);
    }
  };

  const handleAssign = async (ticketId: string) => {
    const updated = await apiClient.assignTicketToSelf(ticketId);
    if (updated) {
      setTickets(tickets.map(t => t.id === ticketId ? updated : t));
    }
  };

  const handleViewTicket = async (ticket: SupportTicket) => {
    setSelectedTicket(ticket);
    const noteData = await apiClient.fetchTicketNotes(ticket.id);
    if (noteData) setNotes(Array.isArray(noteData) ? noteData : []);
  };

  const handleAddNote = async (content: string, isInternal: boolean) => {
    if (!selectedTicket) return;
    const note = await apiClient.addTicketNote(selectedTicket.id, { content, is_internal: isInternal });
    if (note) {
      setNotes([...notes, note]);
    }
  };

  const filteredTickets = tickets.filter(t =>
    search === '' ||
    t.title.toLowerCase().includes(search.toLowerCase()) ||
    t.description.toLowerCase().includes(search.toLowerCase())
  );

  const statusCount = (status: string) => tickets.filter(t => t.status === status).length;
  const priorityCount = (priority: string) => tickets.filter(t => t.priority === priority).length;

  return (
    <div className="space-y-6">
      <div className="flex items-center justify-between">
        <div>
          <h1 className="text-2xl font-bold" style={{ color: 'var(--color-foreground)' }}>Support Manager Dashboard</h1>
          <p className="text-sm mt-0.5" style={{ color: 'var(--color-muted-foreground)' }}>Team oversight, ticket management, analytics & escalation handling</p>
        </div>
        {error && (
          <div className="text-xs px-3 py-2 rounded" style={{ background: 'rgba(205,66,59,0.15)', color: '#cd4239' }}>
            {error}
          </div>
        )}
      </div>

      <div className="border-b" style={{ borderColor: 'var(--color-border)' }}>
        <div className="flex gap-6">
          {['overview', 'tickets', 'team'].map((tab, i) => (
            <button
              key={tab}
              onClick={() => { setActiveTab(tab as any); setSelectedTicket(null); }}
              className={`pb-3 px-1 text-sm font-medium capitalize transition-colors ${
                activeTab === tab ? 'border-b-2' : ''
              }`}
              style={{
                borderColor: activeTab === tab ? 'var(--color-primary)' : 'transparent',
                color: activeTab === tab ? 'var(--color-primary)' : 'var(--color-muted-foreground)',
              }}
            >
              {tab === 'overview' ? 'Team Overview' : tab === 'tickets' ? 'All Tickets' : 'Agent Roster'}
            </button>
          ))}
        </div>
      </div>

      {loading ? (
        <div className="text-center py-8" style={{ color: 'var(--color-muted-foreground)' }}>Loading...</div>
      ) : null}

      {activeTab === 'overview' && analytics && (
        <div className="grid grid-cols-2 md:grid-cols-5 gap-4">
          <div className="p-4 rounded-xl" style={{ background: 'var(--color-card)', border: '1px solid var(--color-border)' }}>
            <div className="text-xs" style={{ color: 'var(--color-muted-foreground)' }}>Total Tickets</div>
            <div className="text-2xl font-bold mt-1" style={{ color: 'var(--color-foreground)' }}>{analytics.total_tickets}</div>
          </div>
          <div className="p-4 rounded-xl" style={{ background: 'var(--color-card)', border: '1px solid var(--color-border)' }}>
            <div className="text-xs" style={{ color: 'var(--color-muted-foreground)' }}>Open</div>
            <div className="text-2xl font-bold mt-1" style={{ color: '#2c84e0' }}>{analytics.open_tickets}</div>
          </div>
          <div className="p-4 rounded-xl" style={{ background: 'var(--color-card)', border: '1px solid var(--color-border)' }}>
            <div className="text-xs" style={{ color: 'var(--color-muted-foreground)' }}>In Progress</div>
            <div className="text-2xl font-bold mt-1" style={{ color: '#f7a501' }}>{analytics.in_progress_tickets}</div>
          </div>
          <div className="p-4 rounded-xl" style={{ background: 'var(--color-card)', border: '1px solid var(--color-border)' }}>
            <div className="text-xs" style={{ color: 'var(--color-muted-foreground)' }}>Resolved</div>
            <div className="text-2xl font-bold mt-1" style={{ color: '#2c8c66' }}>{analytics.resolved_tickets}</div>
          </div>
          <div className="p-4 rounded-xl" style={{ background: 'var(--color-card)', border: '1px solid var(--color-border)' }}>
            <div className="text-xs" style={{ color: 'var(--color-muted-foreground)' }}>Escalation Rate</div>
            <div className="text-2xl font-bold mt-1" style={{ color: '#cd4239' }}>{analytics.escalation_rate.toFixed(1)}%</div>
          </div>
        </div>
      )}

      {activeTab === 'tickets' && !loading && (
        <div className="space-y-4">
          <div className="flex justify-between items-center">
            <input
              type="text" placeholder="Search tickets..." value={search} onChange={e => setSearch(e.target.value)}
              className="px-3 py-2 rounded border text-sm"
              style={{ background: 'var(--color-card)', borderColor: 'var(--color-border)', color: 'var(--color-foreground)' }}
            />
          </div>
          <div className="rounded-xl border" style={{ background: 'var(--color-card)', borderColor: 'var(--color-border)' }}>
            <table className="w-full text-sm">
              <thead>
                <tr style={{ borderBottom: '1px solid var(--color-border)' }}>
                  <th className="text-left px-4 py-3 text-xs" style={{ color: 'var(--color-muted-foreground)' }}>Ticket</th>
                  <th className="text-left px-4 py-3 text-xs" style={{ color: 'var(--color-muted-foreground)' }}>Priority</th>
                  <th className="text-left px-4 py-3 text-xs" style={{ color: 'var(--color-muted-foreground)' }}>Status</th>
                  <th className="text-left px-4 py-3 text-xs" style={{ color: 'var(--color-muted-foreground)' }}>Assigned</th>
                  <th className="text-left px-4 py-3 text-xs" style={{ color: 'var(--color-muted-foreground)' }}>Created</th>
                  <th className="text-left px-4 py-3 text-xs" style={{ color: 'var(--color-muted-foreground)' }}>Actions</th>
                </tr>
              </thead>
              <tbody>
                {filteredTickets.map(t => (
                  <tr key={t.id} style={{ borderBottom: '1px solid var(--color-border)' }}>
                    <td className="px-4 py-3">
                      <div className="font-semibold text-xs" style={{ color: 'var(--color-foreground)' }}>{t.title}</div>
                      <div className="text-xs" style={{ color: 'var(--color-muted-foreground)' }}>{t.description.substring(0, 60)}...</div>
                    </td>
                    <td className="px-4 py-3">
                      <span className="text-xs px-2 py-0.5 rounded"
                        style={{ background: `${PRIORITY_COLORS[t.priority] || PRIORITY_COLORS.medium}20`, color: PRIORITY_COLORS[t.priority] || PRIORITY_COLORS.medium }}>
                        {t.priority}
                      </span>
                    </td>
                    <td className="px-4 py-3">
                      <span className="text-xs px-2 py-0.5 rounded-full"
                        style={{ background: `${STATUS_COLORS[t.status] || '#9b9c92'}20`, color: STATUS_COLORS[t.status] || '#9b9c92' }}>
                        {t.status}
                      </span>
                    </td>
                    <td className="px-4 py-3 text-xs" style={{ color: 'var(--color-foreground)' }}>
                      {t.assigned_to ? t.assigned_to.slice(0, 8) : '—'}
                    </td>
                    <td className="px-4 py-3 text-xs" style={{ color: 'var(--color-muted-foreground)' }}>
                      {new Date(t.created_at).toLocaleDateString()}
                    </td>
                    <td className="px-4 py-3">
                      <button
                        onClick={() => handleViewTicket(t)}
                        className="text-xs px-2 py-1 rounded"
                        style={{ background: 'rgba(44,132,224,0.15)', color: '#2c84e0' }}
                      >
                        View
                      </button>
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </div>
      )}

      {activeTab === 'team' && (
        <div className="text-center py-8" style={{ color: 'var(--color-muted-foreground)' }}>
          Agent roster will be available when user management service is integrated.
        </div>
      )}

      {selectedTicket && (
        <TicketDetailModal
          ticket={selectedTicket}
          notes={notes}
          onClose={() => setSelectedTicket(null)}
          onStatusChange={handleStatusChange}
          onAddNote={handleAddNote}
        />
      )}
    </div>
  );
}

interface TicketDetailModalProps {
  ticket: SupportTicket;
  notes: TicketNote[];
  onClose: () => void;
  onStatusChange: (ticketId: string, status: string) => void;
  onAddNote: (content: string, isInternal: boolean) => void;
}

function TicketDetailModal({ ticket, notes, onClose, onStatusChange, onAddNote }: TicketDetailModalProps) {
  const [status, setStatus] = useState(ticket.status);
  const [noteContent, setNoteContent] = useState('');
  const [isInternal, setIsInternal] = useState(true);

  const handleStatusSave = () => {
    onStatusChange(ticket.id, status);
  };

  const handleNoteSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    if (!noteContent.trim()) return;
    onAddNote(noteContent, isInternal);
    setNoteContent('');
  };

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center bg-black/50 backdrop-blur-sm">
      <div className="bg-card rounded-xl max-w-3xl w-full max-h-[85vh] overflow-y-auto border"
        style={{ borderColor: 'var(--color-border)' }}>
        <div className="flex items-center justify-between p-6 border-b" style={{ borderColor: 'var(--color-border)' }}>
          <h2 className="text-lg font-bold" style={{ color: 'var(--color-foreground)' }}>{ticket.title}</h2>
          <button onClick={onClose} className="text-muted" style={{ color: 'var(--color-muted-foreground)' }}>&times;</button>
        </div>
        <div className="p-6 space-y-4">
          <div>
            <label className="text-xs uppercase" style={{ color: 'var(--color-muted-foreground)' }}>Description</label>
            <div className="mt-1 text-sm" style={{ color: 'var(--color-foreground)' }}>{ticket.description}</div>
          </div>
          <div>
            <label className="text-xs uppercase" style={{ color: 'var(--color-muted-foreground)' }}>Status</label>
            <select value={status} onChange={e => setStatus(e.target.value)}
              className="mt-1 w-full px-3 py-2 rounded border text-sm"
              style={{ background: '#1e293b', borderColor: 'var(--color-border)', color: 'var(--color-foreground)' }}>
              <option value="open">Open</option>
              <option value="in_progress">In Progress</option>
              <option value="pending">Pending</option>
              <option value="resolved">Resolved</option>
              <option value="closed">Closed</option>
              <option value="reopened">Reopened</option>
            </select>
            <button onClick={handleStatusSave} className="mt-2 px-3 py-1.5 text-xs rounded"
              style={{ background: 'var(--color-primary)', color: 'var(--color-on-primary)' }}>
              Save Status
            </button>
          </div>
          <div>
            <label className="text-xs uppercase" style={{ color: 'var(--color-muted-foreground)' }}>Notes</label>
            <div className="mt-2 space-y-2 max-h-48 overflow-y-auto">
              {notes.map(n => (
                <div key={n.id} className="p-3 rounded border text-sm"
                  style={{ background: '#1e293b', borderColor: 'var(--color-border)' }}>
                  <div className="flex items-center justify-between mb-1">
                    <span className="text-xs font-semibold" style={{ color: 'var(--color-foreground)' }}>
                      {n.author_type}
                    </span>
                    <span className={`text-xs px-1.5 py-0.5 rounded ${n.is_internal ? 'bg-orange-500/15 text-orange-400' : 'bg-gray-500/15 text-gray-400'}`}>
                      {n.is_internal ? 'Internal' : 'Public'}
                    </span>
                  </div>
                  <div className="text-xs" style={{ color: 'var(--color-muted-foreground)' }}>{n.content}</div>
                </div>
              ))}
            </div>
          </div>
          <form onSubmit={handleNoteSubmit} className="space-y-3 pt-4 border-t" style={{ borderColor: 'var(--color-border)' }}>
            <div>
              <textarea value={noteContent} onChange={e => setNoteContent(e.target.value)}
                placeholder="Add a note..." rows={3}
                className="w-full px-3 py-2 rounded border text-sm resize-none"
                style={{ background: '#1e293b', borderColor: 'var(--color-border)', color: 'var(--color-foreground)' }} />
            </div>
            <div className="flex items-center gap-4">
              <label className="flex items-center gap-2 text-xs" style={{ color: 'var(--color-muted-foreground)' }}>
                <input type="checkbox" checked={isInternal} onChange={e => setIsInternal(e.target.checked)} />
                Internal note
              </label>
            </div>
            <button type="submit" className="px-3 py-1.5 text-xs rounded"
              style={{ background: 'var(--color-primary)', color: 'var(--color-on-primary)' }}>
              Add Note
            </button>
          </form>
        </div>
      </div>
    </div>
  );
}
