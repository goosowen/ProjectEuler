#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Project Euler Problem 119
=======================

The number 512 is interesting because it is equal to the sum of its digits
raised to some power: 5 + 1 + 2 = 8, and 8^3 = 512. Another example of a
number with this property is 614656 = 28^4.

We shall define a[n] to be the nth term of this sequence and insist that a
number must contain at least two digits to have a sum.

You are given that a[2] = 512 and a[10] = 614656.

Find a[30].

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
