#!/usr/bin/python

def validateInput(s):
	if ( 1 <= len(s) <= 100):
		return True
	else:
		print len(s)
		return False

def answer (s):
	
	if validateInput(s) is True:		
		l = list(s)
		a = [i for i in l if i in ["<",">"]]
		rl = {'right': [], 'left': []}

		for x in a:
			if x == ">":
				rl['right'].append(x)

			if x == "<":
				rl['left'].append(x)			

		return rl

print answer("<<>><")
print answer("--->-><-><-->-")
