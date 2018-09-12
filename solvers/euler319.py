#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Project Euler Problem 319
=======================

Let x[1], x[2], ..., x[n] be a sequence of length n such that:

 • x[1] = 2
 • for all 1 < i ≤ n : x[i-1] < x[i]
 • for all i and j with 1 ≤ i, j ≤ n : (x[i]) ^ j < (x[j] + 1)^i

There are only five such sequences of length 2, namely: {2,4}, {2,5},
{2,6}, {2,7} and {2,8}.

There are 293 such sequences of length 5; three examples are given below:
{2,5,11,25,55}, {2,6,14,36,88}, {2,8,22,64,181}.

Let t(n) denote the number of such sequences of length n.
You are given that t(10) = 86195 and t(20) = 5227991891.

Find t(10^10) and give your answer modulo 10^9.

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
