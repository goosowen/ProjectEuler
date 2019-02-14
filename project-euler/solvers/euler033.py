#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Project Euler Problem 33
=======================

The fraction 49/98 is a curious fraction, as an inexperienced
mathematician in attempting to simplify it may incorrectly believe that
49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less
than one in value, and containing two digits in the numerator and
denominator.

If the product of these four fractions is given in its lowest common
terms, find the value of the denominator.

"""


def main():
    from fractions import Fraction

    def get_two_digit_curious_fractions():
        curious_fractions = []
        for numerator in range(10, 100):
            num_str = str(numerator)
            for denominator in range(numerator + 1, 100):
                den_str = str(denominator)
                actual_decimal = float(numerator) / denominator
                if is_curious(num_str, den_str, actual_decimal):
                    curious_fractions.append((num_str, den_str))

        return curious_fractions

    # def simplify_fraction(numerator, denominator):

    def is_curious(num_str, den_str, actual_decimal):
        if den_str[1] != '0':
            if num_str[0] == den_str[0]:
                cancel_decimal = float(num_str[1]) / float(den_str[1])
                if cancel_decimal == actual_decimal:
                    return True

            if num_str[1] == den_str[0]:
                cancel_decimal = float(num_str[0]) / float(den_str[1])
                if cancel_decimal == actual_decimal:
                    return True

        if num_str[1] != '0' and num_str[1] == den_str[1]:
            cancel_decimal = float(num_str[0]) / float(den_str[0])
            if cancel_decimal == actual_decimal:
                return True

        if num_str[0] == den_str[1]:
            cancel_decimal = float(num_str[1]) / float(den_str[0])
            if cancel_decimal == actual_decimal:
                return True

        return False

    curious_fractions = get_two_digit_curious_fractions()
    numerator = 1
    denominator = 1
    for frac in curious_fractions:
        numerator *= int(frac[0])
        denominator *= int(frac[1])

    return Fraction(numerator, denominator).denominator


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
