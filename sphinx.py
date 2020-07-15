# coding: utf-8

# Imports
import random
from time import sleep

# Extra code
import toolbox as tb
import player_actions as pa

# FUNCTIONS
# The challenge
def guess_number():
    """
        The first challenge
    """

    def sphinx_printer(tries, rounds, historic):
        """
            Sphinx challenge ASCII and player interface
        """

        print(f"\n\u001b[38;5;222m                        .sSSSSSSSs            \u001b[0mGuess : {historic}")
        print("\u001b[38;5;222m                        sSS=\"\"^^^\"s")
        print("            /\\       , /  \\_\\_\\|_/_)")
        print("           /';;     /| \\\\\\/.-. .-./")
        print("          / \\;|    /. \\,S'  0   0 |")
        print(f"         / -.;|    | '.SS     _|  ;             \u001b[0mTries :     {tries}")
        print(f"\u001b[38;5;222m        ; '-.;\\,   |'-.SS\\   __  /S             \u001b[0mRound won : {rounds}")
        print("\u001b[38;5;222m        | _  ';\\\\.  \\' SSS\\_____/SS")
        print("        |  '- ';\\\\.  \\_SSS[_____]SS")
        try:
            print(f"        \\ '--.-';;-. __S{print_mm[0]}S/\\    S{print_mm[1]}S")
        except:
            print(f"        \\ '--.-';;-. __S{print_mm[0]}S/\\    SSS")
        print("        \\  .--' ';;'.=SSS`\\\\_\\_SSS")
        print("        `._ .-'` _';;..=.=.=.\\.=\\")
        print("            ;-._-'  _.;\\.=.=.=.|.=|")
        print("    ,     _.-'    `\"=._  ;\\=.=__/__/")
        print("    )\\ .'`   __        \".;|.=.=.=./")
        print("    (_\\   .-`  '.   |    \\/=.=.=/`")
        print("     /\\\\         \\-,|     |.--'|")
        print("    /  \\`,       //  \\    | |  |")
        print("   ( (__) )  _.-'--,  \\   | |  '--,")
        print("    ;----' -'--,__}}}  \\  '--, __}}}")
        print("    \\_________}}}       \\___}}}\u001b[0m\n")

    rounds = 0
    tries = 0

    while rounds < 3 and tries < 20:
        # Player can play
        # Set win variable
        win = False
        # Initialize guess historic
        historic = ""
        # Sphinx choose a number
        mysterious_number = random.randint(1, 100)
        # Set mysterious number to string to print it in the secret place
        print_mm = str(mysterious_number)
        tb.clear()
        # Print the game status
        sphinx_printer(tries, rounds, historic)
        while not win:
            # Player did not win
            try :
                guess = int(input("What number do I have in mind human ? "))
            except ValueError:
                print("Don't mess with me Human. Only numbers.")
                try :
                    guess = int(input("What number do I have in mind human ? "))
                except ValueError:
                    print("I am losing my patience. I said only numbers, I have no time for your jibberish.")
                    try :
                        guess = int(input("What number do I have in mind human ? "))
                    except:
                        tb.clear()
                        print("^(;,;)^  ^(;,;)^  ^(;,;)^  ^(;,;)^  ^(;,;)^  ^(;,;)^  ^(;,;)^  ^(;,;)^")
                        print("^(;,;)^                       ENOUGH !                         ^(;,;)^")
                        print("^(;,;)^   Ph'nglui mglw'nafh Cthulhu R'lyeh wgah'nagl fhtagn   ^(;,;)^")
                        print("^(;,;)^  ^(;,;)^  ^(;,;)^  ^(;,;)^  ^(;,;)^  ^(;,;)^  ^(;,;)^  ^(;,;)^")
                        sleep(3)
                        # Quit the challenge
                        return
            if guess > mysterious_number:
                tries+=1
                historic = historic + " " + str(guess)
                tb.clear()
                sphinx_printer(tries, rounds, historic)
                print("No, no my number is lower !")
            elif guess < mysterious_number:
                historic = historic + " " + str(guess)
                tries+=1
                tb.clear()
                sphinx_printer(tries, rounds, historic)
                print("No, no my number is higher !")
            else:
                win = True
                tries+=1
                rounds+=1
                print("You won one round !")
                sleep(2)
    tb.clear()
    sphinx_printer(tries, rounds, historic)
    print("The Sphinx let the Bronze Key fall on the floor, you move towards it and pick it up !")
    sleep(3)
    return True