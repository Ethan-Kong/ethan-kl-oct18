# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 10:36:31 2018

@author: ethan.kong
"""
"""
def add_item(item, item_list = []):
    item_list.append(item)
    print (item_list)
"""

def add_item(item, item_list = None):
    if item_list == None :
        item_list = []
        
    item_list.append(item)
    print (item_list)    
    
def printIt(**kwargs):
    print(kwargs)    
    
def printDict(**kwargs):
    print(kwargs)      
    
def printTuple(*args):
    print(args)      