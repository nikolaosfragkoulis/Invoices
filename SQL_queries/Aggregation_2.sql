use InvoiceDWH
Go

/* -----------------------------------------------------
   Top 10 Best-Selling Products
   -----------------------------------------------------
   This query retrieves the top 10 best-selling products 
   based on total quantity sold.
   -----------------------------------------------------
*/


SELECT TOP 10
    p.description AS product_name, 
    SUM(f.quantity) AS total_quantity_sold
FROM dbo.fact_sales f
inner JOIN dbo.dim_product p 
	ON f.product_id = p.product_id
GROUP BY p.description
ORDER BY total_quantity_sold DESC;