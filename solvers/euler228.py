#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Project Euler Problem 228
=======================

Let S[n] be the regular n-sided polygon – or shape – whose vertices v[k]
(k = 1,2,…,n) have coordinates:

      x[k]   =   cos( ^2k-1/[n] × 180° )
      y[k]   =   sin( ^2k-1/[n] × 180° )

Each S[n] is to be interpreted as a filled shape consisting of all points
on the perimeter and in the interior.

The Minkowski sum, S+T, of two shapes S and T is the result of adding
every point in S to every point in T, where point addition is performed
coordinate-wise: (u, v) + (x, y) = (u+x, v+y).

For example, the sum of S[3] and S[4] is the six-sided shape shown in pink
below:

[Image: 228.png]

How many sides does S[1864] + S[1865] + … + S[1909] have?

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
