# infra — Infrastructure Configuration

**Belongs here:** Environment templates, nginx config, CI/CD config.
**Must NOT go here:** Application code, secrets, or production environment values.

## Database Setup (PostgreSQL native)

Cài PostgreSQL 16 và extension pgvector trực tiếp trên máy:

### 1. Cài PostgreSQL 16

- Windows: tải từ https://www.postgresql.org/download/windows/
- Sau khi cài, đảm bảo `psql` có trong PATH.

### 2. Cài pgvector extension

```powershell
# Clone và build pgvector (hoặc dùng installer từ https://github.com/pgvector/pgvector)
# Với Windows + pgAdmin, có thể cài qua Stack Builder
```

### 3. Tạo database

```sql
-- Chạy trong psql hoặc pgAdmin:
CREATE USER docite WITH PASSWORD 'docite';
CREATE DATABASE docite OWNER docite;
\c docite
CREATE EXTENSION IF NOT EXISTS vector;
```

### 4. Cấu hình connection string

Trong `apps/api/.env`:
```
DATABASE_URL=postgresql+asyncpg://docite:docite@localhost:5432/docite
```
