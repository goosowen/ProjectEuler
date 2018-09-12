#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Project Euler Problem 239
=======================

A set of disks numbered 1 through 100 are placed in a line in random
order.

What is the probability that we have a partial derangement such that
exactly 22 prime number discs are found away from their natural positions?
(Any number of non-prime disks may also be found in or out of their
natural positions.)

Give your answer rounded to 12 places behind the decimal point in the form
0.abcdefghijkl.

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
