#!/usr/bin/python

"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
"""

__author__ = 'moriano'

#Easy approach, just iterate
solution = 0
for idx in xrange(0, 1000):
    print idx
    if idx % 3 == 0 or idx % 5 == 0:
        solution += idx

print solution
