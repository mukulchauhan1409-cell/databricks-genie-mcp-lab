# Sample MCP Flow

This is a conceptual example, not a production protocol trace.

User question:

What is the total revenue by region?

Conceptual flow:

1. AI client receives the user question.
2. Client invokes the available Genie capability through MCP.
3. Genie interprets the business question using its configured context.
4. The request is evaluated within the Databricks governance model.
5. The underlying data is queried.
6. The analytical result is returned to the client.

The exact request and response payloads depend on the client and current Databricks implementation and should be taken from the relevant official documentation when implementing this for real.
