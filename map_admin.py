# coding: utf-8

# Imports
import variables
import toolbox as tb

# FUNCTIONS
# Load the a new map from the island_map.txt
def new_map():
    """
        Load the map from the base_map.txt
    """

    # Open the map file
    with open("C:/Users/PYTHON/Documents/GitHub/the-mysterious-island/map/base_map.txt", "r", encoding="utf-8") as map:
        # Put everyline in a list and remove the \n at the end
        temp_map = [line[:-1] for line in map]

        for line in temp_map:
        # Recreate a list
            x = [char for char in line]
            variables.island_map.append(x)

# Load the saved map when the player load a game
def saved_map():
    """
        Load the map from the saved_map.txt
    """

    # Open the map files
    with open("C:/Users/PYTHON/Documents/GitHub/the-mysterious-island/map/saved_map.txt", "r", encoding="utf-8") as map:
        # Put everyline in a list and remove the \n at the end
        temp_map = [line[:-1] for line in map]

        for line in temp_map:
        # Recreate a list
            x = [char for char in line]
            variables.island_map.append(x)

# Print the map for the player
def map_printer():
    """
        Clear the console and print the map
    """

    # Console clear
    tb.clear()
    # Print map
    for line in variables.island_map:
        print("".join(line))


def map_reveal():
    """
        Reveal the Skull Door and let the player pass through
    """
    # Si nombre de keys = 3
    variables.island_map[1][21] = "∩"
    variables.island_map[2][96] = "Skull Door"