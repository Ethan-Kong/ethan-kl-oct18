# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 10:42:12 2018

@author: ethan.kong
"""

import datetime;

birthday = input("What is your birthday? (mm/dd/yy)");

birthday = datetime.datetime.strptime(birthday, "%d/%m/%Y").date();

print("Your birth month is " + birthday.strftime('%B'));