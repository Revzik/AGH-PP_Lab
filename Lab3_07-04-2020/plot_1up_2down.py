import matplotlib.pyplot as plt
import numpy as np

# wyniki Bartka
level_diff_bartek = np.abs([-6, -5, -4, -3, -2, -3, -3, -2, -2, -1, -2, -2, -1, -1.5, -1.5, -1.0, -1.5, -2.0, -2.0, -1.5, -1.5, -1.0, -1.0, -1.5, -1.5, -2.0, -2.0, -1.5, -1.5, -1.0, -1.5, -1.5, -2.0, -2.0, -1.5, -1.5, -2.0, -2.5, -2.5, -2.0, -2.0, -1.5, -2.0, -2.0])
level_tp_bartek = np.abs([-2, -3, -1, -2, -1, -1.5, -1.0, -2.0, -1.0, -2.0, -1.0, -2.0, -1.5, -2.5, -1.5, -2.0])
level_threshold_bartek = np.mean(level_tp_bartek[4:])

plt.plot(level_diff_bartek, marker='.')
plt.hlines(y=level_threshold_bartek, xmin=0, xmax=len(level_diff_bartek), linestyles='dashed')
plt.title("Interaural level difference - Bartek\nThreshold: {:.1f}dB".format(level_threshold_bartek))
plt.grid()
plt.show()


time_diff_bartek = [500, 450, 400, 350, 300, 250, 200, 150, 100, 50, 100, 150, 200, 200, 150, 150, 100, 100, 50, 100, 100, 150, 150, 200, 200, 150, 150, 175, 175, 150, 150, 125, 125, 100, 100, 75, 75, 50, 50, 25, 50, 75, 75, 50, 75, 100, 125, 125, 100, 100, 75, 100, 100, 75, 100, 100, 125, 150, 150, 125, 125, 100, 100, 125, 125, 150, 150]
time_tp_bartek = [50, 200, 50, 200, 150, 175, 25, 75, 50, 125, 75, 100, 75, 150, 100, 150]
time_threshold_bartek = np.mean(time_tp_bartek[4:])

plt.plot(time_diff_bartek, marker='.')
plt.hlines(y=time_threshold_bartek, xmin=0, xmax=len(time_diff_bartek), linestyles='dashed')
plt.title("Interaural time difference - Bartek\nThreshold: {:.2f}us".format(time_threshold_bartek))
plt.grid()
plt.show()
