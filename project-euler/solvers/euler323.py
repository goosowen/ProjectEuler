#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Project Euler Problem 323
=======================

Let y[0], y[1], y[2],... be a sequence of random unsigned 32 bit integers
(i.e. 0 ≤ y[i] < 2^32, every value equally likely).

For the sequence x[i] the following recursion is given:

 • x[0] = 0 and
 • x[i] = x[i-1] | y[i-1], for i > 0. ( | is the bitwise-OR operator)

It can be seen that eventually there will be an index N such that x[i] =
2^32 -1 (a bit-pattern of all ones) for all i ≥ N.

Find the expected value of N.
Give your answer rounded to 10 digits after the decimal point.

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
