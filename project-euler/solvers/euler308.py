#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Project Euler Problem 308
=======================

A program written in the programming language Fractran consists of a list
of fractions.

The internal state of the Fractran Virtual Machine is a positive integer,
which is initially set to a seed value. Each iteration of a Fractran
program multiplies the state integer by the first fraction in the list
which will leave it an integer.

For example, one of the Fractran programs that John Horton Conway wrote
for prime-generation consists of the following 14 fractions:

17 , 78 , 19 , 23 , 29 , 77 , 95 , 77 , 1  , 11 , 13 , 15 , 1 , 55 .
91   85   51   38   33   29   23   19   17   13   11   2    7   1

Starting with the seed integer 2, successive iterations of the program
produce the sequence:
15, 825, 725, 1925, 2275, 425, ..., 68, 4, 30, ..., 136, 8, 60, ..., 544,
32, 240, ...

The powers of 2 that appear in this sequence are 2^2, 2^3, 2^5, ...
It can be shown that all the powers of 2 in this sequence have prime
exponents and that all the primes appear as exponents of powers of 2, in
proper order!

If someone uses the above Fractran program to solve Project Euler Problem
7 (find the 10001^st prime), how many iterations would be needed until the
program produces 2^10001st prime?

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
