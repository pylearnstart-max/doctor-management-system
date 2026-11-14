
import pyodbc

def get_connection():
    try:
        con = pyodbc.connect(
            "DRIVER={ODBC Driver 17 for SQL Server};"
            "SERVER=localhost\\SQLEXPRESS;"
            "DATABASE=doctor_management_db;"
            "Trusted_Connection=yes;"
        )
        return con

    except pyodbc.Error as e:
        print("Database Connection Error:", e)
        return None
