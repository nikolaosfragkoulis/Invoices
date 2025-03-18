
import os
from pathlib import Path
from dotenv import load_dotenv  # Import dotenv

"""
This code dynamically determines file paths based on the location of config.py.
It identifies the parent directory (project root) of the current scripts folder, then constructs paths to the csv dataset.
"""

#Find the current directory
scripts_dir = os.path.dirname(os.path.abspath(__file__))

#Reference the parent folder named INVOICES
project_root = os.path.dirname(scripts_dir)

#Construct the paths for csv datasets:
invoices_datasets_csv_path = os.path.join(project_root, "invoice_files") + os.sep

# CSV file name
csv_files = "Invoices_Year_2009-2010.csv"

dotenv_path = Path(scripts_dir+"\\sql_cred.env")

print(dotenv_path)

load_dotenv(dotenv_path=dotenv_path)


#Database Connection Details
sql_server_nm = os.getenv("SQL_SERVER_NM")
database_nm = os.getenv("DATABASE_NM")
server_username = os.getenv("SERVER_USERNAME")
server_password = os.getenv("SERVER_PASSWORD")


# Validate credentials

if not all([sql_server_nm, database_nm, server_username, server_password]):
    raise ValueError("Missing database credentials. Check your .env file.")

print("Credentials loaded successfully.")