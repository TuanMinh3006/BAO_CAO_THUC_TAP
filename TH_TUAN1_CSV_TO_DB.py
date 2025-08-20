import pandas as pd
import sys
import os
import mysql.connector
def csv_to_mysql(csv_file,db_config):
    try:
        conn=mysql.connector.connect(**db_config)
        df=pd.read_csv(csv_file)
        print(df)

    except Exception as e:
        print(f"Error connecting to database or reading CSV file: {e}")
        sys.exit(1)
csv_file=r"\\wsl.localhost\Ubuntu\home\tuanminh\people-1000.csv"
db_config = {
    'user': 'root',
    'password': '',
    'host': 'localhost',
    'database': 'tuan1'
}
csv_to_mysql(csv_file, db_config=db_config)
