'''
The sum of the squares of the first ten natural numbers is,

1^2 + 2^2 + ... + 10^2 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)^2 = 55^2 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 - 385 = 2640.
Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
'''
NUMBER = 100


def sum_of_squares(n):
    total = 0
    for i in xrange(1, n + 1):
        total += i ** 2
    return total


def square_of_sum(n):
    return (n * (n + 1) / 2) ** 2


print square_of_sum(NUMBER) - sum_of_squares(NUMBER)
