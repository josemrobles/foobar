#!/usr/bin/python

def validateInput(s):
	if ( 1 <= len(s) <= 100):
		return True
	else:
		print len(s)
		return False

def calcLeft(d):
	count = 0
	for r1 in d['right']:
		for l1 in d['left']:
			if r1 > l1:
				count += 1
	return count

def calcRight(d):
	count = 0
	for r1 in d['right']:
		for l1 in d['left']:
			if r1 > l1:
				count += 1
	return count

def answer (s):
	
	if validateInput(s) is True:		
		l = list(s)
		a = [i for i in l if i in ["<",">"]]
		d = {'right': [], 'left': []}

		for x in a:
			if x == ">":
				d['right'].append(x)

			if x == "<":
				d['left'].append(x)			

		return calcLeft(d) + calcRight(d)

print answer("<<>><")
#print answer("--->-><-><-->-")
