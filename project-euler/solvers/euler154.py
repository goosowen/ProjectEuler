#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Project Euler Problem 154
=======================

A triangular pyramid is constructed using spherical balls so that each
ball rests on exactly three balls of the next lower level.

Then, we calculate the number of paths leading from the apex to each
position:

A path starts at the apex and progresses downwards to any of the three
spheres directly below the current position.

Consequently, the number of paths to reach a certain position is the sum
of the numbers immediately above it (depending on the position, there are
up to three numbers above it).

The result is Pascal's pyramid and the numbers at each level n are the
coefficients of the trinomial expansion (x + y + z)^n.

How many coefficients in the expansion of (x + y + z)^200000 are multiples
of 10^12?

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
