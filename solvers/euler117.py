#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Project Euler Problem 117
=======================

Using a combination of black square tiles and oblong tiles chosen from:
red tiles measuring two units, green tiles measuring three units, and blue
tiles measuring four units, it is possible to tile a row measuring five
units in length in exactly fifteen different ways.

                      +----+  +----+  +----+  +----+
                      +----+  +----+  +----+  +----+

                      +----+  +----+  +----+  +----+
                      +----+  +----+  +----+  +----+

                      +----+  +----+  +----+  +----+
                      +----+  +----+  +----+  +----+

                      +----+  +----+  +----+
                      +----+  +----+  +----+

How many ways can a row measuring fifty units in length be tiled?

NOTE: This is related to problem 116.

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
