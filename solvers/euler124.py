#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Project Euler Problem 124
=======================

The radical of n, rad(n), is the product of distinct prime factors of n.
For example, 504 = 2^3 * 3^2 * 7, so rad(504) = 2 * 3 * 7 = 42.

If we calculate rad(n) for 1 n 10, then sort them on rad(n), and sorting
on n if the radical values are equal, we get:

                         Unsorted       Sorted
                         n  rad(n)   n  rad(n) k
                         1    1      1    1    1
                         2    2      2    2    2
                         3    3      4    2    3
                         4    2      8    2    4
                         5    5      3    3    5
                         6    6      9    3    6
                         7    7      5    5    7
                         8    2      6    6    8
                         9    3      7    7    9
                         10   10     10   10   10

Let E(k) be the kth element in the sorted n column; for example, E(4) = 8
and E(6) = 9.

If rad(n) is sorted for 1 n 100000, find E(10000).

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
