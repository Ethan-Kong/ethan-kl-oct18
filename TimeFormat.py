# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 11:08:02 2018

@author: ethan.kong
"""

import datetime;

currentTime = datetime.datetime.now();

print(currentTime);
print("Hour:");
print(currentTime.hour);
print("Minute:");
print(currentTime.minute);
print("Second:");
print(currentTime.second);
print("Time in Hour:Minute:");
print(datetime.datetime.strftime(currentTime, '%H:%M'));
print("Time in Hour:Minute with AM/PM");
print(datetime.datetime.strftime(currentTime, '%I:%M %p'));