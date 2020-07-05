# coding: utf-8

# Imports


# Extra code
import main_menu as mm
import map_admin as ma
import sys

# FUNCTIONS
# Let the player choose his action
def player_actions():
    """
        Interface for the player actions
    """

    # Print the possible actions
    print("\n1 - Move     2- Check Inventory      3 - Sleep       4- Save Game (Quit Game)\n")
    player_choice = mm.menu_choice()
    # Use the player choice
    if player_choice == "1":
        ma.map_printer()
        print("You can move")
    elif player_choice == "2":
        print("Open the inventory windows")
        print("You check your inventory")
    elif player_choice == "3":
        print("You sleep for X hours")
    else:
        print("You saved")
        sys.exit()