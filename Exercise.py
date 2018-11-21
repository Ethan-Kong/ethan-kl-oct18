# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 10:13:16 2018

@author: ethan.kong
"""
guests = []
name = "n"

while name != "n" :
    name = input("What is your name? <Enter a space if no more>: ") 
    guests.append(name)
    
guests.sort()

for guest in guests :
    print(guest)
  