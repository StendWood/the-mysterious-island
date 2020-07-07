# coding: utf-8

# Imports
import variables
import toolbox as tb
import game_data as gdat

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
    # Initialize the counters and status
    status_counter()

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
    # Initialize the counters and status from the save file
    status_counter()

# Print the map for the player
def map_printer():
    """
        Clear the console and print the map
    """

    # Console clear
    tb.clear()
    # Status and counter refresh
    status_counter()
    # Print map
    for line in variables.island_map:
        print("".join(line))

# Initialize the counters
def status_counter():
    """
        Initialize the status and counters after the map is loaded and the saved data (if any) is loaded
    """

    # Movements counter
    variables.island_map[25][87] = str(gdat.game_data["player"]["movements counter"])
    # Actions counter
    variables.island_map[26][85] = str(gdat.game_data["player"]["actions counter"])
    # Energy Status
    variables.island_map[28][84] = str(gdat.game_data["player"]["energy"])
    # Hydratation status
    variables.island_map[29][89] = str(gdat.game_data["player"]["hydratation"])
    # Satiety status
    variables.island_map[30][85] = str(gdat.game_data["player"]["satiety"])

# Skull door
def map_reveal():
    """
        Reveal the Skull Door and let the player pass through
    """
    # Si nombre de keys = 3
    variables.island_map[1][21] = "∩"
    variables.island_map[2][96] = "Skull Door"


# MAP DATA
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