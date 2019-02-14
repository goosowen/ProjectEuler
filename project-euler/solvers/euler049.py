#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Project Euler Problem 49
=======================

The arithmetic sequence, 1487, 4817, 8147, in which each of the terms
increases by 3330, is unusual in two ways: (i) each of the three terms are
prime, and, (ii) each of the 4-digit numbers are permutations of one
another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit
primes, exhibiting this property, but there is one other 4-digit
increasing sequence.

What 12-digit number do you form by concatenating the three terms in this
sequence?
"""


# TODO optimize
def main():
    from common.euler_functions import is_prime

    def get_all_four_digit_primes():
        s = []
        for i in range(1000, 10001):
            if is_prime(i):
                s.append(i)

        return s

    primes = get_all_four_digit_primes()
    permutations_dict = {}
    for p in primes:
        p_str = str(p)
        digits = []
        for c in p_str:
            digits.append(int(c))
        digits.sort()
        p_perm = ''.join(str(d) for d in digits)
        permutations_dict[p_perm] = permutations_dict.get(p_perm, [])
        permutations_dict[p_perm].append(p)

        if len(permutations_dict[p_perm]) >= 3:

            # TODO doesn't quite capture all cases.
            # Needs to check the diffs between all the permutations, not just the latest consecutive ones.
            if permutations_dict[p_perm][-1] - permutations_dict[p_perm][-2] == permutations_dict[p_perm][-2] - \
                    permutations_dict[p_perm][-3]:
                answer = ''
                answer += str(permutations_dict[p_perm][-3])
                answer += str(permutations_dict[p_perm][-2])
                answer += str(permutations_dict[p_perm][-1])
                return answer


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
