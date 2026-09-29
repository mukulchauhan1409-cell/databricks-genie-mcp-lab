# Genie One MCP

Databricks provides Genie One MCP as a Databricks-provided MCP Service that exposes Genie as a conversational analytics tool over the Model Context Protocol.

The current GA service is `system.ai.genie_one_mcp`, available through Unity Gateway. The previous Beta endpoint `/api/2.0/mcp/genie` is deprecated and is scheduled to sunset on October 31, 2026.

## Why it is interesting

A natural-language question can be handled through a conversational analytics layer while keeping enterprise data governance in the architecture.

Conceptually:

AI Client
  |
  v
MCP
  |
  v
Genie
  |
  +--> Business context
  |
  v
Governed Databricks data

## Hands-on validation

This repository now includes a Python MCP validation client under `client/`. The client uses the local Databricks CLI OAuth profile, calls `genie_ask`, polls with `genie_poll_response`, and prints the completed analytical answer.

The repository's validation used the current `system.ai.genie_one_mcp` service. `genie_get_query_result` was separately investigated but is documented as not validated for the tested SDK response because the completed response exposed no usable `query_items` value.
