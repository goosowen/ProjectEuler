#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Project Euler Problem 51
=======================

By replacing the 1st digit of *57, it turns out that six of the possible
values: 157, 257, 457, 557, 757, and 857, are all prime.

By replacing the 3rd and 4th digits of 56**3 with the same digit, this
5-digit number is the first example having seven primes, yielding the
family: 56003, 56113, 56333, 56443, 56663, 56773, and 56993. Consequently
56003, being the first member of this family, is the smallest prime with
this property.

Find the smallest prime which, by replacing part of the number (not
necessarily adjacent digits) with the same digit, is part of an eight
prime value family.

"""


def main():
    import itertools
    from common.euler_functions import is_prime_mem

    def get_masks(digit_length):
        return [''.join(x) for x in itertools.product(['d', '*'], repeat=digit_length)]

    largest_prime_fam_len = 2
    largest_prime_fam = set()
    largest_prime_fam_mask = 0
    largest_prime_fam_min_digit = 0

    primes = set([2])

    for digit_length in range(1, 4):
        masks = get_masks(digit_length)
        current_primes = set()

        start = 10**(digit_length-1) + 1
        if start == 2:
            start = 3
        end = 10**digit_length

        for i in range(start, end, 2):
            if is_prime_mem(i, primes):
                primes.add(i)
                current_primes.add(i)

        if digit_length > 2:
            for p in current_primes:
                p_str = str(p)
                for m in masks:
                    candidates = set()
                    for d in range(10):
                        str_d = str(d)
                        candidate = ""
                        for i in range(digit_length):
                            if m[i] == '*':
                                candidate += str_d
                            else:
                                candidate += p_str[i]

                        candidates.add(int(candidate))

                    # use current primes to remove numbers starting with 0 (that aren't actually the same digit length).
                    prime_candidates = set.intersection(candidates, current_primes)

                    if len(prime_candidates) > largest_prime_fam_len:
                        largest_prime_fam_len = len(prime_candidates)
                        largest_prime_fam_min_digit = min(prime_candidates)
                        largest_prime_fam_mask = m
                        largest_prime_fam = prime_candidates

                        print()
                        print(largest_prime_fam)
                        print(largest_prime_fam_min_digit)
                        print(largest_prime_fam_mask)
                        print(largest_prime_fam_len)

                        if largest_prime_fam_len == 8:
                            print()
                            print(current_primes)
                            return largest_prime_fam_min_digit


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
