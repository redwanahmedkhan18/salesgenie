# Product Intelligence Service

AI-powered market research, competitor analysis, and product launch strategy for the SalesGenie platform.

## Overview

The Product Intelligence Service helps businesses research markets, analyze competitors,
identify opportunities, and generate product launch strategies powered by AI.

## API Endpoints

### Research Projects
- `POST /api/v1/product-intelligence/projects` - Create research project
- `GET /api/v1/product-intelligence/projects` - List projects
- `GET /api/v1/product-intelligence/projects/{id}` - Get project details
- `PATCH /api/v1/product-intelligence/projects/{id}` - Update project
- `DELETE /api/v1/product-intelligence/projects/{id}` - Delete project

### Evidence
- `POST /api/v1/product-intelligence/evidence` - Add evidence item
- `GET /api/v1/product-intelligence/projects/{id}/evidence` - Get project evidence

### Competitors
- `POST /api/v1/product-intelligence/competitors` - Add competitor
- `GET /api/v1/product-intelligence/projects/{id}/competitors` - List competitors

### Analysis
- `GET /api/v1/product-intelligence/projects/{id}/opportunities` - Get market opportunities
- `GET /api/v1/product-intelligence/projects/{id}/strategy` - Get product strategy
- `POST /api/v1/product-intelligence/projects/{id}/analyze` - Trigger AI analysis
- `POST /api/v1/product-intelligence/analyze` - Quick one-off analysis

### Scenarios & Planning
- `POST /api/v1/product-intelligence/scenarios` - Create scenario model
- `GET /api/v1/product-intelligence/projects/{id}/scenarios` - List scenarios
- `GET /api/v1/product-intelligence/projects/{id}/launch-plan` - Get launch plan
- `GET /api/v1/product-intelligence/projects/{id}/report` - Get final report

## Running Locally

```bash
pip install -r ../../requirements.txt
cp .env.example .env
export PYTHONPATH=/path/to/enterprise-ai-platform
python3 -m uvicorn main:app --reload --port 8027
```

## Testing

```bash
pytest tests/ -v
```
