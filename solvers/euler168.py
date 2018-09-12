#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Project Euler Problem 168
=======================

Consider the number 142857. We can right-rotate this number by moving the
last digit (7) to the front of it, giving us 714285.
It can be verified that 714285=5 * 142857.
This demonstrates an unusual property of 142857: it is a divisor of its
right-rotation.

Find the last 5 digits of the sum of all integers n, 10 < n < 10^100, that
have this property.

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
