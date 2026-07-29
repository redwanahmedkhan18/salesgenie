"""
End-to-End tests for SalesGenie platform
Tests full user workflows from login to feature usage
"""

import pytest
from playwright.sync_api import sync_playwright, Page, BrowserContext
import os


BASE_URL = os.getenv("TEST_BASE_URL", "http://localhost:3000")
API_URL = os.getenv("TEST_API_URL", "http://localhost:8000/api/v1")


class TestAuthenticationFlow:
    def test_login_page_loads(self, page: Page):
        page.goto(f"{BASE_URL}/login")
        assert page.title().contains("SalesGenie") or page.locator("text=Login").is_visible()

    def test_user_login_flow(self, page: Page, test_user: dict):
        page.goto(f"{BASE_URL}/login")
        
        page.fill('input[name="email"]', test_user["email"])
        page.fill('input[name="password"]', test_user["password"])
        page.click('button[type="submit"]')
        
        page.wait_for_url("**/dashboard", timeout=5000)
        assert "dashboard" in page.url

    def test_mfa_flow(self, page: Page, test_user: dict):
        page.goto(f"{BASE_URL}/login")
        page.fill('input[name="email"]', test_user["email"])
        page.fill('input[name="password"]', test_user["password"])
        page.click('button[type="submit"]')
        
        page.wait_for_selector('input[name="mfa_code"]', timeout=5000)
        page.fill('input[name="mfa_code"]', "123456")
        page.click('button[type="submit"]')
        
        assert "dashboard" in page.url


class TestLeadIntelligenceFlow:
    def test_lead_search_workflow(self, page: Page, authenticated_session: Page):
        page.goto(f"{BASE_URL}/app/leads")
        
        assert page.locator("text=Lead Intelligence").is_visible()
        
        page.fill('input[placeholder*="Industry" i], input[placeholder*="industry" i]', "Technology")
        page.click('button:has-text("Search")')
        
        page.wait_for_selector('.company-card, .result-item', timeout=10000)

    def test_lead_qualification_workflow(self, page: Page, authenticated_session: Page):
        page.goto(f"{BASE_URL}/app/leads")
        
        page.click('button:has-text("Qualify")', timeout=5000)
        
        page.wait_for_selector('.lead-score, .score-display', timeout=5000)

    def test_outreach_draft_generation(self, page: Page, authenticated_session: Page):
        page.goto(f"{BASE_URL}/app/leads")
        
        page.click('button:has-text("Generate Draft")', timeout=5000)
        
        page.wait_for_selector('.draft-preview, textarea', timeout=5000)

    def test_language_switching(self, page: Page, authenticated_session: Page):
        page.goto(f"{BASE_URL}/app/leads")
        
        page.click('.language-selector, button:has-text("🌐")', timeout=5000)
        
        page.click('text=Spanish', timeout=5000)
        
        page.wait_for_selector('text=Español', timeout=3000)


class TestWhatsAppIntegration:
    def test_channel_management(self, page: Page, authenticated_session: Page):
        page.goto(f"{BASE_URL}/app/channels")
        
        assert page.locator("text=Channels").is_visible()
        
        page.click('button:has-text("WhatsApp")', timeout=5000)
        
        page.wait_for_selector('.channel-card, .whatsapp-setup', timeout=5000)

    def test_whatsapp_message_send(self, page: Page, authenticated_session: Page):
        page.goto(f"{BASE_URL}/app/channels")
        
        page.click('button:has-text("Send Message")', timeout=5000)
        
        page.fill('input[name="to"]', "+1234567890")
        page.fill('textarea[name="message"]', "Test message from SalesGenie")
        page.click('button:has-text("Send")')
        
        assert page.locator('text=Message sent').is_visible() or page.locator('.toast-success').is_visible()


class TestMultiLanguage:
    def test_english_ui(self, page: Page):
        page.goto(f"{BASE_URL}/")
        
        assert page.locator("text=Login").is_visible()

    def test_spanish_ui(self, page: Page):
        page.goto(f"{BASE_URL}/?lang=es")
        
        page.wait_for_selector('html[lang="es"], html[lang="es-ES"]', timeout=5000)


class TestSecurity:
    def test_no_sensitive_data_in_response(self, page: Page):
        page.goto(f"{BASE_URL}/")
        
        content = page.content()
        
        assert "password" not in content.lower() or "type=\"password\"" in content.lower()
        assert "api_key" not in content.lower()
        assert "secret" not in content.lower() or "secret-key" in content.lower()

    def test_security_headers(self, page: Page):
        response = page.request.get(f"{BASE_URL}/")
        
        headers = response.headers
        
        assert "x-content-type-options" in {k.lower() for k in headers.keys()}
        assert "x-frame-options" in {k.lower() for k in headers.keys()}

    def test_authentication_required(self, page: Page):
        page.goto(f"{BASE_URL}/app/leads")
        
        page.wait_for_url("**/login", timeout=5000)


@pytest.fixture
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()
        yield page
        browser.close()


@pytest.fixture
def authenticated_session(page: Page, test_user: dict):
    page.goto(f"{BASE_URL}/login")
    page.fill('input[name="email"]', test_user["email"])
    page.fill('input[name="password"]', test_user["password"])
    page.click('button[type="submit"]')
    page.wait_for_url("**/dashboard", timeout=10000)
    yield page


@pytest.fixture
def test_user():
    return {
        "email": "test@salesgenie.ai",
        "password": "TestPassword123!",
    }