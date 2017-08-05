#!/usr/bin/python

foo = [1, 2, 3, 4, 5, 6]
#foo = [1,1,1]

def answer(l):
	if len(l) < 3:
		return 0
	else:
		i = 0
		c = 0
		j = 0
		ln = len(l)

		while i < ln:
			while j+1 < ln:
				if l[i]%l[j] == 0:
					c += 1
			i += 1

		return c


print answer(foo)
