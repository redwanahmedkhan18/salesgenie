"""
Email Service Tests
Test email sending functionality with Mailpit mock server.
"""

import pytest
from fastapi.testclient import TestClient
from main import app, send_email


client = TestClient(app)


def test_health_check():
    """Test health check endpoint."""
    response = client.get("/health/live")
    assert response.status_code == 200
    assert response.json() == {"status": "UP", "service": "email-service"}


def test_readiness_check():
    """Test readiness check endpoint."""
    response = client.get("/health/ready")
    assert response.status_code == 200
    assert response.json() == {"status": "READY", "service": "email-service"}


def test_send_email():
    """Test sending an email."""
    email_data = {
        "to": ["test@example.com"],
        "subject": "Test Email",
        "body": "This is a test email body",
    }
    response = client.post("/api/v1/email/send", json=email_data)
    assert response.status_code == 200
    assert response.json()["status"] == "sent"
    assert "message_id" in response.json()


def test_send_email_with_html():
    """Test sending an email with HTML content."""
    email_data = {
        "to": ["test@example.com"],
        "subject": "Test HTML Email",
        "body": "Plain text content",
        "html": "<html><body><h1>HTML Content</h1></body></html>",
    }
    response = client.post("/api/v1/email/send", json=email_data)
    assert response.status_code == 200


def test_send_bulk_emails():
    """Test sending multiple emails."""
    emails = [
        {"to": ["user1@example.com"], "subject": "Email 1", "body": "Body 1"},
        {"to": ["user2@example.com"], "subject": "Email 2", "body": "Body 2"},
    ]
    response = client.post("/api/v1/email/bulk", json=emails)
    assert response.status_code == 200
    assert len(response.json()) == 2


def test_get_email_config():
    """Test getting email configuration."""
    response = client.get("/api/v1/email/config")
    assert response.status_code == 200
    data = response.json()
    assert "smtp_host" in data
    assert "smtp_port" in data


if __name__ == "__main__":
    pytest.main([__file__, "-v"])