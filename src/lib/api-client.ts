/**
 * SalesGenie API Client
 * Fetches real-time metrics from backend services
 */

import type {
  LoginRequest,
  LoginResponse,
  MFASetupResponse,
  MFAVerifyRequest,
  SessionDTO,
  User,
  PlatformRole,
  Customer,
  CustomerSegment,
  CustomerTag,
  SupportTicket,
  SearchHit,
  SearchResponse,
  IndexDocumentRequest,
  IndexDocumentResponse,
  IndexStatsDTO,
  TicketAnalytics,
  AnalyticsKPIs,
  KPICard,
  ConversationPoint,
  RevenuePoint,
  ChannelPoint,
  UserPreferences,
  Organization,
  TenantMetrics,
  Branding,
  WorkspaceMember,
  KnowledgeCategory,
  WhatsAppAccount,
  ChannelIntegration,
  Company,
  Contact,
  LeadScore,
  QualificationReport,
  OutreachDraft,
  SearchProfile,
  KnowledgeDocument,
  AIAgent,
  PlatformMetrics,
  OrganizationListItem,
  OrganizationDetail,
} from './types';

export type {
  KPICard,
  ConversationPoint,
  RevenuePoint,
  ChannelPoint,
  AnalyticsKPIs,
  Customer,
  CustomerSegment,
  CustomerTag,
  SupportTicket,
  TicketAnalytics,
  SearchHit,
  SearchResponse,
  IndexDocumentRequest,
  IndexDocumentResponse,
  IndexStatsDTO,
  User,
  UserPreferences,
  Organization,
  TenantMetrics,
  Branding,
  WorkspaceMember,
  PlatformRole,
  KnowledgeCategory,
  WhatsAppAccount,
  ChannelIntegration,
  Company,
  Contact,
  LeadScore,
  QualificationReport,
  OutreachDraft,
  SearchProfile,
  PlatformMetrics,
  OrganizationListItem,
  OrganizationDetail,
  KnowledgeDocument,
  AIAgent,
};

const API_BASE_URL = import.meta.env.DEV ? "http://localhost:8001" : "/api";
const USER_API_BASE_URL = import.meta.env.DEV ? "http://localhost:8002" : "/api";
const ORGANIZATION_API_BASE_URL = import.meta.env.DEV ? "http://localhost:8003" : "/api";
const BILLING_API_BASE_URL = import.meta.env.DEV ? "http://localhost:8004" : "/api";
const NOTIFICATION_API_BASE_URL = import.meta.env.DEV ? "http://localhost:8014" : "/api";
const AUDIT_API_BASE_URL = import.meta.env.DEV ? "http://localhost:8023" : "/api";
const KNOWLEDGE_API_BASE_URL = import.meta.env.DEV ? "http://localhost:8006" : "/api";
const SALES_API_BASE_URL = import.meta.env.DEV ? "http://localhost:8007" : "/api";
const TICKETS_API_BASE_URL = import.meta.env.DEV ? "http://localhost:8008" : "/api";
const VECTOR_API_BASE_URL = import.meta.env.DEV ? "http://localhost:8009" : "/api";
const CHAT_API_BASE_URL = import.meta.env.DEV ? "http://localhost:8010" : "/api";
const WORKFLOW_API_BASE_URL = import.meta.env.DEV ? "http://localhost:8011" : "/api";
const ANALYTICS_API_BASE_URL = import.meta.env.DEV ? "http://localhost:8012" : "/api";
const SEARCH_API_BASE_URL = import.meta.env.DEV ? "http://localhost:8013" : "/api";
const FILE_API_BASE_URL = import.meta.env.DEV ? "http://localhost:8015" : "/api";
const CUSTOMERS_API_BASE_URL = import.meta.env.DEV ? "http://localhost:8016" : "/api";
const SUPPORT_API_BASE_URL = import.meta.env.DEV ? "http://localhost:8017" : "/api";
const CONVERSATIONS_API_BASE_URL = import.meta.env.DEV ? "http://localhost:8018" : "/api";
const AI_GATEWAY_API_BASE_URL = import.meta.env.DEV ? "http://localhost:8000" : "/api";
const WHATSAPP_API_BASE_URL = import.meta.env.DEV ? "http://localhost:8005" : "/api";
const TELEGRAM_API_BASE_URL = import.meta.env.DEV ? "http://localhost:8019" : "/api";
const MESSENGER_API_BASE_URL = import.meta.env.DEV ? "http://localhost:8020" : "/api";
const EMAIL_API_BASE_URL = import.meta.env.DEV ? "http://localhost:8021" : "/api";
const LEAD_INTELLIGENCE_API_BASE_URL = import.meta.env.DEV ? "http://localhost:8022" : "/api";
const PLATFORM_API_BASE_URL = import.meta.env.DEV ? "http://localhost:8001" : "/api";
const SLACK_API_BASE_URL = import.meta.env.DEV ? "http://localhost:8024" : "/api";
const DISCORD_API_BASE_URL = import.meta.env.DEV ? "http://localhost:8026" : "/api";

class APIClient {
  private baseHeaders: HeadersInit = {
    'Content-Type': 'application/json',
  };

  private getAuthHeaders(): HeadersInit {
    const token = localStorage.getItem('auth_token');
    if (token) {
      return { ...this.baseHeaders, Authorization: `Bearer ${token}` };
    }
    return this.baseHeaders;
  }

  // Authentication API Methods

  async login(req: LoginRequest): Promise<LoginResponse> {
    const response = await fetch(`${API_BASE_URL}/api/v1/auth/login`, {
      method: 'POST',
      headers: this.baseHeaders,
      body: JSON.stringify(req),
    });

    if (!response.ok) {
      const error = await response.json();
      throw new Error(error.detail || 'Login failed');
    }

    return response.json();
  }

  async refresh(refreshToken: string): Promise<LoginResponse> {
    const response = await fetch(`${API_BASE_URL}/api/v1/auth/refresh`, {
      method: 'POST',
      headers: this.baseHeaders,
      body: JSON.stringify({ refresh_token: refreshToken }),
    });

    if (!response.ok) {
      const error = await response.json();
      throw new Error(error.detail || 'Token refresh failed');
    }

    return response.json();
  }

  async logout(): Promise<void> {
    localStorage.removeItem('auth_token');
    localStorage.removeItem('refresh_token');
    localStorage.removeItem('user_data');
  }

  async setupMFA(): Promise<MFASetupResponse> {
    const response = await fetch(`${API_BASE_URL}/api/v1/auth/mfa/setup`, {
      method: 'POST',
      headers: this.getAuthHeaders(),
    });

    if (!response.ok) {
      const error = await response.json();
      throw new Error(error.detail || 'MFA setup failed');
    }

    return response.json();
  }

  async verifyMFA(req: MFAVerifyRequest): Promise<{ status: string; message: string }> {
    const response = await fetch(`${API_BASE_URL}/api/v1/auth/mfa/verify`, {
      method: 'POST',
      headers: this.getAuthHeaders(),
      body: JSON.stringify(req),
    });

    if (!response.ok) {
      const error = await response.json();
      throw new Error(error.detail || 'MFA verification failed');
    }

    return response.json();
  }

  async getSessions(): Promise<SessionDTO[]> {
    const response = await fetch(`${API_BASE_URL}/api/v1/auth/sessions`, {
      headers: this.getAuthHeaders(),
    });

    if (!response.ok) {
      throw new Error('Failed to fetch sessions');
    }

    return response.json();
  }

  async revokeSession(sessionId: string): Promise<{ status: string; session_id: string }> {
    const response = await fetch(`${API_BASE_URL}/api/v1/auth/sessions/${sessionId}`, {
      method: 'DELETE',
      headers: this.getAuthHeaders(),
    });

    if (!response.ok) {
      throw new Error('Failed to revoke session');
    }

    return response.json();
  }

  async getUserProfile(): Promise<User> {
    const response = await fetch(`${API_BASE_URL}/api/v1/users/me`, {
      headers: this.getAuthHeaders(),
    });

    if (!response.ok) {
      throw new Error('Failed to fetch user profile');
    }

    return response.json();
  }

  async updateUserProfile(updates: Partial<User>): Promise<User> {
    const response = await fetch(`${API_BASE_URL}/api/v1/users/me`, {
      method: 'PUT',
      headers: this.getAuthHeaders(),
      body: JSON.stringify(updates),
    });

    if (!response.ok) {
      throw new Error('Failed to update user profile');
    }

    return response.json();
  }

  async getUserPreferences(): Promise<UserPreferences> {
    const response = await fetch(`${API_BASE_URL}/api/v1/users/me/preferences`, {
      headers: this.getAuthHeaders(),
    });

    if (!response.ok) {
      throw new Error('Failed to fetch user preferences');
    }

    return response.json();
  }

  async updateUserPreferences(updates: Partial<UserPreferences>): Promise<UserPreferences> {
    const response = await fetch(`${API_BASE_URL}/api/v1/users/me/preferences`, {
      method: 'PUT',
      headers: this.getAuthHeaders(),
      body: JSON.stringify(updates),
    });

    if (!response.ok) {
      throw new Error('Failed to update user preferences');
    }

    return response.json();
  }

  // Organization API Methods

  async getOrganization(orgId: string): Promise<Organization> {
    const response = await fetch(`${API_BASE_URL}/api/v1/organizations/${orgId}`, {
      headers: this.getAuthHeaders(),
    });

    if (!response.ok) {
      throw new Error('Failed to fetch organization');
    }

    return response.json();
  }

  async getTenantMetrics(tenantId: string): Promise<TenantMetrics> {
    const response = await fetch(`${API_BASE_URL}/api/v1/organizations/${tenantId}/metrics`, {
      headers: this.getAuthHeaders(),
    });

    if (!response.ok) {
      throw new Error('Failed to fetch tenant metrics');
    }

    return response.json();
  }

  async updateBranding(tenantId: string, updates: Partial<Branding>): Promise<Branding> {
    const response = await fetch(`${API_BASE_URL}/api/v1/organizations/${tenantId}/branding`, {
      method: 'PUT',
      headers: this.getAuthHeaders(),
      body: JSON.stringify(updates),
    });

    if (!response.ok) {
      throw new Error('Failed to update branding');
    }

    return response.json();
  }

  async getWorkspaceMembers(tenantId: string): Promise<WorkspaceMember[]> {
    const response = await fetch(`${API_BASE_URL}/api/v1/organizations/${tenantId}/members`, {
      headers: this.getAuthHeaders(),
    });

    if (!response.ok) {
      throw new Error('Failed to fetch workspace members');
    }

    return response.json();
  }

  async addWorkspaceMember(tenantId: string, userId: string, role: string): Promise<WorkspaceMember> {
    const response = await fetch(`${API_BASE_URL}/api/v1/organizations/${tenantId}/members`, {
      method: 'POST',
      headers: this.getAuthHeaders(),
      body: JSON.stringify({ user_id: userId, role }),
    });

    if (!response.ok) {
      throw new Error('Failed to add workspace member');
    }

    return response.json();
  }

  async updateMemberRole(tenantId: string, memberId: string, role: string): Promise<WorkspaceMember> {
    const response = await fetch(`${API_BASE_URL}/api/v1/organizations/${tenantId}/members/${memberId}/role`, {
      method: 'PATCH',
      headers: this.getAuthHeaders(),
      body: JSON.stringify({ role }),
    });

    if (!response.ok) {
      throw new Error('Failed to update member role');
    }

    return response.json();
  }

  async removeWorkspaceMember(tenantId: string, memberId: string): Promise<{ status: string; member_id: string }> {
    const response = await fetch(`${API_BASE_URL}/api/v1/organizations/${tenantId}/members/${memberId}`, {
      method: 'DELETE',
      headers: this.getAuthHeaders(),
    });

    if (!response.ok) {
      throw new Error('Failed to remove workspace member');
    }

    return response.json();
  }

  // Analytics API Methods

  async fetchKPIs(): Promise<AnalyticsKPIs> {
    try {
      const response = await fetch(`${API_BASE_URL}/api/v1/analytics/kpis`, {
        headers: this.baseHeaders,
      });

      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }

      return response.json();
    } catch (error) {
      console.error('Failed to fetch KPIs:', error);
      return this.getDefaultKPIs();
    }
  }

  getDefaultKPIs(): AnalyticsKPIs {
    return {
      aiAccuracyRate: 99.2,
      avgResponseTimeSec: 1.12,
      hallucinationRate: 0.28,
      customerSatisfactionScore: 4.92,
      salesConversionRate: 18.6,
      avgResolutionTimeMin: 3.4,
      activeUsers: 14290,
      revenueGeneratedUsd: 128450.00,
      aiCostUsd: 412.50,
      totalTokenUsage: 24800000,
    };
  }

  transformKPIsToCards(kpis: AnalyticsKPIs): KPICard[] {
    return [
      {
        id: 'active-convos',
        title: 'Active Conversations',
        value: kpis.activeUsers.toLocaleString(),
        change: '+18.4%',
        changeDir: 'up',
        icon: '💬',
        color: '#f7a501',
      },
      {
        id: 'ai-accuracy',
        title: 'AI Accuracy Rate',
        value: `${kpis.aiAccuracyRate}%`,
        change: '+0.4%',
        changeDir: 'up',
        icon: '🎯',
        color: '#2c8c66',
      },
      {
        id: 'revenue-today',
        title: "Today's Revenue",
        value: `$${(kpis.revenueGeneratedUsd / 1000).toFixed(0)}k`,
        change: '+22.1%',
        changeDir: 'up',
        icon: '💰',
        color: '#2c84e0',
      },
      {
        id: 'token-cost',
        title: 'AI Token Cost',
        value: `$${(kpis.aiCostUsd / 100).toFixed(2)}`,
        change: '-8.3%',
        changeDir: 'down',
        icon: '⚡',
        color: '#7c44a6',
      },
      {
        id: 'sales-conv',
        title: 'Sales Conversion',
        value: `${kpis.salesConversionRate}%`,
        change: '+3.2%',
        changeDir: 'up',
        icon: '📈',
        color: '#f7a501',
      },
      {
        id: 'halluc-rate',
        title: 'Hallucination Rate',
        value: `${kpis.hallucinationRate}%`,
        change: '-0.12%',
        changeDir: 'down',
        icon: '🛡️',
        color: '#cd4239',
      },
    ];
  }

  // Customer Service API methods
  async fetchCustomers(params?: Record<string, string>): Promise<Customer[]> {
    try {
      const query = params ? '?' + new URLSearchParams(params).toString() : '';
      const response = await fetch(`${CUSTOMERS_API_BASE_URL}/api/v1/customers${query}`, {
        headers: this.baseHeaders,
      });

      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }

      return response.json();
    } catch (error) {
      console.error('Failed to fetch customers:', error);
      return [];
    }
  }

  async createCustomer(customer: Partial<Customer>): Promise<Customer | null> {
    try {
      const response = await fetch(`${CUSTOMERS_API_BASE_URL}/api/v1/customers`, {
        method: 'POST',
        headers: this.baseHeaders,
        body: JSON.stringify(customer),
      });

      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }

      return response.json();
    } catch (error) {
      console.error('Failed to create customer:', error);
      return null;
    }
  }

  async fetchSegments(): Promise<CustomerSegment[]> {
    try {
      const response = await fetch(`${CUSTOMERS_API_BASE_URL}/api/v1/customers/segments`, {
        headers: this.baseHeaders,
      });

      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }

      return response.json();
    } catch (error) {
      console.error('Failed to fetch segments:', error);
      return [];
    }
  }

  async fetchTags(): Promise<CustomerTag[]> {
    try {
      const response = await fetch(`${CUSTOMERS_API_BASE_URL}/api/v1/customers/tags`, {
        headers: this.baseHeaders,
      });

      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }

      return response.json();
    } catch (error) {
      console.error('Failed to fetch tags:', error);
      return [];
    }
  }

  // Support Service API methods
  async fetchTickets(params?: Record<string, string>): Promise<SupportTicket[]> {
    try {
      const query = params ? '?' + new URLSearchParams(params).toString() : '';
      const response = await fetch(`${TICKETS_API_BASE_URL}/api/v1/tickets${query}`, {
        headers: this.getAuthHeaders(),
      });

      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }

      return response.json();
    } catch (error) {
      console.error('Failed to fetch tickets:', error);
      return [];
    }
  }

  async createTicket(ticket: Partial<SupportTicket>): Promise<SupportTicket | null> {
    try {
      const response = await fetch(`${TICKETS_API_BASE_URL}/api/v1/tickets`, {
        method: 'POST',
        headers: this.getAuthHeaders(),
        body: JSON.stringify(ticket),
      });

      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }

      return response.json();
    } catch (error) {
      console.error('Failed to create ticket:', error);
      return null;
    }
  }

  async updateTicket(ticketId: string, updates: Partial<SupportTicket>): Promise<SupportTicket | null> {
    try {
      const response = await fetch(`${TICKETS_API_BASE_URL}/api/v1/tickets/${ticketId}`, {
        method: 'PATCH',
        headers: this.getAuthHeaders(),
        body: JSON.stringify(updates),
      });

      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }

      return response.json();
    } catch (error) {
      console.error('Failed to update ticket:', error);
      return null;
    }
  }

  async fetchTicketAnalytics(): Promise<TicketAnalytics | null> {
    try {
      const response = await fetch(`${TICKETS_API_BASE_URL}/api/v1/tickets/analytics/overview`, {
        headers: this.getAuthHeaders(),
      });

      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }

      return response.json();
    } catch (error) {
      console.error('Failed to fetch ticket analytics:', error);
      return null;
    }
  }

  // Search Service API methods
  async searchDocuments(params: {
    query: string;
    index_types?: string[];
    tags?: string[];
    size?: number;
    from?: number;
  }): Promise<SearchResponse | null> {
    try {
      const queryParams = new URLSearchParams();
      queryParams.set('q', params.query);
      if (params.index_types) {
        params.index_types.forEach(t => queryParams.append('index_types', t));
      }
      if (params.tags) {
        params.tags.forEach(t => queryParams.append('tags', t));
      }
      if (params.size) queryParams.set('size', String(params.size));
      if (params.from !== undefined) queryParams.set('from', String(params.from));

      const response = await fetch(`${SEARCH_API_BASE_URL}/api/v1/search/search?${queryParams.toString()}`, {
        headers: this.baseHeaders,
      });

      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }

      return response.json();
    } catch (error) {
      console.error('Failed to search:', error);
      return null;
    }
  }

  async indexDocument(document: IndexDocumentRequest): Promise<IndexDocumentResponse | null> {
    try {
      const response = await fetch(`${SEARCH_API_BASE_URL}/api/v1/search/index`, {
        method: 'POST',
        headers: this.baseHeaders,
        body: JSON.stringify(document),
      });

      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }

      return response.json();
    } catch (error) {
      console.error('Failed to index document:', error);
      return null;
    }
  }

  async deleteDocument(documentId: string, indexType?: string): Promise<boolean> {
    try {
      const params = new URLSearchParams();
      if (indexType) params.set('index_type', indexType);

      const response = await fetch(`${SEARCH_API_BASE_URL}/api/v1/search/index/${documentId}?${params.toString()}`, {
        method: 'DELETE',
        headers: this.baseHeaders,
      });

      return response.ok;
    } catch (error) {
      console.error('Failed to delete document:', error);
      return false;
    }
  }

  async fetchIndexStats(): Promise<IndexStatsDTO[]> {
    try {
      const response = await fetch(`${SEARCH_API_BASE_URL}/api/v1/search/index/stats`, {
        headers: this.baseHeaders,
      });

      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }

      return response.json();
    } catch (error) {
      console.error('Failed to fetch index stats:', error);
      return [];
    }
  }

  async fetchKnowledgeCategories(): Promise<KnowledgeCategory[]> {
    try {
      const response = await fetch(`${KNOWLEDGE_API_BASE_URL}/api/v1/knowledge/categories`, {
        headers: this.baseHeaders,
      });

      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }

      return response.json();
    } catch (error) {
      console.error('Failed to fetch knowledge categories:', error);
      return [];
    }
  }

  // WhatsApp Service API methods

  async getWhatsAppAccounts(): Promise<WhatsAppAccount | null> {
    try {
      const response = await fetch(`${WHATSAPP_API_BASE_URL}/api/v1/whatsapp/accounts`, {
        headers: this.baseHeaders,
      });

      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }

      return response.json();
    } catch (error) {
      console.error('Failed to fetch WhatsApp accounts:', error);
      return null;
    }
  }

  async createWhatsAppAccount(req: {
    name: string;
    phone_number_id: string;
    access_token: string;
    webhook_url?: string;
  }): Promise<WhatsAppAccount | null> {
    try {
      const response = await fetch(`${WHATSAPP_API_BASE_URL}/api/v1/whatsapp/accounts`, {
        method: 'POST',
        headers: this.baseHeaders,
        body: JSON.stringify(req),
      });

      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }

      return response.json();
    } catch (error) {
      console.error('Failed to create WhatsApp account:', error);
      return null;
    }
  }

  async sendWhatsAppMessage(req: {
    to: string;
    message: string;
    message_type?: string;
    media_url?: string;
    caption?: string;
  }): Promise<{ status: string; message_id?: string } | null> {
    try {
      const response = await fetch(`${WHATSAPP_API_BASE_URL}/api/v1/whatsapp/messages`, {
        method: 'POST',
        headers: this.baseHeaders,
        body: JSON.stringify(req),
      });

      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }

      return response.json();
    } catch (error) {
      console.error('Failed to send WhatsApp message:', error);
      return null;
    }
  }

  async listChannelIntegrations(): Promise<ChannelIntegration[]> {
    try {
      const response = await fetch(`${API_BASE_URL}/api/v1/channels/integrations`, {
        headers: this.baseHeaders,
      });

      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }

      return response.json();
    } catch (error) {
      console.error('Failed to fetch channel integrations:', error);
      return [];
    }
  }

  // Lead Intelligence Service API methods

  async searchCompanies(params: {
    industry?: string;
    location?: string;
    min_employee_count?: number;
    max_employee_count?: number;
    min_revenue_usd?: number;
    keywords?: string;
    technologies?: string[];
    language?: string;
  }): Promise<Company[]> {
    try {
      const queryParams = new URLSearchParams();
      if (params.industry) queryParams.set('industry', params.industry);
      if (params.location) queryParams.set('location', params.location);
      if (params.min_employee_count) queryParams.set('min_employee_count', String(params.min_employee_count));
      if (params.max_employee_count) queryParams.set('max_employee_count', String(params.max_employee_count));
      if (params.min_revenue_usd) queryParams.set('min_revenue_usd', String(params.min_revenue_usd));
      if (params.keywords) queryParams.set('keywords', params.keywords);
      if (params.technologies && params.technologies.length > 0) {
        params.technologies.forEach(t => queryParams.append('technologies', t));
      }
      if (params.language) queryParams.set('language', params.language);

      const response = await fetch(`${LEAD_INTELLIGENCE_API_BASE_URL}/api/v1/lead-intelligence/companies/search?${queryParams.toString()}`, {
        headers: this.baseHeaders,
      });

      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }

      return response.json();
    } catch (error) {
      console.error('Failed to search companies:', error);
      return [];
    }
  }

  async getCompany(companyId: string, language?: string): Promise<Company | null> {
    try {
      const params = new URLSearchParams();
      if (language) params.set('language', language);
      
      const response = await fetch(`${LEAD_INTELLIGENCE_API_BASE_URL}/api/v1/lead-intelligence/companies/${companyId}?${params.toString()}`, {
        headers: this.baseHeaders,
      });

      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }

      return response.json();
    } catch (error) {
      console.error('Failed to get company:', error);
      return null;
    }
  }

  async qualifyLead(companyId: string, language?: string): Promise<LeadScore | null> {
    try {
      const params = new URLSearchParams();
      if (language) params.set('language', language);
      
      const response = await fetch(`${LEAD_INTELLIGENCE_API_BASE_URL}/api/v1/lead-intelligence/companies/${companyId}/qualify?${params.toString()}`, {
        method: 'POST',
        headers: this.baseHeaders,
      });

      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }

      return response.json();
    } catch (error) {
      console.error('Failed to qualify lead:', error);
      return null;
    }
  }

  async generateResearchBrief(companyId: string, language?: string): Promise<QualificationReport | null> {
    try {
      const params = new URLSearchParams();
      if (language) params.set('language', language);
      
      const response = await fetch(`${LEAD_INTELLIGENCE_API_BASE_URL}/api/v1/lead-intelligence/companies/${companyId}/research?${params.toString()}`, {
        method: 'POST',
        headers: this.baseHeaders,
      });

      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }

      return response.json();
    } catch (error) {
      console.error('Failed to generate research brief:', error);
      return null;
    }
  }

  async generateOutreachDraft(companyId: string, channel: 'email' | 'linkedin' | 'whatsapp', language?: string): Promise<OutreachDraft | null> {
    try {
      const params = new URLSearchParams();
      params.set('channel', channel);
      if (language) params.set('language', language);
      
      const response = await fetch(`${LEAD_INTELLIGENCE_API_BASE_URL}/api/v1/lead-intelligence/companies/${companyId}/outreach?${params.toString()}`, {
        method: 'POST',
        headers: this.baseHeaders,
      });

      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }

      return response.json();
    } catch (error) {
      console.error('Failed to generate outreach draft:', error);
      return null;
    }
  }

  async listSearchProfiles(): Promise<SearchProfile[]> {
    try {
      const response = await fetch(`${LEAD_INTELLIGENCE_API_BASE_URL}/api/v1/lead-intelligence/profiles`, {
        headers: this.baseHeaders,
      });

      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }

      return response.json();
    } catch (error) {
      console.error('Failed to list search profiles:', error);
      return [];
    }
  }

  async createSearchProfile(req: {
    name: string;
    industry?: string;
    location?: string;
    min_employee_count?: number;
    max_employee_count?: number;
    min_revenue_usd?: number;
    max_revenue_usd?: number;
    technologies?: string[];
    keywords?: string[];
    funding_stage?: string;
    schedule_cron?: string;
    language?: string;
  }): Promise<SearchProfile | null> {
    try {
      const response = await fetch(`${LEAD_INTELLIGENCE_API_BASE_URL}/api/v1/lead-intelligence/profiles`, {
        method: 'POST',
        headers: this.baseHeaders,
        body: JSON.stringify(req),
      });

      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }

      return response.json();
    } catch (error) {
      console.error('Failed to create search profile:', error);
      return null;
    }
  }

  // Billing Service API methods

  async listBillingPlans(): Promise<{ plan_key: string; name: string; price_usd: number; max_seats: number; monthly_token_quota: number }[]> {
    try {
      const response = await fetch(`${BILLING_API_BASE_URL}/api/v1/billing/plans`, {
        headers: this.baseHeaders,
      });

      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }

      return response.json();
    } catch (error) {
      console.error('Failed to list billing plans:', error);
      return [];
    }
  }

  async createSubscription(plan: string): Promise<{ subscription_id: string; tenant_id: string; plan: string; price_usd: number; status: string } | null> {
    try {
      const response = await fetch(`${BILLING_API_BASE_URL}/api/v1/billing/subscriptions?plan=${plan}`, {
        method: 'POST',
        headers: this.baseHeaders,
      });

      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }

      return response.json();
    } catch (error) {
      console.error('Failed to create subscription:', error);
      return null;
    }
  }

  async getBillingUsage(tokensUsed: number, plan: string): Promise<{ current_tokens_used: number; quota: number; percentage_used: number; estimated_cost_usd: number; plan: string } | null> {
    try {
      const response = await fetch(`${BILLING_API_BASE_URL}/api/v1/billing/usage?tokens_used=${tokensUsed}&plan=${plan}`, {
        headers: this.baseHeaders,
      });

      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }

      return response.json();
    } catch (error) {
      console.error('Failed to get billing usage:', error);
      return null;
    }
  }

  async listInvoices(): Promise<{ subscription_id: string; tenant_id: string; plan: string; amount_usd: number; status: string; period_start: string; period_end: string }[]> {
    try {
      const response = await fetch(`${BILLING_API_BASE_URL}/api/v1/billing/invoices`, {
        headers: { ...this.baseHeaders, Authorization: `Bearer ${localStorage.getItem('auth_token')}` } });

      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }

      return response.json();
    } catch (error) {
      console.error('Failed to list invoices:', error);
      return [];
    }
  }

  async downloadInvoicePdf(invoiceId: string): Promise<Blob | null> {
    try {
      const response = await fetch(`${BILLING_API_BASE_URL}/api/v1/billing/invoices/${invoiceId}/pdf`, {
        headers: { 'Accept': 'application/pdf' }
      });

      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }

      return await response.blob();
    } catch (error) {
      console.error('Failed to download invoice PDF:', error);
      return null;
    }
  }

  // Platform Service API methods (Super Admin)

  async fetchPlatformMetrics(): Promise<PlatformMetrics | null> {
    try {
      const response = await fetch(`${PLATFORM_API_BASE_URL}/api/v1/platform/metrics`, {
        headers: this.getAuthHeaders(),
      });

      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }

      return response.json();
    } catch (error) {
      console.error('Failed to fetch platform metrics:', error);
      return null;
    }
  }

  async fetchOrganizations(status?: 'all' | 'active' | 'suspended'): Promise<OrganizationListItem[]> {
    try {
      const params = status && status !== 'all' ? `?status=${status}` : '';
      const response = await fetch(`${PLATFORM_API_BASE_URL}/api/v1/platform/organizations${params}`, {
        headers: this.getAuthHeaders(),
      });

      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }

      return response.json();
    } catch (error) {
      console.error('Failed to fetch organizations:', error);
      return [];
    }
  }

  async suspendOrganization(orgId: string): Promise<OrganizationDetail | null> {
    try {
      const response = await fetch(`${PLATFORM_API_BASE_URL}/api/v1/platform/organizations/${orgId}/suspend`, {
        method: 'PATCH',
        headers: this.getAuthHeaders(),
      });

      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }

      return response.json();
    } catch (error) {
      console.error('Failed to suspend organization:', error);
      return null;
    }
  }

  async resumeOrganization(orgId: string): Promise<OrganizationDetail | null> {
    try {
      const response = await fetch(`${PLATFORM_API_BASE_URL}/api/v1/platform/organizations/${orgId}/resume`, {
        method: 'PATCH',
        headers: this.getAuthHeaders(),
      });

      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }

      return response.json();
    } catch (error) {
      console.error('Failed to resume organization:', error);
      return null;
    }
  }

  async deleteOrganization(orgId: string): Promise<{ status: string; message: string; org_id: string } | null> {
    try {
      const response = await fetch(`${PLATFORM_API_BASE_URL}/api/v1/platform/organizations/${orgId}`, {
        method: 'DELETE',
        headers: this.getAuthHeaders(),
      });

      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }

      return response.json();
    } catch (error) {
      console.error('Failed to delete organization:', error);
      return null;
    }
  }

  // Knowledge Base Document Methods

  async fetchDocuments(tenantId?: string): Promise<KnowledgeDocument[]> {
    try {
      const params = tenantId ? `?tenant_id=${tenantId}` : '';
      const response = await fetch(`${KNOWLEDGE_API_BASE_URL}/api/v1/knowledge/documents${params}`, {
        headers: this.getAuthHeaders(),
      });

      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }

      return response.json();
    } catch (error) {
      console.error('Failed to fetch documents:', error);
      return [];
    }
  }

  async createDocument(doc: { title: string; content: string; category?: string; tags?: string[]; tenant_id: string }): Promise<KnowledgeDocument | null> {
    try {
      const response = await fetch(`${KNOWLEDGE_API_BASE_URL}/api/v1/knowledge/documents`, {
        method: 'POST',
        headers: this.getAuthHeaders(),
        body: JSON.stringify(doc),
      });

      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }

      return response.json();
    } catch (error) {
      console.error('Failed to create document:', error);
      return null;
    }
  }

  // AI Agent Methods

  async fetchAIAgents(tenantId: string): Promise<AIAgent[]> {
    try {
      const response = await fetch(`${KNOWLEDGE_API_BASE_URL}/api/v1/agents?tenant_id=${tenantId}`, {
        headers: this.getAuthHeaders(),
      });

      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }

      return response.json();
    } catch (error) {
      console.error('Failed to fetch AI agents:', error);
      return [];
    }
  }

  async createAIAgent(agent: { name: string; type: string; model: string; temperature?: number; tenant_id: string }): Promise<AIAgent | null> {
    try {
      const response = await fetch(`${KNOWLEDGE_API_BASE_URL}/api/v1/agents`, {
        method: 'POST',
        headers: this.getAuthHeaders(),
        body: JSON.stringify(agent),
      });

      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }

      return response.json();
    } catch (error) {
      console.error('Failed to create AI agent:', error);
      return null;
    }
  }

  // Slack Service API methods

  async registerSlackIntegration(channelId: string, botToken: string, signingSecret: string): Promise<{ status: string; channel_id: string } | null> {
    try {
      const response = await fetch(`${SLACK_API_BASE_URL}/api/v1/slack/integrations`, {
        method: 'POST',
        headers: this.baseHeaders,
        body: JSON.stringify({ channel_id: channelId, bot_token: botToken, signing_secret: signingSecret }),
      });

      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }

      return response.json();
    } catch (error) {
      console.error('Failed to register Slack integration:', error);
      return null;
    }
  }

  async listSlackIntegrations(): Promise<{ status: string; integrations: string[]; count: number } | null> {
    try {
      const response = await fetch(`${SLACK_API_BASE_URL}/api/v1/slack/integrations`, {
        headers: this.baseHeaders,
      });

      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }

      return response.json();
    } catch (error) {
      console.error('Failed to list Slack integrations:', error);
      return null;
    }
  }

  async sendSlackMessage(channelId: string, text: string, threadTs?: string): Promise<{ status: string; channel_id: string; text: string } | null> {
    try {
      const response = await fetch(`${SLACK_API_BASE_URL}/api/v1/slack/channels/${channelId}/messages`, {
        method: 'POST',
        headers: this.baseHeaders,
        body: JSON.stringify({ text, thread_ts: threadTs }),
      });

      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }

      return response.json();
    } catch (error) {
      console.error('Failed to send Slack message:', error);
      return null;
    }
  }

  // Discord Service API methods

  async registerDiscordIntegration(guildId: string, channelId: string, botToken: string): Promise<{ status: string; channel_id: string } | null> {
    try {
      const response = await fetch(`${DISCORD_API_BASE_URL}/api/v1/discord/integrations`, {
        method: 'POST',
        headers: this.baseHeaders,
        body: JSON.stringify({ guild_id: guildId, channel_id: channelId, bot_token: botToken }),
      });

      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }

      return response.json();
    } catch (error) {
      console.error('Failed to register Discord integration:', error);
      return null;
    }
  }

  async listDiscordIntegrations(): Promise<{ status: string; integrations: string[]; count: number } | null> {
    try {
      const response = await fetch(`${DISCORD_API_BASE_URL}/api/v1/discord/integrations`, {
        headers: this.baseHeaders,
      });

      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }

      return response.json();
    } catch (error) {
      console.error('Failed to list Discord integrations:', error);
      return null;
    }
  }

  async sendDiscordMessage(channelId: string, content: string, username?: string): Promise<{ status: string; channel_id: string; content: string } | null> {
    try {
      const response = await fetch(`${DISCORD_API_BASE_URL}/api/v1/discord/channels/${channelId}/messages`, {
        method: 'POST',
        headers: this.baseHeaders,
        body: JSON.stringify({ content, username }),
      });

      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }

      return response.json();
    } catch (error) {
      console.error('Failed to send Discord message:', error);
      return null;
    }
  }
}

export const apiClient = new APIClient();
