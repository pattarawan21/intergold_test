import pyodbc
import pandas as pd
import os
from datetime import datetime # นำเข้า datetime เพื่อใช้กับวันที่

def get_customer_info(id: str, start_date: datetime = None, end_date: datetime = None) -> pd.DataFrame:
    df = pd.DataFrame() 
    conn_str = os.getenv('CUSTOMER_DB_CONN')
    
    if not conn_str:
        return df

    try:
        with pyodbc.connect(conn_str) as conn:
            sql_query_parts = ["SELECT id, name, email, transactions, created_at FROM Customer WHERE id = ?"]
            parameters = [id]

            if start_date:
                sql_query_parts.append("AND created_at >= ?")
                parameters.append(start_date)
            if end_date:
                sql_query_parts.append("AND created_at <= ?")
                parameters.append(end_date)

            sql = " ".join(sql_query_parts)
            
            df = pd.read_sql(sql, conn, params=parameters)
        
    except pyodbc.Error as ex:
        sqlstate = ex.args[0]
        print(f"Database error occurred: {sqlstate} - {ex.args[1]}")
    except Exception as ex:
        print(f"An unexpected error occurred: {ex}")
    return df