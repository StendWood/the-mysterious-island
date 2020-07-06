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

# Map Tiles
map_tiles = {
                "▲" :
                            [
                                "Mountain",    #  0 - Name
                                False,  # 1 - If player can pass through
                            ],
                "↑" :
                            [
                                "Trees",    # 0 - Name
                                False,  # 1 - If player can pass through
                            ],
                "|" :
                            [
                                "Shoreline",    # 0 - Name
                                False,  # 1 - If player can pass through
                            ],
                "_" :
                            [
                                "Shoreline",    # 0 - Name
                                False,  # 1 - If player can pass through
                            ],
                "░" :
                            [
                                "Sea",    # 0 - Name
                                False,  # 1 - If player can pass through
                            ],
                "~" :
                            [
                                "River",    # 0 - Name
                                False,  # 1 - If player can pass through
                            ],
                "φ" :
                            [
                                "Mysterious Places",    # 0 - Name
                                True,  # 1 - If player can pass through
                                (      # 2 - Position tuple
                                    [27, 42],   # 0 - Position of the first challenge
                                    [24, 8],    # 1 - Position of the second challenge
                                    [5, 64]     # 2 - Position of the third challenge
                                )    
                            ],
                "√" :
                            [
                                "Mysteries Solved",    # 0 - Symbol
                                True,  # 1 - If player can pass through
                            ],
                "¤" :
                            [
                                "Items stashes",    # 0 - Symbol
                                True,  # 1 - If player can pass through
                            ],
                "∩" :
                            [
                                "Skull Door",    # 0 - Symbol
                                True,  # 1 - If player can pass through
                            ],
                " " :
                            [
                                "Sand or Dirt",    # 0 - Symbol
                                True,  # 1 - If player can pass through
                            ],
}

def map_reveal():
    """
        Reveal the Skull Door and let the player pass through
    """
    # Si nombre de keys = 3
    variables.island_map[1][21] = "∩"
    variables.island_map[2][96] = "Skull Door"