import pyodbc
import pandas as pd
import os # สำหรับอ่าน Environment Variable

def get_customer_info(id):
    df = pd.DataFrame()
    conn_str = os.getenv('CUSTOMER_DB_CONN') 
    
    if not conn_str:
        return df

    try:
        with pyodbc.connect(conn_str) as conn:
            sql = "SELECT id, name, email, transactions FROM Customer WHERE id = ?" # ใช้ '?' สำหรับ pyodbc parameter
            # ใช้ pandas ดึงข้อมูลออกมาเป็น DataFrame พร้อมส่ง parameters
            df = pd.read_sql(sql, conn, params=[id])

    except pyodbc.Error as ex:
        sqlstate = ex.args[0]
        print(f"Database error occurred: {sqlstate} - {ex.args[1]}")
    except Exception as ex:
        print(f"An unexpected error occurred: {ex}")

    return df
