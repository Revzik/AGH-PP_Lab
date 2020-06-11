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

sg = SoundGenerator(silent=args.silent, bitrate=44100)


def percieved_pitch_task(reference_frequency,duration,harmonics):

    all_cents = []
    all_turning_points = []
    cents = 0
    step = 6
    answer = ""
    # getting down to the first turning point
    ans = NONE
    while ans != YES or cents < 0:
        ans = NONE
        sg.play_mono(np.hstack((sg.sin(frequency=change_pith(reference_frequency,cents),duration=duration),sg.silence(duration=0.5), sg.hct(frequency=reference_frequency,duration=duration,harmonics=harmonics))))
        all_cents.append(cents)
        log.debug("frequency = " + str(change_pith(reference_frequency, cents)))
        while ans == NONE:
            ans = validate_yes_no(input('Are the tones equal in frequency or the first tone is higher? (y/n): '))
            if ans == YES:
                all_turning_points.append(cents)
                cents -= step
            elif ans == NO:
                cents += step

    if cents <= 0:
        cents = 0

    turning_points = 1
    direction = 1
    next_down = False

    # counting next turning points using one up, two down method
    while turning_points < 16:
        ans = NONE
        sg.play_mono(np.hstack((sg.sin(frequency=change_pith(reference_frequency,cents),duration=duration),sg.silence(duration=0.5), sg.hct(frequency=reference_frequency,duration=duration,harmonics=harmonics))))
        all_cents.append(cents)
        prev_cents = cents
        log.debug("frequency = " + str(change_pith(reference_frequency, cents)))
        log.debug("next_down = " + str(next_down))
        log.debug("step = " + str(step) + ", turning_points = " + str(turning_points))

        while ans == NONE:
            ans = validate_yes_no(input('Are the tones equal in frequency or the first tone is higher? (y/n): '))

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
            cents = 0

    original = sg.hct(frequency=reference_frequency, duration=duration, harmonics=harmonics)
    harmonics.remove(np.random.randint(1, len(harmonics)))
    harmonics.remove(np.random.randint(1, len(harmonics)))
    without_harmonics = sg.hct(frequency=reference_frequency, duration=duration, harmonics=harmonics)
    sg.play_mono(np.hstack((original, sg.silence(duration=0.5), without_harmonics)))
    answer = validate_yes_no(input("Is second tone pitch different from first?"))

    return {"all_cents: ": all_cents, "all_turning_points": all_turning_points, "Does the pitch change": answer == YES}


def percieved_pitch():
    reference_frequency = 1000
    duration = 2
    harmonics = [1, 2, 3, 4, 5]

    prompt = "You will be played simple tone and Harmonic Complex Tone separated by half a second of silence. " + \
             "You will have to answer whether you hear the difference in pitch or not by providing \"y\" for yes or \"n\" for no."
    log.msg(prompt)

    ans = NONE
    while ans == NONE:
        ans = validate_yes_no(input("Are you ready to begin? (y/n): "))
        if ans == NO:
            return
        elif ans == YES:
            return percieved_pitch_task(reference_frequency,duration,harmonics)


def perceived_loudness_task(reference_hct, reference_volume, frequency, duration):
    all_volume = []
    all_turning_points = []
    volume = reference_volume
    step = 1

    log.debug("hct amplitude = {:3f} - {:3f}".format(np.min(reference_hct), np.max(reference_hct)))

    # getting down to the first turning point
    ans = NONE
    while ans != YES and volume < 0:
        ans = NONE
        sg.play_mono(np.hstack((sg.sin(frequency=frequency, duration=duration, volume=volume), reference_hct)))
        all_volume.append(volume)
        log.debug("volume difference = " + str(np.abs(volume - reference_volume)))
        while ans == NONE:
            ans = validate_yes_no(input('Are the sounds equal in volume or the first one is louder? (y/n): '))
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
        log.debug("volume difference = " + str(np.abs(volume - reference_volume)))
        log.debug("next_down = " + str(next_down))
        log.debug("step = " + str(step) + ", turning_points = " + str(turning_points))

        while ans == NONE:
            ans = validate_yes_no(input('Are the sounds equal in volume or the first one is louder? (y/n): '))

            # if the user no longer hears the difference, the volume should immediately go lower
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
                step = 0.5

    return {"all_volume: ": all_volume, "all_turning_points": all_turning_points}


def perceived_loudness():
    frequency = 1000
    duration = 2
    volume = -6
    harmonics = [1, 2, 3, 4, 5]

    prompt = "You will be played simple tone and Harmonic Complex Tone separated by half a second of silence. " + \
             "You will have to answer whether you hear the difference in loudnes or not by providing \"y\" for yes or \"n\" for no."
    log.msg(prompt)

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
    original_harmonics = [1, 2, 3, 4, 5]
    harmonics = [2, 3, 4, 5]

    prompt = "You will be played two Harmonic Complex Tones separated by half a second of silence." + \
             "The second tone will be played without its fundamental frequency." + \
             "You will have to answer whether you hear the difference in pitch or not by providing \"y\" for yes or \"n\" for no."
    log.msg(prompt)

    ans = NONE
    while ans == NONE:
        ans = validate_yes_no(input("Are you ready to begin? (y/n): "))
        if ans == NO:
            return

    silence = sg.silence(duration=0.5)

    ans = NONE
    sg.play_mono(np.hstack((sg.hct(frequency=frequency, duration=duration, volume=volume, harmonics=original_harmonics),
                            silence,
                            sg.hct(frequency=frequency, duration=duration, volume=volume, harmonics=harmonics))))
    while ans == NONE:
        ans = validate_yes_no(input('Do you hear difference in pitch? (y/n): '))
        if ans == NO:
            return {"Difference perceived": False}

    for i in range(len(harmonics) - 1):
        ans = NONE
        sg.play_mono(np.hstack((sg.hct(frequency=frequency, duration=duration, volume=volume, harmonics=original_harmonics),
                                silence,
                                sg.hct(frequency=frequency, duration=duration, volume=volume, harmonics=harmonics))))
        while ans == NONE:
            ans = validate_yes_no(input('Can you hear residual pitch? (y/n): '))
            if ans == YES:
                return {"Difference perceived": True, "Residual pitch perceived": True, "harmonics": harmonics}
            elif ans == NO:
                harmonics.pop(len(harmonics) - 1)

    return {"Difference perceived": True, "Residual pitch perceived": False}


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
             " 1 - Perceived pitch \n" \
             " 2 - Perceived loudness \n" \
             " 3 - Residual pitch \n" \
             "To quit provide \"q\": "
    ans = NONE
    while ans != QUIT:
        ans = validate_tasks(input(prompt))
        if ans == ONE:
            result = percieved_pitch()
            if result is not None:
                results.append("Task 1 - Perceived pitch:")
                results.append(result)
        elif ans == TWO:
            result = perceived_loudness()
            if result is not None:
                results.append("Task 2 - Perceived loudness")
                results.append(result)
        elif ans == THREE:
            result = residual_pitch()
            if result is not None:
                results.append("Task 3 - Residual pitch")
                results.append(result)

    save_results(results)


__main__()
