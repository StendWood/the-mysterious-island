# coding: utf-8

# Imports
import random
from time import sleep

# Extra code
import  variables
import toolbox as tb

# FUNCTIONS
# The Fizz Buzz is launched nothing can stop it
def fizz_buzz():
    """
        The player is playing with 10 monkeys, no input needed everything is automatic
    """

    # Set up the game interface
    def fizz_buzz_printer():
        """
            Interface print for the FizzBuzz game !
        """

        # Welcome ASCII Art
        print("\n\t\t     .-\"-.            .-\"-.           .-\"-.")
        print("\t\t   _/.-.-.\\_        _/.-.-.\\_       _/.-.-.\\_")
        print("\t\t  /|( o o )|\\      ( ( o o ) )     ( ( o o ) )")
        print("\t\t | //  \"  \\\\ |      |/  \"  \\|       |/  \"  \\|")
        print("\t\t/ / \\'---'/ \\ \\      \\'/^\\'/         \\ .-. /")
        print("\t\t\\ \\_/`\"\"\"`\\_/ /      /`\\ /`\\         /`\"\"\"`\\")
        print("\t\t \\           /      /  /|\\  \\       /       \\")
        print("\n\t\t   ▀█▀ █░█ █▀▀   █▀▀ █ ▀█ ▀█   █▄▄ █░█ ▀█ ▀█")
        print("\t\t   ░█░ █▀█ ██▄   █▀░ █ █▄ █▄   █▄█ █▄█ █▄ █▄\n")

    # Randomize the success chances of every player
    game_data = {
                    "Monkey chief" : random.randint(50, 80),
                    "Monkeys" : random.randint(10, 70),
                    variables.game_data["player"]["name"] : random.randint(80, 90)
    }
    # Player list : 1 chief 9 monkeys 1 player
    player_pool = ["Monkey chief", "Monkey 1", "Monkey 2", "Monkey 3", "Monkey 4", "Monkey 5", 
                    "Monkey 6", "Monkey 7", "Monkey 8", "Monkey 9", 
                    variables.game_data["player"]["name"]]
    # Shuffle the list
    random.shuffle(player_pool)
    # Print the interface
    tb.clear()
    fizz_buzz_printer()
    # Initialize game counter and turn counter
    counter = 1
    turn = 1
    # Launch the actual game cycle
    counter = 0
    while len(player_pool) > 1 and variables.game_data["player"]["name"] in player_pool:
        # Still more than one player and the player is still in the game
        # Print the number of turn and the number of player
        print(f"\nThis is turn {turn}     |   {len(player_pool)} player in the game !\n")
        for who_is_playing in player_pool:
            # Iterate through the list
            if "chief" in who_is_playing:
                # If the chief is playing
                if random.randint(0, 100) < game_data["Monkey chief"]:
                    # The random number is in the Chief chances to say the right answer
                    # Print the right answer using the function
                    print(f"\t{who_is_playing} said {counter_changer(counter)}")
                    counter+=1
                else:
                    # The random number is above the Chief chance to say the right answer
                    print(f"\t{who_is_playing} got it wrong ! BWHAHAHAAHAH !")
                    # Remove the chief from the player list
                    player_pool.remove(who_is_playing)
                    counter+=1
                sleep(0.5)
            elif who_is_playing == variables.game_data["player"]["name"]:
                # The main protagonist is playing
                if random.randint(0, 100) < game_data[variables.game_data["player"]["name"]]:
                    # The random number is in the main protagonist chances to say the right answer
                    # Print the right answer using the function
                    print(f"\t{who_is_playing} said {counter_changer(counter)}")
                    sleep(0.5)
                    counter+=1
                else:
                    # Main protagonist got it wrong
                    print(f"\t{who_is_playing} got it wrong ! BWHAHAHAAHAH !")
                    print("\n\tThe monkeys laugh at you...")
                    sleep(2)
                    # End the game
                    return False
            else:
                # A normal monkey is playing
                if random.randint(0, 100) < game_data["Monkeys"]:
                    # He gets the right answer
                    print(f"\t{who_is_playing} said {counter_changer(counter)}")
                    counter+=1
                else:
                    # The monkey got the wrong answer
                    print(f"\t{who_is_playing} got it wrong ! BWHAHAHAAHAH !")
                    # Remove the monkey from the player list
                    player_pool.remove(who_is_playing)
                    counter+=1
                sleep(0.5)
        turn+=1
    # Player is the last man standing
    print("You won !")
    sleep(1)
    return True


def gameflow():
    """
        Control the flow of the FizzBuzz game
    """

    # Launch the first game and save the return (bool)
    game = fizz_buzz()
    while not game:
        # Player keep losing
        if not game:
            # Player lost
            # Ask if he wants to play again
            choice = input("\nPress any Key to try again or press Q to leave...")
            if choice.upper() == "Q":
                # Input is Q, return to the map
                return False
            else:
                # Any other input launch another game
                game = fizz_buzz()
    # The player won
    sleep(3)
    tb.clear()
    # End game ASCII Art
    print("\u001b[38;5;255m __________")
    print("/\\_________\\")
    print("| /         /")
    print("`...........")
    print("|\\         \\")
    print("| |---------|")
    print("\\ | MONKEYS |")
    print(" \\|_________|\u001b[0m")
    print("\nThe monkeys run away screaming : YOU CHEATED YOU CHEATED !\n")
    print("As you reach for the \u001b[38;5;220mGolden Key\u001b[0m, you see a mysterious chest close by...")
    input("\n\t\tPress any key to continue")
    return True


def counter_changer(counter):
    """
        Change the counter int to Fizz, Buzz or Fizz Buzz
    """

    # Check if counter is a multiple of 3 or 5 or both
    if counter % 3 == 0 and counter %5 == 0:
        # Counter is multiple of both
        return "FizzBuzz"
    elif counter % 3 == 0:
        # Counter is multiple of 3
        return "Fizz"
    elif counter % 5 == 0:
        # Counter is multiple of 5
        return "Buzz"
    else:
        # Counter is not a multiple of 3 or 5
        return counter
