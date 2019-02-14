#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Project Euler Problem 190
=======================

Let S[m] = (x[1], x[2], ... , x[m]) be the m-tuple of positive real
numbers with x[1] + x[2] + ... + x[m] = m for which P[m] = x[1] * x[2]^2 *
... * x[m]^m is maximised.

For example, it can be verified that [P[10]] = 4112 ([ ] is the integer
part function).

Find S[P[m]] for 2 m 15.

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
