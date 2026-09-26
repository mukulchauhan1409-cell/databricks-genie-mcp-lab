# Databricks notebook source
# Genie + MCP learning lab
#
# This notebook prepares the small demo dataset used by the repository.

# COMMAND ----------

spark.sql("""
CREATE SCHEMA IF NOT EXISTS genie_mcp_demo.analytics
""")

spark.sql("""
CREATE TABLE IF NOT EXISTS genie_mcp_demo.analytics.customers (
  customer_id BIGINT,
  customer_name STRING,
  region STRING
)
USING DELTA
""")

spark.sql("""
CREATE TABLE IF NOT EXISTS genie_mcp_demo.analytics.orders (
  order_id BIGINT,
  customer_id BIGINT,
  order_date DATE,
  amount DECIMAL(18,2)
)
USING DELTA
""")

customers = [
    (101, "Customer A", "North"),
    (102, "Customer B", "South"),
    (103, "Customer C", "West"),
]

orders = [
    (1001, 101, "2026-09-01", 5000.00),
    (1002, 102, "2026-09-02", 7500.00),
    (1003, 101, "2026-09-05", 3000.00),
    (1004, 103, "2026-09-07", 4200.00),
    (1005, 102, "2026-09-10", 2800.00),
]

customers_df = spark.createDataFrame(customers, ["customer_id", "customer_name", "region"])
orders_df = spark.createDataFrame(orders, ["order_id", "customer_id", "order_date", "amount"])

customers_df.write.mode("overwrite").saveAsTable("genie_mcp_demo.analytics.customers")
orders_df.write.mode("overwrite").saveAsTable("genie_mcp_demo.analytics.orders")

display(
    spark.sql("""
    SELECT c.region, SUM(o.amount) AS total_revenue
    FROM genie_mcp_demo.analytics.orders o
    JOIN genie_mcp_demo.analytics.customers c
      ON o.customer_id = c.customer_id
    GROUP BY c.region
    ORDER BY total_revenue DESC
    """)
)
