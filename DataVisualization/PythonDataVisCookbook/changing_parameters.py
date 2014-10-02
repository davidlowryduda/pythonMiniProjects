#!/usr/bin/env python
# encoding: utf-8

"""
From page 15: Customizing matplotlib's parameters in code.
"""

"""
import matplotlib as mpl
mpl.rc('lines', linewidth=5, color='w')
"""

#""" equivalent to
import matplotlib as mpl
mpl.rcParams['lines.linewidth'] = 9
mpl.rcParams['lines.color'] = 'g'
#"""

#import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

t = np.arange(0.0, 1.0, 0.01)

#mpl.rcdefaults()

s = np.sin(2 * np.pi * t)
# make line red - as far as I can tell - this is completely ignored
#mpl.rcParams['lines.color'] = 'r'
plt.plot(t, s)

# But this, which I did on my own, totally works. I don't know how to set
# default colors
#plt.plot(t,s, color = 'r')

c = np.cos(2 * np.pi * t)
# make line thick
mpl.rcParams['lines.linewidth'] = '3'
plt.plot(t,c)

plt.show()
