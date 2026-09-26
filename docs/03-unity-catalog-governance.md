# Unity Catalog and Governance

A governed AI-data architecture needs access controls in addition to an interaction protocol.

The conceptual request path is:

AI request
  |
  v
MCP
  |
  v
Genie
  |
  v
Unity Catalog governance
  |
  v
Authorized data

## Governance questions

When an AI client asks for data, the design should consider:

- Which identity is making the request?
- Which catalogs and schemas can that identity use?
- Which tables or views are accessible?
- Which operations are allowed?
- Are sensitive columns protected appropriately?
- How can access be audited?

The goal is to let AI work with data through the same governed platform rather than creating an uncontrolled copy of the data or credentials.

Always verify exact authorization behavior against current Databricks documentation for the configured product and deployment model.
