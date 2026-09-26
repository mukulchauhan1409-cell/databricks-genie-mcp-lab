# What is MCP?

Model Context Protocol (MCP) is a standardized way for an AI application to interact with external tools and data capabilities.

For this project, the useful mental model is:

AI Client -> MCP -> Tool or data capability

MCP can act as the interaction layer while the data platform remains responsible for identity, authorization, semantics, and data processing.

## In this project

AI Client
  |
  v
MCP
  |
  v
Databricks Genie
  |
  v
Unity Catalog
  |
  v
Enterprise Data

MCP is not a replacement for the data platform or its governance model. It is an interface through which an AI client can interact with capabilities.
