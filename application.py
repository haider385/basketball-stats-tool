from constants import TEAMS, PLAYERS
from random import choice



def clean_data():
    #cleans data in order for compatibility with the rest of the program
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
    #ensures equal number of experienced and inexperienced players on each team
    num_per_team = int(len(PLAYERS)/len(TEAMS))
    new_teams = {team:[] for team in TEAMS}
    experienced = [player for player in cleaned if player['experience'] == True]
    inexperienced = [player for player in cleaned if player['experience'] == False]
    for team in new_teams:
        for i in range(int(num_per_team/2)):
            inexp_player, exp_player = choice(inexperienced), choice(experienced)
            new_teams[team].append(inexp_player)
            inexperienced.remove(inexp_player)
            new_teams[team].append(exp_player)
            experienced.remove(exp_player)
                
    return new_teams


def total_experienced(team):
    experienced = 0
    for player in team:
        if player['experience'] == True:
            experienced += 1

    return experienced


def total_inexperienced(team):
    inexperienced = 0
    for player in team:
        if player['experience'] == False:
            inexperienced += 1

    return inexperienced


def average_height(team):
    heights = [player['height'] for player in team]
    return sum(heights)/ len(heights)


def guardian_names(team):
    names = ', '.join([', '.join(player['guardians']) for player in team])
    return names


def player_names(team):
    names = ', '.join([player['name'] for player in team])
    return names


if __name__ == '__main__':
    new_teams = balance_teams(clean_data())
    quitting = False
    while not quitting:
        print("-" * 50 +
              "\nMENU\n\nSelect one of the following options:\n " +
              "1. Display Team Stats\n 2. Quit\n")
        try:
            option = int(input("Enter an option: "))
        except:
            print("\nThat is not one of the options, please try again. ")
            continue
        else:
            if option not in  [1, 2]:
                print("\nThat is not one of the options, please try again. ")
                continue

        if option == 1:
            team_names = list(new_teams.keys())
            print()
            for name in team_names:
                print("{}. {}".format(team_names.index(name) + 1, name))
            try:
                chosen_team = int(input("\nWhich team? (enter the corresponding number): "))
            except:
                print("\nThat is not one of the options, please return to the menu. ")
                continue
            else:
                if chosen_team - 1 in list(range(len(team_names))):
                    print('-' * 50)
                    chosen_team_name = team_names[chosen_team - 1]
                    team = new_teams[chosen_team_name]
                    print(f"\nHere are the stats for the {chosen_team_name}:\n")
                    print("Total number of players: {}\n".format(
                        total_inexperienced(team) + total_experienced(team)))
                    print("Names of all players:\n{}\n".format(
                        player_names(team)))
                    print("Total number of inexperienced players: {}\n".format(
                        total_inexperienced(team)))
                    print("Total number of experienced players: {}\n".format(
                        total_experienced(team)))
                    print("Average height of the team: {} inches\n".format(
                        average_height(team)))
                    print("Guardian names of all player on the team: \n{}".format(
                        guardian_names(team)))
                else:
                    print("\nThat is not one of the options, please return to the menu. ")
                    continue     
        else:
            print("\nGoodbye!")
            quitting = True
