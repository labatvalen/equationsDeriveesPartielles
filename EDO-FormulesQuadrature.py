#!/usr/bin/python
#-*- coding: Utf-8 -*-

from math import cos, exp, pi, log
from scipy.integrate import quad
import math
from matplotlib.pyplot import *

# FORMULES
def rectangles(f, a, b, n):
	return sum(f(a+k*(b-a)/float(n)) for k in range(n))*(b-a)/n

def trapezes(f, a, b, n):
	return rectangles(f, a, b, n) + (f(b)-f(a))*float((b-a))/(2*n)

def simpson(f, a, b, n):
	return trapezes(f, a, b, n)/3 + \
        2*sum(f(a+(b-a)*(2*k+1)/(2.*n)) for k in range(n))*float((b-a))/(3*n)


# DEFINITION DES 4 FONCTIONS
def f1(x):
	return x
def f2(x):
	return x**10
f3 = cos
f4 = exp


# BORNES INF-SUP DES 4 FONCTIONS
a = [0, 0, 0, -3]
b = [1, 1, pi/2, 3]

# CALCULS
for k in range(4):
                  f = [f1, f2, f3, f4][k]
	print("****** Pour f%i *******"%(1+k))
	# AFFICHAGE TABLEAU
	for n in [10, 10**3, 10**5]:
		print("n=%i\tApprox=%.10f"%(n,rectangles(f, a[k], b[k], n)))
	print("Approximation de scipy.integrate.quad : %.10f"%quad(f, a[k], b[k])[0])

	for n in [1, 3, 5]:
		print("n=10**%i\tApprox[trapezes]=%.10f"%(n,trapezes(f, a[k], b[k], 10**n)))
	print("Approximation de scipy.integrate.quad : %.10f"%quad(f, a[k], b[k])[0])
	
	for n in [1, 3, 5]:
		print("n=10**%i\tApprox[paraboles]=%.15f"%(n,simpson(f, a[k], b[k], 10**n)))
	print("Approximation de scipy.integrate.quad : %.15f"%quad(f, a[k], b[k])[0])
