# -*- coding: utf-8 -*-
"""
Created on Thu Nov  8 11:28:50 2018

@author: ethan.kong
"""

class PuppyNewGen :
    name = []
    color = []
    def __init__(self) :
        self.name = []
        self.color = []
    
    def __setitem__(self, name, color) :
        self.name.append(name)
        self.color.append(color)
        
    def __getitem__(self, name) :
        if name in self.name :
            return self.color[self.name.index(name)]