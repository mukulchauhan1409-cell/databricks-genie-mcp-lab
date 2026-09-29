# Hands-on Validation: Genie One MCP

## Status

Hands-on validation: COMPLETE

Validation date: September 29, 2026

## Objective

Validate the end-to-end integration between a Python MCP client, Databricks Genie One MCP, Genie, and governed Unity Catalog data.

The objective was to confirm that natural-language business questions can be sent through MCP and that Genie can return analytical results from the configured data.

## Environment

- Databricks Free Edition workspace
- Databricks CLI 1.18.0
- Python 3.11.5
- MCP Python SDK 2.2.0
- Databricks Genie One
- Unity Catalog
- Genie One MCP service
- Python MCP client using Streamable HTTP

## Demo Data

Catalog:

`genie_mcp_demo`

Schema:

`analytics`

Tables:

- `genie_mcp_demo.analytics.customers`
- `genie_mcp_demo.analytics.orders`

### Customers

| customer_id | customer_name | region |
| --- | --- | --- |
| 101 | Customer A | North |
| 102 | Customer B | South |
| 103 | Customer C | West |

### Orders

| order_id | customer_id | order_date | amount |
| --- | --- | --- | ---: |
| 1001 | 101 | 2026-09-01 | 5000.00 |
| 1002 | 102 | 2026-09-02 | 7500.00 |
| 1003 | 101 | 2026-09-05 | 3000.00 |
| 1004 | 103 | 2026-09-07 | 4200.00 |
| 1005 | 102 | 2026-09-10 | 2800.00 |

## Genie Configuration

Genie Space:

`Genie MCP Revenue Analytics`

Business context defined:

- customers contains customer master information.
- customer_id uniquely identifies a customer.
- orders contains individual customer orders.
- order_id uniquely identifies an order.
- orders.customer_id joins to customers.customer_id.
- orders.amount represents revenue.
- Revenue is calculated as SUM(orders.amount).
- Revenue by region is calculated by joining orders to customers and grouping by customers.region.

## MCP Endpoint

The validation used the Databricks-provided Genie One MCP service:

`https://<workspace-hostname>/ai-gateway/mcp-services/system.ai.genie_one_mcp`

The MCP client authenticated using the existing Databricks CLI OAuth profile.

No access token was hardcoded in the source code.

## MCP Request Flow

The Python client performs the following sequence:

```text
Python MCP Client
        |
        | OAuth
        v
Databricks Authentication
        |
        v
system.ai.genie_one_mcp
        |
        | genie_ask
        v
Genie One
        |
        v
Genie MCP Revenue Analytics
        |
        v
Unity Catalog
        |
        +-- customers
        |
        +-- orders
        |
        v
Business Query
        |
        v
genie_poll_response
        |
        v
Completed Response
        |
        v
Python MCP Client
