#!/usr/bin/env python3

"""
This script provides objects which allow the display of wiggly traces.

The vision for this script, though not its current reality is:

    --numpy arrays with associated receiver locations, with timestep and metadata, as input.
    --wiggle traces displayed at the receiver location, in 3D.
    --amplitudes dynamically scaled by user.
    --metadata coloring of wiggle traces.

This script has no user-interface capabilities. Its value is found in embedding it into tkinter UIs.

TODO:
    -- Put this in a namespace!

"""

import numpy
import matplotlib
import matplotlib.pyplot
import math
import unittest

def ricker_wavelet(sigma, t):
    return (1-t**2/sigma**2)*math.exp(-t**2/sigma**2)

trace = numpy.zeros(5000)
for ii in range(0, len(trace)):
    trace[ii] = ricker_wavelet(len(trace)/10.0, ii - len(trace)/2.0)

#matplotlib.pyplot.style.use('dark_background')
fig, ax = matplotlib.pyplot.subplots()

tAxis = numpy.linspace(0, len(trace)*0.001, len(trace))
ax.fill_between(trace, tAxis, where=trace>0)
ax.plot(trace, tAxis)
matplotlib.pyplot.gca().invert_yaxis()
matplotlib.pyplot.style.use('grayscale')
matplotlib.pyplot.show()


