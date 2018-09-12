#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Project Euler Problem 91
=======================

The points P (x[1], y[1]) and Q (x[2], y[2]) are plotted at integer
co-ordinates and are joined to the origin, O(0,0), to form DOPQ.

There are exactly fourteen triangles containing a right angle that can be
formed when each co-ordinate lies between 0 and 2 inclusive; that is,
0 x[1], y[1], x[2], y[2] 2.

Given that 0 x[1], y[1], x[2], y[2] 50, how many right triangles can be
formed?

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
