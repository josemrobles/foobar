#!/usr/bin/python

def answer (s):
		
	l = list(s)
	#a = [i for i in l if i is not "-"]
	a_ = [i for i in l if i in ["<",">"]]

	print l

	for x in l:
		print x

	return a_

print answer("<<->><000")
