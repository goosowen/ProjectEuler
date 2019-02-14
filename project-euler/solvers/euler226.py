#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Project Euler Problem 226
=======================

The blancmange curve is the set of points (x,y) such that 0 ≤ x ≤ 1 and

[Image: 226_formula.gif]

where s(x) = the distance from x to the nearest integer.

The area under the blancmange curve is equal to ½, shown in pink in the
diagram below.

[Image: 226_scoop2.gif]

Let C be the circle with centre (¼,½) and radius ¼, shown in black in the
diagram.

What area under the blancmange curve is enclosed by C?
Give your answer rounded to eight decimal places in the form 0.abcdefgh

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
