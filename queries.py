first_match_cards = ("SELECT match_category "
                     "FROM euro2024 "
                     "WHERE team_one = 'Niemcy' OR team_two = 'Niemcy'")
cards_group_stage = ("SELECT yellow_cards_sum "
                     "FROM euro2024 "
                     "WHERE match_category "
                     "LIKE '% mecz grupowy'")
cards_by_match_category = ("SELECT match_category, AVG(yellow_cards_sum) "
                           "AS cards_sum "
                           "FROM euro%s "
                           "GROUP BY match_category "
                           "ORDER BY match_category")
fouls_by_match_category = ("SELECT match_category, AVG(fouls_sum) "
                           "AS fouls_sum "
                           "FROM euro%s "
                           "GROUP BY match_category "
                           "ORDER BY match_category ")
