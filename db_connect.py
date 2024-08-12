import mysql.connector


def get_connection():
    connection = mysql.connector.connect(
        host='localhost',
        user='<USERNAME>',
        password='<PASSWORD>',
        database='eurostats'
    )
    if connection.is_connected():
        print('Connected succesfully')
        return connection


def fetch_results(query, year):
    try:
        mydb = get_connection()
        cursor = mydb.cursor()
        cursor.execute(query, (year,))

        results = cursor.fetchall()

        cursor.close()
        mydb.close()
        return results
    except Exception as e:
        print(e)
