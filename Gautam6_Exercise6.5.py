#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 15:36:21 2020

@author: gautam6
"""

def gcd(a,b):   # defines a function for greatest common diviser of any variable a and b
    if a>b:     #When a is greater than b,if b is zero gcd will be a
        if b==0:
            return a
        else:              #Or else reminder of a/b will again run in a function 
            reminder=a%b         #So, the gcd will be the value when reminder is zero
            return gcd(b,reminder)
    else:                   #When b is equals to a or greater than a, repeat the step just exchanging the position
        if a==0:
            return b
        else:
            reminder=b%a
            return gcd(a,reminder)