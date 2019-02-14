#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Project Euler Problem 37
=======================

The number 3797 has an interesting property. Being prime itself, it is
possible to continuously remove digits from left to right, and remain
prime at each stage: 3797, 797, 97, and 7. Similarly we can work from
right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left
to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.

"""


def main():
    from common.euler_functions import is_prime

    mem_primes = {'1': False}
    LIMIT = 1000000

    truncatable_primes = []
    num = 10
    while len(truncatable_primes) <= 11 and num < LIMIT:
        trunctable = True
        num_str_left = str(num)
        while len(num_str_left) > 0:
            prime_mem = mem_primes.get(num_str_left)
            if prime_mem == None:
                if not is_prime(int(num_str_left)):
                    trunctable = False
                    mem_primes[num_str_left] = False
                    break
                else:
                    mem_primes[num_str_left] = True
                    num_str_left = num_str_left[1:]
            elif prime_mem == True:
                num_str_left = num_str_left[1:]
            else:
                trunctable = False
                break

        if trunctable:
            num_str_right = str(num)[:-1]
            while len(num_str_right) > 0:
                prime_mem = mem_primes.get(num_str_right)
                if prime_mem == None:
                    if not is_prime(int(num_str_right)):
                        trunctable = False
                        mem_primes[num_str_right] = False
                        break
                    else:
                        mem_primes[num_str_right] = True
                        num_str_right = num_str_right[:-1]
                elif prime_mem:
                    num_str_right = num_str_right[:-1]
                else:
                    trunctable = False
                    break

        if trunctable:
            truncatable_primes.append(num)

        num += 1

    return sum(truncatable_primes)


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
