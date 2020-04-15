import matplotlib.pyplot as plt
import numpy as np

# wyniki Bartka
cents_bartek = []
turning_points_bartek = []
threshold_bartek = np.mean(turning_points_bartek[-12:])

plt.plot(cents_bartek, marker='.')
plt.hlines(y=threshold_bartek, xmin=0, xmax=len(cents_bartek), linestyles='dashed')
plt.grid()
plt.show()
