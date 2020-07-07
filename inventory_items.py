# coding: utf-8

# Imports


# Extra code
import game_data as gdat

# FUNCTIONS
# Show the inventory
def inv_show():
                                                    
    print(".------------------------------------------------.")
    print("|                                                |")
    print("|                                                |")
    print("|                                                |")
    print("|                                                |")
    print("|                                                |")
    print("|                                                |")
    print("|                                                |")
    print("|                                                |")
    print("|                                                |")
    print("|                                                |")
    print("|                                                |")
    print("|                                                |")
    print("|                                                |")
    print("|                                                |")
    print("|                                                |")
    print("|                                                |")
    print("|                                                |")
    print("|                                                |")
    print("'------------------------------------------------'")


# Use an item
def use_item(item_name):
    """
        Let the player use the item.
    """

    # Check if the item is usable
    if not items_data[item_name]["actions"]["use"]:
        # If the item actions use is False
        print(items_data[item_name]["actions"]["error message"])
    else:
        # If item is usable use it and apply the effects
        # From game data [in player][from item data [name of the item]["use"][status concerned by the items]] += from item data [name of the item]["use"][what change to the status]]
        gdat.game_data["player"][items_data[item_name]["use"][0]] += items_data[item_name]["use"][1]
        # Show the use message
        print(str([items_data[item_name]["message"]]).replace("'", "").strip("[]") + "\n")

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
                                                        "take"      : False,    # Can you take that item from the floor
                                                    },
                                        "uses" : 5,     # Number of use
                                        "use" : ["hydratation", 20],     # What actions the item do on use (+20 hydratation)
                                        "message" : "You take a sip and feel refreshed ! (+20 Hydratation)", # What is shown when you use the item
                                        "error message" : "Your bottle is empty" # What is shown when you can't use the item
                                    },
                "Knife" :
                                    {
                                        "actions" :     #What actions can the item support
                                                    {
                                                        "use"       : False,    # Can the item be used
                                                        "drop"      : False,    # Can the item be dropped
                                                        "refill"    : False,    # Can the item refill
                                                        "take"      : False,    # Can you take that item from the floor
                                                    },
                                        "uses" : 0,     # Number of use
                                        "use" : 5,     # What actions the item do on use (-5 hydratation)
                                        "error message" : "You tried to use the knife and cut yourself (-5 Hydratation)." # What is shown when you can't use the item
                                    },
                "Laptop" :
                                    {
                                        "actions" :     #What actions can the item support
                                                    {
                                                        "use"       : True,    # Can the item be used
                                                        "drop"      : False,    # Can the item be dropped
                                                        "refill"    : False,    # Can the item refill
                                                        "take"      : False,    # Can you take that item from the floor
                                                    },
                                        "uses" : 1000,     # Number of use
                                        "use" : 5,     # What actions the item do on use (+5 energy)
                                        "message" : "You watched a motivationnal video (+5 Energy)." # What is shown when you try to use the item
                                    },
                "Solar panel" :
                                    {
                                        "actions" :     #What actions can the item support
                                                    {
                                                        "use"       : False,    # Can the item be used
                                                        "drop"      : False,    # Can the item be dropped
                                                        "refill"    : False,    # Can the item refill
                                                        "take"      : False,    # Can you take that item from the floor
                                                    },
                                        "uses" : 1000,     # Number of use
                                        "use" : 5,     # What actions the item do on use (+5 energy)
                                        "message" : "You charged yourself. Are you even human ? (+5 Energy)." # What is shown when you try to use the item
                                    },
                # Items you can find on the map
                "Avocado" :
                                    {
                                        "actions" :     #What actions can the item support
                                                    {
                                                        "use"       : True,    # Can the item be used
                                                        "drop"      : True,    # Can the item be dropped
                                                        "refill"    : False,    # Can the item refill
                                                        "take"      : True,    # Can you take that item from the floor
                                                    },
                                        "uses" : 1,     # Number of use
                                        "use" : ["satiety", 10],     # What actions the item do on use (+10 satiety)
                                        "message" : "That avocado was tasty ! (+10 Satiety)." # What is shown when you try to use the item
                                    },
}