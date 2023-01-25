def main():

    #Step 2 - Create a complex data structure
    hockey_team = {
        'name': 'maple leafs',
        'city':'Toronto',
        'players': [
            'marner',
            'tavares',
            'nylander',
            'matthers'
            ],
            'games': [
                {
                    'opponent': 'Canadiens',
                    'goals for': 8,
                    'goals against': 0
                },
                {   'opponent': 'Red Wings',
                    'goalsfor': 3,
                    'goalsagainst': 2
                    }
                ]
    }

    
    #Step 3 - Add another movie to the data structure
    new_game = {
    'opponent': 'Blues',
    'goalsfor': 5,
    'goalsagainst': 6
}
    hockey_team['games'].insert(1, new_game)
   
    print_team_name(hockey_team)
    add_players(hockey_team, ('murray', 'reilly', 'simmonds'))
    print_players(hockey_team)
    print_opponents(hockey_team)
    pass
    
# Step 4 - Function that prints team city and name	
def print_team_name(team):
    print(f"The {team['city'].title()} {team['name'].title()} will maybe win some playoff games")

# Step 5 - Function that adds playeres to data structure
def add_players(team, new_players):
    team['players'].extend(new_players)
    for i,p in enumerate(team['players']):
        team['players'][i] = p.title()
    team['players'].sort()

# TODO: Step 6 - Function that prints bullet list of players.
def print_players(team):
    print('\nthe player list is')     
    for p in team['players']:
        print(f'- {p}')

# TODO: Step 7 - Function that prints comma-separated list of opponents
def print_opponents(team):
    print('\nThe leafs have played against the ', end='')     
    #for i,g in enumerate(team['games']):
     #   if i < len(team['games']) -1:
      #      print(f'{g["opponent"]},', end='')
       # else:
        #    print(f'{g["opponent"]}')

    opponent_names = [g['opponent'] for g in team['games']]
    opponent_csl = ', '.join(opponent_names)
    print(opponent_csl)
    pass
        


    return 

# TODO: Step 8 - Function that prints comma-separated list of movie titles
def print_movie_titles(movie_list):
    return
    
if __name__ == '__main__':
    main()