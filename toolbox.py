# coding: utf-8

# Imports
import os
import sys

# √ done mysterious place
# φ mysterious place

#FUNCTION
# Clear the console for sexier print
def clear():
    """
        This function clears the console depending on OS
    """

    if "win" in sys.platform.lower():
        os.system("cls")
    elif "linux" in sys.platform.lower():
        os.system("clear")

# Text color
# Red Text
def printRed(text):
    """
        Print text in Red
    """

    print("\033[91m {}\033[00m" .format(text))

# Yellow Text
def printYellow(text):
    """
        Print text in Yellow
    """

    print("\033[93m {}\033[00m" .format(text))

# Cyan Text
def printCyan(text):
    """
        Print text in Cyan
    """

    print("\033[96m {}\033[00m" .format(text))

# Light Gray Text
def printLightGray(text):
    """
        Print text in Light Gray
    """

    print("\033[97m {}\033[00m" .format(text)) 