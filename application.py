from constants import TEAMS, PLAYERS
from random import choice


def clean_data():
    #cleans data in order for compatibility with rest of program
    cleaned = []
    for player in PLAYERS:
        height = int(player['height'].split()[0])
        if player['experience'] == 'YES':
            experience = True
        else:
            experience = False
        cleaned.append({
            'name': player['name'],
            'guardians': player['guardians'].split(' and '),
            'experience': experience,
            'height': height
            })

    return cleaned


def balance_teams(cleaned):
    #ensures equal number of experienced and unexperienced on each team
    num_per_team = int(len(PLAYERS)/len(TEAMS))
    new_teams = {team:[] for team in TEAMS}
    experienced = [player for player in cleaned if player['experience'] == True]
    unexperienced = [player for player in cleaned if player['experience'] == False]
    for team in new_teams:
        for i in range(int(num_per_team/2)):
            unexp_player, exp_player = choice(unexperienced), choice(experienced)
            new_teams[team].append(unexp_player)
            unexperienced.remove(unexp_player)
            new_teams[team].append(exp_player)
            experienced.remove(exp_player)
                
    return new_teams
        
        
   
if __name__ == '__main__':
    new_teams = balance_teams(clean_data())
    quitting = False
    while not quitting:
        print("\nMENU\n\nSelect one of the following options:\n " +
              "1. Display Team Stats\n 2. Quit\n")
        try:
            option = int(input("Enter an option: "))
        except:
            print("\nThat is not one of the options, please try again. ")
            continue
        else:
            if option not in  [1, 2]:
                print("That is not one of the options, please try again. ")
                continue
