import mysql.connector
from mysql.connector import Error
from queries import select_room

def connect():
    try:
        conn = mysql.connector.connect(
            host='',
            database='',
            user='',
            password=''
        )
        if conn.is_connected():
            print('Connected to MySQL database')
            select_room(conn, True, 330)
    except Error as e:
        print(e)

    finally:
        conn.close()

print('Running')
connect()
