# -*- coding: utf-8 -*-
"""
Created on Wed Nov  7 10:15:53 2018

@author: ethan.kong
"""

import csv

myCSVfile = open('data/demo.csv','r')
dataFromFile = csv.reader(myCSVfile)

print(dataFromFile)

for row in dataFromFile:
    print(row)
    
myCSVfile.close()

fileName = "GuestList.txt"
accessMode = "r"

with open(fileName, accessMode) as myCSVFile:
    dataFromFIle = csv.reader(myCSVFile)
    
    for row in dataFromFile:
        print(row)
    