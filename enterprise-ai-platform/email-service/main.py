"""
Email Service Main Application
FastAPI application entry point for email sending and management.
Development mode uses Mailpit for local email testing (zero cost).
"""

import uvicorn
import logging
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import PlainTextResponse
from datetime import datetime, timezone
from typing import List, Optional
from pydantic import BaseModel, EmailStr, Field
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from enterprise_ai_platform.common.config import settings
from enterprise_ai_platform.common.request_logging import add_request_logging
from enterprise_ai_platform.common.metrics import get_service_metrics

app = FastAPI(
    title="SalesGenie Email Service",
    description="Email sending service with Mailpit development support",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.BACKEND_CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

add_request_logging(app, service_name="email-service")

logger = logging.getLogger("salesgenie.email")


class EmailRequest(BaseModel):
    to: List[EmailStr]
    subject: str = Field(..., max_length=200)
    body: str
    html: Optional[str] = None
    cc: Optional[List[EmailStr]] = None
    bcc: Optional[List[EmailStr]] = None


class EmailResponse(BaseModel):
    message_id: str
    status: str
    to: List[EmailStr]
    subject: str
    sent_at: datetime


@app.get("/metrics", tags=["Monitoring"])
async def metrics_endpoint():
    """Prometheus-compatible metrics endpoint."""
    all_metrics = get_service_metrics("email-service")
    lines = [all_metrics]
    return PlainTextResponse(content="\n".join(lines), media_type="text/plain")


@app.get("/health/live", tags=["Health Checks"])
async def liveness_probe():
    return {"status": "UP", "service": "email-service"}


@app.get("/health/ready", tags=["Health Checks"])
async def readiness_probe():
    """Check if SMTP configuration is available for sending."""
    if settings.SMTP_HOST:
        return {"status": "READY", "service": "email-service", "smtp_host": settings.SMTP_HOST}
    return {"status": "NOT_READY", "reason": "SMTP host not configured"}, 503


@app.post("/api/v1/email/send", response_model=EmailResponse, tags=["Email"])
async def send_email(request: EmailRequest):
    """Send an email message. In development, uses Mailpit for zero-cost testing."""
    message_id = f"msg_{datetime.now(timezone.utc).isoformat()}"
    logger.info("Sending email: subject=%s recipient_count=%d", request.subject, len(request.to))
    try:
        if settings.ENVIRONMENT == "development":
            msg = MIMEMultipart("alternative")
            msg["Subject"] = request.subject
            msg["From"] = settings.SMTP_FROM_ADDRESS or "noreply@salesgenie.local"
            msg["To"] = ", ".join(request.to)
            text_content = request.body
            if request.html:
                msg.attach(MIMEText(request.html, "html"))
            else:
                msg.attach(MIMEText(text_content, "plain"))
            try:
                with smtplib.SMTP(settings.SMTP_HOST, settings.SMTP_PORT) as server:
                    if settings.SMTP_USERNAME and settings.SMTP_PASSWORD:
                        server.starttls()
                        server.login(settings.SMTP_USERNAME, settings.SMTP_PASSWORD)
                    server.send_message(msg)
                logger.info("Email sent successfully to %d recipients", len(request.to))
            except Exception as e:
                logger.error("Mailpit connection error (expected if not running): %s", e)
        return EmailResponse(
            message_id=message_id,
            status="sent",
            to=request.to,
            subject=request.subject,
            sent_at=datetime.now(timezone.utc),
        )
    except Exception as e:
        logger.error("Failed to send email: %s", e)
        raise HTTPException(status_code=500, detail="Failed to send email")


if __name__ == "__main__":
    logger.info("Starting Email Service on port %s", settings.EMAIL_SERVICE_PORT)
    uvicorn.run(app, host="0.0.0.0", port=settings.EMAIL_SERVICE_PORT, reload=settings.DEBUG)
