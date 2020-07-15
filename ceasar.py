# coding: utf-8

# Imports
import random
from time import sleep
# Extra code
import variables

# FUNCTIONS
# The Ceasar code
def ceasar_sypher():
    # Every possible sypher keys
    sypher_list = ["","a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    # choose one key from the list
    sypher_key = random.choice(sypher_list)
    # Extract the index from the list using the key
    sypher_key = sypher_list.index(sypher_key)
    turn = 5
    # Message de sypher
    message = "Beautiful is better than ugly. Explicit is better than implicit. Simple is better than complex."
    # Sypher the player name using the sypher key
    player_name = sypher(sypher_key, variables.game_data["player"]["name"]).lower()
    # Sypher the message using the sypher key
    sypher_message = sypher(sypher_key, message)
    # Show the rules to the player
    print("\nThe message as been crypted using Ceasar Code")
    print("Your first task is to find the Key used to sypher the message")
    print("When you think you found it, use it to sypher your name with that key and type it !")

    while turn != 0:
        print(f"You have \u001b[38;5;196m{turn}\u001b[0m chances to enter your name !\n")
        print(f"\u001b[38;5;255m{sypher_message}\u001b[0m")
        # Player chose an input, must be letters
        key = input("Enter a key : ").lower()
        while not key.isalpha():
            # Check if key is a letter
            key = input("Enter a key : ").lower()
        # Print the key for the player
        for char in enumerate(sypher_list):
            if char[1] == key:
                print(f"\nThe current key is : {char}")
        if key == player_name:
            # If the key is the player name with the sypher the player win
            print("\nYou found your name using the sypher, you won !")
            sleep(2)
            return True
        if len(key) > 1:
            # If the player enter more than one letter, only use the first one
            key = key[0]
        # Extract the index from the list using the key
        key = sypher_list.index(key)
        # Desypher the message using the key
        desypher_message = desypher(key, sypher_message)
        # Print the desyphered message using the player input key
        print(f"\u001b[38;5;255m{desypher_message}\u001b[0m")
        turn-=1
    print("\n\u001b[38;5;196mAfter your 5 tries the letters start moving around, they're not stopping...")
    print("You decide to wait for a while...\u001b[0m")
    sleep(3)


def sypher(key, message, sypher_list = ["","a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]):
    """
        Transform the message using the key randomized at the start of the game.
    """

    # Change the message to a list
    message = message.split()
    # Initialize the empty temp list
    temp_message = []
    result_message = []
    for word in enumerate(message):
        # For every word in message create a list of every letter
        temp_message.append(list(word[1]))
    # Save the word index
    y = 0
    for word in temp_message:
        # Save the letter index
        x = 0
        # For every word in temp
        for char in word:
            # For every letter in word save the index of that letter
            try :
                # Save the index if it exist in the sypher list
                letter_index = int(sypher_list.index(char.lower()))
            except:
                # Pass that letter
                break
            # Add the sypher key to the letter index to sypher or decipher the message
            letter_index+=key
            if letter_index > 26:
                # The letter index is beyond 26, soustract 26 to stay in the sypher list
                letter_index-=26
            elif letter_index < 1:
                # The letter index is below 1, add 26 to stay in the sypher list
                letter_index+=26
            # Change the letter using the sypher key
            temp_message[y][x] = sypher_list[letter_index]
            # Move to the next X index
            x+=1
        # Move to the next Y index
        y+=1
        result_message.append("".join(word))
    return " ".join(result_message)


def desypher(key, message, sypher_list = ["","a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]):
    """
        Desypher the message using the input of the player as key.
    """

    # Change the message to a list
    message = message.split()
    # Initialize the empty temp list
    temp_message = []
    result_message = []
    for word in enumerate(message):
        # For every word in message create a list of every letter
        temp_message.append(list(word[1]))
    # Save the word index
    y = 0
    for word in temp_message:
        # Save the letter index
        x = 0
        # For every word in temp
        for char in word:
            # For every letter in word save the index of that letter
            try :
                # Save the index if it exist in the sypher list
                letter_index = sypher_list.index(char.lower())
            except:
                # Pass that letter
                break
            # Add the sypher key to the letter index to sypher or decipher the message
            letter_index-=key
            if letter_index > 26:
                # The letter index is beyond 26, soustract 26 to stay in the sypher list
                letter_index-=26
            elif letter_index < 1:
                # The letter index is below 1, add 26 to stay in the sypher list
                letter_index+=26
            # Change the letter using the sypher key
            temp_message[y][x] = sypher_list[letter_index]
            # Move to the next X index
            x+=1
        # Move to the next Y index
        y+=1
        result_message.append("".join(word))
    return " ".join(result_message)