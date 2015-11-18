#!/usr/bin/env python
# encoding: utf-8

"""
align.py
========

A short aligner written in python.

Usage:

  $ python align.py S < STDIN

or

  $ cat STDINFILE | python align.py S

Copyright (C) 2015 David Lowry-Duda <davidlowryduda@davidlowryduda.com>
Everyone is permitted to copy and distribute verbatim or modified copies
of this license document, and changing it is allowed as long as the
changes are not attributed to David Lowry-Duda.
"""

import sys

def print_usage():
    print
    print "======================================"
    print "Usage:"
    print
    print "  $ python align.py S < STDIN"
    print
    print "where S is the separator to align on"
    print "and STDIN is the source to be aligned."
    print "======================================"
    print
    return


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print_usage()
        quit()
    separator = sys.argv[1]
    lines = []
    maxlength = 0
    for line in sys.stdin:
        lines.append(line)
        length = line.find(separator)
        if length > maxlength:
            maxlength = length

    output = ""
    for line in lines:
        length = max(line.find(separator), 0)
        outl = " " * (maxlength - length)
        outl += line
        output += outl
    print output, # comma because this is python 2 and we don't want newline
