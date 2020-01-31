#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import turtle #Importing math and turtle module
import math
def arc(t,r,angle):      #Define the arc function as in example
    #t-turtle,r-radius of arc and angle-angle to turn
    arc_length=2*math.pi*r*angle/360
    n=int(arc_length/3)+1
    step_length=arc_length/n
    step_angle=angle/n
    for i in range(n):
        t.fd(step_length)
        t.lt(step_angle)   
def petal(t,r,angle):
    for i in range (2):  #Since each petal has 2 arc and angle needs to be turn.
        arc(t,r,angle)
        t.lt(180-angle)
def flower(t,n,r,angle):  #Creat a function flower which has n n number of petals
    for i in range(n):
        petal(t,r,angle)
        t.lt(360/n)
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