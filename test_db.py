from db import get_connection

con = get_connection()

if con:
    print("Database Connected Successfully")
    con.close()