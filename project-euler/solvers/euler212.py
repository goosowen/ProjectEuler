#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Project Euler Problem 212
=======================

An axis-aligned cuboid, specified by parameters { (x[0],y[0],z[0]),
(dx,dy,dz) }, consists of all points (X,Y,Z) such that x[0] ≤ X ≤ x[0]+dx,
y[0] ≤ Y ≤ y[0]+dy and z[0] ≤ Z ≤ z[0]+dz. The volume of the cuboid is the
product, dx × dy × dz. The combined volume of a collection of cuboids is
the volume of their union and will be less than the sum of the individual
volumes if any cuboids overlap.

Let C[1],...,C[50000] be a collection of 50000 axis-aligned cuboids such
that C[n] has parameters

x[0] = S[6n-5] modulo 10000
y[0] = S[6n-4] modulo 10000
z[0] = S[6n-3] modulo 10000
dx = 1 + (S[6n-2] modulo 399)
dy = 1 + (S[6n-1] modulo 399)
dz = 1 + (S[6n] modulo 399)

where S[1],...,S[300000] come from the "Lagged Fibonacci Generator":

For 1 ≤ k ≤ 55, S[k] = [100003 - 200003k + 300007k^3]   (modulo 1000000)
For 56 ≤ k, S[k] = [S[k-24] + S[k-55]]   (modulo 1000000)

Thus, C[1] has parameters {(7,53,183),(94,369,56)}, C[2] has parameters
{(2383,3563,5079),(42,212,344)}, and so on.

The combined volume of the first 100 cuboids, C[1],...,C[100], is
723581599.

What is the combined volume of all 50000 cuboids, C[1],...,C[50000]?

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
