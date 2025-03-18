import pandas as pd

#function to import csv into a dataset
def import_csv(invoices_datasets_csv_path, csv_files):

    # Iterate through the list of files
        try:
            df = pd.read_csv(invoices_datasets_csv_path+csv_files,encoding="utf-8",low_memory=False)
        # If UTF-8 decoding fails, try with Latin-1 encoding
        except UnicodeDecodeError:
            try:
                df = pd.read_csv(invoices_datasets_csv_path+csv_files,encoding="latin-1",low_memory=False)
            # If Latin-1 decoding fails, try with Windows-1252 encoding
            except  UnicodeDecodeError:
                df = pd.read_csv(invoices_datasets_csv_path+csv_files,encoding="windows-1252",low_memory=False)
        return  df # Return the DataFrame of the last successfully read file