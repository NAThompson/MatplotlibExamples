#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np

points = 10000
d1 = np.random.beta(2, 5, size=points)
d2 = np.random.lognormal(mean=1.0, sigma=1.0, size=points)


plt.figure(1)
plt.grid(True)
plt.subplot(211) # 2x1 grid, 1st subplot
n, bins, patches = plt.hist(d1, bins=40, facecolor='b', alpha=0.8)
plt.subplot(212) # 2x1 grid, 2nd subplot
n, bins, patches = plt.hist(d2, bins=40, facecolor='b', alpha=0.8)

plt.show()
