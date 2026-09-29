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

1. Create the demo catalog, schema, and Delta tables in a Databricks workspace.
2. Run the preparation notebook and verify the expected sample data.
3. Configure a Genie space using the demo tables and relevant business context.
4. Validate the business questions listed above directly in Genie.
5. Validate the Genie + MCP request path using a supported MCP client.
6. Capture observed behavior, limitations, and screenshots/results in the repository.
7. Only then change the project status from architecture exploration to hands-on validated.

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
