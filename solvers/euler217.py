#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Project Euler Problem 217
=======================

A positive integer with k (decimal) digits is called balanced if its first
⌈^k/[2]⌉ digits sum to the same value as its last ⌈^k/[2]⌉ digits, where
⌈x⌉, pronounced ceiling of x, is the smallest integer ≥ x, thus ⌈π⌉ = 4
and ⌈5⌉ = 5.

So, for example, all palindromes are balanced, as is 13722.

Let T(n) be the sum of all balanced numbers less than 10^n.
Thus: T(1) = 45, T(2) = 540 and T(5) = 334795890.

Find T(47) mod 3^15

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
