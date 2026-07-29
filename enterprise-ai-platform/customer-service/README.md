# Customer Service

Customer profiles, segments, tags, notes, and purchase history management for the SalesGenie platform.

## Overview

The Customer Service manages all customer-related data including:

- **Customer Profiles** - Contact info, company, lead status, lead score
- **Segments** - Customer grouping for targeted campaigns
- **Tags** - Quick categorization labels
- **Notes** - Internal customer notes and interactions
- **Orders** - Purchase history tracking
- **Interaction Summaries** - AI-generated summaries of customer conversations

## API Endpoints

### Customers
- `POST /api/v1/customers` - Create a new customer
- `GET /api/v1/customers` - List customers (with filtering)
- `GET /api/v1/customers/{id}` - Get customer details with history
- `PATCH /api/v1/customers/{id}` - Update customer
- `DELETE /api/v1/customers/{id}` - Soft delete customer

### Segments
- `POST /api/v1/customers/segments` - Create a segment
- `GET /api/v1/customers/segments` - List all segments

### Tags
- `POST /api/v1/customers/tags` - Create a tag
- `GET /api/v1/customers/tags` - List all tags

### Notes
- `POST /api/v1/customers/notes` - Add a note to a customer

### Analytics
- `GET /api/v1/customers/analytics/overview` - Get customer analytics

## Filtering Options

- `lead_status` - Filter by lead status (cold, warm, hot, qualified, converted, churned)
- `segment_id` - Filter by segment membership
- `tag_id` - Filter by tag
- `search` - Search by name, email, or phone
- `limit` / `offset` - Pagination

## Running Locally

```bash
# Install dependencies
pip install -r ../../requirements.txt

# Set environment variables
cp .env.example .env
# Edit .env with your values

# Run migrations
cd migrations
alembic upgrade head

# Start the service
python main.py
```

## Docker

```bash
docker build -t salesgenie-customer-service .
docker run -p 8014:8014 --env-file .env salesgenie-customer-service
```

## Testing

```bash
# Unit tests
pytest tests/test_customer_models.py -v

# Integration tests
pytest tests/test_customer_integration.py -v

# All tests
pytest tests/ -v
```

## Database Schema

The service uses PostgreSQL with the following tables:

- `customers` - Customer profiles
- `customer_segments` - Segment definitions
- `customer_segment_members` - Segment membership (many-to-many)
- `customer_tags` - Tag definitions
- `customer_tag_members` - Tag membership (many-to-many)
- `customer_notes` - Internal notes
- `customer_orders` - Purchase history
- `customer_interaction_summaries` - AI-generated summaries

All tables use UUID primary keys and include tenant isolation via `tenant_id`.