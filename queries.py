first_match_cards = ("SELECT match_category "
                     "FROM csv_meczyki_euro "
                     "WHERE team_one = 'Niemcy' OR team_two = 'Niemcy'")
cards_group_stage = ("SELECT yellow_cards_sum "
                     "FROM csv_meczyki_euro "
                     "WHERE match_category "
                     "LIKE '% mecz grupowy'")
cards_by_match_category = ("SELECT match_category, AVG(yellow_cards_sum) "
                           "AS cards_sum "
                           "FROM csv_meczyki_euro "
                           "GROUP BY match_category "
                           "ORDER BY match_category")
fouls_by_match_category = ("SELECT match_category, AVG(fouls_sum) "
                           "AS fouls_sum "
                           "FROM csv_meczyki_euro "
                           "GROUP BY match_category "
                           "ORDER BY match_category ")
