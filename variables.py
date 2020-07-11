# coding: utf-8

# Imports

# Variables Declaration
# Map
island_map = []

# VARIABLES
# Game Data
game_data = {
                "player" : 
                            {
                                "name" : "",
                                "position" : [26, 58],
                                "energy" : 100,
                                "hydratation" : 100,
                                "satiety" : 100,
                                "movements counter" : 0,
                                "actions counter" : 0,
                            },
                "inventory" :
                                {
                                    "keychain" :
                                                [
                                                    False, # 0 - Bronze Key
                                                    False, # 1 - Silver Key
                                                    False  # 2 - Golden Key
                                                ],
                                    "item_0" : 
                                                {
                                                    "name" : "Water bottle",
                                                    "uses" : 5,     # Number of use
                                                    "use" : ["hydratation", 20],     # What actions the item do on use (+20 hydratation)
                                                },
                                    "item_1" : 
                                                {
                                                    "name" : "Knife",
                                                    "uses" : "∞",     # Number of use
                                                    "use" : ["hydratation", -5],     # What actions the item do on use (-5 hydratation)
                                                },
                                    "item_2" : {
                                                    "name" : "Map",
                                                    "uses" : "∞"
                                                },
                                    "item_3" : {
                                                    "name" : "Laptop",
                                                    "uses" : 1,     # Number of use
                                                    "use" : ["energy", 5],     # What actions the item do on use (+5 energy)
                                                },
                                    "item_4" : {
                                                    "name" : "Solar panel",
                                                    "uses" : 1,     # Number of use
                                                    "use" : ["energy", 5],     # What actions the item do on use (+5 energy)
                                                },
                                    "item_5" : {
                                                    "name" : None,
                                                    "uses" : None,     # Number of use
                                                    "use" : None,     # What actions the item do on use
                                                },
                                    "item_6" : {
                                                    "name" : "Banana",
                                                    "uses" : 2,     # Number of use
                                                    "use" : ["satiety", 5],     # What actions the item do on use
                                                },
                                    "item_7" : {
                                                    "name" : None,
                                                    "uses" : None,     # Number of use
                                                    "use" : None,     # What actions the item do on use
                                                },
                                    "item_8" : {
                                                    "name" : "Banana",
                                                    "uses" : 2,     # Number of use
                                                    "use" : ["satiety", 5],     # What actions the item do on use
                                                },
                                    "item_9" : {
                                                    "name" : None,
                                                    "uses" : None,     # Number of use
                                                    "use" : None,     # What actions the item do on use
                                                },
                                },
                "Item stash" : 
                                {   
                                    "item_stash_1" : 
                                                        {
                                                            "position" : [],
                                                            "items" : [],
                                                        },
                                    "item_stash_2" : 
                                                        {
                                                            "position" : [],
                                                            "items" : [],
                                                        },
                                    "item_stash_3" : 
                                                        {
                                                            "position" : [],
                                                            "items" : [],
                                                        },
                                    "item_stash_4" : 
                                                        {
                                                            "position" : [],
                                                            "items" : [],
                                                        },
                                    "item_stash_5" : 
                                                        {
                                                            "position" : [],
                                                            "items" : [],
                                                        },
                                },
}