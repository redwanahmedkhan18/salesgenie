import React, { useState, useEffect, useCallback } from 'react';
import { AreaChart, Area, BarChart, Bar, Line, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer } from 'recharts';
import { Sidebar, CommandPalette } from './AppShell';
import { apiClient, type KPICard, type ConversationPoint, type RevenuePoint, type ChannelPoint } from '../../lib/api-client';

const formatCurrency = (value: number | undefined) => {
  if (value === undefined) return '$0';
  return `$${value.toLocaleString()}`;
};

/* ─── Mock Data Generators ─── */
const conversationTrend: ConversationPoint[] = Array.from({ length: 24 }, (_, i) => ({
  hour: `${i}:00`,
  conversations: Math.floor(800 + Math.random() * 600),
  ai: Math.floor(600 + Math.random() * 400),
  human: Math.floor(50 + Math.random() * 100),
}));

const revenueSeries: RevenuePoint[] = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'].map(d => ({
  day: d,
  revenue: Math.floor(8000 + Math.random() * 8000),
  target: 12000,
}));

const channelData: ChannelPoint[] = [
  { name: 'Website', value: 38 },
  { name: 'WhatsApp', value: 25 },
  { name: 'Email', value: 16 },
  { name: 'Slack', value: 11 },
  { name: 'Telegram', value: 10 },
];

/* ─── Sub-components ─── */
function KPICardComponent({ card }: { card: KPICard }) {
  return (
    <div className="kpi-card group" id={`kpi-${card.id || card.title.toLowerCase().replace(/\s+/g, '-')}`}>
      <div className="flex items-start justify-between mb-3">
        <div className="text-2xl">{card.icon}</div>
        <span
          className={`badge-status text-xs ${card.changeDir === 'up' ? 'bg-green-500/15 text-green-400' : card.changeDir === 'down' && card.id === 'token-cost' ? 'bg-green-500/15 text-green-400' : 'bg-red-500/15 text-red-400'}`}
        >
          {card.changeDir === 'up' ? '↑' : '↓'} {card.change}
        </span>
      </div>
      <div className="text-2xl font-bold tracking-tight" style={{ color: 'var(--color-foreground)' }}>
        {card.value}
      </div>
      <div className="text-xs mt-1" style={{ color: 'var(--color-muted-foreground)' }}>
        {card.title}
      </div>
      {/* Mini sparkline indicator */}
      <div className="mt-3 h-1 rounded-full overflow-hidden" style={{ background: 'var(--color-border)' }}>
        <div className="h-full rounded-full transition-all duration-1000"
          style={{ width: `${Math.random() * 40 + 50}%`, background: card.color }} />
      </div>
    </div>
  );
}

function SkeletonCard() {
  return (
    <div className="kpi-card">
      <div className="skeleton h-5 w-5 rounded mb-3" />
      <div className="skeleton h-7 w-24 rounded mb-2" />
      <div className="skeleton h-3 w-32 rounded" />
    </div>
  );
}

/* ─── Main Dashboard ─── */
export default function Dashboard() {
  const [activeRoute, setActiveRoute] = useState('dashboard');
  const [paletteOpen, setPaletteOpen] = useState(false);
  const [loading, setLoading] = useState(true);
  const [kpiCards, setKpiCards] = useState<KPICard[]>([]);

  useEffect(() => {
    const loadDashboardData = async () => {
      setLoading(true);
      try {
        const kpis = await apiClient.fetchKPIs();
        setKpiCards(apiClient.transformKPIsToCards(kpis));
      } catch (error) {
        console.error('Error loading dashboard data:', error);
        setKpiCards([]);
      } finally {
        setLoading(false);
      }
    };

    const timer = setTimeout(() => setLoading(false), 900);
    loadDashboardData();
    document.addEventListener('open-command-palette', () => setPaletteOpen(true));
    return () => {
      clearTimeout(timer);
    };
  }, []);

  const handleKeyDown = useCallback((e: KeyboardEvent) => {
    if ((e.metaKey || e.ctrlKey) && e.key === 'k') {
      e.preventDefault();
      setPaletteOpen(p => !p);
    }
    if (e.key === 'Escape') setPaletteOpen(false);
  }, []);

  useEffect(() => {
    window.addEventListener('keydown', handleKeyDown);
    return () => window.removeEventListener('keydown', handleKeyDown);
  }, [handleKeyDown]);

  return (
    <div className="flex h-screen overflow-hidden" style={{ background: 'var(--color-background)' }}>
      <Sidebar activeRoute={activeRoute} onRouteChange={setActiveRoute} />

      {/* Main content */}
      <main className="flex-1 overflow-y-auto">
        {/* Topbar */}
        <header className="sticky top-0 z-20 flex items-center justify-between px-6 py-4 border-b"
          style={{ background: 'var(--color-background)', borderColor: 'var(--color-border)' }}>
          <div>
            <h1 className="text-xl font-bold" style={{ color: 'var(--color-foreground)' }}>
              AI Operations Dashboard
            </h1>
            <p className="text-xs mt-0.5" style={{ color: 'var(--color-muted-foreground)' }}>
              Real-time platform metrics · Last updated just now
            </p>
          </div>
          <div className="flex items-center gap-3">
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
            <div className="w-px h-6" style={{ background: 'var(--color-border)' }} />
            <div className="w-8 h-8 rounded-full flex items-center justify-center text-xs font-bold"
              style={{ background: 'var(--color-primary)', color: 'var(--color-on-primary)' }}>
              AD
            </div>
          </div>
        </header>

        <div className="px-6 py-6 space-y-6">
          {/* KPI Cards Grid */}
          <section aria-label="Key performance indicators">
            <div className="grid grid-cols-2 md:grid-cols-3 xl:grid-cols-6 gap-4">
              {loading
                ? Array.from({ length: 6 }).map((_, i) => <SkeletonCard key={i} />)
                : kpiCards.map(card => <KPICardComponent key={card.id} card={card} />)
              }
            </div>
          </section>

          {/* Charts Row */}
          <section className="grid grid-cols-1 xl:grid-cols-3 gap-6" aria-label="Analytics charts">
            {/* Conversation Volume */}
            <div className="xl:col-span-2 rounded-xl p-5 border" style={{ background: 'var(--color-card)', borderColor: 'var(--color-border)' }}>
              <div className="flex items-center justify-between mb-4">
                <div>
                  <h2 className="text-sm font-bold" style={{ color: 'var(--color-foreground)' }}>Conversation Volume</h2>
                  <p className="text-xs mt-0.5" style={{ color: 'var(--color-muted-foreground)' }}>24-hour rolling window · All channels</p>
                </div>
                <div className="flex gap-4 text-xs" style={{ color: 'var(--color-muted-foreground)' }}>
                  <span className="flex items-center gap-1.5"><span className="w-2 h-2 rounded-full inline-block" style={{ background: '#f7a501' }} />Total</span>
                  <span className="flex items-center gap-1.5"><span className="w-2 h-2 rounded-full inline-block" style={{ background: '#2c84e0' }} />AI</span>
                  <span className="flex items-center gap-1.5"><span className="w-2 h-2 rounded-full inline-block" style={{ background: '#2c8c66' }} />Human</span>
                </div>
              </div>
              {loading ? (
                <div className="skeleton h-48 rounded-lg" />
              ) : (
                <ResponsiveContainer width="100%" height={200}>
                  <AreaChart data={conversationTrend}>
                    <defs>
                      <linearGradient id="grad-total" x1="0" y1="0" x2="0" y2="1">
                        <stop offset="5%" stopColor="#f7a501" stopOpacity={0.3} />
                        <stop offset="95%" stopColor="#f7a501" stopOpacity={0} />
                      </linearGradient>
                      <linearGradient id="grad-ai" x1="0" y1="0" x2="0" y2="1">
                        <stop offset="5%" stopColor="#2c84e0" stopOpacity={0.2} />
                        <stop offset="95%" stopColor="#2c84e0" stopOpacity={0} />
                      </linearGradient>
                    </defs>
                    <CartesianGrid strokeDasharray="3 3" stroke="rgba(255,255,255,0.05)" />
                    <XAxis dataKey="hour" tick={{ fill: '#9b9c92', fontSize: 10 }} tickLine={false} interval={3} />
                    <YAxis tick={{ fill: '#9b9c92', fontSize: 10 }} tickLine={false} axisLine={false} />
                    <Tooltip
                      contentStyle={{ background: '#23251d', border: '1px solid rgba(255,255,255,0.1)', borderRadius: 8, fontSize: 12 }}
                      labelStyle={{ color: '#f0f0ec' }}
                    />
                    <Area type="monotone" dataKey="conversations" stroke="#f7a501" fill="url(#grad-total)" strokeWidth={2} dot={false} />
                    <Area type="monotone" dataKey="ai" stroke="#2c84e0" fill="url(#grad-ai)" strokeWidth={1.5} dot={false} />
                    <Line type="monotone" dataKey="human" stroke="#2c8c66" strokeWidth={1.5} dot={false} />
                  </AreaChart>
                </ResponsiveContainer>
              )}
            </div>

            {/* Channel Distribution */}
            <div className="rounded-xl p-5 border" style={{ background: 'var(--color-card)', borderColor: 'var(--color-border)' }}>
              <h2 className="text-sm font-bold mb-1" style={{ color: 'var(--color-foreground)' }}>Channel Distribution</h2>
              <p className="text-xs mb-4" style={{ color: 'var(--color-muted-foreground)' }}>Omnichannel traffic breakdown</p>
              {loading ? (
                <div className="skeleton h-48 rounded-lg" />
              ) : (
                <div className="space-y-3">
                  {channelData.map(ch => (
                    <div key={ch.name}>
                      <div className="flex justify-between text-xs mb-1" style={{ color: 'var(--color-muted-foreground)' }}>
                        <span>{ch.name}</span><span className="font-semibold" style={{ color: 'var(--color-foreground)' }}>{ch.value}%</span>
                      </div>
                      <div className="h-1.5 rounded-full" style={{ background: 'var(--color-border)' }}>
                        <div className="h-full rounded-full transition-all duration-700"
                          style={{ width: `${ch.value * 2.5}%`, background: 'var(--color-primary)' }} />
                      </div>
                    </div>
                  ))}
                </div>
              )}
            </div>
          </section>

          {/* Revenue Chart */}
          <section className="rounded-xl p-5 border" style={{ background: 'var(--color-card)', borderColor: 'var(--color-border)' }}>
            <div className="flex items-center justify-between mb-4">
              <div>
                <h2 className="text-sm font-bold" style={{ color: 'var(--color-foreground)' }}>Weekly Revenue vs. Target</h2>
                <p className="text-xs mt-0.5" style={{ color: 'var(--color-muted-foreground)' }}>AI-assisted sales conversions · Rolling 7 days</p>
              </div>
              <span className="text-xs px-2 py-1 rounded" style={{ background: 'rgba(44,140,102,0.15)', color: '#2c8c66' }}>
                ↑ 22.1% vs last week
              </span>
            </div>
            {loading ? (
              <div className="skeleton h-40 rounded-lg" />
            ) : (
              <ResponsiveContainer width="100%" height={160}>
                <BarChart data={revenueSeries} barGap={4}>
                  <CartesianGrid strokeDasharray="3 3" stroke="rgba(255,255,255,0.05)" />
                  <XAxis dataKey="day" tick={{ fill: '#9b9c92', fontSize: 11 }} tickLine={false} axisLine={false} />
                  <YAxis tick={{ fill: '#9b9c92', fontSize: 11 }} tickLine={false} axisLine={false} tickFormatter={(v: number) => `$${(v / 1000).toFixed(0)}k`} />
                  <Tooltip
                    contentStyle={{ background: '#23251d', border: '1px solid rgba(255,255,255,0.1)', borderRadius: 8, fontSize: 12 }}
                    formatter={(val: unknown) => {
                      const numVal = val as number | undefined;
                      return [formatCurrency(numVal), ''];
                    }}
                  />
                  <Bar dataKey="revenue" fill="#f7a501" radius={[4, 4, 0, 0]} />
                  <Bar dataKey="target" fill="rgba(247,165,1,0.15)" radius={[4, 4, 0, 0]} />
                </BarChart>
              </ResponsiveContainer>
            )}
          </section>
        </div>
      </main>

      {/* Command Palette */}
      <CommandPalette open={paletteOpen} onClose={() => setPaletteOpen(false)} onNavigate={setActiveRoute} />
    </div>
  );
}
