#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Project Euler Problem 139
=======================

Let (a, b, c) represent the three sides of a right angle triangle with
integral length sides. It is possible to place four such triangles
together to form a square with length c.

For example, (3, 4, 5) triangles can be placed together to form a 5 by 5
square with a 1 by 1 hole in the middle and it can be seen that the 5 by 5
square can be tiled with twenty-five 1 by 1 squares.

However, if (5, 12, 13) triangles were used then the hole would measure 7
by 7 and these could not be used to tile the 13 by 13 square.

Given that the perimeter of the right triangle is less than one-hundred
million, how many Pythagorean triangles would allow such a tiling to take
place?

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
