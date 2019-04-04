import random
from constants import PLAYERS, TEAMS

#Here I am seperating all the players by experience and no experience. Using random shuffle will ensure that the teams are always randomized. I am then splitting the list of players to teams.

def team_creation(): 
    for PLAYER in PLAYERS:
        player_name = PLAYER['name']
        player_exp = PLAYER['experience']
        if player_exp == 'YES':
            players_with_exp.append(player_name)
        else:
            players_with_no_exp.append(player_name)
            
    random.shuffle(players_with_exp)
    random.shuffle(players_with_no_exp)
    
    team_panthers.append(players_with_exp.pop())
    team_panthers.append(players_with_exp.pop())
    team_panthers.append(players_with_exp.pop())
    team_panthers.append(players_with_no_exp.pop())
    team_panthers.append(players_with_no_exp.pop())
    team_panthers.append(players_with_no_exp.pop())

    team_bandits.append(players_with_exp.pop())
    team_bandits.append(players_with_exp.pop())
    team_bandits.append(players_with_exp.pop())
    team_bandits.append(players_with_no_exp.pop())
    team_bandits.append(players_with_no_exp.pop())
    team_bandits.append(players_with_no_exp.pop())

    team_warriors.append(players_with_exp.pop())
    team_warriors.append(players_with_exp.pop())
    team_warriors.append(players_with_exp.pop())
    team_warriors.append(players_with_no_exp.pop())
    team_warriors.append(players_with_no_exp.pop())
    team_warriors.append(players_with_no_exp.pop())

#The following three functions print the team details per team. 

def panthers_info():
    print("\nTeam: Panthers Stats\n", "-" * 15)
    print("Total players: {}\n".format(len(team_panthers)))
    print("Players on the Team:\n")
    print(', '.join(team_panthers))


def bandits_info():
    print("\nTeam: Bandits Stats\n", "-" * 15)
    print("Total players: {}\n".format(len(team_bandits)))
    print("Players on the Team:\n")
    print(', '.join(team_bandits))


def warriors_info():
    print("\nTeam: Warriors Stats\n", "-" * 15)
    print("Total players: {}\n".format(len(team_warriors)))
    print("Players on the Team:\n")
    print(', '.join(team_warriors))
    
#This asks user if they want to continue. Yes loops back to pick_team

def go_again():
    while True:
        again = input("\nWould you like to continue? (yes/no) ")
        if again.lower() == 'yes':
            break
        elif again.lower() == 'no':
            print("\nThank you for using the stats tool!\n")
            quit()
        else:
            print("\nOops, I didn't understand. Please try again.")

#Logic calls on team's info. 

def pick_team():
    print("\n1) Panthers \n2) Bandits \n3) Warriors")
    while True:
        team_picked = input("\nPlease select a team (1 - 3):  ")
        try:
            team_picked = int(team_picked)
            if team_picked != 1 and team_picked != 2 and team_picked != 3:
                raise ValueError()
        except ValueError:
            print("\nOops! I didn't understand. Please choose the number of the desired team. (1 - 3)")
        if team_picked == 1:
            panthers_info()
            go_again()
        if team_picked == 2:
            bandits_info()
            go_again()
        if team_picked == 3:
            warriors_info()
            go_again()

#Initial menu
def show_menu():
    print("--" * 3, "MENU", "--" * 3)
    print("\nHere are your choices: \n1) Display Team Stats \n2) Quit")
    while True:
        display_stats = input("\nEnter an option (1 or 2) >  ")
        try:
            display_stats = int(display_stats)
            if display_stats != 1 and display_stats != 2:
                raise ValueError()
        except ValueError:
            print("\nOops, that is not a valid input. Please enter '1' for Team Stats or '2' to Quit the app.")
            continue
        if display_stats == 2:
            print("\nThank you for using this tool! Have a great day!\n")
            break
        if display_stats == 1:
            pick_team()
                

if __name__ == "__main__":

    team_panthers = []
    team_bandits = []
    team_warriors = []
    players_with_exp = []
    players_with_no_exp = []
    team_creation()
    print("\nBASKETBALL TEAM STATS TOOL\n")
    show_menu()
