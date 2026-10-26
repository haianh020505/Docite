# apps/api/app/workers — Background Jobs

Async jobs triggered after API operations (e.g. document upload).

**Belongs here:** Long-running or async background tasks (ingest pipeline, email delivery, etc.).
**Must NOT go here:** HTTP handlers, direct user responses, or sync-blocking operations without an async wrapper.
