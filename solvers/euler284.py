#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Project Euler Problem 284
=======================

The 3-digit number 376 in the decimal numbering system is an example of
numbers with the special property that its square ends with the same
digits: 376^2 = 141376. Let's call a number with this property a steady
square.

Steady squares can also be observed in other numbering systems. In the
base 14 numbering system, the 3-digit number c37 is also a steady square:
c37^2 = aa0c37, and the sum of its digits is c + 3 + 7 = 18 in the same
numbering system. The letters a, b, c and d are used for the 10, 11, 12
and 13 digits respectively, in a manner similar to the hexadecimal
numbering system.

For 1 ≤ n ≤ 9, the sum of the digits of all the n-digit steady squares in
the base 14 numbering system is 2d8 (582 decimal). Steady squares with
leading 0's are not allowed.

Find the sum of the digits of all the n-digit steady squares in the base
14 numbering system for 1 ≤ n ≤ 10000 (decimal) and give your answer in
the base 14 system using lower case letters where necessary.

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
