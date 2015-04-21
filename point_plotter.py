#!/usr/bin/env python3

import matplotlib.pyplot as plt

def plot_point(event):
    plt.scatter(event.xdata, event.ydata)
    print("Adding point at ({}, {})".format(event.xdata, event.ydata))
    plt.draw()

fig, ax = plt.subplots(1,1)
fig.canvas.mpl_connect('button_press_event', plot_point)
plt.show()
