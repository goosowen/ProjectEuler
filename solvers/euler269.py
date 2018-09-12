#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Project Euler Problem 269
=======================

A root or zero of a polynomial P(x) is a solution to the equation P(x) = 0.
Define P[n] as the polynomial whose coefficients are the digits of n.
For example, P[5703](x) = 5x^3 + 7x^2 + 3.

We can see that:

 • P[n](0) is the last digit of n,
 • P[n](1) is the sum of the digits of n,
 • P[n](10) is n itself.

Define Z(k) as the number of positive integers, n, not exceeding k for
which the polynomial P[n] has at least one integer root.

It can be verified that Z(100 000) is 14696.

What is Z(10^16)?

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
