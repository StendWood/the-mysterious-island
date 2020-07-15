# coding: utf-8

# Imports
import random
from time import sleep

# Extra code
import  variables
import toolbox as tb
import map_admin as ma

# FUNCTIONS
# The Fizz Buzz is launched nothing can stop it
def fizz_buzz():
    """
        The player is playing with 10 monkeys, no input needed everything is automatic
    """

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
    # Iterate through the list
    counter = 1
    turn = 1
    # Launch the actual game cycle
    counter = 0
    while len(player_pool) > 1 and variables.game_data["player"]["name"] in player_pool:
        print(f"\nThis is turn {turn}     |   {len(player_pool)} player in the game !\n")
        for who_is_playing in player_pool:
            if "chief" in who_is_playing:
                if random.randint(0, 100) < game_data["Monkey chief"]:
                    print(f"\t{who_is_playing} said {counter_changer(counter)}")
                    counter+=1
                else:
                    print(f"\t{who_is_playing} got it wrong ! BWHAHAHAAHAH !")
                    player_pool.remove(who_is_playing)
                    counter+=1
                sleep(0.5)
            elif who_is_playing == variables.game_data["player"]["name"]:
                if random.randint(0, 100) < game_data[variables.game_data["player"]["name"]]:
                    print(f"\t{who_is_playing} said {counter_changer(counter)}")
                    sleep(0.5)
                    counter+=1
                else:
                    print(f"\t{who_is_playing} got it wrong ! BWHAHAHAAHAH !")
                    print("\n\tThe monkeys laugh at you...")
                    sleep(2)
                    return False
            else:
                if random.randint(0, 100) < game_data["Monkeys"]:
                    print(f"\t{who_is_playing} said {counter_changer(counter)}")
                    counter+=1
                else:
                    print(f"\t{who_is_playing} got it wrong ! BWHAHAHAAHAH !")
                    player_pool.remove(who_is_playing)
                    counter+=1
                sleep(0.5)
        turn+=1
    print("You won !")
    sleep(1)
    return True

def gameflow():
    game = fizz_buzz()
    while not game:
        if not game:
            choice = input("Replay")
            if choice.upper() == "Q":
                return False
            else:
                game = fizz_buzz()
    sleep(3)
    tb.clear()
    # The player won
    print("\u001b[38;5;255m __________")
    print("/\\_________\\")
    print("| /         /")
    print("`...........")
    print("|\\         \\")
    print(f"| |---------|")
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

    if counter % 3 == 0 and counter %5 == 0:
        return "FizzBuzz"
    elif counter % 3 == 0:
        return "Fizz"
    elif counter % 5 == 0:
        return "Buzz"
    else:
        return counter