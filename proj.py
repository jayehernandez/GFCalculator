def printPoly(arr):
	x = len(arr)
	x = x - 1
	for i in arr:
		if x == 0:
			print str(i)
		else:
			print str(i) + "x^" + str(x) + " + ",
			x = x - 1
	return " "

Ax = raw_input("Input A(x): ")
Bx = raw_input("Input B(x): ")
# Px = raw_input("Input P(x): ")

Ax = Ax.split(" ")
Bx = Bx.split(" ")

# printing
print "A(x): ", printPoly(Ax)
print "B(x): ", printPoly(Bx)

# for i in range(max(len(Ax), len(Bx))):
	# print Ax[i]
	# print Bx[i]