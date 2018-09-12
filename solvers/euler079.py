#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Project Euler Problem 79
=======================

A common security method used for online banking is to ask the user for
three random characters from a passcode. For example, if the passcode was
531278, they may asked for the 2nd, 3rd, and 5th characters; the expected
reply would be: 317.

The text file keylog.txt contains fifty successful login attempts.

Given that the three characters are always asked for in order, analyse the
file so as to determine the shortest possible secret passcode of unknown
length.

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
