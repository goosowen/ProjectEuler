#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Project Euler Problem 202
=======================

Three mirrors are arranged in the shape of an equilateral triangle, with
their reflective surfaces pointing inwards. There is an infinitesimal gap
at each vertex of the triangle through which a laser beam may pass.

Label the vertices A, B and C. There are 2 ways in which a laser beam may
enter vertex C, bounce off 11 surfaces, then exit through the same vertex:
one way is shown below; the other is the reverse of that.

[Image: 202_laserbeam.gif]

There are 80840 ways in which a laser beam may enter vertex C, bounce off
1000001 surfaces, then exit through the same vertex.

In how many ways can a laser beam enter at vertex C, bounce off
12017639147 surfaces, then exit through the same vertex?

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
