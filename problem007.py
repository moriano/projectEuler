#!/usr/bin/python
"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""
import time
__author__ = 'moriano'

def simple_solution():
    """
    Simplest approach is to evaluate every odd number to check if it is prime, although it solves the problem,
    we can do better
    """
    primes = [2]

    def is_prime(candidate):
        for prime in primes:
            if candidate % prime == 0:
                return False

        for test in range(3, int(candidate/2)):
            if candidate % test == 0:
                return False

        return True

    candidate = 3
    while len(primes) < 10001:
        if is_prime(candidate):
            primes.append(candidate)

        candidate += 2

    return primes[len(primes)-1]

start = time.time()
solution = simple_solution()
end = time.time()
print "Solution is %d calculation took %d seconds" % (solution, end-start)