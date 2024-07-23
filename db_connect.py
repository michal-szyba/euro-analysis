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
