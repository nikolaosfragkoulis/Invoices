USE [InvoiceDWH]
GO

/* -------------------------------
   Step 1: Exploring Data
--------------------------------- */

--select distinct country
--from [dbo].[raw_data]

--select count(*), country
--from [dbo].[raw_data]
--group by country
--order by 1 asc


--select distinct customer
--from [dbo].[raw_data]
--order by 1 desc

--select distinct cast([date] as date) as date
--from [dbo].[raw_data]
--order by 1 asc

/* -------------------------------
   Step 2: Populate DIM_COUNTRY Table
--------------------------------- */
INSERT INTO [dbo].[DIM_COUNTRY]
           ([COUNTRY_NAME])
select country
from [dbo].[raw_data]
group by country

GO

/* -------------------------------
   Step 3: Populate DIM_CUSTOMER Table
--------------------------------- */

INSERT INTO [dbo].[DIM_CUSTOMER]
           ([CUSTOMER])
select customer
from [dbo].[raw_data]
group by customer
GO

/* -------------------------------
   Step 4: Populate DIM_DATE Table
--------------------------------- */

INSERT INTO [dbo].[DIM_DATE]
           ([DATE_ID]
		   ,[INVOICE_DATE]
           ,[YEAR]
           ,[MONTH]
           ,[DAY]
           ,[WEEKDAY]
           ,[QUARTER])
select distinct replace(cast([date] as date), '-','') as date
				 ,cast([date] as date)as [INVOICE_DATE]
				,year([date]) as [YEAR]
				,month([date]) as [MONTH]
				,day([date]) as [DAY]
				,DATEPART(dw,[date])  as [WEEKDAY]
				,DATEPART(QUARTER, [date])  as [QUARTER]
from [dbo].[raw_data]


/* -------------------------------
   Step 5: Insert Latest Product Descriptions into DIM_PRODUCT
--------------------------------- */
-- For the records with price > 0 we investigate if the same product has multiple distinct descriptions
  
--;with b as (
--			select product, count(distinct description) as count_distinct_description
--			from [dbo].[raw_data]
--			where price  > 0.0
--			group by product 
--)
--select *
--from b
--where count_distinct_description > 1


/* - We took the assumption that only products with positive price are considered 
   - Also, the most recent product description is used and if historical product descriptions differ, the latest entry should override older ones.

*/

;WITH LatestDescriptions AS (
    SELECT 
        product, 
        description, 
        date,
        ROW_NUMBER() OVER (PARTITION BY product ORDER BY date DESC) AS row_num
    FROM [dbo].[raw_data]
	where cast(price as decimal(10,2)) > 0.0
)
INSERT INTO [dbo].[DIM_PRODUCT]
           ([STOCKCODE]
           ,[DESCRIPTION])

SELECT product, description 
FROM LatestDescriptions
WHERE row_num = 1;

