#!/usr/bin/python
"""
By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom of the triangle below:

75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23

NOTE: As there are only 16384 routes, it is possible to solve this problem by trying every route. However, Problem 67,
is the same challenge with a triangle containing one-hundred rows; it cannot be solved by brute force, and requires a
clever method! ;o)

"""
__author__ = 'moriano'
import time


"""
This can be done even without a computer, just computer the maximun possible for the triangle starting from the
bottom and recursively go to the top, example

Problem base
3
7 4
2 4 6
8 5 9 3

Take the bottom line, and compare it with the upper one, and check which ones are the maximuns, example
2 + 8 > 2 +5 ==> 10
4 + 9 > 4 +5 ==> 13
6 + 9 > 6 +3 ==> 15

Which gives us a smaller triangle

3
7  4
10 13 15

We now repeat the process

3
20 19

And once again

23

Ta - da! solved

"""
problem = [
    [75],
    [95, 64],
    [17, 47, 82],
    [18, 35, 87, 10],
    [20, 04, 82, 47, 65],
    [19, 01, 23, 75, 03, 34],
    [88, 02, 77, 73, 07, 63, 67],
    [99, 65, 04, 28, 06, 16, 70, 92],
    [41, 41, 26, 56, 83, 40, 80, 70, 33],
    [41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
    [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
    [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
    [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
    [63, 66, 04, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
    [04, 62, 98, 27, 23,  9, 70, 98, 73, 93, 38, 53, 60, 04, 23]
]


def maximize(triangle):

    if len(triangle) == 1:
        return triangle[0]
    else:
        last_row = triangle[len(triangle)-1]
        second_last_row = triangle[len(triangle) - 2]

        for i in range(0, len(second_last_row)):
            second_last_row[i] = second_last_row[i] + last_row[i] if second_last_row[i] + last_row[i] > second_last_row[i] + last_row[i+1] else second_last_row[i] + last_row[i+1]

        del(triangle[len(triangle)-1])

        return maximize(triangle)

start = time.time()
print "Solution is %d, took %f" % (maximize(problem)[0], time.time() - start)
