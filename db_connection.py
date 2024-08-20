import mysql.connector

from mysql.connector import Error

def connect_lib():
    db_name = 'lib'
    user = 'root' # select the specific database user 
    password = ''
    host = '127.0.0.1'

# Establish our connection

    try: 
        conn = mysql.connector.connect(
            database = db_name,
            user = user,
            password = password,
            host = host
        )
        if conn.is_connected():
            print("Connection to MySql database successful!")
            return conn
    
    except Error as e:
        print(f"Error: {e}")
        return None
