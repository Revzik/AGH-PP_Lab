import matplotlib.pyplot as plt
import numpy as np

# reference values
ref_level = 1.0
ref_time = 0
ref_freq = 1000

# results Bartek
# 1
broadband_volume_bartek = [0, -4, -8, -12, -16, -20, -24, -28, -32, -28, -28, -32, -28, -24, -20, -20, -24, -20, -20, -22, -22, -20, -20, -22, -22, -24, -24, -26, -26, -24, -24, -26, -26, -28, -26, -26, -28, -28, -30, -28, -28, -26, -26, -28, -26, -26, -28]
broadband_tp_bartek = [-32, -32, -20, -24, -20, -22, -20, -26, -24, -28, -26, -30, -26, -28, -26, -28]
broadband_audible = True
broadband_threshold_bartek = np.mean(broadband_tp_bartek[4:])

if broadband_audible:
    broadband_audible_text = "Tone without noise was audible"
else:
    broadband_audible_text = "Tone without noise was not audible"

plt.figure(1)
plt.plot(broadband_volume_bartek, marker='.')
plt.hlines(y=broadband_threshold_bartek, xmin=0, xmax=len(broadband_volume_bartek), linestyles='dashed')
plt.title("Broadband masking - Bartek\nInitial noise level: -6dBFS, Threshold: {:.1f}dBFS\n{}"
          .format(broadband_threshold_bartek, broadband_audible_text))
plt.xlabel("trial number")
plt.ylabel("tone volume [dBFS]")
plt.grid()


# 2
bandpassed_volume_bartek = [0, -4, -8, -12, -16, -20, -24, -28, -24, -24, -28, -24, -24, -28, -24, -22, -22, -24, -24, -22, -22, -24, -24, -22, -22, -24, -24, -26, -24, -24, -26, -24, -24, -26, -24, -22, -22, -24, -24, -26]
bandpassed_tp_bartek = [-28, -28, -24, -28, -22, -24, -22, -24, -22, -26, -24, -26, -24, -26, -22, -26]
bandpassed_audible = True
bandpassed_threshold_bartek = np.mean(bandpassed_tp_bartek[4:])

if bandpassed_audible:
    bandpassed_audible_text = "Tone without noise was audible"
else:
    bandpassed_audible_text = "Tone without noise was not audible"

plt.figure(2)
plt.plot(bandpassed_volume_bartek, marker='.')
plt.hlines(y=bandpassed_threshold_bartek, xmin=0, xmax=len(bandpassed_volume_bartek), linestyles='dashed')
plt.title("Bandpassed (800Hz - 1kHz) masking - Bartek\nInitial noise level: 0dBFS, Threshold: {:.1f}dBFS\n{}"
          .format(bandpassed_threshold_bartek, bandpassed_audible_text))
plt.xlabel("trial number")
plt.ylabel("tone volume [dBFS]")
plt.grid()


# 2
gap_dur_bartek = [0.8, 0.7000000000000001, 0.6000000000000001, 0.5000000000000001, 0.6000000000000001, 0.6000000000000001, 0.5000000000000001, 0.5000000000000001, 0.6000000000000001, 0.6000000000000001, 0.5000000000000001, 0.6000000000000001, 0.6000000000000001, 0.55, 0.55, 0.5, 0.55, 0.55, 0.5, 0.5, 0.55, 0.55, 0.5, 0.55, 0.55, 0.5, 0.55, 0.55, 0.5, 0.55, 0.55, 0.5, 0.5]
gap_tp_bartek = [0.5000000000000001, 0.5000000000000001, 0.6000000000000001, 0.5000000000000001, 0.6000000000000001, 0.5, 0.55, 0.5, 0.55, 0.5, 0.55, 0.5, 0.55, 0.5, 0.55, 0.5]
gap_audible = True
gap_threshold_bartek = np.mean(gap_tp_bartek[4:])

if gap_audible:
    gap_audible_text = "Tone without noise was audible"
else:
    gap_audible_text = "Tone without noise was not audible"

plt.figure(3)
plt.plot(gap_dur_bartek, marker='.')
plt.hlines(y=gap_threshold_bartek, xmin=0, xmax=len(gap_dur_bartek), linestyles='dashed')
plt.title("Post masking - Bartek\nInitial noise level: 0dBFS, Gap length hreshold: {:.3f}s\n{}"
          .format(gap_threshold_bartek, gap_audible_text))
plt.xlabel("trial number")
plt.ylabel("gap length [s]")
plt.grid()


plt.show()
