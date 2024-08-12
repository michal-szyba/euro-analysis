import numpy as np
from db_connect import get_connection, fetch_results
import queries
import matplotlib.pyplot as plt

match_order = ['I mecz grupowy',
               'II mecz grupowy',
               'III mecz grupowy',
               '1/8 finału',
               '1/4 finału',
               '1/2 finału',
               'finał']


def analyze(year):
    query_results_cards = fetch_results(queries.cards_by_match_category, year)
    results_cards = [(match_category, float(cards_sums)) for match_category, cards_sums in query_results_cards]
    sorted_results_cards = sorted(results_cards, key=lambda x: match_order.index(x[0]), )
    match_categories, cards_sums = zip(*sorted_results_cards)

    query_results_fouls = fetch_results(queries.fouls_by_match_category, year)
    results_fouls = [(match_category, float(fouls_sums)) for match_category, fouls_sums in query_results_fouls]
    sorted_results_fouls = sorted(results_fouls, key=lambda x: match_order.index(x[0]), )
    _, fouls_sums = zip(*sorted_results_fouls)

    color_yellow = '#F7C300'
    color_blue = '#0047AB'

    fig, ax1 = plt.subplots()
    plt.title('Kartki / faule w Euro 2024')

    ax1.bar(match_categories, fouls_sums, color=color_blue, label='Faule')
    ax1.set_ylabel('Faule', color=color_blue)
    ax1.set_xticks(np.arange(len(match_categories)))
    ax1.set_xticklabels(match_categories, rotation=60)
    ax1.grid(True, linestyle='-', alpha=0.4, color=color_blue)
    ax1.yaxis.set_major_locator(plt.MultipleLocator(5))
    ax1.legend(loc='upper left', bbox_to_anchor=(0, 1.12))

    ax2 = ax1.twinx()
    ax2.plot(match_categories, cards_sums, color=color_yellow, label='Kartki')
    ax2.set_ylabel('Żółte kartki', color=color_yellow)
    ax2.grid(True, linestyle='-', alpha=0.4, color=color_yellow)
    ax2.yaxis.set_major_locator(plt.MultipleLocator(0.25))
    ax2.legend(loc='upper right', bbox_to_anchor=(1, 1.12))

    fig.tight_layout()

    plt.show()
