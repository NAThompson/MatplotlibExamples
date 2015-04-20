#!/usr/bin/env python3

import matplotlib
import matplotlib.pyplot
import numpy
import math

t = numpy.linspace(0, 2 * numpy.pi, 400)
A = numpy.sin(t)

f, ax = matplotlib.pyplot.subplots()
ax.plot(t, A)
matplotlib.pyplot.show()
