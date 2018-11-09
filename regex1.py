# -*- coding: utf-8 -*-
"""
Created on Fri Nov  9 10:53:56 2018

@author: ethan.kong
"""
import re

hand = open('data/mbox-short.txt')

for line in hand:
    line = line.rstrip()
    #if(line.find('From:'))>=0: 
    #if re.search('From:', line):
    #if re.search('^From:', line):
    #if re.search('^X.*:', line):
    #if re.search('^X-\S+', line):
    #if re.search('[0-9]+[A-Z]+',line):   
        #print(line)
    
#print(re.findall('[0-9]+:',line))
x='From: Using the : character'
print(re.findall('^F.+:',x)) #Greedy match
print(re.findall('^F.+?:',x)) #None Greedy match

    
        
        