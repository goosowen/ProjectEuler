#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Project Euler Problem 126
=======================

The minimum number of cubes to cover every visible face on a cuboid
measuring 3 x 2 x 1 is twenty-two.

If we then add a second layer to this solid it would require forty-six
cubes to cover every visible face, the third layer would require
seventy-eight cubes, and the fourth layer would require one-hundred and
eighteen cubes to cover every visible face.

However, the first layer on a cuboid measuring 5 x 1 x 1 also requires
twenty-two cubes; similarly the first layer on cuboids measuring
5 x 3 x 1, 7 x 2 x 1, and 11 x 1 x 1 all contain forty-six cubes.

We shall define C(n) to represent the number of solids that contain n
cubes in one of its layers. So C(22) = 2, C(46) = 4, C(78) = 5, and C(118)
= 8.

It turns out that 154 is the least value of n for which C(n) = 10.

Find the least value of n for which C(n) = 1000.

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
