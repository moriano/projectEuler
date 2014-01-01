#!/usr/bin/python

"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is
9009 = 91 x 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""


__author__ = 'moriano'

candidates = []
for i in xrange(999, 101, -1):
    for j in xrange(999, 101, -1):
        candidate = i * j
        candidates.append(candidate)

candidates.sort(reverse=True)

for candidate in candidates:
    candidate_str = str(candidate)
    limit = len(candidate_str) / 2 if len(candidate_str) % 2 == 0 else (len(candidate_str) + 1) % 2
    success = True
    for i in range(0, limit):
        if candidate_str[i] != candidate_str[len(candidate_str)-1-i]:
            success = False
            break

    if success:
        print candidate
        break