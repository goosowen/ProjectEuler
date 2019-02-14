#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Project Euler Problem 35
=======================

The number, 197, is called a circular prime because all rotations of the
digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37,
71, 73, 79, and 97.

How many circular primes are there below one million?

"""


# TODO use lazy prime initialization with runner
def main():
    from common.euler_functions import is_prime

    LIMIT = 1000000

    circular_primes = []
    for num in range(2, LIMIT):
        num_rotations = 0
        num_str = str(num)
        circular_prime = True
        while num_rotations < len(num_str):
            if not is_prime(int(num_str)):
                circular_prime = False
                break
            else:
                num_rotations += 1
                num_str = num_str[1:] + num_str[:1]

        if circular_prime:
            circular_primes.append(num)

    return len(circular_primes)


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
