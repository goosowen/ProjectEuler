#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Project Euler Problem 230
=======================

For any two strings of digits, A and B, we define F[A,B] to be the
sequence (A,B,AB,BAB,ABBAB,...) in which each term is the concatenation of
the previous two.

Further, we define D[A,B](n) to be the n-th digit in the first term of
F[A,B] that contains at least n digits.

Example:

Let A=1415926535, B=8979323846. We wish to find D[A,B](35), say.

The first few terms of F[A,B] are:
1415926535
8979323846
14159265358979323846
897932384614159265358979323846
14159265358979323846897932384614159265358979323846

Then D[A,B](35) is the 35th digit in the fifth term, which is 9.

Now we use for A the first 100 digits of π behind the decimal point:

14159265358979323846264338327950288419716939937510
58209749445923078164062862089986280348253421170679

and for B the next hundred digits:

82148086513282306647093844609550582231725359408128
48111745028410270193852110555964462294895493038196.

Find ∑[n = 0,1,...,17]   10^n× D[A,B]((127+19n)×7^n).

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
