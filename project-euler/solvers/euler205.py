#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Project Euler Problem 205
=======================

Peter has nine four-sided (pyramidal) dice, each with faces numbered 1, 2,
3, 4.
Colin has six six-sided (cubic) dice, each with faces numbered 1, 2, 3, 4,
5, 6.

Peter and Colin roll their dice and compare totals: the highest total
wins. The result is a draw if the totals are equal.

What is the probability that Pyramidal Pete beats Cubic Colin? Give your
answer rounded to seven decimal places in the form 0.abcdefg

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
