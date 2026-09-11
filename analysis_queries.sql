USE sales_analytics;


-- =====================================================
-- 1. TOTAL SALES
-- =====================================================

SELECT
    ROUND(SUM(sales), 2) AS total_sales
FROM sales_data;


-- =====================================================
-- 2. TOTAL PROFIT
-- =====================================================

SELECT
    ROUND(SUM(profit), 2) AS total_profit
FROM sales_data;


-- =====================================================
-- 3. TOTAL ORDERS
-- =====================================================

SELECT
    COUNT(DISTINCT order_id) AS total_orders
FROM sales_data;


-- =====================================================
-- 4. TOTAL CUSTOMERS
-- =====================================================

SELECT
    COUNT(DISTINCT customer_id) AS total_customers
FROM sales_data;


-- =====================================================
-- 5. TOTAL QUANTITY SOLD
-- =====================================================

SELECT
    SUM(quantity) AS total_quantity
FROM sales_data;


-- =====================================================
-- 6. AVERAGE ORDER VALUE
-- =====================================================

SELECT
    ROUND(
        SUM(sales) / COUNT(DISTINCT order_id),
        2
    ) AS average_order_value
FROM sales_data;


-- =====================================================
-- 7. MONTHLY SALES
-- =====================================================

SELECT
    year,
    month,
    month_name,
    ROUND(SUM(sales), 2) AS monthly_sales
FROM sales_data
GROUP BY
    year,
    month,
    month_name
ORDER BY
    year,
    month;


-- =====================================================
-- 8. MONTHLY PROFIT
-- =====================================================

SELECT
    year,
    month,
    month_name,
    ROUND(SUM(profit), 2) AS monthly_profit
FROM sales_data
GROUP BY
    year,
    month,
    month_name
ORDER BY
    year,
    month;


-- =====================================================
-- 9. CATEGORY-WISE SALES
-- =====================================================

SELECT
    category,
    ROUND(SUM(sales), 2) AS total_sales
FROM sales_data
GROUP BY category
ORDER BY total_sales DESC;


-- =====================================================
-- 10. CATEGORY-WISE PROFIT
-- =====================================================

SELECT
    category,
    ROUND(SUM(profit), 2) AS total_profit
FROM sales_data
GROUP BY category
ORDER BY total_profit DESC;


-- =====================================================
-- 11. SUB-CATEGORY ANALYSIS
-- =====================================================

SELECT
    sub_category,
    ROUND(SUM(sales), 2) AS total_sales,
    ROUND(SUM(profit), 2) AS total_profit
FROM sales_data
GROUP BY sub_category
ORDER BY total_sales DESC;


-- =====================================================
-- 12. TOP 10 PRODUCTS BY SALES
-- =====================================================

SELECT
    product_name,
    ROUND(SUM(sales), 2) AS total_sales
FROM sales_data
GROUP BY product_name
ORDER BY total_sales DESC
LIMIT 10;


-- =====================================================
-- 13. TOP 10 PRODUCTS BY PROFIT
-- =====================================================

SELECT
    product_name,
    ROUND(SUM(profit), 2) AS total_profit
FROM sales_data
GROUP BY product_name
ORDER BY total_profit DESC
LIMIT 10;


-- =====================================================
-- 14. LOSS-MAKING PRODUCTS
-- =====================================================

SELECT
    product_name,
    ROUND(SUM(sales), 2) AS total_sales,
    ROUND(SUM(profit), 2) AS total_profit
FROM sales_data
GROUP BY product_name
HAVING SUM(profit) < 0
ORDER BY total_profit ASC
LIMIT 10;


-- =====================================================
-- 15. TOP 10 CUSTOMERS BY SALES
-- =====================================================

SELECT
    customer_id,
    customer_name,
    ROUND(SUM(sales), 2) AS total_sales
FROM sales_data
GROUP BY
    customer_id,
    customer_name
ORDER BY total_sales DESC
LIMIT 10;


-- =====================================================
-- 16. CUSTOMER SEGMENT ANALYSIS
-- =====================================================

SELECT
    segment,
    COUNT(DISTINCT customer_id) AS customers,
    ROUND(SUM(sales), 2) AS total_sales,
    ROUND(SUM(profit), 2) AS total_profit
FROM sales_data
GROUP BY segment
ORDER BY total_sales DESC;


-- =====================================================
-- 17. REGION-WISE SALES
-- =====================================================

SELECT
    region,
    ROUND(SUM(sales), 2) AS total_sales,
    ROUND(SUM(profit), 2) AS total_profit
FROM sales_data
GROUP BY region
ORDER BY total_sales DESC;


-- =====================================================
-- 18. STATE-WISE SALES
-- =====================================================

SELECT
    state,
    ROUND(SUM(sales), 2) AS total_sales,
    ROUND(SUM(profit), 2) AS total_profit
FROM sales_data
GROUP BY state
ORDER BY total_sales DESC;


-- =====================================================
-- 19. CITY-WISE SALES
-- =====================================================

SELECT
    city,
    ROUND(SUM(sales), 2) AS total_sales
FROM sales_data
GROUP BY city
ORDER BY total_sales DESC
LIMIT 20;


-- =====================================================
-- 20. SHIP MODE ANALYSIS
-- =====================================================

SELECT
    ship_mode,
    COUNT(DISTINCT order_id) AS total_orders,
    ROUND(SUM(sales), 2) AS total_sales,
    ROUND(SUM(profit), 2) AS total_profit
FROM sales_data
GROUP BY ship_mode
ORDER BY total_sales DESC;


-- =====================================================
-- 21. YEAR-WISE SALES
-- =====================================================

SELECT
    year,
    ROUND(SUM(sales), 2) AS total_sales,
    ROUND(SUM(profit), 2) AS total_profit
FROM sales_data
GROUP BY year
ORDER BY year;


-- =====================================================
-- 22. DISCOUNT VS PROFIT
-- =====================================================

SELECT
    discount,
    ROUND(SUM(sales), 2) AS total_sales,
    ROUND(SUM(profit), 2) AS total_profit
FROM sales_data
GROUP BY discount
ORDER BY discount;


-- =====================================================
-- 23. PROFIT MARGIN BY CATEGORY
-- =====================================================

SELECT
    category,
    ROUND(
        SUM(profit) / NULLIF(SUM(sales), 0) * 100,
        2
    ) AS profit_margin_percentage
FROM sales_data
GROUP BY category
ORDER BY profit_margin_percentage DESC;


-- =====================================================
-- 24. MOST PROFITABLE SUB-CATEGORIES
-- =====================================================

SELECT
    sub_category,
    ROUND(SUM(profit), 2) AS total_profit
FROM sales_data
GROUP BY sub_category
ORDER BY total_profit DESC
LIMIT 10;


-- =====================================================
-- 25. OVERALL BUSINESS SUMMARY
-- =====================================================

SELECT
    ROUND(SUM(sales), 2) AS total_sales,
    ROUND(SUM(profit), 2) AS total_profit,
    COUNT(DISTINCT order_id) AS total_orders,
    COUNT(DISTINCT customer_id) AS total_customers,
    SUM(quantity) AS total_quantity,
    ROUND(
        SUM(sales) / COUNT(DISTINCT order_id),
        2
    ) AS average_order_value
FROM sales_data;