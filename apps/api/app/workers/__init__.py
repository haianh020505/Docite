"""app/workers — Background job definitions.

Workers are triggered by the API layer (e.g. after a document upload).
They import services and docite_ai but never respond to HTTP directly.
"""
