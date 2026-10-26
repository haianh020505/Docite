// apps/web/src/config/limits.ts
// Application-level limits and constants shared across features.
// No secrets here — only non-sensitive config.

export const LIMITS = {
  maxFileSizeMb: 50,
  maxFilesPerUpload: 10,
  maxDocumentsPerOrg: 500,
  maxMembersPerOrg: 100,
  chatMessageMaxLength: 2000,
} as const;
