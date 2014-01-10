#!/usr/bin/python
"""
The following iterative sequence is defined for the set of positive integers:

n -> n/2 (n is even)
n -> 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:
13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been
proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""
import time
__author__ = 'moriano'

#The only optimization for this problem is to "cache" the results, a dictionary can do it.

calculated_seq = {} #Key is number, value seq length
max_seq = 0
solution = 0

start = time.time()
for i in range(1, 10**6):
    calculus = 0
    seq_size = 1
    candidate = i
    while calculus != 1:
        if candidate in calculated_seq:
            seq_size += calculated_seq[candidate]
            calculus = 1
        elif candidate % 2 == 0:
            candidate = candidate/2
            calculus = candidate
            seq_size += 1
        else:
            candidate = (3*candidate) + 1
            calculus = candidate
            seq_size += 1


    calculated_seq[i] = seq_size
    if seq_size > max_seq:
        max_seq = seq_size
        solution = i


print "Solution is %d, time taken %f" % (solution, time.time() - start)