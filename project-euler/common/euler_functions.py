import math


def is_prime(i):
    for j in range(2, int(math.sqrt(i)) + 1):
        if i % j == 0:
            return False
    return True


def is_prime_mem(num, primes):
    low_bound = math.sqrt(num)
    for p in primes:
        if num % p == 0:
            return False
        if p > low_bound:
            return True

    return True


def get_primes_distinct(i):
    for j in range(2, int(math.sqrt(i)) + 1):
        if i % j == 0:
            return False
    return True


def get_prime_factors(x, mem={}):
    factors = {}
    remaining = x

    i = 2
    while i <= x / 2:
        if remaining == 1:
            break

        if remaining in mem:
            for k, v in mem[remaining].items():
                factors[k] = factors.get(k, 0) + v
            break

        if remaining % i == 0:
            remaining = remaining / i
            factors[i] = factors.get(i, 0) + 1
        else:
            i += 1

    if len(factors) == 0:
        factors[x] = 1

    return factors


def is_palindrome(num_str):
    return num_str == num_str[::-1]


def is_pandigital(i):
    for j in range(1, len(i) + 1):
        if str(j) not in i:
            return False

    return True


def choose(n, k):
    """
    A fast way to calculate binomial coefficients by Andrew Dalke (contrib).
    """
    if 0 <= k <= n:
        ntok = 1
        ktok = 1
        for t in range(1, min(k, n - k) + 1):
            ntok *= n
            ktok *= t
            n -= 1
        return ntok // ktok
    else:
        return 0