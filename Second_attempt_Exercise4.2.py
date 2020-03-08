#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Created on 2020-01-24 by Asmita Gautam
Assignment 01: Python - Learning the Basics
Think Python Chapter 4: Exercises 4.2
Generate a set of functions that can draw a set of flowers as shown in fig 4.1
Modified to add header and comments for resubmission on 2020-03-04
"""

"""
Importing the required module 
turtle, which allows to create image using turtle graphics
math, which allows for doing mathematical operations
"""
import turtle #Importing math and turtle module
import math

"""
This function 'arc' takes three arguments: 
    t:function, which is a turtle function
    and other two paremeters:
        r: radius of the arc
        angle: angle to make the turn[degree]
"""
def arc(t,r,angle):      #Define the arc function as in example
    arc_length=2*math.pi*r*angle/360
    n=int(arc_length/3)+1
    step_length=arc_length/n
    step_angle=angle/n
    for i in range(n):               #assigning for loop for n
        t.fd(step_length)            #move Turtle forward as given length
        t.lt(step_angle)             #turn Turtle as given angle
                         
"""
This function 'petal' takes three arguments: 
    t:function, which is a turtle function
    and other two paremeters:
        r: radius of the arc
        angle: angle to make the turn [degree]
"""
def petal(t,r,angle):
    for i in range (2):  #Since each petal has 2 arc and angle needs to be turn.
        arc(t,r,angle)   #arc is from the above function
        t.lt(180-angle)  # To left turn Turtle at a given angle
        
"""
This function 'flower' takes four arguments: 
    t:function, which is a turtle function
    and other two paremeters:
        r: radius of the arc
        n: number of petals
        angle: angle to make the turn [degree]
"""
def flower(t,n,r,angle):  #Creat a function flower which has n n number of petals
    for i in range(n):    # For assigns the loop for i
        petal(t,r,angle)   # petal is the above defined function
        t.lt(360/n)        # To left turn Turtle
               
"""
This function move helps to move turtle in the given three flowers: 
   t:function, which is a turtle function
   length = length of movement
""" 
       
def move(t,length):
    t.pu()
    t.fd(length)
    t.pd()
    
bob=turtle.Turtle()
move(bob,-100)
flower(bob,7,60.0,60.0) #Flower with 7 petals and 60 degree angle

move(bob,100)
flower(bob,10,40,80) #Flower with 10 petals and 80 degree angle

move(bob,100)
flower(bob,20,140,20) #Flower with 20 petals and 20 degree angle

bob.hideturtle()
turtle.mainloop() #To display until any action be taken