import operator

def validateInput(s):
	if ( 1 <= len(s) <= 100):
		return True
	else:
		print len(s)
		return False

def calcSalutes(a,b,r):
	count = 0
	for k,v in enumerate(a):
		if v == b:
			for k_,v_ in enumerate(a):
				if (r(k_, k) and v_ == flip(b)):
					count += 1
	return count

def flip(s):
	if s == ">":
		return "<"
	else:
		return ">"

def answer (s):
	if validateInput(s) is True:		
		l = list(s)
		a = [i for i in l if i in ["<",">"]]

		return calcSalutes(a,"<",operator.lt) + calcSalutes(a,">",operator.gt)

print answer("--->-><-><-->-")
