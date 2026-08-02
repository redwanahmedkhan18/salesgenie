import React, { useState, useEffect } from 'react';

interface SecurityIncident {
  id: string;
  type: 'failed_login' | 'permission_escalation' | 'unusual_export' | 'geographic_anomaly' | 'brute_force';
  severity: 'low' | 'medium' | 'high' | 'critical';
  user_id?: string;
  user_email?: string;
  ip_address?: string;
  location?: string;
  timestamp: Date;
  description: string;
  resolved: boolean;
}

interface SecuritySummary {
  total_incidents: number;
  critical_incidents: number;
  high_incidents: number;
  medium_incidents: number;
  low_incidents: number;
  attack_attempts: number;
  blocked_ips: number;
}

interface AIThreatAssessment {
  risk_level: 'low' | 'moderate' | 'high' | 'critical';
  summary: string;
  recommendations: string[];
  detected_patterns: string[];
}

export default function SecurityCenter() {
  const [loading, setLoading] = useState(true);
  const [summary, setSummary] = useState<SecuritySummary | null>(null);
  const [incidents, setIncidents] = useState<SecurityIncident[]>([]);
  const [aiAssessment, setAiAssessment] = useState<AIThreatAssessment | null>(null);
  const [timeRange, setTimeRange] = useState<'1h' | '24h' | '7d'>('24h');

  useEffect(() => {
    loadSecurityData();
  }, [timeRange]);

  const loadSecurityData = async () => {
    setLoading(true);
    try {
      const summaryData = await generateSecuritySummary();
      setSummary(summaryData);

      const incidentData = await generateIncidents();
      setIncidents(incidentData);

      const aiAnalysis = await analyzeThreats();
      setAiAssessment(aiAnalysis);

    } catch (error) {
      console.error('Failed to load security data:', error);
    } finally {
      setLoading(false);
    }
  };

  const generateSecuritySummary = async (): Promise<SecuritySummary> => {
    return {
      total_incidents: 24,
      critical_incidents: 2,
      high_incidents: 5,
      medium_incidents: 8,
      low_incidents: 9,
      attack_attempts: 142,
      blocked_ips: 57
    };
  };

  const generateIncidents = async (): Promise<SecurityIncident[]> => {
    return [
      {
        id: '1',
        type: 'failed_login',
        severity: 'medium',
        user_email: 'admin@customer.com',
        ip_address: '203.0.113.45',
        location: 'Tokyo, Japan',
        timestamp: new Date(Date.now() - 30 * 60 * 1000),
        description: 'Multiple failed login attempts from unfamiliar location',
        resolved: true
      },
      {
        id: '2',
        type: 'brute_force',
        severity: 'high',
        user_email: 'support@business.com',
        ip_address: '198.51.100.23',
        timestamp: new Date(Date.now() - 2 * 60 * 60 * 1000),
        description: 'Brute force attack detected - 50+ attempts in 5 minutes',
        resolved: false
      },
      {
        id: '3',
        type: 'geographic_anomaly',
        severity: 'critical',
        user_email: 'super_admin@salesgenie.com',
        ip_address: '192.0.2.100',
        location: 'Moscow, Russia',
        timestamp: new Date(Date.now() - 1 * 60 * 60 * 1000),
        description: 'Admin login from unusual location during maintenance window',
        resolved: false
      }
    ];
  };

  const analyzeThreats = async (): Promise<AIThreatAssessment> => {
    if (!summary) return { risk_level: 'low', summary: 'Loading...', recommendations: [], detected_patterns: [] };

    const totalIncidents = summary.critical_incidents + summary.high_incidents + summary.medium_incidents;
    const riskLevel = totalIncidents > 10 ? 'high' : totalIncidents > 5 ? 'moderate' : 'low';

    const patterns: string[] = [];
    if (summary.attack_attempts > 100) {
      patterns.push('Increased brute force attempts');
    }
    if (summary.critical_incidents > 0) {
      patterns.push('Multiple critical incidents detected');
    }

    const recommendations: string[] = [];
    if (summary.critical_incidents > 0) {
      recommendations.push('Review admin account security settings');
      recommendations.push('Consider implementing MFA for all admin accounts');
    }
    if (patterns.length > 0) {
      recommendations.push('Enable additional monitoring for affected IP ranges');
    }
    recommendations.push('Review and rotate API keys if compromised');

    return {
      risk_level: riskLevel,
      summary: `Analyzing ${summary.total_incidents} security events in the last ${timeRange === '1h' ? 'hour' : timeRange === '24h' ? '24 hours' : '7 days'}. AI analysis ${riskLevel === 'low' ? 'shows no immediate threats' : 'indicates elevated risk'} based on detected patterns.`,
      recommendations,
      detected_patterns: patterns.length > 0 ? patterns : ['No unusual patterns detected']
    };
  };

  const getSeverityColor = (severity: string) => {
    switch (severity) {
      case 'critical': return '#dc2626';
      case 'high': return '#ea580c';
      case 'medium': return '#ca8a04';
      case 'low': return '#16a34a';
      default: return '#6b7280';
    }
  };

  const handleResolve = (incidentId: string) => {
    setIncidents(prev => prev.map(inc => 
      inc.id === incidentId ? { ...inc, resolved: true } : inc
    ));
  };

  if (loading) {
    return (
      <div className="space-y-4">
        <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
          {[...Array(3)].map((_, i) => (
            <div key={i} className="rounded-xl p-4" style={{ background: 'var(--color-card)', border: '1px solid var(--color-border)' }}>
              <div className="h-4 bg-gray-200 rounded mb-2"></div>
              <div className="h-8 bg-gray-200 rounded"></div>
            </div>
          ))}
        </div>
      </div>
    );
  }

  return (
    <div className="space-y-4">
      {/* AI Security Assessment */}
      <div className="rounded-xl p-4" style={{ background: 'var(--color-card)', border: '1px solid var(--color-border)' }}>
        <h4 className="font-semibold text-sm mb-2 flex items-center gap-2" style={{ color: 'var(--color-foreground)' }}>
          🛡️ AI Security Assessment
        </h4>
        <pre className="text-xs" style={{ color: 'var(--color-muted-foreground)', fontFamily: 'monospace' }}>
          {aiAssessment?.summary}
        </pre>
        {aiAssessment && aiAssessment.recommendations && aiAssessment.recommendations.length > 0 && (
          <div className="mt-3">
            <div className="text-xs font-medium mb-1" style={{ color: 'var(--color-foreground)' }}>Recommendations:</div>
            <ul className="text-xs list-disc list-inside" style={{ color: 'var(--color-muted-foreground)' }}>
              {aiAssessment.recommendations.map((rec, i) => (
                <li key={i}>{rec}</li>
              ))}
            </ul>
          </div>
        )}
      </div>

      {/* Security Summary */}
      <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
        <SecurityStatCard 
          title="Total Incidents" 
          value={summary?.total_incidents?.toString() || '0'} 
          color="#ef4444"
        />
        <SecurityStatCard 
          title="Blocked Attack Attempts" 
          value={summary?.blocked_ips?.toString() || '0'} 
          color="#10b981"
        />
        <SecurityStatCard 
          title="Current Risk Level" 
          value={aiAssessment?.risk_level?.toUpperCase() || 'LOW'} 
          color={getSeverityColor(aiAssessment?.risk_level || 'low')}
        />
      </div>

      {/* Recent Incidents */}
      <div className="rounded-xl border" style={{ background: 'var(--color-card)', borderColor: 'var(--color-border)' }}>
        <div className="p-4 border-b flex items-center justify-between" style={{ borderColor: 'var(--color-border)' }}>
          <h4 className="font-semibold text-sm" style={{ color: 'var(--color-foreground)' }}>Recent Security Events</h4>
          <select
            value={timeRange}
            onChange={(e) => setTimeRange(e.target.value as any)}
            className="px-2 py-1 text-xs rounded border"
            style={{ background: 'var(--color-card)', color: 'var(--color-foreground)', borderColor: 'var(--color-border)' }}
          >
            <option value="1h">Last 1 Hour</option>
            <option value="24h">Last 24 Hours</option>
            <option value="7d">Last 7 Days</option>
          </select>
        </div>
        <div className="p-4">
          {incidents.length > 0 ? (
            <div className="space-y-3">
              {incidents.map(incident => (
                <div key={incident.id} className="p-3 rounded" style={{ background: 'var(--color-card)', border: '1px solid var(--color-border)' }}>
                  <div className="flex items-center justify-between">
                    <div className="flex items-center gap-3">
                      <span 
                        className="w-3 h-3 rounded-full"
                        style={{ backgroundColor: getSeverityColor(incident.severity) }}
                      />
                      <div>
                        <div className="font-medium text-sm" style={{ color: 'var(--color-foreground)' }}>
                          {incident.type.replace('_', ' ').toUpperCase()}
                        </div>
                        <div className="text-xs" style={{ color: 'var(--color-muted-foreground)' }}>
                          {incident.description}
                        </div>
                        {incident.ip_address && (
                          <div className="text-xs" style={{ color: 'var(--color-muted-foreground)' }}>
                            IP: {incident.ip_address}{incident.location ? ` (${incident.location})` : ''}
                          </div>
                        )}
                      </div>
                    </div>
                    <div className="flex items-center gap-2">
                      <span className="text-xs px-2 py-0.5 rounded" style={{ 
                        background: getSeverityColor(incident.severity),
                        color: 'white'
                      }}>
                        {incident.severity.toUpperCase()}
                      </span>
                      {!incident.resolved && (
                        <button
                          onClick={() => handleResolve(incident.id)}
                          className="text-xs px-2 py-0.5 rounded"
                          style={{ background: 'var(--color-primary)', color: 'var(--color-on-primary)' }}
                        >
                          Mark Resolved
                        </button>
                      )}
                    </div>
                  </div>
                </div>
              ))}
            </div>
          ) : (
            <div className="text-center py-6" style={{ color: 'var(--color-muted-foreground)' }}>
              No security incidents detected in the selected time range.
            </div>
          )}
        </div>
      </div>
    </div>
  );
}

interface SecurityStatCardProps {
  title: string;
  value: string;
  color: string;
}

function SecurityStatCard({ title, value, color }: SecurityStatCardProps) {
  return (
    <div className="rounded-xl p-4" style={{ background: 'var(--color-card)', border: '1px solid var(--color-border)' }}>
      <div className="text-xs" style={{ color: 'var(--color-muted-foreground)' }}>{title}</div>
      <div className="text-xl font-bold mt-1" style={{ color }}>{value}</div>
    </div>
  );
}