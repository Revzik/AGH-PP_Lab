"""
Script for Practical Psychoacoustics
Tasks 1-3 from 24.03.2020 - 31.03.2020 week

Authors:
 Bartłomiej Piekarz
 Daniel Tańcula
"""

from soundplayer import *
from answers import *
from logger import Logger

import numpy as np
import random
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--debug', '-d', action='store_true')
parser.add_argument('--silent', '-s', action='store_true')
args = parser.parse_args()

logging_mode = Logger.MESSAGE
if args.silent:
    logging_mode = Logger.INFO
if args.debug:
    logging_mode = Logger.DEBUG
log = Logger(logging_mode)

sg = SoundGenerator(silent=args.silent)


def interaural_level_difference_task(left, volume, step, step_change):
    ans = NONE
    prev_ans = YES
    while ans == NONE:
        right = sg.sin(frequency=1000, duration=1, volume=volume)
        sg.play_stereo(left, right)
        while ans == NONE:
            ans = validate_yes_no(input('Did you hear change in the sound direction ? (y/n): '))
            if ans == NONE:
                log.info('Invalid argument')
            elif ans == prev_ans:
                volume += step
            else:
                step *= -step_change
        prev_ans = ans
        ans = NONE
    return


def interaural_level_difference():
    step = -2
    step_change = 0.3
    volume = -6

    left = sg.sin(frequency=1000, duration=1, volume=volume)

    volume = 0

    ans = NONE
    while ans == NONE:
        ans = validate_yes_no(input("Are you ready to begin? (y/n): "))
        if ans == NO:
            return
        elif ans == YES:
            return interaural_level_difference_task(left, volume, step, step_change)


def interaural_time_difference():
    return ""


def binaural_frequency_discrimination():
    return ""


def binaural_beats():
    return ""


def save_results(results):
    with open("results.txt", "w+") as f:
        for item in results:
            f.write(str(item) + "\n")
            if type(item) is not str or not item.startswith("Task"):
                f.write("\n")
    log.info("\nTask finished, results are in \"results.txt\" file.")


def __main__():
    results = []
    prompt = "Which task would you like to perform: \n" \
             " 1 - Interaural Level Difference \n" \
             " 2 - Interaural Time Difference \n" \
             " 3 - Binaural frequency discrimination \n" \
             " 4 - Binaural beats \n" \
             "To quit provide \"q\" (1/2/3/4): "
    ans = NONE
    while ans != QUIT:
        ans = validate_tasks(input(prompt))
        if ans == ONE:
            result = interaural_level_difference()
            if result is not None:
                results.append("Task 1 - Intensity discrimination:")
                results.append(result)
        elif ans == TWO:
            result = interaural_time_difference()
            if result is not None:
                results.append("Task 2 - Stevens law")
                results.append("dB: " + str(result) + "; abs: " + str(from_db(result)))
        elif ans == THREE:
            result = binaural_frequency_discrimination()
            if result is not None:
                results.append("Task 3 - Hearing adaptation")
                results.append(result)
        elif ans == FOUR:
            result = binaural_beats()
            if result is not None:
                results.append("Task 4 - Binaural beats")
                results.append(result)

    save_results(results)


__main__()
