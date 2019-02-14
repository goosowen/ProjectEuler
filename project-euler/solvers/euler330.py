#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Project Euler Problem 330
=======================

An infinite sequence of real numbers a(n) is defined for all integers n as
follows:

[Image: 330_formula.gif]

For example,

        1     1     1
a(0) = --- + --- + --- + ... = e - 1
        1!    2!    3!

       e − 1    1     1
a(1) = ----- + --- + --- + ... = 2e - 3
         1!     2!    3!

       2e − 3   e − 1    1          7
a(2) = ------ + ----- + --- + ... = - e - 6
         1!       2!     3!         2

with e = 2.7182818... being Euler's constant.

It can be shown that a(n) is of the form:

A(n) e + B(n)
-------------
      n!

for integers A(n) and B(n).

For example:

        328161643e − 652694486
a(10) = ----------------------
                  10!

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
