#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Project Euler Problem 307
=======================

k defects are randomly distributed amongst n integrated-circuit chips
produced by a factory (any number of defects may be found on a chip and
each defect is independent of the other defects).

Let p(k, n) represent the probability that there is a chip with at least
3 defects. For instance p(3, 7) ≈ 0.0204081633.

Find p(20 000, 1 000 000) and give your answer rounded to 10 decimal
places in the form 0.abcdefghij

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
