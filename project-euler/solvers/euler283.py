#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Project Euler Problem 283
=======================

Consider the triangle with sides 6, 8 and 10. It can be seen that the
perimeter and the area are both equal to 24. So the area/perimeter ratio
is equal to 1.

Consider also the triangle with sides 13, 14 and 15. The perimeter equals
42 while the area is equal to 84. So for this triangle the area/perimeter
ratio is equal to 2.

Find the sum of the perimeters of all integer sided triangles for which
the area/perimeter ratios are equal to positive integers not exceeding
1000.

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
