#!/usr/bin/python

"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""
__author__ = 'moriano'


"""
There is no real need of any code to solve this problem, just remember the maths you were teached at school :)

Essentially we need to calculate the minimum common multiple, to do that just decompose the numbers into primes,
then take common and uncommon primes, in the case of common ones, take the ones with the max exponent.

20 = 2^2 * 5
19
18 = 2 * 3^2
17
16 = 2^4
15 = 3 * 5
14 = 2 * 7
13
12 = 2^2 * 3
11
10 = 2 * 5
9 = 3^2
8 = 2^3
7
6 = 2 * 3
4 = 2^2
3
2

Soooo, common and uncommon primes, taking the max power in the case of common ones

19*17*13*11*7*5*3^2*2^4
"""

print 19 * 17 * 13 * 11 * 7 * 5 * 3**2 * 2**4

