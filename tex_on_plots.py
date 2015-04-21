#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np

t = np.linspace(0, 2 * np.pi, 400)
A = np.sin(t)

# Multiple plots:
plt.plot(t, A, 'r', t, 2*A, 'b')


plt.xlabel('$t$', fontsize=20)
plt.ylabel('$A$', fontsize=20)

# Advanced TeX commands can be used if you're willing to fight:
# plt.rc('text', usetex=True)
plt.title(r'Basic TeX commands can be used!')

plt.grid(True)

#TeX strings should be raw:
plt.text(1, 0.0, r'$A=\sin(t)$', fontsize=30)
plt.text(2.5, 1.50, r'$A=2\sin(t)$', fontsize=30)

plt.show()
