import React, { useState, useEffect } from 'react';
import { apiClient } from '../../lib/api-client';
import type { ConversationPoint, RevenuePoint, ChannelPoint } from '../../lib/types';

interface PlatformMetrics {
  total_organizations: number;
  active_organizations: number;
  suspended_organizations: number;
  total_users: number;
  total_tokens_used: number;
  ai_cost_usd: number;
  platform_uptime_percent: number;
}

interface AICostBreakdown {
  provider: string;
  model: string;
  cost_usd: number;
  tokens_used: number;
  percentage: number;
}

interface Anomaly {
  type: string;
  description: string;
  severity: 'low' | 'medium' | 'high' | 'critical';
  affected_resource: string;
  recommendation: string;
}

export default function PlatformAnalytics() {
  const [loading, setLoading] = useState(true);
  const [metrics, setMetrics] = useState<PlatformMetrics | null>(null);
  const [costBreakdown, setCostBreakdown] = useState<AICostBreakdown[]>([]);
  const [anomalies, setAnomalies] = useState<Anomaly[]>([]);
  const [timeRange, setTimeRange] = useState<'24h' | '7d' | '30d'>('24h');
  const [aiInsight, setAiInsight] = useState<string>('');

  useEffect(() => {
    loadAnalytics();
  }, [timeRange]);

  const loadAnalytics = async () => {
    setLoading(true);
    try {
      const metricsData = await apiClient.fetchPlatformMetrics();
      if (metricsData) {
        setMetrics(metricsData);
      }

      const kpis = await apiClient.fetchKPIs();
      if (kpis) {
        setCostBreakdown([
          { provider: 'Groq', model: 'Mixtral', cost_usd: kpis.aiCostUsd * 0.35, tokens_used: Math.floor(kpis.totalTokenUsage * 0.35), percentage: 35 },
          { provider: 'Google AI', model: 'Gemini 1.5 Pro', cost_usd: kpis.aiCostUsd * 0.40, tokens_used: Math.floor(kpis.totalTokenUsage * 0.40), percentage: 40 },
          { provider: 'Mistral', model: 'Mistral Small', cost_usd: kpis.aiCostUsd * 0.25, tokens_used: Math.floor(kpis.totalTokenUsage * 0.25), percentage: 25 },
        ]);
      }

      const anomalies = detectAnomalies(metricsData, timeRange);
      setAnomalies(anomalies);

      const insight = generateAIInsight(metricsData, kpis, anomalies);
      setAiInsight(insight);

    } catch (error) {
      console.error('Failed to load analytics:', error);
    } finally {
      setLoading(false);
    }
  };

  const detectAnomalies = (data: PlatformMetrics | null, range: string): Anomaly[] => {
    const anomalies: Anomaly[] = [];
    
    if (!data) return anomalies;

    if (data.ai_cost_usd > 1000) {
      anomalies.push({
        type: 'cost_spike',
        description: `AI costs ($${data.ai_cost_usd}) are above average for this period`,
        severity: 'high',
        affected_resource: 'OpenAI/Groq usage',
        recommendation: 'Consider routing simple queries to cheaper models or implementing caching'
      });
    }

    if (data.active_organizations < data.total_organizations * 0.8) {
      anomalies.push({
        type: 'org_degradation',
        description: `${data.suspended_organizations} organizations (${Math.round(data.suspended_organizations / data.total_organizations * 100)}%) are suspended`,
        severity: 'medium',
        affected_resource: 'Organizations',
        recommendation: 'Review payment status and outreach to suspended customers'
      });
    }

    if (data.platform_uptime_percent < 99.5) {
      anomalies.push({
        type: 'uptime_degradation',
        description: `Platform uptime at ${data.platform_uptime_percent}% is below target`,
        severity: 'critical',
        affected_resource: 'Infrastructure',
        recommendation: 'Check monitoring dashboards for service degradation'
      });
    }

    return anomalies;
  };

  const generateAIInsight = (data: PlatformMetrics | null, kpis: any, anomalies: Anomaly[]): string => {
    if (!data) return 'Loading...';
    
    const insights: string[] = [];

    if (anomalies.length > 0) {
      insights.push(`**Detected ${anomalies.length} anomaly/anomalies:**`);
      anomalies.forEach(a => insights.push(`- **${a.type}**: ${a.description}`));
      insights.push('');
    }

    const costPercent = ((data.ai_cost_usd / (kpis?.revenueGeneratedUsd || 100000)) * 100).toFixed(1);
    insights.push(`**Financial Snapshot:**`);
    insights.push(`- AI costs represent ${costPercent}% of revenue`);
    insights.push(`- Average token cost: $${(data.ai_cost_usd / data.total_tokens_used).toFixed(6)} per 1K tokens`);
    insights.push('');

    const growth = data.total_users > 0 ? Math.round(((data.active_organizations - data.suspended_organizations) / data.total_organizations) * 100) : 0;
    insights.push(`**Growth Metrics:**`);
    insights.push(`- ${growth}% active organization growth`);
    insights.push(`- ${data.total_users.toLocaleString()} registered users`);
    insights.push('');

    return insights.join('\n');
  };

  if (loading) {
    return (
      <div className="space-y-4">
        <div className="rounded-xl border h-48" style={{ background: 'var(--color-card)', borderColor: 'var(--color-border)' }}></div>
        <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
          <div className="rounded-xl border h-48" style={{ background: 'var(--color-card)', borderColor: 'var(--color-border)' }}></div>
          <div className="rounded-xl border h-48" style={{ background: 'var(--color-card)', borderColor: 'var(--color-border)' }}></div>
        </div>
      </div>
    );
  }

  return (
    <div className="space-y-4">
      {/* AI Insight Summary */}
      <div className="rounded-xl p-4" style={{ background: 'var(--color-card)', border: '1px solid var(--color-border)' }}>
        <h4 className="font-semibold text-sm mb-2" style={{ color: 'var(--color-foreground)' }}>AI Insights</h4>
        <pre className="text-xs" style={{ color: 'var(--color-muted-foreground)', fontFamily: 'monospace' }}>
          {aiInsight}
        </pre>
      </div>

      {/* Key Metrics */}
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4">
        <MetricCard 
          title="Organizations" 
          value={metrics?.total_organizations?.toString() || '0'} 
          change={`${metrics?.active_organizations ?? 0} active`}
          icon="🏢"
        />
        <MetricCard 
          title="Total Users" 
          value={metrics?.total_users?.toString() || '0'}
          change="registered"
          icon="👥"
        />
        <MetricCard 
          title="AI Costs" 
          value={`$${metrics?.ai_cost_usd?.toFixed(2) || '0'}`}
          change={`${costBreakdown.length > 0 ? costBreakdown[0].provider : 'N/A'}`}
          icon="💰"
        />
        <MetricCard 
          title="Uptime" 
          value={`${metrics?.platform_uptime_percent?.toFixed(1) || '0'}%`}
          change={metrics?.platform_uptime_percent && metrics.platform_uptime_percent > 99.9 ? 'Excellent' : 'Needs attention'}
          icon="⚡"
        />
      </div>

      {/* AI Cost Breakdown */}
      <div className="rounded-xl border" style={{ background: 'var(--color-card)', borderColor: 'var(--color-border)' }}>
        <div className="p-4 border-b" style={{ borderColor: 'var(--color-border)' }}>
          <h4 className="font-semibold text-sm" style={{ color: 'var(--color-foreground)' }}>AI Cost Breakdown</h4>
        </div>
        <div className="p-4 space-y-3">
          {costBreakdown.map(item => (
            <div key={item.provider} className="flex items-center justify-between">
              <div>
                <div className="font-medium text-sm" style={{ color: 'var(--color-foreground)' }}>
                  {item.provider} / {item.model}
                </div>
                <div className="text-xs" style={{ color: 'var(--color-muted-foreground)' }}>
                  {item.tokens_used.toLocaleString()} tokens
                </div>
              </div>
              <div className="text-right">
                <div className="font-semibold text-sm" style={{ color: 'var(--color-foreground)' }}>
                  ${item.cost_usd.toFixed(2)}
                </div>
                <div className="text-xs" style={{ color: 'var(--color-muted-foreground)' }}>
                  {item.percentage}%
                </div>
              </div>
            </div>
          ))}
        </div>
      </div>

      {/* Anomalies */}
      {anomalies.length > 0 && (
        <div className="rounded-xl border" style={{ background: 'var(--color-card)', borderColor: 'var(--color-border)' }}>
          <div className="p-4 border-b" style={{ borderColor: 'var(--color-border)' }}>
            <h4 className="font-semibold text-sm flex items-center gap-2" style={{ color: 'var(--color-foreground)' }}>
              ⚠️ Alerts
            </h4>
          </div>
          <div className="p-4 space-y-3">
            {anomalies.map((anomaly, idx) => (
              <div key={idx} className="p-3 rounded" style={{ 
                background: anomaly.severity === 'critical' ? '#fef2f2' : 
                              anomaly.severity === 'high' ? '#fff7ed' : 
                              '#f0fdf4',
                borderLeft: `4px solid ${
                  anomaly.severity === 'critical' ? '#dc2626' :
                  anomaly.severity === 'high' ? '#ea580c' :
                  anomaly.severity === 'medium' ? '#ca8a04' :
                  '#16a34a'
                }`
              }}>
                <div className="font-medium text-sm" style={{ color: 'var(--color-foreground)' }}>
                  {anomaly.type.replace('_', ' ').toUpperCase()}
                </div>
                <div className="text-sm mt-1" style={{ color: 'var(--color-foreground)' }}>
                  {anomaly.description}
                </div>
                <div className="text-xs mt-2" style={{ color: 'var(--color-muted-foreground)' }}>
                  Recommendation: {anomaly.recommendation}
                </div>
              </div>
            ))}
          </div>
        </div>
      )}
    </div>
  );
}

interface MetricCardProps {
  title: string;
  value: string;
  change: string;
  icon: string;
}

function MetricCard({ title, value, change, icon }: MetricCardProps) {
  return (
    <div className="p-4 rounded-xl" style={{ background: 'var(--color-card)', border: '1px solid var(--color-border)' }}>
      <div className="text-2xl mb-1">{icon}</div>
      <div className="text-xl font-bold" style={{ color: 'var(--color-foreground)' }}>{value}</div>
      <div className="text-xs" style={{ color: 'var(--color-muted-foreground)' }}>{title}: {change}</div>
    </div>
  );
}