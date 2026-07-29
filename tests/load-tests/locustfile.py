"""
Load testing script for SalesGenie API
Tests API Gateway, Lead Intelligence, and WhatsApp services
"""

import locust
from locust import HttpUser, task, between, events
import random
import json
from faker import Faker

fake = Faker()


class LeadIntelligenceUser(HttpUser):
    wait_time = between(1, 3)
    
    def on_start(self):
        self.headers = {
            "Authorization": "Bearer test-token",
            "Content-Type": "application/json"
        }
    
    @task(10)
    def search_companies(self):
        industries = ["Technology", "Healthcare", "Finance", "E-commerce", "SaaS"]
        self.client.post(
            "/api/v1/lead-intelligence/companies/search",
            json={
                "industry": random.choice(industries),
                "min_employee_count": random.randint(10, 1000),
                "max_employee_count": random.randint(100, 5000),
                "keywords": "AI,automation"
            },
            headers=self.headers
        )
    
    @task(5)
    def qualify_lead(self):
        company_id = fake.uuid4()
        self.client.post(
            f"/api/v1/lead-intelligence/companies/{company_id}/qualify",
            headers=self.headers
        )
    
    @task(3)
    def generate_research(self):
        company_id = fake.uuid4()
        self.client.post(
            f"/api/v1/lead-intelligence/companies/{company_id}/research",
            headers=self.headers
        )
    
    @task(2)
    def generate_outreach(self):
        company_id = fake.uuid4()
        channels = ["email", "linkedin", "whatsapp"]
        self.client.post(
            f"/api/v1/lead-intelligence/companies/{company_id}/outreach",
            params={"channel": random.choice(channels)},
            headers=self.headers
        )
    
    @task(1)
    def list_search_profiles(self):
        self.client.get(
            "/api/v1/lead-intelligence/profiles",
            headers=self.headers
        )


class WhatsAppUser(HttpUser):
    wait_time = between(2, 5)
    
    def on_start(self):
        self.headers = {
            "Authorization": "Bearer test-token",
            "Content-Type": "application/json"
        }
    
    @task(5)
    def send_text_message(self):
        self.client.post(
            "/api/v1/whatsapp/messages",
            json={
                "to": fake.phone_number(),
                "message": "Test message from Load Tester",
                "message_type": "text"
            },
            headers=self.headers
        )
    
    @task(2)
    def send_template_message(self):
        self.client.post(
            "/api/v1/whatsapp/messages",
            json={
                "to": fake.phone_number(),
                "template_name": "welcome_template",
                "language": "en"
            },
            headers=self.headers
        )
    
    @task(1)
    def list_templates(self):
        self.client.get(
            "/api/v1/whatsapp/templates",
            headers=self.headers
        )


class APIGatewayUser(HttpUser):
    wait_time = between(1, 2)
    
    def on_start(self):
        self.headers = {
            "Authorization": "Bearer test-token",
            "Content-Type": "application/json"
        }
    
    @task(20)
    def get_dashboard_metrics(self):
        self.client.get(
            "/api/v1/analytics/kpis",
            headers=self.headers
        )
    
    @task(10)
    def get_conversations(self):
        self.client.get(
            "/api/v1/conversations",
            headers=self.headers
        )
    
    @task(5)
    def get_customers(self):
        self.client.get(
            "/api/v1/customers",
            headers=self.headers
        )
    
    @task(3)
    def search_documents(self):
        self.client.get(
            "/api/v1/search/search?q=test&size=10",
            headers=self.headers
        )


class AuthUser(HttpUser):
    wait_time = between(5, 10)
    
    @task(1)
    def login(self):
        self.client.post(
            "/api/v1/auth/login",
            json={
                "email": fake.email(),
                "password": "TestPassword123!"
            }
        )


@events.test_start.add_listener
def on_test_start(environment, **kwargs):
    print("Starting Load Test for SalesGenie API")


@events.test_stop.add_listener
def on_test_stop(environment, **kwargs):
    print("Load Test Completed")
    print(f"Total requests: {environment.stats.total.num_requests}")
    print(f"Failures: {environment.stats.total.num_failures}")