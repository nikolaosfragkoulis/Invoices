import pandas as pd
from data_ingestion import import_csv # Import custom function to read CSV files
from config import (invoices_datasets_csv_path,csv_files)


"""
    Loads, cleans, and preprocesses invoice data.

    - Reads CSV files into a DataFrame.
    - Converts the InvoiceDate column to datetime format.
    - Fills missing values in Description, Country, and Customer ID.
    - Drops rows where the Price column has missing values.
    - Prints missing values summary and the first few rows of the cleaned dataset.
"""


def load_cleaned_Data():

    df = import_csv(invoices_datasets_csv_path, csv_files)

    
    df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"],errors="coerce") #if there is an error, convert to NaN
    
    # Handling missing values:
    # Fill missing descriptions with "Unknown Product"
   
    df["Description"] = df["Description"].fillna("Unknown Product")

    # Fill missing Country values with "Unspecified"
    
    df["Country"] = df["Country"].fillna("Unspecified")

    # Fill missing Customer values with "Unknown"
    
    df["Customer ID"] = df["Customer ID"].fillna("Unknown")

    # Drop rows where Price is missing (assuming it's critical for sales calculations)
    
    df = df.dropna(subset=["Price"])



    return df