# Changelog

All notable project changes are documented here.

## 2026-09-29

### Added

- End-to-end Python MCP client validation using Databricks Genie One MCP.
- Controlled Genie demo dataset in Unity Catalog.
- Validation documentation covering customer revenue, top-N orders, and revenue by region.
- Hands-on evidence screenshots for Genie configuration, analytical output, and MCP client execution.
- MIT license and contribution guidelines.

### Documented

- Current Genie One MCP service endpoint: `system.ai.genie_one_mcp`.
- MCP request flow using `genie_ask` and `genie_poll_response`.
- `genie_get_query_result` as not validated because the tested completed response exposed `query_items` as null.
