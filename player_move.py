# coding: utf-8

# Imports


# Extra code
import main_menu as mm
import map_admin as ma
import player_actions as pa
import toolbox as tb
import variables


# FUNCTIONS
# Let the player chose where he wants to move
def player_movement(movement_name):
    """
        Interface for the player movements choices
    """
    
    ma.map_printer()
    # Print the possible actions
    print(f"\n1 - {variables.menu_data[movement_name][1]}     2- {variables.menu_data[movement_name][2]}      3 - {variables.menu_data[movement_name][3]}       4- {variables.menu_data[movement_name][4]}\n")
    player_choice = mm.menu_choice(movement_name)
    # Move depending on the player choice
    if player_choice == "1":
        # Move North
        move(variables.player_position, player_choice)
    elif player_choice == "2":
        # Move West
        move(variables.player_position, player_choice)
    elif player_choice == "3":
        # Move East
        move(variables.player_position, player_choice)
    else:
        # Move south
        move(variables.player_position, player_choice)

# Let the player move North
def move(player_position, directions):
    """
        Check if the player can move north and then move him
    """

    if directions == "1":
        # The player chose to move NORTH
        # Save the symbol of the next position
        next_pos = variables.island_map[player_position[0] - 1][player_position[1]]
        if move_checker(next_pos):
            # Player can move there
            # Change player position
            variables.player_position[0] -= 1
    elif directions == "2":
        # The player chose to move WEST
        # Save the symbol of the next position
        next_pos = variables.island_map[player_position[0]][player_position[1] - 1]
        if move_checker(next_pos):
            # Player can move there
            # Change player position
            variables.player_position[1] -= 1
    elif directions == "3":
        # The player chose to move EAST
        # Save the symbol of the next position
        next_pos = variables.island_map[player_position[0]][player_position[1] + 1]
        if move_checker(next_pos):
            # Player can move there
            # Change player position
            variables.player_position[1] += 1
    elif directions == "4":
        # The player chose to move SOUTH
        # Save the symbol of the next position
        next_pos = variables.island_map[player_position[0] + 1][player_position[1]]
        if move_checker(next_pos):
            # Player can move there
            # Change player position
            variables.player_position[0] += 1
    # Replace the tile where the player go
    variables.island_map[player_position[0]][player_position[1]] = "𓀠"
    # Check if the player is on a tile with an event
    tile_checker()

# Check player movement
def move_checker(next_pos):
    """
        Check if the player can move there byt searching in map_tiles data
    """

    if ma.map_tiles[next_pos][1] == True:
        # The player can move on the next position
        # Replace the tile where the player is
        variables.island_map[variables.player_position[0]][variables.player_position[1]] = " "
        # Validate the move
        return True

# Check where the player stands
def tile_checker():
    """
        Check the tile where the player is standing
    """

    # Check for the mysterious places tiles
    if variables.player_position in ma.map_tiles["φ"][2]:
        # The player position is on a challenge
        tb.clear()
        print("You entered a Challenge")
    else:
        # Clear the console and print the map
        ma.map_printer()
        # Let the player choose again
        pa.player_actions("Actions Menu")