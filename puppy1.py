# -*- coding: utf-8 -*-
"""
Created on Thu Nov  8 10:29:12 2018

@author: ethan.kong
"""

class Puppy :
    name = ""
    color= ""
    
    def __init__(self, name, color) :        
        self.name = name
        self.color = color
        
    def bark(self) :
        print("I am", self.color, self.name)
        
puppy1 = Puppy("Max","brown")
puppy1.bark()

puppy2 = Puppy("Ruby","red")
puppy2.bark()