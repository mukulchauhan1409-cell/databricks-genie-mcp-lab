# Databricks Genie + MCP Lab

A hands-on learning and architecture exploration project for understanding how Databricks Genie, Model Context Protocol (MCP), and Unity Catalog can work together to provide governed access to enterprise data.

## Project status

Status: Learning and architecture exploration

The repository currently contains the architecture, documentation, reproducible demo dataset, SQL setup, and Databricks preparation notebook. The actual Genie + MCP runtime path remains a validation step and will only be marked as tested after a hands-on run.

## Architecture

![Databricks Genie + MCP architecture](architecture/genie-mcp-architecture.svg)

AI Client / Agent -> MCP -> Genie One MCP -> Databricks Genie -> governed data through Unity Catalog

## What this project covers

- What Model Context Protocol (MCP) is
- How Genie One MCP connects AI clients and Databricks Genie
- How business context affects natural-language analytics
- How Unity Catalog governance fits into the request path
- Sample analytical questions and data
- Reproducible Databricks SQL setup for the demo dataset
- A Databricks preparation notebook
- Lessons learned and implementation considerations

## Repository structure

```text
databricks-genie-mcp-lab/
├── architecture/
│   └── genie-mcp-architecture.svg
├── docs/
│   ├── 01-what-is-mcp.md
│   ├── 02-genie-one-mcp.md
│   ├── 03-unity-catalog-governance.md
│   └── 04-end-to-end-flow.md
├── examples/
│   ├── sample-business-questions.md
│   └── sample-mcp-flow.md
├── notebooks/
│   └── 01-genie-data-preparation.py
├── sql/
│   ├── 01-create-catalog.sql
│   ├── 02-create-schema.sql
│   ├── 03-create-tables.sql
│   └── 04-sample-data.sql
└── README.md
```

## Example business questions

- What is the total revenue by region?
- Which customers generated the most revenue?
- What were the top five orders this month?
- How did revenue change over time?

## Validation plan

## Hands-on Validation

Status: COMPLETE

The Genie One MCP integration has been successfully validated end-to-end using a Python MCP client.

### Validation Flow

Python MCP Client
-> Databricks OAuth
-> system.ai.genie_one_mcp
-> Genie One
-> Genie MCP Revenue Analytics
-> Unity Catalog
-> genie_poll_response
-> Completed Business Answer

### Validated Questions

1. Which customer generated the most revenue?
   - Result: Customer B
   - Revenue: $10,300

2. What are the top 3 orders by amount?
   - Order 1002: $7,500
   - Order 1001: $5,000
   - Order 1004: $4,200

3. What is the total revenue by region?
   - South: $10,300
   - North: $8,000
   - West: $4,200
   - Total: $22,500

All three MCP requests completed successfully.

Detailed validation results:
[Hands-on Validation](docs/05-hands-on-validation.md)

## Key learning

Connecting an AI client to enterprise data is not only an integration problem. The data needs business context, and access needs to remain governed.

This project treats the architecture as three related concerns:

1. Interaction: MCP provides a standardized way for clients and AI agents to interact with tools.
2. Data understanding: Genie provides a conversational analytics layer and business context.
3. Governance: Unity Catalog provides the enterprise data governance layer.

## Official references

- Databricks September 2026 release notes: https://docs.databricks.com/aws/en/release-notes/product/2026/september
- Databricks Genie: https://docs.databricks.com/aws/en/genie/
- Databricks MCP documentation: https://docs.databricks.com/aws/en/generative-ai/mcp/
- Unity Catalog: https://docs.databricks.com/aws/en/data-governance/unity-catalog/

## Notes

This project is intended for learning, experimentation, and knowledge sharing. Release-specific capabilities should be verified against current Databricks documentation before production use.

## License

MIT
