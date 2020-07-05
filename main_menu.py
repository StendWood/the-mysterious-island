# coding: utf-8

# Imports
import random
import toolbox as tb
import sys

# Extra code
import variables
import game_data as gdat
import leaderboard as lb

# FUNCTIONS
# Show the welcome screen
def welcome_screen():
    """
        Simple welcome screen in ASCII art
    """

    # Clear the console
    tb.clear()
    # Welcome Ascii art
    print("\n▀█▀ █░█ █▀▀   █▀▄▀█ █▄█ █▀ ▀█▀ █▀▀ █▀█ █ █▀█ █░█ █▀   █ █▀ █░░ ▄▀█ █▄░█ █▀▄")
    print("░█░ █▀█ ██▄   █░▀░█ ░█░ ▄█ ░█░ ██▄ █▀▄ █ █▄█ █▄█ ▄█   █ ▄█ █▄▄ █▀█ █░▀█ █▄▀\n")

# Menu
def main_menu_chooser():
    """
        Let the player choose in the menu
    """

    # Print the menu
    print("\t\t\t1 - New Game")
    print("\t\t\t2 - Load Game")
    print("\t\t\t3 - Leaderboard")
    print("\t\t\t4 - Quit\n")
    # Check the player choice
    player_choice = menu_choice()
    if player_choice == "1":
        # Start the game
        gdat.new_game()
    elif player_choice == "2":
        # Load a game if it exist
        gdat.load_game()
    elif player_choice == "3":
        # Show the leaderboard
        lb.leaderboard()
    else:
        # Quit the game
        sys.exit()

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
    # Main menu
    main_menu_chooser()
