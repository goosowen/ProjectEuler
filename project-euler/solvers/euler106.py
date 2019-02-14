#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Project Euler Problem 106
=======================

Let S(A) represent the sum of elements in set A of size n. We shall call
it a special sum set if for any two non-empty disjoint subsets, B and C,
the following properties are true:

 1. S(B) S(C); that is, sums of subsets cannot be equal.
 2. If B contains more elements than C then S(B) > S(C).

For this problem we shall assume that a given set contains n strictly
increasing elements and it already satisfies the second rule.

Surprisingly, out of the 25 possible subset pairs that can be obtained
from a set for which n = 4, only 1 of these pairs need to be tested for
equality (first rule). Similarly, when n = 7, only 70 out of the 966
subset pairs need to be tested.

For n = 12, how many of the 261625 subset pairs that can be obtained need
to be tested for equality?

NOTE: This problem is related to problems 103 and 105.

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
