#!/usr/bin/env python3

"""
This is a short script modified from Interactive Applications Using Matplotlib,
demonstrating the basics of key events.
"""

import matplotlib.pyplot as plt

def process_key(event):
    print("Name:", event.name)
    print("Canvas:", event.canvas)
    print("In axes?", event.inaxes)
    print("Key:", event.key)

def process_button(event):
    print("Button:", event.x, event.y, event.xdata, event.ydata, event.button)

fig, ax = plt.subplots(1, 1)
fig.canvas.mpl_connect('key_press_event', process_key)
fig.canvas.mpl_connect('button_press_event', process_button)

plt.show()
