# coding: utf-8

# Imports
import random

# Extra code
import game_data as gdat
import main_menu as mm
import map_admin as ma
import toolbox as tb

# FUNCTIONS
# Show the inventory
def inv_show():
    """
        Simply show the inventory and ask what the player wants to do
    """

    # Clea console
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
    print(f"            .'       '.   _.'                   Movements :     {gdat.game_data['player']['movements counter']}")
    print(f"           /::         \\ `                      Actions :       {gdat.game_data['player']['actions counter']}")
    print("          |::           |")
    print(f"          \\::.          /                       Energy :        {gdat.game_data['player']['energy']}")
    print(f"           '::_      _.'                        Hydratation :   {gdat.game_data['player']['hydratation']}")
    print(f"               ``````                           Satiety :       {gdat.game_data['player']['satiety']}")
    # Print the inventory page
    print()
    # Counter to keep track of how many items are in the inventory
    item_number = 0
    for key in gdat.game_data["inventory"]:
        # Get the first key
        if "item" in key:
            # Key contains the string "item"
            for key_2 in gdat.game_data["inventory"][key]:
                # Get the second key
                if key_2 == "name":
                    # Key_2 is the name
                    if gdat.game_data["inventory"][key][key_2] != None:
                        # Name is not None
                        print(f"{item_number} - {gdat.game_data['inventory'][key][key_2]} {gdat.game_data['inventory'][key]['uses']}")
                        item_number+=1
    print()
    return item_number


# Inventory item choices
def inventory_choices():
    """
        Show the ivnentory and let the player choose an item
    """
    # Print the inventory and show save how many items are in the bag
    items = inv_show()
    # Create the valid input from the number of items in the inventory
    valid = [str(num) for num in range(items)]
    # Ask for the player choice
    choice = input("\t\tChoose what you want to do : ")
    while not choice.isdigit() or choice not in valid :
        # Player choice is not a digit or not in valid
        choice = input(f"\t\tChoose from 0 - {items-1} : ")
    # Choice is a digit and in valid
    # Refresh the screen
    inv_show()
    # Print the item chosed by the player
    print(f"\t\tYou chose the {gdat.game_data['inventory'][f'item_{choice}']['name']}")
    # Save the item name
    item_name = f"{gdat.game_data['inventory'][f'item_{choice}']['name']}"
    # Save the item number
    item_number = f"item_{choice}"
    # Ask what he wants to do with that item
    print(f"\n1 - {ma.menu_data['Item Actions'][1]}     2- {ma.menu_data['Item Actions'][2]}      3 - {ma.menu_data['Item Actions'][3]}\n")
    choice = mm.menu_choice("Item Actions")
    # Refresh the screen
    inv_show()
    # The player choose
    if choice == "1":
        use_item(item_name, item_number)

# Use an item
def use_item(item_name, item_number):
    """
        Use the targeted item
    """

    # Check if the item is usable
    if not items_data[item_name]["actions"]["use"]:
        # If the item actions use is False
        print(items_data[item_name]["actions"]["error message"])
    else:
        # If item is usable check for uses left
        if gdat.game_data["inventory"][item_number]["uses"] == 0:
            # No uses left, print the error message
            print(items_data[item_name]["error message"])
        elif gdat.game_data["inventory"][item_number]["uses"] == "∞":
            # The item can be used an unlimited amount of times
            # Use it without changing the uses left
            gdat.game_data["player"][gdat.game_data["inventory"][item_number]["use"][0]] += gdat.game_data["inventory"][item_number]["use"][1]
        else:
            # Use the item, aplly the effect : + or - X to player status
            gdat.game_data["player"][gdat.game_data["inventory"][item_number]["use"][0]] += gdat.game_data["inventory"][item_number]["use"][1]
            if gdat.game_data["player"][gdat.game_data["inventory"][item_number]["use"][0]] > 100:
                # The stats is above 100, set it back to 100
                gdat.game_data["player"][gdat.game_data["inventory"][item_number]["use"][0]] = 100
            # Reduce uses by 1
            gdat.game_data["inventory"][item_number]["uses"] -= 1
            # Refresh the screen
        inv_show()
        # Show the use message
        print(items_data[item_name]["message"])


# take an item
def take_item(item_name):
    """
        Let the player take the item.
    """

    pass


# Drop an item
def drop_item(item_name, player_choice):
    """
        Let the player drop the item.
    """

    # Check if the item is dropable
    if not items_data[item_name]["actions"]["drop"]:
        # If the item actions drop is False
        print("You can't drop that !")
    else:
        # If item is dropable drop it and show it on the map
        # From game data [in player][from item data [name of the item]["drop"][status concerned by the items]] += from item data [name of the item]["drop"][what change to the status]]
        gdat.game_data["inventory"][f"item_{player_choice}"]
        # Show the drop message
        print(items_data[item_name]["message"])


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
                                    "message" : "\u001b[38;5;45mYou take a sip and feel refreshed ! (+20 Hydratation)\u001b[38;5;0m", # What is shown when you use the item
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
                                    "message" : "\u001b[38;5;45mYou tried to use the knife and cut yourself (-5 Hydratation).\u001b[38;5;0m" # What is shown when you use the item
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
                                    "message" : "\u001b[38;5;15mYou watched a motivationnal video (+5 Energy).\u001b[38;5;0m", # What is shown when you use the item
                                    "error message" : "\u001b[38;5;196mYoubrokespacebaronthekeyboard!\u001b[38;5;0m" # What is shown when can't use the item
                                },
                "Solar panel" :
                                {
                                    "actions" :     #What actions can the item support
                                                {
                                                    "use"       : True,    # Can the item be used
                                                    "drop"      : False,    # Can the item be dropped
                                                    "refill"    : False,    # Can the item refill
                                                },
                                    "message" : "\u001b[38;5;15mYou charged yourself. Are you even human ? (+5 Energy).\u001b[38;5;0m", # What is shown when you use the item
                                    "error message" : "\u001b[38;5;196mYou electrocuted yourself !\u001b[38;5;0m" # What is shown when can't use the item
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
                                    "message" : "\u001b[38;5;118mThat avocado was tasty ! (+10 Satiety).\u001b[38;5;0m" # What is shown when you use the item
                                },
}

# Help populate the random stash
random_item_name = [
                    "Avocado",
]

# Possible positions fo the random stashes
items_stashes_position = [
                            [25,59],
]