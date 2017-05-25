# Project
This repository contains a Galois Field Calculator for GF(2<sup>m</sup>) written in Python. This is a requirement for the subject CS 153: Introduction to Computer Security.

Contains the following files:
1. gf.py
	- Contains all the functions used to perform the operations for Galois field.
2. GFcalcu.py
	- Imports gf.py and contains the code needed to run the interface.

This is based on http://www.ee.unb.ca/cgi-bin/tervo/calc2.pl.

# Instructions

### Installation
Clone the repository.
```git clone https://github.com/jayehernandez/GFCalculator.git```

Run ```python GFcalcu.py```. Note that Python is required to run this program.

### The Program

The user will input A(x), B(x) and an irreducible polynomial P(x). The input polynomials would be entered as decimal coefficients separated by spaces. For example, x<sup>3</sup> + 7x + 6 would be entered as 1 0 7 6.

The user can then choose from these six:
1. A(x) + B(x) - Addition
2. A(x) - B(x) - Subtraction
3. A(x) * B(x) - Multiplication
4. A(x) / B(x) - Division
5. Change values - Modify A(x), B(x), and P(x)
6. Exit 