# apps/web/src/config — Frontend Configuration

App-level constants (limits, feature flags, URLs). No secrets.

**Belongs here:** `limits.ts` and other non-secret constants.
**Must NOT go here:** API keys, secrets, or runtime environment values (use `import.meta.env` for those).
