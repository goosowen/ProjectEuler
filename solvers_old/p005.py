'''
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''

pruned_divisors = range(20, 1, -1)
divisors = range(20, 1, -1)
for d in divisors:
    for other_d in divisors:
        if d < other_d and other_d % d == 0:
            pruned_divisors.remove(d)
            break

print pruned_divisors

n = 1
for d in pruned_divisors:
    n *= d


# completely brute force, takes awhile
def our_num():
    for possible_num in xrange(20, n + 1):
        passable = True
        for divisor in pruned_divisors:
            if possible_num % divisor != 0:
                passable = False
                break

        if passable:
            return possible_num

    return "hah"


print our_num()
