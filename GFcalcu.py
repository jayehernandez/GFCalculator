#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import os
import gf

while True:
	os.system('cls' if os.name == 'nt' else 'clear')

	print """
	\t╔═╗┌─┐┬  ┌─┐┬┌─┐  ╔═╗┬┌─┐┬  ┌┬┐  ╔═╗┌─┐┬  ┌─┐┬ ┬┬  ┌─┐┌┬┐┌─┐┬─┐
	\t║ ╦├─┤│  │ ││└─┐  ╠╣ │├┤ │   ││  ║  ├─┤│  │  │ ││  ├─┤ │ │ │├┬┘
	\t╚═╝┴ ┴┴─┘└─┘┴└─┘  ╚  ┴└─┘┴─┘─┴┘  ╚═╝┴ ┴┴─┘└─┘└─┘┴─┘┴ ┴ ┴ └─┘┴└─
	"""

	# input validation catches all errors when the polynomial entered is not following the specified format
	while True:
		try:
			Ax = raw_input("\t\t\t\tINPUT A(x): ")
			Ax = [int(x) for x in Ax.split(" ")]
			break
		except ValueError:
			if Ax[len(Ax) - 1] == " ":
				print "\n\tInvalid input. There should be no space at the end.\n"
			else:
				print "\n\tInvalid input. Format must be integers separated by spaces.\n"
	while True:
		try:
			Bx = raw_input("\t\t\t\tINPUT B(x): ")
			Bx = [int(x) for x in Bx.split(" ")]
			break
		except ValueError:
			if Bx[len(Bx) - 1] == " ":
				print "\n\tInvalid input. There should be no space at the end.\n"
			else:
				print "\n\tInvalid input. Format must be integers separated by spaces.\n"
	while True:
		try:
			Px = raw_input("\t\t\t\tINPUT P(x): ")
			Px = [int(x) for x in Px.split(" ")]
			break
		except ValueError:
			if Px[len(Px) - 1] == " ":
				print "\n\tInvalid input. There should be no space at the end.\n"
			else:
				print "\n\tInvalid input. Format must be integers separated by spaces.\n"

	# Test values
	# Ax = [1, 0, 7, 6]
	# Bx = [1, 6, 3]
	# Px = [1, 0, 1, 1]

	iter = 1 # for Galois Field Calcu Display
	while True:
		gf.delLeadZeroes(Ax)
		gf.delLeadZeroes(Bx)
		gf.delLeadZeroes(Px)
		if iter != 1:
			print "\n\t\t\t\t     GALOIS FIELD CALCULATOR",
		iter += 1
		print """
		\t\t--------------------------------
		\t\t\t[1] A(x) + B(x)
		\t\t\t[2] A(x) - B(x)
		\t\t\t[3] A(x) x B(x)
		\t\t\t[4] A(x) / B(x)
		\t\t\t[5] Change Values
		\t\t\t[6] Exit
		\t\t--------------------------------
		"""
		while True:
			try:
				op = input("\t\t\t\tCHOOSE AN OPERATION: ")
				break
			except SyntaxError:
				print "\n\t\t\t\tPlease input a valid choice.\n"

		if op == 1 or op == 2:
			gf.printGiven(Ax, Bx, Px)
			gf.printPoly(gf.addOrSub(Ax, Bx, op, 1))
		elif op == 3:
			gf.printGiven(Ax, Bx, Px)
			gf.printPoly(gf.mul(Ax, Bx, Px, 1))
		elif op == 4:
			gf.printGiven(Ax, Bx, Px)
			quo, rem = gf.div(Ax, Bx, Px, 1)
			gf.printPoly(quo)
			print "\t\t\t\tRemainder = ",
			gf.printPoly(rem)
		elif op == 5:
			break
		elif op == 6:
			print "\n\t\t\t\t\tAu Revoir!\n"
			exit()
		else:
			print "\n\t\t\t\tInvalid choice. Input 1 - 6 only.\n"