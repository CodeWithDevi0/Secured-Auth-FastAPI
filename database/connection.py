import mysql.connector
from mysql.connector import Error

def get_db_connection():
   try:
      return mysql.connector.connect(
         host = "localhost",
         user = "root",
         password = "",
         database = "secured_authentication_db",
      )
   except Error as e:
      print(f"Error connecting to MySQL: {e}")
      return None