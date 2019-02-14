#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Project Euler Problem 43
=======================

The number, 1406357289, is a 0 to 9 pandigital number because it is made
up of each of the digits 0 to 9 in some order, but it also has a rather
interesting sub-string divisibility property.

Let d[1] be the 1st digit, d[2] be the 2nd digit, and so on. In this
way, we note the following:

  * d[2]d[3]d[4]=406 is divisible by 2
  * d[3]d[4]d[5]=063 is divisible by 3
  * d[4]d[5]d[6]=635 is divisible by 5
  * d[5]d[6]d[7]=357 is divisible by 7
  * d[6]d[7]d[8]=572 is divisible by 11
  * d[7]d[8]d[9]=728 is divisible by 13
  * d[8]d[9]d[10]=289 is divisible by 17

Find the sum of all 0 to 9 pandigital numbers with this property.

"""


def main():
    from itertools import permutations

    DIGITS = ''.join(str(d) for d in range(10))
    DIVISOR_LIST = [2, 3, 5, 7, 11, 13, 17]

    def follows_property(num_str):
        for start_d in range(1, 8):
            num_sub = int(num_str[start_d:start_d + 3])
            if num_sub % DIVISOR_LIST[start_d - 1] != 0:
                return False

        return True

    # TESTING
    # print is_pandigital("1234567890")
    # print is_pandigital("1234567899")
    # print follows_property("1406357289")

    pandigitals = [''.join(p) for p in permutations(DIGITS)]
    tot = 0
    for num_str in pandigitals:
        if follows_property(num_str):
            tot += int(num_str)

    return tot


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
