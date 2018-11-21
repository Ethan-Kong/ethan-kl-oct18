# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 11:35:58 2018

@author: ethan.kong
"""
""" Sample creating Text file """
"""
fileName = "Sample.txt"
accessMode = "w"

myFile = open(fileName,accessMode)
myFile.write("Hi!!\n")
myFile.write("How are your?")
myFile.close()

"""

""" Sample calling CSV's file """

myFile = open("demo.csv", "r")
#fileContent = myFile.read()
"""read a line"""
fileContent = myFile.readline() 
print(fileContent)
