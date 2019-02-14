#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Project Euler Problem 74
=======================

The number 145 is well known for the property that the sum of the
factorial of its digits is equal to 145:

1! + 4! + 5! = 1 + 24 + 120 = 145

Perhaps less well known is 169, in that it produces the longest chain of
numbers that link back to 169; it turns out that there are only three such
loops that exist:

169 363601 1454 169
871 45361 871
872 45362 872

It is not difficult to prove that EVERY starting number will eventually
get stuck in a loop. For example,

69 363600 1454 169 363601 ( 1454)
78 45360 871 45361 ( 871)
540 145 ( 145)

Starting with 69 produces a chain of five non-repeating terms, but the
longest non-repeating chain with a starting number below one million is
sixty terms.

How many chains, with a starting number below one million, contain exactly
sixty non-repeating terms?

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
