#!/usr/bin/env python3.3

"""
.. module:: sacksSpiral
    Synopsis
    --------
    Sack's Spiral is sort of a co-Ulam Spiral (co in the mathematical sense).
    Numbers are plotted counterclockwise in a spiral, where n gets polar
    coordinates (sqrt(n), 2*pi*sqrt(n)). And they are given a radius
    2^(nu(n)-1), where nu(n) is the number of distinct prime factors.

    Pretty patterns emerge. The output is in file spirals.py.

    Notes
    -----
    Due to normal restrictions on size of files for postscripts written though
    pyx and python, the process is broken up into many smaller chunks and
    assembled together at the end.

    CAUTION
    -------
    Do not use in directories with files called "tt_label.ps" or
    "tt_spiral*.ps",
    as these are deleted at the conclusion of the program.

.. author:: David Lowry-Duda <djlowry@math.brown.edu>

Copyright (c) 2013, 2014, David Lowry-Duda
All rights reserved."""

'''
TODO: write main loop in function
TODO: make main loop accept a generator, like poly or fib, to color nums
Maybe rewrite the generators to output num, color, for color gradients.

'''

from pyx import *
from entDLD import *
import os
import math

# Number of points to plot
n = 50000
unit.set(defaultunit="inch")
documentSize = 36


def poly(k=1):
    n = 2
    while True:
        yield n*(n+k)
        n = n+1


def fib():
    n1 = 2
    n2 = 3
    yield n2
    while True:
        n1, n2 = n2, n1 + n2
        yield n2


def write_file(ca, name, doc_width = documentSize, doc_height = documentSize):
    """
    Writes canvas to file `name` with specified dimensions.

    Parameters
    ----------
    ca : canvas
    name : string
        New file name.
    doc_width : int
    doc_height : int

    """
    posterformat = document.paperformat(unit.length(doc_width, unit="inch"),
                                        unit.length(doc_height, unit="inch"))
    p = document.page(ca, paperformat = posterformat, centered = 0)
    d = document.document(pages = [p])
    d.writePSfile(name)


def combine(pages, n=n, docsize = documentSize):
    """Combines individual pages together to produce final output."""
    labelfile = open("tt_label.ps")
    outfile = open("spiral.ps", "w")
    labellines = labelfile.readlines()
    labelfile.close()
    for line in labellines[0:15]:
        outfile.write(line)

    # Adjust outputs up and to the right so that they're centered.
    psLengthInTicks = 72 * docsize # ps files give 72 ticks to an inch
    xtrans = psLengthInTicks/2.
    ytrans = psLengthInTicks/2.
    outfile.write("{x:.5f} {y:.5f} translate\n".format(x = xtrans, y = ytrans))

    # Write body of label file. Must not include "showpage"
    for line in labellines[15:-4]:
        outfile.write(line)

    # Assemble the component pieces.
    for i in range(pages):
        infile = open("tt_spiral%03d.ps" % (i,))
        outfile.write("/pgsave save def\n")
        lines = infile.readlines()
        for line in lines[15:-4]:
            outfile.write(line)
        infile.close()

    # Finish the document
    for line in labellines[-4:]:
        outfile.write(line)
    outfile.close()


def write_label(ca, n=n):
    """
    Writes LaTeX label in corner to canvas.

    Notes
    -----
    If `documentsize` changes very much, this will need to be changed by hand.
    The placement is too aesthetic to be done automatically.

    """

    label_text = r'\begin{minipage}{6in} \begin{center} {\Huge The Sacks Spiral} \vskip 0.05in \hrule \vskip 0.05in \
            \Large $N=' + str(n)+r'$ \end{center} \large Numbers from 1 to ' +str(n)+r', are arranged \
            in a spiral formation. Numbers wind out in a counterclockwise Archimedian spiral, \
            beginning with 0 in the center. Each number is drawn only if it is composite, and bigger dots have more \
            prime factors. For example, $6 = 2 \cdot 3$ has $2$ prime factors, $2$ and $3$, while $8 = 2^3$ has only \
            $2$ as a prime factor. So $6$ is drawn bigger than $8$. The polar coordinates of each number $n$ are  \
            $r = \sqrt{n}, \theta = 2\pi\sqrt{n}$, so that the squares $(1,~4,~9,~16,~25,\ldots)$ form a straight \
            line heading east of the center.  This is a modified version of the \textit{Sacks Spiral} (developed \
            by Robert Sacks in 1994), which is a modified version of the \textit{Ulam Spiral}, discovered by \
            Stanislaw Ulam in 1963.  \vskip 0.05in \hrule \vskip 0.10in \begin{center} \
            \textsc{David Lowry-Duda} \\ \normalsize \textsc{davidlowryduda.com} \end{center} \end{minipage}'
    t = text.latexrunner()
    # Remember, center of document is at (0,0)
    ca.insert(t.text(14 ,-15 , label_text,[text.halign.boxcenter, text.valign.middle]))


def draw_axis(ca, docsize = documentSize):
    """ Writes circular axis with LaTeX labels to canvas."""
    t = text.latexrunner()
    # radius of the innercircle
    insize = .5*docsize - 1
    # draw the frame
    ca.stroke(path.rect(-17.5,-17.5,35,35))

    # draw the tenth of degree ticks
    for i in range(3600):
        # convert to radians
        ang = (i * math.pi) / 1800.0

        width = 0.001
        outsize = 0.1
        wscale = 2
        oscale = 1.6

        # Resize important ticks
        if i%900 == 0:
            width *= wscale
            outsize*=oscale
        if i%450 == 0:
            width *= wscale
            outsize*=oscale
        if i%50 == 0:
            width *= wscale
            outsize*=oscale
        if i%10 == 0:
            width *=wscale
            outsize *=oscale

        lw = style.linewidth(unit.length(width, type="w", unit="cm"))
        x1 = math.cos(ang) * insize
        y1 = -math.sin(ang) * insize
        x2 = math.cos(ang) * (insize+outsize)
        y2 = -math.sin(ang) * (insize+outsize)
        ca.stroke(path.line(x1,y1,x2,y2), [lw])

        # compute label coordinates
        x3 = math.cos(ang) * (insize+outsize+0.1)
        y3 = -math.sin(ang) * (insize+outsize+0.1)

        # write labels
        if i%900==0:
            ca.insert(t.text(x3,y3,"\\normalsize"+str(i/10),
                             [text.halign.boxcenter, text.valign.middle]))
        elif i%450==0:
            ca.insert(t.text(x3,y3,"\\small"+str(i/10),
                             [text.halign.boxcenter, text.valign.middle]))
        elif i%50==0:
            ca.insert(t.text(x3,y3,"\\footnotesize"+str(i/10),
                             [text.halign.boxcenter, text.valign.middle]))


if __name__ == "__main__":
    ca = canvas.canvas()
    #scale to just fit inside circle
    basescale = (documentSize*.5-1) / (math.sqrt(n)+1)
    pi2 = 2*math.pi
    ctr = 0
    pages = 0

    poly = poly(11)
    nextpoly = next(poly)

    # Draw the dots!
    for j in range(n):
        i = j + 2
        ctr += 1
        r = math.sqrt(i)
        theta = r * pi2
        x = math.cos(theta)*r*basescale
        y = math.sin(theta)*r*basescale
        if i < n:
            factors = factor(i)
            if(len(factors)>1):

                if i == nextpoly:
                    #print(nextpoly, i)
                    ca.fill(path.circle(x,y, basescale*0.05*math.pow(2,((len(factors)-1)))), [color.rgb(1,0,0)])
                    nextpoly = next(poly)
                else:
                    g = (1 - float(i)/n)**2
                    ca.fill(path.circle(x,y, basescale*0.05*math.pow(2,((len(factors)-1)))), [color.rgb(1-(1+g)/5,(2+g**2)/3,1-g)])
                    #ca.fill(path.circle(x,y, basescale*0.05*math.pow(2,((len(factors)-1)))), [color.gray(grayscaling)])
                    #ca.fill(path.circle(x,y, basescale*0.05*math.pow(2,((len(factors)-1)))), [color.rgb.black])


            if(len(factors)==1):
                grayscaling = (1 - float(i)/n)**3
                ca.fill(path.circle(x,y, basescale*0.05*math.pow(2,2)),[color.rgb(0,0,1)])

#            elif i >= nextpoly:
#                print(nextpoly, i)
#                nextpoly = next(poly)

        # split into chunks
        if ctr>=10000:
            ctr = 0
            write_file(ca, "tt_spiral%03d.ps" % (pages,))
            # reinit canvas for next batch
            ca = canvas.canvas()
            pages += 1

    # Handle when not a multiple of 10000
    if ctr != 0:
        write_file(ca, "tt_spiral%03d.ps" % (pages,))
        pages += 1

    # draw the label and axes and assemble the document
    ca = canvas.canvas()
    #ca.fill(path.rect(-18,-18,36,36), [color.gray(0.8)])
    write_label(ca)
    draw_axis(ca)
    write_file(ca, "tt_label")
    combine(pages)

    # clean up junk
    os.system("rm tt_spiral*.ps")
    os.system("rm tt_label.ps")

""" Licencing (BSD2)
Copyright 2013, 2014, David Lowry-Duda
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice,
this list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice,
this list of conditions and the following disclaimer in the documentation
and/or other materials provided with the distribution.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE
LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE
GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT
OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
"""
