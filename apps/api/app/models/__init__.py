"""app/models — SQLAlchemy ORM models.

One file per domain entity. Every table that stores tenant data MUST
include an `organization_id` foreign key column as a non-nullable field.
Must NOT go here: business logic, Pydantic schemas, queries.
"""
