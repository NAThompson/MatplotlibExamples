#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np

t = np.linspace(0.000001, 0.4, 8000)
A = np.sin(1/t)

plt.plot(t, A)
plt.show()
