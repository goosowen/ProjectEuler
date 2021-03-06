#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Project Euler Problem 267
=======================

You are given a unique investment opportunity.

Starting with £1 of capital, you can choose a fixed proportion, f, of your
capital to bet on a fair coin toss repeatedly for 1000 tosses.

Your return is double your bet for heads and you lose your bet for tails.

For example, if f = 1/4, for the first toss you bet £0.25, and if heads
comes up you win £0.5 and so then have £1.5. You then bet £0.375 and if
the second toss is tails, you have £1.125.

Choosing f to maximize your chances of having at least £1,000,000,000
after 1,000 flips, what is the chance that you become a billionaire?

All computations are assumed to be exact (no rounding), but give your
answer rounded to 12 digits behind the decimal point in the form
0.abcdefghijkl.

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
