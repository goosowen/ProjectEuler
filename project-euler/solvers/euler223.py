#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Project Euler Problem 223
=======================

Let us call an integer sided triangle with sides a ≤ b ≤ c barely acute if
the sides satisfy a^2 + b^2 = c^2 + 1.

How many barely acute triangles are there with perimeter ≤ 25,000,000?

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
