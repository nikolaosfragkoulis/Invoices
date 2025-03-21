use InvoiceDWH
Go

/* -----------------------------------------------------
   Total Revenue per Month
   -----------------------------------------------------
   This query calculates total revenue per year and month, 
   allowing us to analyze revenue trends over time.
   -----------------------------------------------------
*/


SELECT 
    d.year, 
    d.month, 
    SUM(f.price * f.quantity) AS total_revenue
FROM dbo.fact_sales f
inner JOIN dbo.dim_date d
	ON f.date_id = d.date_id
GROUP BY d.year
		,d.month
ORDER BY d.year
		,d.month;