#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy

theta = numpy.linspace(0, 2*numpy.pi, 500)
r = 2*numpy.sin(3*theta)

ax = plt.subplot(111, polar=True)
ax.plot(theta, r, 'b-', theta, theta/(numpy.pi), 'g-')
ax.grid(True)

ax.set_title(r"Rose Plot; $r = 2\sin(2\theta)$")
plt.show()
