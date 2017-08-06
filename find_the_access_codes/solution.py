#!/usr/bin/python
from collections import Counter
from itertools import combinations

foo = [1, 2, 3, 4, 5, 6]
bar = [1,1,1]
meh = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

def answer(l):
    count = 0
    size = len(l)
    if size < 3: return 0

    cache = [0] * size
    for x in xrange(size):
        for y in xrange(x + 1, size):
            if l[y] % l[x] == 0:
                cache[y] += 1
                count += cache[x]

    return count



def validateInput(l):

	if len(l) < 3 or len(l) > 2000:
		return False
	else:
		for el in l:
			if el < 0 or el > 999999:
				return False
				break

def _answer(l):
	if validateInput(l) is False:
		return 0
	else:
		c = Counter(l)
		d = Counter()
		m = Counter()
		for x, y in combinations(sorted(c), 2):
			if y % x == 0:
				d[y] += 1
				m[x] += 1
		result = 0
		for x, n in c.items():
			result += d[x] * m[x]
			if n >= 2:
				result += d[x] + m[x]
				if n >= 3:
					result += 1

		if not(int(result)>>32) is True:
			return result
		else:
			return 0
print answer(foo)
print answer(bar)
print answer(meh)
