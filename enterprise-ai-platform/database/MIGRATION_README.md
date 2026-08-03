# SalesGenie Database Migration System

## Overview

Implemented a complete Alembic-style database migration system for PostgreSQL with enterprise-grade security and scalability features.

## Files Created

| File | Size | Purpose |
|------|------|---------|
| `migrate.py` | 7.2KB | Migration manager CLI |
| `schema.sql` | 6.7KB | Main database schema |
| `indexes.sql` | 1.6KB | Performance indexes |
| `migrations/env.py` | 50B | Alembic environment |
| `migrations/versions/base_20260803.py` | 9.3KB | Base schema migration |
| `migrations/versions/add_security_monitoring_20260803.py` | 1.2KB | Security columns |

## Usage

```bash
# Check migration status
python3 migrate.py status

# Run migrations
python3 migrate.py upgrade

# Rollback to specific version
python3 migrate.py downgrade base_20260803

# Create new migration
python3 migrate.py create add_conversations_table

# Run SQL file directly
python3 migrate.py run custom_migration.sql
```

## Base Schema Tables

1. **organizations** - Tenant management
2. **users** - User accounts with MFA, risk scoring
3. **api_keys** - API key tracking with scopes
4. **sessions** - Session management with device tracking
5. **audit_logs** - Complete audit trail
6. **security_events** - Security incident tracking
7. **secrets** - Secure secret storage
8. **security_settings** - Organization settings

## Security Features

- UUID primary keys for security
- Soft delete with `deleted_at`
- Risk scoring on users and sessions
- MFA support with secrets
- IP reputation tracking
- Device fingerprint validation

## Performance Features

- Indexes on all foreign keys
- Composite indexes for common queries
- Partial indexes for active data
- Full-text search index
- BRIN index for time-series audit logs

## Migration Commands

```bash
cd enterprise-ai-platform/database

# Using env vars
export DATABASE_URL="postgresql://user:pass@localhost/salesgenie"

# Upgrade database
python3 migrate.py upgrade

# Get status
python3 migrate.py status
```

## Security Columns Added

- `security_score` on organizations
- `risk_score` on users and sessions
- `last_password_change_at` on users
- `ip_reputation` on audit logs
- Detailed audit fields

## Next Steps

1. Apply schema: `psql -f schema.sql`
2. Apply indexes: `psql -f indexes.sql`
3. Run migrations through the manager