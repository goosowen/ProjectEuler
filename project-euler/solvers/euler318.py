#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Project Euler Problem 318
=======================

Consider the real number √2+√3.
When we calculate the even powers of √2+√3we get:
(√2+√3)^2 = 9.898979485566356...
(√2+√3)^4 = 97.98979485566356...
(√2+√3)^6 = 969.998969071069263...
(√2+√3)^8 = 9601.99989585502907...
(√2+√3)^10 = 95049.999989479221...
(√2+√3)^12 = 940897.9999989371855...
(√2+√3)^14 = 9313929.99999989263...
(√2+√3)^16 = 92198401.99999998915...

It looks like that the number of consecutive nines at the beginning of the
fractional part of these powers is non-decreasing. In fact it can be
proven that the fractional part of (√2+√3)^2n approaches 1 for large n.

Consider all real numbers of the form √p+√q with p and q positive integers
and p<q, such that the fractional part of (√p+√q)^2n approaches 1 for
large n.

Let C(p, q, n) be the number of consecutive nines at the beginning of the
fractional part of (√p+√q)^2n.

Let N(p,q) be the minimal value of n such that C(p,q,n) ≥ 2011.

Find ∑N(p,q) for p+q ≤ 2011.

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
