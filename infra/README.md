# infra — Infrastructure Configuration

**Belongs here:** docker-compose.yml, Dockerfiles, nginx config, environment templates.
**Must NOT go here:** Application code, secrets, or production environment values.

## Quick start (database only)
```powershell
cd infra
docker compose up db -d          # start PostgreSQL with pgvector
docker compose ps                # verify db is healthy
```
