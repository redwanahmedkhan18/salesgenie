# File Service

Manages file storage, uploads, downloads, and metadata for the SalesGenie platform.

## Overview

The File Service provides:

- **File Upload** - Upload files with metadata, tags, and visibility settings
- **Bulk Upload** - Upload multiple files at once
- **File Download** - Generate presigned download URLs
- **File Search** - Search files with rich filtering
- **File Management** - Update metadata, soft delete, version tracking
- **File Sharing** - Create shareable download links
- **Analytics** - Statistics by category, visibility, and storage usage

## API Endpoints

### Upload
- `POST /api/v1/files/upload` - Upload a single file
- `POST /api/v1/files/upload/bulk` - Bulk upload files

### Download & Access
- `GET /api/v1/files/{file_id}/download` - Get download URL
- `GET /api/v1/files/{file_id}/content` - Stream file content

### Search & Management
- `GET /api/v1/files` - Search files with filters
- `GET /api/v1/files/{file_id}` - Get file metadata
- `DELETE /api/v1/files/{file_id}` - Soft delete file
- `PATCH /api/v1/files/{file_id}` - Update file metadata

### Analytics
- `GET /api/v1/files/overview` - Get file overview statistics
- `GET /api/v1/files/stats/by-category` - Statistics by category

### Sharing
- `POST /api/v1/files/share` - Create share link
- `GET /api/v1/files/share/{share_id}` - Access shared file

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