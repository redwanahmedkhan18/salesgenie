"""
Enterprise Platform Configuration
Provides centralized management of environment variables and application settings.
"""

from typing import List, Optional
from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class PlatformSettings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
        case_sensitive=False,
    )

    # Environment
    ENVIRONMENT: str = Field(default="development", description="Environment mode: development, staging, production")
    DEBUG: bool = Field(default=True, description="Debug flag")
    PROJECT_NAME: str = "SalesGenie Enterprise AI Platform"
    API_V1_STR: str = "/api/v1"

    # Database Settings (PostgreSQL + pgvector)
    POSTGRES_USER: str = Field(default="salesgenie_admin", description="PostgreSQL Username")
    POSTGRES_PASSWORD: str = Field(default="salesgenie_secret_pass_2026", description="PostgreSQL Password")
    POSTGRES_HOST: str = Field(default="localhost", description="PostgreSQL Host")
    POSTGRES_PORT: int = Field(default=5432, description="PostgreSQL Port")
    POSTGRES_DB: str = Field(default="salesgenie_db", description="PostgreSQL Database Name")
    
    # DB Pool Tuning
    DB_POOL_SIZE: int = Field(default=20, description="SQLAlchemy connection pool size")
    DB_MAX_OVERFLOW: int = Field(default=10, description="SQLAlchemy connection max overflow")
    DB_POOL_TIMEOUT: int = Field(default=30, description="Pool timeout seconds")
    DB_POOL_RECYCLE: int = Field(default=3600, description="Pool recycle seconds")

    @property
    def ASYNC_DATABASE_URL(self) -> str:
        return f"postgresql+asyncpg://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"

    @property
    def SYNC_DATABASE_URL(self) -> str:
        return f"postgresql+psycopg2://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"

    # Keycloak & Auth Settings
    KEYCLOAK_SERVER_URL: str = Field(default="http://localhost:8080", description="Keycloak server URL")
    KEYCLOAK_REALM: str = Field(default="salesgenie-realm", description="Keycloak realm name")
    KEYCLOAK_CLIENT_ID: str = Field(default="salesgenie-auth-client", description="Keycloak client ID")
    KEYCLOAK_CLIENT_SECRET: str = Field(default="salesgenie-client-secret-keycloak", description="Keycloak client secret")

    # JWT Settings
    JWT_SECRET_KEY: str = Field(default="salesgenie_super_secret_jwt_key_2026_change_in_prod", description="JWT secret key for HS256 fallbacks")
    JWT_ALGORITHM: str = Field(default="HS256", description="JWT Signing Algorithm")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = Field(default=60, description="Access token expiration in minutes")
    REFRESH_TOKEN_EXPIRE_DAYS: int = Field(default=14, description="Refresh token expiration in days")
    JWT_PUBLIC_KEY: Optional[str] = Field(default=None, description="RS256 Public Key for verification")

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

    # CORS
    BACKEND_CORS_ORIGINS: List[str] = [
        "http://localhost:3000",
        "http://localhost:4321",
        "http://127.0.0.1:4321",
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
    SMTP_HOST: Optional[str] = Field(default="smtp.sendgrid.net", description="SMTP Host")
    SMTP_PORT: int = Field(default=587, description="SMTP Port")
    SMTP_USERNAME: Optional[str] = Field(default="apikey", description="SMTP Username")
    SMTP_PASSWORD: Optional[str] = Field(default=None, description="SMTP Password/API Key")
    SMTP_FROM_ADDRESS: Optional[str] = Field(default="noreply@salesgenie.ai", description="SMTP From Address")

    # Channel Integration Settings - SMS (Twilio)
    TWILIO_ACCOUNT_SID: Optional[str] = Field(default=None, description="Twilio Account SID")
    TWILIO_AUTH_TOKEN: Optional[str] = Field(default=None, description="Twilio Auth Token")
    TWILIO_PHONE_NUMBER: Optional[str] = Field(default=None, description="Twilio Phone Number")

    # Channel Integration Settings - SendGrid (Email)
    SENDGRID_API_KEY: Optional[str] = Field(default=None, description="SendGrid API Key")

    # Language Settings
    DEFAULT_LANGUAGE: str = Field(default="en", description="Default application language (ISO 639-1 code)")
    SUPPORTED_LANGUAGES: str = Field(default="en,es,fr,de,it,pt,nl,ru,zh,ja,ko,ar,he,hi,bn,ta,te,mr,gu,kn,ml,pa,ur,id,ms,th,vi,tr,sw,fa,ps,ug", description="Comma-separated list of supported language codes")
    LANGUAGE_DIRECTION_RTL: str = Field(default="ar,he,fa,ps,ug,ur,yi", description="Comma-separated list of RTL language codes")

    # Channel Integration Settings - Service Ports
    WHATSAPP_SERVICE_PORT: int = Field(default=8016, description="WhatsApp Service Port")
    TELEGRAM_SERVICE_PORT: int = Field(default=8017, description="Telegram Service Port")
    MESSENGER_SERVICE_PORT: int = Field(default=8018, description="Messenger Service Port")
    EMAIL_SERVICE_PORT: int = Field(default=8019, description="Email Service Port")
    LEAD_INTELLIGENCE_SERVICE_PORT: int = Field(default=8016, description="Lead Intelligence Service Port")


settings = PlatformSettings()
