"""
Framework class + methods for generating tones on PP course.

Authors:
 Bartłomiej Piekarz
 Daniel Tańcula
"""

import numpy as np
import sounddevice as sd


def from_log(value):
    return np.power(10, value / 20)


class SoundGenerator:
    def __init__(self, bitrate=8000):
        self.bitrate = bitrate

    def silence(self, duration=1):
        return np.zeros(int(duration * self.bitrate))

    def sin(self, frequency=1000, duration=1, phase=0, volume=0):
        t = np.linspace(0, duration, duration * self.bitrate, False)
        tone = self.ramp(np.sin(2 * np.pi * frequency * t))
        return tone * from_log(volume)

    def noise(self, duration=1, volume=0):
        noise = self.ramp(np.random.uniform(low=-1, high=1, size=int(duration * self.bitrate)))
        return noise * from_log(volume)

    def ramp(self, data, duration=0.01):
        ramp_length = int(self.bitrate * duration)
        data_length = data.size
        t_in = np.linspace(-np.pi, 0, ramp_length, False)
        t_out = np.linspace(0, np.pi, ramp_length, False)

        ramp = np.ones(data_length)
        ramp[0:ramp_length] = (1 + np.cos(t_in)) / 2
        ramp[(data_length - ramp_length):data_length] = (1 + np.cos(t_out)) / 2

        return np.multiply(ramp, data)

    def play_mono(self, data):
        try:
            sd.play(data, self.bitrate)
            sd.wait()
        except Exception as e:
            print(e)
