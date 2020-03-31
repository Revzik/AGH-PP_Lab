"""
Answer validation + enums

Authors:
 Bartłomiej Piekarz
 Daniel Tańcula
"""

QUIT = 0
ONE = 1
TWO = 2
THREE = 3
YES = 4
NO = 5
NONE = 6
UP = 7
DOWN = 8
LONGER = 9
SHORTER = 10


def validate_tasks(answer):
    if type(answer) is not str:
        print("Invalid value, please provide with correct (1/2/3): ")
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
        print("Invalid value, please provide with correct (1/2/3): ")
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
