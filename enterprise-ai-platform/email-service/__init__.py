"""
Email Service Module
Handles sending emails with PDF attachments for invoices and receipts.
"""

import os
import base64
from typing import Optional
from smtplib import SMTP
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import logging

logger = logging.getLogger("salesgenie.email")


class EmailService:
    def __init__(self):
        self.smtp_host = os.getenv("SMTP_HOST", "localhost")
        self.smtp_port = int(os.getenv("SMTP_PORT", "1025"))
        self.smtp_user = os.getenv("SMTP_USER", "")
        self.smtp_pass = os.getenv("SMTP_PASS", "")
        self.from_email = os.getenv("FROM_EMAIL", "billing@salesgenie.ai")
        self.from_name = os.getenv("FROM_NAME", "SalesGenie Billing")
    
    def send_invoice_email(
        self,
        tenant_id: str,
        subject: str,
        body: str,
        attachment_bytes: bytes,
        attachment_name: str,
        to_email: Optional[str] = None,
    ) -> dict:
        """Send an email with PDF attachment."""
        try:
            msg = MIMEMultipart()
            msg["From"] = f"{self.from_name} <{self.from_email}>"
            msg["To"] = to_email or f"tenant-{tenant_id}@salesgenie.ai"
            msg["Subject"] = subject
            
            html_part = MIMEText(body, "html")
            msg.attach(html_part)
            
            with open(f"/tmp/{attachment_name}", "wb") as f:
                f.write(attachment_bytes)
            
            with open(f"/tmp/{attachment_name}", "rb") as f:
                pdf_part = MIMEApplication(f.read(), _subtype="pdf")
                pdf_part.add_header("Content-Disposition", "attachment", filename=attachment_name)
                msg.attach(pdf_part)
            
            with SMTP(self.smtp_host, self.smtp_port) as server:
                if self.smtp_user and self.smtp_pass:
                    server.starttls()
                    server.login(self.smtp_user, self.smtp_pass)
                server.send_message(msg)
            
            logger.info(f"Sent invoice email to tenant {tenant_id}: {subject}")
            return {"status": "sent", "to": to_email, "subject": subject}
            
        except Exception as e:
            logger.error(f"Failed to send invoice email: {e}")
            return {"status": "failed", "error": str(e)}


email_service = EmailService()