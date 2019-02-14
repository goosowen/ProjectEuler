#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Project Euler Problem 127
=======================

The radical of n, rad(n), is the product of distinct prime factors of n.
For example, 504 = 2^3 * 3^2 * 7, so rad(504) = 2 * 3 * 7 = 42.

We shall define the triplet of positive integers (a, b, c) to be an
abc-hit if:

 1. GCD(a, b) = GCD(a, c) = GCD(b, c) = 1
 2. a < b
 3. a + b = c
 4. rad(abc) < c

For example, (5, 27, 32) is an abc-hit, because:

 1. GCD(5, 27) = GCD(5, 32) = GCD(27, 32) = 1
 2. 5 < 27
 3. 5 + 27 = 32
 4. rad(4320) = 30 < 32

It turns out that abc-hits are quite rare and there are only thirty-one
abc-hits for c < 1000, with c = 12523.

Find c for c < 110000.

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
