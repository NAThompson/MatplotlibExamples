#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np

theta = np.linspace(0, 2*np.pi, 500)
r = 2*np.sin(3*theta)

ax = plt.subplot(111, polar=True)

ax.plot(theta, r, 'b-', theta, theta/(np.pi), 'g-')
ax.grid(True)

ax.set_title(r"Rose Plot $r = 2\sin(2\theta)$ and Archimedean Spiral $r =\theta/2\pi$")
plt.show()
