#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Project Euler Problem 210
=======================

   Consider the set S(r) of points (x,y) with integer coordinates satisfying
   |x| + |y| ≤ r.
   Let O be the point (0,0) and C the point (r/4,r/4).
   Let N(r) be the number of points B in S(r), so that the triangle OBC has
   an obtuse angle, i.e. the largest angle α satisfies 90°<α<180°.
   So, for example, N(4)=24 and N(8)=100.

   What is N(1,000,000,000)?

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
