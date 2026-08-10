# Production Deployment Checklist & Release Procedures

## Release-Blocking Issues (Must be fixed before any release)

| Priority | Issue | Status |
|----------|-------|--------|
| CRITICAL | Hardcoded `POSTGRES_PASSWORD` default in `common/config.py` → **FIXED** (set to `None`, validated in production) | Fixed |
| CRITICAL | Hardcoded `JWT_SECRET_KEY` default → **FIXED** (set to `None`, validated in production) | Fixed |
| CRITICAL | Hardcoded `KEYCLOAK_CLIENT_SECRET` / `KEYCLOAK_ADMIN_PASSWORD` defaults → **FIXED** (set to `None`) | Fixed |
| CRITICAL | Hardcoded `SALESGENIE_SUPER_ADMIN_PASSWORD` default → **FIXED** (set to `None`, `exclude=True`) | Fixed |
| CRITICAL | `POSTGRES_PASSWORD` included in logs → **FIXED** (`exclude=True` on sensitive fields) | Fixed |
| HIGH | No CI/CD pipeline (`.github/workflows/` was empty) → **FIXED** (created `ci-cd.yml` with lint, test, security, build, scan, deploy stages) | Fixed |
| HIGH | No pinned dependencies (`requirements.txt` uses `>=` only) → **FIXED** (created `requirements.lock` with pinned versions) | Fixed |
| HIGH | Dockerfiles use unpinned `python:3.12-slim` → **FIXED** (pinned to digest in lock file) | Fixed |
| HIGH | Docker images use `latest` tag in K8s manifests → **FIXED** (changed to `v1.0.0`) | Fixed |
| HIGH | No container vulnerability scanning in CI → **FIXED** (added Trivy scan in CI pipeline) | Fixed |
| HIGH | No linting/typecheck in CI → **FIXED** (added ruff and mypy stages) | Fixed |
| HIGH | K8s readiness/liveness probe paths mismatch (`/health` vs `/health/live`) → **FIXED** | Fixed |
| HIGH | No staging deployment in CI → **FIXED** (added `deploy-staging` job with health checks) | Fixed |
| HIGH | No production health checks post-deploy → **FIXED** (kubectl wait for available/ready) | Fixed |
| HIGH | `.env.redis` and `.env.services` tracked in git → **FIXED** (removed from tracking, added to .gitignore) | Fixed |
| HIGH | No environment-specific config (staging vs prod) → **FIXED** (created `values-staging.yaml` and `values-production.yaml`) | Fixed |
| HIGH | No zero-downtime deployment strategy → **FIXED** (added RollingUpdate with maxSurge:1, maxUnavailable:0 + preStop hook) | Fixed |
| MEDIUM | Dockerfiles not multi-stage → Acceptable (single stage with `--no-cache-dir`, small image) | OK |
| MEDIUM | Helm `chart` directory under `charts/` not a proper subchart → **DOCUMENTED** | Documented |

## Production Deployment Checklist

### Pre-Deployment
- [ ] **Code review**: All changes reviewed by at least 1 engineer
- [ ] **Tests pass**: Unit and integration tests pass in CI
- [ ] **Lint**: `ruff check` passes with no errors
- [ ] **Type check**: `mypy` passes (or acceptable baseline)
- [ ] **Security scan**: Trivy container scan passes (no CRITICAL/HIGH vulns)
- [ ] **Bandit**: SAST scan passes (no HIGH/CRITICAL findings)
- [ ] **Secrets**: No hardcoded secrets in code (gitleaks passes)
- [ ] **DB migrations**: Migration files reviewed for backward compatibility
- [ ] **Version bump**: Image tag updated from staging to production version

### Staging Deployment
- [ ] Deploy to `salesgenie-staging` namespace
- [ ] Verify all pods are `Running` and `Ready`
- [ ] Verify `/health/live` returns 200 on all services
- [ ] Verify `/health/ready` returns 200 on all services
- [ ] Verify `/metrics` endpoint accessible
- [ ] Run smoke tests against staging API
- [ ] Verify database migrations applied successfully
- [ ] Verify no errors in structured logs

### Production Deployment (Zero-Downtime Rolling Update)
- [ ] **Pre-deploy**: Verify staging is healthy
- [ ] **Pre-deploy**: Take database snapshot
- [ ] **Deploy**: `helm upgrade salesgenie ./helm/charts/salesgenie -f values-production.yaml`
- [ ] **Monitor**: Watch rollout status (`kubectl rollout status deployment/ai-gateway`)
- [ ] **Health checks**: Verify liveness/readiness probes pass
- [ ] **Smoke test**: Hit `/health/live` on all services
- [ ] **Metric check**: Verify no new error spikes in Prometheus
- [ ] **Wait**: Allow 10 minutes of monitoring post-deploy

### Post-Deployment
- [ ] **Canary**: Monitor first 5% of traffic for errors
- [ ] **Rollback window**: Keep rollback plan ready for 30 minutes post-deploy
- [ ] **Monitor**: Watch application logs, error rates, latency
- [ ] **Notify**: Inform team of successful deployment

## Rollback Procedures

### Docker Image Rollback
```bash
# Roll back to previous known-good image tag
kubectl set image deployment/ai-gateway \
  ai-gateway=ghcr.io/salesgenie/ai-gateway:<previous-good-tag> \
  -n salesgenie

# Or use kubectl rollout undo
kubectl rollout undo deployment/ai-gateway -n salesgenie

# Monitor the rollback
kubectl rollout status deployment/ai-gateway -n salesgenie
```

### Database Migration Rollback
```bash
# 1. Take a backup before any rollback
kubectl exec -it postgres-pod -n salesgenie -- \
  pg_dump -U salesgenie_admin salesgenie_db > backup-pre-rollback.sql

# 2. Check migration history
# Connect to DB and check alembic_version table

# 3. Apply downgrade migration
kubectl exec -it migration-job -n salesgenie -- \
  alembic downgrade -1
```

### Environment Variable Rollback
```bash
# 1. Check current config
kubectl describe configmap/salesgenie-config -n salesgenie

# 2. Revert ConfigMap to previous version
kubectl rollout undo configmap/salesgenie-config -n salesgenie

# 3. Force pod restart to pick up reverted config
kubectl rollout restart deployment/ai-gateway -n salesgenie
```

### Emergency Procedures

#### Emergency Rollback (Critical Production Issue)
```bash
# 1. Immediately stop new traffic
kubectl patch deployment ai-gateway -p '{"spec":{"replicas":0}}' -n salesgenie

# 2. Roll back to last known good version
kubectl rollout undo deployment/api-gateway -n salesgenie

# 3. Verify rollback
kubectl get pods -n salesgenie

# 4. Re-enable traffic (gradually)
kubectl patch deployment api-gateway -p '{"spec":{"replicas":3}}' -n salesgenie
kubectl rollout status deployment/api-gateway -n salesgenie
```

#### Emergency Database Restore
```bash
# 1. Restore from latest backup
kubectl apply -f deployment/kubernetes/manifests/db-restore-job.yaml

# 2. Monitor restore progress
kubectl logs -f job/db-restore -n salesgenie
```

#### Full Rollback Command Sequence
```bash
# 1. Capture current state
kubectl get all -n salesgenie > pre-rollback-state.txt

# 2. Rollback deployment
kubectl rollout undo deployment/api-gateway -n salesgenie
kubectl rollout undo deployment/ai-gateway -n salesgenie
# ... repeat for other services

# 3. Restart pods to pick up rolled-back image
kubectl rollout restart deployment/api-gateway -n salesgenie
kubectl rollout restart deployment/ai-gateway -n salesgenie

# 4. Wait for all deployments to be available
kubectl wait --for=condition=available deployment --all -n salesgenie --timeout=300s

# 5. Run health checks
for pod in $(kubectl get pods -n salesgenie -o name); do
  kubectl exec $pod -n salesgenie -- curl -sf http://localhost:8000/health/live
done
```

## Deployment Configuration

### Environment Separation
| Environment | Namespace | DB | Redis | Image Tag |
|-------------|-----------|-----|-------|-----------|
| Development | N/A (docker-compose) | localhost:5432 | localhost:6379 | `:dev` |
| Testing | N/A | service containers | service containers | `:test` |
| Staging | `salesgenie-staging` | RDS staging | ElastiCache staging | `:staging-latest` |
| Production | `salesgenie` | RDS prod (multi-AZ) | ElastiCache prod (cluster) | `:v1.0.0` |

### CI/CD Pipeline Stages
1. **lint** — ruff + mypy
2. **test** — unit + integration tests
3. **security** — Bandit + gitleaks + Trivy container scan
4. **build** — Docker build & push (multi-arch)
5. **container-scan** — Trivy vulnerability scan on built image
6. **deploy-staging** — Deploy to staging namespace + health checks
7. **deploy-production** — Deploy to production namespace + health checks
8. **performance** — Load tests
9. **notify** — Discord notification

### Required Environment Variables (Production)
```
POSTGRES_PASSWORD  # REQUIRED
JWT_SECRET_KEY      # REQUIRED
KEYCLOAK_CLIENT_SECRET  # REQUIRED
SALESGENIE_SUPER_ADMIN_PASSWORD  # REQUIRED
GROQ_API_KEY        # At least one LLM provider key
SENTRY_DSN          # For error tracking
```
