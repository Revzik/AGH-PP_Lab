"""
Answer validation + enums

Authors:
 Bartłomiej Piekarz
 Daniel Tańcula
 Tomasz Piaseczny
"""


QUIT = 0
ONE = 1
TWO = 2
THREE = 3
FOUR = 4
YES = 5
NO = 6
NONE = 7
UP = 8
DOWN = 9
LONGER = 10
SHORTER = 11


def validate_tasks(answer):
    if type(answer) is not str:
        print("Invalid value, please provide with correct (1/2/3/4/q): ")
        return NONE
    elif answer == "1":
        return ONE
    elif answer == "2":
        return TWO
    elif answer == "3":
        return THREE
    elif answer.lower() == "q" or answer.lower() == "quit":
        return QUIT
    else:
        print("Invalid value, please provide with correct (1/2/3/4/q): ")
        return NONE


def validate_yes_no(answer):
    if type(answer) is not str:
        print("Invalid value, please provide with correct (y/n): ")
        return NONE
    elif answer.lower() == "n" or answer.lower() == "no":
        return NO
    elif answer.lower() == "y" or answer.lower() == "yes":
        return YES
    else:
        print("Invalid value, please provide with correct (y/n): ")
        return NONE


def validate_loud_quiet(answer):
    if type(answer) is not str:
        print("Invalid value, please provide with correct (l/q/y): ")
        return NONE
    elif answer.lower() == "l" or answer.lower() == "louder":
        return UP
    elif answer.lower() == "q" or answer.lower() == "quieter":
        return DOWN
    elif answer.lower() == "y" or answer.lower() == "yes":
        return YES
    else:
        print("Invalid value, please provide with correct (l/q/y): ")
        return NONE


def validate_longer_shorter(answer):
    if type(answer) is not str:
        print("Invalid value, please provide with correct (l/s/y): ")
        return NONE
    elif answer.lower() == "l" or answer.lower() == "longer":
        return LONGER
    elif answer.lower() == "s" or answer.lower() == "shorter":
        return SHORTER
    elif answer.lower() == "y" or answer.lower() == "yes":
        return YES
    else:
        print("Invalid value, please provide with correct (l/s/y): ")
        return NONE
