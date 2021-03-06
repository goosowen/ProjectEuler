#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Project Euler Problem 20
=======================

n! means n * (n - 1) * ... * 3 * 2 * 1

Find the sum of the digits in the number 100!

"""


def main():
    fact = 1
    for i in range(1, 101):
        fact *= i

    tot = 0
    for c in str(fact):
        tot += int(c)

    return tot


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
