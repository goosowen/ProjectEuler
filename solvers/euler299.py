#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Project Euler Problem 299
=======================

Four points with integer coordinates are selected:
A(a, 0), B(b, 0), C(0, c) and D(0, d), with 0 < a < b and 0 < c < d.
Point P, also with integer coordinates, is chosen on the line AC so that
the three triangles ABP, CDP and BDP are all similar.

[Image: 299_ThreeSimTri.gif]

It is easy to prove that the three triangles can be similar, only if a=c.

So, given that a=c, we are looking for triplets (a,b,d) such that at least
one point P (with integer coordinates) exists on AC, making the three
triangles ABP, CDP and BDP all similar.

For example, if (a,b,d)=(2,3,4), it can be easily verified that point
P(1,1) satisfies the above condition. Note that the triplets (2,3,4) and
(2,4,3) are considered as distinct, although point P(1,1) is common for
both.

If b+d < 100, there are 92 distinct triplets (a,b,d) such that point P
exists.
If b+d < 100 000, there are 320471 distinct triplets (a,b,d) such that
point P exists.

If b+d < 100 000 000, how many distinct triplets (a,b,d) are there such
that point P exists?

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
