# coding: utf-8

# Imports
import random


# Other code
import main_menu as mm
import map_admin as ma
import variables

# Function
# Game flow
def adventure():
    """
        Principal gameflow
    """
    
    # Show the main menu
    mm.main_menu()
    mm.menu_chooser()
    # ma.new_map()
    # ma.map_printer()

if __name__ == "__main__":
    adventure()
