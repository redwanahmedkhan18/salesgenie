import React, { useState, useEffect } from 'react';
import { Sidebar, CommandPalette } from './AppShell';
import {
  AreaChart,
  Area,
  BarChart,
  Bar,
  LineChart,
  Line,
  PieChart,
  Pie,
  Cell,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  ResponsiveContainer,
  Legend,
} from 'recharts';

interface AnalyticsOverview {
  total_conversations: number;
  active_conversations: number;
  resolved_conversations: number;
  avg_resolution_time_hours: number;
  avg_satisfaction_score: number;
  handoff_rate: number;
  conversations_by_channel: Record<string, number>;
  conversations_by_status: Record<string, number>;
  top_actors: Array<{ actor_id: string; count: number }>;
  recent_conversations: Array<{
    id: string;
    title: string | null;
    status: string;
    channel: string;
    created_at: string;
    message_count: number;
  }>;
}

interface TicketAnalytics {
  total_tickets: number;
  open_tickets: number;
  resolved_tickets: number;
  avg_resolution_time_hours: number;
  avg_satisfaction_score: number;
  escalation_rate: number;
  tickets_by_priority: Record<string, number>;
  tickets_by_category: Record<string, number>;
}

interface KPIPoint {
  day: string;
  conversations: number;
  tickets: number;
  resolution: number;
}

const CHANNEL_COLORS = ['#2c84e0', '#f7a501', '#2c8c66', '#7c44a6', '#cd4239', '#9b9c92'];
const STATUS_COLORS: Record<string, string> = {
  active: '#2c8c66',
  resolved: '#22c55e',
  closed: '#9b9c92',
  open: '#f7a501',
  escalated: '#cd4239',
};

export default function AnalyticsDashboard() {
  const [activeRoute, setActiveRoute] = useState('analytics');
  const [paletteOpen, setPaletteOpen] = useState(false);
  const [overview, setOverview] = useState<AnalyticsOverview | null>(null);
  const [tickets, setTickets] = useState<TicketAnalytics | null>(null);
  const [loading, setLoading] = useState(true);
  const [dateRange, setDateRange] = useState('30d');

  const convServiceUrl = import.meta.env.DEV ? 'http://localhost:8017/api/v1' : '/api/v1';
  const ticketServiceUrl = import.meta.env.DEV ? 'http://localhost:8008/api/v1' : '/api/v1';
  const analyticsServiceUrl = import.meta.env.DEV ? 'http://localhost:8011/api/v1' : '/api/v1';

  useEffect(() => {
    const loadData = async () => {
      setLoading(true);
      try {
        const token = localStorage.getItem('auth_token');
        const authHeaders = token ? { 'Authorization': `Bearer ${token}` } : {};
        
        const [overviewRes, ticketsRes] = await Promise.all([
          fetch(`${convServiceUrl}/conversations/overview`, {
            headers: { 'Content-Type': 'application/json', ...authHeaders } as HeadersInit,
          }),
          fetch(`${ticketServiceUrl}/tickets/analytics/overview`, {
            headers: { 'Content-Type': 'application/json', ...authHeaders } as HeadersInit,
          }),
        ]);

        if (overviewRes.ok) {
          const data: AnalyticsOverview = await overviewRes.json();
          setOverview(data);
        }
        if (ticketsRes.ok) {
          const data: TicketAnalytics = await ticketsRes.json();
          setTickets(data);
        }
      } catch (error) {
        console.error('Error loading analytics data:', error);
      } finally {
        setLoading(false);
      }
    };

    loadData();
  }, [dateRange]);

  const generateKpiData = (): KPIPoint[] => {
    const days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'];
    return days.map(day => ({
      day,
      conversations: Math.floor(100 + Math.random() * 200),
      tickets: Math.floor(20 + Math.random() * 80),
      resolution: Math.floor(85 + Math.random() * 10),
    }));
  };

  const kpiData = generateKpiData();

  const channelData = overview ? Object.entries(overview.conversations_by_channel).map(([name, value]) => ({
    name,
    value,
  })) : [];

  const priorityData = tickets ? Object.entries(tickets.tickets_by_priority).map(([name, value]) => ({
    name,
    value,
  })) : [];

  const statusData = overview ? Object.entries(overview.conversations_by_status).map(([name, value]) => ({
    name,
    value,
  })) : [];

  const formatNumber = (num: number) => {
    if (num >= 1000000) return `${(num / 1000000).toFixed(1)}M`;
    if (num >= 1000) return `${(num / 1000).toFixed(1)}K`;
    return num.toString();
  };

  return (
    <div className="flex h-screen overflow-hidden" style={{ background: 'var(--color-background)' }}>
      <Sidebar activeRoute={activeRoute} onRouteChange={setActiveRoute} />

      <main className="flex-1 overflow-y-auto">
        <header className="sticky top-0 z-20 flex items-center justify-between px-6 py-4 border-b"
          style={{ background: 'var(--color-background)', borderColor: 'var(--color-border)' }}>
          <div>
            <h1 className="text-xl font-bold" style={{ color: 'var(--color-foreground)' }}>
              Analytics Dashboard
            </h1>
            <p className="text-xs mt-0.5" style={{ color: 'var(--color-muted-foreground)' }}>
              Business metrics, KPIs, and performance insights
            </p>
          </div>
          <div className="flex items-center gap-3">
            <select
              value={dateRange}
              onChange={(e) => setDateRange(e.target.value)}
              className="px-3 py-2 rounded-lg text-sm outline-none"
              style={{ background: 'var(--color-card)', color: 'var(--color-foreground)', border: '1px solid var(--color-border)' }}
            >
              <option value="7d">Last 7 days</option>
              <option value="30d">Last 30 days</option>
              <option value="90d">Last 90 days</option>
              <option value="all">All time</option>
            </select>
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
          {/* KPI Summary Cards */}
          <div className="grid grid-cols-2 md:grid-cols-4 gap-4">
            <div className="rounded-xl p-4 border" style={{ background: 'var(--color-card)', borderColor: 'var(--color-border)' }}>
              <div className="text-xs" style={{ color: 'var(--color-muted-foreground)' }}>Total Conversations</div>
              <div className="text-2xl font-bold" style={{ color: 'var(--color-foreground)' }}>
                {overview ? formatNumber(overview.total_conversations) : '-'}
              </div>
            </div>
            <div className="rounded-xl p-4 border" style={{ background: 'var(--color-card)', borderColor: 'var(--color-border)' }}>
              <div className="text-xs" style={{ color: 'var(--color-muted-foreground)' }}>Active Conversations</div>
              <div className="text-2xl font-bold" style={{ color: '#2c84e0' }}>
                {overview ? formatNumber(overview.active_conversations) : '-'}
              </div>
            </div>
            <div className="rounded-xl p-4 border" style={{ background: 'var(--color-card)', borderColor: 'var(--color-border)' }}>
              <div className="text-xs" style={{ color: 'var(--color-muted-foreground)' }}>Avg Satisfaction</div>
              <div className="text-2xl font-bold" style={{ color: '#2c8c66' }}>
                {overview ? `${overview.avg_satisfaction_score.toFixed(1)}/5` : '-'}
              </div>
            </div>
            <div className="rounded-xl p-4 border" style={{ background: 'var(--color-card)', borderColor: 'var(--color-border)' }}>
              <div className="text-xs" style={{ color: 'var(--color-muted-foreground)' }}>Handoff Rate</div>
              <div className="text-2xl font-bold" style={{ color: '#7c44a6' }}>
                {overview ? `${overview.handoff_rate.toFixed(1)}%` : '-'}
              </div>
            </div>
          </div>

          {/* Ticket Analytics */}
          {tickets && (
            <div className="grid grid-cols-2 md:grid-cols-4 gap-4">
              <div className="rounded-xl p-4 border" style={{ background: 'var(--color-card)', borderColor: 'var(--color-border)' }}>
                <div className="text-xs" style={{ color: 'var(--color-muted-foreground)' }}>Total Tickets</div>
                <div className="text-2xl font-bold" style={{ color: 'var(--color-foreground)' }}>
                  {formatNumber(tickets.total_tickets)}
                </div>
              </div>
              <div className="rounded-xl p-4 border" style={{ background: 'var(--color-card)', borderColor: 'var(--color-border)' }}>
                <div className="text-xs" style={{ color: 'var(--color-muted-foreground)' }}>Open Tickets</div>
                <div className="text-2xl font-bold" style={{ color: '#f7a501' }}>
                  {tickets.open_tickets}
                </div>
              </div>
              <div className="rounded-xl p-4 border" style={{ background: 'var(--color-card)', borderColor: 'var(--color-border)' }}>
                <div className="text-xs" style={{ color: 'var(--color-muted-foreground)' }}>Resolved</div>
                <div className="text-2xl font-bold" style={{ color: '#22c55e' }}>
                  {tickets.resolved_tickets}
                </div>
              </div>
              <div className="rounded-xl p-4 border" style={{ background: 'var(--color-card)', borderColor: 'var(--color-border)' }}>
                <div className="text-xs" style={{ color: 'var(--color-muted-foreground)' }}>Escalation Rate</div>
                <div className="text-2xl font-bold" style={{ color: '#cd4239' }}>
                  {tickets.escalation_rate.toFixed(1)}%
                </div>
              </div>
            </div>
          )}

          {/* Charts Row 1 */}
          <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
            <div className="rounded-xl border p-4" style={{ background: 'var(--color-card)', borderColor: 'var(--color-border)' }}>
              <h3 className="text-sm font-semibold mb-3" style={{ color: 'var(--color-foreground)' }}>Conversations & Tickets Trend</h3>
              <ResponsiveContainer width="100%" height={250}>
                <AreaChart data={kpiData}>
                  <defs>
                    <linearGradient id="convGradient" x1="0" y1="0" x2="0" y2="1">
                      <stop offset="5%" stopColor="#2c84e0" stopOpacity={0.3} />
                      <stop offset="95%" stopColor="#2c84e0" stopOpacity={0} />
                    </linearGradient>
                    <linearGradient id="ticketGradient" x1="0" y1="0" x2="0" y2="1">
                      <stop offset="5%" stopColor="#f7a501" stopOpacity={0.3} />
                      <stop offset="95%" stopColor="#f7a501" stopOpacity={0} />
                    </linearGradient>
                  </defs>
                  <CartesianGrid strokeDasharray="3 3" vertical={false} opacity={0.1} />
                  <XAxis dataKey="day" axisLine={false} tickLine={false}
                    tick={{ fontSize: 11, fill: 'var(--color-muted-foreground)' }} />
                  <YAxis axisLine={false} tickLine={false}
                    tick={{ fontSize: 11, fill: 'var(--color-muted-foreground)' }} />
                  <Tooltip
                    contentStyle={{ backgroundColor: 'var(--color-card)', border: '1px solid var(--color-border)' }}
                    labelStyle={{ color: 'var(--color-foreground)' }}
                  />
                  <Area type="monotone" dataKey="conversations" stroke="#2c84e0" fill="url(#convGradient)" strokeWidth={2} />
                  <Area type="monotone" dataKey="tickets" stroke="#f7a501" fill="url(#ticketGradient)" strokeWidth={2} />
                </AreaChart>
              </ResponsiveContainer>
            </div>

            <div className="rounded-xl border p-4" style={{ background: 'var(--color-card)', borderColor: 'var(--color-border)' }}>
              <h3 className="text-sm font-semibold mb-3" style={{ color: 'var(--color-foreground)' }}>Resolution Rate</h3>
              <ResponsiveContainer width="100%" height={250}>
                <LineChart data={kpiData}>
                  <CartesianGrid strokeDasharray="3 3" vertical={false} opacity={0.1} />
                  <XAxis dataKey="day" axisLine={false} tickLine={false}
                    tick={{ fontSize: 11, fill: 'var(--color-muted-foreground)' }} />
                  <YAxis axisLine={false} tickLine={false} domain={[0, 100]}
                    tick={{ fontSize: 11, fill: 'var(--color-muted-foreground)' }} />
                  <Tooltip
                    contentStyle={{ backgroundColor: 'var(--color-card)', border: '1px solid var(--color-border)' }}
                    labelStyle={{ color: 'var(--color-foreground)' }}
                  />
                  <Line type="monotone" dataKey="resolution" stroke="#2c8c66" strokeWidth={3} dot={{ r: 4 }} />
                </LineChart>
              </ResponsiveContainer>
            </div>
          </div>

          {/* Charts Row 2 */}
          <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
            <div className="rounded-xl border p-4" style={{ background: 'var(--color-card)', borderColor: 'var(--color-border)' }}>
              <h3 className="text-sm font-semibold mb-3" style={{ color: 'var(--color-foreground)' }}>Channels</h3>
              <ResponsiveContainer width="100%" height={200}>
                <PieChart>
                  <Pie
                    data={channelData}
                    cx="50%"
                    cy="50%"
                    innerRadius={50}
                    outerRadius={80}
                    paddingAngle={2}
                    dataKey="value"
                    label={({ name, percent }) => `${name} ${(percent ?? 0 * 100).toFixed(0)}%`}
                    labelLine={false}
                  >
                    {channelData.map((_, i) => (
                      <Cell key={`channel-${i}`} fill={CHANNEL_COLORS[i % CHANNEL_COLORS.length]} />
                    ))}
                  </Pie>
                  <Tooltip
                    contentStyle={{ backgroundColor: 'var(--color-card)', border: '1px solid var(--color-border)' }}
                  />
                </PieChart>
              </ResponsiveContainer>
            </div>

            <div className="rounded-xl border p-4" style={{ background: 'var(--color-card)', borderColor: 'var(--color-border)' }}>
              <h3 className="text-sm font-semibold mb-3" style={{ color: 'var(--color-foreground)' }}>Ticket Priority</h3>
              <ResponsiveContainer width="100%" height={200}>
                <BarChart data={priorityData} layout="vertical">
                  <CartesianGrid strokeDasharray="3 3" horizontal={false} opacity={0.1} />
                  <XAxis type="number" axisLine={false} tickLine={false}
                    tick={{ fontSize: 11, fill: 'var(--color-muted-foreground)' }} />
                  <YAxis type="category" axisLine={false} tickLine={false}
                    tick={{ fontSize: 11, fill: 'var(--color-muted-foreground)' }} />
                  <Tooltip
                    contentStyle={{ backgroundColor: 'var(--color-card)', border: '1px solid var(--color-border)' }}
                  />
                  <Bar dataKey="value" radius={[0, 4, 4, 0]}>
                    {priorityData.map((_, i) => (
                      <Cell key={`priority-${i}`} fill={CHANNEL_COLORS[i % CHANNEL_COLORS.length]} />
                    ))}
                  </Bar>
                </BarChart>
              </ResponsiveContainer>
            </div>

            <div className="rounded-xl border p-4" style={{ background: 'var(--color-card)', borderColor: 'var(--color-border)' }}>
              <h3 className="text-sm font-semibold mb-3" style={{ color: 'var(--color-foreground)' }}>Conversation Status</h3>
              <ResponsiveContainer width="100%" height={200}>
                <PieChart>
                  <Pie
                    data={statusData}
                    cx="50%"
                    cy="50%"
                    outerRadius={80}
                    paddingAngle={2}
                    dataKey="value"
                    label={({ name, percent }) => `${(percent ?? 0 * 100).toFixed(0)}%`}
                  >
                    {statusData.map((entry, i) => (
                      <Cell key={`status-${i}`} fill={STATUS_COLORS[entry.name] || CHANNEL_COLORS[i % CHANNEL_COLORS.length]} />
                    ))}
                  </Pie>
                  <Tooltip
                    contentStyle={{ backgroundColor: 'var(--color-card)', border: '1px solid var(--color-border)' }}
                  />
                  <Legend
                    layout="vertical"
                    verticalAlign="middle"
                    align="right"
                    wrapperStyle={{ fontSize: 10, color: 'var(--color-muted-foreground)' }}
                  />
                </PieChart>
              </ResponsiveContainer>
            </div>
          </div>
        </div>
      </main>

      <CommandPalette open={paletteOpen} onClose={() => setPaletteOpen(false)} onNavigate={setActiveRoute} />
    </div>
  );
}
