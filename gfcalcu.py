def addLeadZeroes(arr, a, b):
	for i in range(a - b):
		arr.insert(0,0)	

def printPoly(arr):
	x = len(arr)
	x = x - 1
	for i in arr:
		if x == 0:
			print str(i)
		elif x == 1:
			print str(i) + "x + ",
			x = x - 1
		else:
			print str(i) + "x^" + str(x) + " + ",
			x = x - 1
	return " "

def addOrSub(a, b):
	if len(a) > len(b):
		addLeadZeroes(b, len(a), len(b))
	elif len(a) < len(b):
		addLeadZeroes(a, len(b), len(a))

	out = []
	for i in range(len(a)):
		out.append(a[i] ^ b[i])
	printPoly(out)

Ax = raw_input("Input A(x): ")
Bx = raw_input("Input B(x): ")
Px = raw_input("Input P(x): ")

Ax = [int(x) for x in Ax.split(" ")]
Bx = [int(x) for x in Bx.split(" ")]

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

if op == 1 or op == 2:
	addOrSub(Ax, Bx)
