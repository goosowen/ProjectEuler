'''
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
'''

THRESHOLD = 1000

def get_sum_multiples(x):
	num_multiples_of_x = (THRESHOLD-1) / x 
	sum_multiples_of_x = x * (num_multiples_of_x + 1) * (num_multiples_of_x) / 2.0
	return sum_multiples_of_x

#print get_sum_multiples(3)
print get_sum_multiples(3) + get_sum_multiples(5) - get_sum_multiples(15)
x = [1,2,3]