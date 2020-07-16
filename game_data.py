# coding: utf-8

# Imports
import json
import os
from time import sleep
import time

# Extra code
import variables
import toolbox as tb
import main_menu as mm
import map_admin as ma
import leaderboard as lb

# FUNCTIONS
# Player chose New Game in the main menu
def new_game():
    """
        Start a new game
    """

    # Get the starting time
    variables.time_data["start time"] = round(time.time())
    # Reprint the welcome screen
    mm.welcome_screen()
    # Adk player name
    tb.ask_player_name()
    # Print the rules and stories after asking for player name
    tb.rules_stories()
    # Load the base_map.txt
    ma.new_map()


# Player chose Load Game in the main menu
def load_game():
    # Check if the save file exist at that location
    if os.path.isfile("C:/Users/PYTHON/Documents/GitHub/the-mysterious-island/maps/saved_map.txt") and os.path.isfile("C:/Users/PYTHON/Documents/GitHub/the-mysterious-island/save/data_save.json"):
        # Save file exist
        # Load saved map
        ma.saved_map()
        # Load Saved data
        load_data()
        # Load the historic
        lb.load_historic()
        # Get the starting time
        variables.time_data["start time"] = round(time.time())
    else:
        # Save fil doesn't exist
        print("\n\t\t\tNo save file")
        # Wait for 3 seconds
        sleep(3)
        # Return to the menu
        mm.main_menu()


# Player chose Save Game in the player actions menu
def save_game():
    """
        Clean the save file and save the map and save the data
    """

    # Delete any save file
    save_cleaner()
    # Get the end time
    variables.time_data["end time"] = round(time.time())
    # Calculate the total duration
    variables.game_data["duration"] += tb.duration()
    # Save the map
    ma.save_map()
    # Save the data
    save_data()


# Remove any save files
def save_cleaner():
    """
        Delete the save file if any exist
    """

    try:
        # Delete the previous files if any
        os.remove("C:/Users/PYTHON/Documents/GitHub/the-mysterious-island/maps/saved_map.txt")
        os.remove("C:/Users/PYTHON/Documents/GitHub/the-mysterious-island/save/data_save.json")
    except:
        # No file to delete
        pass


# Save the data
def save_data():
    """
        Save the game_data DICT into JSON save file.
    """

    with open("C:/Users/PYTHON/Documents/GitHub/the-mysterious-island/save/data_save.json", "w") as save_file:
        save_file.write(json.dumps(variables.game_data, indent= 4))


# Load the data
def load_data():
    """
        Load the game data DICT from the JSON save file to the game_data variable.
    """

    with open("C:/Users/PYTHON/Documents/GitHub/the-mysterious-island/save/data_save.json", "r") as load_file:
        variables.game_data = json.loads(load_file.read())
