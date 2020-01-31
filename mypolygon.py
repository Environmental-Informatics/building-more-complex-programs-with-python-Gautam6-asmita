#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 14:35:41 2020

@author: gautam6
"""

def check_fermet(a,b,c,n):
    if 2<n and a**n+b**n==c**n:
        print("Holy smokes,fermat was wrong")
    else:
        print("No that doesnot work")
def corrected_check_fermet(a,b,c,n):
    a_int=int(a)
    b_int=int(b)
    c_int=int(c)
    n_int=int(n)
    check_fermet(a_int,b_int,c_int,n_int)
