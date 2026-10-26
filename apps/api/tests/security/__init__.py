"""tests/security — Cross-tenant isolation and authorization tests.

Required tests (see docs/tenancy-and-privacy.md):
  - Cross-tenant retrieval returns nothing
    (Org A's question never returns Org B's documents)
  - Forbidden role cannot call admin endpoints
    (member role cannot invite/remove members)
"""
