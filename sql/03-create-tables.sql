CREATE TABLE IF NOT EXISTS genie_mcp_demo.analytics.customers (
  customer_id BIGINT,
  customer_name STRING,
  region STRING
)
USING DELTA;

CREATE TABLE IF NOT EXISTS genie_mcp_demo.analytics.orders (
  order_id BIGINT,
  customer_id BIGINT,
  order_date DATE,
  amount DECIMAL(18,2)
)
USING DELTA;
