// Shared type definitions for SalesGenie frontend islands

export interface KPICard {
  id: string;
  title: string;
  value: string;
  change: string;
  changeDir: 'up' | 'down' | 'neutral';
  icon: string;
  color: string;
}

export interface NavItem {
  id: string;
  label: string;
  icon: string;
  href: string;
  badge?: number;
  children?: NavItem[];
}

export interface Message {
  id: string;
  role: 'user' | 'assistant' | 'system';
  content: string;
  timestamp: Date;
  channel?: string;
  agentType?: string;
  confidence?: number;
}

export interface Lead {
  id: string;
  name: string;
  email: string;
  company: string;
  score: number;
  status: 'new' | 'qualified' | 'contacted' | 'won' | 'lost';
  value: number;
  stage?: string;
  phone?: string;
  industry?: string;
  notes?: string;
}

export interface Ticket {
  id: string;
  number: string;
  title: string;
  customer: string;
  status: 'new' | 'open' | 'in_progress' | 'escalated' | 'resolved';
  priority: 'low' | 'medium' | 'high' | 'urgent';
  category: string;
  aiConfidence: number;
  createdAt: Date;
}

// Authentication Types

export type PlatformRole =
  | 'super_admin'
  | 'workspace_admin'
  | 'org_admin'
  | 'sales_manager'
  | 'sales_agent'
  | 'support_manager'
  | 'support_agent'
  | 'knowledge_manager'
  | 'auditor'
  | 'end_user';

export interface User {
  id: string;
  email: string;
  full_name: string | null;
  avatar_url: string | null;
  tenant_id: string;
  language?: string;
  created_at: string;
}

export interface Session {
  token: string;
  refreshToken: string;
  expiresAt: number;
  user: User;
  roles: PlatformRole[];
  permissions: string[];
}

export interface LoginRequest {
  email: string;
  password: string;
  tenant_id?: string;
  mfa_code?: string;
}

export interface LoginResponse {
  access_token: string;
  refresh_token: string;
  token_type: string;
  expires_in: number;
  user_id: string;
  roles: PlatformRole[];
  tenant_id: string;
  mfa_required: boolean;
}

export interface MFASetupResponse {
  secret_key: string;
  qr_code_uri: string;
  qr_code: string;
  backup_codes: string[];
}

export interface MFAVerifyRequest {
  code: string;
}

export interface SessionDTO {
  id: string;
  device_name: string | null;
  ip_address: string | null;
  user_agent: string | null;
  created_at: string;
  is_active: boolean;
}

// Analytics Types

export interface AnalyticsKPIs {
  aiAccuracyRate: number;
  avgResponseTimeSec: number;
  hallucinationRate: number;
  customerSatisfactionScore: number;
  salesConversionRate: number;
  avgResolutionTimeMin: number;
  activeUsers: number;
  revenueGeneratedUsd: number;
  aiCostUsd: number;
  totalTokenUsage: number;
}

export interface ConversationPoint {
  hour: string;
  conversations: number;
  ai: number;
  human: number;
}

export interface RevenuePoint {
  day: string;
  revenue: number;
  target: number;
}

export interface ChannelPoint {
  name: string;
  value: number;
}

// Customer Types

export interface Customer {
  id: string;
  email: string | null;
  phone_number: string | null;
  full_name: string;
  company_name: string | null;
  avatar_url: string | null;
  job_title: string | null;
  lead_status: string;
  lead_score: number;
  lifetime_value: number;
  total_orders: number;
  last_interaction_at: string | null;
  is_active: boolean;
  tenant_id: string;
  created_at: string;
  segments: string[];
  tags: string[];
}

export interface CustomerSegment {
  id: string;
  name: string;
  description: string | null;
  color: string;
  is_system: boolean;
  customer_count: number;
  tenant_id: string;
  created_at: string;
}

export interface CustomerTag {
  id: string;
  name: string;
  color: string;
  customer_count: number;
  tenant_id: string;
  created_at: string;
}

// Support Ticket Types

export interface SupportTicket {
  id: string;
  customer_id: string;
  conversation_id: string | null;
  title: string;
  description: string;
  status: string;
  priority: string;
  category: string;
  source: string;
  assigned_to: string | null;
  assigned_at: string | null;
  resolved_at: string | null;
  closed_at: string | null;
  resolution_notes: string | null;
  satisfaction_score: number | null;
  satisfaction_feedback: string | null;
  is_escalated: boolean;
  escalation_reason: string | null;
  tenant_id: string;
  created_at: string;
  updated_at: string;
}

export interface TicketAnalytics {
  total_tickets: number;
  open_tickets: number;
  in_progress_tickets: number;
  resolved_tickets: number;
  closed_tickets: number;
  avg_resolution_time_hours: number;
  avg_satisfaction_score: number;
  tickets_by_priority: Record<string, number>;
  tickets_by_category: Record<string, number>;
  escalation_rate: number;
}

// Search Types

export interface SearchHit {
  id: string;
  index_type: string;
  document_id: string;
  title: string;
  content: string;
  tags?: string[];
  metadata?: Record<string, unknown>;
  score: number;
  highlights?: Record<string, string[]>;
}

export interface SearchResponse {
  query: string;
  total_hits: number;
  hits: SearchHit[];
  took_ms: number;
  aggregations?: Record<string, unknown>;
}

export interface IndexDocumentRequest {
  index_type: string;
  document_id: string;
  title: string;
  content: string;
  tags?: string[];
  metadata?: Record<string, unknown>;
  is_public?: boolean;
}

export interface IndexDocumentResponse {
  document_id: string;
  index_type: string;
  status: string;
  indexed_at: string;
}

export interface IndexStatsDTO {
  index_type: string;
  document_count: number;
  last_updated: string;
}

// User Service Types

export interface UserPreferences {
  user_id: string;
  theme: string;
  language: string;
  email_notifications: boolean;
  slack_notifications: boolean;
  keyboard_shortcuts: boolean;
  preferred_channel: string;
}

// Organization Service Types

export interface Organization {
  id: string;
  name: string;
  slug: string;
  domain: string | null;
  subscription_tier: string;
  max_seats: number;
  max_monthly_tokens: number;
  is_active: boolean;
  created_at: string;
}

export interface TenantMetrics {
  tenant_id: string;
  total_conversations: number;
  active_conversations: number;
  total_tokens_used: number;
  ai_cost_usd: number;
  ai_accuracy_rate: number;
  hallucination_rate: number;
  sales_conversion_rate: number;
}

export interface PlatformMetrics {
  total_organizations: number;
  active_organizations: number;
  suspended_organizations: number;
  total_users: number;
  total_tokens_used: number;
  ai_cost_usd: number;
  platform_uptime_percent: number;
}

export interface OrganizationListItem {
  id: string;
  name: string;
  slug: string;
  domain: string | null;
  subscription_tier: string;
  is_active: boolean;
  created_at: string;
  max_seats: number;
  max_monthly_tokens: number;
}

export interface OrganizationDetail {
  id: string;
  name: string;
  slug: string;
  domain: string | null;
  subscription_tier: string;
  is_active: boolean;
  created_at: string;
  max_seats: number;
  max_monthly_tokens: number;
}

export interface Branding {
  tenant_id: string;
  primary_color: string;
  secondary_color: string;
  logo_url: string | null;
  custom_domain: string | null;
  is_white_label_enabled: boolean;
}

export interface WorkspaceMember {
  id: string;
  user_id: string;
  role: string;
  status: string;
  created_at: string;
}

// Knowledge Base Types

export interface KnowledgeDocument {
  id: string;
  title: string;
  slug: string;
  content: string;
  document_type: string;
  category: string;
  tags: string[] | null;
  status: string;
  is_public: boolean;
  view_count: number;
  word_count: number | null;
  language: string;
  source_url: string | null;
  created_at: string;
  updated_at: string;
}

export interface KnowledgeCategory {
  id: string;
  name: string;
  slug: string;
  description: string | null;
  color: string | null;
  document_count: number;
  created_at: string;
}

export interface AIAgent {
  id: string;
  name: string;
  type: 'sales' | 'support' | 'refund' | 'booking' | 'hr';
  model: 'groq' | 'google' | 'mistral';
  temperature: number;
  is_active: boolean;
  created_at: string;
  tenant_id: string;
}

// Super Admin Types

export interface SuperAdminUser {
  id: string;
  email: string;
  full_name: string | null;
  role: string;
  is_active: boolean;
  created_at: string;
  last_login_at: string | null;
  tenant_id: string | null;
}

export interface AuditEvent {
  id: string;
  action: string;
  resource_type: string;
  resource_id: string | null;
  user_id: string | null;
  user_email: string | null;
  tenant_id: string | null;
  ip_address: string | null;
  user_agent: string | null;
  severity: 'low' | 'medium' | 'high' | 'critical';
  details: Record<string, any>;
  created_at: string;
}

export interface SystemHealth {
  service: string;
  status: 'healthy' | 'degraded' | 'down';
  response_time_ms: number;
  last_check: string;
}

export interface AIProviderStatus {
  name: string;
  status: 'healthy' | 'degraded' | 'down';
  models: string[];
  daily_limit: number;
  daily_used: number;
  rate_limit_remaining: number;
}

export interface PlatformSettings {
  maintenance_mode: boolean;
  feature_flags: Record<string, boolean>;
  rate_limits_enabled: boolean;
  max_api_requests_per_minute: number;
  ai_token_budget_usd: number;
  created_at: string;
  updated_at: string;
}

export interface SystemInfo {
  version: string;
  instance_id: string;
  environment: string;
  python_version: string;
  database: string;
  redis: string;
}

// Channel Integration Types

export interface ChannelIntegration {
  id: string;
  name: string;
  type: 'whatsapp' | 'email' | 'telegram' | 'messenger' | 'instagram' | 'slack' | 'teams' | 'discord' | 'sms' | 'website';
  is_active: boolean;
  verified: boolean;
  display_name?: string;
  webhook_url?: string;
  last_sync?: string;
}

export type ChannelStatus = 'active' | 'inactive' | 'error' | 'pending';

export interface WhatsAppAccount {
  id: string;
  name: string;
  phone_number_id: string;
  access_token: string;
  is_active: boolean;
  verified: boolean;
  webhook_url?: string;
  created_at: string;
  updated_at: string;
}

export interface ChannelStats {
  total_messages: number;
  sent_messages: number;
  received_messages: number;
  pending_messages: number;
  last_activity: string;
}

export interface SecurityEvent {
  id: string;
  type: 'failed_login' | 'permission_escalation' | 'unusual_export' | 'geographic_anomaly' | 'brute_force' | 'suspicious_activity';
  severity: 'low' | 'medium' | 'high' | 'critical';
  user_id?: string;
  user_email?: string;
  ip_address?: string;
  location?: string;
  user_agent?: string;
  timestamp: string;
  description: string;
  resolved: boolean;
}

// Lead Intelligence Types

export interface Company {
  id: string;
  tenant_id: string;
  name: string;
  domain?: string;
  industry?: string;
  description?: string;
  employee_count?: number;
  estimated_revenue_usd?: number;
  headquarters_location?: string;
  country?: string;
  state?: string;
  city?: string;
  technologies?: Record<string, any>;
  funding_stage?: string;
  funding_amount_usd?: number;
  growth_signals?: Record<string, any>;
  news_mentions?: number;
  website_url?: string;
  linkedin_url?: string;
  twitter_url?: string;
  source?: string;
  confidence_score: number;
  language: string;
  last_enriched_at?: string;
  created_at: string;
  updated_at: string;
}

export interface Contact {
  id: string;
  tenant_id: string;
  company_id: string;
  full_name: string;
  email?: string;
  phone?: string;
  job_title?: string;
  seniority_level?: string;
  department?: string;
  is_decision_maker: boolean;
  decision_influence: number;
  linkedin_url?: string;
  twitter_url?: string;
  source?: string;
  confidence_score: number;
  language: string;
  enrichment_history?: Array<{
    timestamp: string;
    source: string;
    data: Record<string, any>;
  }>;
  created_at: string;
  updated_at: string;
}

export interface LeadScore {
  id: string;
  tenant_id: string;
  company_id: string;
  contact_id?: string;
  total_score: number;
  icp_match_score: number;
  buying_intent_score: number;
  engagement_score: number;
  industry_match: number;
  company_size_match: number;
  revenue_match: number;
  technology_match: number;
  growth_signals: number;
  pain_points_identified?: string[];
  use_cases?: string[];
  challenges?: string[];
  recommended_salesperson_id?: string;
  recommended_workflow?: string;
  scored_at: string;
  expires_at?: string;
}

export interface QualificationReport {
  id: string;
  tenant_id: string;
  company_id: string;
  contact_id?: string;
  business_summary: string;
  opportunity_assessment: string;
  risk_assessment: string;
  technology_analysis?: string;
  growth_analysis?: string;
  competitive_landscape?: string;
  recommended_pitch?: string;
  outreach_recommendations?: Record<string, any>;
  ai_model_version: string;
  generated_at: string;
  language: string;
}

export interface OutreachDraft {
  id: string;
  tenant_id: string;
  company_id: string;
  contact_id?: string;
  email_draft?: string;
  linkedin_draft?: string;
  whatsapp_draft?: string;
  sequence_steps?: Array<{
    step_number: number;
    channel: string;
    delay_days: number;
    content: string;
  }>;
  follow_up_days?: number[];
  channel: string;
  language: string;
  created_at: string;
  updated_at: string;
}

export interface SearchProfile {
  id: string;
  tenant_id: string;
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
  is_active: boolean;
  schedule_cron?: string;
  last_run_at?: string;
  next_run_at?: string;
  language: string;
  created_at: string;
  updated_at: string;
}

// Language Support Types

export interface Language {
  code: string;
  name: string;
  native_name: string;
  direction: 'ltr' | 'rtl';
  is_active: boolean;
  flag?: string;
}

export const SUPPORTED_LANGUAGES: Language[] = [
  { code: 'en', name: 'English', native_name: 'English', direction: 'ltr', is_active: true, flag: '🇬🇧' },
  { code: 'es', name: 'Spanish', native_name: 'Español', direction: 'ltr', is_active: true, flag: '🇪🇸' },
  { code: 'fr', name: 'French', native_name: 'Français', direction: 'ltr', is_active: true, flag: '🇫🇷' },
  { code: 'de', name: 'German', native_name: 'Deutsch', direction: 'ltr', is_active: true, flag: '🇩🇪' },
  { code: 'it', name: 'Italian', native_name: 'Italiano', direction: 'ltr', is_active: true, flag: '🇮🇹' },
  { code: 'pt', name: 'Portuguese', native_name: 'Português', direction: 'ltr', is_active: true, flag: '🇧🇷' },
  { code: 'nl', name: 'Dutch', native_name: 'Nederlands', direction: 'ltr', is_active: true, flag: '🇳🇱' },
  { code: 'ru', name: 'Russian', native_name: 'Русский', direction: 'ltr', is_active: true, flag: '🇷🇺' },
  { code: 'zh', name: 'Chinese', native_name: '中文', direction: 'ltr', is_active: true, flag: '🇨🇳' },
  { code: 'ja', name: 'Japanese', native_name: '日本語', direction: 'ltr', is_active: true, flag: '🇯🇵' },
  { code: 'ko', name: 'Korean', native_name: '한국어', direction: 'ltr', is_active: true, flag: '🇰🇷' },
  { code: 'ar', name: 'Arabic', native_name: 'العربية', direction: 'rtl', is_active: true, flag: '🇸🇦' },
  { code: 'he', name: 'Hebrew', native_name: 'עברית', direction: 'rtl', is_active: true, flag: '🇮🇱' },
  { code: 'hi', name: 'Hindi', native_name: 'हिन्दी', direction: 'ltr', is_active: true, flag: '🇮🇳' },
  { code: 'bn', name: 'Bengali', native_name: 'বাংলা', direction: 'ltr', is_active: true, flag: '🇧🇩' },
  { code: 'ta', name: 'Tamil', native_name: 'தமிழ்', direction: 'ltr', is_active: true, flag: '🇱🇰' },
  { code: 'te', name: 'Telugu', native_name: 'తెలుగు', direction: 'ltr', is_active: true, flag: '🇮🇳' },
  { code: 'mr', name: 'Marathi', native_name: 'मराठी', direction: 'ltr', is_active: true, flag: '🇮🇳' },
  { code: 'gu', name: 'Gujarati', native_name: 'ગુજરાતી', direction: 'ltr', is_active: true, flag: '🇮🇳' },
  { code: 'kn', name: 'Kannada', native_name: 'ಕನ್ನಡ', direction: 'ltr', is_active: true, flag: '🇮🇳' },
  { code: 'ml', name: 'Malayalam', native_name: 'മലയാളം', direction: 'ltr', is_active: true, flag: '🇮🇳' },
  { code: 'pa', name: 'Punjabi', native_name: 'ਪੰਜਾਬੀ', direction: 'ltr', is_active: true, flag: '🇮🇳' },
  { code: 'ur', name: 'Urdu', native_name: 'اردو', direction: 'rtl', is_active: true, flag: '🇵🇰' },
  { code: 'id', name: 'Indonesian', native_name: 'Bahasa Indonesia', direction: 'ltr', is_active: true, flag: '🇮🇩' },
  { code: 'ms', name: 'Malay', native_name: 'Bahasa Melayu', direction: 'ltr', is_active: true, flag: '🇲🇾' },
  { code: 'th', name: 'Thai', native_name: 'ไทย', direction: 'ltr', is_active: true, flag: '🇹🇭' },
  { code: 'vi', name: 'Vietnamese', native_name: 'Tiếng Việt', direction: 'ltr', is_active: true, flag: '🇻🇳' },
  { code: 'tr', name: 'Turkish', native_name: 'Türkçe', direction: 'ltr', is_active: true, flag: '🇹🇷' },
  { code: 'sw', name: 'Swahili', native_name: 'Kiswahili', direction: 'ltr', is_active: true, flag: '🇹🇿' },
  { code: 'fa', name: 'Persian', native_name: 'فارسی', direction: 'rtl', is_active: true, flag: '🇮🇷' },
  { code: 'ps', name: 'Pashto', native_name: 'پښتو', direction: 'rtl', is_active: true, flag: '🇦🇫' },
  { code: 'ug', name: 'Uyghur', native_name: 'ئۇيغۇرچە', direction: 'rtl', is_active: true, flag: '🇨🇳' },
  { code: 'my', name: 'Burmese', native_name: 'ဗမာ', direction: 'ltr', is_active: true, flag: '�🇲🇲' },
  { code: 'yo', name: 'Yoruba', native_name: 'Yorùbá', direction: 'ltr', is_active: true, flag: '🇳🇬' },
  { code: 'ig', name: 'Igbo', native_name: 'Igbo', direction: 'ltr', is_active: true, flag: '🇳🇬' },
  { code: 'ha', name: 'Hausa', native_name: 'Hausa', direction: 'ltr', is_active: true, flag: '🇳🇬' },
  { code: 'zu', name: 'Zulu', native_name: 'IsiZulu', direction: 'ltr', is_active: true, flag: '🇿🇦' },
  { code: 'af', name: 'Afrikaans', native_name: 'Afrikaans', direction: 'ltr', is_active: true, flag: '🇿🇦' },
  { code: 'xh', name: 'Xhosa', native_name: 'IsiXhosa', direction: 'ltr', is_active: true, flag: '🇿🇦' },
  { code: 'st', name: 'Southern Sotho', native_name: 'Sesotho', direction: 'ltr', is_active: true, flag: '🇿🇦' },
  { code: 'tn', name: 'Tswana', native_name: 'Setswana', direction: 'ltr', is_active: true, flag: '🇧🇼' },
  { code: 'kg', name: 'Kongo', native_name: 'Kikongo', direction: 'ltr', is_active: true, flag: '🇨🇬' },
  { code: 'sn', name: 'Shona', native_name: 'ChiShona', direction: 'ltr', is_active: true, flag: '🇿🇼' },
  { code: 'ny', name: 'Chichewa', native_name: 'Chichewa', direction: 'ltr', is_active: true, flag: '🇲🇼' },
  { code: 'so', name: 'Somali', native_name: 'Soomaali', direction: 'ltr', is_active: true, flag: '🇸🇴' },
  { code: 'aa', name: 'Afar', native_name: 'Afar', direction: 'ltr', is_active: true, flag: '🇩🇯' },
  { code: 'ab', name: 'Abkhaz', native_name: 'Абхаз', direction: 'ltr', is_active: true, flag: '🇷🇺' },
  { code: 'ak', name: 'Akan', native_name: 'Akan', direction: 'ltr', is_active: true, flag: '🇬🇭' },
  { code: 'am', name: 'Amharic', native_name: 'አማርኛ', direction: 'ltr', is_active: true, flag: '🇪🇹' },
  { code: 'an', name: 'Aragonese', native_name: 'Aragones', direction: 'ltr', is_active: true, flag: '🇪🇸' },
  { code: 'as', name: 'Assamese', native_name: 'অসমীয়া', direction: 'ltr', is_active: true, flag: '🇮🇳' },
  { code: 'av', name: 'Avaric', native_name: 'Авар', direction: 'ltr', is_active: true, flag: '🇷🇺' },
  { code: 'ay', name: 'Aymara', native_name: 'Aimar', direction: 'ltr', is_active: true, flag: '🇧🇴' },
  { code: 'az', name: 'Azerbaijani', native_name: 'Azərbaycan', direction: 'ltr', is_active: true, flag: '🇦🇿' },
  { code: 'ba', name: 'Bashkir', native_name: 'Башҡорт', direction: 'ltr', is_active: true, flag: '🇷🇺' },
  { code: 'be', name: 'Belarusian', native_name: 'Беларуская', direction: 'ltr', is_active: true, flag: '🇧🇾' },
  { code: 'bg', name: 'Bulgarian', native_name: 'Български', direction: 'ltr', is_active: true, flag: '🇧🇬' },
  { code: 'bh', name: 'Bihari', native_name: 'भिजारी', direction: 'ltr', is_active: true, flag: '🇮🇳' },
  { code: 'bm', name: 'Bambara', native_name: 'Bamanankan', direction: 'ltr', is_active: true, flag: '🇰🇼' },
  { code: 'bo', name: 'Tibetan', native_name: 'བོད་ཡིག', direction: 'ltr', is_active: true, flag: '🇨🇳' },
  { code: 'br', name: 'Breton', native_name: 'Brezhoneg', direction: 'ltr', is_active: true, flag: '🇫🇷' },
  { code: 'bs', name: 'Bosnian', native_name: 'Bosanski', direction: 'ltr', is_active: true, flag: '🇧🇷' },
  { code: 'ca', name: 'Catalan', native_name: 'Català', direction: 'ltr', is_active: true, flag: '🇪🇸' },
  { code: 'ce', name: 'Chechen', native_name: 'Нохчийн', direction: 'ltr', is_active: true, flag: '🇷🇺' },
  { code: 'ch', name: 'Chamorro', native_name: 'Chamoru', direction: 'ltr', is_active: true, flag: '🇬🇺' },
  { code: 'co', name: 'Corsican', native_name: 'Corsu', direction: 'ltr', is_active: true, flag: '🇫🇷' },
  { code: 'cr', name: 'Cree', native_name: 'ᓀᐦᓂ', direction: 'ltr', is_active: true, flag: '🇨🇦' },
  { code: 'cs', name: 'Czech', native_name: 'Čeština', direction: 'ltr', is_active: true, flag: '🇨🇿' },
  { code: 'cv', name: 'Chuvash', native_name: 'Чӑваш', direction: 'ltr', is_active: true, flag: '🇷🇺' },
  { code: 'cy', name: 'Welsh', native_name: 'Cymraeg', direction: 'ltr', is_active: true, flag: '🇬🇧' },
  { code: 'da', name: 'Danish', native_name: 'Dansk', direction: 'ltr', is_active: true, flag: '🇩🇰' },
  { code: 'dv', name: 'Divehi', native_name: 'ދިވެހި', direction: 'rtl', is_active: true, flag: '🇲🇻' },
  { code: 'dz', name: 'Dzongkha', native_name: 'གདོང་ཁ', direction: 'ltr', is_active: true, flag: '🇧🇹' },
  { code: 'ee', name: 'Ewe', native_name: 'Eʔe', direction: 'ltr', is_active: true, flag: '🇬🇭' },
  { code: 'el', name: 'Greek', native_name: 'Ελληνικά', direction: 'ltr', is_active: true, flag: '🇬🇷' },
  { code: 'eo', name: 'Esperanto', native_name: 'Esperanto', direction: 'ltr', is_active: true, flag: '🇪🇺' },
  { code: 'et', name: 'Estonian', native_name: 'Eesti', direction: 'ltr', is_active: true, flag: '�.ee' },
  { code: 'eu', name: 'Basque', native_name: 'Euskara', direction: 'ltr', is_active: true, flag: '🇪🇸' },
  { code: 'fi', name: 'Finnish', native_name: 'Suomi', direction: 'ltr', is_active: true, flag: '🇫🇮' },
  { code: 'fj', name: 'Fijian', native_name: 'Vosa Vakaviti', direction: 'ltr', is_active: true, flag: '🇫🇯' },
  { code: 'fo', name: 'Faroese', native_name: 'Føroyskt', direction: 'ltr', is_active: true, flag: '🇫🇴' },
  { code: 'ga', name: 'Irish', native_name: 'Gaeilge', direction: 'ltr', is_active: true, flag: '🇮🇪' },
  { code: 'gd', name: 'Scottish Gaelic', native_name: 'Gàidhlig', direction: 'ltr', is_active: true, flag: '🇮🇪' },
  { code: 'gl', name: 'Galician', native_name: 'Galego', direction: 'ltr', is_active: true, flag: '🇪🇸' },
  { code: 'gn', name: 'Guarani', native_name: 'Avañe\'em', direction: 'ltr', is_active: true, flag: '🇧🇴' },
  { code: 'gu', name: 'Gujarati', native_name: 'ગુજરાતી', direction: 'ltr', is_active: true, flag: '🇮🇳' },
  { code: 'gv', name: 'Manx', native_name: 'Gaelg', direction: 'ltr', is_active: true, flag: '🇲🇨' },
  { code: 'ha', name: 'Hausa', native_name: 'Hausa', direction: 'ltr', is_active: true, flag: '🇳🇬' },
  { code: 'ho', name: 'Hiri Motu', native_name: 'Hiri Motu', direction: 'ltr', is_active: true, flag: '🇵🇫' },
  { code: 'hr', name: 'Croatian', native_name: 'Hrvatski', direction: 'ltr', is_active: true, flag: '🇭🇷' },
  { code: 'ht', name: 'Haitian', native_name: 'Kreyòl Ayisyen', direction: 'ltr', is_active: true, flag: '🇭🇹' },
  { code: 'hu', name: 'Hungarian', native_name: 'Magyar', direction: 'ltr', is_active: true, flag: '🇭🇺' },
  { code: 'hy', name: 'Armenian', native_name: 'Հայերեն', direction: 'ltr', is_active: true, flag: '🇰🇿' },
  { code: 'hz', name: 'Herero', native_name: 'Oshiwambo', direction: 'ltr', is_active: true, flag: 'NA' },
  { code: 'ia', name: 'Interlingua', native_name: 'Interlingua', direction: 'ltr', is_active: true, flag: '🇵🇦' },
  { code: 'ie', name: 'Interlingue', native_name: 'Interlingue', direction: 'ltr', is_active: true, flag: '🇦🇹' },
  { code: 'ik', name: 'Inupiaq', native_name: 'Iñupiaq', direction: 'ltr', is_active: true, flag: '🇺🇸' },
  { code: 'io', name: 'Ido', native_name: 'Ido', direction: 'ltr', is_active: true, flag: '🇮🇸' },
  { code: 'is', name: 'Icelandic', native_name: 'Íslenska', direction: 'ltr', is_active: true, flag: '🇮🇸' },
  { code: 'iu', name: 'Inuktitut', native_name: 'ᐃᓄᒃᑎᑐ', direction: 'ltr', is_active: true, flag: '🇨🇦' },
  { code: 'jv', name: 'Javanese', native_name: 'Basa Jawa', direction: 'ltr', is_active: true, flag: '🇮🇩' },
  { code: 'ka', name: 'Georgian', native_name: 'ქართული', direction: 'ltr', is_active: true, flag: '🇬🇪' },
  { code: 'kk', name: 'Kazakh', native_name: 'Қазақ', direction: 'ltr', is_active: true, flag: '🇰🇿' },
  { code: 'kl', name: 'Kalaallisut', native_name: 'Kalaallisut', direction: 'ltr', is_active: true, flag: '🇬🇱' },
  { code: 'km', name: 'Khmer', native_name: 'ភាសាខ្មែរ', direction: 'ltr', is_active: true, flag: '🇰🇭' },
  { code: 'ko', name: 'Korean', native_name: '한국어', direction: 'ltr', is_active: true, flag: '🇰🇷' },
  { code: 'kr', name: 'Kanuri', native_name: 'Kanuri', direction: 'ltr', is_active: true, flag: '🇳🇬' },
  { code: 'ks', name: 'Kashmiri', native_name: 'کشمیری', direction: 'rtl', is_active: true, flag: '🇵🇰' },
  { code: 'ku', name: 'Kurdish', native_name: 'Kurdî', direction: 'ltr', is_active: true, flag: '🇹🇷' },
  { code: 'kv', name: 'Komi', native_name: 'Коми', direction: 'ltr', is_active: true, flag: '🇷🇺' },
  { code: 'kw', name: 'Cornish', native_name: 'Kernewek', direction: 'ltr', is_active: true, flag: '🇬🇧' },
  { code: 'ky', name: 'Kyrgyz', native_name: 'Кыргыз', direction: 'ltr', is_active: true, flag: '🇨�yrillic' },
  { code: 'la', name: 'Latin', native_name: 'Latine', direction: 'ltr', is_active: true, flag: '🇻🇦' },
  { code: 'lb', name: 'Luxembourgish', native_name: 'Lëtzebuergesch', direction: 'ltr', is_active: true, flag: '🇱🇺' },
  { code: 'lg', name: 'Ganda', native_name: 'Oluganda', direction: 'ltr', is_active: true, flag: '🇺🇬' },
  { code: 'li', name: 'Limburgish', native_name: 'Limburgs', direction: 'ltr', is_active: true, flag: '🇳🇱' },
  { code: 'ln', name: 'Lingala', native_name: 'Lingala', direction: 'ltr', is_active: true, flag: '🇨🇬' },
  { code: 'lo', name: 'Lao', native_name: 'ລາວ', direction: 'ltr', is_active: true, flag: '🇱🇦' },
  { code: 'lt', name: 'Lithuanian', native_name: 'Lietuvių', direction: 'ltr', is_active: true, flag: '🇱🇹' },
  { code: 'lu', name: 'Luba-Katanga', native_name: 'Lubaa', direction: 'ltr', is_active: true, flag: '🇨🇩' },
  { code: 'lv', name: 'Latvian', native_name: 'Latviešu', direction: 'ltr', is_active: true, flag: '🇱🇻' },
  { code: 'mg', name: 'Malagasy', native_name: 'Malagasy', direction: 'ltr', is_active: true, flag: '🇲🇬' },
  { code: 'mh', name: 'Marshallese', native_name: 'Kajin M̧ajeļ', direction: 'ltr', is_active: true, flag: '🇲🇭' },
  { code: 'mi', name: 'Maori', native_name: 'Māori', direction: 'ltr', is_active: true, flag: '🇳🇿' },
  { code: 'mk', name: 'Macedonian', native_name: 'Македонски', direction: 'ltr', is_active: true, flag: '🇷🇴' },
  { code: 'mn', name: 'Mongolian', native_name: 'Монгол', direction: 'ltr', is_active: true, flag: '🇳🇲' },
  { code: 'mt', name: 'Maltese', native_name: 'Malti', direction: 'ltr', is_active: true, flag: '🇲🇹' },
  { code: 'my', name: 'Burmese', native_name: 'ဗမာ', direction: 'ltr', is_active: true, flag: '🇲🇲' },
  { code: 'na', name: 'Nauru', native_name: 'Nauru', direction: 'ltr', is_active: true, flag: '🇳🇷' },
  { code: 'nb', name: 'Norwegian Bokmål', native_name: 'Bokmål', direction: 'ltr', is_active: true, flag: '🇳🇴' },
  { code: 'nd', name: 'North Ndebele', native_name: 'iNdebele', direction: 'ltr', is_active: true, flag: '🇿🇼' },
  { code: 'ne', name: 'Nepali', native_name: 'नेपाली', direction: 'ltr', is_active: true, flag: '🇨🇵' },
  { code: 'ng', name: 'Ndonga', native_name: 'Oshindonga', direction: 'ltr', is_active: true, flag: 'NA' },
  { code: 'nn', name: 'Norwegian Nynorsk', native_name: 'Nynorsk', direction: 'ltr', is_active: true, flag: '🇳🇴' },
  { code: 'nr', name: 'South Ndebele', native_name: 'iSindebele', direction: 'ltr', is_active: true, flag: '🇿🇼' },
  { code: 'nv', name: 'Navajo', native_name: 'Diné', direction: 'ltr', is_active: true, flag: '🇺🇸' },
  { code: 'ny', name: 'Chichewa', native_name: 'Chichewa', direction: 'ltr', is_active: true, flag: '🇲🇼' },
  { code: 'oc', name: 'Occitan', native_name: 'Occitan', direction: 'ltr', is_active: true, flag: '🇫🇷' },
  { code: 'oj', name: 'Ojibwa', native_name: 'Ojibwemowin', direction: 'ltr', is_active: true, flag: '🇨🇦' },
  { code: 'om', name: 'Oromo', native_name: 'Afaan Oromoo', direction: 'ltr', is_active: true, flag: '🇪🇹🇴' },
  { code: 'or', name: 'Oriya', native_name: 'ଓଡ଼ିଆ', direction: 'ltr', is_active: true, flag: '🇮🇳' },
  { code: 'os', name: 'Ossetian', native_name: 'Осетин', direction: 'ltr', is_active: true, flag: '🇷🇺' },
  { code: 'pi', name: 'Pali', native_name: 'पालि', direction: 'ltr', is_active: true, flag: '🇮🇳' },
  { code: 'pl', name: 'Polish', native_name: 'Polski', direction: 'ltr', is_active: true, flag: '🇵🇱' },
  { code: 'qu', name: 'Quechua', native_name: 'Qhapaq Ñui', direction: 'ltr', is_active: true, flag: '🇵🇪' },
  { code: 'rm', name: 'Romansh', native_name: 'Rumantsch', direction: 'ltr', is_active: true, flag: '🇨🇭' },
  { code: 'ro', name: 'Romanian', native_name: 'Română', direction: 'ltr', is_active: true, flag: '🇷🇴' },
  { code: 'rw', name: 'Kinyarwanda', native_name: 'Ikinyarwanda', direction: 'ltr', is_active: true, flag: '🇷🇼' },
  { code: 'sa', name: 'Sanskrit', native_name: 'संस्कृत', direction: 'ltr', is_active: true, flag: 'IN' },
  { code: 'sc', name: 'Sardinian', native_name: 'Sardu', direction: 'ltr', is_active: true, flag: '🇮🇹' },
  { code: 'se', name: 'Northern Sami', native_name: 'Davvisámegiella', direction: 'ltr', is_active: true, flag: '🇩🇪' },
  { code: 'sg', name: 'Sango', native_name: 'Sängö', direction: 'ltr', is_active: true, flag: '🇨🇬' },
  { code: 'si', name: 'Sinhala', native_name: 'සිංහල', direction: 'ltr', is_active: true, flag: '🇱🇰' },
  { code: 'sk', name: 'Slovak', native_name: 'Slovenčina', direction: 'ltr', is_active: true, flag: '🇸🇰' },
  { code: 'sl', name: 'Slovenian', native_name: 'Slovenščina', direction: 'ltr', is_active: true, flag: '🇸🇮' },
  { code: 'sm', name: 'Samoan', native_name: 'Samoa', direction: 'ltr', is_active: true, flag: '🇼🇸' },
  { code: 'so', name: 'Somali', native_name: 'Soomaali', direction: 'ltr', is_active: true, flag: '🇸🇴' },
  { code: 'sq', name: 'Albanian', native_name: 'Shqip', direction: 'ltr', is_active: true, flag: '🇦🇱' },
  { code: 'sr', name: 'Serbian', native_name: 'Српски', direction: 'ltr', is_active: true, flag: '🇷🇸' },
  { code: 'ss', name: 'Swati', native_name: 'SiSwati', direction: 'ltr', is_active: true, flag: '🇸🇿' },
  { code: 'sv', name: 'Swedish', native_name: 'Svenska', direction: 'ltr', is_active: true, flag: '🇸🇪' },
  { code: 'ta', name: 'Tamil', native_name: 'தமிழ்', direction: 'ltr', is_active: true, flag: '🇲🇰' },
  { code: 'te', name: 'Telugu', native_name: 'తెలుగు', direction: 'ltr', is_active: true, flag: '🇮🇳' },
  { code: 'tg', name: 'Tajik', native_name: 'Тоҷикӣ', direction: 'ltr', is_active: true, flag: '🇹🇯' },
  { code: 'th', name: 'Thai', native_name: 'ไทย', direction: 'ltr', is_active: true, flag: '🇹🇭' },
  { code: 'ti', name: 'Tigrinya', native_name: 'ትግርኛ', direction: 'ltr', is_active: true, flag: '🇪🇷' },
  { code: 'tk', name: 'Turkmen', native_name: 'Türkmen', direction: 'ltr', is_active: true, flag: '🇹🇲' },
  { code: 'tl', name: 'Tagalog', native_name: 'Tagalog', direction: 'ltr', is_active: true, flag: '🇵🇭' },
  { code: 'tn', name: 'Tswana', native_name: 'Setswana', direction: 'ltr', is_active: true, flag: '🇧🇼' },
  { code: 'to', name: 'Tonga', native_name: 'Faka Tonga', direction: 'ltr', is_active: true, flag: '🇹🇴' },
  { code: 'tt', name: 'Tatar', native_name: 'Татар', direction: 'ltr', is_active: true, flag: '🇷🇺' },
  { code: 'tw', name: 'Twi', native_name: 'Twi', direction: 'ltr', is_active: true, flag: '🇬🇭' },
  { code: 'ty', name: 'Tahitian', native_name: 'Reo Mā`ohi', direction: 'ltr', is_active: true, flag: '🇵🇫' },
  { code: 'ug', name: 'Uyghur', native_name: 'ئۇيغۇرچە', direction: 'rtl', is_active: true, flag: '🇨🇳' },
  { code: 'uk', name: 'Ukrainian', native_name: 'Українська', direction: 'ltr', is_active: true, flag: '🇺🇦' },
  { code: 'uz', name: 'Uzbek', native_name: 'O\'zbek', direction: 'ltr', is_active: true, flag: '🇺🇿' },
  { code: 've', name: 'Venda', native_name: 'Tshivenda', direction: 'ltr', is_active: true, flag: '🇿🇼' },
  { code: 'vo', name: 'Volapük', native_name: 'Volapük', direction: 'ltr', is_active: true, flag: 'VO' },
  { code: 'wa', name: 'Walloon', native_name: 'Wallon', direction: 'ltr', is_active: true, flag: '🇧🇪' },
  { code: 'wo', name: 'Wolof', native_name: 'Wolof', direction: 'ltr', is_active: true, flag: '🇸🇳' },
  { code: 'xh', name: 'Xhosa', native_name: 'IsiXhosa', direction: 'ltr', is_active: true, flag: '🇿🇦' },
  { code: 'yi', name: 'Yiddish', native_name: 'ייִדיש', direction: 'rtl', is_active: true, flag: '🇦🇹' },
  { code: 'za', name: 'Zulu', native_name: 'IsiZulu', direction: 'ltr', is_active: true, flag: '🇿🇦' },
];