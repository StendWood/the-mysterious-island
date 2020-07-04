# coding: utf-8

# Imports
import random
import toolbox as tb

# Other code
import map_admin
import variables

# Functions
# Show the welcome screen
def welcome_screen():
    """
        Simple welcome screen in ASCII art
    """

    # Clear the console
    tb.clear()
    # Welcome Ascii art
    print("▀█▀ █░█ █▀▀   █▀▄▀█ █▄█ █▀ ▀█▀ █▀▀ █▀█ █ █▀█ █░█ █▀   █ █▀ █░░ ▄▀█ █▄░█ █▀▄")
    print("░█░ █▀█ ██▄   █░▀░█ ░█░ ▄█ ░█░ ██▄ █▀▄ █ █▄█ █▄█ ▄█   █ ▄█ █▄▄ █▀█ █░▀█ █▄▀\n")

# Menu
def menu_chooser():
    """
        Let the player choose in the menu
    """

    print("\t\t\t1 - New Game")
    print("\t\t\t2 - Load Game")
    print("\t\t\t3 - Leaderboard")
    print("\t\t\t4 - Quit\n")
    player_choice = menu_choice()
    if player_choice == 1:
        # Start the game
        pass
    elif player_choice == 2:
        # Load a game if it exist
        pass
    elif player_choice == 3:
        # Show the leaderboard
        pass
    else:
        # Quit the game
        pass

# Player menu choice
def menu_choice():
    """
        Process the player choice
    """

    # Valid string
    valid = "1234"
    # Ask player choice
    choice = input("\t\tChoose what you want to do : ")
    while not choice.isdigit() or choice not in valid :
        # Player choice is not a digit or not in valid
        choice = input("\t\tChoose from 1 - 4 : ")
    return choice

# Call the main menu
def main_menu():
    """
        Launch the main menu
    """

    # ASCII Art for the game
    welcome_screen()
