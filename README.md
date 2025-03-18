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
    We began with raw invoice data provided in CSV format stored in the football_datasets/ folder.




## Steps to Run the Project

  1. **Clone the Repository**

   Open your terminal or command prompt and navigate to the directory where you want to store the project. Then, run the following command to clone the Git repository:

   ```bash
   git clone https://github.com/nikolaosfragkoulis/Gaming.git
   ```

  2. **Navigate to the Project Directory**

   Change your current directory to the newly cloned project:

   ```bash
   cd Gaming
   ```

  3. **Create and Activate a virtual environment (Optional)**
  
   - **Create a new environment**:
     ```bash
     python -m venv venv
     ```
   - **Activate the environment**:
     ```bash
     venv\Scripts\activate
     ```

  4. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

  4. **Run the code**
   ```bash
   python Code\main.py
   ```
