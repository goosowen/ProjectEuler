import time   
import math

letter_to_score = {"A":1, "B":2, "C":3, "D":4, "E":5, "F":6, "G":7, "H":8, "I":9, "J":10, "K":11,
    "L":12, "M":13, "N":14, "O":15, "P":16, "Q":17, "R":18, "S":19, "T":20, "U":21, "V":22, "W":23,
    "X":24, "Y":25, "Z":26}

def timeit(method):

    def timed(*args, **kw):
        ts = time.time()
        result = method(*args, **kw)
        te = time.time()

        print '%r (%r, %r) %2.2f sec' % \
              (method.__name__, args, kw, te-ts)
        return result

    return timed

def is_prime(i):
	for j in xrange(2,int(math.sqrt(i))+1):
		if i % j == 0:
			return False
	return True

def is_palindrome(num_str):
	return num_str == num_str[::-1]

def is_pandigital(num, length_check=False):
    for j in xrange(1,len(i)+1):
        if str(j) not in i:
            return False

    return True