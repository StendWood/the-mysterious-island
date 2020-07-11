# coding: utf-8

# Imports


# Extra code
import main_menu as mm
import map_admin as ma
import player_actions as pa
import toolbox as tb
import game_data as gdat
import variables
import inventory_items as inv

# FUNCTIONS
# Let the player chose where he wants to move
def player_movement(movement_name):
    """
        Interface for the player movements choices
    """
    
    # Clear the console and print the map
    ma.map_printer()
    # Print the possible actions
    print(f"\n1 - {ma.menu_data[movement_name][1]}     2- {ma.menu_data[movement_name][2]}      3 - {ma.menu_data[movement_name][3]}       4- {ma.menu_data[movement_name][4]}\n")
    # Ask the player choice
    player_choice = mm.menu_choice(movement_name)
    # Move depending on the player choice
    if player_choice == "1":
        # Move North
        move(variables.game_data["player"]["position"], player_choice)
    elif player_choice == "2":
        # Move West
        move(variables.game_data["player"]["position"], player_choice)
    elif player_choice == "3":
        # Move East
        move(variables.game_data["player"]["position"], player_choice)
    else:
        # Move south
        move(variables.game_data["player"]["position"], player_choice)


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
            variables.game_data["player"]["position"][0] -= 1
    elif directions == "2":
        # The player chose to move WEST
        # Save the symbol of the next position
        next_pos = variables.island_map[player_position[0]][player_position[1] - 1]
        if move_checker(next_pos):
            # Player can move there
            # Change player position
            variables.game_data["player"]["position"][1] -= 1
    elif directions == "3":
        # The player chose to move EAST
        # Save the symbol of the next position
        next_pos = variables.island_map[player_position[0]][player_position[1] + 1]
        if move_checker(next_pos):
            # Player can move there
            # Change player position
            variables.game_data["player"]["position"][1] += 1
    elif directions == "4":
        # The player chose to move SOUTH
        # Save the symbol of the next position
        next_pos = variables.island_map[player_position[0] + 1][player_position[1]]
        if move_checker(next_pos):
            # Player can move there
            # Change player position
            variables.game_data["player"]["position"][0] += 1
    # Clear the console and print the map
    ma.map_printer()
    # Print the move
    print(f"\n\t\t\tYou moved {ma.menu_data['Move Menu'][int(directions)][5::]}")
    # Check if the player is on a tile with an event
    tile_checker()


# Check player movement
def move_checker(next_pos):
    """
        Check if the player can move there by searching in map_tiles data
    """

    if ma.map_tiles[next_pos][1] == True:
        # The player can move on the next position
        # Increment the movement score
        variables.game_data["player"]["movements counter"]+=1
        # Energy decay
        variables.game_data["player"]["energy"]-=3
        # Hydratation decay
        variables.game_data["player"]["hydratation"]-=2
        # Satiety decay
        variables.game_data["player"]["satiety"]-=2
        # Check if player is alive after the move
        pa.check_vitals()
        # Validate the move
        return True


# Check where the player stands
def tile_checker():
    """
        Check the tile where the player is standing
    """

    # Check for the mysterious places tiles
    if variables.game_data["player"]["position"] in ma.map_tiles["φ"][4]:
        # The player position is on a challenge
        if variables.game_data["player"]["position"] == ma.map_tiles["φ"][4][0]:
            # Launch the first challenge
            tb.clear()
            print("You entered the first Challenge")
        if variables.game_data["player"]["position"] == ma.map_tiles["φ"][4][1]:
            # Launch the second challenge
            tb.clear()
            print("You entered the second Challenge")
        if variables.game_data["player"]["position"] == ma.map_tiles["φ"][4][2]:
            # Launch the third challenge
            tb.clear()
            print("You entered the third Challenge")
    else:
        # The player is on an item stash
        for key in variables.game_data["Item stash"]:
            # Check the first key layer
            for key_2 in variables.game_data["Item stash"][key]:
                # Iterate second key layer
                if variables.game_data["Item stash"][key][key_2] == variables.game_data["player"]["position"]:
                    # Extract the item name if the position is the one
                    item_name = variables.game_data["Item stash"][key]["items"]
                    # Clear console
                    tb.clear()
                    # # Print the stash with the item right item name
                    inv.show_stash(key, key_2, item_name)
        # Let the player choose again
        pa.player_actions("Actions Menu")