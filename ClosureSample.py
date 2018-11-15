# -*- coding: utf-8 -*-
"""
Created on Thu Nov 15 10:25:18 2018

@author: ethan.kong
"""

def make_inc(x):
    def inc(y):
        
        return x+y
    return inc

if __name__ == "__main__":
    inc5 = make_inc(5)
    inc10 = make_inc(10)
    
    print(inc5(5))
    print(inc10(5))
    