#!/usr/bin/python

"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143
"""

__author__ = 'moriano'

number = 600851475143 #It is an odd number, so no need to use even numbers as possible factors
factor=3
solution = 1
while number > 1:
    if number % factor == 0:
        solution = factor
        number /= factor
        while number % factor == 0:
            number /= factor
        print "Found factor %d" % solution
    factor += 2 #Optimization, no need to check even numbers

print "Final solution %d" % solution



























