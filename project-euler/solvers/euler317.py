#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Project Euler Problem 317
=======================

A firecracker explodes at a height of 100 m above level ground. It breaks
into a large number of very small fragments, which move in every
direction; all of them have the same initial velocity of 20 m/s.

We assume that the fragments move without air resistance, in a uniform
gravitational field with g=9.81 m/s^2.

Find the volume (in m^3) of the region through which the fragments move
before reaching the ground. Give your answer rounded to four decimal
places.

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
