# PRODUCT BRIEF: Multi-tenant Document QA System (web app)

## WHAT IT IS
A SaaS-style web app where each organization (tenant) uploads its own PDF
documents and asks questions about them in a chat interface. An AI answers
using only that organization's documents and cites its sources (document
name + page). Data of one organization must never be visible to another.

## USERS & ROLES
- Admin (per organization): uploads/deletes documents, sees storage usage,
  can also chat.
- Member: can only chat and view their own chat history.

## CORE SCREENS
1. Auth: login; register a new organization (organization name, admin email,
   password).
2. Documents (admin only): upload area (drag & drop, PDF only), document
   table (name, size, upload date, status), delete action, and a quota
   indicator (e.g. "7/20 documents, 64 MB / 200 MB").
   Status values: Processing / Ready / Failed.
3. Chat: left sidebar with chat sessions (new chat, history); main area with
   message thread; input box; each AI answer shows source citations (document
   name + page) as small chips that can be expanded; loading state while the
   answer is generated.
4. Organization members list (optional, simple).

## KEY STATES TO DESIGN
- Empty states (no documents yet, no chats yet)
- Upload in progress / processing / failed
- Quota exceeded error (file too large, too many documents, storage full)
- Session expired -> back to login
- Answer with no relevant source found

## DESIGN DIRECTION
- Clean, professional B2B tool; calm colors; light mode (dark mode optional)
- Desktop-first, responsive
- UI language: Vietnamese
- Tech: React + Tailwind CSS
- Runs directly on the developer's machine (Python virtualenv + PostgreSQL +
  Node); no Docker / containerization

## OUT OF SCOPE
Billing, super-admin dashboard, multi-language UI, Docker / containerization.