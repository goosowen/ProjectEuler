#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Project Euler Problem 132
=======================

A number consisting entirely of ones is called a repunit. We shall define
R(k) to be a repunit of length k.

For example, R(10) = 1111111111 = 11 * 41 * 271 * 9091, and the sum of
these prime factors is 9414.

Find the sum of the first forty prime factors of R(10^9).

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
