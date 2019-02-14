#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Project Euler Problem 88
=======================

A natural number, N, that can be written as the sum and product of a given
set of at least two natural numbers, {a[1], a[2], ... , a[k]} is called a
product-sum number: N = a[1] + a[2] + ... + a[k] = a[1] * a[2] * ... *
a[k].

For example, 6 = 1 + 2 + 3 = 1 * 2 * 3.

For a given set of size, k, we shall call the smallest N with this
property a minimal product-sum number. The minimal product-sum numbers for
sets of size, k = 2, 3, 4, 5, and 6 are as follows.

k=2: 4 = 2 * 2 = 2 + 2
k=3: 6 = 1 * 2 * 3 = 1 + 2 + 3
k=4: 8 = 1 * 1 * 2 * 4 = 1 + 1 + 2 + 4
k=5: 8 = 1 * 1 * 2 * 2 * 2 = 1 + 1 + 2 + 2 + 2
k=6: 12 = 1 * 1 * 1 * 1 * 2 * 6 = 1 + 1 + 1 + 1 + 2 + 6

Hence for 2k6, the sum of all the minimal product-sum numbers is 4+6+8+12
= 30; note that 8 is only counted once in the sum.

In fact, as the complete set of minimal product-sum numbers for 2k12 is
{4, 6, 8, 12, 15, 16}, the sum is 61.

What is the sum of all the minimal product-sum numbers for 2k12000?

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
