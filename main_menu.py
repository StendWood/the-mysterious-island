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
    # Clear the console
    tb.clear()
    # Welcome Ascii art
    print("▀█▀ █░█ █▀▀   █▀▄▀█ █▄█ █▀ ▀█▀ █▀▀ █▀█ █ █▀█ █░█ █▀   █ █▀ █░░ ▄▀█ █▄░█ █▀▄")
    print("░█░ █▀█ ██▄   █░▀░█ ░█░ ▄█ ░█░ ██▄ █▀▄ █ █▄█ █▄█ ▄█   █ ▄█ █▄▄ █▀█ █░▀█ █▄▀\n")

# Menu
def menu_chooser():
    print("\t\t1 - New Game")
    print("\t\t2 - Load Game")
    print("\t\t3 - Leaderboard")
    print("\t\t4 - Quit")

# Call the main menu
def main_menu():
    # ASCII Art for the game
    welcome_screen()
