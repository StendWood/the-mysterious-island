# coding: utf-8

# Imports

# Extra code
import variables
import toolbox as tb
import main_menu as mm
import map_admin as ma
import os
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
    # Delete the previous files
    # os.remove("C:/Users/PYTHON/Documents/GitHub/the-mysterious-island/map/saved_map.txt")
    # Save the map
    ma.save_map()

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
                                    "item_1" : "",
                                    "item_2" : "",
                                    "item_3" : "",
                                    "item_4" : "",
                                    "item_5" : "",
                                    "item_6" : "",
                                    "item_7" : "",
                                    "item_8" : "",
                                    "item_9" : "",
                                    "item_10" : "",
                                }

}