# coding: utf-8

# Imports
import sys

# Extra code
import main_menu as mm
import map_admin as ma
import toolbox as tb
import game_data as gdat
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
        player_sleep()
        ma.map_printer()
        player_actions("Actions Menu")
    else:
        print("You saved")
        sys.exit()

# Sleep
def player_sleep():
    """
        Let the player sleep for any time he wants
    """

    # Clear console and reprint the map
    ma.map_printer()
    # Ask how many hours
    sleep_time = input("\n\t\tHow many hours do you want to sleep ? ")
    while not sleep_time.isdigit():
        sleep_time = input("\n\t\tHow many hours do you want to sleep ? (Choose a number) ")
    # Increment the actions score
    gdat.game_data["player"]["actions counter"]+=1
    # Energy regeneration
    gdat.game_data["player"]["energy"] += (6 * int(sleep_time))
    if gdat.game_data["player"]["energy"] > 100:
        # If energy over 100 set it back to 100
        gdat.game_data["player"]["energy"] = 100
    # Hydratation decay
    gdat.game_data["player"]["hydratation"] -= (2 * int(sleep_time))
    # Satiety decay
    gdat.game_data["player"]["satiety"] -= (1 * int(sleep_time))
    # Check if player is alive
    check_vitals()

# Check if any vitals is at 0
def check_vitals():
    """
        Check the player status, if any is < 0 the game stops and the player lose.
    """

    if gdat.game_data["player"]["energy"] <= 0:
        # Print the death art
        tb.death_art()
        # Energy reached 0
        print("\u001b[38;5;196mYou died of exhaustion...\u001b[0m")
        # Save score to leader board
        pass
        # Exit the programm
        sys.exit()
    elif gdat.game_data["player"]["hydratation"] <= 0:
        # Print the death art
        tb.death_art()
        # Hydratation reached 0
        print("\u001b[38;5;196mYou died of thirst... Even drinking your own sweat wasn't enough...\u001b[0m")
        # Save score to leader board
        pass
        # Exit the programm
        sys.exit()
    elif gdat.game_data["player"]["satiety"] <= 0:
        # Print the death art
        tb.death_art()
        # Satiety reached 0
        print("\u001b[38;5;196mYou died of hunger... You try to eat your fingers but it was too painful...\u001b[0m")
        # Save score to leader board
        pass
        # Exit the programm
        sys.exit()