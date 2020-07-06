# coding: utf-8

# Imports
import sys

# Extra code
import main_menu as mm
import map_admin as ma
import variables
import player_move as pm

# FUNCTIONS
# Let the player choose his action
def player_actions(action_name):
    """
        Interface for the player actions
    """

    # Print the possible actions
    print(f"\n1 - {variables.menu_data[action_name][1]}     2- {variables.menu_data[action_name][2]}      3 - {variables.menu_data[action_name][3]}       4- {variables.menu_data[action_name][4]}\n")
    player_choice = mm.menu_choice(action_name)
    # Use the player choice
    if player_choice == "1":
        pm.player_movement("Move Menu")
        # Check the tile
    elif player_choice == "2":
        print("Open the inventory windows")
        print("You check your inventory")
    elif player_choice == "3":
        print("You sleep for X hours")
    else:
        print("You saved")
        sys.exit()