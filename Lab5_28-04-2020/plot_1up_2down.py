import matplotlib.pyplot as plt
import numpy as np

# results Bartek
# 1
pitch_diff_bartek = [0, 6, 12, 18, 24, 18, 18, 12, 18, 24, 30, 30, 24, 24, 27, 30, 33, 33, 30, 30, 27, 27, 24, 27, 27, 30, 30, 27, 30, 30, 27, 27, 30, 33, 33, 36, 39, 39, 36, 36, 33, 33, 30, 33, 33, 30, 33, 33]
pitch_tp_bartek = [24, 18, 12, 30, 24, 33, 24, 30, 27, 30, 27, 39, 30, 33, 30, 33]
pitch_changed_bartek = True
pitch_threshold_bartek = np.mean(pitch_tp_bartek[4:])

if pitch_changed_bartek:
    pitch_changed_text_bartek = "After removing two harmonics perceived pitch changed"
else:
    pitch_changed_text_bartek = "After removing two harmonics perceived pitch did not change"

plt.figure(1)
plt.plot(pitch_diff_bartek, marker='.')
plt.hlines(y=pitch_threshold_bartek, xmin=0, xmax=len(pitch_diff_bartek), linestyles='dashed')
plt.title("Pitch difference - Bartek\n{}".format(pitch_changed_text_bartek))
plt.xlabel("trial number")
plt.ylabel("pitch difference [cent]")
plt.grid()


# 2
volume_diff_bartek = np.abs([-6, -5, -4, -3, -4, -3, -3, -4, -3, -2.5, -2.5, -3.0, -2.5, -2.0, -1.5, -1.5, -2.0, -1.5, -1.5, -2.0, -1.5, -1.5, -2.0, -1.5, -1.5, -2.0, -2.0, -2.5, -2.0, -2.0, -2.5])
volume_tp_bartek = np.abs([-6, -5, -4, -4, -3, -4, -2.5, -3.0, -1.5, -2.0, -1.5, -2.0, -1.5, -2.0, -1.5, -2.5, -2.0, -2.5])
volume_threshold_bartek = np.mean(volume_tp_bartek[4:])

plt.figure(2)
plt.plot(volume_diff_bartek, marker='.')
plt.hlines(y=volume_threshold_bartek, xmin=0, xmax=len(volume_diff_bartek), linestyles='dashed')
plt.title("Volume difference - Bartek")
plt.xlabel("trial number")
plt.ylabel("volume difference [dB]")
plt.grid()

plt.show()