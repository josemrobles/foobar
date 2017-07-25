#!/usr/bin/python

def validateInput(s):
	if ( 1 <= len(s) <= 100):
		return True
	else:
		print len(s)
		return False

def calcLeft(a):
	count = 0
	for k,v in enumerate(a):
		if v == ">":
			for k_,v_ in enumerate(a):
				if (k_ > k and v_ == "<"):
					count += 1
	return count

def calcRight(a):
	count = 0
	for k,v in enumerate(a):
		if v == "<":
			for k_,v_ in enumerate(a):
				if (k_ < k and v_ == ">"):
					count += 1
	return count

def answer (s):
	
	if validateInput(s) is True:		
		l = list(s)
		a = [i for i in l if i in ["<",">"]]

		return calcLeft(a) + calcRight(a)
