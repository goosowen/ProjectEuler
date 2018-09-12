#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Project Euler Problem 216
=======================

 Consider numbers t(n) of the form t(n) = 2n^2-1 with n > 1.
 The first such numbers are 7, 17, 31, 49, 71, 97, 127 and 161.
 It turns out that only 49 = 7*7 and 161 = 7*23 are not prime.
 For n ≤ 10000 there are 2202 numbers t(n) that are prime.

 How many numbers t(n) are prime for n ≤ 50,000,000?

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
