import React, { useState, useEffect } from 'react';
import { useAuth } from '../../../auth/AuthProvider';
import { apiClient } from '../../../lib/api-client';
import type { Company, LeadScore, QualificationReport } from '../../../lib/types';

interface LeadCardProps {
  company: Company;
  score: LeadScore | null;
  onViewDetails: (company: Company) => void;
}

function LeadCard({ company, score, onViewDetails }: LeadCardProps) {
  return (
    <div className="rounded-xl border p-4" style={{ background: 'var(--color-card)', borderColor: 'var(--color-border)' }}>
      <div className="flex items-start justify-between">
        <div className="flex-1">
          <h3 className="font-semibold text-sm" style={{ color: 'var(--color-foreground)' }}>{company.name}</h3>
          <p className="text-xs mt-0.5" style={{ color: 'var(--color-muted-foreground)' }}>
            {company.industry} • {company.employee_count ? `${company.employee_count.toLocaleString()} employees` : 'Unknown size'}
          </p>
          {company.description && (
            <p className="text-xs mt-1 line-clamp-2" style={{ color: 'var(--color-muted-foreground)' }}>
              {company.description}
            </p>
          )}
        </div>
        {score && (
          <div className="text-right">
            <div className="text-xl font-bold" style={{ color: score.total_score >= 70 ? '#2c8c66' : score.total_score >= 50 ? '#f7a501' : '#cd4239' }}>
              {score.total_score}
            </div>
            <div className="text-xs" style={{ color: 'var(--color-muted-foreground)' }}>Lead Score</div>
          </div>
        )}
      </div>
      <div className="flex gap-2 mt-3">
        <button
          onClick={() => onViewDetails(company)}
          className="flex-1 text-xs px-3 py-1.5 rounded border transition-colors"
          style={{ borderColor: 'var(--color-border)', color: 'var(--color-muted-foreground)' }}
        >
          Details
        </button>
        <button
          className="flex-1 text-xs px-3 py-1.5 rounded font-semibold transition-colors"
          style={{ background: 'var(--color-primary)', color: 'var(--color-on-primary)' }}
        >
          Qualify
        </button>
      </div>
    </div>
  );
}

export function LeadIntelligence() {
  const { hasRole, hasAnyRole } = useAuth();
  const [companies, setCompanies] = useState<Company[]>([]);
  const [selectedCompany, setSelectedCompany] = useState<Company | null>(null);
  const [leadScore, setLeadScore] = useState<LeadScore | null>(null);
  const [researchReport, setResearchReport] = useState<QualificationReport | null>(null);
  const [loading, setLoading] = useState(true);
  const [searchQuery, setSearchQuery] = useState('');
  const [activeTab, setActiveTab] = useState<'discover' | 'qualified' | 'research'>('discover');
  const [industryFilter, setIndustryFilter] = useState('');
  const [locationFilter, setLocationFilter] = useState('');

  useEffect(() => {
    if (activeTab === 'discover') {
      searchCompanies();
    }
  }, [activeTab, searchQuery, industryFilter, locationFilter]);

  const searchCompanies = async () => {
    setLoading(true);
    try {
      const results = await apiClient.searchCompanies({
        industry: industryFilter || undefined,
        location: locationFilter || undefined,
        keywords: searchQuery || undefined,
      });
      setCompanies(results);
    } catch (error) {
      console.error('Failed to search companies:', error);
    } finally {
      setLoading(false);
    }
  };

  const handleQualify = async (company: Company) => {
    const score = await apiClient.qualifyLead(company.id);
    if (score) {
      setLeadScore(score);
      setSelectedCompany(company);
    }
  };

  const handleGenerateResearch = async (company: Company) => {
    const report = await apiClient.generateResearchBrief(company.id);
    if (report) {
      setResearchReport(report);
      setSelectedCompany(company);
    }
  };

  const handleGenerateOutreach = async (company: Company, channel: 'email' | 'linkedin' | 'whatsapp') => {
    const draft = await apiClient.generateOutreachDraft(company.id, channel);
    if (draft) {
      alert(`Generated ${channel} outreach draft for ${company.name}`);
    }
  };

  if (!hasAnyRole(['org_admin', 'super_admin', 'sales_manager', 'sales_agent', 'knowledge_manager'])) {
    return (
      <div className="flex items-center justify-center min-h-screen" style={{ background: 'var(--color-background)' }}>
        <div className="text-center p-8 rounded-xl" style={{ background: 'var(--color-card)', border: '1px solid var(--color-border)' }}>
          <div className="text-4xl mb-4">🔒</div>
          <h2 className="text-xl font-bold mb-2" style={{ color: 'var(--color-foreground)' }}>Access Denied</h2>
          <p className="text-sm" style={{ color: 'var(--color-muted-foreground)' }}>
            You don't have permission to access Lead Intelligence.
          </p>
        </div>
      </div>
    );
  }

  return (
    <div className="p-6 space-y-6">
      <div className="flex items-center justify-between">
        <div>
          <h1 className="text-2xl font-bold" style={{ color: 'var(--color-foreground)' }}>AI Lead Intelligence Engine</h1>
          <p className="text-sm mt-0.5" style={{ color: 'var(--color-muted-foreground)' }}>
            Discover, qualify, and engage high-quality prospects with AI
          </p>
        </div>
      </div>

      {/* Tabs */}
      <div className="flex gap-1 p-1 rounded-lg" style={{ background: 'var(--color-muted)' }}>
        {['discover', 'qualified', 'research'].map(tab => (
          <button
            key={tab}
            onClick={() => setActiveTab(tab as any)}
            className={`flex-1 px-4 py-2 text-sm font-semibold rounded-md transition-all ${activeTab === tab ? 'shadow' : ''}`}
            style={{
              background: activeTab === tab ? 'var(--color-card)' : 'transparent',
              color: activeTab === tab ? 'var(--color-foreground)' : 'var(--color-muted-foreground)',
            }}
          >
            {tab === 'discover' ? 'Discover Leads' : tab === 'qualified' ? 'Qualified Leads' : 'Research'}
          </button>
        ))}
      </div>

      {/* Discover Tab */}
      {activeTab === 'discover' && (
        <div className="space-y-4">
          {/* Search Filters */}
          <div className="flex flex-col sm:flex-row gap-3">
            <input
              type="text"
              value={searchQuery}
              onChange={e => setSearchQuery(e.target.value)}
              placeholder="Search companies, industries, keywords..."
              className="flex-1 px-4 py-2.5 rounded-xl text-sm outline-none"
              style={{ background: 'var(--color-card)', color: 'var(--color-foreground)', border: '1px solid var(--color-border)' }}
            />
            <input
              type="text"
              value={industryFilter}
              onChange={e => setIndustryFilter(e.target.value)}
              placeholder="Industry"
              className="px-4 py-2.5 rounded-xl text-sm outline-none"
              style={{ background: 'var(--color-card)', color: 'var(--color-foreground)', border: '1px solid var(--color-border)' }}
            />
            <input
              type="text"
              value={locationFilter}
              onChange={e => setLocationFilter(e.target.value)}
              placeholder="Location"
              className="px-4 py-2.5 rounded-xl text-sm outline-none"
              style={{ background: 'var(--color-card)', color: 'var(--color-foreground)', border: '1px solid var(--color-border)' }}
            />
            <button
              onClick={searchCompanies}
              className="px-4 py-2.5 rounded-xl font-semibold text-sm"
              style={{ background: 'var(--color-primary)', color: 'var(--color-on-primary)' }}
            >
              Search
            </button>
          </div>

          {/* Results */}
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
            {loading ? (
              Array.from({ length: 6 }).map((_, i) => (
                <div key={i} className="rounded-xl border p-4" style={{ background: 'var(--color-card)', borderColor: 'var(--color-border)' }}>
                  <div className="skeleton h-4 w-full rounded mb-2" />
                  <div className="skeleton h-3 w-3/4 rounded mb-2" />
                  <div className="skeleton h-3 w-1/2 rounded" />
                </div>
              ))
            ) : companies.length === 0 ? (
              <div className="col-span-full text-center py-8" style={{ color: 'var(--color-muted-foreground)' }}>
                <div className="text-3xl mb-4">🔍</div>
                <p>No companies found matching your criteria</p>
              </div>
            ) : (
              companies.map(company => (
                <LeadCard
                  key={company.id}
                  company={company}
                  score={null}
                  onViewDetails={() => setSelectedCompany(company)}
                />
              ))
            )}
          </div>
        </div>
      )}

      {/* Research Modal */}
      {selectedCompany && activeTab === 'discover' && (
        <div className="fixed inset-0 bg-black/50 flex items-center justify-center z-50">
          <div className="rounded-2xl p-6 w-full max-w-2xl max-h-[80vh] overflow-y-auto" style={{ background: 'var(--color-card)', border: '1px solid var(--color-border)' }}>
            <div className="flex items-center justify-between mb-4">
              <h2 className="text-xl font-bold" style={{ color: 'var(--color-foreground)' }}>{selectedCompany.name}</h2>
              <button onClick={() => setSelectedCompany(null)} className="text-xl" style={{ color: 'var(--color-muted-foreground)' }}>✕</button>
            </div>
            
            {researchReport ? (
              <div className="space-y-4">
                <div>
                  <h3 className="font-semibold text-sm" style={{ color: 'var(--color-foreground)' }}>Business Summary</h3>
                  <p className="text-sm mt-1" style={{ color: 'var(--color-muted-foreground)' }}>{researchReport.business_summary}</p>
                </div>
                <div>
                  <h3 className="font-semibold text-sm" style={{ color: 'var(--color-foreground)' }}>Opportunity Assessment</h3>
                  <p className="text-sm mt-1" style={{ color: 'var(--color-muted-foreground)' }}>{researchReport.opportunity_assessment}</p>
                </div>
                <div>
                  <h3 className="font-semibold text-sm" style={{ color: 'var(--color-foreground)' }}>Recommended Pitch</h3>
                  <p className="text-sm mt-1" style={{ color: 'var(--color-muted-foreground)' }}>{researchReport.recommended_pitch}</p>
                </div>
              </div>
            ) : (
              <div className="space-y-3">
                <button
                  onClick={() => handleGenerateResearch(selectedCompany)}
                  className="w-full px-4 py-2.5 rounded-xl font-semibold text-sm"
                  style={{ background: 'var(--color-primary)', color: 'var(--color-on-primary)' }}
                >
                  Generate AI Research Brief
                </button>
                <button
                  onClick={() => handleQualify(selectedCompany)}
                  className="w-full px-4 py-2.5 rounded-xl font-semibold text-sm"
                  style={{ background: 'var(--color-secondary)', color: 'var(--color-on-secondary)' }}
                >
                  Qualify Lead
                </button>
              </div>
            )}
          </div>
        </div>
      )}
    </div>
  );
}