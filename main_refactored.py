import pandas as pd


def calc_price_tournament(df: object, person_quote: float, tournament: str) -> int:
    """This function calculate the price by tournament"""
    element = df[df['Name'] == tournament]
    tournament_resul = element.to_dict('records')
    tournament_line = tournament_resul[0]

    total_quote = 0

    total_quote += person_quote * int(tournament_line['Group Stage Matches'])
    total_quote += person_quote * (int(tournament_line['Elimination Rounds']) * 2)

    return total_quote


def main():
    df = pd.read_csv('Assignment/data/players.csv')
    df.loc[df['Skill level'].isnull(), 'Skill level'] = 0
    new_lines_people = df.to_dict('records')

    print(new_lines_people)

    df2 = pd.read_csv('Assignment/data/tournaments.csv')
    df2.rename(columns={'Elimination Matches': 'Elimination Rounds'}, inplace=True)

    dict_cost = {1: 1.5, 2: 3, 3: 5, 4: 7}
    calc_price_game = lambda content, cost: cost.get(int(content['Skill level']), 10)

    tournaments = {}
    for dict_content in new_lines_people:
        if not dict_content['Tournament'] in tournaments.keys():
            tournaments[dict_content['Tournament']] = {}
        if not dict_content['Team'] in tournaments[dict_content['Tournament']].keys():
            tournaments[dict_content['Tournament']][dict_content['Team']] = 0

        person_quote = calc_price_game(dict_content, dict_cost)
        tournament_quote = calc_price_tournament(df2, person_quote, dict_content['Tournament'])
        tournaments[dict_content['Tournament']][dict_content['Team']] = \
            tournaments[dict_content['Tournament']][dict_content['Team']] + tournament_quote

    for tournament, teams in tournaments.items():
        for team, quote in teams.items():
            print(f"=== {tournament} === {team} => {str(quote)} ===")


if __name__ == '__main__':
    main()
