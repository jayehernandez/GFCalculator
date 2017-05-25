#!/usr/bin/env python
# -*- coding: utf-8 -*- 

def addLeadZeroes(arr, a):
	for x in range(a - len(arr)):
		arr.insert(0,0)	

def delLeadZeroes(arr):
	while (arr[0] == 0 and len(arr) != 1):
		arr.remove(0)

def addEndZeroes(arr, a):
	for x in range(a - len(arr)):
		arr.append(0)

# Given an array, prints into a readable polynomial equation form
def printPoly(arr):
	x = len(arr)
	x = x - 1
	for i in arr:
		if i == 0: # if term is 0, don't print
			x -= 1 
		elif x == 0: # if last term, constant
			print str(i)
		elif x == 1: # if x^1, just change to x
			if i == 1:
				print "x + ",
			else:
				print str(i) + "x + ",
			x -= 1
		else: 
			if i == 1:
				print "x^" + str(x) + " + ",
			else:
				print str(i) + "x^" + str(x) + " + ",
			x -= 1
	return " "

# Printing the polynomials the user inputs calls on the function printPoly
def printGiven(a, b, p):
	print "\n\t\t\t\t\tGIVEN EQUATIONS"
	print "\n\t\t\t\tA(x) = ", printPoly(a)
	print "\t\t\t\tB(x) = ", printPoly(b)
	print "\t\t\t\tP(x) = ", printPoly(p)

# Addition or subtraction with detailed computation
def addOrSub(a, b, op=0, pr=0):
	if pr:
		if op == 1:
			print "\t\t\t\t\tSOLUTION FOR ADDITION\n"
		elif op == 2:
			print "\t\t\t\t\tSOLUTION FOR SUBTRACTION\n"
	if len(a) > len(b):
		addLeadZeroes(b, len(a))
		if pr:
			print "\t\tWe first add lead zeroes to B(x) so that their lengths would match."
	elif len(a) < len(b):
		addLeadZeroes(a, len(b))
		if pr:
			print "\t\tWe first add lead zeroes to A(x) so that their lengths would match."
	if pr:	
		print "\n\t\tTo get the answer, we simply do an XOR (⊕) for each term."
		print "\n\t\t\t\t\t" + "   ".join(str(x) for x in a)
		print "\t\t\t\t⊕\t" + "   ".join(str(x) for x in b)
		print "\t\t\t\t---------------------------"
	out = []
	for i in range(len(a)):
		out.append(a[i] ^ b[i]) # xor each
	if pr:
		print "\t\t\t\t\t" + "   ".join(str(x) for x in out)
		print "\n\n\t\t\t\t\tFINAL ANSWER"
		if op == 1:
			print "\t\t\t\tA(x) + B(x) = ",
		elif op == 2:
			print "\t\t\t\tA(x) - B(x) = ",
	return out	

# Multiply two decimals, change them to binary first
def binMul(a, b, p, pr=0):
	a = [int(x) for x in bin(a)[2:]]
	b = [int(x) for x in bin(b)[2:]]
	out = []
	# Multiply binary numbers
	for x in range(len(b)-1, -1, -1):
		toAdd = []
		for y in range(len(a)):
			toAdd.append(a[y]*b[x]) # add to a row	
		for y in range((len(b)-1)-x):
			toAdd.append(0) # add zeroes at the back
		addLeadZeroes(out, len(toAdd))
		out = addOrSub(out, toAdd) # xor, current product
	delLeadZeroes(out) 
	# Need to mod p if > m - 1
	p1 = list(p) # make a copy of P(x), so that P(x) will not be manipulated
	while(len(out) > len(p1)-1):
		addEndZeroes(p1, len(out)) # add zeroes before xor to p(x)
		out = addOrSub(out, p1) # xor
		delLeadZeroes(out) 
	return int(''.join(map(str,out)),2)

# Main multiplication function
def mul(a, b, p, pr=0):
	if pr:	
		print "\t\t\t\t\tSOLUTION FOR MULTIPLICATION"
		if len(a) > len(b):
			y = len(a) - len(b)
			z = 0
		elif len(a) < len(b):
			y = 0
			z = len(b) - len(a)
		print "\n\t\t\t\t\t" + "    "*z + "   ".join(str(x) for x in a)
		print "\t\t\t\t*\t" + "    "*y + "   ".join(str(x) for x in b)
		print "\t\t\t\t---------------------------"
		space = len(b)-1
	
	out = []
	for x in range(len(b)-1, -1, -1):
		toAdd = []
		# Multiplies each in binary then mod P(x) if necessary
		for y in range(len(a)):
			toAdd.append(binMul(a[y],b[x],p)) # append each after binMult
		for y in range((len(b)-1)-x):
			toAdd.append(0)
		addLeadZeroes(out, len(toAdd))
		out = addOrSub(out, toAdd) # xor na agad
		if pr:
			print "\t\t\t\t" + "    "*space +"   ".join(str(x) for x in toAdd)
			space -= 1
	delLeadZeroes(out)
	if pr:
		print "\t\t\t\t---------------------------"
		print "\t\t\t\t" + "   ".join(str(x) for x in out)
		print "\n\n\t\t\t\t\tFINAL ANSWER"
		print "\t\t\t\tA(x) x B(x) = ",
	return out

def div(a, b, p, pr=0):
	if pr:	
		print "\t\t\t\t\tSOLUTION FOR DIVISION"
		print "\t\t\t\t" + "    "*(len(b)) + "_________________________"
		print "\t\t\t\t" + "   ".join(str(x) for x in b) + "  / \t" + "   ".join(str(x) for x in a)

	out = []
	dividend = int(''.join(map(str,a)))
	divisor = int(''.join(map(str,b)))
	space = 0
	while (len(a) > len(b)-1):
		x = a[0]/b[0]
		out.append(x)
		prod = mul(b, [x], p) # multiply x to the divisor
		addEndZeroes(prod, len(a))
		a = addOrSub(a, prod) # xor product to the current dividend
		delLeadZeroes(a)
		dividend = int(''.join(map(str,a)))
		divisor = int(''.join(map(str,b)))
		if pr:
			if space != 0:
				print "\n",
			print "\t\t\t\t\t\t" + "    "*space + "   ".join(str(x) for x in prod) + "\t = B * " + str(x) + " * x^" + str(len(prod)-len(b))
			print "\t\t\t\t\t---------------------------"
			space += 1
			print "\t\t\t\t\t\t" +  "    "*space + "   ".join(str(x) for x in a),
	if pr:
		print "\n\n\t\t\t\t\tFINAL ANSWER"
		print "\t\t\t\tA(x) / B(x) = ",
	return out, a