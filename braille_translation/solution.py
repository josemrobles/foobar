#!/usr/bin/python

import sys

# Take the first cli argument and assign to 'string' var
plaintext = sys.argv[1]

# Function used to validate the string, < 50 characters including spaces, no numbers.
def validateString(s):
	# Check if the length of the string including spaces is less than fifity characters
	if (len(s) > 50):
		return False,None
	else:
		# Place the string into a list
		l = [x.lower() for x in list(s)]

		b = [' ','a','b','c','d','e','f','g','h','i','j','k','l',
		'm','n','o','p','q','r','s','t','u','v','w','x','y','z']
	
		# Detect any invalid characters using 
		d = (set(l) - set(b))
		if len(d) > 0:
			return False,None
		else:
			return True,l

# Converts a letter to the braille cooresponding output... like a boss
def convert(s):
	x = ''
	d = {' ':'000000','a':'100000','b':'110000','c':'100100','d':'100110',
	'e':'100010','f':'110100','g':'110110','h':'110010','i':'010100',
	'j':'010110','k':'101000','l':'111000','m':'101100','n':'101110',
	'o':'101010','p':'111100','q':'111110','r':'111010','s':'011100',
	't':'011110','u':'101001','v':'111001','w':'010111','x':'101101',
	'y':'101111','z':'101011'}

	if s.isupper():
		x = '000001' + convert(s.lower())
		return x
	else:
		return  d[s]

'''
If the string passes validation as defined in validateString() function, start 
parsing. otherwise output feedback stating why the arg was invalid.
'''
def answer (plaintext):
	r,l = validateString(plaintext)
	if r is True:
		response = []
		for i in l:
			response.append(convert(i))
		resp = ''.join(response)
		return resp

# Convert the string to braille!	
print answer(plaintext)
