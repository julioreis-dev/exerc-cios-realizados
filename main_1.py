def calc_price_tournament(person_quote, tournament):
    
    with open('Assignment/data/tournaments.csv') as fht:
        
        lines = [l.strip() for l in fht.readlines()][1:]
        tournaments = []
        for l in lines:
            tournaments.append({k: v for k, v in zip(['Name', 'Group Stage Matches', 'Elimination Rounds', 'Sport'], l.split(','))})
        
        tournament_line = None

        for t in tournaments:
            if t['Name'] == tournament:
                tournament_line = t

        total_quote = 0

        total_quote += person_quote * int(tournament_line['Group Stage Matches'])
        total_quote += person_quote * (int(tournament_line['Elimination Rounds']) * 2)
        
        fht.flush()
        fht.close()
    
    return total_quote

def calc_price_game(l):
    # solution to point 1
    skill_level = '' if l['Skill level'] == '' else int(l['Skill level'])
    if skill_level == 1:
        return 1.5
    elif skill_level == 2:
        return 3
    elif skill_level == 3:
        return 5
    elif skill_level == 4:
        return 7
    else:
        return 10

with open('Assignment/data/players.csv') as fhp:
    # Reading all file lines
    lines = [l.strip() for l in fhp.readlines()][1:]

    new_lines_people = []
    for l in lines:
        new_lines_people.append({k: v for k, v in zip(['First name', 'Last name', 'Skill level', 'Paid', 'Team', 'Tournament'], l.split(','))})

    print(new_lines_people)

    new_lines_people_not_paid = []

    # Remove already paid lines
    for l in new_lines_people:
        if l['Paid'] == 'Yes':
            new_lines_people_not_paid.append(l)

    tournaments = {}
    for l in new_lines_people:
        if not l['Tournament'] in tournaments.keys():
            tournaments[l['Tournament']] = {}
        if not l['Team'] in tournaments[l['Tournament']].keys():
            tournaments[l['Tournament']][l['Team']] = 0
            
        person_quote = calc_price_game(l)
        tournament_quote = calc_price_tournament(person_quote, l['Tournament'])
        tournaments[l['Tournament']][l['Team']] = tournaments[l['Tournament']][l['Team']] + tournament_quote
    
    for tournament, teams in tournaments.items():
        for team, quote in teams.items():
            print("=== " + tournament + " === " + team + " => " + str(quote) + " ===")

    fhp.flush()
    fhp.close()
