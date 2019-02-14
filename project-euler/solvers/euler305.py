#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Project Euler Problem 305
=======================

Let's call S the (infinite) string that is made by concatenating the
consecutive positive integers (starting from 1) written down in base 10.
Thus, S = 1234567891011121314151617181920212223242...

It's easy to see that any number will show up an infinite number of times
in S.

Let's call f(n) the starting position of the n^th occurrence of n in S.
For example, f(1)=1, f(5)=81, f(12)=271 and f(7780)=111111365.

Find ∑f(3^k) for 1 ≤ k ≤ 13.

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
