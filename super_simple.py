#!/usr/bin/env python3

import matplotlib
import matplotlib.pyplot
import numpy
import math

t = numpy.linspace(0, 2 * numpy.pi, 400)
A = numpy.sin(t)

matplotlib.pyplot.plot(t, A)
matplotlib.pyplot.show()
