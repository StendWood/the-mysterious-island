# coding: utf-8

# Imports
import sys
import time

# Extra code
import main_menu as mm
import map_admin as ma
import toolbox as tb
import game_data as gdat
import variables
import player_move as pm
import inventory_items as inv
import leaderboard as lb

# FUNCTIONS
# Let the player choose his action
def player_actions(action_name):
    """
        Interface for the player actions
    """

    # Print the possible actions
    print(f"\n1 - {ma.menu_data[action_name][1]}     2- {ma.menu_data[action_name][2]}      3 - {ma.menu_data[action_name][3]}       4- {ma.menu_data[action_name][4]}\n")
    # Ask what the player wants to do
    player_choice = mm.menu_choice(action_name)
    # Use the player choice
    if player_choice == "1":
        # Player input is 1
        pm.player_movement("Move Menu")
    elif player_choice == "2":
        # Player input is 2
        # Clear the console
        tb.clear()
        # Let the player choose what he wants to do
        inv.inventory_choices()
    elif player_choice == "3":
        # Player input is 3
        # Launch the sleep function and ask a number the player wants to sleep
        player_sleep()
        # Print the map
        ma.map_printer()
        # Return to the actions menu
        player_actions("Actions Menu")
    else:
        # The player choosed to save and thus quit the game
        gdat.save_game()
        # Exit the programm
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
    variables.game_data["player"]["actions counter"]+=1
    # Energy regeneration
    variables.game_data["player"]["energy"] += (6 * int(sleep_time))
    if variables.game_data["player"]["energy"] > variables.game_data["player"]["max energy"]:
        # If energy over 100 set it back to 100
        variables.game_data["player"]["energy"] = variables.game_data["player"]["max energy"]
    # Hydratation decay
    variables.game_data["player"]["hydratation"] -= (2 * int(sleep_time))
    # Satiety decay
    variables.game_data["player"]["satiety"] -= (1 * int(sleep_time))
    # Wait for X hours
    time.sleep(3)
    # Check if player is alive
    check_vitals()


# Check if any vitals is at 0
def check_vitals():
    """
        Check the player status, if any is < 0 the game stops and the player lose.
    """

    if variables.game_data["player"]["energy"] <= 0:
        # Save in the historic
        lb.add_historic(False, "Exhaustion")
        lb.save_historic()
        # Print the death art
        tb.death_art()
        # Energy reached 0
        print("\u001b[38;5;196mYou died of exhaustion...\u001b[0m")
        # Exit the programm
        sys.exit()
    elif variables.game_data["player"]["hydratation"] <= 0:
        # Save in the historic
        lb.add_historic(False, "Dehydratation")
        lb.save_historic()
        # Print the death art
        tb.death_art()
        # Hydratation reached 0
        print("\u001b[38;5;196mYou died of thirst... Even drinking your own sweat wasn't enough...\u001b[0m")
        # Exit the programm
        sys.exit()
    elif variables.game_data["player"]["satiety"] <= 0:
        # Save in the historic
        lb.add_historic(False, "Starvation")
        lb.save_historic()
        # Print the death art
        tb.death_art()
        # Satiety reached 0
        print("\u001b[38;5;196mYou died of hunger... You try to eat your fingers but it was too painful...\u001b[0m")
        # Exit the programm
        sys.exit()