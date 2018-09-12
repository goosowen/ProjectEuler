#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Project Euler Problem 275
=======================

Let us define a balanced sculpture of order n as follows:

 • A polyomino made up of n+1 tiles known as the blocks (n tiles)
   and the plinth (remaining tile);
 • the plinth has its centre at position (x = 0, y = 0);
 • the blocks have y-coordinates greater than zero (so the plinth is the
   unique lowest tile);
 • the centre of mass of all the blocks, combined, has x-coordinate equal
   to zero.

When counting the sculptures, any arrangements which are simply
reflections about the y-axis, are not counted as distinct. For example,
the 18 balanced sculptures of order 6 are shown below; note that each pair
of mirror images (about the y-axis) is counted as one sculpture:

[Image: 275_sculptures2.gif]

There are 964 balanced sculptures of order 10 and 360505 of order 15.
How many balanced sculptures are there of order 18?

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
