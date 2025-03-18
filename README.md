# Invoices DWH Project

This project processes raw invoice data from CSV file, builds a Data Warehouse (DWH) in Microsoft SQL Server using Kimball Methodology, and provides useful assumptions, analyses, and aggregations.
The project is structured for easy maintenance, extension, and execution on any machine with Python 3, SQL Server, and the required dependencies installed.


## Documentation - Steps Taken to Reach the Final Solution

1. ### Dynamic Configuration of File Paths
    **Modular Configuration:**
    To enhance portability, we created a **config.py** file that dynamically determines the project's file paths and database connection details.
    This ensures that the project works correctly regardless of the computer or directory in which it is placed.

   **Centralized Settings:**
    The configuration file also includes a list of CSV filename to be processed, keeping all file path settings in one centralized location.
