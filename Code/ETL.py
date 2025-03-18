import pyodbc
from data_cleaning import load_cleaned_Data
from config import sql_server_nm,database_nm,server_username,server_password


def imp_tbl():
    # Create connection string
    conn = pyodbc.connect(
        f"DRIVER={{SQL Server}};SERVER={sql_server_nm};DATABASE={database_nm};UID={server_username};PWD={server_password}"
    )



    #load dataframe
    raw_data = load_cleaned_Data()

    # Execute query
    cursor = conn.cursor()



  
    print("Insert DataFrame values to SQL SERVER")

    # Insert Data into SQL Server
    insert_query = """
    INSERT INTO [dbo].[raw_data] (INVOICE ,
                                    PRODUCT ,
                                    DESCRIPTION,
                                    QUANTITY ,
                                    DATE ,
                                    PRICE,
                                    CUSTOMER, 
                                    COUNTRY
                                    ) VALUES (?, ?, ?,?,?,?,?,?)
    """

    cursor.fast_executemany = True
    cursor.executemany(insert_query,raw_data.values.tolist())

    # Commit and close
    conn.commit()
    cursor.close()
    conn.close()
    print("\n")
    print("DataFrame values imported Successfully!")

