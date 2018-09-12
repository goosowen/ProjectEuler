#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Project Euler Problem 322
=======================

Let T(m, n) be the number of the binomial coefficients ^iC[n] that are
divisible by 10 for n ≤ i < m(i, m and n are positive integers).
You are given that T(10^9, 10^7-10) = 989697000.

Find T(10^18, 10^12-10).

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
