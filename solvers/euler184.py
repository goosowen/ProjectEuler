#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Project Euler Problem 184
=======================

Consider the set I[r] of points (x,y) with integer co-ordinates in the
interior of the circle with radius r, centered at the origin, i.e. x^2 +
y^2 < r^2.

For a radius of 2, I[2] contains the nine points (0,0), (1,0), (1,1),
(0,1), (-1,1), (-1,0), (-1,-1), (0,-1) and (1,-1). There are eight
triangles having all three vertices in I[2] which contain the origin in
the interior. Two of them are shown below, the others are obtained from
these by rotation.

For a radius of 3, there are 360 triangles containing the origin in the
interior and having all vertices in I[3] and for I[5] the number is 10600.

How many triangles are there containing the origin in the interior and
having all three vertices in I[105]?

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
