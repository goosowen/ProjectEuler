#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Project Euler Problem 261
=======================

Let us call a positive integer k a square-pivot, if there is a pair of
integers m > 0 and n ≥ k, such that the sum of the (m+1) consecutive
squares up to k equals the sum of the m consecutive squares from (n+1) on:

             (k-m)^2 + ... + k^2 = (n+1)^2 + ... + (n+m)^2.

Some small square-pivots are

 • 4: 3^2 + 4^2 = 5^2
 • 21: 20^2 + 21^2 = 29^2
 • 24: 21^2 + 22^2 + 23^2 + 24^2 = 25^2 + 26^2 + 27^2
 • 110: 108^2 + 109^2 + 110^2 = 133^2 + 134^2

Find the sum of all distinct square-pivots ≤ 10^10.

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
