# coding: utf-8

# Imports

# Extra code
import variables
import toolbox as tb
import main_menu as mm
import map_admin as ma

# FUNCTIONS
# Player chose New Game in the main menu
def new_game():
    """
        Start a new game
    """

    # Reprint the welcome screen
    mm.welcome_screen()
    # Adk player name
    tb.ask_player_name()
    # Print the rules and stories after asking for player name
    tb.rules_stories()
    # Load the base_map.txt
    ma.new_map()

# Player chose Load Game in the main menu
def load_game():
    # Load saved map
    ma.saved_map()


# Game Data
game_data = {
                "player" : [
                            variables.player_name,
                            
                            ]

}