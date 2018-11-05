# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 10:13:16 2018

@author: ethan.kong
"""
guests = []
name = " "

while name != " ":
    name = input("What is your name? <Enter a space if no more name>: ") 
    guests.append(name)
    
guests.sort()
for guest in guests :
    print(guest)
  