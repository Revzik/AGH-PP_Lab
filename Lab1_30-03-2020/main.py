"""
Script for Practical Psychoacoustics
Tasks 1-3 from 24.03.2020 - 31.03.2020 week

Authors:
 Bartłomiej Piekarz
 Daniel Tańcula
"""

from soundplayer import *
from answers import *

import numpy as np
import random


sg = SoundGenerator()


def intensity_discrimination_task(volumes, tones):
    i = 1
    for tone in tones:
        ans = NONE
        print("Playing tone " + str(i) + " of " + str(len(tones)))
        sg.play_mono(tone[1])
        while ans == NONE:
            ans = validate_yes_no(input("Did you hear any difference in loudness? (y/n): "))
            if ans == YES:
                volumes[tone[0]] += 1
        i += 1

    return volumes


def intensity_discrimination():
    """
    Generates a set of five different pairs of simple 1kHz tones, each repeated 10 times in random order
    User is told to distinguish the differences between the tones and mark answers

    :return: Dict containing number of correct answers per each volume difference
    """

    reference_volume = -3
    reference_tone = sg.sin(volume=reference_volume)
    silence = sg.silence(0.5)

    volumes = {0.25: 0,
               0.5: 0,
               1: 0,
               2: 0,
               3: 0}
    tones = []
    for volume in volumes.keys():
        for i in range(10):
            tones.append([volume, np.hstack((reference_tone, silence, sg.sin(volume=(reference_volume + volume))))])
    random.shuffle(tones)

    ans = NONE
    while ans == NONE:
        ans = validate_yes_no(input("Are you ready to begin? (y/n): "))
        if ans == NO:
            return
        elif ans == YES:
            return intensity_discrimination_task(volumes, tones)


def stevens_law_task(base_tone, volume):
    ans = NONE
    while ans == NONE:
        tone = sg.sin(3000, volume=volume)
        sg.play_mono(np.hstack((base_tone, tone)))
        while ans == NONE:
            ans = validate_up_down(input("Louder or more quiet? (u/d/y): "))
            if ans == UP:
                volume += 0.5
            elif ans == DOWN:
                volume -= 0.5
            elif ans == YES:
                return volume
        ans = NONE


def stevens_law():
    """
    Generates two tones. First of them is for reference.
    User has to set volume of the second tone to be twice as loud or twice as quiet as reference tone.

    :return: (float) Difference between sounds in decibels
    """

    reference_volume = -9
    reference_tone = sg.sin(3000, volume=reference_volume)
    silence = sg.silence(0.5)

    base_tone = np.hstack((reference_tone, silence))

    ans = NONE
    while ans == NONE:
        ans = validate_yes_no(input("Are you ready to begin? (y/n): "))
        if ans == NO:
            return
        elif ans == YES:
            return stevens_law_task(base_tone, reference_volume) - reference_volume


def hearing_adaptation_task(pre, post, duration):
    ans = NONE
    while ans == NONE:
        burst = sg.noise(duration, 0)
        sg.play_mono(np.hstack((pre, burst, post)))
        while ans == NONE:
            ans = validate_longer_shorter(input("Longer or shorter? (l/s/y): "))
            if ans == LONGER:
                duration += 0.25
            elif ans == SHORTER:
                duration -= 0.3
            elif ans == YES:
                return duration
        ans = NONE


def hearing_adaptation():
    """
    Generates two tones interrupted by louder noise.
    User needs to change the noise duration so the second tone appears clearly quieter.

    :return: (float) Duration of the noise in seconds
    """

    tone = sg.sin(volume=-6)
    silence = sg.silence(0.3)

    pre_burst = np.hstack((tone, silence))
    post_burst = np.hstack((silence, tone))
    noise_duration = 2

    ans = NONE
    while ans == NONE:
        ans = validate_yes_no(input("Are you ready to begin? (y/n): "))
        if ans == NO:
            return
        elif ans == YES:
            return hearing_adaptation_task(pre_burst, post_burst, noise_duration)


def save_results(results):
    with open("results.txt", "w+") as f:
        for item in results:
            f.write(str(item) + "\n")
            if type(item) is not str or not item.startswith("Task"):
                f.write("\n")


def __main__():
    results = []
    prompt = "Which task would you like to perform: \n" \
             " 1 - Intensity discrimination \n" \
             " 2 - Stevens law \n" \
             " 3 - Hearing adaptation \n" \
             "To quit provide \"q\" (1/2/3): "
    ans = NONE
    while ans != QUIT:
        ans = validate_tasks(input(prompt))
        if ans == ONE:
            result = intensity_discrimination()
            if result is not None:
                results.append("Task 1 - Intensity discrimination:")
                results.append(result)
        elif ans == TWO:
            result = stevens_law()
            if result is not None:
                results.append("Task 2 - Stevens law")
                results.append(result)
        elif ans == THREE:
            result = hearing_adaptation()
            if result is not None:
                results.append("Task 3 - Hearing adaptation")
                results.append(result)

    save_results(results)

__main__()
