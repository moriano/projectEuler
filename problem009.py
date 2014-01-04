#!/usr/bin/python
import time
"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a2 + b2 = c2

For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.

"""

__author__ = 'moriano'

import math

for a in range(1, 1000):
    for b in range(a, 1000):
        a_square = a*a
        b_square = b*b
        c_square = a_square + b_square
        c = math.sqrt(c_square)

        if a + b + c == 1000:
            print "Solved %d * %d * %d = %d" % (a, b, c, a*b*c)
            exit(0)
