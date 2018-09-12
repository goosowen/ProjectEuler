#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Project Euler Problem 272
=======================

For a positive number n, define C(n) as the number of the integers x, for
which 1 < x < n and x^3 ≡ 1 mod n.

When n=91, there are 8 possible values for x, namely: 9, 16, 22, 29, 53,
74, 79, 81. Thus, C(91)=8.

Find the sum of the positive numbers n ≤ 10^11 for which C(n) = 242.

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
