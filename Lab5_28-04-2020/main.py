"""
Script for Practical Psychoacoustics
Lab5 - Complex Sounds Related Issues
28.04.2020

Authors:
 Bartłomiej Piekarz
 Daniel Tańcula
 Tomasz Piaseczny
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


def percieved_pitch_task(reference_frequency,hct,duration):

    all_cents = []
    all_turning_points = []
    cents = 0
    step = 8
    simple_tone = sg.sin(frequency=reference_frequency,duration=duration)
    hct = sg.hct(frequency=reference_frequency,duration=duration)
    # getting down to the first turning point
    ans = NONE
    while ans != NO or cents < 0:
        ans = NONE
        sg.play_mono(np.hstack((sg.sin(frequency=,duration=duration),sg.silence(duration=0.5), sg.hct(frequency=reference_frequency,duration=duration))))
        all_cents.append(cents)
        log.debug("frequency = " + str(change_pith(reference_frequency, cents)))
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
        sg.play_mono(np.hstack((simple_tone_tone, hct)))
        all_cents.append(cents)
        prev_cents = cents
        log.debug("frequency = " + str(change_pith(reference_frequency, cents)))
        log.debug("next_down = " + str(next_down))
        log.debug("step = " + str(step) + ", turning_points = " + str(turning_points))

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
                step = 4

        if cents <= 0:
            cents = 0

    return {"all_cents: ": all_cents, "all_turning_points": all_turning_points}

def percieved_pitch():

    reference_frequency = 1000
    duration = 2
    harmonics = [1, 2, 3, 4, 5]


    prompt = "You will be played two stereo tones separated by half a second of silence. " + \
             "First one will be the reference, and second one will have a difference in pitch between left and right channel" + \
             "You will have to answer whether you hear the difference or not by providing \"y\" for yes or \"n\" for no."
    log.msg(prompt)

    frequency = 1000
    reference = np.hstack((sg.sin(frequency=frequency), sg.silence(duration=0.5)))

    ans = NONE
    while ans == NONE:
        ans = validate_yes_no(input("Are you ready to begin? (y/n): "))
        if ans == NO:
            return
        elif ans == YES:
            return percieved_pitch_task(reference_frequency,duration)



def perceived_loudness_task(reference_hct, reference_volume, frequency, duration):
    all_volume = []
    all_turning_points = []
    volume = reference_volume
    step = 1

    # getting down to the first turning point
    ans = NONE
    while ans != YES or volume < 0:
        ans = NONE
        sg.play_mono(np.hstack((sg.sin(frequency=frequency, duration=duration, volume=volume), reference_hct)))
        all_volume.append(volume)
        log.debug("volume difference = " + str(np.abs(volume - reference_volume)))
        while ans == NONE:
            ans = validate_yes_no(input('Are the sounds equal in volume? (y/n): '))
            if ans == YES:
                volume -= step
            elif ans == NO:
                all_turning_points.append(volume)
                volume += step

    turning_points = 1
    direction = -1
    next_down = False

    # counting next turning points using one up, two down method
    while turning_points < 16:
        ans = NONE
        sg.play_mono(np.hstack((sg.sin(frequency=frequency, duration=duration, volume=volume), reference_hct)))
        all_volume.append(volume)
        prev_volume = volume
        log.debug("frequency = " + str(change_pith(reference_frequency, volume)))
        log.debug("next_down = " + str(next_down))
        log.debug("step = " + str(step) + ", turning_points = " + str(turning_points))

        while ans == NONE:
            ans = validate_yes_no(input('Did you hear difference in pitch? (y/n): '))

            # if the user no longer hears the difference, the frequency should immediately go higher
            # if he begins to hear difference, we repeat the tone and then go down - that's what "next_down" does
            if ans == YES:
                if next_down:
                    volume -= step
                    next_down = False
                else:
                    next_down = True
            elif ans == NO:
                volume += step
                next_down = False

        # discriminating if there has been a change in direction
        if direction < 0 and volume > prev_volume or\
           direction > 0 and volume < prev_volume:
            turning_points += 1
            all_turning_points.append(prev_volume)
            direction *= -1
            if turning_points == 4:
                step = 4

        if volume <= 0:
            volume = 0

    return {"all_volume: ": all_volume, "all_turning_points": all_turning_points}


def perceived_loudness():
    frequency = 1000
    duration = 2
    volume = -6
    harmonics = [1, 2, 3, 4, 5]

    silence = sg.silence(duration=0.5)
    hct = sg.hct(frequency=frequency, duration=duration, volume=volume, harmonics=harmonics)
    reference = np.hstack((silence, hct))

    ans = NONE
    while ans == NONE:
        ans = validate_yes_no(input("Are you ready to begin? (y/n): "))
        if ans == NO:
            return
        elif ans == YES:
            return perceived_loudness_task(reference, volume, frequency, duration)


def residual_pitch():
    frequency = 1000
    duration = 2
    volume = -6
    harmonics = [2, 3, 4, 5]

    silence = sg.silence(duration=0.5)
    hct = sg.hct(frequency=frequency, duration=duration, volume=volume, harmonics=harmonics)




def save_results(results):
    with open("results.txt", "w+") as f:
        for item in results:
            f.write(str(item) + "\n")
            if type(item) is not str or not item.startswith("Task"):
                f.write("\n")
    log.info("\nTask finished, results are in \"results.txt\" file.")


def __main__():
    results = []
    prompt = "To quit provide \"q\": "
    ans = NONE
    while ans != QUIT:
        ans = validate_tasks(input(prompt))

    save_results(results)


__main__()
