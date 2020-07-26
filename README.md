# the-mysterious-island

Backlog : https://trello.com/b/KwEYec5F/python-project-1

Title : The Mysterious Island

Subject:

The player is dropped on the beach of a seemingly deserted island.
The only thing he has are:
    - A water bottle
    - his Laptop
    - A multitools Knife
    - A solar panel
    - And a Map
The player has to complete 3 challenges to gather 3 keys and find the skull door to win the game.


Specifications : 

    - Ask the player name.
    - Represent the map in the terminal (ASCII), the minimum resolution is 50x30. Each of these elements will be represented (rock, mountain, sand, river, ocean, plain, tree, mysterious places).
    - Place the player avatar on the map.
    - Player can move in 4 directions (N, W, E, S).
    - Manage an inventory.
    - Manage an item list randomly placed on the map (item stash), the player can take these objects or drop them. (Dropping them will result in the player losing them, or maybe not...).
    - Every item is usable.
    - He has to manage 3 status:
                                - Energy
                                - Satiety
                                - Hydratation
    - Every movements make him lose : -3 Energy, -2 Satiety and -2 Hydratation.
    - He can sleep to win : +6 Energy/hour at the cost of : -2 Hydratation/hour and -1 Satiety/hour.
    - Every actions and movements are counted in 2 counters (They affect your endgame score).
    - The game duration is saved (It also affect your endgame score).
    - The player can manage an inventory of 10 objets, 5 of them are mandatory (Water bottle, Map, Laptop, Multitools Knife, Solar Panel).
    - The player can find item stash on the island and loot them,(Banana, Coco, Avocado) each of this items are a chance to be rotten (5%).
    - Player can refill the water bottle near a river.
    - When the player arrives at a mysterious place a challenge launches, each challenge gives a key :
                        - The Shpinx (Mysterious number) : Bronze Key
                        - Ceasar Sypher : Silver Key
                        - Multi FizzBuzz : Golden Key (Player doesn't actually play this one)
    - The player can save and load his game.
    - The save is removed if a player start a new game and save.
    - When the player loses :  the current date, his name and the cause of death is saved in the game historic (10 last games).
    - When the player wins, his performance is saved on the leaderboard and on the game historic
    - Leaderboard and historic can be checked from the main menu
    - Almost everything is modable, most variables are in game_data.py, the map can be changed using base_map.txt (respect the tiles symbol !).

Mysterious places:

    First challenge : The Sphinx (The Mysterious Number)
        - The sphinx pick a random number (1 - 100)
        - The player guess
        - The Sphinx help the player by saying if his number is lower or higher
        - If the player guess correctly 3 times he win the game and the Bronze Key
        - After 20 tries, the player loses and return to the map
        - You can retry the challenge
        - Every win/lose count as 1 action

    Second challenge : The Ceasar Sypher
        - https://www.wikiwand.com/fr/Chiffrement_par_d%C3%A9calage
        - A phrase is crypted using a random key.
        - Player input a key and see if it is the right one.
        - When the player thinks he has the right one, he enter his name crypted using the guessed key, he win the game and the silver key if his input is correct.
        - The player has 5 tries.
    
    Third challenge : The Multi FizzBuzz
        - 11 participants ( 1 chief monkey, 9 monkeys, the player)
        - Counts start from 1
        - Each participants has to say the right number, the chief monkey has 50-80% chances to say the right answer, the monkeys 10-70% chances and the player 80-90% chances.
        - if the counts is a multiple of 3 the right answer is Fizz
        - if the counts is a multtiple of 5 the right answer is Buzz
        - if the counts is a multiple of both 3-5 the right answer is Fizz Buzz
        - If a participants say the wrong answer he is eliminated
        - The player win the golden Key and a surprise if he is the last one in the game


Modability:

You can change almost everything by going into variables.
Energy,max energy,energy decay...
You can create/change items by adding/changing a line in the inventory_items.py/items_data{} DICT.
The map is modable, make sure to respect the established symbols or expect several errors or needs to change the code.
To change the map you just have to modify the maps/map.txt | RESPECT THE SYMBOLS ESTABLISHED |



Technical specs:

    - PEP8 and DRY
    - English funtions and variables names
    - Commented code and doctring in function
    - Procedural coding
    - UFT-8 prefixed python files
    - Don't use GLOBAL
    - Best UI/UX possible for the player


Folders/Files Architecture:

    Folders : 
                - Maps :
                        - base_map.txt
                        - saved_map.txt
                - Save :
                        - data_save.json
                        - historic.json
                        - leaderboard.json
                - ceasar.py :
                                - ceasar_sypher()
                                - sypher()
                                - desypher()
                - fizzbuzz.py :
                                - fizz_buzz()
                                    - fizz_buzz_printer()
                                - gameflow()
                                - counter_changer()
                - game_data.py :
                                - new_game()
                                - load_game()
                                - save_game()
                                - save_cleaner()
                                - save_data()
                                - load_data()
                - inventory_items.py :
                                - inv_show()
                                - inventory_choices()
                                - use_item()
                                - inventory_cleaner()
                                - take_item()
                                - refill_item()
                                - drop_item()
                                - random_stashes()
                                - show_stash()
                                - monkey_chest()
                                - items_data{}
                                - random_item_name[]
                                - item_stashes_position[]
                - leaderboard.py :
                                - leaderboard()
                                - historic()
                                - add_score()
                                - add_historic()
                                - save_historic()
                                - load_historic()
                                - save_leaderboard()
                                - load_leaderboard()
                - main.py :
                                - adventure()
                - main_menu.py :
                                - welcome_screen()
                                - main_menu_chooser()
                                - menu_choice()
                                - main_menu()
                - map_admin.py :
                                - new_map()
                                - saved_map()
                                - map_printer()
                                - inventory_map_printer()
                                - status_counter_init()
                                - status_counter_reset()
                                - map_reveal()
                                - save_map()
                                - map_tiles{}
                                - menu_data{}
                - player_actions.py :
                                - player_actions()
                                - player_sleep()
                                - check_vitals()
                - player_move.py :
                                - player_movement()
                                - move()
                                - move_checker()
                                - tile_checker()
                - sphinx.py :
                                - guess_number()
                                    - sphinx_printer()
                - toolbox.py :
                                - clear()
                                - ask_player_name()
                                - rules_stories()
                                - death_art()
                                - duration()
                - variables.py :
                                - island_map[]
                                - game_data{}
                                - historic_data[]
                                - leaderboard_data[]
                                - time_data{}
