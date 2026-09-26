# End-to-End Flow

This document describes the conceptual flow used in the lab.

## 1. User asks a business question

Example:

What is the total revenue by region?

## 2. AI client sends a request through MCP

The client uses the MCP interface to reach the available capability.

## 3. Genie handles the analytics request

Genie can use the available data context and semantic definitions to interpret the request.

## 4. Governance is applied

The request operates within the Databricks data governance model.

## 5. Data is queried

The underlying tables contain the demo customer and order data.

## 6. Result is returned

The result is presented to the user in a conversational analytics experience.

The purpose of the flow is to make each layer explicit instead of treating AI querying data as a single black box.
