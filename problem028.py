#!/usr/bin/python
import time
"""


Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?

"""
__author__ = 'moriano'

"""
The solution is simple, if you check the upper right diagonal, the numbers are

1 9 25
Sounds familiar? They are the squares of odd numbers

1**2 3**2 5**2

With that in mind, it is pretty easy to calculate the other diagonals, for example the upper left diagonal is

1 7 21
which essentially is

1**2, 3**2 - (3-1), 5**2 - (5-1)

And then, the same can be done for the rest of the diagonals.
Assuming a 1001 x 1001 square, we must go up to 1001**2
"""

start = time.time()
upper_right = 0
upper_left = 0
lower_right = 0
lower_left = 0
i = 3
while i < 1002:
    upper_right += i**2
    upper_left += i**2 - (i-1)
    lower_left += i**2 - 2*(i-1)
    lower_right += i**2 - 3*(i - 1)
    i+=2
solution = upper_right + upper_left + lower_left + lower_right + 1
print "Solution is %d took %f to calculate" % (solution, time.time() - start)