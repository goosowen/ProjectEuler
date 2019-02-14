#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Project Euler Problem 177
=======================

Let ABCD be a convex quadrilateral, with diagonals AC and BD. At each
vertex the diagonal makes an angle with each of the two sides, creating
eight corner angles.

For example, at vertex A, the two angles are CAD, CAB.

We call such a quadrilateral for which all eight corner angles have
integer values when measured in degrees an "integer angled quadrilateral".
An example of an integer angled quadrilateral is a square, where all eight
corner angles are 45DEG. Another example is given by DAC = 20DEG, BAC =
60DEG, ABD = 50DEG, CBD = 30DEG, BCA = 40DEG, DCA = 30DEG, CDB = 80DEG,
ADB = 50DEG.

What is the total number of non-similar integer angled quadrilaterals?

Note: In your calculations you may assume that a calculated angle is
integral if it is within a tolerance of 10^-9 of an integer value.

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
