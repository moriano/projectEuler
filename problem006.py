#!/usr/bin/python

"""


The sum of the squares of the first ten natural numbers is,
1**2 + 2**2 + ...+ 10**2 = 385

The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)**2 = 552 = 3025

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 - 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

"""


__author__ = 'moriano'

sum_squares = 0
for i in range(1, 101):
    sum_squares += i**2

"""
1 + 2 + 3 + ... + 100

100 + 1 = 101
99 + 2  = 101
98 + 3  = 101
"""
squares_sum = (101*50)**2

print "Solution %d" % (squares_sum-sum_squares)