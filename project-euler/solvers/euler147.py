#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Project Euler Problem 147
=======================

In a 3x2 cross-hatched grid, a total of 37 different rectangles could be
situated within that grid as indicated in the sketch.

There are 5 grids smaller than 3x2, vertical and horizontal dimensions
being important, i.e. 1x1, 2x1, 3x1, 1x2 and 2x2. If each of them is
cross-hatched, the following number of different rectangles could be
situated within those smaller grids:

1x1: 1
2x1: 4
3x1: 8
1x2: 4
2x2: 18

Adding those to the 37 of the 3x2 grid, a total of 72 different rectangles
could be situated within 3x2 and smaller grids.

How many different rectangles could be situated within 47x43 and smaller
grids?

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
