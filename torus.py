#!/usr/bin/env python3
"""
Adapted from matplotlib Plotting Cookbook
"""

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

angle = np.linspace(0, 2*np.pi, 32)
theta, phi = np.meshgrid(angle, angle)

R = 4
r = 1.2


x = (R + r*np.cos(theta))*np.cos(phi)
y = (R + r*np.cos(theta))*np.sin(phi)
z = r*np.sin(theta)

ax.set_xlim3d(-R, R)
ax.set_ylim3d(-R, R)
ax.set_zlim3d(-R, R)
ax.set_zlabel(r"$z = {}\sin(\theta)$".format(r))
ax.plot_surface(x, y, z,  rstride=1, cstride=1, color='b')


plt.title(r"Example use of mpl_toolkits.mplot3d: $x = ({} + {}\cos(\theta))\cos(\phi)$".format(R,r))
plt.xlabel(r"$x = ({} + {}\cos(\theta))\cos(\phi)$".format(R,r))
plt.ylabel(r"$y = ({} + {}\cos(\theta))\sin(\phi)$".format(R,r))
#plt.zlabel(r"$z = {}\sin(\theta)".format(r))

plt.show()

