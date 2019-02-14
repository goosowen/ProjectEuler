#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Project Euler Problem 320
=======================

Let N(i) be the smallest integer n such that n! is divisible by
(i!)^1234567890

Let S(u)=∑N(i) for 10 ≤ i ≤ u.

S(1000)=614538266565663.

Find S(1 000 000) mod 10^18.

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
