# coding: utf-8

# Imports
import sys

# Extra code
import game_data as gdat
import leaderboard as lb
import map_admin as ma
import toolbox as tb

# FUNCTIONS
# Show the welcome screen
def welcome_screen():
    """
        Simple welcome screen in ASCII art
    """

    # Clear the console
    tb.clear()
    # Welcome Ascii art
    print("\n ▀█▀ █░█ █▀▀   █▀▄▀█ █▄█ █▀ ▀█▀ █▀▀ █▀█ █ █▀█ █░█ █▀   █ █▀ █░░ ▄▀█ █▄░█ █▀▄")
    print(" ░█░ █▀█ ██▄   █░▀░█ ░█░ ▄█ ░█░ ██▄ █▀▄ █ █▄█ █▄█ ▄█   █ ▄█ █▄▄ █▀█ █░▀█ █▄▀\n")

# Menu
def main_menu_chooser():
    """
        Let the player choose in the menu
    """

    # Print the menu
    print("\t\t\t1 - New Game")
    print("\t\t\t2 - Load Game")
    print("\t\t\t3 - Leaderboard")
    print("\t\t\t4 - Historic")
    print("\t\t\t5 - Quit\n")

    # Load the historic
    lb.load_historic()
    # Load the leaderboard
    lb.load_leaderboard()

    # Check the player choice
    player_choice = menu_choice("Main Menu")
    if player_choice == "1":
        # Start the game
        gdat.new_game()
    elif player_choice == "2":
        # Load a game if it exist
        gdat.load_game()
    elif player_choice == "3":
        # Show the leaderboard
        lb.leaderboard()
    elif player_choice == "4":
        # Show the historic
        lb.historic()
    else:
        # Quit the game
        sys.exit()

# Player menu choice
def menu_choice(menu_name):
    """
        Process the player choice
    """

    # Valid string
    valid = ma.menu_data[menu_name][0]
    # Ask player choice
    choice = input("\t\tChoose what you want to do : ")
    while not choice.isdigit() or choice not in valid :
        # Player choice is not a digit or not in valid
        choice = input(f"\t\tChoose from {ma.menu_data[menu_name][0][0]} - {ma.menu_data[menu_name][0][-1]} : ")
    return choice

# Call the main menu
def main_menu():
    """
        Launch the main menu
    """

    # ASCII Art for the game
    welcome_screen()
    # Main menu
    main_menu_chooser()
