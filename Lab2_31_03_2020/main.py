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
args = parser.parse_args()

logging_mode = Logger.INFO
if args.debug:
    logging_mode = Logger.DEBUG
logger = Logger(logging_mode)

sg = SoundGenerator()


def const_stimuli_task(pitches, tones):

    i = 1
    for tone in tones:
        ans = NONE
        print("Playing tone " + str(i) + " of " + str(len(tones)))
        sg.play_mono(tone[1])
        while ans == NONE:
            ans = validate_first_second(input("Which tone is higher? (f/s): "))
            if ans == SECOND and tone[0] > 0:
                pitches[tone[0]] += 1
            elif ans == FIRST and tone[0] < 0:
                pitches[tone[0]] += 1
        i += 1

    return pitches


def const_stimuli():

    prompt = "\nThis task checks your frequency discrimination - constant stimuli method.\n" \
             "You will be played a series of two simple tones. First one is reference and the second has a different frequency. \n" \
             "Your task is to distinguish the differences in pitch. \n" \
             "If first sound is higher type \"f\" (first), if second, type \"second\" (second)."

    print(prompt)
    reference_frequency = 1000
    reference_tone = sg.sin(frequency=reference_frequency, volume=0)
    silence = sg.silence(0.5)

    pitches = {2: 0,
               -5: 0,
               8: 0,
               11: 0,
               -14: 0}

    tones = []
    for pitch in pitches.keys():
        for i in range(10):
            tones.append([pitch, np.hstack((reference_tone, silence, sg.sin(frequency=change_pith(reference_frequency, pitch))))])
    random.shuffle(tones)

    ans = NONE
    while ans == NONE:
        ans = validate_yes_no(input("Are you ready to begin? (y/n): "))
        if ans == NO:
            return None
        elif ans == YES:
            return const_stimuli_task(pitches, tones)


def one_up_two_down_task(reference_tone, reference_frequency):
    all_cents = []
    all_turning_points = []
    cents = 50
    step = 6

    # getting down to the first turning point
    ans = NONE
    while ans != NO or cents < 0:
        ans = NONE
        sg.play_mono(np.hstack((reference_tone, sg.sin(frequency=change_pith(reference_frequency, cents)))))
        all_cents.append(cents)
        logger.log_debug("frequency = " + str(change_pith(reference_frequency, cents)))
        while ans == NONE:
            ans = validate_yes_no(input('Did you hear difference in pitch? (y/n): '))
            if ans == YES:
                cents -= step
            elif ans == NO:
                all_turning_points.append(cents)
                cents += step

    if cents <= 0:
        cents = 0

    turning_points = 1
    direction = 1
    next_down = False

    # counting next turning points using one up, two down method
    while turning_points < 16:
        ans = NONE
        sg.play_mono(np.hstack((reference_tone, sg.sin(frequency=change_pith(reference_frequency, cents)))))
        all_cents.append(cents)
        prev_cents = cents
        logger.log_debug("frequency = " + str(change_pith(reference_frequency, cents)))
        logger.log_debug("next_down = " + str(next_down))
        logger.log_debug("step = " + str(step) + ", turning_points = " + str(turning_points))

        while ans == NONE:
            ans = validate_yes_no(input('Did you hear difference in pitch? (y/n): '))

            # if the user no longer hears the difference, the frequency should immediately go higher
            # if he begins to hear difference, we repeat the tone and then go down - that's what "next_down" does
            if ans == YES:
                if next_down:
                    cents -= step
                    next_down = False
                else:
                    next_down = True
            elif ans == NO:
                cents += step
                next_down = False

        # discriminating if there has been a change in direction
        if direction < 0 and cents > prev_cents or\
           direction > 0 and cents < prev_cents:
            turning_points += 1
            all_turning_points.append(prev_cents)
            direction *= -1
            if turning_points == 4:
                step = 3

        if cents <= 0:
            cents = 1

    return {"all_cents: ": all_cents, "all_turning_points": all_turning_points}


def one_up_two_down():
    prompt = "\nThis task checks your frequency discrimination - adaptive method.\n" \
             "You will be played series of two simple tones which vary in frequency. \n" \
             "Your task is to distinguish the differences in hight. \n" \
             "If you can hear the difference, confirm with \"y\" (yes), if not, type \"n\" (no)."

    print(prompt)
    reference_frequency = 1000
    reference_tone = sg.sin(frequency=reference_frequency, volume=0)
    silence = sg.silence(0.5)

    ans = NONE
    while ans == NONE:
        ans = validate_yes_no(input("Are you ready to begin? (y/n): "))
        if ans == NO:
            return NONE
        elif ans == YES:
            return one_up_two_down_task(np.hstack((reference_tone, silence)), reference_frequency)


def save_results(results):
    with open("results.txt", "w+") as f:
        for item in results:
            f.write(str(item) + "\n")
            if type(item) is not str or not item.startswith("Task"):
                f.write("\n")
    print("\nTask finished, results are in \"results.txt\" file.")


def __main__():
    results = []
    prompt = "Which task would you like to perform: \n" \
             " 1 - IFC Task, constant stimuli method \n" \
             " 2 - IFC Task, adaptive method \n" \
             "To quit provide \"q\" (1/2/q): "
    ans = NONE
    while ans != QUIT:
        ans = validate_tasks(input(prompt))
        if ans == ONE:
            result = const_stimuli()
            if result is not None:
                results.append("Task 1 - IFC Task, constant stimuli method")
                results.append(result)
        elif ans == TWO:
            result = one_up_two_down()
            if result is not None:
                results.append("Task 2 - IFC Task, adaptive method")
                results.append(result)

    save_results(results)


__main__()
