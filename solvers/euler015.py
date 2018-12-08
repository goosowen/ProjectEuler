#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Project Euler Problem 15
=======================

Starting in the top left corner of a 2 * 2 grid, there are 6 routes
(without backtracking) to the bottom right corner.

How many routes are there through a 20 * 20 grid?

"""


def main():
    from common.euler_functions import choose

    # It's 40 choose 20 = 137846528820
    # There are 40 moves and 20 of them have to be down, 20 have to be right.
    # It doesn't matter the order.
    return choose(40, 20)


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
