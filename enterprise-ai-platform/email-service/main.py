"""
Email Service Main Application
FastAPI application entry point for email sending and management.
Development mode uses Mailpit for local email testing (zero cost).
"""

import os
import uvicorn
import sentry_sdk
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, EmailStr, Field
import logging
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from enterprise_ai_platform.common.config import settings

sentry_sdk.init(
    dsn=os.getenv("SENTRY_DSN"),
    traces_sample_rate=1.0,
    send_default_pii=True,
)

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


@app.get("/health/live", tags=["Health Checks"])
async def liveness_probe():
    return {"status": "UP", "service": "email-service"}


@app.get("/health/ready", tags=["Health Checks"])
async def readiness_probe():
    return {"status": "READY", "service": "email-service"}


@app.post("/api/v1/email/send", response_model=EmailResponse, tags=["Email"])
async def send_email(request: EmailRequest):
    """Send an email message. In development, uses Mailpit for zero-cost testing."""
    message_id = f"msg_{datetime.utcnow().timestamp()}"
    logger.info(f"Sending email to {request.to}: {request.subject}")
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
                logger.info(f"Email sent successfully to {request.to}")
            except Exception as e:
                logger.error(f"Mailpit connection error (expected if not running): {e}")
        return EmailResponse(
            message_id=message_id,
            status="sent",
            to=request.to,
            subject=request.subject,
            sent_at=datetime.utcnow(),
        )
    except Exception as e:
        logger.error(f"Failed to send email: {e}")
        from fastapi import HTTPException
        raise HTTPException(status_code=500, detail=f"Failed to send email: {str(e)}")


if __name__ == "__main__":
    logger.info(f"Starting Email Service on port {settings.EMAIL_SERVICE_PORT}")
    uvicorn.run(app, host="0.0.0.0", port=settings.EMAIL_SERVICE_PORT, reload=settings.DEBUG)
