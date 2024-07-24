from db_connect import get_connection
import queries

mydb = get_connection()
cursor = mydb.cursor()
cursor.execute(queries.first_match_cards)
print(cursor.fetchall())