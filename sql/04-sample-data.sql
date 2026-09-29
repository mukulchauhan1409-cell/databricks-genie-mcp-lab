-- Load the controlled demo dataset.
-- This script is intentionally rerunnable for a clean validation state.

DELETE FROM genie_mcp_demo.analytics.orders;
DELETE FROM genie_mcp_demo.analytics.customers;

INSERT INTO genie_mcp_demo.analytics.customers VALUES
  (101, 'Customer A', 'North'),
  (102, 'Customer B', 'South'),
  (103, 'Customer C', 'West');

INSERT INTO genie_mcp_demo.analytics.orders VALUES
  (1001, 101, DATE '2026-09-01', 5000.00),
  (1002, 102, DATE '2026-09-02', 7500.00),
  (1003, 101, DATE '2026-09-05', 3000.00),
  (1004, 103, DATE '2026-09-07', 4200.00),
  (1005, 102, DATE '2026-09-10', 2800.00);
