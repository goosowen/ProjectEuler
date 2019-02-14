#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Project Euler Problem 236
=======================

Suppliers 'A' and 'B' provided the following numbers of products for the
luxury hamper market:

                         Product       'A'  'B'
                    Beluga Caviar      5248 640
                    Christmas Cake     1312 1888
                    Gammon Joint       2624 3776
                    Vintage Port       5760 3776
                    Champagne Truffles 3936 5664

Although the suppliers try very hard to ship their goods in perfect
condition, there is inevitably some spoilage - i.e. products gone bad.

The suppliers compare their performance using two types of statistic:

 • The five per-product spoilage rates for each supplier are equal to the
   number of products gone bad divided by the number of products
   supplied, for each of the five products in turn.
 • The overall spoilage rate for each supplier is equal to the total
   number of products gone bad divided by the total number of products
   provided by that supplier.

To their surprise, the suppliers found that each of the five per-product
spoilage rates was worse (higher) for 'B' than for 'A' by the same factor
(ratio of spoilage rates), m>1; and yet, paradoxically, the overall
spoilage rate was worse for 'A' than for 'B', also by a factor of m.

There are thirty-five m>1 for which this surprising result could have
occurred, the smallest of which is 1476/1475.

What's the largest possible value of m?
Give your answer as a fraction reduced to its lowest terms, in the form
u/v.

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
