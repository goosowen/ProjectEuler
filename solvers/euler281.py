#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Project Euler Problem 281
=======================

You are given a pizza (perfect circle) that has been cut into m·n equal
pieces and you want to have exactly one topping on each slice.

Let f(m,n) denote the number of ways you can have toppings on the pizza
with m different toppings (m ≥ 2), using each topping on exactly n slices
(n ≥ 1). Reflections are considered distinct, rotations are not.

Thus, for instance, f(2,1) = 1, f(2,2) = f(3,1) = 2 and f(3,2) = 16.
f(3,2) is shown below:

[Image: 281_pizza.gif]

Find the sum of all f(m,n) such that f(m,n) ≤ 10^15.

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
