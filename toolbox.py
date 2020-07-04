# coding: utf-8

# Imports
import os
import sys

# 🏝️

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
    print("\033[91m {}\033[00m" .format(text))

# Yellow Text
def printYellow(text): 
    print("\033[93m {}\033[00m" .format(text))

# Cyan Text
def printCyan(text): 
    print("\033[96m {}\033[00m" .format(text))

# Light Gray Text
def printLightGray(text): 
    print("\033[97m {}\033[00m" .format(text)) 