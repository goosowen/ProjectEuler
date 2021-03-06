#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Project Euler Problem 262
=======================

The following equation represents the continuous topography of a
mountainous region, giving the elevation h at any point (x,y):

[Image: 262_formula1.gif]

A mosquito intends to fly from A(200,200) to B(1400,1400), without leaving
the area given by 0 ≤ x, y ≤ 1600.

Because of the intervening mountains, it first rises straight up to a
point A', having elevation f. Then, while remaining at the same elevation
f, it flies around any obstacles until it arrives at a point B' directly
above B.

First, determine f[min] which is the minimum constant elevation allowing
such a trip from A to B, while remaining in the specified area.
Then, find the length of the shortest path between A' and B', while flying
at that constant elevation f[min].

Give that length as your answer, rounded to three decimal places.

Note: For convenience, the elevation function in the image above can be
written as the following in Python (the math module must be imported):

def elevation(x, y):
    first = 5000.0 - ((x**2 + y**2 + x*y)/200.0) + (12.5*(x+y))
    second = (0.000001 * (x**2 + y**2)) - (0.0015*(x+y)) + 0.7
    return first * math.exp(-abs(second))

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
