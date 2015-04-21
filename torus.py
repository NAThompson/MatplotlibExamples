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
r = 1


x = (R + r*np.cos(theta))*np.cos(phi)
y = (R + r*np.cos(theta))*np.sin(phi)
z = r*np.sin(theta)

ax.set_xlim3d(-R, R)
ax.set_ylim3d(-R, R)
ax.set_zlim3d(-R, R)
ax.plot_surface(x, y, z,  rstride=1, cstride=1, color='b')



plt.show()

