# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 11:01:44 2018

@author: ethan.kong
"""

#1. Create a function to print Hello
"""
def sayHello(name) :
    #print("Hello there!")
    print("Hello " + name + ", how are you?")
    return
"""

def sayHello(firstname, lastname) :
    #print("Hello there!")
    print("Hello " + firstname + " " + lastname + " , how are you?")
    return

#2. Involke the funtion
#sayHello("abc","123")
#sayHello("456","")

def addTwo(var1, var2) :
    sum = var1 + var2
    return sum

#print("Sum of 5 + 5 = " + str(addTwo(5,5)))
    
def printInfo(name, age) :
    print ("Name: ", name)
    print ("Age: ", age)
    return;

""" 2 way of calling of function """
printInfo("Elle",50)    
printInfo(age=50,name="Elle")
    