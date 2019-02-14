#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Project Euler Problem 194
=======================

Consider graphs built with the units A: and B: , where the units are glued
alongthe vertical edges as in the graph .

A configuration of type (a,b,c) is a graph thus built of a units A and b
units B, where the graph's vertices are coloured using up to c colours, so
that no two adjacent vertices have the same colour.
The compound graph above is an example of a configuration of type (2,2,6),
in fact of type (2,2,c) for all c 4.

Let N(a,b,c) be the number of configurations of type (a,b,c).
For example, N(1,0,3) = 24, N(0,2,4) = 92928 and N(2,2,3) = 20736.

Find the last 8 digits of N(25,75,1984).

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
