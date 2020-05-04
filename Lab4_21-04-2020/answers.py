"""
Answer validation + enums

Authors:
 Bartłomiej Piekarz
 Daniel Tańcula
 Tomasz Piaseczny
"""

from enum import Enum, auto


def validate_tasks(message):
    answer = input(message)
    if type(answer) is not str:
        print("Invalid value, please provide with correct (1/2/3/4/q): ")
        return Answers.NONE
    elif answer == "1":
        return Answers.ONE
    elif answer == "2":
        return Answers.TWO
    elif answer == "3":
        return Answers.THREE
    elif answer.lower() == "q" or answer.lower() == "quit":
        return Answers.QUIT
    else:
        print("Invalid value, please provide with correct (1/2/3/q): ")
        return Answers.NONE


def validate_yes_no(message):
    answer = input(message)
    if type(answer) is not str:
        print("Invalid value, please provide with correct (y/n): ")
        return Answers.NONE
    elif answer.lower() == "n" or answer.lower() == "no":
        return Answers.NO
    elif answer.lower() == "y" or answer.lower() == "yes":
        return Answers.YES
    else:
        print("Invalid value, please provide with correct (y/n): ")
        return Answers.NONE


def validate_loud_quiet(message):
    answer = input(message)
    if type(answer) is not str:
        print("Invalid value, please provide with correct (l/q/y): ")
        return Answers.NONE
    elif answer.lower() == "l" or answer.lower() == "louder":
        return Answers.UP
    elif answer.lower() == "q" or answer.lower() == "quieter":
        return Answers.DOWN
    elif answer.lower() == "y" or answer.lower() == "yes":
        return Answers.YES
    else:
        print("Invalid value, please provide with correct (l/q/y): ")
        return Answers.NONE


def validate_longer_shorter(message):
    answer = input(message)
    if type(answer) is not str:
        print("Invalid value, please provide with correct (l/s/y): ")
        return Answers.NONE
    elif answer.lower() == "l" or answer.lower() == "longer":
        return Answers.LONGER
    elif answer.lower() == "s" or answer.lower() == "shorter":
        return Answers.SHORTER
    elif answer.lower() == "y" or answer.lower() == "yes":
        return Answers.YES
    else:
        print("Invalid value, please provide with correct (l/s/y): ")
        return Answers.NONE


def empty(message):
    input(message)


class Answers(Enum):
    QUIT = auto()
    ONE = auto()
    TWO = auto()
    THREE = auto()
    FOUR = auto()
    YES = auto()
    NO = auto()
    NONE = auto()
    UP = auto()
    DOWN = auto()
    LONGER = auto()
    SHORTER = auto()
