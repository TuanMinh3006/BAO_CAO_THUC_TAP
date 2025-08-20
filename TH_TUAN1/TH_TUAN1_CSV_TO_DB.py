import pandas as pd
import sys
import os
from sqlalchemy import create_engine
from dotenv import load_dotenv
load_dotenv()

def csv_to_mysql(csv_file,db_config,table_name='people', if_exists='replace'):
    try:
        conn_string=f"mysql+mysqlconnector://{db_config['user']}:{db_config['password']}@{db_config['host']}/{db_config['database']}"
        engine = create_engine(conn_string)
        df=pd.read_csv(csv_file)
        print(df)

        df.to_sql(name=table_name, con=engine, if_exists=if_exists, index=False)
    except Exception as e:
        print(f"Error connecting to database or reading CSV file: {e}")
        sys.exit(1)
    finally:
        if 'engine' in locals():
            engine.dispose()
            print("Database connection closed")

csv_file="/home/hadoopuser/BAO_CAO_THUC_TAP/people-1000.csv"
db_config = {
    'user': os.getenv('mysql_user'),
    'password': os.getenv('mysql_pass'),
    'host': os.getenv('mysql_host'),
    'database': os.getenv('mysql_db')
}
csv_to_mysql(csv_file, db_config=db_config,table_name='people', if_exists='append')

