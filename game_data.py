# coding: utf-8

# Imports
import json

# Extra code
import os
import variables
import toolbox as tb
import main_menu as mm
import map_admin as ma
from time import sleep

# FUNCTIONS
# Player chose New Game in the main menu
def new_game():
    """
        Start a new game
    """

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
    if os.path.isfile("C:/Users/PYTHON/Documents/GitHub/the-mysterious-island/map/saved_map.txt"):
        # Save file exist
        # Load saved map
        ma.saved_map()
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
    # Save the map
    ma.save_map()
    # Save the data

def save_cleaner():
    """
        Delete the save file if any exist
    """

    try:
        # Delete the previous files if any
        os.remove("C:/Users/PYTHON/Documents/GitHub/the-mysterious-island/map/saved_map.txt")
    except:
        # No file to delete
        pass

# Game Data
game_data = {
                "player" : 
                            {
                                "name" : "",
                                "position" : [26, 58],
                                "energy" : 100,
                                "hydratation" : 100,
                                "satiety" : 100,
                                "movements counter" : 0,
                                "actions counter" : 0,
                            },
                "inventory" :
                                {
                                    "keychain" :
                                                [
                                                    False, # 0 - Bronze Key
                                                    False, # 1 - Silver Key
                                                    False  # 2 - Golden Key
                                                ],
                                    "item_0" : 
                                                {
                                                    "name" : "Water bottle",
                                                    "uses" : 5,     # Number of use
                                                    "use" : ["hydratation", 20],     # What actions the item do on use (+20 hydratation)
                                                },
                                    "item_1" : 
                                                {
                                                    "name" : "Knife",
                                                    "uses" : "∞",     # Number of use
                                                    "use" : ["hydratation", -5],     # What actions the item do on use (-5 hydratation)
                                                },
                                    "item_2" : {
                                                    "name" : "Map",
                                                    "uses" : "∞"
                                                },
                                    "item_3" : {
                                                    "name" : "Laptop",
                                                    "uses" : 1,     # Number of use
                                                    "use" : ["energy", 5],     # What actions the item do on use (+5 energy)
                                                },
                                    "item_4" : {
                                                    "name" : "Solar panel",
                                                    "uses" : 1,     # Number of use
                                                    "use" : ["energy", 5],     # What actions the item do on use (+5 energy)
                                                },
                                    "item_5" : {
                                                    "name" : "Avocado",
                                                    "uses" : 1,     # Number of use
                                                    "use" : ["satiety", 10],     # What actions the item do on use
                                                },
                                    "item_6" : {
                                                    "name" : None,
                                                    "uses" : None,     # Number of use
                                                    "use" : None,     # What actions the item do on use
                                                },
                                    "item_7" : {
                                                    "name" : None,
                                                    "uses" : None,     # Number of use
                                                    "use" : None,     # What actions the item do on use
                                                },
                                    "item_8" : {
                                                    "name" : None,
                                                    "uses" : None,     # Number of use
                                                    "use" : None,     # What actions the item do on use
                                                },
                                    "item_9" : {
                                                    "name" : None,
                                                    "uses" : None,     # Number of use
                                                    "use" : None,     # What actions the item do on use
                                                },
                                }
}