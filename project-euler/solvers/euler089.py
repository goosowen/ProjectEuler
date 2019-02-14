#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Project Euler Problem 89
=======================

The rules for writing Roman numerals allow for many ways of writing each
number. However, there is always a "best" way of writing a particular number.

For example, the following represent all of the legitimate ways of writing
the number sixteen:

IIIIIIIIIIIIIIII
VIIIIIIIIIII
VVIIIIII
XIIIIII
VVVI
XVI

The last example being considered the most efficient, as it uses the least
number of numerals.

The 11K text file roman.txt contains one thousand numbers written in valid,
but not necessarily minimal, Roman numerals; that is, they are arranged in
descending units and obey the subtractive pair rule (see FAQ for the
definitive rules for this problem).

Find the number of characters saved by writing each of these in their
minimal form.

Note: You can assume that all the Roman numerals in the file contain no
more than four consecutive identical units.

FAQ Link: http://projecteuler.net/about=roman_numerals

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
