from mysql.connector import MySQLConnection, Error
# from python_mysql_dbconfig import read_db_config

def select_room(conn, available, price):
    query = "SELECT * FROM rooms WHERE available = (%s) AND price = (%s)"
    args = (available, price)

    try:
        cursor = conn.cursor()
        cursor.execute(query, args)

        print(cursor);
        # conn.commit()

    except Error as error:
        print(error)

    finally:
        cursor.close()
        conn.close()
