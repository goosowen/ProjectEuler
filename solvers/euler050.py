#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Project Euler Problem 50
=======================

The prime 41, can be written as the sum of six consecutive primes:

                       41 = 2 + 3 + 5 + 7 + 11 + 13

This is the longest sum of consecutive primes that adds to a prime below
one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a
prime, contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most
consecutive primes?

"""


# TODO lazy initialization of primes for runner
# TODO this is algorithmically way too slow. Need a better subproblem/approach.
def main():
    from common.euler_functions import is_prime_mem

    max_consecutive = 0
    best_consecutive = []
    best_num = 0

    limit = 10**6

    primes = [2]
    for i in range(3, limit, 2):
        if is_prime_mem(i, primes):
            primes.append(i)

    print(len(primes))

    # def get_consecutives(i, j, consecutives, primes):
    #     if i == j:
    #         return primes[i]
    #
    #     return get_consecutives()

    consecutives = {}
    for i in range(len(primes)):
        for j in range(i, len(primes)):
            if i == j:
                consecutives[(i, j)] = primes[j]
            else:
                consecutives[(i, j)] = consecutives[(i, j-1)] + primes[j]

            if consecutives[(i, j)] in primes and j-i+1 > max_consecutive:
                max_consecutive = j-i+1
                best_consecutive = primes[i:j+1]
                best_num = consecutives[(i, j)]
                print(best_num, max_consecutive, best_consecutive)
                assert best_num == sum(best_consecutive)

            if consecutives[(i, j)] > limit:
                break

    print(best_num, max_consecutive, best_consecutive)
    return best_num


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
