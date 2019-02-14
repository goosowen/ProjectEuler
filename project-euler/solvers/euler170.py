#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Project Euler Problem 170
=======================

Take the number 6 and multiply it by each of 1273 and 9854:

6 * 1273 = 7638
6 * 9854 = 59124

By concatenating these products we get the 1 to 9 pandigital 763859124. We
will call 763859124 the "concatenated product of 6 and (1273,9854)".
Notice too, that the concatenation of the input numbers, 612739854, is
also 1 to 9 pandigital.

The same can be done for 0 to 9 pandigital numbers.

What is the largest 0 to 9 pandigital 10-digit concatenated product of an
integer with two or more other integers, such that the concatenation of
the input numbers is also a 0 to 9 pandigital 10-digit number?

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
