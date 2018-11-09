# -*- coding: utf-8 -*-
"""
Created on Fri Nov  9 10:06:03 2018

@author: ethan.kong
"""

class Dogv2:
    species = 'mammal'
    name = ""
    age = ""
    
    def __init__(self,name,age):
        self.name = name
        self.age = age 
        
jake = Dogv2("Jake",7)
doug = Dogv2("Doug",8)     
will = Dogv2("William",10)    

def get_biggest_number(*args):  
    return  max(args) 

"""Method 1 to print out with using {}"""
print("The oldest dog {} yesrs old".format(get_biggest_number(jake.age,doug.age,will.age)))

"""Method 2 to print out with using concatenated"""
#print("The oldest dog "+str(get_biggest_number(jake.age,doug.age,will.age))+" yesrs old.")
    