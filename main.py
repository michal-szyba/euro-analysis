import mysql
from db_connect import get_connection
import queries
import matplotlib.pyplot as plt


def fetch_results(query):
    try:
        mydb = get_connection()
        cursor = mydb.cursor()
        cursor.execute(query)

        results = cursor.fetchall()

        cursor.close()
        mydb.close()
        return results
    except Exception as e:
        print(e)


query_results = fetch_results(queries.cards_by_match_category)
results = [(match_category, float(cards_sums)) for match_category, cards_sums in query_results]
match_order = ['I mecz grupowy',
               'II mecz grupowy',
               'III mecz grupowy',
               '1/8 finału',
               '1/4 finału',
               '1/2 finału',
               'finał']

sorted_results = sorted(results, key=lambda x: match_order.index(x[0]), )
match_types, cards_sums = zip(*sorted_results)

plt.figure(figsize=(8, 8))
plt.xticks(rotation=60)
plt.subplots_adjust(bottom=0.2)
plt.bar(match_types, cards_sums, width=0.6, align='center')
plt.show()