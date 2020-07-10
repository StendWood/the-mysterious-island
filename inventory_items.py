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

    tb.clear()
    # ASCII Art
    print("     _....._")
    print("    ';-.--';'")
    print("      }===={       _.---.._")
    print("    .'      '.    ';-..--';")
    print("   /::        \\    `}===={")
    print("  |::          :   /      '.")
    print("  \\::.        _.---_        \\")
    print("   '::_     _`---..-';       |")
    print("       `````  }====={        /")
    print(f"            .'       '.   _.'                   Movements :     {variables.game_data['player']['movements counter']}")
    print(f"           /::         \\ `                      Actions :       {variables.game_data['player']['actions counter']}")
    print("          |::           |")
    print(f"          \\::.          /                       Energy :        {variables.game_data['player']['energy']}")
    print(f"           '::_      _.'                        Hydratation :   {variables.game_data['player']['hydratation']}")
    print(f"               ``````                           Satiety :       {variables.game_data['player']['satiety']}")
    # Print the inventory page
    print()
    # Clean the ivnentory from depleted items
    inventory_cleaner()
    # Counter to keep track of how many items are in the inventory
    item_number = 0
    for key in variables.game_data["inventory"]:
        # Get the first key
        if "item" in key:
            if variables.game_data["inventory"][key]["name"] != None:
                # Name is not None
                print(f"{item_number} - {variables.game_data['inventory'][key]['name']} {variables.game_data['inventory'][key]['uses']}")
                item_number+=1
    # Quit the inventory and return to the map
    print("Q - Return to map")
    print()
    return item_number


# Inventory item choices
def inventory_choices():
    """
        Show the inventory and let the player choose an item
    """

    # # Clean the ivnentory from depleted items
    inventory_cleaner()
    # Print the inventory and show save how many items are in the bag
    items = inv_show()
    # Create the valid input from the number of items in the inventory
    valid = [str(num) for num in range(items)]
    valid.append("Q")
    # Ask for the player choice
    choice = input("\t\tChoose what you want to do : ").upper()
    while choice not in valid :
        # Player choice is not a digit or not in valid
        choice = input(f"\t\tChoose from 0 - {items-1} or Q : ").upper()
    # Choice is a digit and in valid
    if choice.capitalize() == "Q":
        # Choice is Q, return to map
        ma.map_printer()
        # Ask what the player wants to do
        pa.player_actions("Actions Menu")
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
    # Refresh the screen
    inv_show()
    # The player choose
    if choice == "1":
        # Use the selected item if he can be used
        use_item(item_name, item_number)
    elif choice == "2":
        # Drop the selected item if it can be dropped
        drop_item(item_name, item_number)
    elif use_item == "3":
        # Refill the item if it can be refilled
        pass

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
        sleep(7)
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
            if variables.game_data["player"][variables.game_data["inventory"][item_number]["use"][0]] > 100:
                # The stats is above 100, set it back to 100
                variables.game_data["player"][variables.game_data["inventory"][item_number]["use"][0]] = 100
            # Reduce uses by 1
            variables.game_data["inventory"][item_number]["uses"] -= 1
            # Refresh the screen
            inv_show()
            # Show the use message
            print(items_data[item_name]["message"])
    # Wait 3 seconds then refresh the screen
    sleep(3)
    # Show the inventory choice again
    inventory_choices()

# Delete the depleted items
def inventory_cleaner():
    """
        Clean the inventory from items at 0 use, start from item_5 to item_9
    """

    # List of item to protect from deletion if depleted
    item_protected = ["item_0", "item_3", "item_4"]
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
        Let the player take the item.
    """

    pass

# Refill an item
def refill_item(item_name):
    """
        Refill the water bottle and set it's use back to 5
    """

    if item_name != "Water bottle":
        print(f"Despite your best effort you can't refill that {item_name}...")

# Drop an item
def drop_item(item_name, player_choice):
    """
        Let the player drop the item.
    """

    # Check if the item is dropable
    if not items_data[item_name]["actions"]["drop"]:
        inv_show()
        # If the item actions drop is False
        print("\t\t\t\u001b[38;5;196mYou can't drop that !\u001b[0m")
        sleep(3)
    else:
        # If item is dropable drop it and show it on the map
        pass
        # Show the drop message
    inventory_choices()


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
                                    "error message" : "\u001b[38;5;196mYour bottle is empty\u001b[38;5;0m" # What is shown when you can't use the item
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
                                    "use" : ["satiety", 10],     # What actions the item do on use (+10 satiety)
                                    "message" : "\u001b[38;5;118mThat Avocado was tasty ! (+10 Satiety).\u001b[0m" # What is shown when you use the item
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
                                    "use" : ["satiety", 5],     # What actions the item do on use (+5 satiety)
                                    "message" : "\u001b[38;5;118mThat Banana was so sweet ! (+5 Satiety).\u001b[0m" # What is shown when you use the item
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
                                    "use" : ["hydratation", 10],     # What actions the item do on use (+10 hydratation)
                                    "message" : "\u001b[38;5;118mThat Coco was refreshing ! (+10 hydratation).\u001b[0m" # What is shown when you use the item
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

# Possible positions fo the random stashes
items_stashes_position = [
                            [25,59],
]