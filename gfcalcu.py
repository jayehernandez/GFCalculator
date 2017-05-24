def addLeadZeroes(arr, a):
	for x in range(a - len(arr)):
		arr.insert(0,0)	

def delLeadZeroes(arr):
	while (arr[0] == 0 and len(arr) != 1):
		arr.remove(0)

def addEndZeroes(arr, a):
	for x in range(a - len(arr)):
		arr.append(0)

def printPoly(arr):
	x = len(arr)
	x = x - 1
	for i in arr:
		if i == 0:
			x -= 1 
		elif x == 0:
			print str(i)
		elif x == 1:
			print str(i) + "x + ",
			x -= 1
		else:
			print str(i) + "x^" + str(x) + " + ",
			x -= 1
	return " "

def addOrSub(a, b):
	if len(a) > len(b):
		addLeadZeroes(b, len(a))
	elif len(a) < len(b):
		addLeadZeroes(a, len(b))
	out = []
	for i in range(len(a)):
		out.append(a[i] ^ b[i])
	return out

def binMul(a, b, p):
	a = [int(x) for x in bin(a)[2:]]
	b = [int(x) for x in bin(b)[2:]]

	out = []
	for x in range(len(b)-1, -1, -1):
		toAdd = []
		for y in range(len(a)):
			toAdd.append(a[y]*b[x])
		for y in range((len(b)-1)-x):
			toAdd.append(0)
		addLeadZeroes(out, len(toAdd))
		out = addOrSub(out, toAdd)
	delLeadZeroes(out)
	# need to mod p if > m - 1
	p1 = list(p)
	while(len(out) > len(p1)-1):
		addEndZeroes(p1, len(out))
		out = addOrSub(out, p1)
		delLeadZeroes(out)
	return int(''.join(map(str,out)),2)

def mul(a, b, p):
	out = []
	for x in range(len(b)-1, -1, -1):
		toAdd = []
		for y in range(len(a)):
			toAdd.append(binMul(a[y],b[x],p))
		for y in range((len(b)-1)-x):
			toAdd.append(0) # append sa dulo
		addLeadZeroes(out, len(toAdd))
		out = addOrSub(out, toAdd)
	delLeadZeroes(out)
	return out

def div(a, b, p):
	out = []
	dividend = int(''.join(map(str,a)))
	divisor = int(''.join(map(str,b)))
	while (dividend > divisor):
		x = a[0]/b[0]
		out.append(x)
		prod = mul(b, [x], p)
		addEndZeroes(prod, len(a))
		a = addOrSub(a, prod)
		delLeadZeroes(a)
		dividend = int(''.join(map(str,a)))
		divisor = int(''.join(map(str,b)))
	return out, a

Ax = raw_input("Input A(x): ")
Bx = raw_input("Input B(x): ")
Px = raw_input("Input P(x): ")

Ax = [int(x) for x in Ax.split(" ")]
Bx = [int(x) for x in Bx.split(" ")]
Px = [int(x) for x in Px.split(" ")]

print """
Four operations that could be done:
1. A(x) + B(x)
2. A(x) - B(x)
3. A(x) x B(x)
4. A(x) / B(x)
"""

op = input("Pick an operation to perform (Input 1, 2, 3, or 4): ")

# printing
print "A(x): ", printPoly(Ax)
print "B(x): ", printPoly(Bx)
print "P(x): ", printPoly(Px)

if op == 1 or op == 2:
	printPoly(addOrSub(Ax, Bx))
elif op == 3:
	printPoly(mul(Ax, Bx, Px))
elif op == 4:
	quo, rem = div(Ax, Bx, Px)
	printPoly(quo)
	printPoly(rem)