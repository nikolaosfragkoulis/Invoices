# Invoices DWH Project

This project processes raw invoice data from CSV file, builds a Data Warehouse (DWH) in Microsoft SQL Server using Kimball Methodology, and provides useful assumptions, analyses, and aggregations.
The project is structured for easy maintenance, extension, and execution on any machine with Python 3, SQL Server, and the required dependencies installed.


## Documentation - Steps Taken to Reach the Final Solution

1. ### Dynamic Configuration of File Paths
    **Modular Configuration:**
    To enhance portability, we created a **config.py** file that dynamically determines the project's file paths and includes database connection details.
    This ensures that the project works correctly regardless of the computer or directory in which it is placed.

2. ### Data Ingestion and Preparation
    **Raw Data:**
    We began with raw invoice data provided in CSV format stored in the **invoice_files/** folder.

      ```
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
      │   ├── Fill_dim_tables.sql
      │   ├── Fill_Fact_table.sql
      │   ├── Examples_of_Data_investigation.sql
      │   ├── Revenue_by_Country.sql
      │   ├── Top_10_Best_Selling_Products.sql
      │   ├── Total_Revenue_per_Month.sql
      │── invoice_files/
      │   ├── Invoices_Year_2009-2010.csv
      │── Assumptions-Abnormalities.txt
      ├── README.md
      ```

## Steps to Run the Project

  1. **Clone the Repository**

   Open your terminal or command prompt and navigate to the directory where you want to store the project. Then, run the following command to clone the Git repository:

   ```bash
   git clone https://github.com/nikolaosfragkoulis/Invoices.git
   ```

  2. **Setting Up SQL Server Credentials & Running the First Query**

     ### Step 1: Configure SQL Server Credentials
      
      1. Navigate to the **`Invoices/Code`** folder.
      2. Open the **`sql_cred.env`** file using a text editor
      3. Enter your SQL Server credentials in the following format:

         ```env
         SQL_SERVER_NM=Your_Server_Name
         DATABASE_NM=InvoiceDWH <-- This should not be changed
         SERVER_USERNAME=Your_Username
         SERVER_PASSWORD=Your_Password
         ```
      4. Save the file and close the editor.

     ### Step 2: Open SQL Server Management Studio (SSMS)
      1. Launch SQL Server Management Studio (SSMS).
      2. Connect to your SQL Server using the credentials you entered in **sql_cred.env**.
      3. Open a new Query Editor.

     ### Step 3: Execute the First SQL Query
      1. Navigate to the **Invoices/SQL_queries** folder.
      2. Open the file **1_Database_schema_creation.sql** in SSMS.
      3. Click Execute 

 3. **Run the Python Script**

     ### Step 1: Install Required Dependencies

      1. Open the command prompt.
      2. Navigate to the **Invoices/Code** directory:
      3. Run the **requirements.py** script to install dependencies:
         ```bash
            pip install -r requirements.txt
         ```

     ### Step 2: Run the code
      1. Run the script:
         ```bash
            python main.py
         ```
