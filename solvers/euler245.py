#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Project Euler Problem 245
=======================

We shall call a fraction that cannot be cancelled down a resilient
fraction. Furthermore we shall define the resilience of a denominator,
R(d), to be the ratio of its proper fractions that are resilient; for
example, R(12) = 4⁄/11.

The resilience of a number d > 1 is then φ(d) / (d - 1), where φ is Euler's
totient function.

We further define the coresilience of a number n > 1 as
C(n) = (n - φ(n)) / (n-1).

The coresilience of a prime p is C(p) = 1 / (p - 1).

Find the sum of all composite integers 1 < n ≤ 2×10^11, for which C(n) is
a unit fraction.

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
