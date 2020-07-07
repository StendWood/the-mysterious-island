# coding: utf-8

# Imports

# Extra code
import variables
import main_menu as mm
import map_admin as ma
import player_actions as pa

# Function
# Game flow
def adventure():
    """
        Principal gameflow
    """
    
    # Show the main menu
    mm.main_menu()
    # Print the map after the main menu
    ma.map_printer()
    # Let the player move
    pa.player_actions("Actions Menu")

if __name__ == "__main__":
    adventure()