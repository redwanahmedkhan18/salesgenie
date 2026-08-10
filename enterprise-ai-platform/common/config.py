"""
Enterprise Platform Configuration
Provides centralized management of environment variables and application settings.
"""

from typing import List, Optional
from pydantic import Field, model_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class PlatformSettings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
        case_sensitive=False,
    )

    ENVIRONMENT: str = Field(default="development", description="Environment mode: development, staging, production")
    DEBUG: bool = Field(default=True, description="Debug flag")
    LOG_LEVEL: str = Field(default="INFO", description="Log level: DEBUG, INFO, WARNING, ERROR, CRITICAL")
    PROJECT_NAME: str = "SalesGenie Enterprise AI Platform"
    API_V1_STR: str = "/api/v1"

    # Stripe (Billing) - REQUIRED if billing service is enabled
    STRIPE_SECRET_KEY: Optional[str] = Field(default=None, description="Stripe secret API key - REQUIRED in production", exclude=True)
    STRIPE_WEBHOOK_SECRET: Optional[str] = Field(default=None, description="Stripe webhook signing secret", exclude=True)

    POSTGRES_USER: str = Field(default="salesgenie_admin", description="PostgreSQL Username")
    POSTGRES_PASSWORD: Optional[str] = Field(default=None, description="PostgreSQL Password - REQUIRED in production", exclude=True)
    POSTGRES_HOST: str = Field(default="localhost", description="PostgreSQL Host")
    POSTGRES_PORT: int = Field(default=5432, description="PostgreSQL Port")
    POSTGRES_DB: str = Field(default="salesgenie_db", description="PostgreSQL Database Name")
    
    USE_SQLITE: bool = Field(default=False, description="Use SQLite instead of PostgreSQL (for development)")
    
    DB_POOL_SIZE: int = Field(default=20, description="SQLAlchemy connection pool size")
    DB_MAX_OVERFLOW: int = Field(default=10, description="SQLAlchemy connection max overflow")
    DB_POOL_TIMEOUT: int = Field(default=30, description="Pool timeout seconds")
    DB_POOL_RECYCLE: int = Field(default=3600, description="Pool recycle seconds")

    @property
    def ASYNC_DATABASE_URL(self) -> str:
        if self.USE_SQLITE:
            return "sqlite+aiosqlite:///./salesgenie_dev.db"
        return f"postgresql+asyncpg://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"

    @property
    def SYNC_DATABASE_URL(self) -> str:
        if self.USE_SQLITE:
            return "sqlite:///./salesgenie_dev.db"
        return f"postgresql+psycopg2://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"

    # Keycloak & Auth Settings
    KEYCLOAK_SERVER_URL: str = Field(default="http://localhost:8080", description="Keycloak server URL")
    KEYCLOAK_REALM: str = Field(default="salesgenie-realm", description="Keycloak realm name")
    KEYCLOAK_CLIENT_ID: str = Field(default="salesgenie-auth-client", description="Keycloak client ID")
    KEYCLOAK_CLIENT_SECRET: Optional[str] = Field(default=None, description="Keycloak client secret - REQUIRED in production", exclude=True)
    KEYCLOAK_ADMIN_USERNAME: Optional[str] = Field(default=None, description="Keycloak admin username", exclude=True)
    KEYCLOAK_ADMIN_PASSWORD: Optional[str] = Field(default=None, description="Keycloak admin password - REQUIRED in production", exclude=True)

    # JWT Settings
    JWT_SECRET_KEY: Optional[str] = Field(default=None, description="JWT secret key - REQUIRED in production", exclude=True)
    JWT_ALGORITHM: str = Field(default="HS256", description="JWT Signing Algorithm")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = Field(default=60, description="Access token expiration in minutes")
    REFRESH_TOKEN_EXPIRE_DAYS: int = Field(default=14, description="Refresh token expiration in days")
    JWT_PUBLIC_KEY: Optional[str] = Field(default=None, description="RS256 Public Key for verification")

    # PII Encryption
    PII_ENCRYPTION_KEY: Optional[str] = Field(default=None, description="PII field encryption key - REQUIRED in production", exclude=True)

    # Redis Settings
    REDIS_HOST: str = Field(default="localhost", description="Redis Host")
    REDIS_PORT: int = Field(default=6379, description="Redis Port")
    REDIS_PASSWORD: Optional[str] = Field(default=None, description="Redis Password")
    REDIS_DB: int = Field(default=0, description="Redis DB Index")

    @property
    def REDIS_URL(self) -> str:
        auth_str = f":{self.REDIS_PASSWORD}@" if self.REDIS_PASSWORD else ""
        return f"redis://{auth_str}{self.REDIS_HOST}:{self.REDIS_PORT}/{self.REDIS_DB}"

    # OAuth2 Providers Configuration
    GOOGLE_CLIENT_ID: Optional[str] = Field(default=None)
    GOOGLE_CLIENT_SECRET: Optional[str] = Field(default=None)
    MICROSOFT_CLIENT_ID: Optional[str] = Field(default=None)
    MICROSOFT_CLIENT_SECRET: Optional[str] = Field(default=None)
    GITHUB_CLIENT_ID: Optional[str] = Field(default=None)
    GITHUB_CLIENT_SECRET: Optional[str] = Field(default=None)

    # Sentry (Error Tracking) - Optional but recommended for production
    SENTRY_DSN: Optional[str] = Field(default=None, description="Sentry DSN for error tracking")

    # CORS
    BACKEND_CORS_ORIGINS: List[str] = [
        "http://localhost:3000",
        "http://localhost:4321",
        "http://127.0.0.1:4321",
        "http://192.168.0.106:4321",
        "https://salesgenie.ai",
    ]

    # Channel Integration Settings - WhatsApp
    WHATSAPP_ACCESS_TOKEN: Optional[str] = Field(default=None, description="WhatsApp Business API Access Token")
    WHATSAPP_PHONE_NUMBER_ID: Optional[str] = Field(default=None, description="WhatsApp Phone Number ID")
    WHATSAPP_WEBHOOK_URL: Optional[str] = Field(default=None, description="WhatsApp Webhook URL")
    WHATSAPP_VERIFY_TOKEN: Optional[str] = Field(default="salesgenie_webhook_verify_token", description="WhatsApp Webhook Verify Token")

    # Channel Integration Settings - Telegram
    TELEGRAM_BOT_TOKEN: Optional[str] = Field(default=None, description="Telegram Bot Token")
    TELEGRAM_WEBHOOK_URL: Optional[str] = Field(default=None, description="Telegram Webhook URL")

    # Channel Integration Settings - Facebook Messenger
    FACEBOOK_PAGE_ACCESS_TOKEN: Optional[str] = Field(default=None, description="Facebook Page Access Token")
    FACEBOOK_WEBHOOK_URL: Optional[str] = Field(default=None, description="Facebook Messenger Webhook URL")
    FACEBOOK_VERIFY_TOKEN: Optional[str] = Field(default="salesgenie_messenger_verify", description="Facebook Webhook Verify Token")
    INSTAGRAM_BUSINESS_ACCOUNT_ID: Optional[str] = Field(default=None, description="Instagram Business Account ID")

    # Channel Integration Settings - Email
    SMTP_HOST: str = Field(default="localhost", description="SMTP Host - use localhost for Mailpit in dev")
    SMTP_PORT: int = Field(default=1025, description="SMTP Port - 1025 for Mailpit, 587 for SendGrid")
    SMTP_USERNAME: Optional[str] = Field(default=None, description="SMTP Username")
    SMTP_PASSWORD: Optional[str] = Field(default=None, description="SMTP Password/API Key")
    SMTP_FROM_ADDRESS: str = Field(default="noreply@salesgenie.local", description="SMTP From Address")
    FRONTEND_BASE_URL: str = Field(default="http://localhost:4321", description="Frontend base URL for password reset links")
    PASSWORD_RESET_PATH: str = Field(default="/reset-password", description="Password reset page path")

    # Channel Integration Settings - SMS (Twilio)
    TWILIO_ACCOUNT_SID: Optional[str] = Field(default=None, description="Twilio Account SID")
    TWILIO_AUTH_TOKEN: Optional[str] = Field(default=None, description="Twilio Auth Token")
    TWILIO_PHONE_NUMBER: Optional[str] = Field(default=None, description="Twilio Phone Number")

    # Channel Integration Settings - SendGrid (Email)
    SENDGRID_API_KEY: Optional[str] = Field(default=None, description="SendGrid API Key")

    # Channel Integration Settings - Slack
    SLACK_BOT_TOKEN: Optional[str] = Field(default=None, description="Slack Bot Token")
    SLACK_SIGNING_SECRET: Optional[str] = Field(default=None, description="Slack Signing Secret")
    SLACK_WEBHOOK_URL: Optional[str] = Field(default=None, description="Slack Webhook URL")

    # Channel Integration Settings - Discord
    DISCORD_BOT_TOKEN: Optional[str] = Field(default=None, description="Discord Bot Token")

    # Super Admin Configuration
    SALESGENIE_SUPER_ADMIN_EMAILS: str = Field(
        default="admin@yourcompany.com,owner@yourcompany.com",
        description="Comma-separated list of emails that receive super admin role on signup"
    )
    SALESGENIE_SUPER_ADMIN_NAME: str = Field(
        default="Super Admin",
        description="Default name for super admin users"
    )
    SALESGENIE_SUPER_ADMIN_PASSWORD: Optional[str] = Field(
        default=None,
        description="Default password for super admin users - REQUIRED in production",
        exclude=True,
    )

    # Language Settings
    DEFAULT_LANGUAGE: str = Field(default="en", description="Default application language (ISO 639-1 code)")
    SUPPORTED_LANGUAGES: str = Field(default="en,es,fr,de,it,pt,nl,ru,zh,ja,ko,ar,he,hi,bn,ta,te,mr,gu,kn,ml,pa,ur,id,ms,th,vi,tr,sw,fa,ps,ug", description="Comma-separated list of supported language codes")
    LANGUAGE_DIRECTION_RTL: str = Field(default="ar,he,fa,ps,ug,ur,yi", description="Comma-separated list of RTL language codes")

    # Channel Integration Settings - Service Ports
    AUTH_SERVICE_PORT: int = Field(default=8001, description="Auth Service Port")
    USER_SERVICE_PORT: int = Field(default=8002, description="User Service Port")
    ORGANIZATION_SERVICE_PORT: int = Field(default=8003, description="Organization Service Port")
    BILLING_SERVICE_PORT: int = Field(default=8004, description="Billing Service Port")
    AI_GATEWAY_SERVICE_PORT: int = Field(default=8000, description="AI Gateway Service Port")
    WEBSOCKET_SERVICE_PORT: int = Field(default=8000, description="WebSocket Service Port")
    WHATSAPP_SERVICE_PORT: int = Field(default=8005, description="WhatsApp Service Port")
    KNOWLEDGE_SERVICE_PORT: int = Field(default=8006, description="Knowledge Service Port")
    SALES_SERVICE_PORT: int = Field(default=8007, description="Sales Service Port")
    TICKET_SERVICE_PORT: int = Field(default=8008, description="Ticket Service Port")
    VECTOR_SERVICE_PORT: int = Field(default=8009, description="Vector Service Port")
    CHAT_SERVICE_PORT: int = Field(default=8010, description="Chat Service Port")
    WORKFLOW_SERVICE_PORT: int = Field(default=8011, description="Workflow Service Port")
    ANALYTICS_SERVICE_PORT: int = Field(default=8012, description="Analytics Service Port")
    SEARCH_SERVICE_PORT: int = Field(default=8013, description="Search Service Port")
    NOTIFICATION_SERVICE_PORT: int = Field(default=8014, description="Notification Service Port")
    FILE_SERVICE_PORT: int = Field(default=8015, description="File Service Port")
    CUSTOMER_SERVICE_PORT: int = Field(default=8016, description="Customer Service Port")
    SUPPORT_SERVICE_PORT: int = Field(default=8017, description="Support Service Port")
    CONVERSATION_SERVICE_PORT: int = Field(default=8018, description="Conversation Service Port")
    TELEGRAM_SERVICE_PORT: int = Field(default=8019, description="Telegram Service Port")
    MESSENGER_SERVICE_PORT: int = Field(default=8020, description="Messenger Service Port")
    EMAIL_SERVICE_PORT: int = Field(default=8021, description="Email Service Port")
    LEAD_INTELLIGENCE_SERVICE_PORT: int = Field(default=8022, description="Lead Intelligence Service Port")
    AUDIT_SERVICE_PORT: int = Field(default=8023, description="Audit Service Port")
    SLACK_SERVICE_PORT: int = Field(default=8024, description="Slack Service Port")
    DISCORD_SERVICE_PORT: int = Field(default=8026, description="Discord Service Port")

    @model_validator(mode="after")
    def validate_production_secrets(self):
        """Enforce that required secrets are set in production environment."""
        if self.ENVIRONMENT == "production":
            required_secrets = {
                "POSTGRES_PASSWORD": self.POSTGRES_PASSWORD,
                "JWT_SECRET_KEY": self.JWT_SECRET_KEY,
            }

            # Add optional production-only secrets if services are enabled
            if getattr(self, 'STRIPE_SECRET_KEY', None):
                required_secrets["STRIPE_SECRET_KEY"] = self.STRIPE_SECRET_KEY
            if getattr(self, 'STRIPE_WEBHOOK_SECRET', None):
                required_secrets["STRIPE_WEBHOOK_SECRET"] = self.STRIPE_WEBHOOK_SECRET

            required_secrets["PII_ENCRYPTION_KEY"] = self.PII_ENCRYPTION_KEY

            missing = [k for k, v in required_secrets.items() if not v]
            if missing:
                raise ValueError(
                    f"Production environment requires these secrets to be set: {missing}. "
                    f"Please set them via environment variables or secret manager."
                )
        return self


settings = PlatformSettings()
