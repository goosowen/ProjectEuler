#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Project Euler Problem 166
=======================

A 4x4 grid is filled with digits d, 0 d 9.

It can be seen that in the grid

                                 6 3 3 0
                                 5 0 4 3
                                 0 7 1 4
                                 1 2 4 5

the sum of each row and each column has the value 12. Moreover the sum of
each diagonal is also 12.

In how many ways can you fill a 4x4 grid with the digits d, 0 d 9 so that
each row, each column, and both diagonals have the same sum?

"""


def main():
    return "unimplemented"


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
