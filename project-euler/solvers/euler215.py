#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Project Euler Problem 215
=======================

Consider the problem of building a wall out of 2×1 and 3×1 bricks
(horizontal×vertical dimensions) such that, for extra strength, the gaps
between horizontally-adjacent bricks never line up in consecutive layers,
i.e. never form a "running crack".

For example, the following 9×3 wall is not acceptable due to the running
crack shown in red:

[Image: 215_crackfree.gif]

There are eight ways of forming a crack-free 9×3 wall, written W(9,3) = 8.

Calculate W(32,10).

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
