# coding: utf-8

# Imports
import random
from time import sleep

# Extra code
import variables
import game_data as gdat
import main_menu as mm
import map_admin as ma
import toolbox as tb
import player_actions as pa

# FUNCTIONS
# Show the inventory
def inv_show():
    """
        Simply show the inventory and ask what the player wants to do
    """

    # Key checker
    bronze_key = "\u001b[38;5;196mX\u001b[0m"
    silver_key = "\u001b[38;5;196mX\u001b[0m"
    golden_key = "\u001b[38;5;196mX\u001b[0m"

    if variables.game_data['inventory']['keychain'][0]:
        # The player has the bronze key
        bronze_key = "\u001b[38;5;118m√\u001b[0m"
    if variables.game_data['inventory']['keychain'][1]:
        # The player has the silver key
        silver_key = "\u001b[38;5;118m√\u001b[0m"
    if variables.game_data['inventory']['keychain'][2]:
        # The player has the golden key
        golden_key = "\u001b[38;5;118m√\u001b[0m"
    
    tb.clear()
    # ASCII Art
    print("\u001b[38;5;255m     _....._")
    print(f"     ';-.--';'                                  \u001b[38;5;136mBronze Key\u001b[0m : {bronze_key}")
    print(f"\u001b[38;5;255m      )====(       _.---.._                     \u001b[38;5;252mSilver Key\u001b[0m : {silver_key}")
    print(f"\u001b[38;5;255m    .'      '.    ';-..--';                     \u001b[38;5;220mGolden Key\u001b[0m : {golden_key}")
    print("\u001b[38;5;255m   /::        \\    `)====(")
    print("  |::          :   /      '.")
    print("  \\::.        _.---_        \\")
    print("   '::_     _`---..-';       |")
    print("       `````  )=====(        /")
    print(f"            .'       '.   _.'                   \u001b[0mMovements :     {variables.game_data['player']['movements counter']}")
    print(f"\u001b[38;5;255m           /::         \\ `                      \u001b[0mActions :       {variables.game_data['player']['actions counter']}")
    print("\u001b[38;5;255m          |::           |")
    print(f"\u001b[38;5;255m          \\::.          /                       \u001b[38;5;11mEnergy\u001b[0m :        {variables.game_data['player']['energy']}")
    print(f"\u001b[38;5;255m           '::_      _.'                        \u001b[38;5;75mHydratation\u001b[0m :   {variables.game_data['player']['hydratation']}")
    print(f"\u001b[38;5;255m               ``````                           \u001b[38;5;118mSatiety\u001b[0m :       {variables.game_data['player']['satiety']}")
    # Print the inventory page
    print()
    # Clean the ivnentory from depleted items
    inventory_cleaner()
    item_uses = "▌"
    for key in variables.game_data["inventory"]:
        # Get the first key
        if "item" in key:
            if variables.game_data["inventory"][key]["name"] != None:
                # Name is not None
                if variables.game_data['inventory'][key]['uses'] == "∞":
                    print(f"{key[-1]} - {variables.game_data['inventory'][key]['name']} {variables.game_data['inventory'][key]['uses']}")
                else:
                    print(f"{key[-1]} - {variables.game_data['inventory'][key]['name']} {item_uses*int(variables.game_data['inventory'][key]['uses'])}")
                # item_number+=1
    # Quit the inventory and return to the map
    print("Q - Return to map")
    print()
    # return item_number


# Inventory item choices
def inventory_choices():
    """
        Show the inventory and let the player choose an item
    """

    # # Clean the ivnentory from depleted items
    inventory_cleaner()
    # Print the inventory and show save how many items are in the bag
    inv_show()
    # Ask for the player choice
    choice = input("\t\tChoose what you want to do : ").upper()
    # Choice is a digit and in valid
    if choice.capitalize() == "Q":
        # Choice is Q, return to map
        ma.map_printer()
        # Ask what the player wants to do
        pa.player_actions("Actions Menu")
    try:
        if variables.game_data['inventory'][f'item_{choice}']['name'] == None:
            # Player choice is not a digit or not in valid
            print(f"\t\tChoose from the item list or choose Q to go back to the map.")
            sleep(2)
            inventory_choices()
        else:
            # Refresh the screen
            inv_show()
            # Print the item chosed by the player
            print(f"\t\tYou chose the {variables.game_data['inventory'][f'item_{choice}']['name']}")
            # Save the item name
            item_name = f"{variables.game_data['inventory'][f'item_{choice}']['name']}"
            # Save the item number
            item_number = f"item_{choice}"
            # Ask what he wants to do with that item
            print(f"\n1 - {ma.menu_data['Item Actions'][1]}     2- {ma.menu_data['Item Actions'][2]}      3 - {ma.menu_data['Item Actions'][3]}\n")
            choice = mm.menu_choice("Item Actions")
    except KeyError:
        print(f"\t\tChoose from the item list or choose Q to go back to the map.")
        sleep(2)
        inventory_choices()
    
    # Refresh the screen
    inv_show()
    # The player choose
    if choice == "1":
        # Use the selected item if he can be used
        use_item(item_name, item_number)
    elif choice == "2":
        # Drop the selected item if it can be dropped
        drop_item(item_name, item_number)
    elif choice == "3":
        # Refill the item if it can be refilled
        refill_item(item_name)
    inventory_choices()
    # Player choice is not a digit or not in valid
    print(f"\t\tChoose from the item list or choose Q to go back to the map")
    sleep(2)
    inventory_choices()


# Use an item
def use_item(item_name, item_number):
    """
        Use the targeted item
    """

    # The player used the map
    if item_name == "Map":
        # Print the map without any special tiles
        ma.inventory_map_printer()
        # Add 1 action to the counter
        variables.game_data["player"]["actions counter"]+=1
        # Wait for 7 seconds
        sleep(5)
    # Check if the item is usable
    elif not items_data[item_name]["actions"]["use"]:
        # If the item actions use is False
        print(items_data[item_name]["actions"]["error message"])
    else:
        # If item is usable check for uses left
        if variables.game_data["inventory"][item_number]["uses"] == 0:
            # No uses left, print the error message
            print(items_data[item_name]["error message"])
        elif variables.game_data["inventory"][item_number]["uses"] == "∞":
            # The item can be used an unlimited amount of times
            # Use it without changing the uses left
            variables.game_data["player"][variables.game_data["inventory"][item_number]["use"][0]] += variables.game_data["inventory"][item_number]["use"][1]
            # Add 1 action to the counter
            variables.game_data["player"]["actions counter"]+=1
            # Refresh the screen
            inv_show()
            # Show the use message
            print(items_data[item_name]["message"])
        else:
            # Add 1 action to the counter
            variables.game_data["player"]["actions counter"]+=1
            # Use the item, aplly the effect : + or - X to player status
            variables.game_data["player"][variables.game_data["inventory"][item_number]["use"][0]] += variables.game_data["inventory"][item_number]["use"][1]
            if variables.game_data["player"]["energy"] > variables.game_data["player"]["max energy"]:
                # Max energy is above max
                # Change is to tthe maximum value
                variables.game_data["player"]["energy"] = variables.game_data["player"]["max energy"]
            elif variables.game_data["player"]["satiety"] > variables.game_data["player"]["max satiety"]:
                # Max satiety is above max
                # Change is to tthe maximum value
                variables.game_data["player"]["satiety"] = variables.game_data["player"]["max satiety"]
            elif variables.game_data["player"]["hydratation"] > variables.game_data["player"]["max hydratation"]:
                # Max hydratation is above max
                # Change is to tthe maximum value
                variables.game_data["player"]["hydratation"] = variables.game_data["player"]["max hydratation"]
            # Reduce uses by 1
            variables.game_data["inventory"][item_number]["uses"] -= 1
            # Refresh the screen
            inv_show()
            # Show the use message
            print(items_data[item_name]["message"])
    sleep(3)


# Delete the depleted items
def inventory_cleaner():
    """
        Clean the inventory from items at 0 use, start from item_5 to item_9
    """

    # List of item to protect from deletion if depleted
    item_protected = ["item_0", "item_3", "ite"]
    for key in variables.game_data["inventory"]:
        # Get the first key
        if "item" in key and key not in item_protected:
            # Key contains the string "item" ans is not a protected item
            if variables.game_data["inventory"][key]["uses"] == 0:
                variables.game_data["inventory"][key]["name"] = None
                variables.game_data["inventory"][key]["uses"] = None
                variables.game_data["inventory"][key]["use"] = None


# take an item
def take_item(item_name):
    """
        Let the player take the item from a stash
    """

    # Search for an empty slot
    for key in variables.game_data["inventory"]:
        if "item" in key:
            if variables.game_data["inventory"][key]["name"] == None:
                variables.game_data["inventory"][key]["name"] = item_name
                variables.game_data["inventory"][key]["uses"] = items_data[item_name]["uses"]
                variables.game_data["inventory"][key]["use"] = items_data[item_name]["use"]
                print(f"{item_name} added to your inventory")
                sleep(2)
                break


# Refill an item
def refill_item(item_name):
    """
        Refill the water bottle and set it's number of uses back to 5
    """

    if item_name != "Water bottle":
        # Item is not the water bottle
        print(f"\u001b[38;5;196mDespite your best effort you failed to fill that {item_name} with water...\u001b[0m")
    else:
        # Item is the water bottle
        # Check if any tile around the player is the river
        tiles_check = []
        tiles_check.append(variables.island_map[variables.game_data["player"]["position"][0]-1][variables.game_data["player"]["position"][1]])
        tiles_check.append(variables.island_map[variables.game_data["player"]["position"][0]][variables.game_data["player"]["position"][1]-1])
        tiles_check.append(variables.island_map[variables.game_data["player"]["position"][0]][variables.game_data["player"]["position"][1]+1])
        tiles_check.append(variables.island_map[variables.game_data["player"]["position"][0]+1][variables.game_data["player"]["position"][1]])
        tiles_check.append(variables.island_map[variables.game_data["player"]["position"][0]-1][variables.game_data["player"]["position"][1]-1])
        tiles_check.append(variables.island_map[variables.game_data["player"]["position"][0]+1][variables.game_data["player"]["position"][1]+1])
        tiles_check.append(variables.island_map[variables.game_data["player"]["position"][0]+1][variables.game_data["player"]["position"][1]-1])
        tiles_check.append(variables.island_map[variables.game_data["player"]["position"][0]+1][variables.game_data["player"]["position"][1]+1])
        if "~" in tiles_check:
            # A river is found around the player
            # Set the number of uses back to max
            variables.game_data["inventory"]["item_0"]["uses"] = variables.game_data["inventory"]["item_0"]["max uses"]
            # Print success message
            print(items_data["Water bottle"]["refill message"])
        else:
            # No river found
            # Print error message
            print(items_data["Water bottle"]["refill error"])
    sleep(3)


# Drop an item
def drop_item(item_name, player_choice):
    """
        Let the player drop the item, add it to the monkey chest list
    """

    # Check if the item is dropable
    if not items_data[item_name]["actions"]["drop"]:
        inv_show()
        # If the item actions drop is False
        print("\t\t\t\u001b[38;5;196mYou can't drop that !\u001b[0m")
    else:
        # Add the item to the monkey chest
        variables.game_data["Monkey chest"].append(variables.game_data["inventory"][player_choice]["name"])
        # The item is dropable, drop it
        variables.game_data["inventory"][player_choice]["name"] = None
        variables.game_data["inventory"][player_choice]["uses"] = None
        variables.game_data["inventory"][player_choice]["use"] = None
        # Show the drop message
        print(f"You dropped the {item_name} but a monkey stole it !")
    sleep(3)


# Generate the random items stashes
def random_stashes():
    """
        Generate and populate the item stashes on the map
    """

    # Choose 5 position at random in the possible positions
    pos = random.sample(items_stashes_position, k=5)
    # Add the position and item in the stash
    for i in range(5):
        # Change the position from every stash
        variables.game_data["Item stash"][f"item_stash_{i+1}"]["position"] = pos[i]
        # Add the item to the stash using a random with weights
        variables.game_data["Item stash"][f"item_stash_{i+1}"]["items"] = "".join(random.choices(random_item_name, weights=(30,30,5,5,25,5)))
        # Change the map tile
        variables.island_map[variables.game_data["Item stash"][f"item_stash_{i+1}"]["position"][0]][variables.game_data["Item stash"][f"item_stash_{i+1}"]["position"][1]] = "¤"


def show_stash(key, key_2, item_name):
    """
        Show the stash by extracting the position (key, key_2) of an item stash and the name of the item that populates it (item_name)
    """

    print(" __________")
    print("/\\_________\\")
    print("| /         /")
    print("`...........")
    print("|\\         \\")
    print(f"| |---------|           1 - {item_name}")
    print("\\ |         |           Q - Quit")
    print(" \\|_________|")

    choice = input("\t\tChoose what you want to do : ").upper()
    while choice not in "1Q" :
        # Player choice is not a digit or not in valid
        choice = input(f"\t\tChoose from 1 or Q : ").upper()
    if choice == "1":
        # Player chosed to take the item
        # Empty the stash
        variables.game_data["Item stash"][key]["position"] = []
        variables.game_data["Item stash"][key]["items"] = []
        # Reset symbol position
        variables.island_map[variables.game_data["player"]["position"][0]][variables.game_data["player"]["position"][1]] = " "
        # Take the item
        take_item(item_name)
        # Return the player to the map
        ma.map_printer()
        pa.player_actions("Actions Menu")
    elif choice == "Q":
        # Return the player to the map
        ma.map_printer()
        pa.player_actions("Actions Menu")


# VARIABLES
# Items list
items_data = {
                # Important Items / Most likely can't drop / Can't use for now
                "Water bottle" :
                                {
                                    "actions" :     #What actions can the item support
                                                {
                                                    "use"       : True,     # Can the item be used
                                                    "drop"      : False,    # Can the item be dropped
                                                    "refill"    : True,     # Can the item refill
                                                },
                                    "message" : "\u001b[38;5;45mYou take a sip and feel refreshed ! (+20 Hydratation)\u001b[0m", # What is shown when you use the item
                                    "error message" : "\u001b[38;5;196mYour bottle is empty\u001b[38;5;0m", # What is shown when you can't use the item
                                    "refill message" : "\u001b[38;5;45mYour bottle is now back to full with fresh and clean water !\u001b[0m",
                                    "refill error" : "\u001b[38;5;196mYou can't find any water around you !\u001b[0m",
                                },
                "Knife" :
                                {
                                    "actions" :     #What actions can the item support
                                                {
                                                    "use"       : True,    # Can the item be used
                                                    "drop"      : False,    # Can the item be dropped
                                                    "refill"    : False,    # Can the item refill
                                                },
                                    "message" : "\u001b[38;5;45mYou tried to use the knife and cut yourself (-5 Hydratation).\u001b[0m" # What is shown when you use the item
                                },
                "Map" :
                                {
                                    "actions" :     #What actions can the item support
                                                {
                                                    "use"       : True,    # Can the item be used
                                                    "drop"      : False,    # Can the item be dropped
                                                    "refill"    : False,    # Can the item refill
                                                },
                                },
                "Laptop" :
                                {
                                    "actions" :     #What actions can the item support
                                                {
                                                    "use"       : True,    # Can the item be used
                                                    "drop"      : False,    # Can the item be dropped
                                                    "refill"    : False,    # Can the item refill
                                                },
                                    "message" : "\u001b[38;5;11mYou watched a motivationnal video (+5 Energy).\u001b[0m", # What is shown when you use the item
                                    "error message" : "\u001b[38;5;196mYoubrokethespacebaronthekeyboard!\u001b[0m" # What is shown when can't use the item
                                },
                "Solar panel" :
                                {
                                    "actions" :     #What actions can the item support
                                                {
                                                    "use"       : True,    # Can the item be used
                                                    "drop"      : False,    # Can the item be dropped
                                                    "refill"    : False,    # Can the item refill
                                                },
                                    "message" : "\u001b[38;5;11mYou charged yourself. Are you even human ? (+5 Energy).\u001b[0m", # What is shown when you use the item
                                    "error message" : "\u001b[38;5;196mYou electrocuted yourself !\u001b[0m" # What is shown when can't use the item
                                },
                # Items you can find on the map
                "Avocado" :
                                {
                                    "actions" :     #What actions can the item support
                                                {
                                                    "use"       : True,    # Can the item be used
                                                    "drop"      : True,    # Can the item be dropped
                                                    "refill"    : False,    # Can the item refill
                                                },
                                    "uses" : 1,     # Number of use
                                    "use" : ["satiety", 40],     # What actions the item do on use (+40 satiety)
                                    "message" : "\u001b[38;5;118mThat Avocado was tasty ! (+40 Satiety).\u001b[0m" # What is shown when you use the item
                                },
                "Passed Avocado" :
                                {
                                    "actions" :     #What actions can the item support
                                                {
                                                    "use"       : True,    # Can the item be used
                                                    "drop"      : True,    # Can the item be dropped
                                                    "refill"    : False,    # Can the item refill
                                                },
                                    "uses" : 1,     # Number of use
                                    "use" : ["satiety", -10],     # What actions the item do on use (-10 satiety)
                                    "message" : "\u001b[38;5;118mThat Avocado was way passed ! (-10 Satiety).\u001b[0m" # What is shown when you use the item
                                },
                "Banana" :
                                {
                                    "actions" :     #What actions can the item support
                                                {
                                                    "use"       : True,    # Can the item be used
                                                    "drop"      : True,    # Can the item be dropped
                                                    "refill"    : False,    # Can the item refill
                                                },
                                    "uses" : 2,     # Number of use
                                    "use" : ["satiety", 25],     # What actions the item do on use (+25 satiety)
                                    "message" : "\u001b[38;5;118mThat Banana was so sweet ! (+25 Satiety).\u001b[0m" # What is shown when you use the item
                                },
                "Rotten Banana" :
                                {
                                    "actions" :     #What actions can the item support
                                                {
                                                    "use"       : True,    # Can the item be used
                                                    "drop"      : True,    # Can the item be dropped
                                                    "refill"    : False,    # Can the item refill
                                                },
                                    "uses" : 2,     # Number of use
                                    "use" : ["satiety", -5],     # What actions the item do on use (-5 satiety)
                                    "message" : "\u001b[38;5;118mThat Banana was rotten ! (-5 Satiety).\u001b[0m" # What is shown when you use the item
                                },
                "Coco" :
                                {
                                    "actions" :     #What actions can the item support
                                                {
                                                    "use"       : True,    # Can the item be used
                                                    "drop"      : True,    # Can the item be dropped
                                                    "refill"    : False,    # Can the item refill
                                                },
                                    "uses" : 1,     # Number of use
                                    "use" : ["hydratation", 50],     # What actions the item do on use (+50 hydratation)
                                    "message" : "\u001b[38;5;118mThat Coco was refreshing ! (+50 hydratation).\u001b[0m" # What is shown when you use the item
                                },
                "Empty Coco" :
                                {
                                    "actions" :     #What actions can the item support
                                                {
                                                    "use"       : True,    # Can the item be used
                                                    "drop"      : True,    # Can the item be dropped
                                                    "refill"    : False,    # Can the item refill
                                                },
                                    "uses" : 1,     # Number of use
                                    "use" : ["hydratation", 0],     # What actions the item do on use (+0 hydratation)
                                    "message" : "\u001b[38;5;118mThat Coco was completely empty ! (.+0 hydratation).\u001b[0m" # What is shown when you use the item
                                },
}

# Help populate the random stash
random_item_name = [
                    "Avocado",
                    "Banana",
                    "Passed Avocado",
                    "Rotten Banana",
                    "Coco",
                    "Empty Coco"
]

# Possible positions for the random stashes
items_stashes_position = [
                            [25,59], [16,51], [16,4], [28,7], [6,4], [6,24], [2,38], [14,24], [27,28], [13,62], [10,38]
]