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

		#for x in a:
		#	print x

		return a

print answer("<<>><")
