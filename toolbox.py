# coding: utf-8

# Imports
import os
import sys

# Extra code
import variables
import toolbox as tb
import main_menu as mm

#FUNCTIONS
# Clear the console for sexier print
def clear():
    """
        This function clears the console depending on OS
    """

    if "win" in sys.platform.lower():
        os.system("cls")
    elif "linux" in sys.platform.lower():
        os.system("clear")

def ask_player_name():
    """
        Ask the name of the player
    """

    # Clear the console
    mm.welcome_screen()
    # Ask the player name
    variables.player_name = input("What's you name fellow adventurer ? ")
    while variables.player_name == "":
        # If the player name is empty ask again
        variables.player_name = input("Lost your tongue ? ")

# Rules and story
def rules_stories():
    """
        Print a personalized story and the rules
    """

    # Main the game title
    mm.welcome_screen()
    # Print the story
    print("You wake up on a beach, not sure where. The ship is gone but at least you have all your equipments.")
    print("You look inside your backpack and find an old and wet parchment.\n\n")
    print(f"\tWelcome \u001b[1m\u001b[83m{variables.player_name}\u001b[0m,\n")    # Bold text \033[1m
    print(f"\tYou lost your way ? Do not worry, what the ocean takes, this island can give.\n")
    print(f"\tYou'll need to find your way to three \033[91mMysterious Places\033[00m.")
    print("\tThree keys you must find and win : ")
    print("\t\t\t\tthe \u001b[38;5;136mBronze Key\u001b[0m,")   # Bronze colored text \u001b[38;5;136m
    print("\t\t\t\tthe \u001b[38;5;250mSilver Key\u001b[0m,")   # Silver colored text \u001b[38;5;250m
    print("\t\t\t\tthe \u001b[38;5;220mGolden Key\u001b[0m\n")  # Gold colored text \u001b[38;5;220m
    print("\tIn your quest do not neglect yourself, you'll need to \u001b[38;5;15mSLEEP\u001b[0m, \u001b[38;5;118mEAT\u001b[0m and \u001b[38;5;75mDRINK\u001b[0m.")
    print("\tOr you'll \u001b[38;5;196mDIE\u001b[0m.")  # Red colored text \u001b[38;5;196m
    print("\tEvery step will drain your \u001b[38;5;15mENERGY\u001b[0m, \u001b[38;5;118mSATIETY\u001b[0m and \u001b[38;5;75mHYDRATATION\u001b[0m.")
    print("\tUse your wits to overcome the challenges ahead.\n")
    print("\tI wish you good luck.\n")
    # Let the player continue
    input("\t\t\t\t\tPress Enter to continue")