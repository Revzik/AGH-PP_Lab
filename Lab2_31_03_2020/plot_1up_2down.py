import matplotlib.pyplot as plt
import numpy as np

# wyniki Bartka
# 2
cents_bartek = [50, 42, 34, 26, 18, 10, 2, 10, 10, 18, 18, 10, 10, 2, 10, 10, 2, 6, 10, 10, 6, 10, 10, 6, 10, 10, 6, 10, 10, 6, 6, 10, 10, 6, 6, 2, 6, 6]
turning_points_bartek = [2, 18, 2, 10, 2, 10, 6, 10, 6, 10, 6, 10, 6, 10, 2, 6]
threshold_bartek = np.mean(turning_points_bartek[4:])

plt.figure(1)
plt.plot(cents_bartek, marker='.')
plt.hlines(y=threshold_bartek, xmin=0, xmax=len(cents_bartek), linestyles='dashed')
plt.title("IFC, adaptive method - Bartek\nThreshold: {:.2f} cents".format(threshold_bartek))
plt.xlabel("trial number")
plt.ylabel("frequency difference [cent]")
plt.grid()


plt.show()
