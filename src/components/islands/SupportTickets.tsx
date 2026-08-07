import React, { useState, useEffect } from 'react';
import { Sidebar, CommandPalette } from './AppShell';
import { apiClient } from '../../lib/api-client';
import type { SupportTicket, TicketAnalytics } from '../../lib/api-client';

export default function SupportTickets() {
  const [activeRoute, setActiveRoute] = useState('tickets');
  const [paletteOpen, setPaletteOpen] = useState(false);
  const [tickets, setTickets] = useState<SupportTicket[]>([]);
  const [analytics, setAnalytics] = useState<TicketAnalytics | null>(null);
  const [loading, setLoading] = useState(true);
  const [search, setSearch] = useState('');
  const [filterStatus, setFilterStatus] = useState<string | null>(null);
  const [filterPriority, setFilterPriority] = useState<string | null>(null);
  const [showModal, setShowModal] = useState(false);

  useEffect(() => {
    const loadData = async () => {
      setLoading(true);
      try {
        const [ticketData, analyticsData] = await Promise.allSettled([
          apiClient.fetchTickets(),
          apiClient.fetchTicketAnalytics(),
        ]);
        if (ticketData.status === 'fulfilled' && ticketData.value) {
          setTickets(Array.isArray(ticketData.value) ? ticketData.value : []);
        }
        if (analyticsData.status === 'fulfilled' && analyticsData.value) {
          setAnalytics(analyticsData.value);
        }
      } catch (error) {
        console.error('Error loading ticket data:', error);
      } finally {
        setLoading(false);
      }
    };
    loadData();
  }, []);

  const filteredTickets = tickets.filter(t => {
    if (search && !t.title.toLowerCase().includes(search.toLowerCase()) &&
        !t.description.toLowerCase().includes(search.toLowerCase())) {
      return false;
    }
    if (filterStatus && t.status !== filterStatus) {
      return false;
    }
    if (filterPriority && t.priority !== filterPriority) {
      return false;
    }
    return true;
  });

  const handleCreateTicket = async (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    const formData = new FormData(e.currentTarget);
    
    const customerId = formData.get('customer_id') as string;
    const title = formData.get('title') as string;
    const description = formData.get('description') as string;
    const priority = (formData.get('priority') as string) || 'medium';
    const category = (formData.get('category') as string) || 'general';
    
    if (!customerId || !title || !description) {
      alert('Please fill in all required fields (Customer ID, Title, Description)');
      return;
    }
    
    try {
      console.debug('Creating ticket with data:', { customerId, title, description, priority, category });
      const ticket = await apiClient.createTicket({
        customer_id: customerId,
        title: title,
        description: description,
        priority: priority as 'low' | 'medium' | 'high' | 'urgent' | 'critical',
        category: category as 'general' | 'technical' | 'billing' | 'sales' | 'account',
        source: 'web',
      });
      
      console.debug('Ticket creation response:', ticket);
      
      if (ticket && ticket.id) {
        setTickets([ticket, ...tickets]);
        setShowModal(false);
        e.currentTarget.reset();
        alert(`Ticket created successfully! Ticket ID: ${ticket.id}`);
      } else {
        console.error('Failed to create ticket: no response or invalid response');
        alert('Failed to create ticket: Server returned no valid response. Please try again.');
      }
    } catch (err: any) {
      console.error('Error creating ticket:', err);
      alert(`Failed to create ticket: ${err.message || 'Unknown error'}. Please try again.`);
    }
  };

  const handleStatusChange = async (ticketId: string, newStatus: string) => {
    const updated = await apiClient.updateTicket(ticketId, { status: newStatus });
    if (updated) {
      setTickets(tickets.map(t => t.id === ticketId ? updated : t));
    }
  };

  const statusColors: Record<string, string> = {
    open: 'bg-blue-500/15 text-blue-400',
    in_progress: 'bg-yellow-500/15 text-yellow-400',
    pending: 'bg-orange-500/15 text-orange-400',
    resolved: 'bg-green-500/15 text-green-400',
    closed: 'bg-gray-500/15 text-gray-400',
    reopened: 'bg-red-500/15 text-red-400',
  };

  const priorityColors: Record<string, string> = {
    low: 'bg-gray-500/15 text-gray-400',
    medium: 'bg-blue-500/15 text-blue-400',
    high: 'bg-orange-500/15 text-orange-400',
    urgent: 'bg-red-500/15 text-red-400',
    critical: 'bg-red-600/15 text-red-500',
  };

return (
    <div className="flex h-screen overflow-hidden" style={{ background: 'var(--color-background)' }}>
      <Sidebar activeRoute={activeRoute} onRouteChange={setActiveRoute} />

      <main className="flex-1 overflow-y-auto">
        <header className="sticky top-0 z-20 flex items-center justify-between px-6 py-4 border-b"
          style={{ background: 'var(--color-background)', borderColor: 'var(--color-border)' }}>
          <div>
            <h1 className="text-xl font-bold" style={{ color: 'var(--color-foreground)' }}>
              Support Tickets
            </h1>
            <p className="text-xs mt-0.5" style={{ color: 'var(--color-muted-foreground)' }}>
              {tickets.length} tickets · {analytics?.open_tickets || 0} open · {analytics?.resolved_tickets || 0} resolved
            </p>
          </div>
          <div className="flex items-center gap-3">
            <button
              onClick={() => setShowModal(true)}
              className="px-4 py-2 text-sm font-semibold rounded-lg transition-all"
              style={{ background: 'var(--color-primary)', color: 'var(--color-on-primary)' }}
            >
              + New Ticket
            </button>
            <button
              id="open-command-palette-btn"
              onClick={() => setPaletteOpen(true)}
              className="flex items-center gap-2 px-3 py-2 rounded-lg text-sm transition-colors"
              style={{ background: 'var(--color-muted)', color: 'var(--color-muted-foreground)', border: '1px solid var(--color-border)' }}
            >
              <span>🔍</span>
              <span>Search</span>
              <kbd className="text-xs">⌘K</kbd>
            </button>
          </div>
        </header>

        <div className="px-6 py-6 space-y-6">
          {/* Analytics Cards */}
          {analytics && (
            <div className="grid grid-cols-2 md:grid-cols-5 gap-4">
              <div className="rounded-xl p-4 border" style={{ background: 'var(--color-card)', borderColor: 'var(--color-border)' }}>
                <div className="text-xs" style={{ color: 'var(--color-muted-foreground)' }}>Total</div>
                <div className="text-2xl font-bold" style={{ color: 'var(--color-foreground)' }}>{analytics.total_tickets}</div>
              </div>
              <div className="rounded-xl p-4 border" style={{ background: 'var(--color-card)', borderColor: 'var(--color-border)' }}>
                <div className="text-xs" style={{ color: 'var(--color-muted-foreground)' }}>Open</div>
                <div className="text-2xl font-bold" style={{ color: '#3b82f6' }}>{analytics.open_tickets}</div>
              </div>
              <div className="rounded-xl p-4 border" style={{ background: 'var(--color-card)', borderColor: 'var(--color-border)' }}>
                <div className="text-xs" style={{ color: 'var(--color-muted-foreground)' }}>Resolved</div>
                <div className="text-2xl font-bold" style={{ color: '#22c55e' }}>{analytics.resolved_tickets}</div>
              </div>
              <div className="rounded-xl p-4 border" style={{ background: 'var(--color-card)', borderColor: 'var(--color-border)' }}>
                <div className="text-xs" style={{ color: 'var(--color-muted-foreground)' }}>Avg. Satisfaction</div>
                <div className="text-2xl font-bold" style={{ color: 'var(--color-foreground)' }}>{analytics.avg_satisfaction_score.toFixed(1)}/5</div>
              </div>
              <div className="rounded-xl p-4 border" style={{ background: 'var(--color-card)', borderColor: 'var(--color-border)' }}>
                <div className="text-xs" style={{ color: 'var(--color-muted-foreground)' }}>Escalation Rate</div>
                <div className="text-2xl font-bold" style={{ color: 'var(--color-foreground)' }}>{analytics.escalation_rate.toFixed(1)}%</div>
              </div>
            </div>
          )}

          {/* Filters */}
          <div className="flex gap-4 items-center">
            <input
              type="text"
              placeholder="Search tickets..."
              value={search}
              onChange={(e) => setSearch(e.target.value)}
              className="px-3 py-2 rounded-lg text-sm outline-none"
              style={{ background: 'var(--color-card)', color: 'var(--color-foreground)', border: '1px solid var(--color-border)' }}
            />
            
            <select
              value={filterStatus || ''}
              onChange={(e) => setFilterStatus(e.target.value || null)}
              className="px-3 py-2 rounded-lg text-sm outline-none"
              style={{ background: 'var(--color-card)', color: 'var(--color-foreground)', border: '1px solid var(--color-border)' }}
            >
              <option value="">All Statuses</option>
              <option value="open">Open</option>
              <option value="in_progress">In Progress</option>
              <option value="pending">Pending</option>
              <option value="resolved">Resolved</option>
              <option value="closed">Closed</option>
            </select>

            <select
              value={filterPriority || ''}
              onChange={(e) => setFilterPriority(e.target.value || null)}
              className="px-3 py-2 rounded-lg text-sm outline-none"
              style={{ background: 'var(--color-card)', color: 'var(--color-foreground)', border: '1px solid var(--color-border)' }}
            >
              <option value="">All Priorities</option>
              <option value="low">Low</option>
              <option value="medium">Medium</option>
              <option value="high">High</option>
              <option value="urgent">Urgent</option>
              <option value="critical">Critical</option>
            </select>
          </div>

          {/* Tickets Table */}
          <div className="rounded-xl border" style={{ background: 'var(--color-card)', borderColor: 'var(--color-border)' }}>
            <div className="overflow-x-auto">
              <table className="w-full">
                <thead>
                  <tr style={{ borderBottom: '1px solid var(--color-border)' }}>
                    <th className="text-left px-4 py-3 text-xs font-semibold" style={{ color: 'var(--color-muted-foreground)' }}>Title</th>
                    <th className="text-left px-4 py-3 text-xs font-semibold" style={{ color: 'var(--color-muted-foreground)' }}>Customer</th>
                    <th className="text-left px-4 py-3 text-xs font-semibold" style={{ color: 'var(--color-muted-foreground)' }}>Status</th>
                    <th className="text-left px-4 py-3 text-xs font-semibold" style={{ color: 'var(--color-muted-foreground)' }}>Priority</th>
                    <th className="text-left px-4 py-3 text-xs font-semibold" style={{ color: 'var(--color-muted-foreground)' }}>Category</th>
                    <th className="text-left px-4 py-3 text-xs font-semibold" style={{ color: 'var(--color-muted-foreground)' }}>Created</th>
                    <th className="text-left px-4 py-3 text-xs font-semibold" style={{ color: 'var(--color-muted-foreground)' }}>Actions</th>
                  </tr>
                </thead>
                <tbody>
                  {loading ? (
                    <tr>
                      <td colSpan={7} className="px-4 py-8 text-center" style={{ color: 'var(--color-muted-foreground)' }}>
                        Loading tickets...
                      </td>
                    </tr>
                  ) : filteredTickets.length === 0 ? (
                    <tr>
                      <td colSpan={7} className="px-4 py-8 text-center" style={{ color: 'var(--color-muted-foreground)' }}>
                        No tickets found
                      </td>
                    </tr>
                  ) : (
                    filteredTickets.map(ticket => (
                      <tr key={ticket.id} style={{ borderBottom: '1px solid var(--color-border)' }}>
                        <td className="px-4 py-3">
                          <div className="font-semibold text-sm" style={{ color: 'var(--color-foreground)' }}>{ticket.title}</div>
                          <div className="text-xs" style={{ color: 'var(--color-muted-foreground)' }}>
                            {ticket.description.substring(0, 50)}...
                          </div>
                        </td>
                        <td className="px-4 py-3 text-sm" style={{ color: 'var(--color-foreground)' }}>
                          {ticket.customer_id.substring(0, 8)}...
                        </td>
                        <td className="px-4 py-3">
                          <span className={`text-xs px-2 py-1 rounded-full ${statusColors[ticket.status] || statusColors.open}`}>
                            {ticket.status}
                          </span>
                        </td>
                        <td className="px-4 py-3">
                          <span className={`text-xs px-2 py-1 rounded-full ${priorityColors[ticket.priority] || priorityColors.medium}`}>
                            {ticket.priority}
                          </span>
                        </td>
                        <td className="px-4 py-3 text-sm" style={{ color: 'var(--color-foreground)' }}>
                          {ticket.category}
                        </td>
                        <td className="px-4 py-3 text-xs" style={{ color: 'var(--color-muted-foreground)' }}>
                          {new Date(ticket.created_at).toLocaleDateString()}
                        </td>
                        <td className="px-4 py-3">
                          <select
                            value={ticket.status}
                            onChange={(e) => handleStatusChange(ticket.id, e.target.value)}
                            className="text-xs px-2 py-1 rounded outline-none"
                            style={{ background: 'var(--color-background)', color: 'var(--color-foreground)', border: '1px solid var(--color-border)' }}
                          >
                            <option value="open">Open</option>
                            <option value="in_progress">In Progress</option>
                            <option value="pending">Pending</option>
                            <option value="resolved">Resolved</option>
                            <option value="closed">Closed</option>
                          </select>
                        </td>
                      </tr>
                    ))
                  )}
                </tbody>
              </table>
            </div>
          </div>
        </div>
      </main>

      {/* Create Ticket Modal */}
      {showModal && (
        <div className="fixed inset-0 bg-black/50 flex items-center justify-center z-50">
          <div className="rounded-xl p-6 w-full max-w-lg" style={{ background: 'var(--color-card)', border: '1px solid var(--color-border)' }}>
            <h2 className="text-lg font-bold mb-4" style={{ color: 'var(--color-foreground)' }}>Create Support Ticket</h2>
            <form onSubmit={handleCreateTicket} className="space-y-4">
              <div>
                <label className="text-xs font-semibold block mb-1" style={{ color: 'var(--color-muted-foreground)' }}>
                  Customer ID *
                </label>
                <input
                  name="customer_id"
                  required
                  className="w-full px-3 py-2 rounded-lg text-sm outline-none"
                  style={{ background: 'var(--color-background)', color: 'var(--color-foreground)', border: '1px solid var(--color-border)' }}
                />
              </div>
              <div>
                <label className="text-xs font-semibold block mb-1" style={{ color: 'var(--color-muted-foreground)' }}>
                  Title *
                </label>
                <input
                  name="title"
                  required
                  className="w-full px-3 py-2 rounded-lg text-sm outline-none"
                  style={{ background: 'var(--color-background)', color: 'var(--color-foreground)', border: '1px solid var(--color-border)' }}
                />
              </div>
              <div>
                <label className="text-xs font-semibold block mb-1" style={{ color: 'var(--color-muted-foreground)' }}>
                  Description *
                </label>
                <textarea
                  name="description"
                  required
                  rows={3}
                  className="w-full px-3 py-2 rounded-lg text-sm outline-none resize-none"
                  style={{ background: 'var(--color-background)', color: 'var(--color-foreground)', border: '1px solid var(--color-border)' }}
                />
              </div>
              <div className="grid grid-cols-2 gap-4">
                <div>
                  <label className="text-xs font-semibold block mb-1" style={{ color: 'var(--color-muted-foreground)' }}>
                    Priority
                  </label>
                  <select
                    name="priority"
                    defaultValue="medium"
                    className="w-full px-3 py-2 rounded-lg text-sm outline-none"
                    style={{ background: 'var(--color-background)', color: 'var(--color-foreground)', border: '1px solid var(--color-border)' }}
                  >
                    <option value="low">Low</option>
                    <option value="medium">Medium</option>
                    <option value="high">High</option>
                    <option value="urgent">Urgent</option>
                    <option value="critical">Critical</option>
                  </select>
                </div>
                <div>
                  <label className="text-xs font-semibold block mb-1" style={{ color: 'var(--color-muted-foreground)' }}>
                    Category
                  </label>
                  <select
                    name="category"
                    defaultValue="general"
                    className="w-full px-3 py-2 rounded-lg text-sm outline-none"
                    style={{ background: 'var(--color-background)', color: 'var(--color-foreground)', border: '1px solid var(--color-border)' }}
                  >
                    <option value="general">General</option>
                    <option value="technical">Technical</option>
                    <option value="billing">Billing</option>
                    <option value="sales">Sales</option>
                    <option value="account">Account</option>
                  </select>
                </div>
              </div>
              <div className="flex justify-end gap-3 pt-4">
                <button
                  type="button"
                  onClick={() => setShowModal(false)}
                  className="px-4 py-2 text-sm rounded-lg transition-colors cursor-pointer hover:opacity-80"
                  style={{ background: 'var(--color-muted)', color: 'var(--color-muted-foreground)', border: '1px solid var(--color-border)' }}
                >
                  Cancel
                </button>
                <button
                  type="submit"
                  className="px-4 py-2 text-sm font-semibold rounded-lg transition-all cursor-pointer hover:opacity-90 disabled:opacity-50 disabled:cursor-not-allowed"
                  style={{ background: 'var(--color-primary)', color: 'var(--color-on-primary)', border: '1px solid var(--color-primary)' }}
                >
                  Create Ticket
                </button>
              </div>
            </form>
          </div>
        </div>
      )}

      <CommandPalette open={paletteOpen} onClose={() => setPaletteOpen(false)} onNavigate={setActiveRoute} />
    </div>
  );
}