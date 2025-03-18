# Invoices DWH Project

This project processes raw invoice data from CSV file, builds a Data Warehouse (DWH) in Microsoft SQL Server using Kimball Methodology, and provides useful assumptions, analyses, and aggregations.
The project is structured for easy maintenance, extension, and execution on any machine with Python 3, SQL Server, and the required dependencies installed.

---

## **📌 Project Overview**
This project follows a structured ETL (Extract, Transform, Load) process to:
- **Extract** raw invoice data from CSV files.
- **Transform** the data by cleaning, handling missing values, and applying business rules.
- **Load** the structured data into a SQL Server Data Warehouse using Kimball’s methodology.
- **Provide meaningful insights** through SQL aggregations.

---

## **📁 Folder Structure**

      Invoices/
      │── Code/
      │   ├── config.py
      │   ├── data_cleaning.py
      │   ├── data_ingestion.py
      │   ├── ETL.py
      │   ├── main.py
      │   ├── sql_cred.env
      │   ├── requirements.txt
      │── SQL_queries/
      │   ├── 1_Database_schema_creation.sql
      │   ├── 2_Fill_Dim_tables.sql
      │   ├── 3_Fill_Fact_table.sql
      │   ├── Aggregation_1.sql
      │   ├── Aggregation_2.sql
      │   ├── Aggregation_3.sql
      │── invoice_files/
      │   ├── Invoices_Year_2009-2010.csv
      │── Assumptions-Abnormalities.txt
      └── README.md



## 📝 Documentation - Steps Taken to Reach the Final Solution

### **1. Dynamic Configuration**
   - Created **config.py** file to dynamically determine the project's file paths
   - Included database connection details and env variables

### **2. Data Ingestion and Preparation**
   - Based on raw csv data, we converted date fields to datetime format and handled missing values.
   - Removed duplicates and filtered out records with invalid values.
   - Applied some rules to missing values.
    
### **3. Data Warehouse Design**
   - Applied **Kimball Methodology** for dimensional modeling.
   - Designed and created **dimensional tables (dim_products, dim_customers, dim_dates)**.
   - Created a **fact table (fact_sales)** to store transactional data.
   - Established relationships between dimensions and the fact table.

### **4. Data Load Process**
   - Loaded cleaned and structured data into **Microsoft SQL Server**.
   - Inserted **dimension data** (dim_products, dim_customers, dim_dates, dim_time).
   - Inserted **fact data** (fact_sales)
     
### **5. Business Assumptions & Data Issues**
   - Handled multiple descriptions for the same product by keeping the latest description.
   - Removed transactions with zero or negative price values.

### **6. Aggregations**
   - Created SQL queries for three key aggregations:
     - **Total Revenue per Month (Aggregation_1.sql)**
     - **Top 10 Best-Selling Products (Aggregation_2.sql)**
     - **Revenue by Country (Aggregation_3.sql)**
   - Queries can be executed in **SQL Server Management Studio**.

---

## Steps to Run the Project

  1. **Clone the Repository**

   Open your terminal or command prompt and navigate to the directory where you want to store the project. Then, run the following command to clone the Git repository:

   ```bash
   git clone https://github.com/nikolaosfragkoulis/Invoices.git
   ```

  2. **Setting Up SQL Server Credentials & Running the First Query for DB schema creation**

     ### Step 1: Configure SQL Server Credentials
      
      1. Navigate to the **`Invoices/Code`** folder.
      2. Open the **`sql_cred.env`** file using a text editor
      3. Enter your SQL Server credentials in the following format:

         ```env
         SQL_SERVER_NM=Your_Server_Name
         DATABASE_NM=InvoiceDWH  #Do Not Change this
         SERVER_USERNAME=Your_Username
         SERVER_PASSWORD=Your_Password
         ```
      4. Save and close the file.

     ### Step 2: Open SQL Server Management Studio (SSMS)
      1. Launch SQL Server Management Studio (SSMS).
      2. Connect to your SQL Server using the credentials you entered in **sql_cred.env**.
      3. Open a new Query Editor.

     ### Step 3: Execute the First SQL Query
      1. Navigate to the **Invoices/SQL_queries** folder.
      2. Open the file **1_Database_schema_creation.sql** in SSMS.
      3. Click Execute to create the database schema.

  3. **Run the Python Script**

     ### Step 1: Install Required Dependencies

      1. Open the command prompt.
      2. Navigate to the **Invoices/Code** directory.
      3. Run the **requirements.py** script to install dependencies:
         ```bash
            pip install -r requirements.txt
         ```

     ### Step 2: Run the main script
      1. Run the script in order to extract data, clean it, and prepare it for loading into SQL Server in **raw_data** table:
         ```bash
            python main.py
         ```

         
  4. **Fill DWH tables with values**

      ### Step 1: Load Dimension Tables
        1. Navigate to the **Invoices/SQL_queries** folder.
        2. Open **2_Fill_Dim_tables.sql** in SSMS.
        3. Click **Execute** to populate the dimension tables.

      ### Step 2: Load Fact Table
        1. Open **3_Fill_Fact_table.sql** in SSMS.
        2. Click **Execute** to populate the `fact_sales` table with transactional data.
  
      ### Step 3: Run SQL Aggregation Queries**
       Once the data is fully loaded, execute the following SQL queries to analyze the dataset:

      - **Total Revenue per Month:** Run **Aggregation_1.sql**
      - **Top 10 Best-Selling Products:** Run **Aggregation_2.sql**
      - **Revenue by Country:** Run **Aggregation_3.sql**

These queries will provide insights into sales trends, product performance, and market distribution.

---
