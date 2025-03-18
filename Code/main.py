import pandas as pd
from config import (invoices_datasets_csv_path,csv_files)
from data_ingestion import import_csv
from data_cleaning import load_cleaned_Data
from ETL import imp_tbl

"""
    Main function to handle the data pipeline:
    1. Imports raw CSV files.
    2. Displays dataset information, preview, and missing values.
    3. Calls the data cleaning function for preprocessing.
    """


def main():

    print("Importing files...")
    data = import_csv(invoices_datasets_csv_path,csv_files)

    print("\nGeneral Dataset Information: ")
    print(data.info())
    print("\n")

    print("Displaying the top 5 rows of the dataset: ")
    print(data.head())
    print("\n")

    print("Checking missing values in the dataset: ")
    print(data.isnull().sum())
    print("\n")

    print("Start Data Cleaning: ")
    print("\nConverting InvoiceDate to datetime format...")
    print("\nHandling missing values:")
    print("- Fill missing values in Description Column to Unknown Product")
    print("- Fill missing Country values with 'Unspecified' ")
    print("- Fill missing Customer values with 'Unknown' ") 
    print("Drop rows with missing Price")
    cl_df = load_cleaned_Data()
    missing_values = cl_df.isnull().sum()
    print("\nFinal Missing Values per Column:\n", missing_values)
    print("\nShow the top 5 rows of the dataset: ")
    print(cl_df.head())

    print("\nImporting Dataframe to SQL...")
    print("\n")
    imp_tbl()
if __name__=="__main__":
    main()