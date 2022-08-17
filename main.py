def calc_price_tournament(tournaments, person_quote: float, tournament: str) -> int:
    """This function calculate the price by tournament"""
    tournament_line = None
    for t in tournaments:
        if t['Name'] == tournament:
            tournament_line = t

    total_quote = 0
    total_quote += person_quote * int(tournament_line['Group Stage Matches'])
    total_quote += person_quote * (int(tournament_line['Elimination Rounds']) * 2)

    return total_quote


def main(tournaments_df, new_lines_people):
    print(new_lines_people)
    # cost for skill level (key = skill level, value = cost for level)
    dict_cost = {1: 1.5, 2: 3, 3: 5, 4: 7}
    # function to calculate the cos for each player
    calc_price_game = lambda data, cost: cost.get(0 if data['Skill level'] == '' else int(data['Skill level']), 10)

    tournaments = {}
    for dict_content in new_lines_people:
        if not dict_content['Tournament'] in tournaments.keys():
            tournaments[dict_content['Tournament']] = {}
        if not dict_content['Team'] in tournaments[dict_content['Tournament']].keys():
            tournaments[dict_content['Tournament']][dict_content['Team']] = 0

        person_quote = calc_price_game(dict_content, dict_cost)
        tournament_quote = calc_price_tournament(tournaments_df, person_quote, dict_content['Tournament'])
        tournaments[dict_content['Tournament']][dict_content['Team']] = \
            tournaments[dict_content['Tournament']][dict_content['Team']] + tournament_quote

    for tournament, teams in tournaments.items():
        for team, quote in teams.items():
            print(f"=== {tournament} === {team} => {str(quote)} ===")


if __name__ == '__main__':
    with open('Assignment/data/tournaments.csv') as fht:
        # Reading all file lines in tournaments.csv
        lines_tournaments = [row.strip() for row in fht.readlines()][1:]
        # creating a list with dict content
        group_games = [{k: v for k, v in zip(['Name', 'Group Stage Matches', 'Elimination Rounds', 'Sport'],
                                             line.split(','))} for line in lines_tournaments]
        fht.flush()

    with open('Assignment/data/players.csv') as fhp:
        # Reading all file lines in players.csv
        lines = [row.strip() for row in fhp.readlines()][1:]
        # changing each line to be storage in a dict where the keys are title
        lines_people = [{k: v for k, v in zip(['First name', 'Last name', 'Skill level', 'Paid', 'Team', 'Tournament'],
                                              line.split(','))} for line in lines]
        fhp.flush()

    main(group_games, lines_people)
