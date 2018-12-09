#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Project Euler Problem 67
=======================

By starting at the top of the triangle below and moving to adjacent
numbers on the row below, the maximum total from top to bottom is 23.

                                    3
                                   7 4
                                  2 4 6
                                 8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom in triangle.txt, a 15K text file
containing a triangle with one-hundred rows.

NOTE: This is a much more difficult version of Problem 18. It is not
possible to try every route to solve this problem, as there are 2^99
altogether! If you could check one trillion (10^12) routes every second it
would take over twenty billion years to check them all. There is an
efficient algorithm to solve it. ;o)

"""


# TODO put the chdir into the file template
def main():
    import os
    from config import WORKING_DIR

    os.chdir(WORKING_DIR)
    with open('resources/p067_triangle.txt') as f:
        content = f.read().splitlines()

    TRIANGLE = []
    for l in content:
        TRIANGLE.append([int(x) for x in l.split(' ')])

    # maps position (r,c) to best total to that position
    mem = {(0, 0): TRIANGLE[0][0], (1, 0): TRIANGLE[0][0] + TRIANGLE[1][0], (1, 1): TRIANGLE[0][0] + TRIANGLE[1][1]}

    for row in range(2, len(TRIANGLE)):
        mem[(row, 0)] = mem[(row - 1, 0)] + TRIANGLE[row][0]
        mem[(row, row)] = mem[(row - 1, row - 1)] + TRIANGLE[row][row]
        for col in range(1, row):
            mem[(row, col)] = max(mem[(row - 1, col - 1)], mem[(row - 1, col)]) + TRIANGLE[row][col]

    return max(mem.values())


if __name__ == "__main__":
    import ntpath
    import time
    from common.shared_functions import verify_solution

    problem_number = int(ntpath.basename(__file__).replace("euler", "").replace(".py", ""))
    print("Retrieving my answer to Euler Problem {0} ...".format(problem_number))

    ts = time.time()
    my_answer = main()
    te = time.time()

    print("My answer: {1}".format(problem_number, my_answer))

    verification_type = verify_solution(problem_number, my_answer)
    print("Verification: {0}".format(verification_type.name))
    print("Took {0} seconds.".format(te - ts))
