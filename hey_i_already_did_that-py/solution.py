#!/usr/bin/python

def dToBase (n,b):
    if n == 0:
        return '0'
    numbers = []
    while n:
        n, r = divmod(n, b)
        numbers.append(str(r))
    return ''.join(reversed(numbers))

def bToDecimal(bn,cb):
  n = 0
  for d in str(bn):
    n = cb * n + int(d)
  return n

def subtract(x,y,b):
  if b==10:
    return int(x) - int(y)
  else:
    dx=bToDecimal(x,b)
    dy=bToDecimal(y,b)
    dz=dx-dy
    return dToBase(dz,b)

def answer(n,b):
    foo=[]
    while True:
        x = "".join(sorted(str(n), reverse=True))
        y = "".join(sorted(str(n)))
        z = subtract(x,y,b)

        _z = len(str(z))
        _x = len(str(x))

        if (_z) != _x:
            z = z * pow(10 ,(_x-_z)) 

        for index, item in enumerate(foo):
          if item == z:
            return index + 1
            break
        foo = [z] + foo
        n = z

print answer("1211",10)
