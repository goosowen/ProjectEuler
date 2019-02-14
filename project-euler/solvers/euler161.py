#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Project Euler Problem 161
=======================

A triomino is a shape consisting of three squares joined via the
edges.There are two basic forms:

If all possible orientations are taken into account there are six:

Any n by m grid for which nxm is divisible by 3 can be tiled with
triominoes.
If we consider tilings that can be obtained by reflection or rotation from
another tiling as different there are 41 ways a 2 by 9 grid can be tiled
with triominoes:

In how many ways can a 9 by 12 grid be tiled in this way by triominoes?

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
