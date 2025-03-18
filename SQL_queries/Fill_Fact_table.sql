INSERT INTO fact_sales (
						invoice_id
						,customer_id
						,product_id
						,date_id
						,country_id
						,quantity
						,price
						)


SELECT f.[INVOICE]
		,c.[CUSTOMER_ID]
		,p.[PRODUCT_ID]
		,d.[DATE_ID]
		,cntry.[COUNTRY_ID]
		,f.[QUANTITY]
		,f.[PRICE]
FROM [dbo].[raw_data] as  f
INNER JOIN dbo.dim_date d 
	ON d.invoice_date = CAST(f.date AS DATE)
inner join [dbo].[DIM_COUNTRY] cntry
	on cntry.[COUNTRY_NAME] = f.[COUNTRY]
INNER JOIN [dbo].dim_customer c 
	ON c.customer = f.customer
LEFT JOIN [dbo].dim_product p 
	ON p.STOCKCODE = f.PRODUCT
where PRICE >0.00