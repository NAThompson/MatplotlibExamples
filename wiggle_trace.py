#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
import math
import unittest

def ricker_wavelet(sigma, t):
    return (1-t**2/sigma**2)*math.exp(-t**2/sigma**2)

trace = np.zeros(5000)
for ii in range(0, len(trace)):
    trace[ii] = ricker_wavelet(len(trace)/10.0, ii - len(trace)/2.0)

#plt.style.use('dark_background')
#plt.style.use('grayscale')
#plt.style.use('ggplot')
#plt.style.use('bmh')

plt.style.use('fivethirtyeight')

fig, ax = plt.subplots()

tAxis = np.linspace(0, len(trace)*0.001, len(trace))

# Add positive fill:
ax.fill_between(trace, tAxis, where=trace>0)

# Plot vertically by switching independent and dependent variables:
ax.plot(trace, tAxis)

# Make time increase downwards:
plt.gca().invert_yaxis()


plt.show()


