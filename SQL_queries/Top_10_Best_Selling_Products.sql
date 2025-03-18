/*
Top 10 Best-Selling Products
This aggregation identifies the most popular products by sales quantity.
*/


SELECT TOP 10
    p.description AS product_name, 
    SUM(f.quantity) AS total_quantity_sold
FROM fact_sales f
inner JOIN dim_product p 
	ON f.product_id = p.product_id
GROUP BY p.description
ORDER BY total_quantity_sold DESC;