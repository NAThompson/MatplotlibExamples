#!/usr/bin/env python3

import numpy
import matplotlib.pyplot as plt
import math
import unittest

p0 = (1+math.sqrt(3))/4
p1 = (3+math.sqrt(3))/4
p2 = (3-math.sqrt(3))/4
p3 = (1-math.sqrt(3))/4

class Daub4(object):
    def __init__(self, dx):
        if dx > 1.5 or dx <= 0:
            raise Exception("dx must be < 1.5 and >= 0")

        m = 1
        while m < math.ceil(1/dx):
            m = m*2

        self.phi = numpy.full(3*m, numpy.inf)
        self.dx = 1.0/m
        # index i corresponds to x = (i/m); so i = mx
        # phi(1) := (1+math.sqrt(3))/2
        self.phi[m*0] = 0
        self.phi[m*1] = (1+math.sqrt(3))/2
        self.phi[m*2] = (1-math.sqrt(3))/2

        for n in range(1, int(math.log(m, 2)) + 1):
            i = 0
            while (2*i+1)/math.pow(2, n) < 3:
                j = int((2*i+1)*m/math.pow(2, n))
                self.phi[j] = 0
                if 2*j < 3*m:
                    self.phi[j] += p0*self.phi[2*j]
                if 2*j - m < 3*m and 2*j -m > 0:
                    self.phi[j] += p1*self.phi[2*j-m]
                if 2*j - 2*m < 3*m and 2*j - m > 0:
                    self.phi[j] += p2*self.phi[2*j-2*m]
                if 2*j - 3*m < 3*m and 2*j - 3*m > 0:
                    self.phi[j] += p3*self.phi[2*j-3*m]

                i = i+1

    def dx(self):
        return self.dx

    def phi(self):
        return self.phi

    def phi_x(self, x):
        return self.phi[int(x/self.dx)]


class TestDaub4(unittest.TestCase):

    def test_three_points(self):
        daub = Daub4(1.5)
        self.assertAlmostEqual(daub.phi_x(0.0), 0)
        self.assertAlmostEqual(daub.phi_x(1.0), (1+math.sqrt(3))/2)
        self.assertAlmostEqual(daub.phi_x(2.0), (1-math.sqrt(3))/2)

    def test_six_points(self):
        daub = Daub4(0.4)
        self.assertAlmostEqual(daub.phi_x(0.0), 0)
        self.assertAlmostEqual(daub.phi_x(0.5), (2+math.sqrt(3))/4)
        self.assertAlmostEqual(daub.phi_x(1.0), (1+math.sqrt(3))/2)
        self.assertAlmostEqual(daub.phi_x(1.5), 0)
        self.assertAlmostEqual(daub.phi_x(2.0), (1-math.sqrt(3))/2)
        self.assertAlmostEqual(daub.phi_x(2.5), (2 - math.sqrt(3))/4)

    def test_more_points(self):
        daub = Daub4(0.2)
        self.assertAlmostEqual(daub.phi_x(0.00), 0)
        self.assertAlmostEqual(daub.phi_x(0.25), (5+3*math.sqrt(3))/16)
        self.assertAlmostEqual(daub.phi_x(0.50), (2+math.sqrt(3))/4)
        self.assertAlmostEqual(daub.phi_x(1.00), (1+math.sqrt(3))/2)
        self.assertAlmostEqual(daub.phi_x(1.50), 0)
        self.assertAlmostEqual(daub.phi_x(2.00), (1-math.sqrt(3))/2)
        self.assertAlmostEqual(daub.phi_x(2.50), (2 - math.sqrt(3))/4)

if __name__ == "__main__":
    daubechies = Daub4(0.01)
    xAxis = numpy.linspace(0, 3, len(daubechies.phi))
    fig = plt.figure(facecolor='black')
    plt.style.use('dark_background')
    #plt.style.use('fivethirtyeight')
    plt.plot(xAxis, daubechies.phi, 'g--', linewidth=2.0)
    plt.grid(True)
    plt.title("The Daubechies 4 tap scaling function")
    plt.show()
    unittest.main()
