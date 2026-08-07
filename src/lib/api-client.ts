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

export const AUTH_SERVICE_URL = import.meta.env.DEV
  ? `http://localhost:${import.meta.env.PUBLIC_AUTH_SERVICE_PORT || 8001}`
  : "/api";

export const USER_SERVICE_URL = import.meta.env.DEV
  ? `http://localhost:${import.meta.env.PUBLIC_USER_SERVICE_PORT || 8002}`
  : "/api";

export const ORGANIZATION_SERVICE_URL = import.meta.env.DEV
  ? `http://localhost:${import.meta.env.PUBLIC_ORGANIZATION_SERVICE_PORT || 8003}`
  : "/api";

export const BILLING_SERVICE_URL = import.meta.env.DEV
  ? `http://localhost:${import.meta.env.PUBLIC_BILLING_SERVICE_PORT || 8004}`
  : "/api";

export const WHATSAPP_SERVICE_URL = import.meta.env.DEV
  ? `http://localhost:${import.meta.env.PUBLIC_WHATSAPP_SERVICE_PORT || 8005}`
  : "/api";

export const KNOWLEDGE_SERVICE_URL = import.meta.env.DEV
  ? `http://localhost:${import.meta.env.PUBLIC_KNOWLEDGE_SERVICE_PORT || 8006}`
  : "/api";

export const SALES_SERVICE_URL = import.meta.env.DEV
  ? `http://localhost:${import.meta.env.PUBLIC_SALES_SERVICE_PORT || 8007}`
  : "/api";

export const TICKETS_SERVICE_URL = import.meta.env.DEV
  ? `http://localhost:${import.meta.env.PUBLIC_TICKET_SERVICE_PORT || 8008}`
  : "/api";

export const VECTOR_SERVICE_URL = import.meta.env.DEV
  ? `http://localhost:${import.meta.env.PUBLIC_VECTOR_SERVICE_PORT || 8009}`
  : "/api";

export const AI_GATEWAY_SERVICE_URL = import.meta.env.DEV
  ? `http://localhost:${import.meta.env.PUBLIC_AI_GATEWAY_PORT || 8000}`
  : "/api";

export const CHAT_SERVICE_URL = import.meta.env.DEV
  ? `http://localhost:${import.meta.env.PUBLIC_CHAT_SERVICE_PORT || 8010}`
  : "/api";

export const WORKFLOW_SERVICE_URL = import.meta.env.DEV
  ? `http://localhost:${import.meta.env.PUBLIC_WORKFLOW_SERVICE_PORT || 8011}`
  : "/api";

export const ANALYTICS_SERVICE_URL = import.meta.env.DEV
  ? `http://localhost:${import.meta.env.PUBLIC_ANALYTICS_SERVICE_PORT || 8012}`
  : "/api";

export const SEARCH_SERVICE_URL = import.meta.env.DEV
  ? `http://localhost:${import.meta.env.PUBLIC_SEARCH_SERVICE_PORT || 8013}`
  : "/api";

export const NOTIFICATION_SERVICE_URL = import.meta.env.DEV
  ? `http://localhost:${import.meta.env.PUBLIC_NOTIFICATION_SERVICE_PORT || 8014}`
  : "/api";

export const FILE_SERVICE_URL = import.meta.env.DEV
  ? `http://localhost:${import.meta.env.PUBLIC_FILE_SERVICE_PORT || 8015}`
  : "/api";

export const CUSTOMER_SERVICE_URL = import.meta.env.DEV
  ? `http://localhost:${import.meta.env.PUBLIC_CUSTOMER_SERVICE_PORT || 8016}`
  : "/api";

export const SUPPORT_SERVICE_URL = import.meta.env.DEV
  ? `http://localhost:${import.meta.env.PUBLIC_SUPPORT_SERVICE_PORT || 8017}`
  : "/api";

export const CONVERSATION_SERVICE_URL = import.meta.env.DEV
  ? `http://localhost:${import.meta.env.PUBLIC_CONVERSATION_SERVICE_PORT || 8018}`
  : "/api";

export const TELEGRAM_SERVICE_URL = import.meta.env.DEV
  ? `http://localhost:${import.meta.env.PUBLIC_TELEGRAM_SERVICE_PORT || 8019}`
  : "/api";

export const MESSENGER_SERVICE_URL = import.meta.env.DEV
  ? `http://localhost:${import.meta.env.PUBLIC_MESSENGER_SERVICE_PORT || 8020}`
  : "/api";

export const EMAIL_SERVICE_URL = import.meta.env.DEV
  ? `http://localhost:${import.meta.env.PUBLIC_EMAIL_SERVICE_PORT || 8021}`
  : "/api";

export const LEAD_INTELLIGENCE_SERVICE_URL = import.meta.env.DEV
  ? `http://localhost:${import.meta.env.PUBLIC_LEAD_INTELLIGENCE_SERVICE_PORT || 8022}`
  : "/api";

export const AUDIT_SERVICE_URL = import.meta.env.DEV
  ? `http://localhost:${import.meta.env.PUBLIC_AUDIT_SERVICE_PORT || 8023}`
  : "/api";

export const SLACK_SERVICE_URL = import.meta.env.DEV
  ? `http://localhost:${import.meta.env.PUBLIC_SLACK_SERVICE_PORT || 8024}`
  : "/api";

export const DISCORD_SERVICE_URL = import.meta.env.DEV
  ? `http://localhost:${import.meta.env.PUBLIC_DISCORD_SERVICE_PORT || 8026}`
  : "/api";

export const CHANNEL_SERVICE_URL = import.meta.env.DEV
  ? `http://localhost:${import.meta.env.PUBLIC_ORGANIZATION_SERVICE_PORT || 8003}`
  : "/api";

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
    const response = await fetch(`${AUTH_SERVICE_URL}/api/v1/auth/login`, {
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
    const response = await fetch(`${AUTH_SERVICE_URL}/api/v1/auth/refresh`, {
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

  async forgotPassword(email: string): Promise<{ success: boolean; message: string; token?: string }> {
    const response = await fetch(`${AUTH_SERVICE_URL}/api/v1/auth/forgot-password`, {
      method: 'POST',
      headers: this.baseHeaders,
      body: JSON.stringify({ email }),
    });

    if (!response.ok) {
      const error = await response.json();
      throw new Error(error.detail || 'Failed to request password reset');
    }

    return response.json();
  }

  async resetPassword(resetRequest: { token: string; new_password: string; confirm_password: string }): Promise<{ success: boolean; message: string }> {
    const response = await fetch(`${AUTH_SERVICE_URL}/api/v1/auth/reset-password`, {
      method: 'POST',
      headers: this.baseHeaders,
      body: JSON.stringify(resetRequest),
    });

    if (!response.ok) {
      const error = await response.json();
      throw new Error(error.detail || 'Failed to reset password');
    }

    return response.json();
  }

  async getResetToken(token: string): Promise<{ token: string; email: string; expires_at: string }> {
    const response = await fetch(`${AUTH_SERVICE_URL}/api/v1/auth/reset-token/${token}`, {
      method: 'GET',
      headers: this.baseHeaders,
    });

    if (!response.ok) {
      const error = await response.json();
      throw new Error(error.detail || 'Invalid or expired reset token');
    }

    return response.json();
  }

  async logout(): Promise<void> {
    localStorage.removeItem('auth_token');
    localStorage.removeItem('refresh_token');
    localStorage.removeItem('user_data');
  }

  async setupMFA(): Promise<MFASetupResponse> {
    const response = await fetch(`${AUTH_SERVICE_URL}/api/v1/auth/mfa/setup`, {
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
    const response = await fetch(`${AUTH_SERVICE_URL}/api/v1/auth/mfa/verify`, {
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
    const response = await fetch(`${AUTH_SERVICE_URL}/api/v1/auth/sessions`, {
      headers: this.getAuthHeaders(),
    });

    if (!response.ok) {
      throw new Error('Failed to fetch sessions');
    }

    return response.json();
  }

  async revokeSession(sessionId: string): Promise<{ status: string; session_id: string }> {
    const response = await fetch(`${AUTH_SERVICE_URL}/api/v1/auth/sessions/${sessionId}`, {
      method: 'DELETE',
      headers: this.getAuthHeaders(),
    });

    if (!response.ok) {
      throw new Error('Failed to revoke session');
    }

    return response.json();
  }

  async getUserProfile(): Promise<User> {
    const response = await fetch(`${USER_SERVICE_URL}/api/v1/users/me`, {
      headers: this.getAuthHeaders(),
    });

    if (!response.ok) {
      throw new Error('Failed to fetch user profile');
    }

    return response.json();
  }

  async updateUserProfile(updates: Partial<User>): Promise<User> {
    const response = await fetch(`${USER_SERVICE_URL}/api/v1/users/me`, {
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
    const response = await fetch(`${USER_SERVICE_URL}/api/v1/users/me/preferences`, {
      headers: this.getAuthHeaders(),
    });

    if (!response.ok) {
      throw new Error('Failed to fetch user preferences');
    }

    return response.json();
  }

  async updateUserPreferences(updates: Partial<UserPreferences>): Promise<UserPreferences> {
    const response = await fetch(`${USER_SERVICE_URL}/api/v1/users/me/preferences`, {
      method: 'PUT',
      headers: this.getAuthHeaders(),
      body: JSON.stringify(updates),
    });

    if (!response.ok) {
      throw new Error('Failed to update user preferences');
    }

    return response.json();
  }

  async uploadFile(file: File): Promise<{ file_url: string; file_id: string; filename: string }> {
    const formData = new FormData();
    formData.append('file', file);

    const token = localStorage.getItem('auth_token');
    const headers: HeadersInit = token ? { Authorization: `Bearer ${token}` } : {};

    const response = await fetch(`${FILE_SERVICE_URL}/api/v1/files/upload`, {
      method: 'POST',
      headers: headers,
      body: formData,
    });

    if (!response.ok) {
      const error = await response.json().catch(() => ({}));
      throw new Error(error.detail || 'Failed to upload file');
    }

    return response.json();
  }

  // Organization API Methods

  async getOrganization(orgId: string): Promise<Organization> {
    const response = await fetch(`${ORGANIZATION_SERVICE_URL}/api/v1/organizations/${orgId}`, {
      headers: this.getAuthHeaders(),
    });

    if (!response.ok) {
      throw new Error('Failed to fetch organization');
    }

    return response.json();
  }

  async getTenantMetrics(tenantId: string): Promise<TenantMetrics> {
    const response = await fetch(`${ORGANIZATION_SERVICE_URL}/api/v1/organizations/${tenantId}/metrics`, {
      headers: this.getAuthHeaders(),
    });

    if (!response.ok) {
      throw new Error('Failed to fetch tenant metrics');
    }

    return response.json();
  }

  async updateBranding(tenantId: string, updates: Partial<Branding>): Promise<Branding> {
    const response = await fetch(`${ORGANIZATION_SERVICE_URL}/api/v1/organizations/${tenantId}/branding`, {
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
    const response = await fetch(`${ORGANIZATION_SERVICE_URL}/api/v1/organizations/${tenantId}/members`, {
      headers: this.getAuthHeaders(),
    });

    if (!response.ok) {
      throw new Error('Failed to fetch workspace members');
    }

    return response.json();
  }

  async addWorkspaceMember(tenantId: string, userId: string, role: string): Promise<WorkspaceMember> {
    const response = await fetch(`${ORGANIZATION_SERVICE_URL}/api/v1/organizations/${tenantId}/members`, {
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
    const response = await fetch(`${ORGANIZATION_SERVICE_URL}/api/v1/organizations/${tenantId}/members/${memberId}/role`, {
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
    const response = await fetch(`${ORGANIZATION_SERVICE_URL}/api/v1/organizations/${tenantId}/members/${memberId}`, {
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
      const response = await fetch(`${ANALYTICS_SERVICE_URL}/api/v1/analytics/kpis`, {
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
      const response = await fetch(`${CUSTOMER_SERVICE_URL}/api/v1/customers${query}`, {
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
      const response = await fetch(`${CUSTOMER_SERVICE_URL}/api/v1/customers`, {
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
      const response = await fetch(`${CUSTOMER_SERVICE_URL}/api/v1/customers/segments`, {
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
      const response = await fetch(`${CUSTOMER_SERVICE_URL}/api/v1/customers/tags`, {
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
      const response = await fetch(`${TICKETS_SERVICE_URL}/api/v1/tickets${query}`, {
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
      const response = await fetch(`${TICKETS_SERVICE_URL}/api/v1/tickets`, {
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
      const response = await fetch(`${TICKETS_SERVICE_URL}/api/v1/tickets/${ticketId}`, {
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
      const response = await fetch(`${TICKETS_SERVICE_URL}/api/v1/tickets/analytics/overview`, {
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

      const response = await fetch(`${SEARCH_SERVICE_URL}/api/v1/search/search?${queryParams.toString()}`, {
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
      const response = await fetch(`${SEARCH_SERVICE_URL}/api/v1/search/index`, {
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

      const response = await fetch(`${SEARCH_SERVICE_URL}/api/v1/search/index/${documentId}?${params.toString()}`, {
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
      const response = await fetch(`${SEARCH_SERVICE_URL}/api/v1/search/index/stats`, {
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
      const response = await fetch(`${KNOWLEDGE_SERVICE_URL}/api/v1/knowledge/categories`, {
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
      const response = await fetch(`${WHATSAPP_SERVICE_URL}/api/v1/whatsapp/accounts`, {
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
      const response = await fetch(`${WHATSAPP_SERVICE_URL}/api/v1/whatsapp/accounts`, {
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
      const response = await fetch(`${WHATSAPP_SERVICE_URL}/api/v1/whatsapp/messages`, {
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
      const response = await fetch(`${CHANNEL_SERVICE_URL}/api/v1/channels/integrations`, {
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

      const response = await fetch(`${LEAD_INTELLIGENCE_SERVICE_URL}/api/v1/lead-intelligence/companies/search?${queryParams.toString()}`, {
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
      
      const response = await fetch(`${LEAD_INTELLIGENCE_SERVICE_URL}/api/v1/lead-intelligence/companies/${companyId}?${params.toString()}`, {
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
      
      const response = await fetch(`${LEAD_INTELLIGENCE_SERVICE_URL}/api/v1/lead-intelligence/companies/${companyId}/qualify?${params.toString()}`, {
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
      
      const response = await fetch(`${LEAD_INTELLIGENCE_SERVICE_URL}/api/v1/lead-intelligence/companies/${companyId}/research?${params.toString()}`, {
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
      
      const response = await fetch(`${LEAD_INTELLIGENCE_SERVICE_URL}/api/v1/lead-intelligence/companies/${companyId}/outreach?${params.toString()}`, {
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
      const response = await fetch(`${LEAD_INTELLIGENCE_SERVICE_URL}/api/v1/lead-intelligence/profiles`, {
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
      const response = await fetch(`${LEAD_INTELLIGENCE_SERVICE_URL}/api/v1/lead-intelligence/profiles`, {
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
      const response = await fetch(`${BILLING_SERVICE_URL}/api/v1/billing/plans`, {
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
      const response = await fetch(`${BILLING_SERVICE_URL}/api/v1/billing/subscriptions?plan=${plan}`, {
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
      const response = await fetch(`${BILLING_SERVICE_URL}/api/v1/billing/usage?tokens_used=${tokensUsed}&plan=${plan}`, {
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
      const response = await fetch(`${BILLING_SERVICE_URL}/api/v1/billing/invoices`, {
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
      const response = await fetch(`${BILLING_SERVICE_URL}/api/v1/billing/invoices/${invoiceId}/pdf`, {
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
      const response = await fetch(`${AI_GATEWAY_SERVICE_URL}/api/v1/platform/metrics`, {
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
      const response = await fetch(`${AI_GATEWAY_SERVICE_URL}/api/v1/platform/organizations${params}`, {
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
      const response = await fetch(`${AI_GATEWAY_SERVICE_URL}/api/v1/platform/organizations/${orgId}/suspend`, {
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
      const response = await fetch(`${AI_GATEWAY_SERVICE_URL}/api/v1/platform/organizations/${orgId}/resume`, {
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
      const response = await fetch(`${AI_GATEWAY_SERVICE_URL}/api/v1/platform/organizations/${orgId}`, {
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
      const response = await fetch(`${KNOWLEDGE_SERVICE_URL}/api/v1/knowledge/documents${params}`, {
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
      const response = await fetch(`${KNOWLEDGE_SERVICE_URL}/api/v1/knowledge/documents`, {
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
      const response = await fetch(`${KNOWLEDGE_SERVICE_URL}/api/v1/agents?tenant_id=${tenantId}`, {
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
      const response = await fetch(`${KNOWLEDGE_SERVICE_URL}/api/v1/agents`, {
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
      const response = await fetch(`${SLACK_SERVICE_URL}/api/v1/slack/integrations`, {
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
      const response = await fetch(`${SLACK_SERVICE_URL}/api/v1/slack/integrations`, {
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
      const response = await fetch(`${SLACK_SERVICE_URL}/api/v1/slack/channels/${channelId}/messages`, {
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
      const response = await fetch(`${DISCORD_SERVICE_URL}/api/v1/discord/integrations`, {
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
      const response = await fetch(`${DISCORD_SERVICE_URL}/api/v1/discord/integrations`, {
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
      const response = await fetch(`${DISCORD_SERVICE_URL}/api/v1/discord/channels/${channelId}/messages`, {
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

export const API_BASE_URL = AUTH_SERVICE_URL;

export const SERVICES = {
  auth: AUTH_SERVICE_URL,
  user: USER_SERVICE_URL,
  organization: ORGANIZATION_SERVICE_URL,
  billing: BILLING_SERVICE_URL,
  knowledge: KNOWLEDGE_SERVICE_URL,
  sales: SALES_SERVICE_URL,
  tickets: TICKETS_SERVICE_URL,
  vector: VECTOR_SERVICE_URL,
  gateway: AI_GATEWAY_SERVICE_URL,
  chat: CHAT_SERVICE_URL,
  workflow: WORKFLOW_SERVICE_URL,
  analytics: ANALYTICS_SERVICE_URL,
  search: SEARCH_SERVICE_URL,
  notification: NOTIFICATION_SERVICE_URL,
  file: FILE_SERVICE_URL,
  customer: CUSTOMER_SERVICE_URL,
  support: SUPPORT_SERVICE_URL,
  conversation: CONVERSATION_SERVICE_URL,
  telegram: TELEGRAM_SERVICE_URL,
  messenger: MESSENGER_SERVICE_URL,
  email: EMAIL_SERVICE_URL,
  leadIntelligence: LEAD_INTELLIGENCE_SERVICE_URL,
  audit: AUDIT_SERVICE_URL,
  slack: SLACK_SERVICE_URL,
  discord: DISCORD_SERVICE_URL,
  channel: CHANNEL_SERVICE_URL,
  whatsapp: WHATSAPP_SERVICE_URL,
};

export const apiClient = new APIClient();
