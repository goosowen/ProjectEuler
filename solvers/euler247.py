#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Project Euler Problem 247
=======================

Consider the region constrained by 1 ≤ x and 0 ≤ y ≤ 1/x.

Let S[1] be the largest square that can fit under the curve.
Let S[2] be the largest square that fits in the remaining area, and so on.
Let the index of S[n] be the pair (left, below) indicating the number of
squares to the left of S[n] and the number of squares below S[n].

[Image: 247_hypersquares.gif]

The diagram shows some such squares labelled by number.
S[2] has one square to its left and none below, so the index of S[2] is
(1,0).
It can be seen that the index of S[32] is (1,1) as is the index of S[50].
50 is the largest n for which the index of S[n] is (1,1).

What is the largest n for which the index of S[n] is (3,3)?

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
