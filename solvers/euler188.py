#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Project Euler Problem 188
=======================

The hyperexponentiation or tetration of a number a by a positive integer
b, denoted by a-^-^b or ^ba, is recursively defined by:

a-^-^1 = a,
a-^-^(k+1) = a^(a-^-^k).

Thus we have e.g. 3-^-^2 = 3^3 = 27, hence 3-^-^3 = 3^27 = 7625597484987
and 3-^-^4 is roughly 10^3.6383346400240996*10^12.

Find the last 8 digits of 1777-^-^1855.

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
