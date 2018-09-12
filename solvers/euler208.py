#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Project Euler Problem 208
=======================

A robot moves in a series of one-fifth circular arcs (72°), with a free
choice of a clockwise or an anticlockwise arc for each step, but no
turning on the spot.

One of 70932 possible closed paths of 25 arcs starting northward is:

[Image: 208_robotwalk.gif]

Given that the robot starts facing North, how many journeys of 70 arcs in
length can it take that return it, after the final arc, to its starting
position?
(Any arc may be traversed multiple times.)

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
