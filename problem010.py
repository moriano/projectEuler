#!/usr/bin/python
"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""
__author__ = 'moriano'
import math
import time

"""
To solve this problem I will just calculate all primes lower than 2 millions, to do that effectively, Eratostenes'
sieve is used.

The algorithm is simple

1-Build a list with all the numbers from 0 to 2 millions
2-Starting with 2, mark every multiple, for example
    2.1 For 2, mark multiples 4,6,8,10,12...
    2.2 FOr 3, mark multiples 6,9,12,15...
3-The numbers that are NOT marked, are primes, just iterate over them and sum them.

That's all folks
"""
start = time.time()
limit = 2*10**6
eratostenes_limit = int(math.sqrt(limit))

candidates = [0]
for i in xrange(1, limit):
    candidates.append(i)

for i in range(2, eratostenes_limit):
    removed = i
    while removed < limit:
        removed += i
        if removed < limit:
            candidates[removed] = False

solution = 0
for candidate in candidates:
    if candidate:
        solution += candidate


#Note that 1 is NOT prime
print "Solution %d. Time to calculate %.4f" % (solution-1, time.time()-start)
