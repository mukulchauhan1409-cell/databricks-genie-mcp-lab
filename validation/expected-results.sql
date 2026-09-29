-- Expected results for the controlled demo dataset.
-- These queries provide independent values to compare with Genie responses.

SELECT SUM(amount) AS total_revenue
FROM genie_mcp_demo.analytics.orders;
-- Expected: 22500.00

SELECT c.region, SUM(o.amount) AS total_revenue
FROM genie_mcp_demo.analytics.orders o
JOIN genie_mcp_demo.analytics.customers c
  ON o.customer_id = c.customer_id
GROUP BY c.region
ORDER BY total_revenue DESC;
-- Expected: South 10300.00, North 8000.00, West 4200.00

SELECT c.customer_name, SUM(o.amount) AS total_revenue
FROM genie_mcp_demo.analytics.orders o
JOIN genie_mcp_demo.analytics.customers c
  ON o.customer_id = c.customer_id
GROUP BY c.customer_name
ORDER BY total_revenue DESC;
-- Expected top customer: Customer B, 10300.00

SELECT order_id, amount
FROM genie_mcp_demo.analytics.orders
ORDER BY amount DESC
LIMIT 3;
-- Expected: 1002 7500.00, 1001 5000.00, 1004 4200.00
