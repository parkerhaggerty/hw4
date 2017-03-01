# Author: Parker Haggerty
# Date: 2/27/17
# Assignment 4, Problem 2


# Import stuff..
import numpy
import random


# Define functions...
def f(x):
    return (x**(-1./2))/(numpy.exp(x) + 1)

def pfunc():
    x = 1.0/(4*((random.uniform(0,1))**2))
    return x

def w(x):
    return x**(1./2)


N = 1000000
integral = 0.0

for i in range(N):
    xi = pfunc()
    #if i%100000==0:
    #    print xi
    integral += (f(xi)/w(xi))

integral = integral*(1./N)*(2./3)
print(integral)


# Results:
# Integral = 0.324222381913