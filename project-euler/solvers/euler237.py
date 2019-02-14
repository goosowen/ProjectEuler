#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Project Euler Problem 237
=======================

Let T(n) be the number of tours over a 4 × n playing board such that:

 • The tour starts in the top left corner.
 • The tour consists of moves that are up, down, left, or right one
   square.
 • The tour visits each square exactly once.
 • The tour ends in the bottom left corner.

The diagram shows one tour over a 4 × 10 board:

[Image: 237.gif]

T(10) is 2329. What is T(10^12) modulo 10^8?

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
