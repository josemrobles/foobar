#!/usr/bin/python

def answer (s):
		
	# Place the string into a list
	l = [x for x in list(s)]

	for x in l:
		print x

	return l

print answer("<<>><")
