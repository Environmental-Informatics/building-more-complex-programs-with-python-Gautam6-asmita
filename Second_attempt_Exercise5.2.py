#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Created on 2020-01-24 by Asmita Gautam
Assignment 01: Python - Learning the Basics
Think Python Chapter 5: Exercises 5.2
##Check fermat equation

Modified for resubmission on 2020-03-04
"""
"""
This function 'check_fermat' takes 4 parameters: a,b,c and d
    to check the 'check fermat' equation given in exercise 5.2
"""

def check_fermat(a,b,c,n):    #Define a function check_fermat
    if 2<n and a**n+b**n==c**n: #** denotes ^, if the given 2 statement holds true than print
        print("Holy smokes,fermat was wrong")
    else:                                  #else than also print 
        print("No, that doesnot work")

"""
This function 'check_fermat_input' doesnot take any arguments
    It prints the input inquiry
"""        

def check_fermat_input():                      # to print input inquiry in the console
    a = int(input("Input 'a' value here: "))   # int(input...) is to convert the input to be integer instead of string
    b = int(input("Input 'b' value here: "))
    c = int(input("Input 'c' value here: "))
    n = int(input("Input 'n' value here: "))
    return check_fermat(a,b,c,n)

check_fermat_input()