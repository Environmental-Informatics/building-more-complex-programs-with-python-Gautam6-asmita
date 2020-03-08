#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Created on 2020-01-24 by Asmita Gautam
Assignment 01: Python - Learning the Basics
Think Python Chapter 7: Exercises 7.1

##To make the table as given in 7.1   

Modified for resubmission on 2020-03-04
"""

"""
Importing the required module math, which allows for doing mathematical operations
"""
import math

"""
This function 'mysqrt' takes a parameter a
    to determine squareroot of the variable a
"""

def mysqrt (a):       #Defines a function mysqrt which takes a variable a
    x=2
    a=int(a)
    while True:    #while function runs the iteration untile the statement is true
        y=(x+a/x)/2
        if y==x:
            break
        x=y
    return y   

"""
This function 'diff' takes a parameter a
    to i.e difference of math.sqrt and my.sqrt for each value of a 
"""
 
def diff(a):             #Define the function diff, 
    d=math.sqrt(a)- mysqrt(a)
    return d

"""
This function 'test_square_root' doesnot takes any argument
  to print the test_square_root as sample table in Exercise 7.1
"""

def test_square_root():       #Defines a function test_square_root
    header=['a','mysqrt(a)','math.sqrt(a)','diff']  #For header of table
    print('{:<6s} {:<20s} {:<20s} {:<20s}'.format(header[0],header[1],header[2],header[3])) #Print the header
    print('{:<6s} {:<20s} {:<20s} {:<20s}'.format('-','------','--------','------'))  # Print the -- lines making as string
    for a in range(1,10):
        lst=[a,mysqrt(a),math.sqrt(a),diff(a)]   #[ ] includes the list of variables and functions
        print('{:.1f}   {:<20.11f} {:<20.11f} {:<20.11f}'.format(lst[0],lst[1],lst[2],lst[3]))


test_square_root()            #Displays the table created
