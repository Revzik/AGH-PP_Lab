import matplotlib.pyplot as plt
import numpy as np

# reference values
ref_level = 1.0
ref_time = 0
ref_freq = 1000

# results Bartek
# 1
level_diff_bartek = np.abs([-6, -5, -4, -3, -2, -3, -3, -2, -2, -1, -2, -2, -1, -1.5, -1.5, -1.0, -1.5, -2.0, -2.0, -1.5, -1.5, -1.0, -1.0, -1.5, -1.5, -2.0, -2.0, -1.5, -1.5, -1.0, -1.5, -1.5, -2.0, -2.0, -1.5, -1.5, -2.0, -2.5, -2.5, -2.0, -2.0, -1.5, -2.0, -2.0])
level_tp_bartek = np.abs([-2, -3, -1, -2, -1, -1.5, -1.0, -2.0, -1.0, -2.0, -1.0, -2.0, -1.5, -2.5, -1.5, -2.0])
level_threshold_bartek = np.mean(level_tp_bartek[4:])
level_jnd_bartek = np.abs(ref_level - 10**(-level_threshold_bartek/20)) / ref_level

plt.figure(1)
plt.plot(level_diff_bartek, marker='.')
plt.hlines(y=level_threshold_bartek, xmin=0, xmax=len(level_diff_bartek), linestyles='dashed')
plt.title("Interaural level difference - Bartek\nThreshold: {:.1f}dB, JND: {:.1f}%".format(level_threshold_bartek, level_jnd_bartek*100))
plt.xlabel("trial number")
plt.ylabel("volume difference [dB]")
plt.grid()

# 2
time_diff_bartek = [500, 450, 400, 350, 300, 250, 200, 150, 100, 50, 100, 150, 200, 200, 150, 150, 100, 100, 50, 100, 100, 150, 150, 200, 200, 150, 150, 175, 175, 150, 150, 125, 125, 100, 100, 75, 75, 50, 50, 25, 50, 75, 75, 50, 75, 100, 125, 125, 100, 100, 75, 100, 100, 75, 100, 100, 125, 150, 150, 125, 125, 100, 100, 125, 125, 150, 150]
time_tp_bartek = [50, 200, 50, 200, 150, 175, 25, 75, 50, 125, 75, 100, 75, 150, 100, 150]
time_threshold_bartek = np.mean(time_tp_bartek[4:])

plt.figure(2)
plt.plot(time_diff_bartek, marker='.')
plt.hlines(y=time_threshold_bartek, xmin=0, xmax=len(time_diff_bartek), linestyles='dashed')
plt.title("Interaural time difference - Bartek\nThreshold: {:.2f}$\mu$s".format(time_threshold_bartek))
plt.xlabel("trial number")
plt.ylabel("time difference [$\mu$s]")
plt.grid()

# 3
freq_diff_bartek = [50, 42, 34, 26, 18, 10, 18, 18, 10, 10, 2, 10, 10, 2, 6, 6, 2, 6, 6, 2, 6, 6, 2, 6, 6, 2, 6, 6, 2, 6, 6, 10, 10]
freq_tp_bartek = [10, 18, 2, 10, 2, 6, 2, 6, 2, 6, 2, 6, 2, 6, 2, 10]
freq_threshold_bartek = np.mean(freq_tp_bartek[4:])
freq_jnd_bartek = np.abs(1 - 2**(freq_threshold_bartek/1200))

plt.figure(3)
plt.plot(freq_diff_bartek, marker='.')
plt.hlines(y=freq_threshold_bartek, xmin=0, xmax=len(freq_diff_bartek), linestyles='dashed')
plt.title("Binaural frequency discrimination - Bartek\nThreshold: {:.2f} cents, JND: {:.1f}%".format(freq_threshold_bartek, freq_jnd_bartek*100))
plt.xlabel("trial number")
plt.ylabel("frequency difference [cent]")
plt.grid()


plt.show()
