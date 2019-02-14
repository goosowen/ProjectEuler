#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Project Euler Problem 12
=======================

The sequence of triangle numbers is generated by adding the natural
numbers. So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 =
28. The first ten terms would be:

                 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

Let us list the factors of the first seven triangle numbers:

   1: 1
   3: 1,3
   6: 1,2,3,6
  10: 1,2,5,10
  15: 1,3,5,15
  21: 1,3,7,21
  28: 1,2,4,7,14,28

We can see that 28 is the first triangle number to have over five
divisors.

What is the value of the first triangle number to have over five hundred
divisors?

"""


# pure brute force method
def main():
    import math

    DIVISORS = 500

    def find_num(limit):
        tot = 0

        for i in range(1, limit):
            tot += i

            num_divisors = 1
            for d in range(int(math.sqrt(tot)), 1, -1):
                if tot % d == 0:
                    num_divisors += 1

            if num_divisors * 2 >= DIVISORS:
                tot, num_divisors * 2
                return tot

        # mem[tot] = divisor_list

        return "limit not big enough"

    return find_num(50000)


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