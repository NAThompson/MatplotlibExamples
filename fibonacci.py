#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy
import math
length = 25
fib = numpy.ones(length)
x = numpy.zeros(length)
x[1] = 1
for ii in range(2, len(fib)):
    fib[ii] = fib[ii-1] + fib[ii-2]
    x[ii] = ii

golden_ratio  = 1.61803398875

plt.semilogy(x, fib, 'go', label='Fibonacci numbers')
plt.semilogy(x, (golden_ratio**x)/math.sqrt(5), 'bd', label=r"$\phi^{n}/\sqrt{5}$")

legend = plt.legend(loc='upper left', shadow=True, fontsize='x-large')

plt.title(r"Fibonnacci numbers are asymptotic to $\frac{\phi^{n}}{\sqrt{5}}$; an example using $\tt{plt.semilogy}$")

plt.show()
