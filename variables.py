# coding: utf-8

# Imports

# Variables Declaration
# Map
island_map = []


# Player
player_name = ""
player_position = [26, 58]    #[ y, x]

# Menu actions
menu_data = {
                "Main Menu" : # Menu Name
                                [
                                    "1234"      # Possible inputs
                                ],
                "Actions Menu" :
                                [
                                    "1234",     # Possible inputs
                                    "Move",     # First action
                                    "Open Inventory",   # Second action
                                    "Sleep",            # Third action
                                    "Save (Quit Game)"  # Fourth action
                                ],
                "Move Menu" :
                                [
                                    "1234",
                                    "Move NORTH ↑",
                                    "Move WEST  ←-",
                                    "Move EAST  -→",
                                    "Move SOUTH ↓"
                                ],
                "Items Selection" :
                                [
                                    "123456789",

                                ]
}