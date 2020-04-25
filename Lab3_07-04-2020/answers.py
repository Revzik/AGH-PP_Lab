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
FOUR = 4
YES = 5
NO = 6
NONE = 7
UP = 8
DOWN = 9
LONGER = 10
SHORTER = 11
LEFT = 12
RIGHT = 13
REPEAT = 14


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
    elif answer == "4":
        return FOUR
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


def validate_channel_frequency(answer):
    if type(answer) is not str:
        print("Invalid value, please provide with correct (l/r (0-1500)): ")
        return [NONE, 0]
    elif answer.lower() == "q" or answer.lower() == "quit":
        return [QUIT, 0]
    elif answer.lower() == "rp" or answer.lower() == "repeat":
        return [REPEAT, 0]
    values = answer.split(" ")
    if len(values) == 2:
        channel = values[0].lower()
        try:
            frequency = float(values[1])
            if 0 < frequency < 1500:
                if channel == "l" or channel == "left":
                    return [LEFT, frequency]
                elif channel == "r" or channel == "right":
                    return [RIGHT, frequency]
                else:
                    print("Invalid channel provided (l/r (0-1500)): ")
            else:
                print("Invalid frequency (l/r (0-1500)): ")
        except ValueError:
            print("Invalid value, please provide with correct (l/r (0-1500)): ")
    else:
        print("Invalid value, please provide with correct (l/r (0-1500)): ")
    return [NONE, 0]
