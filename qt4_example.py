#!/usr/bin/env python3

"""
To get this to work in a virtualenv requires some heroics:

sudo apt-get install python3-pyqt4
cp -R /usr/lib/python3/dist-packages/PyQt4/ lib/python3.4/site-packages/PyQt4
cp /usr/lib/python3/dist-packages/sip* lib/python3.4/site-packages/

The rest is adapted from:

Matplotlib for Python Developers, Chapter 6

"""

import sys
import PyQt4
from PyQt4 import QtGui

import numpy as np
import matplotlib
matplotlib.use('qt4agg')

from matplotlib.figure import Figure

from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas

class Qt4MplCanvas(FigureCanvas):
    def __init__(self):
        self.fig = Figure()
        self.axes = self.fig.add_subplot(111)
        self.x = np.arange(0.0, 3.0, 0.01)
        self.y = np.cos(2*np.pi*self.x)
        self.axes.plot(self.x, self.y)
        FigureCanvas.__init__(self, self.fig)

qApp = QtGui.QApplication(sys.argv)
mpl = Qt4MplCanvas()

mpl.show()
sys.exit(qApp.exec_())
