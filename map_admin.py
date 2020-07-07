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
        temp_map = [line for line in map]

        for line in temp_map:
        # Recreate a list
            x = [char for char in line]
            variables.island_map.append(x)
    # Initialize the counters and status
    status_counter_init()

# Load the saved map when the player load a game
def saved_map():
    """
        Load the map from the saved_map.txt
    """

    # Open the map files
    with open("C:/Users/PYTHON/Documents/GitHub/the-mysterious-island/map/saved_map.txt", "r", encoding="utf-8") as map:
        # Put everyline in a list and remove the \n at the end
        temp_map = [line for line in map]

        for line in temp_map:
        # Recreate a list
            x = [char for char in line]
            variables.island_map.append(x)

    # Initialize the counters and status from the save file
    status_counter_init()

# Print the map for the player
def map_printer():
    """
        Clear the console and print the map (apply color)
    """

    # Console clear
    tb.clear()
    # Status and counter refresh
    status_counter_init()
    # Print map
    for line in variables.island_map:
        # Take the first item of the list
        for character in line:
            # Extract the first character of the list
            if character in map_tiles:
                # Check if the character is a tile
                # Print the character with a color
                print(f"{map_tiles[character][2]}{character}{map_tiles[character][3]}", end = "")
            else:
                # Print the normal character
                print(character, end = "")

# Initialize the counters
def status_counter_init():
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

# Reset the counters and status after a load
def status_counter_reset():
    """
        Reset to " " the counters and status before the map save
    """
    # Reset Movements counter
    variables.island_map[25][87] = " "
    # Reset Actions counter
    variables.island_map[26][85] = " "
    # Reset Energy Status
    variables.island_map[28][84] = " "
    # Reset Hydratation status
    variables.island_map[29][89] = " "
    # Reset Satiety status
    variables.island_map[30][85] = " "

# Skull door
def map_reveal():
    """
        Reveal the Skull Door and let the player pass through
    """
    # Si nombre de keys = 3
    variables.island_map[1][21] = "∩"
    variables.island_map[2][96] = "Skull Door"

# Save the map
def save_map():
    # Reset the counters and status before saving the map
    status_counter_reset()
    # Modify the save file
    with open("C:/Users/PYTHON/Documents/GitHub/the-mysterious-island/map/saved_map.txt", "w", encoding="utf-8") as map:
        for line in variables.island_map:
            line = "".join(line)
            map.writelines(line)


# MAP DATA
# Map Tiles
map_tiles = {
                "▲" :
                            [
                                "Mountain",    #  0 - Name
                                False,  # 1 - If player can pass through
                                "\u001b[38;5;102m",  # 2 - Color of the character
                                "\u001b[0m"         # 3 - Reset color
                            ],
                "↑" :
                            [
                                "Trees",    # 0 - Name
                                False,  # 1 - If player can pass through
                                "\u001b[38;5;64m",  # 2 - Color of the character
                                "\u001b[0m"         # 3 - Reset color
                            ],
                "|" :
                            [
                                "Shoreline",    # 0 - Name
                                False,  # 1 - If player can pass through
                                "",  # 2 - Color of the character
                                "",         # 3 - Reset color
                            ],
                "_" :
                            [
                                "Shoreline",    # 0 - Name
                                False,  # 1 - If player can pass through
                                "",  # 2 - Color of the character
                                ""         # 3 - Reset color
                            ],
                "▓" :
                            [
                                "Sea",    # 0 - Name
                                False,  # 1 - If player can pass through
                                "\u001b[38;5;20m",  # 2 - Color of the character
                                "\u001b[0m"         # 3 - Reset color
                            ],
                "~" :
                            [
                                "River",    # 0 - Name
                                False,  # 1 - If player can pass through
                                "\u001b[38;5;117m",  # 2 - Color of the character
                                "\u001b[0m"         # 3 - Reset color
                            ],
                "φ" :
                            [
                                "Mysterious Places",    # 0 - Name
                                True,  # 1 - If player can pass through
                                "\u001b[38;5;88m",  # 2 - Color of the character
                                "\u001b[0m",         # 3 - Reset color
                                (      # 4 - Position tuple
                                    [27, 42],   # 0 - Position of the first challenge
                                    [24, 8],    # 1 - Position of the second challenge
                                    [5, 64]     # 2 - Position of the third challenge
                                ),
                            ],
                "√" :
                            [
                                "Mysteries Solved",    # 0 - Symbol
                                True,  # 1 - If player can pass through
                                "",  # 2 - Color of the character
                                "",         # 3 - Reset color
                            ],
                "¤" :
                            [
                                "Items stashes",    # 0 - Symbol
                                True,  # 1 - If player can pass through
                                "\u001b[38;5;128m",  # 2 - Color of the character
                                "\u001b[0m",         # 3 - Reset color
                            ],
                "∩" :
                            [
                                "Skull Door",    # 0 - Symbol
                                True,  # 1 - If player can pass through
                                "\u001b[38;5;255m",  # 2 - Color of the character
                                "\u001b[0m",         # 3 - Reset color
                            ],
                " " :
                            [
                                "Sand or Dirt",    # 0 - Symbol
                                True,  # 1 - If player can pass through
                                "",  # 2 - Color of the character
                                "",         # 3 - Reset color
                            ],
                "Ø" :
                            [
                                "Player",    # 0 - Symbol
                                True,  # 1 - If player can pass through
                                "",  # 2 - Color of the character
                                "",         # 3 - Reset color
                            ],
}