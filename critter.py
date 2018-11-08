# -*- coding: utf-8 -*-
"""
Created on Thu Nov  8 10:56:59 2018

@author: ethan.kong
"""

class Critter :
    def __init__(self, msg) :        
        self.msg = msg
        
    def talk(self) :
      print(self.msg)  

critter1 = Critter("Hi!")
critter1.talk()