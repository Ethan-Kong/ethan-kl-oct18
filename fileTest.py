# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 11:35:58 2018

@author: ethan.kong
"""

fileName = "Sample.txt"
accessMode = "w"

myFile = open(fileName,accessMode)
myFile.write("Hi!!!")
myFile.write("How are your?")

