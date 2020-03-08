#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Created on 2020-01-24 by Asmita Gautam
Assignment 01: Python - Learning the Basics
Think Python Chapter 6: Exercises 6.5

##Greatest common diviser(GCD) is the greatest number that divides both number with no reminder   

Modified for resubmission on 2020-03-04
"""

"""
This function 'gcd' takes 2 parameters: a and b
    to determine greatest common diviser
"""

def gcd(a,b):   # defines a function for greatest common diviser of any variable a and b
    if a > b:     #When a is greater than b,if b is zero gcd will be a
        if b == 0:
            print (a)
        else:              #Or else reminder of a/b will again run in a function 
            reminder= a%b         #So, the gcd will be the value when reminder is zero
            return gcd(b,reminder)
    else:                   #When b is equals to a or greater than a, repeat the step just exchanging the position
        if a == 0:
            print (b)
        else:
            reminder=b%a
            return gcd(a,reminder)

# Taking imput from user
a = input("Input 'a' value here: ")  
b = input("Input 'b' value here: ")

# Convert str to float
a = float(a)
b = float(b)

# Call function
gcd(a, b)