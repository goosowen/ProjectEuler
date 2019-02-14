#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Project Euler Problem 116
=======================

A row of five black square tiles is to have a number of its tiles replaced
with coloured oblong tiles chosen from red (length two), green (length
three), or blue (length four).

If red tiles are chosen there are exactly seven ways this can be done.

                      +----+  +----+  +----+  +----+
                      +----+  +----+  +----+  +----+

                      +----+  +----+  +----+
                      +----+  +----+  +----+

If green tiles are chosen there are three ways.

                        +----+  +----+  +----+
                        +----+  +----+  +----+

And if blue tiles are chosen there are two ways.

                              +----+  +----+
                              +----+  +----+

Assuming that colours cannot be mixed there are 7 + 3 + 2 = 12 ways of
replacing the black tiles in a row measuring five units in length.

How many different ways can the black tiles in a row measuring fifty units
in length be replaced if colours cannot be mixed and at least one coloured
tile must be used?

NOTE: This is related to problem 117.

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
