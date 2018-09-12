#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Project Euler Problem 241
=======================

For a positive integer n, let σ(n) be the sum of all divisors of n, so
e.g. σ(6) = 1 + 2 + 3 + 6 = 12.

A perfect number, as you probably know, is a number with σ(n) = 2n.

Let us define the perfection quotient of a positive integer as
p(n) = σ(n) / n.

Find the sum of all positive integers n ≤ 10^18 for which p(n) has the
form k + ^1⁄[2], where k is an integer.

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
