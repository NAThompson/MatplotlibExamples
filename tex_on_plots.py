#!/usr/bin/env python3

import matplotlib
import matplotlib.pyplot as plt
import numpy
import math

t = numpy.linspace(0, 2 * numpy.pi, 400)
A = numpy.sin(t)

plt.plot(t, A)
plt.xlabel('$t$', fontsize=20)
plt.ylabel('$A$', fontsize=20)
plt.title('Super-simple Stuff')
plt.grid(True)
plt.text(5, 0.75, r'$A=\sin(t)$', fontsize=30)

plt.show()
