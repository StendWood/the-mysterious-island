# coding: utf-8

# Imports
from time import sleep

# Extra code
import variables
import toolbox as tb
import inventory_items as inv

# FUNCTIONS
# Load the a new map from the island_map.txt
def new_map():
    """
        Load the map from the base_map.txt
    """

    # Open the map file
    with open("C:/Users/PYTHON/Documents/GitHub/the-mysterious-island/maps/base_map.txt", "r", encoding="utf-8") as map:
        # Put everyline in a list and remove the \n at the end
        temp_map = [line for line in map]

        for line in temp_map:
        # Recreate a list
            x = [char for char in line]
            variables.island_map.append(x)

    # Initialize the counters and status
    status_counter_init()
    # Populate the items stashes
    inv.random_stashes()

# Load the saved map when the player load a game
def saved_map():
    """
        Load the map from the saved_map.txt
    """

    # Open the map files
    with open("C:/Users/PYTHON/Documents/GitHub/the-mysterious-island/maps/saved_map.txt", "r", encoding="utf-8") as map:
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
    # Set the Y axis to 0
    y = 0
    for line in variables.island_map:
        # Take the first item of the list
        # Set the X axis to 0
        x = 0
        for symbol in line:
            # Extract the first symbol of the list
            if symbol in map_tiles:
                # The symbol is a map tile
                if variables.game_data["player"]["position"][0] == y and variables.game_data["player"]["position"][1] == x:
                    # The position to print is equal to the position of the player
                    # Print the player in place of the symbol
                    print(f"{map_tiles['Ø'][2]}{'Ø'}{map_tiles['Ø'][3]}", end = "")
                    x+=1
                else:
                    # Print the symbol with a color
                    print(f"{map_tiles[symbol][2]}{symbol}{map_tiles[symbol][3]}", end = "")
                    x+=1
            else:
                # Print the normal symbol
                print(symbol, end = "")
                x+=1
        y+=1

# Inventory Map use
def inventory_map_printer():
    for line in variables.island_map:
        for symbol in line:
            if symbol == "φ" or symbol == "¤":
                print(" ", end = "")
            else:
                print(symbol, end = "")

# Initialize the counters
def status_counter_init():
    """
        Initialize the status and counters after the map is loaded and the saved data (if any) is loaded
    """

    # Movements counter
    variables.island_map[25][87] = str(variables.game_data["player"]["movements counter"])
    # Actions counter
    variables.island_map[26][85] = str(variables.game_data["player"]["actions counter"])
    # Energy Status
    variables.island_map[28][84] = str(variables.game_data["player"]["energy"])
    # Hydratation status
    variables.island_map[29][89] = str(variables.game_data["player"]["hydratation"])
    # Satiety status
    variables.island_map[30][85] = str(variables.game_data["player"]["satiety"])

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

    if all(variables.game_data['inventory']['keychain']):
        # Player has all the keys
        # Reveal the end game door tile
        variables.island_map[1][21] = "∩"
        # Change the ∩ info in the status print
        variables.island_map[2][96] = "Skull Door"
        tb.clear()
        # 3 keys ASCII Art and story
        print("      \u001b[38;5;136m_   ")
        print("     \u001b[38;5;136m( )   \u001b[38;5;220m_\u001b[0m")
        print("      \u001b[38;5;136mT   \u001b[38;5;220m( )\u001b[0m            As you reach for the last key,")
        print(" \u001b[38;5;252m_    \u001b[38;5;136m|    \u001b[38;5;220mT\u001b[0m             you hear a noise in the distance,")
        print("\u001b[38;5;252m( )   \u001b[38;5;136m|E   \u001b[38;5;220m|\u001b[0m             the ground is shaking,")
        print(" \u001b[38;5;252mT         \u001b[38;5;220m|E\u001b[0m            something big is in motion...")
        print(" \u001b[38;5;252m|")
        print(" \u001b[38;5;252m|E\u001b[0m")
        sleep(5)

# Save the map
def save_map():
    """
        Save the map when the player save his game
    """
    # Reset the counters and status before saving the map
    status_counter_reset()
    # Modify the save file
    with open("C:/Users/PYTHON/Documents/GitHub/the-mysterious-island/maps/saved_map.txt", "w+", encoding="utf-8") as map:
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
                                "\u001b[38;5;102m",  # 2 - Color of the symbol
                                "\u001b[0m",         # 3 - Reset color
                                "\n\t\tYou can't move past a mountain !"    # 4 Error message
                            ],
                "↑" :
                            [
                                "Trees",    # 0 - Name
                                False,  # 1 - If player can pass through
                                "\u001b[38;5;64m",  # 2 - Color of the symbol
                                "\u001b[0m",         # 3 - Reset color
                                "\n\t\t A tree is blocking your path !"    # 4 Error message
                            ],
                "|" :
                            [
                                "Shoreline",    # 0 - Name
                                False,  # 1 - If player can pass through
                                "",  # 2 - Color of the symbol
                                "",         # 3 - Reset color
                                "\n\t\tThe current is too much in the ocean !"    # 4 Error message
                            ],
                "_" :
                            [
                                "Shoreline",    # 0 - Name
                                False,  # 1 - If player can pass through
                                "",  # 2 - Color of the symbol
                                "",         # 3 - Reset color
                                "\n\t\tThe current is too much in the ocean !"    # 4 Error message
                            ],
                "▓" :
                            [
                                "Sea",    # 0 - Name
                                False,  # 1 - If player can pass through
                                "\u001b[38;5;20m",  # 2 - Color of the symbol
                                "\u001b[0m",         # 3 - Reset color
                                "\n\t\tThe current is too much in the ocean !"    # 4 Error message
                            ],
                "~" :
                            [
                                "River",    # 0 - Name
                                False,  # 1 - If player can pass through
                                "\u001b[38;5;117m",  # 2 - Color of the symbol
                                "\u001b[0m",         # 3 - Reset color
                                "\n\t\tThe water is too cold ! Brrrrrrr !"        # 4 Error message
                            ],
                "φ" :
                            [
                                "Mysterious Places",    # 0 - Name
                                True,  # 1 - If player can pass through
                                "\u001b[38;5;88m",  # 2 - Color of the symbol
                                "\u001b[0m",         # 3 - Reset color
                                (      # 4 - Position tuple
                                    [4, 64],   # 0 - Position of the first challenge
                                    [27, 42],    # 1 - Position of the second challenge
                                    [24, 8]# 2 - Position of the third challenge
                                ),
                            ],
                "√" :
                            [
                                "Mysteries Solved",    # 0 - Symbol
                                True,  # 1 - If player can pass through
                                "\u001b[38;5;118m",  # 2 - Color of the symbol
                                "\u001b[0m",         # 3 - Reset color
                            ],
                "¤" :
                            [
                                "Items stashes",    # 0 - Symbol
                                True,  # 1 - If player can pass through
                                "\u001b[38;5;128m",  # 2 - Color of the symbol
                                "\u001b[0m",         # 3 - Reset color
                                # 4 -Item stahes positions
                                [
                                    
                                ],
                                # 5 - Item drops
                                [

                                ]
                            ],
                "∩" :
                            [
                                "Skull Door",    # 0 - Symbol
                                True,  # 1 - If player can pass through
                                "\u001b[38;5;255m",  # 2 - Color of the symbol
                                "\u001b[0m",         # 3 - Reset color
                                (      # 4 - Position tuple
                                    [1, 21]
                                )
                            ],
                " " :
                            [
                                "Dirt",    # 0 - Symbol
                                True,  # 1 - If player can pass through
                                "",  # 2 - Color of the symbol
                                "",         # 3 - Reset color
                            ],
                "░" :
                            [
                                "Sand",    # 0 - Symbol
                                True,  # 1 - If player can pass through
                                "\u001b[38;5;11m",  # 2 - Color of the symbol
                                "\u001b[0m",         # 3 - Reset color
                            ],
                "Ø" :
                            [
                                "Player",    # 0 - Symbol
                                True,  # 1 - If player can pass through
                                "\u001b[38;5;226m",  # 2 - Color of the symbol
                                "\u001b[0m",         # 3 - Reset color
                            ],
}

# Menu actions
menu_data = {
                "Main Menu" : # Menu Name
                                [
                                    "12345"      # Possible inputs
                                ],
                "Actions Menu" :
                                [
                                    ["1","2","3","4"],     # Possible inputs
                                    "Move",     # First action
                                    "Open Inventory",   # Second action
                                    "Sleep",            # Third action
                                    "Save (Quit Game)"  # Fourth action
                                ],
                "Move Menu" :
                                [
                                    ["1","2","3","4"],
                                    "Move NORTH",
                                    "Move WEST",
                                    "Move EAST",
                                    "Move SOUTH"
                                ],
                "Item Actions" :
                                [
                                    ["1","2","3"],
                                    "Use",
                                    "Drop",
                                    "Refill",
                                    "Take",
                                ]
}