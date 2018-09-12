#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Project Euler Problem 189
=======================

Consider the following configuration of 64 triangles:

We wish to colour the interior of each triangle with one of three colours:
red, green or blue, so that no two neighbouring triangles have the same
colour. Such a colouring shall be called valid. Here, two triangles are
said to be neighbouring if they share an edge.
Note: if they only share a vertex, then they are not neighbours.

For example, here is a valid colouring of the above grid:

A colouring C' which is obtained from a colouring C by rotation or
reflection is considered distinct from C unless the two are identical.

How many distinct valid colourings are there for the above configuration?

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
