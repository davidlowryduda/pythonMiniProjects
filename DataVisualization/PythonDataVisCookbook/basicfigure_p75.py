#!/usr/bin/env python
# encoding: utf-8

from matplotlib.pyplot import *

# Some simple data
x = [1,2,3,4]
y = [5,4,3,2]

# Create a new figure
figure()

# Divide subplots into 2x3 grid
# and select the first subplot
# basic line-plot
subplot(231)
plot(x,y)

# select second subplot
# bar plot
subplot(232)
bar(x,y)

# select third subplot
# horizontal bar plot
subplot(233)
barh(x,y)

# select 4th plot, add more data
# stacked bar plot
subplot(234)
bar(x,y)
y1 = [7, 8, 5, 3]
bar(x, y1, bottom=y, color='r')

"""
Notice that the stacked bar plot is additive - so the first columns are both of height 12.
"""

# select 5th plot
# box plot
subplot(235)
boxplot(x)

# select 6th plot
# scatter plot
subplot(236)
scatter(x,y)

show()

