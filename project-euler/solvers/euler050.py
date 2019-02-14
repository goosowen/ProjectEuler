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

    max_seq_length = 0
    best_seq = []
    best_num = 0

    limit = 10**6

    primes = [2]
    for i in range(3, limit, 2):
        if is_prime_mem(i, primes):
            primes.append(i)

    for i in range(len(primes)):
        tot_at_i = 0
        for j in range(i, len(primes)):
            tot_at_i += primes[j]

            if tot_at_i > limit:
                break

            seq_length = j - i + 1
            if seq_length > max_seq_length and tot_at_i in primes:
                max_seq_length = seq_length
                best_seq = primes[i:j + 1]
                best_num = tot_at_i
                # print(best_num, max_seq_length, best_seq)

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
