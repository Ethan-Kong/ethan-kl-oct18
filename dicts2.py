# -*- coding: utf-8 -*-
"""
Created on Wed Nov  7 11:26:59 2018

@author: ethan.kong
"""

counts = dict()
names = ['a','b','c','d','e']

for name in names :
    if name not in counts:
        counts[name] = 1
    else :
        counts[name] = counts[name]+1
        
print(counts)

counts = dict()
for name in names :
    counts[name] = counts.get(name,0) + 1
print(counts)

print(counts.get('b',0))
print(counts.get('abc',0))        