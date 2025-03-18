/*Revenue by Country
This aggregation provides insights into which countries generate the most revenue.
*/


SELECT 
    c.country_name, 
    SUM(f.price * f.quantity) AS total_revenue
FROM fact_sales f
INNER JOIN dim_customer cu 
	ON f.customer_id = cu.customer_id
INNER JOIN dim_country c
	ON f.country_id = c.country_id
GROUP BY c.country_name
ORDER BY total_revenue DESC;