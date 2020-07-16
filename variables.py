# coding: utf-8

# Imports

# Variables Declaration
# Map
island_map = []

# VARIABLES
# Game Data
game_data = {
                "duration" : 0,
                "score" : 0,
                "player" : 
                            {
                                "name" : "John Doe",
                                "position" : [26, 58],
                                "energy" : 100,
                                "max energy" : 100,
                                "energy decay" : -3,
                                "hydratation" : 100,
                                "max hydratation" : 100,
                                "hydratation decay" : -2,
                                "satiety" : 100,
                                "max satiety" : 100,
                                "satiety decay" : -2,
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
                                                    "max uses" : 5,
                                                    "use" : ["hydratation", 25],     # What actions the item do on use (+20 hydratation)
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
                                                    "use" : ["energy", 10],     # What actions the item do on use (+10 energy)
                                                },
                                    "item_4" : {
                                                    "name" : "Solar panel",
                                                    "uses" : 1,     # Number of use
                                                    "use" : ["energy", 10],     # What actions the item do on use (+10 energy)
                                                },
                                    "item_5" : {
                                                    "name" : None,
                                                    "uses" : None,     # Number of use
                                                    "use" : None,     # What actions the item do on use
                                                },
                                    "item_6" : {
                                                    "name" : None,
                                                    "uses" : None,     # Number of use
                                                    "use" : None,     # What actions the item do on use
                                                },
                                    "item_7" : {
                                                    "name" : None,
                                                    "uses" : None,     # Number of use
                                                    "use" : None,     # What actions the item do on use
                                                },
                                    "item_8" : {
                                                    "name" : None,
                                                    "uses" : None,     # Number of use
                                                    "use" : None,     # What actions the item do on use
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
                                                            "items" : "",
                                                        },
                                    "item_stash_2" : 
                                                        {
                                                            "position" : [],
                                                            "items" : "",
                                                        },
                                    "item_stash_3" : 
                                                        {
                                                            "position" : [],
                                                            "items" : "",
                                                        },
                                    "item_stash_4" : 
                                                        {
                                                            "position" : [],
                                                            "items" : "",
                                                        },
                                    "item_stash_5" : 
                                                        {
                                                            "position" : [],
                                                            "items" : "",
                                                        },
                                },
                "Monkey chest" :
                                {
                                    "position" : None,
                                    "items" : []
                                },
}

# Historic data
historic_data = [
                    
]

# Leaderboard data
leaderboard_data = [
                    
]

# Time data
time_data = {
                "start time" : "",
                "end time"   : ""
}