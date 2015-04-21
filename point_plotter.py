#!/usr/bin/env python

import matplotlib.pyplot as plt

def plot_point(event):
    plt.scatter(event.xdata, event.ydata)
    plt.draw()

fig, ax = plt.subplots(1,1)
fig.canvas.mpl_connect('button_press_event', plot_point)
plt.show()
