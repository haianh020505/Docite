"""app/repositories — Database access layer.

All queries go here. Every public function that reads or writes tenant data
MUST take `organization_id: uuid.UUID` as a REQUIRED parameter with no default.
The organization_id MUST come only from the authenticated session (deps.py).
Must NOT import FastAPI, services, or AI packages.
"""
