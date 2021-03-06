#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Project Euler Problem 264
=======================

Consider all the triangles having:

 • All their vertices on lattice points.
 • Circumcentre at the origin O.
 • Orthocentre at the point H(5, 0).

There are nine such triangles having a perimeter ≤ 50.
Listed and shown in ascending order of their perimeter, they are:

A(-4, 3), B(5, 0), C(4, -3)
A(4, 3),  B(5, 0), C(-4, -3)
A(-3, 4), B(5, 0), C(3, -4)

A(3, 4),  B(5, 0),  C(-3, -4)
A(0, 5),  B(5, 0),  C(0, -5)
A(1, 8),  B(8, -1), C(-4, -7)

A(8, 1),  B(1, -8), C(-4, 7)
A(2, 9),  B(9, -2), C(-6, -7)
A(9, 2),  B(2, -9), C(-6, 7)

[Image: 264_TriangleCentres.gif]

The sum of their perimeters, rounded to four decimal places, is 291.0089.

Find all such triangles with a perimeter ≤ 10^5.
Enter as your answer the sum of their perimeters rounded to four decimal
places.

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
