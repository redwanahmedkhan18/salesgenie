# Search Service

Full-text search across knowledge base, customers, tickets, and conversations for the SalesGenie platform.

## Overview

The Search Service provides:

- **Full-Text Search** - Search across all indexed content
- **Document Indexing** - Index documents for search
- **Bulk Indexing** - Index multiple documents at once
- **Index Management** - Statistics, settings, and rebuild operations
- **Faceted Search** - Filter by index type, tags, and metadata

## API Endpoints

### Search
- `POST /api/v1/search/search` - Full-text search
- `GET /api/v1/search/search?q=query` - Search via GET

### Indexing
- `POST /api/v1/search/index` - Index a document
- `POST /api/v1/search/index/bulk` - Bulk index documents
- `DELETE /api/v1/search/index/{document_id}` - Delete from index

### Index Management
- `GET /api/v1/search/index/stats` - Get index statistics
- `GET /api/v1/search/index/settings` - Get index settings
- `POST /api/v1/search/index/rebuild` - Rebuild index

## Running Locally

```bash
pip install -r ../../requirements.txt
cp .env.example .env
cd migrations && alembic upgrade head
python main.py
```

## Testing

```bash
pytest tests/ -v
```