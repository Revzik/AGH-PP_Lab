"""
Script for Practical Psychoacoustics

Authors:
 Bartłomiej Piekarz
 Daniel Tańcula
 Tomasz Piaseczny
"""

from soundplayer import *
from answers import *
from logger import Logger

import numpy as np
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


def play_masked_tone(noise, tone_frequency, tone_volume):
    silencio = sg.silence(duration=0.25)
    tone = sg.sin(frequency=tone_frequency, duration=0.5, volume=tone_volume)
    sound = np.hstack((silencio, tone, silencio))
    combined = noise + sound
    sg.play_mono(combined)


def broadband_noise_task(noise, tone_freq, reference_volume):
    all_volume = []
    all_turning_points = []
    volume = reference_volume
    step = 4

    # getting down to the first turning point
    ans = Answers.NONE
    while ans != Answers.NO:
        ans = Answers.NONE
        play_masked_tone(noise, tone_freq, volume)
        all_volume.append(volume)
        log.debug("volume = " + str(volume) + "dB, step = " + str(step) + "dB")
        while ans == Answers.NONE:
            ans = validate_yes_no('Did you hear the tone? (y/n): ')
            if ans == Answers.YES:
                volume -= step
            elif ans == Answers.NO:
                all_turning_points.append(volume)
                volume += step

    turning_points = 1
    direction = 1
    next_down = False

    # counting next turning points using one up, two down method
    while turning_points < 16:
        ans = Answers.NONE
        play_masked_tone(noise, tone_freq, volume)
        all_volume.append(volume)
        prev_volume = volume
        log.debug("volume = " + str(volume) + "dB, step = " + str(step) + "dB")
        log.debug("turning points = " + str(turning_points))
        while ans == Answers.NONE:
            ans = validate_yes_no('Did you hear the tone? (y/n): ')

            # if the user no longer hears the difference, the level difference should decrease
            # if they begin to hear difference, we repeat the tone and then go down - that's what "next_down" does
            if ans == Answers.YES:
                if next_down:
                    volume -= step
                    next_down = False
                else:
                    next_down = True
            elif ans == Answers.NO:
                volume += step
                next_down = False

        # discriminating if there has been a change in direction
        if direction > 0 and volume > prev_volume or \
           direction < 0 and volume < prev_volume:
            turning_points += 1
            all_turning_points.append(prev_volume)
            direction *= -1
            if turning_points == 4:
                step = 2

    empty('Now the noise will be removed, proceed when ready: ')
    ans = Answers.NONE
    sg.play_mono(sg.sin(frequency=tone_freq, volume=volume))
    while ans == Answers.NONE:
        ans = validate_yes_no('Could you hear the tone? (y/n): ')

    return {"all volume": all_volume, "all turning points": all_turning_points, "pure tone audible: ": ans == Answers.YES}


def sim_masking_broadband_noise():
    prompt = "You will be played a tone mixed with noise.\n" + \
             "You will have to answer whether you or not you can hear the tone in the noise\n" + \
             "Answer by providing \"y\" for yes or \"n\" for no."
    log.msg(prompt)

    noise_volume = -6
    tone_volume = 0
    tone_frequency = 1000
    noise = sg.noise(duration=1, volume=noise_volume)

    ans = Answers.NONE
    while ans == Answers.NONE:
        ans = validate_yes_no("Are you ready to begin? (y/n): ")
        if ans == Answers.NO:
            return
        elif ans == Answers.YES:
            return broadband_noise_task(noise, tone_frequency, tone_volume)


def bandpassed_noise_task(noise, tone_freq, reference_volume):
    all_volume = []
    all_turning_points = []
    volume = reference_volume
    step = 4

    # getting down to the first turning point
    ans = Answers.NONE
    while ans != Answers.NO:
        ans = Answers.NONE
        play_masked_tone(noise, tone_freq, volume)
        all_volume.append(volume)
        log.debug("volume = " + str(volume) + "dB, step = " + str(step) + "dB")
        while ans == Answers.NONE:
            ans = validate_yes_no('Did you hear the tone? (y/n): ')
            if ans == Answers.YES:
                volume -= step
            elif ans == Answers.NO:
                all_turning_points.append(volume)
                volume += step

    turning_points = 1
    direction = 1
    next_down = False

    # counting next turning points using one up, two down method
    while turning_points < 16:
        ans = Answers.NONE
        play_masked_tone(noise, tone_freq, volume)
        all_volume.append(volume)
        prev_volume = volume
        log.debug("volume = " + str(volume) + "dB, step = " + str(step) + "dB")
        log.debug("turning points = " + str(turning_points))
        while ans == Answers.NONE:
            ans = validate_yes_no('Did you hear the tone? (y/n): ')

            # if the user no longer hears the difference, the level difference should decrease
            # if they begin to hear difference, we repeat the tone and then go down - that's what "next_down" does
            if ans == Answers.YES:
                if next_down:
                    volume -= step
                    next_down = False
                else:
                    next_down = True
            elif ans == Answers.NO:
                volume += step
                next_down = False

        # discriminating if there has been a change in direction
        if direction > 0 and volume > prev_volume or \
           direction < 0 and volume < prev_volume:
            turning_points += 1
            all_turning_points.append(prev_volume)
            direction *= -1
            if turning_points == 4:
                step = 2

    empty('Now the noise will be removed, proceed when ready: ')
    ans = Answers.NONE
    sg.play_mono(sg.sin(frequency=tone_freq, volume=volume))
    while ans == Answers.NONE:
        ans = validate_yes_no('Could you hear the tone? (y/n): ')

    return {"all volume": all_volume, "all turning points": all_turning_points, "pure tone audible: ": ans == Answers.YES}


def sim_masking_bandpassed_noise():
    prompt = "You will be played a tone mixed with a bandpassed noise.\n" + \
             "You will have to answer whether you or not you can hear the tone in the noise\n" + \
             "Answer by providing \"y\" for yes or \"n\" for no."
    log.msg(prompt)

    noise_volume = 0
    tone_volume = 0
    tone_frequency = 1100
    noise = sg.bandpas(sg.noise(duration=1, volume=noise_volume), 800, 1000)

    ans = Answers.NONE
    while ans == Answers.NONE:
        ans = validate_yes_no("Are you ready to begin? (y/n): ")
        if ans == Answers.NO:
            return
        elif ans == Answers.YES:
            return bandpassed_noise_task(noise, tone_frequency, tone_volume)


def post_masking_task(noise, gap_duration, tone):
    all_duration = []
    all_turning_points = []
    duration = gap_duration
    step = 0.1

    # getting down to the first turning point
    ans = Answers.NONE
    while ans != Answers.NO and duration > 0:
        ans = Answers.NONE
        sg.play_mono(np.hstack((noise, sg.silence(duration), tone)))
        all_duration.append(duration)
        log.debug("duration = " + str(duration) + "s, step = " + str(step) + "s")
        while ans == Answers.NONE:
            ans = validate_yes_no('Did you hear the tone? (y/n): ')
            if ans == Answers.YES:
                duration -= step
            elif ans == Answers.NO:
                all_turning_points.append(duration)
                duration += step

    if duration <= 0:
        duration = 0.01

    turning_points = 1
    direction = 1
    next_down = False

    # counting next turning points using one up, two down method
    while turning_points < 16:
        ans = Answers.NONE
        sg.play_mono(np.hstack((noise, sg.silence(duration), tone)))
        all_duration.append(duration)
        prev_duration = duration
        log.debug("duration = " + str(duration) + "s, step = " + str(step) + "s")
        log.debug("turning points = " + str(turning_points))
        while ans == Answers.NONE:
            ans = validate_yes_no('Did you hear the tone? (y/n): ')

            # if the user no longer hears the difference, the level difference should decrease
            # if they begin to hear difference, we repeat the tone and then go down - that's what "next_down" does
            if ans == Answers.YES:
                if next_down:
                    duration -= step
                    next_down = False
                else:
                    next_down = True
            elif ans == Answers.NO:
                duration += step
                next_down = False

            if duration <= 0:
                duration = 0.01

        # discriminating if there has been a change in direction
        if direction > 0 and duration > prev_duration or \
           direction < 0 and duration < prev_duration:
            turning_points += 1
            all_turning_points.append(prev_duration)
            direction *= -1
            if turning_points == 4:
                step = 0.05

    empty('Now the noise will be removed, proceed when ready: ')
    ans = Answers.NONE
    sg.play_mono(tone)
    while ans == Answers.NONE:
        ans = validate_yes_no('Could you hear the tone? (y/n): ')

    return {"all volume": all_duration, "all turning points": all_turning_points, "pure tone audible: ": ans == Answers.YES}


def post_masking():
    noise_volume = 0
    noise_duration = 2
    tone_volume = 0
    tone_frequency = 1000
    tone_duration = 0.20  # shorter cannot be played
    gap_duration = 0.8
    noise = sg.bandpas(sg.noise(duration=noise_duration, volume=noise_volume), 800, 1200)
    tone = sg.sin(frequency=tone_frequency, duration=tone_duration, volume=tone_volume)

    ans = Answers.NONE
    while ans == Answers.NONE:
        ans = validate_yes_no("Are you ready to begin? (y/n): ")
        if ans == Answers.NO:
            return
        elif ans == Answers.YES:
            return post_masking_task(noise, gap_duration, tone)


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
             " 1 - Simultaneous masking - tone vs broadband noise \n" \
             " 2 - Simultaneous masking - tone vs bandpassed noise \n" \
             " 3 - Post masking \n" \
             "To quit provide \"q\" (1/2/3/q): "
    ans = Answers.NONE
    while ans != Answers.QUIT:
        ans = validate_tasks(prompt)
        if ans == Answers.ONE:
            result = sim_masking_broadband_noise()
            if result is not None:
                results.append("Task 1 - Simultaneous masking - tone vs broadband noise:")
                results.append(result)
        if ans == Answers.TWO:
            result = sim_masking_bandpassed_noise()
            if result is not None:
                results.append("Task 2 - Simultaneous masking - tone vs broadband noise:")
                results.append(result)
        if ans == Answers.THREE:
            result = post_masking()
            if result is not None:
                results.append("Task 3 - Post masking:")
                results.append(result)

    save_results(results)


__main__()
