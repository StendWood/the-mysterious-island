# coding: utf-8

# Imports
from datetime import datetime
import json

# Extra Code
import main_menu as mm
import variables

# FUNCTIONS
# Show the leaderboard
def leaderboard():
    mm.welcome_screen()
    print("\n\t\t\t\tThis is the leaderboard\n")
    # Sort the list
    variables.leaderboard_data.sort(reverse=True)
    # Print the leaderboard
    for line in variables.leaderboard_data:
        print(f"Score : {line[0]}   Name : {line[1]}    Energy : {line[2]}    Hydratation : {line[3]}    Satiety : {line[4]}    Movements : {line[5]}    Actions : {line[6]}    Time : {line[7]} seconds\n")
    input("\n\t\t\t\tPress Enter to continue")
    mm.main_menu()


# Show the historic
def historic():
    mm.welcome_screen()
    print("\n\t\t\t\tGame Historic\n")

    # Print the historic
    for line in variables.historic_data[::-1]:
        print(line)

    input("\n\t\t\t\tPress Enter to continue")
    mm.main_menu()


def add_score():
    """
        Add the player score to the leaderboard
    """

    score_data = []
    # Score Equation : (((Score + Energy*10 + Hydratation*10 + Satiety*10) / ((Game duration + Movements * 5 + Actions * 5)) *10000)
    score_data.append(round((variables.game_data["score"] + variables.game_data["player"]["energy"] * 10 + variables.game_data["player"]["hydratation"] * 10 + variables.game_data["player"]["satiety"] * 10) / (variables.game_data["duration"] + variables.game_data["player"]["movements counter"]*5 + variables.game_data["player"]["actions counter"]*5)) * 1000)
    # Add name
    score_data.append(variables.game_data["player"]["name"])
    # Add energy
    score_data.append(variables.game_data["player"]["energy"])
    # Add Hydratation
    score_data.append(variables.game_data["player"]["hydratation"])
    # Add Satiety
    score_data.append(variables.game_data["player"]["satiety"])
    # Add Movements
    score_data.append(variables.game_data["player"]["movements counter"])
    # Add Actions
    score_data.append(variables.game_data["player"]["actions counter"])
    # Get the current time
    score_data.append(variables.game_data["duration"])
    # The list can't be longuer than 10
    if len(variables.leaderboard_data) >= 10:
        # The list is longuer than 10, remove the first index
        variables.leaderboard_data.pop(9)
        # Add the current game
        variables.leaderboard_data.append(score_data)
        # Sort the list
        variables.leaderboard_data.sort(reverse=True)
    else:
        # Add the current game
        variables.leaderboard_data.append(score_data)
        # Sort the list
        variables.leaderboard_data.sort(reverse=True)



def add_historic(status, cause_of_death = None):
    """
        Add the player to the historic
    """

    # Get the current time
    time = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
    # Get the player name
    if status:
        # Player won
        game = "Won"
    else:
        # Player lost
        game = "Lost"
    # Create the string
    end_string = f"{time}    {variables.game_data['player']['name']}     {game}     Cause of death : {cause_of_death}"
    # The list can't be longuer than 10
    if len(variables.historic_data) >= 10:
        # The list is longuer than 10, remove the first index
        variables.historic_data.pop(0)
        # Add the current game
        variables.historic_data.append(end_string)
    else:
        # Add the current
        variables.historic_data.append(end_string)


# Save the historic
def save_historic():
    """
        Save the historic into JSON save file.
    """

    try:
        with open("C:/Users/PYTHON/Documents/GitHub/the-mysterious-island/save/historic.json", "w") as save_file:
            save_file.write(json.dumps(variables.historic_data, indent=4))
    except:
        pass


# Load the historic
def load_historic():
    """
        Load the historic from the JSON save file to the game_data variable.
    """

    try:
        with open("C:/Users/PYTHON/Documents/GitHub/the-mysterious-island/save/historic.json", "r") as load_file:
            variables.historic_data = json.loads(load_file.read())
    except:
        pass


# Save the leaderboard
def save_leaderboard():
    """
        Save the leaderboard into JSON save file.
    """

    try:
        with open("C:/Users/PYTHON/Documents/GitHub/the-mysterious-island/save/leaderboard.json", "w") as save_file:
            save_file.write(json.dumps(variables.leaderboard_data, indent= 4))
    except:
        pass


# Load the leaderboard
def load_leaderboard():
    """
        Load the leaderboard from the JSON save file to the game_data variable.
    """

    try:
        with open("C:/Users/PYTHON/Documents/GitHub/the-mysterious-island/save/leaderboard.json", "r") as load_file:
            variables.leaderboard_data = json.loads(load_file.read())
    except:
        pass

