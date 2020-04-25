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


def interaural_level_difference_task(reference_tone, reference_volume):
    all_volume = []
    all_turning_points = []
    volume = reference_volume - 6
    step = 1

    # getting down to the first turning point
    ans = NONE
    while ans != NO and volume < reference_volume:
        ans = NONE
        sg.play_stereo(np.hstack((reference_tone, sg.sin(volume=reference_volume))),
                       np.hstack((reference_tone, sg.sin(volume=volume))))
        all_volume.append(volume)
        log.debug("volume = " + str(volume) + "dB, step = " + str(step) + "dB")
        while ans == NONE:
            ans = validate_yes_no(input('Did you hear the sound source move? (y/n): '))
            if ans == YES:
                volume += step
            elif ans == NO:
                all_turning_points.append(volume)
                volume -= step

    turning_points = 1
    direction = 1
    next_down = False

    # counting next turning points using one up, two down method
    while turning_points < 16:
        ans = NONE
        sg.play_stereo(np.hstack((reference_tone, sg.sin(volume=reference_volume))),
                       np.hstack((reference_tone, sg.sin(volume=volume))))
        all_volume.append(volume)
        prev_volume = volume
        log.debug("volume = " + str(volume) + "dB, step = " + str(step) + "dB")
        log.debug("turning points = " + str(turning_points))
        while ans == NONE:
            ans = validate_yes_no(input('Did you hear difference in pitch? (y/n): '))

            # if the user no longer hears the difference, the level difference should decrease
            # if they begin to hear difference, we repeat the tone and then go down - that's what "next_down" does
            if ans == YES:
                if next_down:
                    volume += step
                    next_down = False
                else:
                    next_down = True
            elif ans == NO:
                volume -= step
                next_down = False

        # discriminating if there has been a change in direction
        if direction > 0 and volume > prev_volume or \
           direction < 0 and volume < prev_volume:
            turning_points += 1
            all_turning_points.append(prev_volume)
            direction *= -1
            if turning_points == 4:
                step = 0.5

        if volume >= reference_volume:
            volume = reference_volume

    return {"all volume": all_volume, "all turning points": all_turning_points}


def interaural_level_difference():
    volume = 0
    reference = np.hstack((sg.sin(volume=volume), sg.silence(0.5)))

    ans = NONE
    while ans == NONE:
        ans = validate_yes_no(input("Are you ready to begin? (y/n): "))
        if ans == NO:
            return
        elif ans == YES:
            return interaural_level_difference_task(reference, volume)


def interaural_time_difference_task(reference_tone, reference_phase):
    all_diff = []
    all_turning_points = []
    diff = reference_phase + 500
    step = 50

    # getting down to the first turning point
    ans = NONE
    while ans != NO or diff < reference_phase:
        ans = NONE
        sg.play_stereo(np.hstack((reference_tone, sg.sin(phase=reference_phase))),
                       np.hstack((reference_tone, sg.sin(phase=diff, phase_unit='us'))))
        all_diff.append(diff)
        log.debug("diff = " + str(diff) + "us, step = " + str(step) + "us")
        while ans == NONE:
            ans = validate_yes_no(input('Did you hear the sound source move? (y/n): '))
            if ans == YES:
                diff -= step
            elif ans == NO:
                all_turning_points.append(diff)
                diff += step

    turning_points = 1
    direction = 1
    next_down = False

    # counting next turning points using one up, two down method
    while turning_points < 16:
        ans = NONE
        sg.play_stereo(np.hstack((reference_tone, sg.sin(phase=reference_phase))),
                       np.hstack((reference_tone, sg.sin(phase=diff, phase_unit='us'))))
        all_diff.append(diff)
        prev_diff = diff
        log.debug("diff = " + str(diff) + "us, step = " + str(step) + "us")
        log.debug("turning points = " + str(turning_points))
        while ans == NONE:
            ans = validate_yes_no(input('Did you hear difference in pitch? (y/n): '))

            # if the user no longer hears the difference, the time difference should decrease
            # if they begin to hear difference, we repeat the tone and then go down - that's what "next_down" does
            if ans == YES:
                if next_down:
                    diff -= step
                    next_down = False
                else:
                    next_down = True
            elif ans == NO:
                diff += step
                next_down = False

        # discriminating if there has been a change in direction
        if direction < 0 and diff > prev_diff or\
           direction > 0 and diff < prev_diff:
            turning_points += 1
            all_turning_points.append(prev_diff)
            direction *= -1
            if turning_points == 4:
                step = 25

        if diff <= 0:
            diff = 0

    return {"all diff": all_diff, "all turning points": all_turning_points}


def interaural_time_difference():
    phase = 0
    reference = np.hstack((sg.sin(phase=phase, phase_unit='us'), sg.silence(duration=0.5)))

    ans = NONE
    while ans == NONE:
        ans = validate_yes_no(input("Are you ready to begin? (y/n): "))
        if ans == NO:
            return
        elif ans == YES:
            return interaural_time_difference_task(reference, phase)


def binaural_frequency_discrimination():
    return ""


def binaural_beats():
    log.msg("If you want to change channel frequency, provide channel and it's frequency (l/r (0-1500))")
    log.msg("If you want to repeat, provide \"rp\" or \"repeat\"")
    log.msg("When you experienced binaural beats, provide \"q\" or \"quit\"")

    f_left = 500.0
    f_right = 500.0
    duration = 5
    ans = [NONE, 0]
    while ans[0] != QUIT:
        ans = [NONE, 0]
        left = sg.sin(frequency=f_left, duration=duration)
        right = sg.sin(frequency=f_right, duration=duration)
        log.msg("Left frequency: " + str(f_left) + ", Right frequency: " + str(f_right))
        sg.play_stereo(left, right)

        while ans[0] == NONE:
            ans = validate_channel_frequency(input("Provide new frequency (l/r/rp (0-1500)): "))
            if len(ans) == 2 and ans[0] == LEFT:
                f_left = ans[1]
            elif len(ans) == 2 and ans[0] == RIGHT:
                f_right = ans[1]

    return "left: " + str(f_left) + "Hz, right: " + str(f_right) + "Hz"


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
                results.append("Task 1 - Interaural Level Difference:")
                results.append(result)
        elif ans == TWO:
            result = interaural_time_difference()
            if result is not None:
                results.append("Task 2 - Interaural Time Difference")
                results.append(result)
        elif ans == THREE:
            result = binaural_frequency_discrimination()
            if result is not None:
                results.append("Task 3 - Binaural frequency discrimination")
                results.append(result)
        elif ans == FOUR:
            result = binaural_beats()
            if result is not None:
                results.append("Task 4 - Binaural beats")
                results.append(result)

    save_results(results)


__main__()
