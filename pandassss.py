import pandas as pd 

import mysql.connector as connection 
from sqlalchemy import create_engine 
from sqlalchemy.engine import URL

mydb = URL.create("mysql",host="localhost",username = "root",password = "",database = "city_data")
# print(mydb)
engine = create_engine(mydb)
print(engine)
# cursor = mydb.cursor()
# cursor.execute("show databases")
# print(cursor.fetchall())

# df_sql = pd.read_sql("D:/SQLSUDH.sql",engine)
# print(df_sql)
connection = engine.connect()
connection.execute("show databases")
print(connection.fetchall())