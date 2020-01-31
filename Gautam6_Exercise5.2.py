#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 14:35:41 2020

@author: gautam6
"""

def check_fermet(a,b,c,n):    #Define a function check_ferment
    if 2<n and a**n+b**n==c**n: #** denotes ^, if the given 2 statement holds true than print
        print("Holy smokes,fermat was wrong")
    else:                                  #else than also print 
        print("No that doesnot work")
def corrected_check_fermet(a,b,c,n):  #Corrected_check_fermet if the rule will be violates if the values are int.
    a_int=int(a)
    b_int=int(b)
    c_int=int(c)
    n_int=int(n)
    check_fermet(a_int,b_int,c_int,n_int)
