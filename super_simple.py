#!/usr/bin/env python3

import matplotlib
import matplotlib.pyplot
import numpy
import math

t = numpy.linspace(0.00001, 0.4, 4000)
A = numpy.sin(1/t)

matplotlib.pyplot.plot(t, A)
matplotlib.pyplot.show()
